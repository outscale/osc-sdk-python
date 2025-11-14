## 🚀 Usage

Basic usage with the default profile:

```python
from osc_sdk_python import Gateway

gw = Gateway()

# Example: list VMs
vms = gw.ReadVms()
print(vms)
```

Using a specific profile:

```python
from osc_sdk_python import Gateway

gw = Gateway(profile="profile_1")
```

Calling actions:

* **Typed methods**: `gw.ReadVms(...)`, `gw.CreateVms(...)`, etc.
* **Raw calls**: `gw.raw("ActionName", **params)`

Example:

```python
from osc_sdk_python import Gateway

gw = Gateway(profile="profile_1")

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

---

## 💡 Examples

### List all VM and Volume IDs

```python
from osc_sdk_python import Gateway

if __name__ == "__main__":
    gw = Gateway()

    print("Your virtual machines:")
    for vm in gw.ReadVms()["Vms"]:
        print(vm["VmId"])

    print("\nYour volumes:")
    for volume in gw.ReadVolumes()["Volumes"]:
        print(volume["VolumeId"])
```

### Enabling logs

```python
from osc_sdk_python import *

if __name__ == "__main__":
    gw = Gateway(profile="profile_1")

    # 'what' can be LOG_KEEP_ONLY_LAST_REQ or LOG_ALL
    # Here we print logs in memory, standard output and standard error
    gw.log.config(type=LOG_MEMORY | LOG_STDIO | LOG_STDERR, what=LOG_KEEP_ONLY_LAST_REQ)

    result = gw.raw("ReadVms")

    last_request = gw.log.str()
    print(last_request)
```

Usage examples can be combined with the official [Outscale API documentation](https://docs.outscale.com/en/userguide/Home.html).