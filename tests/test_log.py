import unittest
import sys
sys.path.append("..")
from osc_sdk_python import *

class TestLog(unittest.TestCase):

    def test_listing(self):
        gw = Gateway()
        gw.log.config(type=LOG_MEMORY, what=LOG_KEEP_ONLY_LAST_REQ)
        gw.ReadVms()
        self.assertEqual(gw.log.str(),
                         """uri: /api/v1/ReadVms
payload:
{}"""
                         )

        gw.ReadVms(Filters={'TagKeys': ['test']})
        self.assertEqual(gw.log.str(),
                         """uri: /api/v1/ReadVms
payload:
{
  "Filters": {
    "TagKeys": [
      "test"
    ]
  }
}"""
                         )

if __name__ == '__main__':
    unittest.main()
