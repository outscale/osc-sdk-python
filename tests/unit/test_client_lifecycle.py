import asyncio
from unittest.mock import Mock

import pytest

from osc_sdk_python import AsyncClient, Client, SdkConfigurationError, SdkUsageError
from osc_sdk_python.outscale_gateway import OpenAPIActionAPI
from osc_sdk_python.runtime.call import AsyncCall, Call


def test_client_close_closes_service_sessions():
    """Test Client.close closes OSC and OKS sync sessions"""
    client = Client()
    client.osc.call.session.close = Mock()
    client.oks.call.session.close = Mock()

    client.close()

    client.osc.call.session.close.assert_called_once()
    client.oks.call.session.close.assert_called_once()


def test_client_context_manager_closes_service_sessions():
    """Test Client context manager closes OSC and OKS sync sessions"""
    with Client() as client:
        client.osc.call.session.close = Mock()
        client.oks.call.session.close = Mock()
        osc_close = client.osc.call.session.close
        oks_close = client.oks.call.session.close

    osc_close.assert_called_once()
    oks_close.assert_called_once()


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


class FakeSyncClient:
    def __init__(self, tls_skip_verify):
        self.tls_skip_verify = tls_skip_verify
        self.closed = False

    def close(self):
        self.closed = True


class FakeAsyncClient:
    def __init__(self, tls_skip_verify):
        self.tls_skip_verify = tls_skip_verify


class RecordingCall(Call):
    def __init__(self, **kwargs):
        self.created_clients = []
        super().__init__(**kwargs)

    def _make_client(self):
        client = FakeSyncClient(self.profile.tls_skip_verify)
        self.created_clients.append(client)
        return client


class RecordingAsyncCall(AsyncCall):
    def __init__(self, **kwargs):
        self.created_clients = []
        super().__init__(**kwargs)

    def _make_client(self):
        client = FakeAsyncClient(self.profile.tls_skip_verify)
        self.created_clients.append(client)
        return client


def test_update_profile_recreates_sync_client_for_tls_settings():
    call = RecordingCall(tls_skip_verify=False)
    old_session = call.session

    call.update_profile(tls_skip_verify=True)

    assert old_session.closed is True
    assert call.session.tls_skip_verify is True
    assert call.session is not old_session


def test_update_profile_recreates_async_client_for_tls_settings():
    call = RecordingAsyncCall(tls_skip_verify=False)
    old_client = call.client

    call.update_profile(tls_skip_verify=True)

    assert call.client.tls_skip_verify is True
    assert call.client is not old_client


def test_openapi_action_api_raises_configuration_error_for_unreadable_spec():
    with pytest.raises(SdkConfigurationError, match="Problem reading OpenAPI spec"):
        OpenAPIActionAPI("missing-spec.yaml")
