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


class TestLoginPassword(unittest.TestCase):
    @unittest.skipIf(
        not (os.environ.get("OSC_TEST_LOGIN") and os.environ.get("OSC_TEST_PASSWORD")),
        "login/password credentials are not available",
    )
    def test_login(self):
        with EnvironManager():
            os.environ.pop("OSC_ACCESS_KEY", None)
            os.environ.pop("OSC_SECRET_KEY", None)
            email = os.getenv("OSC_TEST_LOGIN")
            password = os.getenv("OSC_TEST_PASSWORD")
            self.assertIsNotNone(email, None)
            self.assertIsNotNone(password, None)
            gw = Gateway(email=email, password=password)
            keys = gw.ReadAccessKeys()
            self.assertIsInstance(keys, dict)
            self.assertIsInstance(keys.get("AccessKeys"), list)


if __name__ == "__main__":
    unittest.main()
