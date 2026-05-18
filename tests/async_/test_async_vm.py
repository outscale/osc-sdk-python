import asyncio
import sys
import unittest

sys.path.append("..")
from osc_sdk_python import AsyncGateway


class TestAsyncVm(unittest.TestCase):
    def test_listing(self):
        async def run():
            gw = AsyncGateway()
            try:
                vms = await gw.ReadVms()
            finally:
                await gw.close()

            self.assertEqual(type(vms), dict)
            self.assertEqual(type(vms.get("Vms")), list)

        asyncio.run(run())

    def test_listing_with_context_manager(self):
        async def run():
            async with AsyncGateway() as gw:
                vms = await gw.ReadVms()
                self.assertEqual(type(vms), dict)
                self.assertEqual(type(vms.get("Vms")), list)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
