import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    CreateKeypairRequest,
    CreateKeypairResponse,
    DeleteKeypairRequest,
    KeypairCreated,
)
from tests.integration.async_.helpers.async_integration_utils import (
    get_tagged_name,
    log_test_step,
)


class TestAsyncKeypair(unittest.TestCase):
    def test_keypair_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                keypair_name = get_tagged_name("osc-sdk-python-keypair-async")
                keypair_id = None
                try:
                    log_test_step(f"Creating keypair {keypair_name} (async)")
                    response = await client.osc.create_keypair(
                        CreateKeypairRequest(keypair_name=keypair_name)
                    )
                    self.assertIsInstance(response, CreateKeypairResponse)
                    keypair = response.keypair
                    self.assertIsInstance(keypair, KeypairCreated)
                    keypair_id = keypair.keypair_id
                    self.assertTrue(keypair_id)
                    log_test_step(f"Created keypair {keypair_id} (async)")
                finally:
                    if keypair_id:
                        log_test_step(f"Deleting keypair {keypair_id} (async)")
                        await client.osc.delete_keypair(
                            DeleteKeypairRequest(keypair_id=keypair_id)
                        )

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
