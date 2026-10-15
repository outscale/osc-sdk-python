import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    BackendVmHealth,
    CreateLoadBalancerRequest,
    CreateLoadBalancerResponse,
    CreateVmsRequest,
    CreateVmsResponse,
    DeleteLoadBalancerRequest,
    DeleteVmsRequest,
    LinkLoadBalancerBackendMachinesRequest,
    LoadBalancer,
    ReadLoadBalancersRequest,
    ReadLoadBalancersResponse,
    ReadVmsHealthRequest,
    ReadVmsHealthResponse,
    ReadVmsRequest,
    Vm,
)
from tests.integration.async_.helpers.async_integration_utils import (
    build_name_tag_typed_request,
    get_first_subregion_name,
    get_latest_public_ubuntu_image_id,
    get_linux_http_user_data,
    get_tagged_name,
    log_test_step,
    read_single_resource,
)


class TestAsyncLoadBalancerBackend(unittest.TestCase):
    def test_load_balancer_backend_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                subregion_name = await get_first_subregion_name(client)
                image_id = await get_latest_public_ubuntu_image_id(client)
                log_test_step(
                    f"Using subregion {subregion_name} and image {image_id} (async)"
                )
                vm_id = None
                load_balancer_name = get_tagged_name("osc-sdk-python-lb")
                load_balancer_created = False
                try:
                    log_test_step("Creating backend VM (async)")
                    vm_response = await client.osc.create_vms(
                        CreateVmsRequest(
                            image_id=image_id,
                            min_vms_count=1,
                            max_vms_count=1,
                            placement={
                                "SubregionName": subregion_name,
                                "Tenancy": "default",
                            },
                            user_data=get_linux_http_user_data(),
                            vm_type="tinav6.c1r1p2",
                        )
                    )
                    self.assertIsInstance(vm_response, CreateVmsResponse)
                    vms = vm_response.vms
                    self.assertIsInstance(vms, list)
                    self.assertEqual(len(vms), 1)
                    self.assertIsInstance(vms[0], Vm)
                    vm_id = vms[0].vm_id
                    self.assertTrue(vm_id)
                    log_test_step(f"Created backend VM {vm_id} (async)")

                    await client.osc.create_tags(build_name_tag_typed_request(vm_id))
                    log_test_step(f"Tagged backend VM {vm_id} (async)")

                    for _ in range(36):
                        vm = await read_single_resource(
                            client,
                            "read_vms",
                            ReadVmsRequest,
                            "vms",
                            "VmIds",
                            vm_id,
                        )
                        self.assertIsInstance(vm, Vm)
                        log_test_step(f"VM {vm_id} state={vm.state} (async)")
                        if vm.state == "running":
                            break
                        if vm.state in ("stopped", "terminated", "shutting-down"):
                            self.fail(f"VM {vm_id} entered unexpected state {vm.state}")
                        await asyncio.sleep(10)

                    log_test_step(
                        f"Creating load balancer {load_balancer_name} (async)"
                    )
                    load_balancer_response = await client.osc.create_load_balancer(
                        CreateLoadBalancerRequest(
                            load_balancer_name=load_balancer_name,
                            listeners=[
                                {
                                    "BackendPort": 80,
                                    "LoadBalancerPort": 80,
                                    "LoadBalancerProtocol": "TCP",
                                    "BackendProtocol": "TCP",
                                }
                            ],
                            subregion_names=[subregion_name],
                            tags=[
                                {
                                    "Key": "Name",
                                    "Value": get_tagged_name(
                                        "osc-sdk-python-lb-tag-async"
                                    ),
                                }
                            ],
                        )
                    )
                    self.assertIsInstance(
                        load_balancer_response, CreateLoadBalancerResponse
                    )
                    self.assertIsInstance(
                        load_balancer_response.load_balancer, LoadBalancer
                    )
                    load_balancer_created = True

                    log_test_step(
                        f"Linking backend VM {vm_id} to {load_balancer_name} (async)"
                    )
                    await client.osc.link_load_balancer_backend_machines(
                        LinkLoadBalancerBackendMachinesRequest(
                            load_balancer_name=load_balancer_name,
                            backend_vm_ids=[vm_id],
                        )
                    )

                    log_test_step(f"Reading load balancer {load_balancer_name} (async)")
                    read_balancers = await client.osc.read_load_balancers(
                        ReadLoadBalancersRequest(
                            filters={"LoadBalancerNames": [load_balancer_name]}
                        )
                    )
                    self.assertIsInstance(read_balancers, ReadLoadBalancersResponse)
                    balancers = read_balancers.load_balancers
                    self.assertIsInstance(balancers, list)
                    self.assertEqual(len(balancers), 1)
                    self.assertIsInstance(balancers[0], LoadBalancer)
                    self.assertIn(vm_id, balancers[0].backend_vm_ids or [])

                    health = None
                    for _ in range(18):
                        health = await client.osc.read_vms_health(
                            ReadVmsHealthRequest(
                                load_balancer_name=load_balancer_name,
                                backend_vm_ids=[vm_id],
                            )
                        )
                        self.assertIsInstance(health, ReadVmsHealthResponse)
                        entry_count = len(health.backend_vm_health or [])
                        if health.backend_vm_health:
                            self.assertIsInstance(
                                health.backend_vm_health[0], BackendVmHealth
                            )
                        log_test_step(
                            f"Backend health entries for {load_balancer_name}: {entry_count} (async)"
                        )
                        if any(
                            entry.vm_id == vm_id
                            for entry in health.backend_vm_health or []
                        ):
                            break
                        await asyncio.sleep(10)

                    self.assertIsNotNone(health)
                    self.assertTrue(
                        any(
                            entry.vm_id == vm_id
                            for entry in health.backend_vm_health or []
                        )
                    )
                    log_test_step(
                        f"Backend VM {vm_id} is registered in {load_balancer_name} (async)"
                    )
                finally:
                    if load_balancer_created:
                        log_test_step(
                            f"Deleting load balancer {load_balancer_name} (async)"
                        )
                        await client.osc.delete_load_balancer(
                            DeleteLoadBalancerRequest(
                                load_balancer_name=load_balancer_name
                            )
                        )
                    if vm_id:
                        await asyncio.sleep(1)
                        log_test_step(f"Deleting backend VM {vm_id} (async)")
                        await client.osc.delete_vms(DeleteVmsRequest(vm_ids=[vm_id]))

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
