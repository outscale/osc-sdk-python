import asyncio
import unittest

from osc_sdk_python import AsyncClient, LOG_KEEP_ONLY_LAST_REQ, LOG_MEMORY
from osc_sdk_python.generated.osc import ReadVmsRequest, ReadVmsResponse


class TestAsyncLog(unittest.TestCase):
    def test_listing(self):
        async def run():
            async with AsyncClient() as client:
                client.osc.log.config(type=LOG_MEMORY, what=LOG_KEEP_ONLY_LAST_REQ)
                vms = await client.osc.read_vms(ReadVmsRequest())
                self.assertIsInstance(vms, ReadVmsResponse)
                self.assertEqual(
                    client.osc.log.str(),
                    """uri: /api/v1/ReadVms
payload:
{}""",
                )

                vms = await client.osc.read_vms(
                    ReadVmsRequest(filters={"TagKeys": ["test"]})
                )
                self.assertIsInstance(vms, ReadVmsResponse)
                self.assertEqual(
                    client.osc.log.str(),
                    """uri: /api/v1/ReadVms
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
