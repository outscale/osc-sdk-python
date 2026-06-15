import asyncio
import logging
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVmsRequest, ReadVmsResponse


class TestAsyncLog(unittest.TestCase):
    def test_listing(self):
        async def run():
            async with AsyncClient() as client:
                with self.assertLogs("osc_sdk_python", level=logging.INFO) as logs:
                    vms = await client.osc.read_vms(ReadVmsRequest())
                self.assertIsInstance(vms, ReadVmsResponse)
                self.assertEqual(
                    logs.records[-1].getMessage(),
                    """mode: async
service: api
method: POST
uri: /api/v1/ReadVms
payload:
{}""",
                )

                with self.assertLogs("osc_sdk_python", level=logging.INFO) as logs:
                    vms = await client.osc.read_vms(
                        ReadVmsRequest(filters={"TagKeys": ["test"]})
                    )
                self.assertIsInstance(vms, ReadVmsResponse)
                self.assertEqual(
                    logs.records[-1].getMessage(),
                    """mode: async
service: api
method: POST
uri: /api/v1/ReadVms
payload:
{
  "Filters": {
    "TagKeys": [
      "test"
    ]
  }
}""",
                )

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
