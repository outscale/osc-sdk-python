## 🚀 Usage

Basic usage with the default profile:

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
from osc_sdk_python import AsyncClient

client = AsyncClient(profile="profile_1")
```

Using multiple services from one client:

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

* **Typed methods**: `await client.osc.read_vms(...)`, `await client.osc.create_vms(...)`, etc.
* **Dynamic methods**: `await client.osc.ReadVms(...)`, `await client.osc.CreateVms(...)`, etc.
* **Raw calls**: `await client.osc.raw("ActionName", **params)`

Typed request and response models under `osc_sdk_python.generated.*` are exposed on `AsyncClient` with snake_case operation names. Dynamic action methods remain available for compatibility with action-style names.

Example:

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
        if err.request_id is not None:
            print("request_id:", err.request_id)
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
import asyncio
import logging

from osc_sdk_python import AsyncClient

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    async def main():
        async with AsyncClient(profile="profile_1") as client:
            result = await client.osc.raw("ReadVms")
            print(result)

    asyncio.run(main())
```

This logs requests through Python's standard `logging` module using the `osc_sdk_python` logger:

```text
2026-06-15 12:45:10,123 - INFO - service: api
method: POST
uri: /api/v1/ReadVms
payload:
{}
```

Usage examples can be combined with the official [Outscale API documentation](https://docs.outscale.com/en/userguide/Home.html).
