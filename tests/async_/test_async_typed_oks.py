import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.oks import (
    KubernetesVersionsResponse,
    ListProjectsRequest,
    ProjectResponseList,
)

class TestAsyncTypedOks(unittest.TestCase):

    def test_typed_async_oks_methods_use_runtime_and_models(self):

        async def run():
            async with AsyncClient() as client:
                projects = await client.oks.list_projects(
                    ListProjectsRequest(name="demo", deleted=False)
                )
                versions = await client.oks.get_kubernetes_versions()
            assert isinstance(projects, ProjectResponseList)
            assert isinstance(versions, KubernetesVersionsResponse)

        asyncio.run(run())
