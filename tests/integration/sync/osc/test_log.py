import logging
import unittest

from osc_sdk_python import Client


class TestLog(unittest.TestCase):
    def test_listing(self):
        with Client() as client:
            with self.assertLogs("osc_sdk_python", level=logging.INFO) as logs:
                client.osc.ReadVms()
            self.assertEqual(
                logs.records[-1].getMessage(),
                """mode: sync
service: api
method: POST
uri: /api/v1/ReadVms
payload:
{}""",
            )

            with self.assertLogs("osc_sdk_python", level=logging.INFO) as logs:
                client.osc.ReadVms(Filters={"TagKeys": ["test"]})
            self.assertEqual(
                logs.records[-1].getMessage(),
                """mode: sync
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


if __name__ == "__main__":
    unittest.main()
