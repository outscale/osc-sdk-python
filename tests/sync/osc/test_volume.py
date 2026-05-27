import unittest
import sys

sys.path.append("..")
from osc_sdk_python import Client

class TestVolume(unittest.TestCase):
    def test_listing(self):
        with Client() as client:
            volumes = client.osc.ReadVolumes()
            self.assertEqual(type(volumes), dict)
            self.assertEqual(type(volumes.get("Volumes")), list)

if __name__ == "__main__":
    unittest.main()
