from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest

from osc_sdk_python.credentials import Profile
from osc_sdk_python.runtime.transport import (
    AsyncSdkTransport,
    RetryPolicy,
    SdkAuth,
    SdkTransport,
)


class FixedDateSdkAuth(SdkAuth):
    def build_dates(self):
        return "20260102T030405Z", "20260102"


class SequenceTransport:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def handle_request(self, request):
        self.requests.append(request)
        if isinstance(self.responses[0], Exception):
            raise self.responses.pop(0)
        return self.responses.pop(0)

    def close(self):
        pass


class AsyncSequenceTransport:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    async def handle_async_request(self, request):
        self.requests.append(request)
        if isinstance(self.responses[0], Exception):
            raise self.responses.pop(0)
        return self.responses.pop(0)

    async def aclose(self):
        pass


def response(status_code, request, headers=None):
    return httpx.Response(
        status_code,
        json={},
        headers={"content-type": "application/json", **(headers or {})},
        request=request,
    )


def text_response(status_code, request=None, text="", headers=None):
    return httpx.Response(
        status_code,
        text=text,
        headers={"content-type": "text/plain", **(headers or {})},
        request=request,
    )


def test_sdk_auth_adds_signed_headers():
    auth = FixedDateSdkAuth(
        Profile(access_key="ak", secret_key="sk", region="eu-west-2"),
        service="api",
    )
    request = httpx.Request(
        "POST",
        "https://api.eu-west-2.outscale.com/ReadVms",
        content="{}",
    )

    signed = next(auth.auth_flow(request))

    assert signed.headers["X-Osc-Date"] == "20260102T030405Z"
    assert signed.headers["Authorization"].startswith("OSC4-HMAC-SHA256 ")
    assert (
        "Credential=ak/20260102/eu-west-2/api/osc4_request"
        in signed.headers["Authorization"]
    )


def test_sdk_auth_adds_basic_auth_headers():
    auth = FixedDateSdkAuth(
        Profile(login="user@example.com", password="secret", region="eu-west-2"),
        service="api",
    )
    request = httpx.Request(
        "POST",
        "https://api.eu-west-2.outscale.com/ReadVms",
        content="{}",
    )

    signed = next(auth.auth_flow(request))

    assert signed.headers["X-Osc-Date"] == "20260102T030405Z"
    assert signed.headers["Authorization"].startswith("Basic ")


def test_sdk_auth_adds_oks_headers():
    auth = FixedDateSdkAuth(
        Profile(access_key="ak", secret_key="sk", region="eu-west-2"),
        service="oks",
    )
    request = httpx.Request(
        "GET",
        "https://api.eu-west-2.oks.outscale.com/projects",
    )

    signed = next(auth.auth_flow(request))

    assert signed.headers["AccessKey"] == "ak"
    assert signed.headers["SecretKey"] == "sk"


def test_transport_retries_429_with_retry_after():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    transport = SdkTransport(retry_policy=RetryPolicy(max_retries=1))
    transport._transport = SequenceTransport(
        [
            response(429, request, {"Retry-After": "0"}),
            response(200, request),
        ]
    )

    with patch("time.sleep") as sleep:
        result = transport.handle_request(request)

    assert result.status_code == 200
    assert len(transport._transport.requests) == 2
    sleep.assert_called_once_with(0.0)


def test_transport_retries_non_json_500():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    transport = SdkTransport(retry_policy=RetryPolicy(max_retries=1))
    transport._transport = SequenceTransport(
        [
            text_response(500, request, "upstream failure"),
            response(200, request),
        ]
    )

    with patch("time.sleep"):
        result = transport.handle_request(request)

    assert result.status_code == 200
    assert len(transport._transport.requests) == 2


def test_transport_retries_connection_error_until_max_retries():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    transport = SdkTransport(retry_policy=RetryPolicy(max_retries=2))
    transport._transport = SequenceTransport(
        [
            httpx.ConnectError("connection failed", request=request),
            httpx.ConnectError("connection failed", request=request),
            httpx.ConnectError("connection failed", request=request),
        ]
    )

    with patch("time.sleep") as sleep:
        with pytest.raises(httpx.ConnectError):
            transport.handle_request(request)

    assert len(transport._transport.requests) == 3
    assert sleep.call_count == 2


def test_transport_retries_timeout_until_max_retries():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    transport = SdkTransport(retry_policy=RetryPolicy(max_retries=2))
    transport._transport = SequenceTransport(
        [
            httpx.TimeoutException("timed out", request=request),
            httpx.TimeoutException("timed out", request=request),
            httpx.TimeoutException("timed out", request=request),
        ]
    )

    with patch("time.sleep") as sleep:
        with pytest.raises(httpx.TimeoutException):
            transport.handle_request(request)

    assert len(transport._transport.requests) == 3
    assert sleep.call_count == 2


