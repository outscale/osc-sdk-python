import asyncio
from unittest.mock import Mock, patch

import httpx
import pytest

from osc_sdk_python.runtime.async_.retry import AsyncRetry


class RecordingAsyncClient:
    def __init__(self, responses=None, exception=None):
        self.calls = []
        self.responses = list(responses or [])
        self.exception = exception

    async def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        if self.exception is not None:
            raise self.exception
        return self.responses.pop(0)


class TestAsyncRetry:
    def setup_method(self):
        self.method = "POST"
        self.url = "https://api.test-region.outscale.com/"
        self.base_kwargs = {"timeout": 30}

    def build_response(self, status_code, reason="OK", content_type="application/json"):
        return httpx.Response(
            status_code,
            headers={"content-type": content_type},
            json={"Errors": []},
            request=httpx.Request(self.method, self.url),
            extensions={"reason_phrase": reason.encode()},
        )

    def build_response_success(self):
        return self.build_response(200)

    def test_execute_once_success(self):
        async def run():
            response = self.build_response_success()
            client = RecordingAsyncClient([response])

            retry = AsyncRetry(client, self.method, self.url, **self.base_kwargs)
            result = await retry.execute_once()

            assert result is response
            assert client.calls == [(self.method, self.url, self.base_kwargs)]

        asyncio.run(run())

    def test_should_retry_with_4xx_error(self):
        retry = AsyncRetry(Mock(), self.method, self.url, **self.base_kwargs)
        exception = httpx.HTTPStatusError(
            "bad request",
            request=httpx.Request(self.method, self.url),
            response=self.build_response(400),
        )

        assert not retry.should_retry(exception)

    def test_should_retry_with_429_error(self):
        retry = AsyncRetry(Mock(), self.method, self.url, **self.base_kwargs)
        exception = httpx.HTTPStatusError(
            "too many requests",
            request=httpx.Request(self.method, self.url),
            response=self.build_response(429),
        )

        assert retry.should_retry(exception)

    def test_should_retry_with_5xx_error_under_limit(self):
        retry = AsyncRetry(Mock(), self.method, self.url, **self.base_kwargs)
        exception = httpx.HTTPStatusError(
            "server error",
            request=httpx.Request(self.method, self.url),
            response=self.build_response(500),
        )

        assert retry.should_retry(exception)

    def test_should_retry_with_no_response(self):
        retry = AsyncRetry(Mock(), self.method, self.url, **self.base_kwargs)
        exception = httpx.ConnectError(
            "connection failed",
            request=httpx.Request(self.method, self.url),
        )

        assert retry.should_retry(exception)

    def test_should_retry_at_max_retries(self):
        retry = AsyncRetry(
            Mock(),
            self.method,
            self.url,
            attempt=3,
            **self.base_kwargs,
        )
        exception = httpx.ConnectError(
            "connection failed",
            request=httpx.Request(self.method, self.url),
        )

        assert not retry.should_retry(exception)

    def test_should_not_retry_too_many_redirects(self):
        retry = AsyncRetry(Mock(), self.method, self.url, **self.base_kwargs)
        exception = httpx.TooManyRedirects(
            "too many redirects",
            request=httpx.Request(self.method, self.url),
        )

        assert not retry.should_retry(exception)

    @patch("random.uniform")
    def test_get_backoff_time(self, mock_random):
        mock_random.return_value = 1.5
        retry = AsyncRetry(
            Mock(),
            self.method,
            self.url,
            attempt=2,
            **self.base_kwargs,
        )

        assert retry.get_backoff_time() == 5.5

    @patch("random.uniform")
    def test_get_backoff_time_with_max(self, mock_random):
        mock_random.return_value = 5.0
        retry = AsyncRetry(
            Mock(),
            self.method,
            self.url,
            attempt=10,
            backoff_factor=2.0,
            backoff_max=10.0,
            **self.base_kwargs,
        )

        assert retry.get_backoff_time() == 10.0

    def test_execute_success_no_retry(self):
        async def run():
            response = self.build_response_success()
            client = RecordingAsyncClient([response])
            retry = AsyncRetry(client, self.method, self.url, **self.base_kwargs)

            result = await retry.execute()

            assert result is response
            assert len(client.calls) == 1

        asyncio.run(run())

    @patch("asyncio.sleep")
    @patch("random.uniform")
    def test_execute_with_retry_success(self, mock_random, mock_sleep):
        async def run():
            mock_random.return_value = 1.0
            mock_sleep.return_value = None
            client = RecordingAsyncClient(
                [
                    self.build_response(500, "Internal Server Error"),
                    self.build_response_success(),
                ]
            )
            retry = AsyncRetry(client, self.method, self.url, **self.base_kwargs)

            result = await retry.execute()

            assert result.status_code == 200
            assert len(client.calls) == 2
            mock_sleep.assert_called_once()

        asyncio.run(run())

    def test_execute_with_4xx_error_no_retry(self):
        async def run():
            client = RecordingAsyncClient([self.build_response(400, "Bad Request")])
            retry = AsyncRetry(client, self.method, self.url, **self.base_kwargs)

            with pytest.raises(httpx.HTTPStatusError):
                await retry.execute()

            assert len(client.calls) == 1

        asyncio.run(run())

    @patch("asyncio.sleep")
    @patch("random.uniform")
    def test_execute_with_429_error_retry(self, mock_random, mock_sleep):
        async def run():
            mock_random.return_value = 1.0
            mock_sleep.return_value = None
            client = RecordingAsyncClient(
                [self.build_response(429, "Too Many Requests") for _ in range(3)]
            )
            retry = AsyncRetry(
                client,
                self.method,
                self.url,
                max_retries=2,
                **self.base_kwargs,
            )

            with pytest.raises(httpx.HTTPStatusError):
                await retry.execute()

            assert len(client.calls) == 3
            assert mock_sleep.call_count == 2

        asyncio.run(run())

    @patch("asyncio.sleep")
    @patch("random.uniform")
    def test_execute_with_500_error_retry_wrong_content_type(
        self, mock_random, mock_sleep
    ):
        async def run():
            mock_random.return_value = 1.0
            mock_sleep.return_value = None
            client = RecordingAsyncClient(
                [
                    self.build_response(
                        500,
                        "Internal Server Error",
                        content_type="text/plain",
                    )
                    for _ in range(3)
                ]
            )
            retry = AsyncRetry(
                client,
                self.method,
                self.url,
                max_retries=2,
                **self.base_kwargs,
            )

            with pytest.raises(httpx.HTTPStatusError):
                await retry.execute()

            assert len(client.calls) == 3
            assert mock_sleep.call_count == 2

        asyncio.run(run())

    @patch("asyncio.sleep")
    @patch("random.uniform")
    def test_execute_max_retries_exceeded(self, mock_random, mock_sleep):
        async def run():
            mock_random.return_value = 1.0
            mock_sleep.return_value = None
            exception = httpx.ConnectError(
                "connection failed",
                request=httpx.Request(self.method, self.url),
            )
            client = RecordingAsyncClient(exception=exception)
            retry = AsyncRetry(
                client,
                self.method,
                self.url,
                max_retries=2,
                **self.base_kwargs,
            )

            with pytest.raises(httpx.ConnectError):
                await retry.execute()

            assert len(client.calls) == 3
            assert mock_sleep.call_count == 2

        asyncio.run(run())
