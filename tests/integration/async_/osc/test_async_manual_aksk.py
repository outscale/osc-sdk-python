import asyncio
import copy
import os
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVolumesRequest, ReadVolumesResponse, Volume


class EnvironManager:
    def __enter__(self):
        self.env = copy.deepcopy(os.environ)

    def __exit__(self, *args):
        os.environ = self.env


class TestAsyncLoginManualAkSk(unittest.TestCase):
    def test_manual_ak_sk(self):
        async def run():
            with EnvironManager():
                ak = os.environ.pop("OSC_ACCESS_KEY", None)
                sk = os.environ.pop("OSC_SECRET_KEY", None)
                self.assertIsNotNone(ak)
                self.assertIsNotNone(sk)
                async with AsyncClient(access_key=ak, secret_key=sk) as client:
                    volumes = await client.osc.read_volumes(ReadVolumesRequest())

                self.assertIsInstance(volumes, ReadVolumesResponse)
                self.assertIsInstance(volumes.volumes, list)
                if volumes.volumes:
                    self.assertIsInstance(volumes.volumes[0], Volume)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
