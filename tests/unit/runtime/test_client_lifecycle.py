import asyncio
from unittest.mock import Mock

import pytest

from osc_sdk_python import AsyncClient, SdkConfigurationError, SdkUsageError
from osc_sdk_python.outscale_gateway import OpenAPIActionAPI
from osc_sdk_python.runtime.call import AsyncCall


def test_async_client_close_closes_service_clients():
    """Test AsyncClient.close closes OSC and OKS async clients"""

    async def run():
        client = AsyncClient()

        await client.close()

        assert client.osc.call.client.is_closed
        assert client.oks.call.client.is_closed

    asyncio.run(run())


def test_async_client_context_manager_closes_service_clients():
    """Test AsyncClient context manager closes OSC and OKS async clients"""

    async def run():
        async with AsyncClient() as client:
            osc_client = client.osc.call.client
            oks_client = client.oks.call.client

        assert osc_client.is_closed
        assert oks_client.is_closed

    asyncio.run(run())


def test_async_client_rejects_sync_context_manager():
    """Test AsyncClient cannot be used with a sync context manager"""
    with pytest.raises(SdkUsageError):
        with AsyncClient():
            pass


class FakeAsyncClient:
    def __init__(self, tls_skip_verify):
        self.tls_skip_verify = tls_skip_verify


class RecordingAsyncCall(AsyncCall):
    def __init__(self, **kwargs):
        self.created_clients = []
        super().__init__(**kwargs)

    def _make_client(self):
        client = FakeAsyncClient(self.profile.tls_skip_verify)
        self.created_clients.append(client)
        return client


def test_update_profile_recreates_async_client_for_tls_settings():
    call = RecordingAsyncCall(tls_skip_verify=False)
    old_client = call.client

    call.update_profile(tls_skip_verify=True)

    assert call.client.tls_skip_verify is True
    assert call.client is not old_client


def test_openapi_action_api_raises_configuration_error_for_unreadable_spec():
    with pytest.raises(SdkConfigurationError, match="Problem reading OpenAPI spec"):
        OpenAPIActionAPI("missing-spec.yaml")


def test_dynamic_service_hasattr_reflects_available_operations():
    async def run():
        async with AsyncClient() as client:
            assert hasattr(client.osc, "ReadVms")
            assert not hasattr(client.osc, "TotallyWrongAction")
            assert "ReadVms" in dir(client.osc)

            assert hasattr(client.oks, "ListProjects")
            assert not hasattr(client.oks, "TotallyWrongOperation")
            assert "ListProjects" in dir(client.oks)

    asyncio.run(run())


def test_unknown_dynamic_service_attribute_raises_attribute_error():
    async def run():
        async with AsyncClient() as client:
            with pytest.raises(AttributeError):
                _ = client.osc.TotallyWrongAction

            with pytest.raises(AttributeError):
                _ = client.oks.TotallyWrongOperation

    asyncio.run(run())
