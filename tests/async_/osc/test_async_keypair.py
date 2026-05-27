import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    CreateKeypairRequest,
    CreateKeypairResponse,
    DeleteKeypairRequest,
    KeypairCreated,
)
from tests.async_.osc.async_integration_utils import get_tagged_name, log_test_step


class TestAsyncKeypair(unittest.TestCase):
    def test_keypair_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                keypair_name = get_tagged_name("osc-sdk-python-keypair-async")
                keypair_id = None
                try:
                    log_test_step("Creating keypair {} (async)".format(keypair_name))
                    response = await client.osc.create_keypair(
                        CreateKeypairRequest(keypair_name=keypair_name)
                    )
                    self.assertIsInstance(response, CreateKeypairResponse)
                    keypair = response.keypair
                    self.assertIsInstance(keypair, KeypairCreated)
                    keypair_id = keypair.keypair_id
                    self.assertTrue(keypair_id)
                    log_test_step("Created keypair {} (async)".format(keypair_id))
                finally:
                    if keypair_id:
                        log_test_step("Deleting keypair {} (async)".format(keypair_id))
                        await client.osc.delete_keypair(
                            DeleteKeypairRequest(keypair_id=keypair_id)
                        )

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
