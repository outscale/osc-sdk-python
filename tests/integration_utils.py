import base64
import random
import string
import time

def random_string(length=10):
    alphabet = string.ascii_lowercase + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def tagged_name(prefix="osc-sdk-python-test", length=10):
    return "{}-{}".format(prefix, random_string(length))


def log_step(message):
    print("[tests] {}".format(message), flush=True)


def wait_until(fetch, ready, timeout=300, interval=10, failure=None, describe=None):
    deadline = time.time() + timeout
    last_value = None
    while time.time() < deadline:
        last_value = fetch()
        if describe is not None:
            log_step(describe(last_value))
        if ready(last_value):
            return last_value
        if failure is not None and failure(last_value):
            raise AssertionError("Resource entered an unexpected state: {}".format(last_value))
        time.sleep(interval)
    raise AssertionError("Timed out waiting for resource state: {}".format(last_value))


def first(items, message):
    if not items:
        raise AssertionError(message)
    return items[0]


def first_subregion_name(gw):
    subregions = gw.ReadSubregions()
    subregion = first(subregions.get("Subregions"), "No subregions returned")
    name = subregion.get("SubregionName")
    if not name:
        raise AssertionError("SubregionName is missing")
    return name


def latest_public_ubuntu_image_id(gw):
    images = gw.ReadImages(
        Filters={
            "AccountAliases": ["Outscale"],
            "ImageNames": ["Ubuntu*"],
            "PermissionsToLaunchGlobalPermission": True,
            "States": ["available"],
        },
        ResultsPerPage=10,
    ).get("Images", [])
    image = first(
        sorted(images, key=lambda item: item.get("CreationDate", ""), reverse=True),
        "No public Ubuntu image returned",
    )
    image_id = image.get("ImageId")
    if not image_id:
        raise AssertionError("ImageId is missing")
    return image_id


def read_single(gw, action, key, resource_id_key, resource_id):
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


def create_name_tag(resource_id):
    return {
        "ResourceIds": [resource_id],
        "Tags": [{"Key": "Name", "Value": tagged_name("osc-sdk-python-tag")}],
    }


def linux_http_user_data():
    script = """#!/bin/sh
set -eu
mkdir -p /tmp/python-sdk-lb
echo ok > /tmp/python-sdk-lb/index.html
nohup python3 -m http.server 80 --directory /tmp/python-sdk-lb >/tmp/python-sdk-lb/http.log 2>&1 &
"""
    return base64.b64encode(script.encode("utf-8")).decode("ascii")
