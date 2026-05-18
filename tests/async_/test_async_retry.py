import asyncio

import httpx
import pytest

from osc_sdk_python.runtime.async_.retry import AsyncRetry


def test_async_retry_success_no_retry():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, json={"ok": True}, request=request)

    async def run():
        async with httpx.AsyncClient(
            transport=httpx.MockTransport(handler),
            trust_env=False,
        ) as client:
            retry = AsyncRetry(client, "POST", "https://example.test")
            result = await retry.execute()

        assert result.json() == {"ok": True}
        assert len(calls) == 1

    asyncio.run(run())


def test_async_retry_retries_429(monkeypatch):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(429, json={"Errors": []}, request=request)

    async def fake_sleep(_):
        return None

    async def run():
        monkeypatch.setattr("asyncio.sleep", fake_sleep)
        async with httpx.AsyncClient(
            transport=httpx.MockTransport(handler),
            trust_env=False,
        ) as client:
            retry = AsyncRetry(
                client,
                "POST",
                "https://example.test",
                max_retries=2,
            )
            with pytest.raises(httpx.HTTPStatusError):
                await retry.execute()

        assert len(calls) == 3

    asyncio.run(run())
