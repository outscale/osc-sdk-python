import unittest
import sys

sys.path.append("..")
from osc_sdk_python import Gateway


class TestVm(unittest.TestCase):

    def test_listing(self):
        gw = Gateway()
        vms = gw.ReadVms()
        self.assertEqual(type(vms), dict)
        self.assertEqual(type(vms.get("Vms")), list)

    def test_listing_with_context_manager(self):
        with Gateway() as gw:
            vms = gw.ReadVms()
            self.assertEqual(type(vms), dict)
            self.assertEqual(type(vms.get("Vms")), list)


if __name__ == "__main__":
    unittest.main()
