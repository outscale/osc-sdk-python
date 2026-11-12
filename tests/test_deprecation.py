import sys
import unittest
import warnings
from unittest import mock

sys.path.append("..")
from osc_sdk_python import Gateway


class TestDeprecation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gw = Gateway()

    def _call_with_warnings(self, fn):
        with mock.patch.object(self.gw.call, "api", return_value={}):
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                fn()
        return [str(w.message) for w in caught]

    def test_deprecated_action_warns(self):
        messages = self._call_with_warnings(lambda: self.gw.CreateCa(CaPem="pem"))
        self.assertEqual(
            messages, ["CreateCa action is deprecated and will be removed."]
        )

    def test_deprecated_field_warns(self):
        messages = self._call_with_warnings(
            lambda: self.gw.CreateVms(
                ImageId="ami-x", VmInitiatedShutdownBehavior="stop"
            )
        )
        self.assertEqual(
            messages,
            [
                "CreateVms.VmInitiatedShutdownBehavior parameter is deprecated and will be removed."
            ],
        )

    def test_no_warning_for_current_api(self):
        messages = self._call_with_warnings(lambda: self.gw.CreateVms(ImageId="ami-x"))
        self.assertEqual(messages, [])

    def test_raw_does_not_warn(self):
        messages = self._call_with_warnings(
            lambda: self.gw.raw("CreateCa", CaPem="pem")
        )
        self.assertEqual(messages, [])


if __name__ == "__main__":
    unittest.main()
