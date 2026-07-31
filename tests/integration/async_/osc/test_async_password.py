import asyncio
import copy
import os
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    AccessKey,
    ReadAccessKeysRequest,
    ReadAccessKeysResponse,
)


class EnvironManager:
    def __enter__(self):
        self.env = copy.deepcopy(os.environ)

    def __exit__(self, *args):
        os.environ = self.env


class TestAsyncLoginPassword(unittest.TestCase):
    @unittest.skipIf(
        not (os.environ.get("OSC_TEST_LOGIN") and os.environ.get("OSC_TEST_PASSWORD")),
        "login/password credentials are not available",
    )
    def test_login(self):
        async def run():
            with EnvironManager():
                os.environ.pop("OSC_ACCESS_KEY", None)
                os.environ.pop("OSC_SECRET_KEY", None)
                email = os.getenv("OSC_TEST_LOGIN")
                password = os.getenv("OSC_TEST_PASSWORD")
                self.assertIsNotNone(email)
                self.assertIsNotNone(password)
                async with AsyncClient(email=email, password=password) as client:
                    keys = await client.osc.read_access_keys(ReadAccessKeysRequest())

                self.assertIsInstance(keys, ReadAccessKeysResponse)
                self.assertIsInstance(keys.access_keys, list)
                if keys.access_keys:
                    self.assertIsInstance(keys.access_keys[0], AccessKey)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
