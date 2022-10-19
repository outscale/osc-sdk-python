import unittest
import sys
import os
sys.path.append("..")
from osc_sdk_python import Gateway

class TestLoginPassword(unittest.TestCase):

    def test_login(self):
        os.environ.pop("OSC_ACCESS_KEY", None)
        os.environ.pop("OSC_SECRET_KEY", None)
        email = os.getenv('OSC_TEST_LOGIN')
        password = os.getenv('OSC_TEST_PASSWORD')
        self.assertNotEqual(email, None)
        self.assertNotEqual(password, None)
        gw = Gateway(email=email, password=password)
        keys = gw.ReadAccessKeys()
        self.assertEqual(type(keys), dict)
        self.assertEqual(type(keys.get("AccessKeys")), list)

if __name__ == '__main__':
    unittest.main()
