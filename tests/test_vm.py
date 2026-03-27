import unittest
import sys
import time

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import (
    build_name_tag_request,
    get_first_subregion_name,
    get_latest_public_ubuntu_image_id,
    log_test_step,
    read_single_resource,
)


class TestVm(unittest.TestCase):
    def test_listing(self):
        gw = Gateway()
        vms = gw.ReadVms()
        self.assertEqual(type(vms), dict)
        self.assertEqual(type(vms.get("Vms")), list)

    def test_listing_with_context_manager(self):
        with Gateway() as gw:
            vms = gw.ReadVms()
            self.assertEqual(type(vms), dict)
            self.assertEqual(type(vms.get("Vms")), list)

    def test_vm_lifecycle(self):
        gw = Gateway()
        subregion_name = get_first_subregion_name(gw)
        image_id = get_latest_public_ubuntu_image_id(gw)
        log_test_step("Using subregion {} and image {}".format(subregion_name, image_id))

        created_vm_ids = []
        try:
            log_test_step("Creating VM")
            response = gw.CreateVms(
                ImageId=image_id,
                MinVmsCount=1,
                MaxVmsCount=1,
                Placement={"SubregionName": subregion_name, "Tenancy": "default"},
                VmType="tinav4.c1r1p2",
            )
            vms = response.get("Vms")
            self.assertIsInstance(vms, list)
            self.assertEqual(len(vms), 1)

            vm_id = vms[0].get("VmId")
            self.assertTrue(vm_id)
            created_vm_ids = [vm_id]
            log_test_step("Created VM {}".format(vm_id))

            gw.CreateTags(**build_name_tag_request(vm_id))
            log_test_step("Tagged VM {}".format(vm_id))

            vm = None
            for _ in range(36):
                vm = read_single_resource(gw, "ReadVms", "Vms", "VmIds", vm_id)
                log_test_step("VM {} state={}".format(vm_id, vm.get("State")))
                if vm.get("State") == "running":
                    break
                if vm.get("State") in ("terminated", "shutting-down"):
                    self.fail("VM {} entered unexpected state {}".format(vm_id, vm.get("State")))
                time.sleep(10)

            self.assertIsNotNone(vm)
            self.assertEqual(vm.get("State"), "running")

            self.assertEqual(vm.get("ImageId"), image_id)
            self.assertTrue(
                any(tag.get("Key") == "Name" for tag in vm.get("Tags", [])),
                "expected a Name tag on the VM",
            )
            log_test_step("VM {} is running".format(vm_id))
        finally:
            if created_vm_ids:
                time.sleep(1)
                log_test_step("Deleting VM {}".format(created_vm_ids[0]))
                gw.DeleteVms(VmIds=created_vm_ids)


if __name__ == "__main__":
    unittest.main()
