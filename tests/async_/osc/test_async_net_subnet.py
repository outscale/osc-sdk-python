import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    CreateNetRequest,
    CreateNetResponse,
    CreateSubnetRequest,
    CreateSubnetResponse,
    DeleteNetRequest,
    DeleteSubnetRequest,
    Net,
    ReadSubnetsRequest,
    Subnet,
    UpdateSubnetRequest,
    UpdateSubnetResponse,
)
from tests.async_.osc.async_integration_utils import (
    build_name_tag_typed_request,
    log_test_step,
    read_single_resource,
)


class TestAsyncNetAndSubnet(unittest.TestCase):
    def test_net_and_subnet_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                net_id = None
                subnet_id = None
                try:
                    log_test_step("Creating net 10.0.0.0/16 (async)")
                    net_response = await client.osc.create_net(
                        CreateNetRequest(ip_range="10.0.0.0/16")
                    )
                    self.assertIsInstance(net_response, CreateNetResponse)
                    net = net_response.net
                    self.assertIsInstance(net, Net)
                    net_id = net.net_id
                    self.assertTrue(net_id)
                    log_test_step("Created net {} (async)".format(net_id))

                    await client.osc.create_tags(build_name_tag_typed_request(net_id))
                    await asyncio.sleep(2)

                    log_test_step("Creating subnet 10.0.1.0/24 in {} (async)".format(net_id))
                    subnet_response = await client.osc.create_subnet(
                        CreateSubnetRequest(net_id=net_id, ip_range="10.0.1.0/24")
                    )
                    self.assertIsInstance(subnet_response, CreateSubnetResponse)
                    subnet = subnet_response.subnet
                    self.assertIsInstance(subnet, Subnet)
                    subnet_id = subnet.subnet_id
                    self.assertTrue(subnet_id)
                    log_test_step("Created subnet {} (async)".format(subnet_id))

                    await client.osc.create_tags(build_name_tag_typed_request(subnet_id))
                    await asyncio.sleep(2)

                    log_test_step("Reading subnet {} (async)".format(subnet_id))
                    subnet = await read_single_resource(
                        client,
                        "read_subnets",
                        ReadSubnetsRequest,
                        "subnets",
                        "SubnetIds",
                        subnet_id,
                    )
                    self.assertIsInstance(subnet, Subnet)
                    self.assertEqual(subnet.subnet_id, subnet_id)
                    self.assertTrue(
                        any(tag.key == "Name" for tag in subnet.tags or []),
                        "expected a Name tag on the subnet",
                    )

                    log_test_step("Updating subnet {} (async)".format(subnet_id))
                    updated = await client.osc.update_subnet(
                        UpdateSubnetRequest(
                            subnet_id=subnet_id,
                            map_public_ip_on_launch=False,
                        )
                    )
                    self.assertIsInstance(updated, UpdateSubnetResponse)
                    self.assertIsInstance(updated.subnet, Subnet)
                finally:
                    if subnet_id:
                        log_test_step("Deleting subnet {} (async)".format(subnet_id))
                        await client.osc.delete_subnet(
                            DeleteSubnetRequest(subnet_id=subnet_id)
                        )
                    if net_id:
                        log_test_step("Deleting net {} (async)".format(net_id))
                        await client.osc.delete_net(DeleteNetRequest(net_id=net_id))

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
