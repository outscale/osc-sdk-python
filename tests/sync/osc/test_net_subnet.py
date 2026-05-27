import sys
import time
import unittest

sys.path.append("..")
from osc_sdk_python import Client
from tests.integration_utils import (
    build_name_tag_request,
    log_test_step,
    read_single_resource,
)


class TestNetAndSubnet(unittest.TestCase):
    def test_net_and_subnet_lifecycle(self):
        client = Client()
        osc = client.osc
        net_id = None
        subnet_id = None
        try:
            log_test_step("Creating net 10.0.0.0/16")
            net_response = osc.CreateNet(IpRange="10.0.0.0/16")
            net = net_response.get("Net")
            self.assertIsInstance(net, dict)
            net_id = net.get("NetId")
            self.assertTrue(net_id)
            log_test_step("Created net {}".format(net_id))

            osc.CreateTags(**build_name_tag_request(net_id))
            time.sleep(2)

            log_test_step("Creating subnet 10.0.1.0/24 in {}".format(net_id))
            subnet_response = osc.CreateSubnet(NetId=net_id, IpRange="10.0.1.0/24")
            subnet = subnet_response.get("Subnet")
            self.assertIsInstance(subnet, dict)
            subnet_id = subnet.get("SubnetId")
            self.assertTrue(subnet_id)
            log_test_step("Created subnet {}".format(subnet_id))

            osc.CreateTags(**build_name_tag_request(subnet_id))
            time.sleep(2)

            log_test_step("Reading subnet {}".format(subnet_id))
            subnet = read_single_resource(osc, "ReadSubnets", "Subnets", "SubnetIds", subnet_id)
            self.assertEqual(subnet.get("SubnetId"), subnet_id)
            self.assertTrue(
                any(tag.get("Key") == "Name" for tag in subnet.get("Tags", [])),
                "expected a Name tag on the subnet",
            )

            log_test_step("Updating subnet {}".format(subnet_id))
            updated = osc.UpdateSubnet(SubnetId=subnet_id, MapPublicIpOnLaunch=False)
            self.assertIsInstance(updated.get("Subnet"), dict)
        finally:
            if subnet_id:
                log_test_step("Deleting subnet {}".format(subnet_id))
                osc.DeleteSubnet(SubnetId=subnet_id)
            if net_id:
                log_test_step("Deleting net {}".format(net_id))
                osc.DeleteNet(NetId=net_id)
            client.close()


if __name__ == "__main__":
    unittest.main()
