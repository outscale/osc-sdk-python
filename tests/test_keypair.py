import sys
import unittest

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import log_step, tagged_name


class TestKeypair(unittest.TestCase):
    def test_keypair_lifecycle(self):
        gw = Gateway()
        keypair_name = tagged_name("osc-sdk-python-keypair")
        keypair_id = None
        try:
            log_step("Creating keypair {}".format(keypair_name))
            response = gw.CreateKeypair(KeypairName=keypair_name)
            keypair = response.get("Keypair")
            self.assertIsInstance(keypair, dict)
            keypair_id = keypair.get("KeypairId")
            self.assertTrue(keypair_id)
            log_step("Created keypair {}".format(keypair_id))
        finally:
            if keypair_id:
                log_step("Deleting keypair {}".format(keypair_id))
                gw.DeleteKeypair(KeypairId=keypair_id)


if __name__ == "__main__":
    unittest.main()
