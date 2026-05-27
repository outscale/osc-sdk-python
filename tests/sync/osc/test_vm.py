import unittest
import sys

sys.path.append("..")
from osc_sdk_python import Client

class TestVm(unittest.TestCase):
    def test_listing(self):
        with Client() as client:
            vms = client.osc.ReadVms()
            self.assertEqual(type(vms), dict)
            self.assertEqual(type(vms.get("Vms")), list)

    def test_listing_with_context_manager(self):
        with Client() as client:
            vms = client.osc.ReadVms()
            self.assertEqual(type(vms), dict)
            self.assertEqual(type(vms.get("Vms")), list)

if __name__ == "__main__":
    unittest.main()
