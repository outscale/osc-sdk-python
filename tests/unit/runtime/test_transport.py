from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest

from osc_sdk_python.credentials import Profile
from osc_sdk_python.exceptions import (
    SdkClientError,
    SdkConfigurationError,
    SdkServerError,
    SdkTransportError,
    extract_request_id,
)
from osc_sdk_python.runtime.transport import (
    AsyncSdkTransport,
    RetryPolicy,
    SdkAuth,
)


class FixedDateSdkAuth(SdkAuth):
    def build_dates(self):
        return "20260102T030405Z", "20260102"


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


def test_sdk_auth_requires_signed_credentials():
    auth = FixedDateSdkAuth(Profile(region="eu-west-2"), service="api")
    request = httpx.Request(
        "POST",
        "https://api.eu-west-2.outscale.com/ReadVms",
        content="{}",
    )

    with pytest.raises(SdkConfigurationError):
        next(auth.auth_flow(request))


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


def test_sdk_auth_requires_oks_credentials():
    auth = FixedDateSdkAuth(Profile(region="eu-west-2"), service="oks")
    request = httpx.Request(
        "GET",
        "https://api.eu-west-2.oks.outscale.com/projects",
    )

    with pytest.raises(SdkConfigurationError):
        next(auth.auth_flow(request))


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


def test_async_transport_retries_429_with_retry_after():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=1))
        transport._transport = AsyncSequenceTransport(
            [
                response(429, request, {"Retry-After": "0"}),
                response(200, request),
            ]
        )

        with patch("asyncio.sleep", new_callable=AsyncMock) as sleep:
            result = await transport.handle_async_request(request)

        assert result.status_code == 200
        assert len(transport._transport.requests) == 2
        sleep.assert_called_once_with(0.0)

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


def test_async_transport_retries_connection_error_without_response():
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
            with pytest.raises(SdkTransportError) as exc_info:
                await transport.handle_async_request(request)

        assert len(transport._transport.requests) == 3
        assert sleep.call_count == 2
        assert isinstance(exc_info.value.__cause__, httpx.ConnectError)

    import asyncio

    asyncio.run(run())


def test_async_transport_wraps_httpx_error_without_request():
    async def run():
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=0))
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport._transport = AsyncSequenceTransport([httpx.ReadTimeout("timed out")])

        with pytest.raises(SdkTransportError) as exc_info:
            await transport.handle_async_request(request)

        assert exc_info.value.request is None
        assert exc_info.value.response is None
        assert isinstance(exc_info.value.__cause__, httpx.ReadTimeout)

    import asyncio

    asyncio.run(run())


def test_async_transport_does_not_retry_timeout_without_response():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=2))
        transport._transport = AsyncSequenceTransport(
            [httpx.TimeoutException("timed out", request=request)]
        )

        with patch("asyncio.sleep", new_callable=AsyncMock) as sleep:
            with pytest.raises(SdkTransportError) as exc_info:
                await transport.handle_async_request(request)

        assert len(transport._transport.requests) == 1
        sleep.assert_not_called()
        assert isinstance(exc_info.value.__cause__, httpx.TimeoutException)

    import asyncio

    asyncio.run(run())


def test_async_transport_uses_backoff_when_retry_after_missing():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(
            retry_policy=RetryPolicy(
                max_retries=1,
                backoff_factor=2.0,
                backoff_jitter=3.0,
            )
        )
        transport._transport = AsyncSequenceTransport(
            [
                text_response(500, request, "upstream failure"),
                response(200, request),
            ]
        )

        with patch("random.uniform", return_value=1.5):
            with patch("asyncio.sleep", new_callable=AsyncMock) as sleep:
                result = await transport.handle_async_request(request)

        assert result.status_code == 200
        sleep.assert_called_once_with(3.5)

    import asyncio

    asyncio.run(run())


def test_async_transport_error_uses_original_request_when_response_has_none():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=0))
        transport._transport = AsyncSequenceTransport(
            [text_response(500, text="upstream failure")]
        )

        with pytest.raises(SdkServerError) as exc_info:
            await transport.handle_async_request(request)

        assert exc_info.value.request is request
        assert "https://example.test/ReadVms" in str(exc_info.value)

    import asyncio

    asyncio.run(run())


def test_async_transport_does_not_retry_400():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=3))
        transport._transport = AsyncSequenceTransport([response(400, request)])

        with pytest.raises(SdkClientError):
            await transport.handle_async_request(request)

        assert len(transport._transport.requests) == 1

    import asyncio

    asyncio.run(run())


def test_async_http_error_exposes_legacy_request_id():
    async def run():
        request = httpx.Request("POST", "https://example.test/ReadVms")
        body = {
            "ResponseContext": {"RequestId": "req-legacy"},
            "Errors": [{"Code": "InvalidParameter", "Type": "Sender"}],
        }
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=0))
        transport._transport = AsyncSequenceTransport(
            [
                httpx.Response(
                    400,
                    json=body,
                    headers={"content-type": "application/json"},
                    request=request,
                )
            ]
        )

        with pytest.raises(SdkClientError) as exc_info:
            await transport.handle_async_request(request)

        assert exc_info.value.request_id == "req-legacy"
        assert "request_id = req-legacy" in str(exc_info.value)

    import asyncio

    asyncio.run(run())


def test_async_http_error_exposes_problem_request_id_extra():
    async def run():
        request = httpx.Request("GET", "https://example.test/projects")
        transport = AsyncSdkTransport(retry_policy=RetryPolicy(max_retries=0))
        transport._transport = AsyncSequenceTransport(
            [
                httpx.Response(
                    403,
                    json={"title": "Forbidden", "request_id": "req-problem"},
                    headers={"content-type": "application/problem+json"},
                    request=request,
                )
            ]
        )

        with pytest.raises(SdkClientError) as exc_info:
            await transport.handle_async_request(request)

        assert exc_info.value.request_id == "req-problem"
        assert "request_id=req-problem" in str(exc_info.value)
        assert "request_id='req-problem'" in repr(exc_info.value)

    import asyncio

    asyncio.run(run())


def test_extract_request_id_falls_back_to_response_header():
    request = httpx.Request("POST", "https://example.test/ReadVms")
    response = text_response(
        500,
        request,
        "upstream failure",
        headers={"x-osc-request-id": "req-header"},
    )

    error = SdkTransportError("boom", response=response)

    assert extract_request_id(response=response) == "req-header"
    assert error.request_id == "req-header"
    assert str(error) == "boom (request_id=req-header)"
