import os
import unittest
import unittest.mock

from osc_sdk_python.call import Call
from osc_sdk_python.credentials import Profile


class TestProxySupport(unittest.TestCase):
    def test_proxy_env_passed_to_session(self):
        with unittest.mock.patch.object(
            Profile, "from_standard_configuration"
        ) as mock_from_std:
            mock_from_std.return_value = Profile(region="eu-west-2", protocol="https")

            with unittest.mock.patch.dict(
                os.environ, {"HTTPS_PROXY": "http://proxy.example.com:8080"}
            ):
                call = Call(access_key="fake-ak", secret_key="fake-sk")

                captured_proxies = []

                class FakeAdapter:
                    def send(self, request, **kwargs):
                        captured_proxies.append(kwargs.get("proxies"))
                        import requests

                        resp = requests.Response()
                        resp.status_code = 200
                        resp._content = b'{"status": "ok"}'
                        resp.request = request
                        resp.url = request.url
                        return resp

                call.session.mount("https://", FakeAdapter())

                result = call.api("ReadVms")

                self.assertEqual(len(captured_proxies), 1)
                self.assertEqual(
                    captured_proxies[0],
                    {"https": "http://proxy.example.com:8080"},
                )
                self.assertEqual(result, {"status": "ok"})

    def test_no_proxy_env_no_proxies_kwarg(self):
        with unittest.mock.patch.object(
            Profile, "from_standard_configuration"
        ) as mock_from_std:
            mock_from_std.return_value = Profile(region="eu-west-2", protocol="https")

            with unittest.mock.patch.dict(os.environ, {}, clear=True):
                call = Call(access_key="fake-ak", secret_key="fake-sk")

                captured_proxies = []

                class FakeAdapter:
                    def send(self, request, **kwargs):
                        captured_proxies.append(kwargs.get("proxies"))
                        import requests

                        resp = requests.Response()
                        resp.status_code = 200
                        resp._content = b'{"status": "ok"}'
                        resp.request = request
                        resp.url = request.url
                        return resp

                call.session.mount("https://", FakeAdapter())

                call.api("ReadVms")

                self.assertEqual(len(captured_proxies), 1)
                self.assertEqual(captured_proxies[0], {})


if __name__ == "__main__":
    unittest.main()
