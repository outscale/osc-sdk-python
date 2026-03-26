import sys
import time
import unittest

sys.path.append("..")
from osc_sdk_python import Gateway
from tests.integration_utils import (
    create_name_tag,
    first_subregion_name,
    log_step,
    read_single,
    tagged_name,
)


class TestSnapshot(unittest.TestCase):
    def test_snapshot_lifecycle(self):
        gw = Gateway()
        subregion_name = first_subregion_name(gw)
        log_step("Using subregion {}".format(subregion_name))
        volume_id = None
        snapshot_id = None
        description = tagged_name("osc-sdk-python-snapshot")
        try:
            log_step("Creating source volume")
            volume_response = gw.CreateVolume(Size=10, SubregionName=subregion_name)
            volume = volume_response.get("Volume")
            self.assertIsInstance(volume, dict)
            volume_id = volume.get("VolumeId")
            self.assertTrue(volume_id)
            log_step("Created volume {}".format(volume_id))

            gw.CreateTags(**create_name_tag(volume_id))
            log_step("Tagged volume {}".format(volume_id))

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

            log_step("Creating snapshot from volume {}".format(volume_id))
            snapshot_response = gw.CreateSnapshot(Description=description, VolumeId=volume_id)
            snapshot = snapshot_response.get("Snapshot")
            self.assertIsInstance(snapshot, dict)
            snapshot_id = snapshot.get("SnapshotId")
            self.assertTrue(snapshot_id)
            log_step("Created snapshot {}".format(snapshot_id))

            gw.CreateTags(**create_name_tag(snapshot_id))
            log_step("Tagged snapshot {}".format(snapshot_id))

            snapshot = None
            for _ in range(60):
                snapshot = read_single(gw, "ReadSnapshots", "Snapshots", "SnapshotIds", snapshot_id)
                log_step("Snapshot {} state={}".format(snapshot_id, snapshot.get("State")))
                if snapshot.get("State") == "completed":
                    break
                if snapshot.get("State") == "error":
                    self.fail(
                        "Snapshot {} entered unexpected state {}".format(
                            snapshot_id, snapshot.get("State")
                        )
                    )
                time.sleep(10)

            self.assertIsNotNone(snapshot)

            self.assertEqual(snapshot.get("SnapshotId"), snapshot_id)
            self.assertEqual(snapshot.get("VolumeId"), volume_id)
            self.assertEqual(snapshot.get("Description"), description)
            self.assertTrue(
                any(tag.get("Key") == "Name" for tag in snapshot.get("Tags", [])),
                "expected a Name tag on the snapshot",
            )
            log_step("Snapshot {} is completed".format(snapshot_id))
        finally:
            if snapshot_id:
                log_step("Deleting snapshot {}".format(snapshot_id))
                gw.DeleteSnapshot(SnapshotId=snapshot_id)
            if volume_id:
                time.sleep(1)
                log_step("Deleting volume {}".format(volume_id))
                gw.DeleteVolume(VolumeId=volume_id)


if __name__ == "__main__":
    unittest.main()
