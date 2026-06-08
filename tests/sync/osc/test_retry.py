from unittest.mock import Mock, patch

import httpx
import pytest

from osc_sdk_python.runtime.sync.retry import Retry


class TestRetry:
    """Test cases for the Retry class"""

    def setup_method(self):
        """Set up test fixtures"""
        self.mock_session = Mock(spec=httpx.Client)
        self.method = "POST"
        self.url = "https://api.test-region.outscalce.com/"
        self.base_kwargs = {"timeout": 30}

    def build_response(self, status_code, reason):
        return httpx.Response(
            status_code,
            json={},
            headers={"content-type": "application/json"},
            request=httpx.Request(self.method, self.url),
            extensions={"reason_phrase": reason.encode()},
        )

    def build_response_success(self):
        return self.build_response(200, "OK")

    def test_execute_once_success(self):
        """Test execute_once method with successful request"""
        mock_response = Mock(spec=httpx.Response)
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
        exception = httpx.HTTPStatusError(
            "bad request",
            request=Mock(),
            response=mock_response,
        )

        assert not retry.should_retry(exception)

    def test_should_retry_with_429_error(self):
        """Test should_retry returns True for 429 client errors"""
        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        mock_response = Mock()
        mock_response.status_code = 429
        exception = httpx.HTTPStatusError(
            "too many requests",
            request=Mock(),
            response=mock_response,
        )

        assert retry.should_retry(exception)

    def test_should_retry_with_5xx_error_under_limit(self):
        """Test should_retry returns True for 5xx server errors under retry limit"""
        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        mock_response = Mock()
        mock_response.status_code = 500
        exception = httpx.HTTPStatusError(
            "server error",
            request=Mock(),
            response=mock_response,
        )

        assert retry.should_retry(exception)

    def test_should_retry_with_no_response(self):
        """Test should_retry returns True for exceptions without response"""
        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        assert retry.should_retry(httpx.ConnectError("connection failed"))

    def test_should_retry_at_max_retries(self):
        """Test should_retry returns False when at max retries"""
        retry = Retry(
            self.mock_session, self.method, self.url, attempt=3, **self.base_kwargs
        )

        assert not retry.should_retry(httpx.ConnectError("connection failed"))

    @patch("random.uniform")
    def test_get_backoff_time(self, mock_random):
        """Test get_backoff_time calculation"""
        mock_random.return_value = 1.5

        retry = Retry(
            self.mock_session, self.method, self.url, attempt=2, **self.base_kwargs
        )

        expected_backoff = 1.0 * (2**2) + 1.5
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
        mock_response_fail = self.build_response(500, "Internal Server Error")
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
        self.mock_session.request.return_value = self.build_response(400, "Bad Request")

        retry = Retry(self.mock_session, self.method, self.url, **self.base_kwargs)

        with pytest.raises(httpx.HTTPStatusError):
            retry.execute()

        self.mock_session.request.assert_called_once()

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_with_429_error_retry(self, mock_random, mock_sleep):
        """Test execute method retry on 429 errors"""
        mock_random.return_value = 1.0
        self.mock_session.request.return_value = self.build_response(
            429, "Too Many Requests"
        )

        retry = Retry(
            self.mock_session, self.method, self.url, max_retries=2, **self.base_kwargs
        )

        with pytest.raises(httpx.HTTPStatusError):
            retry.execute()

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

        with pytest.raises(httpx.HTTPStatusError):
            retry.execute()

        assert self.mock_session.request.call_count == 3
        assert mock_sleep.call_count == 2

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_max_retries_exceeded(self, mock_random, mock_sleep):
        """Test execute method when max retries are exceeded"""
        mock_random.return_value = 1.0
        self.mock_session.request.side_effect = httpx.ConnectError("connection failed")

        retry = Retry(
            self.mock_session, self.method, self.url, max_retries=2, **self.base_kwargs
        )

        with pytest.raises(httpx.ConnectError):
            retry.execute()

        assert self.mock_session.request.call_count == 3
        assert mock_sleep.call_count == 2

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_with_timeout_retry(self, mock_random, mock_sleep):
        """Test execute method retries timeout errors"""
        mock_random.return_value = 1.0
        self.mock_session.request.side_effect = httpx.TimeoutException("timed out")

        retry = Retry(
            self.mock_session, self.method, self.url, max_retries=2, **self.base_kwargs
        )

        with pytest.raises(httpx.TimeoutException):
            retry.execute()

        assert self.mock_session.request.call_count == 3
        assert mock_sleep.call_count == 2

    @patch("time.sleep")
    @patch("random.uniform")
    def test_execute_uses_retry_after_header(self, mock_random, mock_sleep):
        """Test Retry-After header overrides calculated backoff"""
        mock_random.return_value = 1.0
        mock_response = self.build_response(429, "Too Many Requests")
        mock_response.headers["Retry-After"] = "7"
        self.mock_session.request.return_value = mock_response

        retry = Retry(
            self.mock_session, self.method, self.url, max_retries=1, **self.base_kwargs
        )

        with pytest.raises(httpx.HTTPStatusError):
            retry.execute()

        assert self.mock_session.request.call_count == 2
        mock_sleep.assert_called_once_with(7.0)
