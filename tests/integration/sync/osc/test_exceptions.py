import unittest

from osc_sdk_python import Client, SdkClientError


class TestExcept(unittest.TestCase):
    def test_listing(self):
        with Client() as client:
            # a is not a valide argument
            with self.assertRaises(SdkClientError):
                client.osc.ReadVms(Filters="a")


if __name__ == "__main__":
    unittest.main()
