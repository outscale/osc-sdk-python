import unittest
import sys

sys.path.append("..")
import httpx

from osc_sdk_python import Client


class TestExcept(unittest.TestCase):
    def test_listing(self):
        with Client() as client:
            # a is not a valide argument
            with self.assertRaises(httpx.HTTPStatusError):
                client.osc.ReadVms(Filters="a")


if __name__ == "__main__":
    unittest.main()
