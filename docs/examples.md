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

## 💡 Examples

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
from osc_sdk_python import Client, LOG_ALL, LOG_KEEP_ONLY_LAST_REQ, LOG_MEMORY, LOG_STDERR, LOG_STDIO

if __name__ == "__main__":
    with Client(profile="profile_1") as client:
        # 'what' can be LOG_KEEP_ONLY_LAST_REQ or LOG_ALL
        # Here we print logs in memory, standard output and standard error
        client.osc.log.config(type=LOG_MEMORY | LOG_STDIO | LOG_STDERR, what=LOG_KEEP_ONLY_LAST_REQ)

        result = client.osc.raw("ReadVms")

        last_request = client.osc.log.str()
        print(last_request)
```

Usage examples can be combined with the official [Outscale API documentation](https://docs.outscale.com/en/userguide/Home.html).
