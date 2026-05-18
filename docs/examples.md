## 🚀 Usage

Basic usage with the default profile:

```python
from osc_sdk_python import Gateway

with Gateway() as gw:
    # Example: list VMs
    vms = gw.ReadVms()
    print(vms)
```

Async usage with the default profile:

```python
import asyncio

from osc_sdk_python import AsyncGateway


async def main():
    async with AsyncGateway() as gw:
        # Example: list VMs
        vms = await gw.ReadVms()
        print(vms)


if __name__ == "__main__":
    asyncio.run(main())
```

Using a specific profile:

```python
from osc_sdk_python import Gateway

gw = Gateway(profile="profile_1")
```

Using a specific profile with the async client:

```python
from osc_sdk_python import AsyncGateway

gw = AsyncGateway(profile="profile_1")
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
        vms = await client.osc.ReadVms()
        projects = await client.oks.ListProjects()


if __name__ == "__main__":
    asyncio.run(main())
```

Calling actions:

* **Typed methods**: `gw.ReadVms(...)`, `gw.CreateVms(...)`, etc.
* **Raw calls**: `gw.raw("ActionName", **params)`
* **Async calls**: `await gw.ReadVms(...)`, `await gw.raw("ActionName", **params)`

Example:

```python
from osc_sdk_python import Gateway

with Gateway(profile="profile_1") as gw:
    # Calls with API action as method
    result = gw.ReadSecurityGroups(Filters={"SecurityGroupNames": ["default"]})
    result = gw.CreateVms(ImageId="ami-3e158364", VmType="tinav4.c2r4")

    # Or raw calls:
    result = gw.raw("ReadVms")
    result = gw.raw(
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

from osc_sdk_python import AsyncGateway


async def main():
    async with AsyncGateway(profile="profile_1") as gw:
        # Calls with API action as method
        result = await gw.ReadSecurityGroups(
            Filters={"SecurityGroupNames": ["default"]}
        )
        result = await gw.CreateVms(ImageId="ami-3e158364", VmType="tinav4.c2r4")

        # Or raw calls:
        result = await gw.raw("ReadVms")
        result = await gw.raw(
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
from osc_sdk_python import Gateway

if __name__ == "__main__":
    with Gateway() as gw:
        print("Your virtual machines:")
        for vm in gw.ReadVms()["Vms"]:
            print(vm["VmId"])

        print("\nYour volumes:")
        for volume in gw.ReadVolumes()["Volumes"]:
            print(volume["VolumeId"])
```

### List all VM and Volume IDs asynchronously

```python
import asyncio

from osc_sdk_python import AsyncGateway


async def main():
    async with AsyncGateway() as gw:
        print("Your virtual machines:")
        for vm in (await gw.ReadVms())["Vms"]:
            print(vm["VmId"])

        print("\nYour volumes:")
        for volume in (await gw.ReadVolumes())["Volumes"]:
            print(volume["VolumeId"])


if __name__ == "__main__":
    asyncio.run(main())
```

### Enabling logs

```python
from osc_sdk_python import *

if __name__ == "__main__":
    with Gateway(profile="profile_1") as gw:
        # 'what' can be LOG_KEEP_ONLY_LAST_REQ or LOG_ALL
        # Here we print logs in memory, standard output and standard error
        gw.log.config(type=LOG_MEMORY | LOG_STDIO | LOG_STDERR, what=LOG_KEEP_ONLY_LAST_REQ)

        result = gw.raw("ReadVms")

        last_request = gw.log.str()
        print(last_request)
```

Usage examples can be combined with the official [Outscale API documentation](https://docs.outscale.com/en/userguide/Home.html).
