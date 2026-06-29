## 🚀 Usage

Basic usage with the default profile:

```python
from osc_sdk_python import Client

with Client() as client:
    # Example: list VMs
    vms = client.osc.ReadVms()
    print(vms)
```

Async usage with the default profile:

```python
import asyncio

from osc_sdk_python import AsyncClient


async def main():
    async with AsyncClient() as client:
        # Example: list VMs
        vms = await client.osc.read_vms()
        print(vms)


if __name__ == "__main__":
    asyncio.run(main())
```

Using a specific profile:

```python
from osc_sdk_python import Client

client = Client(profile="profile_1")
```

Using a specific profile with the async client:

```python
from osc_sdk_python import AsyncClient

client = AsyncClient(profile="profile_1")
```

Using multiple services from one client:

```python
from osc_sdk_python import Client

with Client(profile="profile_1") as client:
    vms = client.osc.ReadVms()
    projects = client.oks.ListProjects()
```

Using multiple services from one async client:

```python
import asyncio

from osc_sdk_python import AsyncClient


async def main():
    async with AsyncClient(profile="profile_1") as client:
        vms = await client.osc.read_vms()
        projects = await client.oks.list_projects()


if __name__ == "__main__":
    asyncio.run(main())
```

Calling actions:

* **Sync dynamic methods**: `client.osc.ReadVms(...)`, `client.osc.CreateVms(...)`, etc.
* **Raw calls**: `client.osc.raw("ActionName", **params)`
* **Async typed methods**: `await client.osc.read_vms(...)`, `await client.osc.create_vms(...)`, etc.
* **Async raw calls**: `await client.osc.raw("ActionName", **params)`

Typed request and response models under `osc_sdk_python.generated.*` are async-first today: generated typed methods are exposed on `AsyncClient` and use snake_case operation names. Synchronous callers should continue to use dynamic action methods such as `client.osc.ReadVms(...)` or raw calls such as `client.osc.raw("ReadVms", **params)`.

Example:

```python
from osc_sdk_python import Client

with Client(profile="profile_1") as client:
    # Calls with API action as method
    result = client.osc.ReadSecurityGroups(Filters={"SecurityGroupNames": ["default"]})
    result = client.osc.CreateVms(ImageId="ami-3e158364", VmType="tinav4.c2r4")

    # Or raw calls:
    result = client.osc.raw("ReadVms")
    result = client.osc.raw(
        "CreateVms",
        ImageId="ami-xx",
        BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
        SecurityGroupIds=["sg-aaa", "sg-bbb"],
        Wrong="wrong",
    )
```

Async example:

```python
import asyncio

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import CreateVmsRequest, ReadSecurityGroupsRequest


async def main():
    async with AsyncClient(profile="profile_1") as client:
        # Calls with operationId converted to snake_case
        result = await client.osc.read_security_groups(
            ReadSecurityGroupsRequest(filters={"SecurityGroupNames": ["default"]})
        )
        result = await client.osc.create_vms(
            CreateVmsRequest(image_id="ami-3e158364", vm_type="tinav4.c2r4")
        )

        # Or raw calls:
        result = await client.osc.raw("ReadVms")
        result = await client.osc.raw(
            "CreateVms",
            ImageId="ami-xx",
            BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
            SecurityGroupIds=["sg-aaa", "sg-bbb"],
            Wrong="wrong",
        )


if __name__ == "__main__":
    asyncio.run(main())
```

---

### Handling SDK exceptions

Public SDK methods raise exceptions owned by the SDK. Catch `SdkError` to handle any SDK failure, or catch a narrower subclass when you need a specific category.

```python
import asyncio

from osc_sdk_python import AsyncClient, SdkError, SdkClientError

async def main():
    try:
        async with AsyncClient() as client:
            print(await client.osc.read_vms())
    except SdkClientError as err:
        print("API rejected the request:", err)
        if err.response is not None:
            print("status:", err.response.status_code)
    except SdkError as err:
        print("SDK error:", err)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Examples

### List all VM and Volume IDs

```python
from osc_sdk_python import Client

if __name__ == "__main__":
    with Client() as client:
        print("Your virtual machines:")
        for vm in client.osc.ReadVms()["Vms"]:
            print(vm["VmId"])

        print("\nYour volumes:")
        for volume in client.osc.ReadVolumes()["Volumes"]:
            print(volume["VolumeId"])
```

### List all VM and Volume IDs asynchronously

```python
import asyncio

from osc_sdk_python import AsyncClient


async def main():
    async with AsyncClient() as client:
        print("Your virtual machines:")
        for vm in (await client.osc.read_vms()).vms:
            print(vm.vm_id)

        print("\nYour volumes:")
        for volume in (await client.osc.read_volumes()).volumes:
            print(volume.volume_id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Enabling logs

```python
import logging

from osc_sdk_python import Client

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    with Client(profile="profile_1") as client:
        result = client.osc.raw("ReadVms")
        print(result)
```

This logs requests through Python's standard `logging` module using the `osc_sdk_python` logger:

```text
2026-06-15 12:45:10,123 - INFO - mode: sync
service: api
method: POST
uri: /api/v1/ReadVms
payload:
{}
```

Usage examples can be combined with the official [Outscale API documentation](https://docs.outscale.com/en/userguide/Home.html).
