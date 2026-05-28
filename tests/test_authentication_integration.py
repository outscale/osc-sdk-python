import asyncio

import httpx
import pytest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVmsRequest


def test_invalid_credentials_raise_http_error():
    """Test invalid credentials are rejected by the API in the async client"""
    async def run():
        async with AsyncClient(
            access_key="invalid-access-key",
            secret_key="invalid-secret-key",
            max_retries=0,
        ) as client:
            with pytest.raises(httpx.HTTPStatusError) as exc_info:
                await client.osc.read_vms(ReadVmsRequest())

        assert exc_info.value.response is not None
        assert exc_info.value.response.status_code in {400, 401, 403}
        assert "code = 4120" in str(exc_info.value)

    asyncio.run(run())
