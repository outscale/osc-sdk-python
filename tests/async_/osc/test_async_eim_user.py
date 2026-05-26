import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    CreateUserResponse,
    CreateUserRequest,
    DeleteUserRequest,
    ReadUsersResponse,
    ReadUsersRequest,
    User,
)
from tests.async_.osc.async_integration_utils import get_tagged_name, log_test_step


class TestAsyncEimUser(unittest.TestCase):
    def test_eim_user_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                user_name = get_tagged_name("osc-sdk-python-user-async")
                user_email = "{}@example.com".format(user_name)
                user_id = None
                try:
                    log_test_step("Creating EIM user {} (async)".format(user_name))
                    response = await client.osc.create_user(
                        CreateUserRequest(
                            path="/",
                            user_email=user_email,
                            user_name=user_name,
                        )
                    )
                    self.assertIsInstance(response, CreateUserResponse)
                    user = response.user
                    self.assertIsInstance(user, User)
                    user_id = user.user_id
                    self.assertTrue(user_id)
                    log_test_step("Created EIM user {} (async)".format(user_id))
                    self.assertEqual(user.user_name, user_name)
                    self.assertEqual(user.user_email, user_email)
                    self.assertEqual(user.path, "/")

                    log_test_step("Reading EIM user {} (async)".format(user_id))
                    read_response = await client.osc.read_users(
                        ReadUsersRequest(filters={"UserIds": [user_id]})
                    )
                    self.assertIsInstance(read_response, ReadUsersResponse)
                    users = read_response.users
                    self.assertIsInstance(users, list)
                    self.assertEqual(len(users), 1)
                    self.assertIsInstance(users[0], User)
                    self.assertEqual(users[0].user_id, user_id)
                    self.assertEqual(users[0].user_name, user_name)
                    self.assertEqual(users[0].user_email, user_email)
                finally:
                    if user_id:
                        log_test_step("Deleting EIM user {} (async)".format(user_name))
                        await client.osc.delete_user(
                            DeleteUserRequest(user_name=user_name)
                        )

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
