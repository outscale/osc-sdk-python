import asyncio
from unittest.mock import Mock

import pytest

from osc_sdk_python import AsyncClient, Client


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
    with pytest.raises(TypeError):
        with AsyncClient():
            pass
