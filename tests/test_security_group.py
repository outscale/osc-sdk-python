import sys
import unittest

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import get_tagged_name, log_test_step


class TestSecurityGroup(unittest.TestCase):
    def test_security_group_lifecycle(self):
        gw = Gateway()
        security_group_id = None
        tcp = "tcp"
        ip_range = "0.0.0.0/0"
        try:
            log_test_step("Creating security group")
            response = gw.CreateSecurityGroup(
                SecurityGroupName=get_tagged_name("osc-sdk-python-sg"),
                Description="Test security group lifecycle",
            )
            security_group = response.get("SecurityGroup")
            self.assertIsInstance(security_group, dict)
            security_group_id = security_group.get("SecurityGroupId")
            self.assertTrue(security_group_id)
            log_test_step("Created security group {}".format(security_group_id))

            log_test_step("Creating inbound SSH rule on {}".format(security_group_id))
            rule_response = gw.CreateSecurityGroupRule(
                SecurityGroupId=security_group_id,
                Flow="Inbound",
                IpProtocol=tcp,
                FromPortRange=22,
                ToPortRange=22,
                IpRange=ip_range,
            )
            self.assertIsInstance(rule_response.get("SecurityGroup"), dict)

            log_test_step("Reading security group {}".format(security_group_id))
            read_response = gw.ReadSecurityGroups(
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

            log_test_step("Deleting inbound SSH rule on {}".format(security_group_id))
            gw.DeleteSecurityGroupRule(
                SecurityGroupId=security_group_id,
                Flow="Inbound",
                IpProtocol=tcp,
                FromPortRange=22,
                ToPortRange=22,
                IpRange=ip_range,
            )
        finally:
            if security_group_id:
                log_test_step("Deleting security group {}".format(security_group_id))
                gw.DeleteSecurityGroup(SecurityGroupId=security_group_id)


if __name__ == "__main__":
    unittest.main()
