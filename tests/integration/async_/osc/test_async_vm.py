import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVmsRequest, ReadVmsResponse, Vm


class TestAsyncVm(unittest.TestCase):
    def test_listing(self):
        async def run():
            client = AsyncClient()
            try:
                vms = await client.osc.read_vms(ReadVmsRequest())
            finally:
                await client.close()

            self.assertIsInstance(vms.vms, list)
            self.assertIsInstance(vms, ReadVmsResponse)
            if vms.vms:
                self.assertIsInstance(vms.vms[0], Vm)

        asyncio.run(run())

    def test_listing_with_context_manager(self):
        async def run():
            async with AsyncClient() as client:
                vms = await client.osc.read_vms(ReadVmsRequest())
                self.assertIsInstance(vms, ReadVmsResponse)
                self.assertIsInstance(vms.vms, list)
                if vms.vms:
                    self.assertIsInstance(vms.vms[0], Vm)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
