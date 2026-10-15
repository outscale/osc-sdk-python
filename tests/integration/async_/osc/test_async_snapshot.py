import asyncio
import unittest

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import (
    CreateSnapshotRequest,
    CreateSnapshotResponse,
    CreateVolumeRequest,
    CreateVolumeResponse,
    DeleteSnapshotRequest,
    DeleteVolumeRequest,
    ReadSnapshotsRequest,
    ReadVolumesRequest,
    Snapshot,
    Volume,
)
from tests.integration.async_.helpers.async_integration_utils import (
    build_name_tag_typed_request,
    get_first_subregion_name,
    get_tagged_name,
    log_test_step,
    read_single_resource,
)


class TestAsyncSnapshot(unittest.TestCase):
    def test_snapshot_lifecycle(self):
        async def run():
            async with AsyncClient() as client:
                subregion_name = await get_first_subregion_name(client)
                log_test_step(f"Using subregion {subregion_name} (async)")
                volume_id = None
                snapshot_id = None
                description = get_tagged_name("osc-sdk-python-snapshot-async")
                try:
                    log_test_step("Creating source volume (async)")
                    volume_response = await client.osc.create_volume(
                        CreateVolumeRequest(size=10, subregion_name=subregion_name)
                    )
                    self.assertIsInstance(volume_response, CreateVolumeResponse)
                    volume = volume_response.volume
                    self.assertIsInstance(volume, Volume)
                    volume_id = volume.volume_id
                    self.assertTrue(volume_id)
                    log_test_step(f"Created volume {volume_id} (async)")

                    await client.osc.create_tags(
                        build_name_tag_typed_request(volume_id)
                    )
                    log_test_step(f"Tagged volume {volume_id} (async)")

                    for _ in range(30):
                        volume = await read_single_resource(
                            client,
                            "read_volumes",
                            ReadVolumesRequest,
                            "volumes",
                            "VolumeIds",
                            volume_id,
                        )
                        self.assertIsInstance(volume, Volume)
                        log_test_step(
                            f"Volume {volume_id} state={volume.state} (async)"
                        )
                        if volume.state == "available":
                            break
                        if volume.state == "error":
                            self.fail(
                                f"Volume {volume_id} entered unexpected state {volume.state}"
                            )
                        await asyncio.sleep(10)

                    log_test_step(f"Creating snapshot from volume {volume_id} (async)")
                    snapshot_response = await client.osc.create_snapshot(
                        CreateSnapshotRequest(
                            description=description,
                            volume_id=volume_id,
                        )
                    )
                    self.assertIsInstance(snapshot_response, CreateSnapshotResponse)
                    snapshot = snapshot_response.snapshot
                    self.assertIsInstance(snapshot, Snapshot)
                    snapshot_id = snapshot.snapshot_id
                    self.assertTrue(snapshot_id)
                    log_test_step(f"Created snapshot {snapshot_id} (async)")

                    await client.osc.create_tags(
                        build_name_tag_typed_request(snapshot_id)
                    )
                    log_test_step(f"Tagged snapshot {snapshot_id} (async)")

                    snapshot = None
                    for _ in range(60):
                        snapshot = await read_single_resource(
                            client,
                            "read_snapshots",
                            ReadSnapshotsRequest,
                            "snapshots",
                            "SnapshotIds",
                            snapshot_id,
                        )
                        self.assertIsInstance(snapshot, Snapshot)
                        log_test_step(
                            f"Snapshot {snapshot_id} state={snapshot.state} (async)"
                        )
                        if snapshot.state == "completed":
                            break
                        if snapshot.state == "error":
                            self.fail(
                                f"Snapshot {snapshot_id} entered unexpected state {snapshot.state}"
                            )
                        await asyncio.sleep(10)

                    self.assertIsNotNone(snapshot)
                    self.assertIsInstance(snapshot, Snapshot)
                    self.assertEqual(snapshot.snapshot_id, snapshot_id)
                    self.assertEqual(snapshot.volume_id, volume_id)
                    self.assertEqual(snapshot.description, description)
                    self.assertTrue(
                        any(tag.key == "Name" for tag in snapshot.tags or []),
                        "expected a Name tag on the snapshot",
                    )
                    log_test_step(f"Snapshot {snapshot_id} is completed (async)")
                finally:
                    if snapshot_id:
                        log_test_step(f"Deleting snapshot {snapshot_id} (async)")
                        await client.osc.delete_snapshot(
                            DeleteSnapshotRequest(snapshot_id=snapshot_id)
                        )
                    if volume_id:
                        await asyncio.sleep(1)
                        log_test_step(f"Deleting volume {volume_id} (async)")
                        await client.osc.delete_volume(
                            DeleteVolumeRequest(volume_id=volume_id)
                        )

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
