import sys
import time
import unittest

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import create_name_tag, log_step, read_single


class TestNetAndSubnet(unittest.TestCase):
    def test_net_and_subnet_lifecycle(self):
        gw = Gateway()
        net_id = None
        subnet_id = None
        try:
            log_step("Creating net 10.0.0.0/16")
            net_response = gw.CreateNet(IpRange="10.0.0.0/16")
            net = net_response.get("Net")
            self.assertIsInstance(net, dict)
            net_id = net.get("NetId")
            self.assertTrue(net_id)
            log_step("Created net {}".format(net_id))

            gw.CreateTags(**create_name_tag(net_id))
            time.sleep(2)

            log_step("Creating subnet 10.0.1.0/24 in {}".format(net_id))
            subnet_response = gw.CreateSubnet(NetId=net_id, IpRange="10.0.1.0/24")
            subnet = subnet_response.get("Subnet")
            self.assertIsInstance(subnet, dict)
            subnet_id = subnet.get("SubnetId")
            self.assertTrue(subnet_id)
            log_step("Created subnet {}".format(subnet_id))

            gw.CreateTags(**create_name_tag(subnet_id))
            time.sleep(2)

            log_step("Reading subnet {}".format(subnet_id))
            subnet = read_single(gw, "ReadSubnets", "Subnets", "SubnetIds", subnet_id)
            self.assertEqual(subnet.get("SubnetId"), subnet_id)
            self.assertTrue(
                any(tag.get("Key") == "Name" for tag in subnet.get("Tags", [])),
                "expected a Name tag on the subnet",
            )

            log_step("Updating subnet {}".format(subnet_id))
            updated = gw.UpdateSubnet(SubnetId=subnet_id, MapPublicIpOnLaunch=False)
            self.assertIsInstance(updated.get("Subnet"), dict)
        finally:
            if subnet_id:
                log_step("Deleting subnet {}".format(subnet_id))
                gw.DeleteSubnet(SubnetId=subnet_id)
            if net_id:
                log_step("Deleting net {}".format(net_id))
                gw.DeleteNet(NetId=net_id)


if __name__ == "__main__":
    unittest.main()
