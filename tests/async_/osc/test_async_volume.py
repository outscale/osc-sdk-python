import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVolumesRequest, ReadVolumesResponse, Volume


class TestAsyncVolume(unittest.TestCase):
    def test_listing(self):
        async def run():
            async with AsyncClient() as client:
                volumes = await client.osc.read_volumes(ReadVolumesRequest())

            self.assertIsInstance(volumes, ReadVolumesResponse)
            self.assertIsInstance(volumes.volumes, list)
            if volumes.volumes:
                self.assertIsInstance(volumes.volumes[0], Volume)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
