import unittest
import threading
import http.server
import socketserver
import sys
import os
import time

sys.path.append("..")
from osc_sdk_python import Gateway
from requests.exceptions import RetryError
from requests import HTTPError
import copy


class EnvironManager:
    def __enter__(self):
        self.env = copy.deepcopy(os.environ)

    def __exit__(self, *args):
        os.environ = self.env


class Send500(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(500)
        self.send_header("Content-type", "application/json")
        self.send_header("x-amz-requestid", "00000001")
        self.end_headers()
        self.wfile.write(
            b'{"error": "Internal Server Error", "message": "test", "__type": 9}'
        )


@unittest.skip("this test is flaky")
class TestServerError(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = None
        cls.thread = None

        # Start the server
        def start_server():
            with socketserver.TCPServer(("localhost", 8000), Send500) as httpd:
                cls.server = httpd
                httpd.serve_forever()

        cls.thread = threading.Thread(target=start_server)
        cls.thread.daemon = True
        cls.thread.start()

        # Wait a bit for the server to start
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        if cls.server:
            cls.server.shutdown()
            cls.thread.join()

    def test_server_error(self):
        os.environ["OSC_ENDPOINT_API"] = "http://127.0.0.1:8000"
        gw = Gateway()
        # a is not a valide argument
        with self.assertRaises(RetryError):
            gw.ReadVms()
            os.environ.pop("OSC_ENDPOINT_API", None)
            os.environ["OSC_ENDPOINT_API"] = "http://127.0.0.1:8000"
            gw = Gateway()
            # a is not a valide argument
            with self.assertRaises(HTTPError):
                gw.ReadVms()


if __name__ == "__main__":
    unittest.main()
