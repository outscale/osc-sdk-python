import time
import unittest

import requests

from osc_sdk_python import Client
from tests.integration_utils import get_tagged_name, log_test_step


PROJECT_READY_STATUS = "ready"


def wait_project_ready(client, project_id):
    for _ in range(36):
        response = client.oks.GetProject(project_id=project_id)
        project = response.get("Project")
        status = project.get("status")
        log_test_step("OKS project {} status={}".format(project_id, status))
        if status == PROJECT_READY_STATUS:
            return project
        time.sleep(10)

    raise AssertionError("OKS project {} did not become ready".format(project_id))


def delete_project_when_ready(client, project_id):
    for _ in range(36):
        try:
            delete_response = client.oks.DeleteProject(project_id=project_id)
            log_test_step("Deleted OKS project {}".format(project_id))
            return delete_response
        except requests.HTTPError as err:
            if err.response is None or err.response.status_code != 503:
                raise
            log_test_step(
                "OKS project {} is not ready for deletion yet".format(project_id)
            )
            time.sleep(10)

    raise AssertionError("OKS project {} could not be deleted".format(project_id))


class TestOksProject(unittest.TestCase):
    def test_project_lifecycle(self):
        with Client() as client:
            project_id = None
            project_name = get_tagged_name("osc-sdk-python-oks-project")
            updated_description = "Updated OKS project lifecycle test"

            try:
                log_test_step("Reading OKS project template")
                template_response = client.oks.GetProjectTemplate()
                project_input = template_response.get("Template")
                self.assertIsInstance(project_input, dict)
                project_input.update(
                    {
                        "name": project_name,
                        "description": "OKS project lifecycle test",
                        "tags": {"Name": project_name},
                    }
                )

                log_test_step("Creating OKS project {}".format(project_name))
                create_response = client.oks.CreateProject(body=project_input)
                project = create_response.get("Project")
                self.assertIsInstance(project, dict)
                project_id = project.get("id")
                self.assertTrue(project_id)
                self.assertEqual(project.get("name"), project_name)
                log_test_step("Created OKS project {}".format(project_id))

                log_test_step("Reading OKS project {}".format(project_id))
                get_response = client.oks.GetProject(project_id=project_id)
                read_project = get_response.get("Project")
                self.assertIsInstance(read_project, dict)
                self.assertEqual(read_project.get("id"), project_id)
                self.assertEqual(read_project.get("name"), project_name)

                read_project = wait_project_ready(client, project_id)
                self.assertEqual(read_project.get("id"), project_id)
                self.assertEqual(read_project.get("name"), project_name)

                log_test_step("Updating OKS project {}".format(project_id))
                update_response = client.oks.UpdateProject(
                    project_id=project_id,
                    body={
                        "description": updated_description,
                        "tags": {"Name": project_name, "Updated": "true"},
                    },
                )
                updated_project = update_response.get("Project")
                self.assertIsInstance(updated_project, dict)
                self.assertEqual(updated_project.get("id"), project_id)
                self.assertEqual(updated_project.get("name"), project_name)
                self.assertEqual(updated_project.get("description"), updated_description)
            finally:
                if project_id:
                    log_test_step("Deleting OKS project {}".format(project_id))
                    delete_project_when_ready(client, project_id)


if __name__ == "__main__":
    unittest.main()
