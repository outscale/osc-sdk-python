import asyncio
import unittest

from osc_sdk_python import AsyncClient, SdkValidationError


class TestAsyncExcept(unittest.TestCase):
    def test_listing(self):
        async def run():
            async with AsyncClient() as client:
                with self.assertRaises(SdkValidationError):
                    await client.osc.read_vms({"filters": "a"})

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
