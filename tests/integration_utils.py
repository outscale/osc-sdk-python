import base64
import random
import string

def get_random_string(length=10):
    alphabet = string.ascii_lowercase + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def get_tagged_name(prefix="osc-sdk-python-test", length=10):
    return "{}-{}".format(prefix, get_random_string(length))


def log_test_step(message):
    print("[tests] {}".format(message), flush=True)

def get_first_item(items, message):
    if not items:
        raise AssertionError(message)
    return items[0]


def get_first_subregion_name(gw):
    subregions = gw.ReadSubregions()
    subregion = get_first_item(subregions.get("Subregions"), "No subregions returned")
    name = subregion.get("SubregionName")
    if not name:
        raise AssertionError("SubregionName is missing")
    return name


def get_latest_public_ubuntu_image_id(gw):
    images = gw.ReadImages(
        Filters={
            "AccountAliases": ["Outscale"],
            "ImageNames": ["Ubuntu*"],
            "PermissionsToLaunchGlobalPermission": True,
            "States": ["available"],
        },
        ResultsPerPage=10,
    ).get("Images", [])
    image = get_first_item(
        sorted(images, key=lambda item: item.get("CreationDate", ""), reverse=True),
        "No public Ubuntu image returned",
    )
    image_id = image.get("ImageId")
    if not image_id:
        raise AssertionError("ImageId is missing")
    return image_id


def read_single_resource(gw, action, key, resource_id_key, resource_id):
    response = getattr(gw, action)(
        Filters={
            resource_id_key: [resource_id],
        }
    )
    items = response.get(key)
    if not items or len(items) != 1:
        raise AssertionError(
            "{} did not return exactly one resource for {}".format(action, resource_id)
        )
    return items[0]


def build_name_tag_request(resource_id):
    return {
        "ResourceIds": [resource_id],
        "Tags": [{"Key": "Name", "Value": get_tagged_name("osc-sdk-python-tag")}],
    }


def get_linux_http_user_data():
    script = """#!/bin/sh
set -eu
mkdir -p /tmp/python-sdk-lb
echo ok > /tmp/python-sdk-lb/index.html
nohup python3 -m http.server 80 --directory /tmp/python-sdk-lb >/tmp/python-sdk-lb/http.log 2>&1 &
"""
    return base64.b64encode(script.encode("utf-8")).decode("ascii")
