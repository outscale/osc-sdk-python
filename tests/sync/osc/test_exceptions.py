import unittest
import sys

sys.path.append("..")
from osc_sdk_python import Client
from requests.exceptions import HTTPError


class TestExcept(unittest.TestCase):
    def test_listing(self):
        with Client() as client:
            # a is not a valide argument
            with self.assertRaises(HTTPError):
                client.osc.ReadVms(Filters="a")


if __name__ == "__main__":
    unittest.main()
