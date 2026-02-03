import unittest
import sys

sys.path.append("..")
from osc_sdk_python import Gateway
from requests.exceptions import RetryError


class TestExcept(unittest.TestCase):

    def test_listing(self):
        gw = Gateway()
        # a is not a valide argument
        with self.assertRaises(RetryError):
            gw.ReadVms(Filters="a")


if __name__ == "__main__":
    unittest.main()
