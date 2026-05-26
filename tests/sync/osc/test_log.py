import unittest
import sys

sys.path.append("..")
from osc_sdk_python import Client, LOG_MEMORY, LOG_KEEP_ONLY_LAST_REQ


class TestLog(unittest.TestCase):
    def test_listing(self):
        with Client() as client:
            client.osc.log.config(type=LOG_MEMORY, what=LOG_KEEP_ONLY_LAST_REQ)
            client.osc.ReadVms()
            self.assertEqual(
                client.osc.log.str(),
                """uri: /api/v1/ReadVms
payload:
{}""",
            )

            client.osc.ReadVms(Filters={"TagKeys": ["test"]})
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


if __name__ == "__main__":
    unittest.main()
