import sys
import unittest

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import get_tagged_name, log_test_step


class TestEimUser(unittest.TestCase):
    def test_eim_user_lifecycle(self):
        gw = Gateway()
        user_name = get_tagged_name("osc-sdk-python-user")
        user_email = "{}@example.com".format(user_name)
        user_id = None
        try:
            log_test_step("Creating EIM user {}".format(user_name))
            response = gw.CreateUser(Path="/", UserEmail=user_email, UserName=user_name)
            user = response.get("User")
            self.assertIsInstance(user, dict)
            user_id = user.get("UserId")
            self.assertTrue(user_id)
            log_test_step("Created EIM user {}".format(user_id))
            self.assertEqual(user.get("UserName"), user_name)
            self.assertEqual(user.get("UserEmail"), user_email)
            self.assertEqual(user.get("Path"), "/")

            log_test_step("Reading EIM user {}".format(user_id))
            read_response = gw.ReadUsers(Filters={"UserIds": [user_id]})
            users = read_response.get("Users")
            self.assertIsInstance(users, list)
            self.assertEqual(len(users), 1)
            self.assertEqual(users[0].get("UserId"), user_id)
            self.assertEqual(users[0].get("UserName"), user_name)
            self.assertEqual(users[0].get("UserEmail"), user_email)
        finally:
            if user_id:
                log_test_step("Deleting EIM user {}".format(user_name))
                gw.DeleteUser(UserName=user_name)


if __name__ == "__main__":
    unittest.main()
