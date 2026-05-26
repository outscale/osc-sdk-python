import asyncio
import unittest

import httpx

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import CreateNetRequest


class TestAsyncNet(unittest.TestCase):
    def test_creation_error(self):
        async def run():
            async with AsyncClient() as client:
                with self.assertRaises(httpx.HTTPStatusError) as cm:
                    await client.osc.create_net(
                        CreateNetRequest(ip_range="142.42.42.42/32")
                    )

            errors = cm.exception.response.json().get("Errors")
            self.assertIsNotNone(errors)
            self.assertIsInstance(errors, list)
            for error in errors:
                self.assertEqual(error.get("Code"), "9050")

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
