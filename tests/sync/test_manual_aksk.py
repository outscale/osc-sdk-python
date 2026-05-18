import unittest
import sys
import os

sys.path.append("..")
from osc_sdk_python import Gateway
import copy


class EnvironManager:
    def __enter__(self):
        self.env = copy.deepcopy(os.environ)

    def __exit__(self, *args):
        os.environ = self.env


class TestLoginManualAkSk(unittest.TestCase):
    def test_manual_ak_sk(self):
        with EnvironManager():
            ak = os.environ.pop("OSC_ACCESS_KEY", None)
            sk = os.environ.pop("OSC_SECRET_KEY", None)
            self.assertIsNotNone(ak)
            self.assertIsNotNone(sk)
            gw = Gateway(access_key=ak, secret_key=sk)
            volumes = gw.ReadVolumes()
            self.assertIsInstance(volumes, dict)
            self.assertIsInstance(volumes.get("Volumes"), list)


if __name__ == "__main__":
    unittest.main()
