import asyncio
import sys
import unittest

sys.path.append("..")
from osc_sdk_python import AsyncClient
from tests.integration_utils import get_tagged_name, log_test_step


class TestAsyncSecurityGroup(unittest.TestCase):
    def test_security_group_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                security_group_id = None
                tcp = "tcp"
                ip_range = "0.0.0.0/0"
                try:
                    log_test_step("Creating security group (async)")
                    response = await client.osc.CreateSecurityGroup(
                        SecurityGroupName=get_tagged_name("osc-sdk-python-sg-async"),
                        Description="Test security group lifecycle async",
                    )
                    security_group = response.get("SecurityGroup")
                    self.assertIsInstance(security_group, dict)
                    security_group_id = security_group.get("SecurityGroupId")
                    self.assertTrue(security_group_id)
                    log_test_step("Created security group {} (async)".format(security_group_id))

                    log_test_step("Creating inbound SSH rule on {} (async)".format(security_group_id))
                    rule_response = await client.osc.CreateSecurityGroupRule(
                        SecurityGroupId=security_group_id,
                        Flow="Inbound",
                        IpProtocol=tcp,
                        FromPortRange=22,
                        ToPortRange=22,
                        IpRange=ip_range,
                    )
                    self.assertIsInstance(rule_response.get("SecurityGroup"), dict)

                    log_test_step("Reading security group {} (async)".format(security_group_id))
                    read_response = await client.osc.ReadSecurityGroups(
                        Filters={"SecurityGroupIds": [security_group_id]}
                    )
                    security_groups = read_response.get("SecurityGroups")
                    self.assertIsInstance(security_groups, list)
                    self.assertEqual(len(security_groups), 1)

                    rules = security_groups[0].get("InboundRules", [])
                    self.assertTrue(
                        any(
                            rule.get("FromPortRange") == 22
                            and rule.get("ToPortRange") == 22
                            and rule.get("IpProtocol") == tcp
                            and ip_range in rule.get("IpRanges", [])
                            for rule in rules
                        ),
                        "expected SSH inbound rule on the security group",
                    )

                    log_test_step("Deleting inbound SSH rule on {} (async)".format(security_group_id))
                    await client.osc.DeleteSecurityGroupRule(
                        SecurityGroupId=security_group_id,
                        Flow="Inbound",
                        IpProtocol=tcp,
                        FromPortRange=22,
                        ToPortRange=22,
                        IpRange=ip_range,
                    )
                finally:
                    if security_group_id:
                        log_test_step("Deleting security group {} (async)".format(security_group_id))
                        await client.osc.DeleteSecurityGroup(SecurityGroupId=security_group_id)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()