import unittest
import sys
import requests
sys.path.append("..")
from osc_sdk_python import Gateway

class TestNet(unittest.TestCase):
    def test_creation_error(self):
        gw = Gateway()
        with self.assertRaises(requests.exceptions.HTTPError) as cm:
            gw.CreateNet(IpRange='142.42.42.42/32')

        e = cm.exception
        errors = e.response.json().get('Errors')
        self.assertIsNotNone(errors)
        self.assertIsInstance(errors, list)
        for error in errors:
            code = error.get('Code')
            self.assertEqual(code, '9050')
