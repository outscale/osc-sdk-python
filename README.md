# What
Based on oapi-cli this program helps you making Outscale Gateway call.
- Use actions as method name
- Parameters are checked locally. Check if a mandatory parameter is missing. Check if a parameter is valid. Check has correct type.


# Usage
       from osc_python_sdk import Gateway
       gw = Gateway(**{'profile': 'my-profile'})
       # Calls with api Action as method
       result = gw.ReadSecurityGroups(Filters={'SecurityGroupNames': ['default']})
       result = gw.CreateVms(ImageId='ami-3e158364', VmType='tinav4.c2r4')
       # Or raw calls:
       result = gw.raw('ReadVms')
       result = gw.raw('CreateVms', ImageId='ami-xx', BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds=['sg-aaa', 'sg-bbb'], Wrong='wrong')




# Installation
    pip install https://github.com/outscale/osc_python_sdk/releases/download/0.9.7/osc_python_sdk-0.9.7-py3-none-any.whl

## Credentials

When you use the cli you can choose a profile. Profiles are can be setted with environment variables or in a file.
It checks environment variables before loading the file.

In the file, you can set a default profile, naming `default`. It will be used if you don't precise profile in command line.

### Environment variables

    $ export OSC_ACCESS_KEY=<ACCESS_KEY>
    $ export OSC_SECRET_KEY=<SECRET_KEY>
    (optional) $ export OSC_REGION=<REGION> (default: us-west-1)

### Credentials files

    $ cat ~/.oapi_credentials
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
