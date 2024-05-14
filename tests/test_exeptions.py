import unittest
import sys
sys.path.append("..")
from osc_sdk_python import Gateway
from requests import HTTPError

class TestExept(unittest.TestCase):

    def test_listing(self):
        gw = Gateway()
        # a is not a valide argument
        with self.assertRaises(HTTPError):
            gw.ReadVms(Filters="a")

if __name__ == '__main__':
    unittest.main()
