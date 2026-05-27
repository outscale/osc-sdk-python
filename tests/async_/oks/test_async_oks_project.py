import asyncio
import unittest

import httpx

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.oks import (
    CreateProjectRequest,
    DeleteProjectRequest,
    DetailResponse,
    GetProjectRequest,
    GetProjectTemplateRequest,
    Project,
    ProjectInput,
    ProjectResponse,
    ProjectUpdate,
    TemplateResponse_ProjectInput,
    UpdateProjectRequest,
)
from tests.integration_utils import get_tagged_name, log_test_step


PROJECT_READY_STATUS = "ready"


async def wait_project_ready(client, project_id):
    for _ in range(36):
        response = await client.oks.get_project(GetProjectRequest(project_id=project_id))
        project = response.project
        log_test_step(
            "OKS project {} status={} (async)".format(project_id, project.status)
        )
        if project.status == PROJECT_READY_STATUS:
            return project
        await asyncio.sleep(10)

    raise AssertionError("OKS project {} did not become ready".format(project_id))


async def delete_project_when_ready(client, project_id):
    for _ in range(36):
        try:
            delete_response = await client.oks.delete_project(
                DeleteProjectRequest(project_id=project_id)
            )
            log_test_step("Deleted OKS project {} (async)".format(project_id))
            return delete_response
        except httpx.HTTPStatusError as err:
            if err.response is None or err.response.status_code != 503:
                raise
            log_test_step(
                "OKS project {} is not ready for deletion yet (async)".format(
                    project_id
                )
            )
            await asyncio.sleep(10)

    raise AssertionError("OKS project {} could not be deleted".format(project_id))


class TestAsyncOksProject(unittest.TestCase):
    def test_project_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                project_id = None
                project_name = get_tagged_name("osc-sdk-python-oks-project")
                updated_description = "Updated OKS project lifecycle test"

                try:
                    log_test_step("Reading OKS project template (async)")
                    template_response = await client.oks.get_project_template(
                        GetProjectTemplateRequest()
                    )
                    self.assertIsInstance(template_response, TemplateResponse_ProjectInput)
                    project_input = template_response.template.model_copy(
                        update={
                            "name": project_name,
                            "description": "OKS project lifecycle test",
                            "tags": {"Name": project_name},
                        }
                    )
                    self.assertIsInstance(project_input, ProjectInput)

                    log_test_step("Creating OKS project {} (async)".format(project_name))
                    create_response = await client.oks.create_project(
                        CreateProjectRequest(body=project_input)
                    )
                    self.assertIsInstance(create_response, ProjectResponse)
                    project = create_response.project
                    self.assertIsInstance(project, Project)
                    project_id = project.id
                    self.assertTrue(project_id)
                    self.assertEqual(project.name, project_name)
                    log_test_step("Created OKS project {} (async)".format(project_id))

                    log_test_step("Reading OKS project {} (async)".format(project_id))
                    get_response = await client.oks.get_project(
                        GetProjectRequest(project_id=project_id)
                    )
                    self.assertIsInstance(get_response, ProjectResponse)
                    read_project = get_response.project
                    self.assertIsInstance(read_project, Project)
                    self.assertEqual(read_project.id, project_id)
                    self.assertEqual(read_project.name, project_name)

                    read_project = await wait_project_ready(client, project_id)
                    self.assertEqual(read_project.id, project_id)
                    self.assertEqual(read_project.name, project_name)

                    log_test_step("Updating OKS project {} (async)".format(project_id))
                    update_response = await client.oks.update_project(
                        UpdateProjectRequest(
                            project_id=project_id,
                            body=ProjectUpdate(
                                description=updated_description,
                                tags={"Name": project_name, "Updated": "true"},
                            ),
                        )
                    )
                    self.assertIsInstance(update_response, ProjectResponse)
                    updated_project = update_response.project
                    self.assertIsInstance(updated_project, Project)
                    self.assertEqual(updated_project.id, project_id)
                    self.assertEqual(updated_project.name, project_name)
                    self.assertEqual(updated_project.description, updated_description)
                finally:
                    if project_id:
                        log_test_step("Deleting OKS project {} (async)".format(project_id))
                        delete_response = await delete_project_when_ready(
                            client, project_id
                        )
                        self.assertIsInstance(delete_response, DetailResponse)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
