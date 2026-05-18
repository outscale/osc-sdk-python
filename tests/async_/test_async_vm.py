import asyncio
import sys
import unittest

sys.path.append("..")
from osc_sdk_python import AsyncClient


class TestAsyncVm(unittest.TestCase):
    def test_listing(self):
        async def run():
            client = AsyncClient()
            try:
                vms = await client.osc.ReadVms()
            finally:
                await client.close()

            self.assertEqual(type(vms), dict)
            self.assertEqual(type(vms.get("Vms")), list)

        asyncio.run(run())

    def test_listing_with_context_manager(self):
        async def run():
            async with AsyncClient() as client:
                vms = await client.osc.ReadVms()
                self.assertEqual(type(vms), dict)
                self.assertEqual(type(vms.get("Vms")), list)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
