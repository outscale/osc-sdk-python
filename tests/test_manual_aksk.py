import unittest
import sys
import os
sys.path.append("..")
from osc_sdk_python import Gateway

class TestLoginManualAkSk(unittest.TestCase):

    def test_manual_ak_sk(self):
        ak = os.environ.pop("OSC_ACCESS_KEY", None)
        sk = os.environ.pop("OSC_SECRET_KEY", None)
        self.assertNotEqual(ak, None)
        self.assertNotEqual(sk, None)
        gw = Gateway(access_key=ak, secret_key=sk)
        volumes = gw.ReadVolumes()
        self.assertEqual(type(volumes), dict)
        self.assertEqual(type(volumes.get("Volumes")), list)

if __name__ == '__main__':
    unittest.main()
