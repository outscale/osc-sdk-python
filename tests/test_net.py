import unittest
import sys
import requests
sys.path.append("..")
from osc_sdk_python import Gateway

class TestNet(unittest.TestCase):
    def test_creation_error(self):
        gw = Gateway()
        try:
            gw.CreateNet(IpRange='142.42.42.42/32')
            assert "CreateNet should not be allowed"
        except requests.exceptions.HTTPError as e:
            errors = e.response.json().get('Errors')
            self.assertIsNotNone(errors)
            self.assertEqual(type(errors), list)
            for error in errors:
                details = error.get('Details')
                self.assertIsNotNone(details)
                self.assertGreater(len(details), 0)
        except:
            assert "Unexpected error occured"
