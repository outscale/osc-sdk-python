import asyncio
import unittest

from osc_sdk_python import AsyncClient


class TestAsyncOks(unittest.TestCase):
    def test_list_projects(self):
        async def run():
            async with AsyncClient() as client:
                projects = await client.oks.ListProjects()

            self.assertEqual(type(projects), dict)
            self.assertEqual(type(projects.get("Projects")), list)

        asyncio.run(run())

    def test_kubernetes_versions(self):
        async def run():
            async with AsyncClient() as client:
                versions = await client.oks.GetKubernetesVersions()

            self.assertEqual(type(versions), dict)
            self.assertEqual(type(versions.get("Versions")), list)

        asyncio.run(run())

if __name__ == "__main__":
    unittest.main()
