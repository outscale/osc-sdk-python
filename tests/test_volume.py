import unittest
import sys
import time

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import (
    create_name_tag,
    first_subregion_name,
    log_step,
    read_single,
)


class TestVolume(unittest.TestCase):
    def test_listing(self):
        gw = Gateway()
        volumes = gw.ReadVolumes()
        self.assertEqual(type(volumes), dict)
        self.assertEqual(type(volumes.get("Volumes")), list)

    def test_volume_lifecycle(self):
        gw = Gateway()
        subregion_name = first_subregion_name(gw)
        log_step("Using subregion {}".format(subregion_name))
        volume_id = None
        try:
            log_step("Creating volume")
            response = gw.CreateVolume(Size=10, SubregionName=subregion_name)
            volume = response.get("Volume")
            self.assertIsInstance(volume, dict)
            volume_id = volume.get("VolumeId")
            self.assertTrue(volume_id)
            log_step("Created volume {}".format(volume_id))

            gw.CreateTags(**create_name_tag(volume_id))
            log_step("Tagged volume {}".format(volume_id))

            volume = None
            for _ in range(30):
                volume = read_single(gw, "ReadVolumes", "Volumes", "VolumeIds", volume_id)
                log_step("Volume {} state={}".format(volume_id, volume.get("State")))
                if volume.get("State") == "available":
                    break
                if volume.get("State") == "error":
                    self.fail(
                        "Volume {} entered unexpected state {}".format(
                            volume_id, volume.get("State")
                        )
                    )
                time.sleep(10)

            self.assertIsNotNone(volume)

            # volume = wait_until(
            #     fetch=lambda: read_single(gw, "ReadVolumes", "Volumes", "VolumeIds", volume_id),
            #     ready=lambda item: item.get("State") == "available",
            #     timeout=300,
            #     interval=10,
            #     failure=lambda item: item.get("State") == "error",
            #     describe=lambda item: "Volume {} state={}".format(
            #         volume_id, item.get("State")
            #     ),
            # )

            self.assertEqual(volume.get("State"), "available")
            self.assertTrue(
                any(tag.get("Key") == "Name" for tag in volume.get("Tags", [])),
                "expected a Name tag on the volume",
            )
            log_step("Volume {} is available".format(volume_id))
        finally:
            if volume_id:
                time.sleep(1)
                log_step("Deleting volume {}".format(volume_id))
                gw.DeleteVolume(VolumeId=volume_id)


if __name__ == "__main__":
    unittest.main()