def test_transport_uses_backoff_when_retry_after_missing():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    transport = SdkTransport(
        retry_policy=RetryPolicy(
            max_retries=1,
            backoff_factor=2.0,
            backoff_jitter=3.0,
        )
    )
    transport._transport = SequenceTransport(
        [
            text_response(500, request, "upstream failure"),
            response(200, request),
        ]
    )

    with patch("random.uniform", return_value=1.5) as random_uniform:
        with patch("time.sleep") as sleep:
            result = transport.handle_request(request)

    assert result.status_code == 200
    random_uniform.assert_called_once_with(0, 3.0)
    sleep.assert_called_once_with(3.5)


def test_retry_after_http_date_overrides_backoff():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    retry_after = "Fri, 02 Jan 2026 03:04:06 GMT"
    policy = RetryPolicy(max_retries=1)

    error = httpx.HTTPStatusError(
        "too many requests",
        request=request,
        response=response(429, request, {"Retry-After": retry_after}),
    )

    class FixedDateTime:
        @classmethod
        def now(cls, tz=None):
            import datetime

            return datetime.datetime(2026, 1, 2, 3, 4, 5, tzinfo=tz)

    with patch("osc_sdk_python.runtime.transport.datetime", FixedDateTime):
        assert policy.retry_after_time(error) == 1.0


def test_retry_policy_does_not_retry_redirect_or_invalid_request_errors():
    policy = RetryPolicy(max_retries=3)
    request = httpx.Request("POST", "https://example.test/ReadVms")

    assert not policy.should_retry(
        httpx.TooManyRedirects("too many redirects", request=request),
        attempt=0,
    )
    assert not policy.should_retry(httpx.InvalidURL("bad url"), attempt=0)
    assert not policy.should_retry(
        httpx.UnsupportedProtocol("bad protocol", request=request),
        attempt=0,
    )


def test_transport_error_uses_original_request_when_response_has_none():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    transport = SdkTransport(retry_policy=RetryPolicy(max_retries=0))
    transport._transport = SequenceTransport(
        [text_response(500, text="upstream failure")]
    )

    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        transport.handle_request(request)

    assert exc_info.value.request is request
    assert "https://example.test/ReadVms" in str(exc_info.value)


def test_transport_does_not_retry_400():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    transport = SdkTransport(retry_policy=RetryPolicy(max_retries=3))
    transport._transport = SequenceTransport([response(400, request)])

    with pytest.raises(httpx.HTTPStatusError):
        transport.handle_request(request)

    assert len(transport._transport.requests) == 1


def test_async_transport_uses_async_limiter():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        limiter = Mock()
        limiter.async_acquire = AsyncMock()
        transport = AsyncSdkTransport(
            limiter=limiter,
            retry_policy=RetryPolicy(max_retries=0),
        )
        transport._transport = AsyncSequenceTransport([response(200, request)])

        result = await transport.handle_async_request(request)

        assert result.status_code == 200
        limiter.async_acquire.assert_called_once()

    import asyncio

    asyncio.run(run())


def test_async_transport_retries_non_json_500():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=1))
        transport._transport = AsyncSequenceTransport(
            [
                text_response(500, request, "upstream failure"),
                response(200, request),
            ]
        )

        with patch("asyncio.sleep", new_callable=AsyncMock):
            result = await transport.handle_async_request(request)

        assert result.status_code == 200
        assert len(transport._transport.requests) == 2

    import asyncio

    asyncio.run(run())


def test_async_transport_retries_connection_error_until_max_retries():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=2))
        transport._transport = AsyncSequenceTransport(
            [
                httpx.ConnectError("connection failed", request=request),
                httpx.ConnectError("connection failed", request=request),
                httpx.ConnectError("connection failed", request=request),
            ]
        )

        with patch("asyncio.sleep", new_callable=AsyncMock) as sleep:
            with pytest.raises(httpx.ConnectError):
                await transport.handle_async_request(request)

        assert len(transport._transport.requests) == 3
        assert sleep.call_count == 2

    import asyncio

    asyncio.run(run())


def test_async_transport_retries_timeout_until_max_retries():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=2))
        transport._transport = AsyncSequenceTransport(
            [
                httpx.TimeoutException("timed out", request=request),
                httpx.TimeoutException("timed out", request=request),
                httpx.TimeoutException("timed out", request=request),
            ]
        )

        with patch("asyncio.sleep", new_callable=AsyncMock) as sleep:
            with pytest.raises(httpx.TimeoutException):
                await transport.handle_async_request(request)

        assert len(transport._transport.requests) == 3
        assert sleep.call_count == 2

    import asyncio

    asyncio.run(run())
