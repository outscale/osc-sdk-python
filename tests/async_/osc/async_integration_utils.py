from osc_sdk_python.generated.osc import (
    CreateTagsRequest,
    ReadImagesRequest,
    ReadSubregionsRequest,
)
from tests.integration_utils import (
    build_name_tag_request,
    get_first_item,
    get_linux_http_user_data,
    get_tagged_name,
    log_test_step,
)


async def get_first_subregion_name(client):
    subregions = await client.osc.read_subregions(ReadSubregionsRequest())
    subregion = get_first_item(subregions.subregions, "No subregions returned")
    if not subregion.subregion_name:
        raise AssertionError("SubregionName is missing")
    return subregion.subregion_name


async def get_latest_public_ubuntu_image_id(client):
    images = await client.osc.read_images(
        ReadImagesRequest(
            filters={
                "AccountAliases": ["Outscale"],
                "ImageNames": ["Ubuntu*"],
                "PermissionsToLaunchGlobalPermission": True,
                "States": ["available"],
            },
            results_per_page=10,
        )
    )
    image = get_first_item(
        sorted(images.images or [], key=lambda item: item.creation_date or "", reverse=True),
        "No public Ubuntu image returned",
    )
    if not image.image_id:
        raise AssertionError("ImageId is missing")
    return image.image_id


async def read_single_resource(client, method_name, request_cls, key, resource_id_key, resource_id):
    response = await getattr(client.osc, method_name)(
        request_cls(filters={resource_id_key: [resource_id]})
    )
    items = getattr(response, key)
    if not items or len(items) != 1:
        raise AssertionError(
            "{} did not return exactly one resource for {}".format(
                method_name, resource_id
            )
        )
    return items[0]


def build_name_tag_typed_request(resource_id):
    return CreateTagsRequest(**build_name_tag_request(resource_id))


__all__ = [
    "build_name_tag_typed_request",
    "get_first_subregion_name",
    "get_latest_public_ubuntu_image_id",
    "get_linux_http_user_data",
    "get_tagged_name",
    "log_test_step",
    "read_single_resource",
]
