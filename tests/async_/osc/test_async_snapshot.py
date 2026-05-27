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
from tests.async_.osc.async_integration_utils import (
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
                log_test_step("Using subregion {} (async)".format(subregion_name))
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
                    log_test_step("Created volume {} (async)".format(volume_id))

                    await client.osc.create_tags(build_name_tag_typed_request(volume_id))
                    log_test_step("Tagged volume {} (async)".format(volume_id))

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
                            "Volume {} state={} (async)".format(
                                volume_id, volume.state
                            )
                        )
                        if volume.state == "available":
                            break
                        if volume.state == "error":
                            self.fail(
                                "Volume {} entered unexpected state {}".format(
                                    volume_id, volume.state
                                )
                            )
                        await asyncio.sleep(10)

                    log_test_step(
                        "Creating snapshot from volume {} (async)".format(volume_id)
                    )
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
                    log_test_step("Created snapshot {} (async)".format(snapshot_id))

                    await client.osc.create_tags(build_name_tag_typed_request(snapshot_id))
                    log_test_step("Tagged snapshot {} (async)".format(snapshot_id))

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
                            "Snapshot {} state={} (async)".format(
                                snapshot_id, snapshot.state
                            )
                        )
                        if snapshot.state == "completed":
                            break
                        if snapshot.state == "error":
                            self.fail(
                                "Snapshot {} entered unexpected state {}".format(
                                    snapshot_id, snapshot.state
                                )
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
                    log_test_step(
                        "Snapshot {} is completed (async)".format(snapshot_id)
                    )
                finally:
                    if snapshot_id:
                        log_test_step("Deleting snapshot {} (async)".format(snapshot_id))
                        await client.osc.delete_snapshot(
                            DeleteSnapshotRequest(snapshot_id=snapshot_id)
                        )
                    if volume_id:
                        await asyncio.sleep(1)
                        log_test_step("Deleting volume {} (async)".format(volume_id))
                        await client.osc.delete_volume(
                            DeleteVolumeRequest(volume_id=volume_id)
                        )

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
