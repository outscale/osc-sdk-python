import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    CreateSecurityGroupRequest,
    CreateSecurityGroupResponse,
    CreateSecurityGroupRuleRequest,
    CreateSecurityGroupRuleResponse,
    DeleteSecurityGroupRequest,
    DeleteSecurityGroupRuleRequest,
    ReadSecurityGroupsRequest,
    ReadSecurityGroupsResponse,
    SecurityGroup,
)
from tests.async_.osc.async_integration_utils import get_tagged_name, log_test_step


class TestAsyncSecurityGroup(unittest.TestCase):
    def test_security_group_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                security_group_id = None
                tcp = "tcp"
                ip_range = "0.0.0.0/0"
                try:
                    log_test_step("Creating security group (async)")
                    response = await client.osc.create_security_group(
                        CreateSecurityGroupRequest(
                            security_group_name=get_tagged_name(
                                "osc-sdk-python-sg-async"
                            ),
                            description="Test security group lifecycle async",
                        )
                    )
                    self.assertIsInstance(response, CreateSecurityGroupResponse)
                    security_group = response.security_group
                    self.assertIsInstance(security_group, SecurityGroup)
                    security_group_id = security_group.security_group_id
                    self.assertTrue(security_group_id)
                    log_test_step(
                        "Created security group {} (async)".format(security_group_id)
                    )

                    log_test_step(
                        "Creating inbound SSH rule on {} (async)".format(
                            security_group_id
                        )
                    )
                    rule_response = await client.osc.create_security_group_rule(
                        CreateSecurityGroupRuleRequest(
                            security_group_id=security_group_id,
                            flow="Inbound",
                            ip_protocol=tcp,
                            from_port_range=22,
                            to_port_range=22,
                            ip_range=ip_range,
                        )
                    )
                    self.assertIsInstance(rule_response, CreateSecurityGroupRuleResponse)
                    self.assertIsInstance(rule_response.security_group, SecurityGroup)

                    log_test_step(
                        "Reading security group {} (async)".format(security_group_id)
                    )
                    read_response = await client.osc.read_security_groups(
                        ReadSecurityGroupsRequest(
                            filters={"SecurityGroupIds": [security_group_id]}
                        )
                    )
                    self.assertIsInstance(read_response, ReadSecurityGroupsResponse)
                    security_groups = read_response.security_groups
                    self.assertIsInstance(security_groups, list)
                    self.assertEqual(len(security_groups), 1)
                    self.assertIsInstance(security_groups[0], SecurityGroup)

                    rules = security_groups[0].inbound_rules or []
                    self.assertTrue(
                        any(
                            rule.from_port_range == 22
                            and rule.to_port_range == 22
                            and rule.ip_protocol == tcp
                            and ip_range in (rule.ip_ranges or [])
                            for rule in rules
                        ),
                        "expected SSH inbound rule on the security group",
                    )

                    log_test_step(
                        "Deleting inbound SSH rule on {} (async)".format(
                            security_group_id
                        )
                    )
                    await client.osc.delete_security_group_rule(
                        DeleteSecurityGroupRuleRequest(
                            security_group_id=security_group_id,
                            flow="Inbound",
                            ip_protocol=tcp,
                            from_port_range=22,
                            to_port_range=22,
                            ip_range=ip_range,
                        )
                    )
                finally:
                    if security_group_id:
                        log_test_step(
                            "Deleting security group {} (async)".format(
                                security_group_id
                            )
                        )
                        await client.osc.delete_security_group(
                            DeleteSecurityGroupRequest(
                                security_group_id=security_group_id
                            )
                        )

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
