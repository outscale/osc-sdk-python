import sys
import time
import unittest

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import (
    build_name_tag_request,
    get_first_subregion_name,
    get_latest_public_ubuntu_image_id,
    get_linux_http_user_data,
    get_tagged_name,
    log_test_step,
    read_single_resource,
)


class TestLoadBalancerBackend(unittest.TestCase):
    def test_load_balancer_backend_lifecycle(self):
        gw = Gateway()
        subregion_name = get_first_subregion_name(gw)
        image_id = get_latest_public_ubuntu_image_id(gw)
        log_test_step("Using subregion {} and image {}".format(subregion_name, image_id))
        vm_id = None
        load_balancer_name = get_tagged_name("osc-sdk-python-lb")
        load_balancer_created = False
        try:
            log_test_step("Creating backend VM")
            vm_response = gw.CreateVms(
                ImageId=image_id,
                MinVmsCount=1,
                MaxVmsCount=1,
                Placement={"SubregionName": subregion_name, "Tenancy": "default"},
                UserData=get_linux_http_user_data(),
                VmType="tinav6.c1r1p2",
            )
            vms = vm_response.get("Vms")
            self.assertIsInstance(vms, list)
            self.assertEqual(len(vms), 1)
            vm_id = vms[0].get("VmId")
            self.assertTrue(vm_id)
            log_test_step("Created backend VM {}".format(vm_id))

            gw.CreateTags(**build_name_tag_request(vm_id))
            log_test_step("Tagged backend VM {}".format(vm_id))

            for _ in range(36):
                vm = read_single_resource(gw, "ReadVms", "Vms", "VmIds", vm_id)
                log_test_step("VM {} state={}".format(vm_id, vm.get("State")))
                if vm.get("State") == "running":
                    break
                if vm.get("State") in ("stopped", "terminated", "shutting-down"):
                    self.fail("VM {} entered unexpected state {}".format(vm_id, vm.get("State")))
                time.sleep(10)

            log_test_step("Creating load balancer {}".format(load_balancer_name))
            load_balancer_response = gw.CreateLoadBalancer(
                LoadBalancerName=load_balancer_name,
                Listeners=[
                    {
                        "BackendPort": 80,
                        "LoadBalancerPort": 80,
                        "LoadBalancerProtocol": "TCP",
                        "BackendProtocol": "TCP",
                    }
                ],
                SubregionNames=[subregion_name],
                Tags=[{"Key": "Name", "Value": get_tagged_name("osc-sdk-python-lb-tag")}],
            )
            self.assertIsInstance(load_balancer_response.get("LoadBalancer"), dict)
            load_balancer_created = True

            log_test_step("Linking backend VM {} to {}".format(vm_id, load_balancer_name))
            gw.LinkLoadBalancerBackendMachines(
                LoadBalancerName=load_balancer_name, BackendVmIds=[vm_id]
            )

            log_test_step("Reading load balancer {}".format(load_balancer_name))
            read_balancers = gw.ReadLoadBalancers(
                Filters={"LoadBalancerNames": [load_balancer_name]}
            )
            balancers = read_balancers.get("LoadBalancers")
            self.assertIsInstance(balancers, list)
            self.assertEqual(len(balancers), 1)
            self.assertIn(vm_id, balancers[0].get("BackendVmIds", []))

            health = None
            for _ in range(18):
                health = gw.ReadVmsHealth(
                    LoadBalancerName=load_balancer_name, BackendVmIds=[vm_id]
                )
                entry_count = len(health.get("BackendVmHealth", []) or [])
                log_test_step(
                    "Backend health entries for {}: {}".format(
                        load_balancer_name, entry_count
                    )
                )
                if any(
                    entry.get("VmId") == vm_id
                    for entry in health.get("BackendVmHealth", []) or []
                ):
                    break
                time.sleep(10)

            self.assertIsNotNone(health)
            self.assertTrue(
                any(
                    entry.get("VmId") == vm_id
                    for entry in health.get("BackendVmHealth", []) or []
                )
            )
            log_test_step("Backend VM {} is registered in {}".format(vm_id, load_balancer_name))
        finally:
            if load_balancer_created:
                log_test_step("Deleting load balancer {}".format(load_balancer_name))
                gw.DeleteLoadBalancer(LoadBalancerName=load_balancer_name)
            if vm_id:
                time.sleep(1)
                log_test_step("Deleting backend VM {}".format(vm_id))
                gw.DeleteVms(VmIds=[vm_id])


if __name__ == "__main__":
    unittest.main()
