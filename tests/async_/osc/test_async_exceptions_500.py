import asyncio
import copy
import os
import sys
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer

import httpx

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVmsRequest


class EnvironManager:
    def __enter__(self):
        self.env = copy.deepcopy(os.environ)

    def __exit__(self, *args):
        os.environ = self.env


class Send500(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(500)
        self.send_header("Content-type", "application/json")
        self.send_header("x-amz-requestid", "00000001")
        self.end_headers()
        self.wfile.write(
            b'{"error": "Internal Server Error", "message": "test", "__type": 9}'
        )


@unittest.skip("this test is flaky")
class TestAsyncServerError(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = None
        cls.thread = None

        def start_server():
            with TCPServer(("localhost", 8000), Send500) as httpd:
                cls.server = httpd
                httpd.serve_forever()

        cls.thread = threading.Thread(target=start_server)
        cls.thread.daemon = True
        cls.thread.start()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        if cls.server:
            cls.server.shutdown()
            cls.thread.join()

    def test_server_error(self):
        async def run():
            with EnvironManager():
                os.environ["OSC_ENDPOINT_API"] = "http://127.0.0.1:8000"
                async with AsyncClient() as client:
                    with self.assertRaises(httpx.HTTPStatusError):
                        await client.osc.read_vms(ReadVmsRequest())

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
