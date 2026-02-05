import pytest
import requests
from unittest.mock import Mock, patch
from requests.exceptions import RequestException, HTTPError, ConnectionError

from osc_sdk_python.retry import Retry


class TestRetry:
    """Test cases for the Retry class"""

    def setup_method(self):
        """Set up test fixtures"""
        self.mock_session = Mock(spec=requests.Session)
        self.method = "POST"
        self.url = "https://api.test-region.outscalce.com/"
        self.base_kwargs = {"timeout": 30}

    def build_response(self, status_code, reason):
        mock_response = Mock(spec=requests.Response)
        mock_response.status_code = status_code
        mock_response.reason = reason
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = self.url
        return mock_response

    def build_response_success(self):
        return self.build_response(200, "OK")

    def test_execute_once_success(self):
        """Test execute_once method with successful request"""
        mock_response = Mock(spec=requests.Response)
        self.mock_session.request.return_value = mock_response

        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)
        result = retry.execute_once()

        assert result == mock_response
        self.mock_session.request.assert_called_once_with(
            self.method, self.url, **self.base_kwargs
        )

    def test_should_retry_with_4xx_error(self):
        """Test should_retry returns False for 4xx client errors"""
        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        mock_response = Mock()
        mock_response.status_code = 400
        exception = RequestException()
        exception.response = mock_response

        assert not retry.should_retry(exception)

    def test_should_retry_with_429_error(self):
        """Test should_retry returns True for 429 client errors"""
        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        mock_response = Mock()
        mock_response.status_code = 429
        exception = RequestException()
        exception.response = mock_response

        assert retry.should_retry(exception)

    def test_should_retry_with_5xx_error_under_limit(self):
        """Test should_retry returns True for 5xx server errors under retry limit"""
        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        mock_response = Mock()
        mock_response.status_code = 500
        exception = RequestException()
        exception.response = mock_response

        assert retry.should_retry(exception)

    def test_should_retry_with_no_response(self):
        """Test should_retry returns True for exceptions without response"""
        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        exception = ConnectionError()
        exception.response = None

        assert retry.should_retry(exception)

    def test_should_retry_at_max_retries(self):
        """Test should_retry returns False when at max retries"""
        retry = Retry(
            self.mock_session, self.method, self.url, attempt=3, **self.base_kwargs
        )

        exception = ConnectionError()
        exception.response = None

        assert not retry.should_retry(exception)

    @patch("random.uniform")
    def test_get_backoff_time(self, mock_random):
        """Test get_backoff_time calculation"""
        mock_random.return_value = 1.5

        retry = Retry(
            self.mock_session, self.method, self.url, attempt=2, **self.base_kwargs
        )

        expected_backoff = 1.0 * (2**2) + 1.5  # backoff_factor * (2^attempt) + jitter
        assert retry.get_backoff_time() == expected_backoff

    @patch("random.uniform")
    def test_get_backoff_time_with_max(self, mock_random):
        """Test get_backoff_time respects backoff_max"""
        mock_random.return_value = 5.0

        retry = Retry(
            self.mock_session,
            self.method,
            self.url,
            attempt=10,
            backoff_factor=2.0,
            backoff_max=10.0,
            **self.base_kwargs,
        )

        assert retry.get_backoff_time() == 10.0

    def test_execute_success_no_retry(self):
        """Test execute method with successful request"""
        mock_response = self.build_response_success()
        self.mock_session.request.return_value = mock_response

        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)
        result = retry.execute()

        assert result == mock_response
        self.mock_session.request.assert_called_once()

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_with_retry_success(self, mock_random, mock_sleep):
        """Test execute method with retry leading to success"""
        mock_random.return_value = 1.0

        # First call fails, second succeeds
        mock_response_fail = self.build_response(500, "Internal Server Error")

        # Configure the successful response
        mock_response_success = self.build_response_success()

        self.mock_session.request.side_effect = [
            mock_response_fail,
            mock_response_success,
        ]

        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)
        result = retry.execute()

        assert result == mock_response_success
        assert self.mock_session.request.call_count == 2
        mock_sleep.assert_called_once()

    def test_execute_with_4xx_error_no_retry(self):
        """Test execute method doesn't retry on 4xx errors"""
        mock_response = self.build_response(400, "Bad Request")

        self.mock_session.request.return_value = mock_response

        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        with pytest.raises(HTTPError):
            retry.execute()

        self.mock_session.request.assert_called_once()

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_with_429_error_retry(self, mock_random, mock_sleep):
        """Test execute method retry on 429 errors"""
        mock_random.return_value = 1.0

        mock_response = self.build_response(429, "Too Many Requests")
        self.mock_session.request.return_value = mock_response

        retry = Retry(
            self.mock_session, self.method, self.url, max_retries=2, **self.base_kwargs
        )

        with pytest.raises(HTTPError):
            retry.execute()

        # Should try 2 times (initial + 2 retries)
        assert self.mock_session.request.call_count == 3
        assert mock_sleep.call_count == 2

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_with_500_error_retry_wrong_content_type(
        self, mock_random, mock_sleep
    ):
        """Test execute method retry on 500 errors"""
        mock_random.return_value = 1.0

        mock_response = self.build_response(500, "Internal Server Error")
        mock_response.headers["content-type"] = "text/plain"
        self.mock_session.request.return_value = mock_response

        retry = Retry(
            self.mock_session, self.method, self.url, max_retries=2, **self.base_kwargs
        )

        with pytest.raises(HTTPError):
            retry.execute()

        # Should try 2 times (initial + 2 retries)
        assert self.mock_session.request.call_count == 3
        assert mock_sleep.call_count == 2

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_max_retries_exceeded(self, mock_random, mock_sleep):
        """Test execute method when max retries are exceeded"""
        mock_random.return_value = 1.0

        exception = ConnectionError()
        exception.response = None
        self.mock_session.request.side_effect = exception

        retry = Retry(
            self.mock_session, self.method, self.url, max_retries=2, **self.base_kwargs
        )

        with pytest.raises(ConnectionError):
            retry.execute()

        # Should try 3 times (initial + 2 retries)
        assert self.mock_session.request.call_count == 3
        assert mock_sleep.call_count == 2
