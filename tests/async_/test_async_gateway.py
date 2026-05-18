import asyncio
import json

import httpx

from osc_sdk_python import AsyncGateway, LOG_KEEP_ONLY_LAST_REQ, LOG_MEMORY


def test_async_gateway_listing_and_log():
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, json={"Vms": []}, request=request)

    async def run():
        gw = AsyncGateway(access_key="ak", secret_key="sk")
        await gw.call.client.aclose()
        gw.call.client = httpx.AsyncClient(
            transport=httpx.MockTransport(handler),
            trust_env=False,
        )
        gw.log.config(type=LOG_MEMORY, what=LOG_KEEP_ONLY_LAST_REQ)

        try:
            vms = await gw.ReadVms()
        finally:
            await gw.close()

        assert vms == {"Vms": []}
        assert len(requests) == 1
        assert requests[0].method == "POST"
        assert str(requests[0].url) == "https://api.eu-west-2.outscale.com/api/v1/ReadVms"
        assert json.loads(requests[0].content.decode("utf-8")) == {}
        assert gw.log.str() == """uri: /api/v1/ReadVms
payload:
{}"""

    asyncio.run(run())


def test_async_gateway_context_manager_closes_client():
    async def run():
        async with AsyncGateway(access_key="ak", secret_key="sk") as gw:
            assert not gw.call.client.is_closed

        assert gw.call.client.is_closed

    asyncio.run(run())
