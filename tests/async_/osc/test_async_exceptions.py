import asyncio
import unittest

from pydantic import ValidationError

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVmsRequest


class TestAsyncExcept(unittest.TestCase):
    def test_listing(self):
        async def run():
            async with AsyncClient() as client:
                with self.assertRaises(ValidationError):
                    await client.osc.read_vms(ReadVmsRequest(filters="a"))

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
