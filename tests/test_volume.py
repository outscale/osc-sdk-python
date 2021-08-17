import unittest
import sys
sys.path.append("..")
from osc_sdk_python import Gateway

class TestVolume(unittest.TestCase):

    def test_listing(self):
        gw = Gateway()
        volumes = gw.ReadVolumes()
        self.assertEqual(type(volumes), dict)
        self.assertEqual(type(volumes.get("Volumes")), list)

if __name__ == '__main__':
    unittest.main()
