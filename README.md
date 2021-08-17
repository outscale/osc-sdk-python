# Outscale Python SDK

This python SDK helps you to perform actions on Outscale API.

You will need to have an Outscale account, please visit [Outscale website](https://outscale.com/).

API Documentation https://docs-beta.outscale.com/?python#3ds-outscale-api

# Installation

You can install the pre-built python package through this command:

```bash
$ pip install osc_sdk_python
```

# Building

To build the package yourself:
```bash
$ git submodule update --init
$ python3 -m pip install --user --upgrade setuptools wheel
$ python3 setup.py sdist bdist_wheel
```

You can then install it with `pip install dist/osc_sdk_python-0.9.15-py3-none-any.whl`

# Configuration & Credentials

When you use the cli you can choose a profile. Profiles can be set with environment variables or in a file.
It checks environment variables before loading the file.

In the file, you can set a default profile, naming `default`. It will be used if you don't precise profile in command line.

## Environment variables

```
$ export OSC_ACCESS_KEY=<ACCESS_KEY>
$ export OSC_SECRET_KEY=<SECRET_KEY>
$ # optional
$ export OSC_REGION=<REGION> (default: eu-west-2)
```

## Credentials files

```json
$ cat ~/.osc/config.json
{
    "default": {
        "access_key": "<ACCESS_KEY>",
        "secret_key": "<SECRET_KEY>",
        "region": "<REGION>"
    },
    "profile_1": {
        "access_key": "<ACCESS_KEY>",
        "secret_key": "<SECRET_KEY>",
        "region": "<REGION>"
    },
    "profile_2": {
        "access_key": "<ACCESS_KEY>",
        "secret_key": "<SECRET_KEY>",
        "region": "<REGION>"
    }
}
```

Notes:
* if  ~/.osc/config.json is not found, ~/.oapi_credentials will be used
* Environment variables have priority over Credentials files.

# Example

A simple example which prints all your Virtual Machine and Volume ids.
```python
from osc_sdk_python import Gateway

if __name__ == '__main__':
    gw = Gateway()

    print("your virtual machines:")
    for vm in gw.ReadVms()["Vms"]:
        print(vm["VmId"])

    print("\nyour volumes:")
    for volume in gw.ReadVolumes()["Volumes"]:
        print(volume["VolumeId"])
```

Usage example, check [Outscale API documentation](https://docs-beta.outscale.com/) for more details.
```python
from osc_sdk_python import Gateway

if __name__ == '__main__':
    gw = Gateway(**{'profile': 'profile_1'})

    # Calls with api Action as method
    result = gw.ReadSecurityGroups(Filters={'SecurityGroupNames': ['default']})
    result = gw.CreateVms(ImageId='ami-3e158364', VmType='tinav4.c2r4')

    # Or raw calls:
    result = gw.raw('ReadVms')
    result = gw.raw('CreateVms', ImageId='ami-xx', BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds=['sg-aaa', 'sg-bbb'], Wrong='wrong')
```


# Known Issues

## UTF-8
Some people my encounter some issue with utf-8 which looks like this
```bash
Problem reading (…)osc_sdk_python/osc-api/outscale.yaml:'ascii' codec can't decode byte 0xe2 in position 14856: ordinal not in range(128)
```

To avoid this issue, configure you locals as follow:
```bash
LC_ALL=en_US.UTF-8
```

if you don't want your locals to be set system wide you can proceed as follow:
```bash
LC_ALL=en_US.UTF-8 pip install osc-sdk-python
```
