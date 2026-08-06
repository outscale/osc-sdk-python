"""Generated typed OSC client slice.

Typed request and response models are async-first. Generated typed methods are
exposed on AsyncClient; synchronous clients use dynamic action methods.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator

    python -m osc_sdk_python.codegen.generator oks osc
"""

from typing import Any

from pydantic import TypeAdapter, ValidationError

from osc_sdk_python.exceptions import SdkResponseError, SdkValidationError
from osc_sdk_python.runtime.request import RequestSpec
from .models import (
    AcceptNetPeeringRequest,
    AcceptNetPeeringResponse,
    AddUserToUserGroupRequest,
    AddUserToUserGroupResponse,
    CheckAuthenticationRequest,
    CheckAuthenticationResponse,
    CreateAccessKeyRequest,
    CreateAccessKeyResponse,
    CreateAccountRequest,
    CreateAccountResponse,
    CreateApiAccessRuleRequest,
    CreateApiAccessRuleResponse,
    CreateCaRequest,
    CreateCaResponse,
    CreateClientGatewayRequest,
    CreateClientGatewayResponse,
    CreateDedicatedGroupRequest,
    CreateDedicatedGroupResponse,
    CreateDhcpOptionsRequest,
    CreateDhcpOptionsResponse,
    CreateDirectLinkInterfaceRequest,
    CreateDirectLinkInterfaceResponse,
    CreateDirectLinkRequest,
    CreateDirectLinkResponse,
    CreateFlexibleGpuRequest,
    CreateFlexibleGpuResponse,
    CreateImageExportTaskRequest,
    CreateImageExportTaskResponse,
    CreateImageRequest,
    CreateImageResponse,
    CreateInternetServiceRequest,
    CreateInternetServiceResponse,
    CreateKeypairRequest,
    CreateKeypairResponse,
    CreateListenerRuleRequest,
    CreateListenerRuleResponse,
    CreateLoadBalancerListenersRequest,
    CreateLoadBalancerListenersResponse,
    CreateLoadBalancerPolicyRequest,
    CreateLoadBalancerPolicyResponse,
    CreateLoadBalancerRequest,
    CreateLoadBalancerResponse,
    CreateLoadBalancerTagsRequest,
    CreateLoadBalancerTagsResponse,
    CreateNatServiceRequest,
    CreateNatServiceResponse,
    CreateNetAccessPointRequest,
    CreateNetAccessPointResponse,
    CreateNetPeeringRequest,
    CreateNetPeeringResponse,
    CreateNetRequest,
    CreateNetResponse,
    CreateNicRequest,
    CreateNicResponse,
    CreatePolicyRequest,
    CreatePolicyResponse,
    CreatePolicyVersionRequest,
    CreatePolicyVersionResponse,
    CreateProductTypeRequest,
    CreateProductTypeResponse,
    CreatePublicIpRequest,
    CreatePublicIpResponse,
    CreateRouteRequest,
    CreateRouteResponse,
    CreateRouteTableRequest,
    CreateRouteTableResponse,
    CreateSecurityGroupRequest,
    CreateSecurityGroupResponse,
    CreateSecurityGroupRuleRequest,
    CreateSecurityGroupRuleResponse,
    CreateServerCertificateRequest,
    CreateServerCertificateResponse,
    CreateSnapshotExportTaskRequest,
    CreateSnapshotExportTaskResponse,
    CreateSnapshotRequest,
    CreateSnapshotResponse,
    CreateSubnetRequest,
    CreateSubnetResponse,
    CreateTagsRequest,
    CreateTagsResponse,
    CreateUserGroupRequest,
    CreateUserGroupResponse,
    CreateUserRequest,
    CreateUserResponse,
    CreateVirtualGatewayRequest,
    CreateVirtualGatewayResponse,
    CreateVmGroupRequest,
    CreateVmGroupResponse,
    CreateVmTemplateRequest,
    CreateVmTemplateResponse,
    CreateVmsRequest,
    CreateVmsResponse,
    CreateVolumeRequest,
    CreateVolumeResponse,
    CreateVpnConnectionRequest,
    CreateVpnConnectionResponse,
    CreateVpnConnectionRouteRequest,
    CreateVpnConnectionRouteResponse,
    DeleteAccessKeyRequest,
    DeleteAccessKeyResponse,
    DeleteApiAccessRuleRequest,
    DeleteApiAccessRuleResponse,
    DeleteCaRequest,
    DeleteCaResponse,
    DeleteClientGatewayRequest,
    DeleteClientGatewayResponse,
    DeleteDedicatedGroupRequest,
    DeleteDedicatedGroupResponse,
    DeleteDhcpOptionsRequest,
    DeleteDhcpOptionsResponse,
    DeleteDirectLinkInterfaceRequest,
    DeleteDirectLinkInterfaceResponse,
    DeleteDirectLinkRequest,
    DeleteDirectLinkResponse,
    DeleteExportTaskRequest,
    DeleteExportTaskResponse,
    DeleteFlexibleGpuRequest,
    DeleteFlexibleGpuResponse,
    DeleteImageRequest,
    DeleteImageResponse,
    DeleteInternetServiceRequest,
    DeleteInternetServiceResponse,
    DeleteKeypairRequest,
    DeleteKeypairResponse,
    DeleteListenerRuleRequest,
    DeleteListenerRuleResponse,
    DeleteLoadBalancerListenersRequest,
    DeleteLoadBalancerListenersResponse,
    DeleteLoadBalancerPolicyRequest,
    DeleteLoadBalancerPolicyResponse,
    DeleteLoadBalancerRequest,
    DeleteLoadBalancerResponse,
    DeleteLoadBalancerTagsRequest,
    DeleteLoadBalancerTagsResponse,
    DeleteNatServiceRequest,
    DeleteNatServiceResponse,
    DeleteNetAccessPointRequest,
    DeleteNetAccessPointResponse,
    DeleteNetPeeringRequest,
    DeleteNetPeeringResponse,
    DeleteNetRequest,
    DeleteNetResponse,
    DeleteNicRequest,
    DeleteNicResponse,
    DeletePolicyRequest,
    DeletePolicyResponse,
    DeletePolicyVersionRequest,
    DeletePolicyVersionResponse,
    DeleteProductTypeRequest,
    DeleteProductTypeResponse,
    DeletePublicIpRequest,
    DeletePublicIpResponse,
    DeleteRouteRequest,
    DeleteRouteResponse,
    DeleteRouteTableRequest,
    DeleteRouteTableResponse,
    DeleteSecurityGroupRequest,
    DeleteSecurityGroupResponse,
    DeleteSecurityGroupRuleRequest,
    DeleteSecurityGroupRuleResponse,
    DeleteServerCertificateRequest,
    DeleteServerCertificateResponse,
    DeleteSnapshotRequest,
    DeleteSnapshotResponse,
    DeleteSubnetRequest,
    DeleteSubnetResponse,
    DeleteTagsRequest,
    DeleteTagsResponse,
    DeleteUserGroupPolicyRequest,
    DeleteUserGroupPolicyResponse,
    DeleteUserGroupRequest,
    DeleteUserGroupResponse,
    DeleteUserPolicyRequest,
    DeleteUserPolicyResponse,
    DeleteUserRequest,
    DeleteUserResponse,
    DeleteVirtualGatewayRequest,
    DeleteVirtualGatewayResponse,
    DeleteVmGroupRequest,
    DeleteVmGroupResponse,
    DeleteVmTemplateRequest,
    DeleteVmTemplateResponse,
    DeleteVmsRequest,
    DeleteVmsResponse,
    DeleteVolumeRequest,
    DeleteVolumeResponse,
    DeleteVpnConnectionRequest,
    DeleteVpnConnectionResponse,
    DeleteVpnConnectionRouteRequest,
    DeleteVpnConnectionRouteResponse,
    DeregisterVmsInLoadBalancerRequest,
    DeregisterVmsInLoadBalancerResponse,
    DisableOutscaleLoginPerUsersRequest,
    DisableOutscaleLoginPerUsersResponse,
    DisableOutscaleLoginRequest,
    DisableOutscaleLoginResponse,
    EnableOutscaleLoginForUsersRequest,
    EnableOutscaleLoginForUsersResponse,
    EnableOutscaleLoginPerUsersRequest,
    EnableOutscaleLoginPerUsersResponse,
    EnableOutscaleLoginRequest,
    EnableOutscaleLoginResponse,
    LinkFlexibleGpuRequest,
    LinkFlexibleGpuResponse,
    LinkInternetServiceRequest,
    LinkInternetServiceResponse,
    LinkLoadBalancerBackendMachinesRequest,
    LinkLoadBalancerBackendMachinesResponse,
    LinkManagedPolicyToUserGroupRequest,
    LinkManagedPolicyToUserGroupResponse,
    LinkNicRequest,
    LinkNicResponse,
    LinkPolicyRequest,
    LinkPolicyResponse,
    LinkPrivateIpsRequest,
    LinkPrivateIpsResponse,
    LinkPublicIpRequest,
    LinkPublicIpResponse,
    LinkRouteTableRequest,
    LinkRouteTableResponse,
    LinkVirtualGatewayRequest,
    LinkVirtualGatewayResponse,
    LinkVolumeRequest,
    LinkVolumeResponse,
    PutUserGroupPolicyRequest,
    PutUserGroupPolicyResponse,
    PutUserPolicyRequest,
    PutUserPolicyResponse,
    ReadAccessKeysRequest,
    ReadAccessKeysResponse,
    ReadAccountsRequest,
    ReadAccountsResponse,
    ReadAdminPasswordRequest,
    ReadAdminPasswordResponse,
    ReadApiAccessPolicyRequest,
    ReadApiAccessPolicyResponse,
    ReadApiAccessRulesRequest,
    ReadApiAccessRulesResponse,
    ReadApiLogsRequest,
    ReadApiLogsResponse,
    ReadCO2EmissionAccountRequest,
    ReadCO2EmissionAccountResponse,
    ReadCasRequest,
    ReadCasResponse,
    ReadCatalogRequest,
    ReadCatalogResponse,
    ReadCatalogsRequest,
    ReadCatalogsResponse,
    ReadClientGatewaysRequest,
    ReadClientGatewaysResponse,
    ReadConsoleOutputRequest,
    ReadConsoleOutputResponse,
    ReadConsumptionAccountRequest,
    ReadConsumptionAccountResponse,
    ReadDedicatedGroupsRequest,
    ReadDedicatedGroupsResponse,
    ReadDhcpOptionsRequest,
    ReadDhcpOptionsResponse,
    ReadDirectLinkInterfacesRequest,
    ReadDirectLinkInterfacesResponse,
    ReadDirectLinksRequest,
    ReadDirectLinksResponse,
    ReadEntitiesLinkedToPolicyRequest,
    ReadEntitiesLinkedToPolicyResponse,
    ReadFlexibleGpuCatalogRequest,
    ReadFlexibleGpuCatalogResponse,
    ReadFlexibleGpusRequest,
    ReadFlexibleGpusResponse,
    ReadImageExportTasksRequest,
    ReadImageExportTasksResponse,
    ReadImagesRequest,
    ReadImagesResponse,
    ReadInternetServicesRequest,
    ReadInternetServicesResponse,
    ReadKeypairsRequest,
    ReadKeypairsResponse,
    ReadLinkedPoliciesRequest,
    ReadLinkedPoliciesResponse,
    ReadListenerRulesRequest,
    ReadListenerRulesResponse,
    ReadLoadBalancerTagsRequest,
    ReadLoadBalancerTagsResponse,
    ReadLoadBalancersRequest,
    ReadLoadBalancersResponse,
    ReadLocationsRequest,
    ReadLocationsResponse,
    ReadManagedPoliciesLinkedToUserGroupRequest,
    ReadManagedPoliciesLinkedToUserGroupResponse,
    ReadNatServicesRequest,
    ReadNatServicesResponse,
    ReadNetAccessPointServicesRequest,
    ReadNetAccessPointServicesResponse,
    ReadNetAccessPointsRequest,
    ReadNetAccessPointsResponse,
    ReadNetPeeringsRequest,
    ReadNetPeeringsResponse,
    ReadNetsRequest,
    ReadNetsResponse,
    ReadNicsRequest,
    ReadNicsResponse,
    ReadPoliciesRequest,
    ReadPoliciesResponse,
    ReadPolicyRequest,
    ReadPolicyResponse,
    ReadPolicyVersionRequest,
    ReadPolicyVersionResponse,
    ReadPolicyVersionsRequest,
    ReadPolicyVersionsResponse,
    ReadProductTypesRequest,
    ReadProductTypesResponse,
    ReadPublicCatalogRequest,
    ReadPublicCatalogResponse,
    ReadPublicIpRangesRequest,
    ReadPublicIpRangesResponse,
    ReadPublicIpsRequest,
    ReadPublicIpsResponse,
    ReadQuotasRequest,
    ReadQuotasResponse,
    ReadRegionsRequest,
    ReadRegionsResponse,
    ReadRouteTablesRequest,
    ReadRouteTablesResponse,
    ReadSecurityGroupsRequest,
    ReadSecurityGroupsResponse,
    ReadServerCertificatesRequest,
    ReadServerCertificatesResponse,
    ReadSnapshotExportTasksRequest,
    ReadSnapshotExportTasksResponse,
    ReadSnapshotsRequest,
    ReadSnapshotsResponse,
    ReadSubnetsRequest,
    ReadSubnetsResponse,
    ReadSubregionsRequest,
    ReadSubregionsResponse,
    ReadTagsRequest,
    ReadTagsResponse,
    ReadUnitPriceRequest,
    ReadUnitPriceResponse,
    ReadUserGroupPoliciesRequest,
    ReadUserGroupPoliciesResponse,
    ReadUserGroupPolicyRequest,
    ReadUserGroupPolicyResponse,
    ReadUserGroupRequest,
    ReadUserGroupResponse,
    ReadUserGroupsPerUserRequest,
    ReadUserGroupsPerUserResponse,
    ReadUserGroupsRequest,
    ReadUserGroupsResponse,
    ReadUserPoliciesRequest,
    ReadUserPoliciesResponse,
    ReadUserPolicyRequest,
    ReadUserPolicyResponse,
    ReadUsersRequest,
    ReadUsersResponse,
    ReadVirtualGatewaysRequest,
    ReadVirtualGatewaysResponse,
    ReadVmGroupsRequest,
    ReadVmGroupsResponse,
    ReadVmTemplatesRequest,
    ReadVmTemplatesResponse,
    ReadVmTypesRequest,
    ReadVmTypesResponse,
    ReadVmsHealthRequest,
    ReadVmsHealthResponse,
    ReadVmsRequest,
    ReadVmsResponse,
    ReadVmsStateRequest,
    ReadVmsStateResponse,
    ReadVmsStopHistoryRequest,
    ReadVmsStopHistoryResponse,
    ReadVolumeUpdateTasksRequest,
    ReadVolumeUpdateTasksResponse,
    ReadVolumesRequest,
    ReadVolumesResponse,
    ReadVpnConnectionsRequest,
    ReadVpnConnectionsResponse,
    RebootVmsRequest,
    RebootVmsResponse,
    RegisterVmsInLoadBalancerRequest,
    RegisterVmsInLoadBalancerResponse,
    RejectNetPeeringRequest,
    RejectNetPeeringResponse,
    RemoveUserFromUserGroupRequest,
    RemoveUserFromUserGroupResponse,
    ScaleDownVmGroupRequest,
    ScaleDownVmGroupResponse,
    ScaleUpVmGroupRequest,
    ScaleUpVmGroupResponse,
    SetDefaultPolicyVersionRequest,
    SetDefaultPolicyVersionResponse,
    StartVmsRequest,
    StartVmsResponse,
    StopVmsRequest,
    StopVmsResponse,
    UnlinkFlexibleGpuRequest,
    UnlinkFlexibleGpuResponse,
    UnlinkInternetServiceRequest,
    UnlinkInternetServiceResponse,
    UnlinkLoadBalancerBackendMachinesRequest,
    UnlinkLoadBalancerBackendMachinesResponse,
    UnlinkManagedPolicyFromUserGroupRequest,
    UnlinkManagedPolicyFromUserGroupResponse,
    UnlinkNicRequest,
    UnlinkNicResponse,
    UnlinkPolicyRequest,
    UnlinkPolicyResponse,
    UnlinkPrivateIpsRequest,
    UnlinkPrivateIpsResponse,
    UnlinkPublicIpRequest,
    UnlinkPublicIpResponse,
    UnlinkRouteTableRequest,
    UnlinkRouteTableResponse,
    UnlinkVirtualGatewayRequest,
    UnlinkVirtualGatewayResponse,
    UnlinkVolumeRequest,
    UnlinkVolumeResponse,
    UpdateAccessKeyRequest,
    UpdateAccessKeyResponse,
    UpdateAccountRequest,
    UpdateAccountResponse,
    UpdateApiAccessPolicyRequest,
    UpdateApiAccessPolicyResponse,
    UpdateApiAccessRuleRequest,
    UpdateApiAccessRuleResponse,
    UpdateCaRequest,
    UpdateCaResponse,
    UpdateDedicatedGroupRequest,
    UpdateDedicatedGroupResponse,
    UpdateDirectLinkInterfaceRequest,
    UpdateDirectLinkInterfaceResponse,
    UpdateFlexibleGpuRequest,
    UpdateFlexibleGpuResponse,
    UpdateImageRequest,
    UpdateImageResponse,
    UpdateListenerRuleRequest,
    UpdateListenerRuleResponse,
    UpdateLoadBalancerRequest,
    UpdateLoadBalancerResponse,
    UpdateNetAccessPointRequest,
    UpdateNetAccessPointResponse,
    UpdateNetRequest,
    UpdateNetResponse,
    UpdateNicRequest,
    UpdateNicResponse,
    UpdateRoutePropagationRequest,
    UpdateRoutePropagationResponse,
    UpdateRouteRequest,
    UpdateRouteResponse,
    UpdateRouteTableLinkRequest,
    UpdateRouteTableLinkResponse,
    UpdateServerCertificateRequest,
    UpdateServerCertificateResponse,
    UpdateSnapshotRequest,
    UpdateSnapshotResponse,
    UpdateSubnetRequest,
    UpdateSubnetResponse,
    UpdateUserGroupRequest,
    UpdateUserGroupResponse,
    UpdateUserRequest,
    UpdateUserResponse,
    UpdateVmGroupRequest,
    UpdateVmGroupResponse,
    UpdateVmRequest,
    UpdateVmResponse,
    UpdateVmTemplateRequest,
    UpdateVmTemplateResponse,
    UpdateVolumeRequest,
    UpdateVolumeResponse,
    UpdateVpnConnectionRequest,
    UpdateVpnConnectionResponse,
)


def _dump_json_body(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(exclude_none=True, by_alias=True)
    return value


def _validate_request(model: type, value: Any) -> Any:
    try:
        if value is None:
            return model()
        if isinstance(value, model):
            return value
        return TypeAdapter(model).validate_python(value)
    except ValidationError as error:
        raise SdkValidationError(str(error)) from error


def _validate_response(model: type, value: Any) -> Any:
    try:
        return TypeAdapter(model).validate_python(value)
    except ValidationError as error:
        raise SdkResponseError(str(error)) from error


class AsyncOscTypedMixin:
    async def accept_net_peering(
        self,
        request: AcceptNetPeeringRequest | None = None,
    ) -> AcceptNetPeeringResponse:
        request = _validate_request(AcceptNetPeeringRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/AcceptNetPeering",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(AcceptNetPeeringResponse, response)

    async def add_user_to_user_group(
        self,
        request: AddUserToUserGroupRequest | None = None,
    ) -> AddUserToUserGroupResponse:
        request = _validate_request(AddUserToUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/AddUserToUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(AddUserToUserGroupResponse, response)

    async def check_authentication(
        self,
        request: CheckAuthenticationRequest | None = None,
    ) -> CheckAuthenticationResponse:
        request = _validate_request(CheckAuthenticationRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CheckAuthentication",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CheckAuthenticationResponse, response)

    async def create_access_key(
        self,
        request: CreateAccessKeyRequest | None = None,
    ) -> CreateAccessKeyResponse:
        request = _validate_request(CreateAccessKeyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateAccessKey",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateAccessKeyResponse, response)

    async def create_account(
        self,
        request: CreateAccountRequest | None = None,
    ) -> CreateAccountResponse:
        request = _validate_request(CreateAccountRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateAccount",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateAccountResponse, response)

    async def create_api_access_rule(
        self,
        request: CreateApiAccessRuleRequest | None = None,
    ) -> CreateApiAccessRuleResponse:
        request = _validate_request(CreateApiAccessRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateApiAccessRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateApiAccessRuleResponse, response)

    async def create_ca(
        self,
        request: CreateCaRequest | None = None,
    ) -> CreateCaResponse:
        request = _validate_request(CreateCaRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateCa",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateCaResponse, response)

    async def create_client_gateway(
        self,
        request: CreateClientGatewayRequest | None = None,
    ) -> CreateClientGatewayResponse:
        request = _validate_request(CreateClientGatewayRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateClientGateway",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateClientGatewayResponse, response)

    async def create_dedicated_group(
        self,
        request: CreateDedicatedGroupRequest | None = None,
    ) -> CreateDedicatedGroupResponse:
        request = _validate_request(CreateDedicatedGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateDedicatedGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateDedicatedGroupResponse, response)

    async def create_dhcp_options(
        self,
        request: CreateDhcpOptionsRequest | None = None,
    ) -> CreateDhcpOptionsResponse:
        request = _validate_request(CreateDhcpOptionsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateDhcpOptions",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateDhcpOptionsResponse, response)

    async def create_direct_link(
        self,
        request: CreateDirectLinkRequest | None = None,
    ) -> CreateDirectLinkResponse:
        request = _validate_request(CreateDirectLinkRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateDirectLink",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateDirectLinkResponse, response)

    async def create_direct_link_interface(
        self,
        request: CreateDirectLinkInterfaceRequest | None = None,
    ) -> CreateDirectLinkInterfaceResponse:
        request = _validate_request(CreateDirectLinkInterfaceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateDirectLinkInterface",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateDirectLinkInterfaceResponse, response)

    async def create_flexible_gpu(
        self,
        request: CreateFlexibleGpuRequest | None = None,
    ) -> CreateFlexibleGpuResponse:
        request = _validate_request(CreateFlexibleGpuRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateFlexibleGpu",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateFlexibleGpuResponse, response)

    async def create_image(
        self,
        request: CreateImageRequest | None = None,
    ) -> CreateImageResponse:
        request = _validate_request(CreateImageRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateImage",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateImageResponse, response)

    async def create_image_export_task(
        self,
        request: CreateImageExportTaskRequest | None = None,
    ) -> CreateImageExportTaskResponse:
        request = _validate_request(CreateImageExportTaskRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateImageExportTask",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateImageExportTaskResponse, response)

    async def create_internet_service(
        self,
        request: CreateInternetServiceRequest | None = None,
    ) -> CreateInternetServiceResponse:
        request = _validate_request(CreateInternetServiceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateInternetService",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateInternetServiceResponse, response)

    async def create_keypair(
        self,
        request: CreateKeypairRequest | None = None,
    ) -> CreateKeypairResponse:
        request = _validate_request(CreateKeypairRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateKeypair",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateKeypairResponse, response)

    async def create_listener_rule(
        self,
        request: CreateListenerRuleRequest | None = None,
    ) -> CreateListenerRuleResponse:
        request = _validate_request(CreateListenerRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateListenerRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateListenerRuleResponse, response)

    async def create_load_balancer(
        self,
        request: CreateLoadBalancerRequest | None = None,
    ) -> CreateLoadBalancerResponse:
        request = _validate_request(CreateLoadBalancerRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateLoadBalancer",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateLoadBalancerResponse, response)

    async def create_load_balancer_listeners(
        self,
        request: CreateLoadBalancerListenersRequest | None = None,
    ) -> CreateLoadBalancerListenersResponse:
        request = _validate_request(CreateLoadBalancerListenersRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateLoadBalancerListeners",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateLoadBalancerListenersResponse, response)

    async def create_load_balancer_policy(
        self,
        request: CreateLoadBalancerPolicyRequest | None = None,
    ) -> CreateLoadBalancerPolicyResponse:
        request = _validate_request(CreateLoadBalancerPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateLoadBalancerPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateLoadBalancerPolicyResponse, response)

    async def create_load_balancer_tags(
        self,
        request: CreateLoadBalancerTagsRequest | None = None,
    ) -> CreateLoadBalancerTagsResponse:
        request = _validate_request(CreateLoadBalancerTagsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateLoadBalancerTags",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateLoadBalancerTagsResponse, response)

    async def create_nat_service(
        self,
        request: CreateNatServiceRequest | None = None,
    ) -> CreateNatServiceResponse:
        request = _validate_request(CreateNatServiceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateNatService",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateNatServiceResponse, response)

    async def create_net(
        self,
        request: CreateNetRequest | None = None,
    ) -> CreateNetResponse:
        request = _validate_request(CreateNetRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateNet",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateNetResponse, response)

    async def create_net_access_point(
        self,
        request: CreateNetAccessPointRequest | None = None,
    ) -> CreateNetAccessPointResponse:
        request = _validate_request(CreateNetAccessPointRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateNetAccessPoint",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateNetAccessPointResponse, response)

    async def create_net_peering(
        self,
        request: CreateNetPeeringRequest | None = None,
    ) -> CreateNetPeeringResponse:
        request = _validate_request(CreateNetPeeringRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateNetPeering",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateNetPeeringResponse, response)

    async def create_nic(
        self,
        request: CreateNicRequest | None = None,
    ) -> CreateNicResponse:
        request = _validate_request(CreateNicRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateNic",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateNicResponse, response)

    async def create_policy(
        self,
        request: CreatePolicyRequest | None = None,
    ) -> CreatePolicyResponse:
        request = _validate_request(CreatePolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreatePolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreatePolicyResponse, response)

    async def create_policy_version(
        self,
        request: CreatePolicyVersionRequest | None = None,
    ) -> CreatePolicyVersionResponse:
        request = _validate_request(CreatePolicyVersionRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreatePolicyVersion",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreatePolicyVersionResponse, response)

    async def create_product_type(
        self,
        request: CreateProductTypeRequest | None = None,
    ) -> CreateProductTypeResponse:
        request = _validate_request(CreateProductTypeRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateProductType",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateProductTypeResponse, response)

    async def create_public_ip(
        self,
        request: CreatePublicIpRequest | None = None,
    ) -> CreatePublicIpResponse:
        request = _validate_request(CreatePublicIpRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreatePublicIp",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreatePublicIpResponse, response)

    async def create_route(
        self,
        request: CreateRouteRequest | None = None,
    ) -> CreateRouteResponse:
        request = _validate_request(CreateRouteRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateRoute",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateRouteResponse, response)

    async def create_route_table(
        self,
        request: CreateRouteTableRequest | None = None,
    ) -> CreateRouteTableResponse:
        request = _validate_request(CreateRouteTableRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateRouteTable",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateRouteTableResponse, response)

    async def create_security_group(
        self,
        request: CreateSecurityGroupRequest | None = None,
    ) -> CreateSecurityGroupResponse:
        request = _validate_request(CreateSecurityGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateSecurityGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateSecurityGroupResponse, response)

    async def create_security_group_rule(
        self,
        request: CreateSecurityGroupRuleRequest | None = None,
    ) -> CreateSecurityGroupRuleResponse:
        request = _validate_request(CreateSecurityGroupRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateSecurityGroupRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateSecurityGroupRuleResponse, response)

    async def create_server_certificate(
        self,
        request: CreateServerCertificateRequest | None = None,
    ) -> CreateServerCertificateResponse:
        request = _validate_request(CreateServerCertificateRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateServerCertificate",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateServerCertificateResponse, response)

    async def create_snapshot(
        self,
        request: CreateSnapshotRequest | None = None,
    ) -> CreateSnapshotResponse:
        request = _validate_request(CreateSnapshotRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateSnapshot",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateSnapshotResponse, response)

    async def create_snapshot_export_task(
        self,
        request: CreateSnapshotExportTaskRequest | None = None,
    ) -> CreateSnapshotExportTaskResponse:
        request = _validate_request(CreateSnapshotExportTaskRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateSnapshotExportTask",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateSnapshotExportTaskResponse, response)

    async def create_subnet(
        self,
        request: CreateSubnetRequest | None = None,
    ) -> CreateSubnetResponse:
        request = _validate_request(CreateSubnetRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateSubnet",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateSubnetResponse, response)

    async def create_tags(
        self,
        request: CreateTagsRequest | None = None,
    ) -> CreateTagsResponse:
        request = _validate_request(CreateTagsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateTags",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateTagsResponse, response)

    async def create_user(
        self,
        request: CreateUserRequest | None = None,
    ) -> CreateUserResponse:
        request = _validate_request(CreateUserRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateUser",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateUserResponse, response)

    async def create_user_group(
        self,
        request: CreateUserGroupRequest | None = None,
    ) -> CreateUserGroupResponse:
        request = _validate_request(CreateUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateUserGroupResponse, response)

    async def create_virtual_gateway(
        self,
        request: CreateVirtualGatewayRequest | None = None,
    ) -> CreateVirtualGatewayResponse:
        request = _validate_request(CreateVirtualGatewayRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateVirtualGateway",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateVirtualGatewayResponse, response)

    async def create_vm_group(
        self,
        request: CreateVmGroupRequest | None = None,
    ) -> CreateVmGroupResponse:
        request = _validate_request(CreateVmGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateVmGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateVmGroupResponse, response)

    async def create_vm_template(
        self,
        request: CreateVmTemplateRequest | None = None,
    ) -> CreateVmTemplateResponse:
        request = _validate_request(CreateVmTemplateRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateVmTemplate",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateVmTemplateResponse, response)

    async def create_vms(
        self,
        request: CreateVmsRequest | None = None,
    ) -> CreateVmsResponse:
        request = _validate_request(CreateVmsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateVms",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateVmsResponse, response)

    async def create_volume(
        self,
        request: CreateVolumeRequest | None = None,
    ) -> CreateVolumeResponse:
        request = _validate_request(CreateVolumeRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateVolume",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateVolumeResponse, response)

    async def create_vpn_connection(
        self,
        request: CreateVpnConnectionRequest | None = None,
    ) -> CreateVpnConnectionResponse:
        request = _validate_request(CreateVpnConnectionRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateVpnConnection",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateVpnConnectionResponse, response)

    async def create_vpn_connection_route(
        self,
        request: CreateVpnConnectionRouteRequest | None = None,
    ) -> CreateVpnConnectionRouteResponse:
        request = _validate_request(CreateVpnConnectionRouteRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/CreateVpnConnectionRoute",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(CreateVpnConnectionRouteResponse, response)

    async def delete_access_key(
        self,
        request: DeleteAccessKeyRequest | None = None,
    ) -> DeleteAccessKeyResponse:
        request = _validate_request(DeleteAccessKeyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteAccessKey",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteAccessKeyResponse, response)

    async def delete_api_access_rule(
        self,
        request: DeleteApiAccessRuleRequest | None = None,
    ) -> DeleteApiAccessRuleResponse:
        request = _validate_request(DeleteApiAccessRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteApiAccessRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteApiAccessRuleResponse, response)

    async def delete_ca(
        self,
        request: DeleteCaRequest | None = None,
    ) -> DeleteCaResponse:
        request = _validate_request(DeleteCaRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteCa",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteCaResponse, response)

    async def delete_client_gateway(
        self,
        request: DeleteClientGatewayRequest | None = None,
    ) -> DeleteClientGatewayResponse:
        request = _validate_request(DeleteClientGatewayRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteClientGateway",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteClientGatewayResponse, response)

    async def delete_dedicated_group(
        self,
        request: DeleteDedicatedGroupRequest | None = None,
    ) -> DeleteDedicatedGroupResponse:
        request = _validate_request(DeleteDedicatedGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteDedicatedGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteDedicatedGroupResponse, response)

    async def delete_dhcp_options(
        self,
        request: DeleteDhcpOptionsRequest | None = None,
    ) -> DeleteDhcpOptionsResponse:
        request = _validate_request(DeleteDhcpOptionsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteDhcpOptions",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteDhcpOptionsResponse, response)

    async def delete_direct_link(
        self,
        request: DeleteDirectLinkRequest | None = None,
    ) -> DeleteDirectLinkResponse:
        request = _validate_request(DeleteDirectLinkRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteDirectLink",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteDirectLinkResponse, response)

    async def delete_direct_link_interface(
        self,
        request: DeleteDirectLinkInterfaceRequest | None = None,
    ) -> DeleteDirectLinkInterfaceResponse:
        request = _validate_request(DeleteDirectLinkInterfaceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteDirectLinkInterface",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteDirectLinkInterfaceResponse, response)

    async def delete_export_task(
        self,
        request: DeleteExportTaskRequest | None = None,
    ) -> DeleteExportTaskResponse:
        request = _validate_request(DeleteExportTaskRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteExportTask",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteExportTaskResponse, response)

    async def delete_flexible_gpu(
        self,
        request: DeleteFlexibleGpuRequest | None = None,
    ) -> DeleteFlexibleGpuResponse:
        request = _validate_request(DeleteFlexibleGpuRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteFlexibleGpu",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteFlexibleGpuResponse, response)

    async def delete_image(
        self,
        request: DeleteImageRequest | None = None,
    ) -> DeleteImageResponse:
        request = _validate_request(DeleteImageRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteImage",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteImageResponse, response)

    async def delete_internet_service(
        self,
        request: DeleteInternetServiceRequest | None = None,
    ) -> DeleteInternetServiceResponse:
        request = _validate_request(DeleteInternetServiceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteInternetService",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteInternetServiceResponse, response)

    async def delete_keypair(
        self,
        request: DeleteKeypairRequest | None = None,
    ) -> DeleteKeypairResponse:
        request = _validate_request(DeleteKeypairRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteKeypair",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteKeypairResponse, response)

    async def delete_listener_rule(
        self,
        request: DeleteListenerRuleRequest | None = None,
    ) -> DeleteListenerRuleResponse:
        request = _validate_request(DeleteListenerRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteListenerRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteListenerRuleResponse, response)

    async def delete_load_balancer(
        self,
        request: DeleteLoadBalancerRequest | None = None,
    ) -> DeleteLoadBalancerResponse:
        request = _validate_request(DeleteLoadBalancerRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteLoadBalancer",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteLoadBalancerResponse, response)

    async def delete_load_balancer_listeners(
        self,
        request: DeleteLoadBalancerListenersRequest | None = None,
    ) -> DeleteLoadBalancerListenersResponse:
        request = _validate_request(DeleteLoadBalancerListenersRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteLoadBalancerListeners",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteLoadBalancerListenersResponse, response)

    async def delete_load_balancer_policy(
        self,
        request: DeleteLoadBalancerPolicyRequest | None = None,
    ) -> DeleteLoadBalancerPolicyResponse:
        request = _validate_request(DeleteLoadBalancerPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteLoadBalancerPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteLoadBalancerPolicyResponse, response)

    async def delete_load_balancer_tags(
        self,
        request: DeleteLoadBalancerTagsRequest | None = None,
    ) -> DeleteLoadBalancerTagsResponse:
        request = _validate_request(DeleteLoadBalancerTagsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteLoadBalancerTags",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteLoadBalancerTagsResponse, response)

    async def delete_nat_service(
        self,
        request: DeleteNatServiceRequest | None = None,
    ) -> DeleteNatServiceResponse:
        request = _validate_request(DeleteNatServiceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteNatService",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteNatServiceResponse, response)

    async def delete_net(
        self,
        request: DeleteNetRequest | None = None,
    ) -> DeleteNetResponse:
        request = _validate_request(DeleteNetRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteNet",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteNetResponse, response)

    async def delete_net_access_point(
        self,
        request: DeleteNetAccessPointRequest | None = None,
    ) -> DeleteNetAccessPointResponse:
        request = _validate_request(DeleteNetAccessPointRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteNetAccessPoint",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteNetAccessPointResponse, response)

    async def delete_net_peering(
        self,
        request: DeleteNetPeeringRequest | None = None,
    ) -> DeleteNetPeeringResponse:
        request = _validate_request(DeleteNetPeeringRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteNetPeering",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteNetPeeringResponse, response)

    async def delete_nic(
        self,
        request: DeleteNicRequest | None = None,
    ) -> DeleteNicResponse:
        request = _validate_request(DeleteNicRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteNic",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteNicResponse, response)

    async def delete_policy(
        self,
        request: DeletePolicyRequest | None = None,
    ) -> DeletePolicyResponse:
        request = _validate_request(DeletePolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeletePolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeletePolicyResponse, response)

    async def delete_policy_version(
        self,
        request: DeletePolicyVersionRequest | None = None,
    ) -> DeletePolicyVersionResponse:
        request = _validate_request(DeletePolicyVersionRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeletePolicyVersion",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeletePolicyVersionResponse, response)

    async def delete_product_type(
        self,
        request: DeleteProductTypeRequest | None = None,
    ) -> DeleteProductTypeResponse:
        request = _validate_request(DeleteProductTypeRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteProductType",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteProductTypeResponse, response)

    async def delete_public_ip(
        self,
        request: DeletePublicIpRequest | None = None,
    ) -> DeletePublicIpResponse:
        request = _validate_request(DeletePublicIpRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeletePublicIp",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeletePublicIpResponse, response)

    async def delete_route(
        self,
        request: DeleteRouteRequest | None = None,
    ) -> DeleteRouteResponse:
        request = _validate_request(DeleteRouteRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteRoute",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteRouteResponse, response)

    async def delete_route_table(
        self,
        request: DeleteRouteTableRequest | None = None,
    ) -> DeleteRouteTableResponse:
        request = _validate_request(DeleteRouteTableRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteRouteTable",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteRouteTableResponse, response)

    async def delete_security_group(
        self,
        request: DeleteSecurityGroupRequest | None = None,
    ) -> DeleteSecurityGroupResponse:
        request = _validate_request(DeleteSecurityGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteSecurityGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteSecurityGroupResponse, response)

    async def delete_security_group_rule(
        self,
        request: DeleteSecurityGroupRuleRequest | None = None,
    ) -> DeleteSecurityGroupRuleResponse:
        request = _validate_request(DeleteSecurityGroupRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteSecurityGroupRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteSecurityGroupRuleResponse, response)

    async def delete_server_certificate(
        self,
        request: DeleteServerCertificateRequest | None = None,
    ) -> DeleteServerCertificateResponse:
        request = _validate_request(DeleteServerCertificateRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteServerCertificate",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteServerCertificateResponse, response)

    async def delete_snapshot(
        self,
        request: DeleteSnapshotRequest | None = None,
    ) -> DeleteSnapshotResponse:
        request = _validate_request(DeleteSnapshotRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteSnapshot",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteSnapshotResponse, response)

    async def delete_subnet(
        self,
        request: DeleteSubnetRequest | None = None,
    ) -> DeleteSubnetResponse:
        request = _validate_request(DeleteSubnetRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteSubnet",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteSubnetResponse, response)

    async def delete_tags(
        self,
        request: DeleteTagsRequest | None = None,
    ) -> DeleteTagsResponse:
        request = _validate_request(DeleteTagsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteTags",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteTagsResponse, response)

    async def delete_user(
        self,
        request: DeleteUserRequest | None = None,
    ) -> DeleteUserResponse:
        request = _validate_request(DeleteUserRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteUser",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteUserResponse, response)

    async def delete_user_group(
        self,
        request: DeleteUserGroupRequest | None = None,
    ) -> DeleteUserGroupResponse:
        request = _validate_request(DeleteUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteUserGroupResponse, response)

    async def delete_user_group_policy(
        self,
        request: DeleteUserGroupPolicyRequest | None = None,
    ) -> DeleteUserGroupPolicyResponse:
        request = _validate_request(DeleteUserGroupPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteUserGroupPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteUserGroupPolicyResponse, response)

    async def delete_user_policy(
        self,
        request: DeleteUserPolicyRequest | None = None,
    ) -> DeleteUserPolicyResponse:
        request = _validate_request(DeleteUserPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteUserPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteUserPolicyResponse, response)

    async def delete_virtual_gateway(
        self,
        request: DeleteVirtualGatewayRequest | None = None,
    ) -> DeleteVirtualGatewayResponse:
        request = _validate_request(DeleteVirtualGatewayRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteVirtualGateway",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteVirtualGatewayResponse, response)

    async def delete_vm_group(
        self,
        request: DeleteVmGroupRequest | None = None,
    ) -> DeleteVmGroupResponse:
        request = _validate_request(DeleteVmGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteVmGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteVmGroupResponse, response)

    async def delete_vm_template(
        self,
        request: DeleteVmTemplateRequest | None = None,
    ) -> DeleteVmTemplateResponse:
        request = _validate_request(DeleteVmTemplateRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteVmTemplate",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteVmTemplateResponse, response)

    async def delete_vms(
        self,
        request: DeleteVmsRequest | None = None,
    ) -> DeleteVmsResponse:
        request = _validate_request(DeleteVmsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteVms",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteVmsResponse, response)

    async def delete_volume(
        self,
        request: DeleteVolumeRequest | None = None,
    ) -> DeleteVolumeResponse:
        request = _validate_request(DeleteVolumeRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteVolume",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteVolumeResponse, response)

    async def delete_vpn_connection(
        self,
        request: DeleteVpnConnectionRequest | None = None,
    ) -> DeleteVpnConnectionResponse:
        request = _validate_request(DeleteVpnConnectionRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteVpnConnection",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteVpnConnectionResponse, response)

    async def delete_vpn_connection_route(
        self,
        request: DeleteVpnConnectionRouteRequest | None = None,
    ) -> DeleteVpnConnectionRouteResponse:
        request = _validate_request(DeleteVpnConnectionRouteRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeleteVpnConnectionRoute",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeleteVpnConnectionRouteResponse, response)

    async def deregister_vms_in_load_balancer(
        self,
        request: DeregisterVmsInLoadBalancerRequest | None = None,
    ) -> DeregisterVmsInLoadBalancerResponse:
        request = _validate_request(DeregisterVmsInLoadBalancerRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DeregisterVmsInLoadBalancer",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DeregisterVmsInLoadBalancerResponse, response)

    async def disable_outscale_login(
        self,
        request: DisableOutscaleLoginRequest | None = None,
    ) -> DisableOutscaleLoginResponse:
        request = _validate_request(DisableOutscaleLoginRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DisableOutscaleLogin",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DisableOutscaleLoginResponse, response)

    async def disable_outscale_login_for_users(
        self,
        request: DisableOutscaleLoginRequest | None = None,
    ) -> DisableOutscaleLoginResponse:
        request = _validate_request(DisableOutscaleLoginRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DisableOutscaleLoginForUsers",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DisableOutscaleLoginResponse, response)

    async def disable_outscale_login_per_users(
        self,
        request: DisableOutscaleLoginPerUsersRequest | None = None,
    ) -> DisableOutscaleLoginPerUsersResponse:
        request = _validate_request(DisableOutscaleLoginPerUsersRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/DisableOutscaleLoginPerUsers",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(DisableOutscaleLoginPerUsersResponse, response)

    async def enable_outscale_login(
        self,
        request: EnableOutscaleLoginRequest | None = None,
    ) -> EnableOutscaleLoginResponse:
        request = _validate_request(EnableOutscaleLoginRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/EnableOutscaleLogin",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(EnableOutscaleLoginResponse, response)

    async def enable_outscale_login_for_users(
        self,
        request: EnableOutscaleLoginForUsersRequest | None = None,
    ) -> EnableOutscaleLoginForUsersResponse:
        request = _validate_request(EnableOutscaleLoginForUsersRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/EnableOutscaleLoginForUsers",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(EnableOutscaleLoginForUsersResponse, response)

    async def enable_outscale_login_per_users(
        self,
        request: EnableOutscaleLoginPerUsersRequest | None = None,
    ) -> EnableOutscaleLoginPerUsersResponse:
        request = _validate_request(EnableOutscaleLoginPerUsersRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/EnableOutscaleLoginPerUsers",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(EnableOutscaleLoginPerUsersResponse, response)

    async def link_flexible_gpu(
        self,
        request: LinkFlexibleGpuRequest | None = None,
    ) -> LinkFlexibleGpuResponse:
        request = _validate_request(LinkFlexibleGpuRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkFlexibleGpu",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkFlexibleGpuResponse, response)

    async def link_internet_service(
        self,
        request: LinkInternetServiceRequest | None = None,
    ) -> LinkInternetServiceResponse:
        request = _validate_request(LinkInternetServiceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkInternetService",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkInternetServiceResponse, response)

    async def link_load_balancer_backend_machines(
        self,
        request: LinkLoadBalancerBackendMachinesRequest | None = None,
    ) -> LinkLoadBalancerBackendMachinesResponse:
        request = _validate_request(LinkLoadBalancerBackendMachinesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkLoadBalancerBackendMachines",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkLoadBalancerBackendMachinesResponse, response)

    async def link_managed_policy_to_user_group(
        self,
        request: LinkManagedPolicyToUserGroupRequest | None = None,
    ) -> LinkManagedPolicyToUserGroupResponse:
        request = _validate_request(LinkManagedPolicyToUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkManagedPolicyToUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkManagedPolicyToUserGroupResponse, response)

    async def link_nic(
        self,
        request: LinkNicRequest | None = None,
    ) -> LinkNicResponse:
        request = _validate_request(LinkNicRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkNic",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkNicResponse, response)

    async def link_policy(
        self,
        request: LinkPolicyRequest | None = None,
    ) -> LinkPolicyResponse:
        request = _validate_request(LinkPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkPolicyResponse, response)

    async def link_private_ips(
        self,
        request: LinkPrivateIpsRequest | None = None,
    ) -> LinkPrivateIpsResponse:
        request = _validate_request(LinkPrivateIpsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkPrivateIps",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkPrivateIpsResponse, response)

    async def link_public_ip(
        self,
        request: LinkPublicIpRequest | None = None,
    ) -> LinkPublicIpResponse:
        request = _validate_request(LinkPublicIpRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkPublicIp",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkPublicIpResponse, response)

    async def link_route_table(
        self,
        request: LinkRouteTableRequest | None = None,
    ) -> LinkRouteTableResponse:
        request = _validate_request(LinkRouteTableRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkRouteTable",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkRouteTableResponse, response)

    async def link_virtual_gateway(
        self,
        request: LinkVirtualGatewayRequest | None = None,
    ) -> LinkVirtualGatewayResponse:
        request = _validate_request(LinkVirtualGatewayRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkVirtualGateway",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkVirtualGatewayResponse, response)

    async def link_volume(
        self,
        request: LinkVolumeRequest | None = None,
    ) -> LinkVolumeResponse:
        request = _validate_request(LinkVolumeRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/LinkVolume",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(LinkVolumeResponse, response)

    async def put_user_group_policy(
        self,
        request: PutUserGroupPolicyRequest | None = None,
    ) -> PutUserGroupPolicyResponse:
        request = _validate_request(PutUserGroupPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/PutUserGroupPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(PutUserGroupPolicyResponse, response)

    async def put_user_policy(
        self,
        request: PutUserPolicyRequest | None = None,
    ) -> PutUserPolicyResponse:
        request = _validate_request(PutUserPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/PutUserPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(PutUserPolicyResponse, response)

    async def read_access_keys(
        self,
        request: ReadAccessKeysRequest | None = None,
    ) -> ReadAccessKeysResponse:
        request = _validate_request(ReadAccessKeysRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadAccessKeys",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadAccessKeysResponse, response)

    async def read_accounts(
        self,
        request: ReadAccountsRequest | None = None,
    ) -> ReadAccountsResponse:
        request = _validate_request(ReadAccountsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadAccounts",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadAccountsResponse, response)

    async def read_admin_password(
        self,
        request: ReadAdminPasswordRequest | None = None,
    ) -> ReadAdminPasswordResponse:
        request = _validate_request(ReadAdminPasswordRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadAdminPassword",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadAdminPasswordResponse, response)

    async def read_api_access_policy(
        self,
        request: ReadApiAccessPolicyRequest | None = None,
    ) -> ReadApiAccessPolicyResponse:
        request = _validate_request(ReadApiAccessPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadApiAccessPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadApiAccessPolicyResponse, response)

    async def read_api_access_rules(
        self,
        request: ReadApiAccessRulesRequest | None = None,
    ) -> ReadApiAccessRulesResponse:
        request = _validate_request(ReadApiAccessRulesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadApiAccessRules",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadApiAccessRulesResponse, response)

    async def read_api_logs(
        self,
        request: ReadApiLogsRequest | None = None,
    ) -> ReadApiLogsResponse:
        request = _validate_request(ReadApiLogsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadApiLogs",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadApiLogsResponse, response)

    async def read_co2_emission_account(
        self,
        request: ReadCO2EmissionAccountRequest | None = None,
    ) -> ReadCO2EmissionAccountResponse:
        request = _validate_request(ReadCO2EmissionAccountRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadCO2EmissionAccount",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadCO2EmissionAccountResponse, response)

    async def read_cas(
        self,
        request: ReadCasRequest | None = None,
    ) -> ReadCasResponse:
        request = _validate_request(ReadCasRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadCas",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadCasResponse, response)

    async def read_catalog(
        self,
        request: ReadCatalogRequest | None = None,
    ) -> ReadCatalogResponse:
        request = _validate_request(ReadCatalogRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadCatalog",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadCatalogResponse, response)

    async def read_catalogs(
        self,
        request: ReadCatalogsRequest | None = None,
    ) -> ReadCatalogsResponse:
        request = _validate_request(ReadCatalogsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadCatalogs",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadCatalogsResponse, response)

    async def read_client_gateways(
        self,
        request: ReadClientGatewaysRequest | None = None,
    ) -> ReadClientGatewaysResponse:
        request = _validate_request(ReadClientGatewaysRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadClientGateways",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadClientGatewaysResponse, response)

    async def read_console_output(
        self,
        request: ReadConsoleOutputRequest | None = None,
    ) -> ReadConsoleOutputResponse:
        request = _validate_request(ReadConsoleOutputRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadConsoleOutput",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadConsoleOutputResponse, response)

    async def read_consumption_account(
        self,
        request: ReadConsumptionAccountRequest | None = None,
    ) -> ReadConsumptionAccountResponse:
        request = _validate_request(ReadConsumptionAccountRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadConsumptionAccount",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadConsumptionAccountResponse, response)

    async def read_dedicated_groups(
        self,
        request: ReadDedicatedGroupsRequest | None = None,
    ) -> ReadDedicatedGroupsResponse:
        request = _validate_request(ReadDedicatedGroupsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadDedicatedGroups",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadDedicatedGroupsResponse, response)

    async def read_dhcp_options(
        self,
        request: ReadDhcpOptionsRequest | None = None,
    ) -> ReadDhcpOptionsResponse:
        request = _validate_request(ReadDhcpOptionsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadDhcpOptions",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadDhcpOptionsResponse, response)

    async def read_direct_link_interfaces(
        self,
        request: ReadDirectLinkInterfacesRequest | None = None,
    ) -> ReadDirectLinkInterfacesResponse:
        request = _validate_request(ReadDirectLinkInterfacesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadDirectLinkInterfaces",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadDirectLinkInterfacesResponse, response)

    async def read_direct_links(
        self,
        request: ReadDirectLinksRequest | None = None,
    ) -> ReadDirectLinksResponse:
        request = _validate_request(ReadDirectLinksRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadDirectLinks",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadDirectLinksResponse, response)

    async def read_entities_linked_to_policy(
        self,
        request: ReadEntitiesLinkedToPolicyRequest | None = None,
    ) -> ReadEntitiesLinkedToPolicyResponse:
        request = _validate_request(ReadEntitiesLinkedToPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadEntitiesLinkedToPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadEntitiesLinkedToPolicyResponse, response)

    async def read_flexible_gpu_catalog(
        self,
        request: ReadFlexibleGpuCatalogRequest | None = None,
    ) -> ReadFlexibleGpuCatalogResponse:
        request = _validate_request(ReadFlexibleGpuCatalogRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadFlexibleGpuCatalog",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadFlexibleGpuCatalogResponse, response)

    async def read_flexible_gpus(
        self,
        request: ReadFlexibleGpusRequest | None = None,
    ) -> ReadFlexibleGpusResponse:
        request = _validate_request(ReadFlexibleGpusRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadFlexibleGpus",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadFlexibleGpusResponse, response)

    async def read_image_export_tasks(
        self,
        request: ReadImageExportTasksRequest | None = None,
    ) -> ReadImageExportTasksResponse:
        request = _validate_request(ReadImageExportTasksRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadImageExportTasks",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadImageExportTasksResponse, response)

    async def read_images(
        self,
        request: ReadImagesRequest | None = None,
    ) -> ReadImagesResponse:
        request = _validate_request(ReadImagesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadImages",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadImagesResponse, response)

    async def read_internet_services(
        self,
        request: ReadInternetServicesRequest | None = None,
    ) -> ReadInternetServicesResponse:
        request = _validate_request(ReadInternetServicesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadInternetServices",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadInternetServicesResponse, response)

    async def read_keypairs(
        self,
        request: ReadKeypairsRequest | None = None,
    ) -> ReadKeypairsResponse:
        request = _validate_request(ReadKeypairsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadKeypairs",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadKeypairsResponse, response)

    async def read_linked_policies(
        self,
        request: ReadLinkedPoliciesRequest | None = None,
    ) -> ReadLinkedPoliciesResponse:
        request = _validate_request(ReadLinkedPoliciesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadLinkedPolicies",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadLinkedPoliciesResponse, response)

    async def read_listener_rules(
        self,
        request: ReadListenerRulesRequest | None = None,
    ) -> ReadListenerRulesResponse:
        request = _validate_request(ReadListenerRulesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadListenerRules",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadListenerRulesResponse, response)

    async def read_load_balancer_tags(
        self,
        request: ReadLoadBalancerTagsRequest | None = None,
    ) -> ReadLoadBalancerTagsResponse:
        request = _validate_request(ReadLoadBalancerTagsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadLoadBalancerTags",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadLoadBalancerTagsResponse, response)

    async def read_load_balancers(
        self,
        request: ReadLoadBalancersRequest | None = None,
    ) -> ReadLoadBalancersResponse:
        request = _validate_request(ReadLoadBalancersRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadLoadBalancers",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadLoadBalancersResponse, response)

    async def read_locations(
        self,
        request: ReadLocationsRequest | None = None,
    ) -> ReadLocationsResponse:
        request = _validate_request(ReadLocationsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadLocations",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadLocationsResponse, response)

    async def read_managed_policies_linked_to_user_group(
        self,
        request: ReadManagedPoliciesLinkedToUserGroupRequest | None = None,
    ) -> ReadManagedPoliciesLinkedToUserGroupResponse:
        request = _validate_request(ReadManagedPoliciesLinkedToUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadManagedPoliciesLinkedToUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadManagedPoliciesLinkedToUserGroupResponse, response)

    async def read_nat_services(
        self,
        request: ReadNatServicesRequest | None = None,
    ) -> ReadNatServicesResponse:
        request = _validate_request(ReadNatServicesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadNatServices",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadNatServicesResponse, response)

    async def read_net_access_point_services(
        self,
        request: ReadNetAccessPointServicesRequest | None = None,
    ) -> ReadNetAccessPointServicesResponse:
        request = _validate_request(ReadNetAccessPointServicesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadNetAccessPointServices",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadNetAccessPointServicesResponse, response)

    async def read_net_access_points(
        self,
        request: ReadNetAccessPointsRequest | None = None,
    ) -> ReadNetAccessPointsResponse:
        request = _validate_request(ReadNetAccessPointsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadNetAccessPoints",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadNetAccessPointsResponse, response)

    async def read_net_peerings(
        self,
        request: ReadNetPeeringsRequest | None = None,
    ) -> ReadNetPeeringsResponse:
        request = _validate_request(ReadNetPeeringsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadNetPeerings",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadNetPeeringsResponse, response)

    async def read_nets(
        self,
        request: ReadNetsRequest | None = None,
    ) -> ReadNetsResponse:
        request = _validate_request(ReadNetsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadNets",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadNetsResponse, response)

    async def read_nics(
        self,
        request: ReadNicsRequest | None = None,
    ) -> ReadNicsResponse:
        request = _validate_request(ReadNicsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadNics",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadNicsResponse, response)

    async def read_policies(
        self,
        request: ReadPoliciesRequest | None = None,
    ) -> ReadPoliciesResponse:
        request = _validate_request(ReadPoliciesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadPolicies",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadPoliciesResponse, response)

    async def read_policy(
        self,
        request: ReadPolicyRequest | None = None,
    ) -> ReadPolicyResponse:
        request = _validate_request(ReadPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadPolicyResponse, response)

    async def read_policy_version(
        self,
        request: ReadPolicyVersionRequest | None = None,
    ) -> ReadPolicyVersionResponse:
        request = _validate_request(ReadPolicyVersionRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadPolicyVersion",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadPolicyVersionResponse, response)

    async def read_policy_versions(
        self,
        request: ReadPolicyVersionsRequest | None = None,
    ) -> ReadPolicyVersionsResponse:
        request = _validate_request(ReadPolicyVersionsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadPolicyVersions",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadPolicyVersionsResponse, response)

    async def read_product_types(
        self,
        request: ReadProductTypesRequest | None = None,
    ) -> ReadProductTypesResponse:
        request = _validate_request(ReadProductTypesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadProductTypes",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadProductTypesResponse, response)

    async def read_public_catalog(
        self,
        request: ReadPublicCatalogRequest | None = None,
    ) -> ReadPublicCatalogResponse:
        request = _validate_request(ReadPublicCatalogRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadPublicCatalog",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadPublicCatalogResponse, response)

    async def read_public_ip_ranges(
        self,
        request: ReadPublicIpRangesRequest | None = None,
    ) -> ReadPublicIpRangesResponse:
        request = _validate_request(ReadPublicIpRangesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadPublicIpRanges",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadPublicIpRangesResponse, response)

    async def read_public_ips(
        self,
        request: ReadPublicIpsRequest | None = None,
    ) -> ReadPublicIpsResponse:
        request = _validate_request(ReadPublicIpsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadPublicIps",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadPublicIpsResponse, response)

    async def read_quotas(
        self,
        request: ReadQuotasRequest | None = None,
    ) -> ReadQuotasResponse:
        request = _validate_request(ReadQuotasRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadQuotas",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadQuotasResponse, response)

    async def read_regions(
        self,
        request: ReadRegionsRequest | None = None,
    ) -> ReadRegionsResponse:
        request = _validate_request(ReadRegionsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadRegions",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadRegionsResponse, response)

    async def read_route_tables(
        self,
        request: ReadRouteTablesRequest | None = None,
    ) -> ReadRouteTablesResponse:
        request = _validate_request(ReadRouteTablesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadRouteTables",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadRouteTablesResponse, response)

    async def read_security_groups(
        self,
        request: ReadSecurityGroupsRequest | None = None,
    ) -> ReadSecurityGroupsResponse:
        request = _validate_request(ReadSecurityGroupsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadSecurityGroups",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadSecurityGroupsResponse, response)

    async def read_server_certificates(
        self,
        request: ReadServerCertificatesRequest | None = None,
    ) -> ReadServerCertificatesResponse:
        request = _validate_request(ReadServerCertificatesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadServerCertificates",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadServerCertificatesResponse, response)

    async def read_snapshot_export_tasks(
        self,
        request: ReadSnapshotExportTasksRequest | None = None,
    ) -> ReadSnapshotExportTasksResponse:
        request = _validate_request(ReadSnapshotExportTasksRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadSnapshotExportTasks",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadSnapshotExportTasksResponse, response)

    async def read_snapshots(
        self,
        request: ReadSnapshotsRequest | None = None,
    ) -> ReadSnapshotsResponse:
        request = _validate_request(ReadSnapshotsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadSnapshots",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadSnapshotsResponse, response)

    async def read_subnets(
        self,
        request: ReadSubnetsRequest | None = None,
    ) -> ReadSubnetsResponse:
        request = _validate_request(ReadSubnetsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadSubnets",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadSubnetsResponse, response)

    async def read_subregions(
        self,
        request: ReadSubregionsRequest | None = None,
    ) -> ReadSubregionsResponse:
        request = _validate_request(ReadSubregionsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadSubregions",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadSubregionsResponse, response)

    async def read_tags(
        self,
        request: ReadTagsRequest | None = None,
    ) -> ReadTagsResponse:
        request = _validate_request(ReadTagsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadTags",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadTagsResponse, response)

    async def read_unit_price(
        self,
        request: ReadUnitPriceRequest | None = None,
    ) -> ReadUnitPriceResponse:
        request = _validate_request(ReadUnitPriceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUnitPrice",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUnitPriceResponse, response)

    async def read_user_group(
        self,
        request: ReadUserGroupRequest | None = None,
    ) -> ReadUserGroupResponse:
        request = _validate_request(ReadUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUserGroupResponse, response)

    async def read_user_group_policies(
        self,
        request: ReadUserGroupPoliciesRequest | None = None,
    ) -> ReadUserGroupPoliciesResponse:
        request = _validate_request(ReadUserGroupPoliciesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUserGroupPolicies",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUserGroupPoliciesResponse, response)

    async def read_user_group_policy(
        self,
        request: ReadUserGroupPolicyRequest | None = None,
    ) -> ReadUserGroupPolicyResponse:
        request = _validate_request(ReadUserGroupPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUserGroupPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUserGroupPolicyResponse, response)

    async def read_user_groups(
        self,
        request: ReadUserGroupsRequest | None = None,
    ) -> ReadUserGroupsResponse:
        request = _validate_request(ReadUserGroupsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUserGroups",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUserGroupsResponse, response)

    async def read_user_groups_per_user(
        self,
        request: ReadUserGroupsPerUserRequest | None = None,
    ) -> ReadUserGroupsPerUserResponse:
        request = _validate_request(ReadUserGroupsPerUserRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUserGroupsPerUser",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUserGroupsPerUserResponse, response)

    async def read_user_policies(
        self,
        request: ReadUserPoliciesRequest | None = None,
    ) -> ReadUserPoliciesResponse:
        request = _validate_request(ReadUserPoliciesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUserPolicies",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUserPoliciesResponse, response)

    async def read_user_policy(
        self,
        request: ReadUserPolicyRequest | None = None,
    ) -> ReadUserPolicyResponse:
        request = _validate_request(ReadUserPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUserPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUserPolicyResponse, response)

    async def read_users(
        self,
        request: ReadUsersRequest | None = None,
    ) -> ReadUsersResponse:
        request = _validate_request(ReadUsersRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadUsers",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadUsersResponse, response)

    async def read_virtual_gateways(
        self,
        request: ReadVirtualGatewaysRequest | None = None,
    ) -> ReadVirtualGatewaysResponse:
        request = _validate_request(ReadVirtualGatewaysRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVirtualGateways",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVirtualGatewaysResponse, response)

    async def read_vm_groups(
        self,
        request: ReadVmGroupsRequest | None = None,
    ) -> ReadVmGroupsResponse:
        request = _validate_request(ReadVmGroupsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVmGroups",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVmGroupsResponse, response)

    async def read_vm_templates(
        self,
        request: ReadVmTemplatesRequest | None = None,
    ) -> ReadVmTemplatesResponse:
        request = _validate_request(ReadVmTemplatesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVmTemplates",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVmTemplatesResponse, response)

    async def read_vm_types(
        self,
        request: ReadVmTypesRequest | None = None,
    ) -> ReadVmTypesResponse:
        request = _validate_request(ReadVmTypesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVmTypes",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVmTypesResponse, response)

    async def read_vms(
        self,
        request: ReadVmsRequest | None = None,
    ) -> ReadVmsResponse:
        request = _validate_request(ReadVmsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVms",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVmsResponse, response)

    async def read_vms_health(
        self,
        request: ReadVmsHealthRequest | None = None,
    ) -> ReadVmsHealthResponse:
        request = _validate_request(ReadVmsHealthRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVmsHealth",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVmsHealthResponse, response)

    async def read_vms_state(
        self,
        request: ReadVmsStateRequest | None = None,
    ) -> ReadVmsStateResponse:
        request = _validate_request(ReadVmsStateRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVmsState",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVmsStateResponse, response)

    async def read_vms_stop_history(
        self,
        request: ReadVmsStopHistoryRequest | None = None,
    ) -> ReadVmsStopHistoryResponse:
        request = _validate_request(ReadVmsStopHistoryRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVmsStopHistory",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVmsStopHistoryResponse, response)

    async def read_volume_update_tasks(
        self,
        request: ReadVolumeUpdateTasksRequest | None = None,
    ) -> ReadVolumeUpdateTasksResponse:
        request = _validate_request(ReadVolumeUpdateTasksRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVolumeUpdateTasks",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVolumeUpdateTasksResponse, response)

    async def read_volumes(
        self,
        request: ReadVolumesRequest | None = None,
    ) -> ReadVolumesResponse:
        request = _validate_request(ReadVolumesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVolumes",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVolumesResponse, response)

    async def read_vpn_connections(
        self,
        request: ReadVpnConnectionsRequest | None = None,
    ) -> ReadVpnConnectionsResponse:
        request = _validate_request(ReadVpnConnectionsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ReadVpnConnections",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ReadVpnConnectionsResponse, response)

    async def reboot_vms(
        self,
        request: RebootVmsRequest | None = None,
    ) -> RebootVmsResponse:
        request = _validate_request(RebootVmsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/RebootVms",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(RebootVmsResponse, response)

    async def register_vms_in_load_balancer(
        self,
        request: RegisterVmsInLoadBalancerRequest | None = None,
    ) -> RegisterVmsInLoadBalancerResponse:
        request = _validate_request(RegisterVmsInLoadBalancerRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/RegisterVmsInLoadBalancer",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(RegisterVmsInLoadBalancerResponse, response)

    async def reject_net_peering(
        self,
        request: RejectNetPeeringRequest | None = None,
    ) -> RejectNetPeeringResponse:
        request = _validate_request(RejectNetPeeringRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/RejectNetPeering",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(RejectNetPeeringResponse, response)

    async def remove_user_from_user_group(
        self,
        request: RemoveUserFromUserGroupRequest | None = None,
    ) -> RemoveUserFromUserGroupResponse:
        request = _validate_request(RemoveUserFromUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/RemoveUserFromUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(RemoveUserFromUserGroupResponse, response)

    async def scale_down_vm_group(
        self,
        request: ScaleDownVmGroupRequest | None = None,
    ) -> ScaleDownVmGroupResponse:
        request = _validate_request(ScaleDownVmGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ScaleDownVmGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ScaleDownVmGroupResponse, response)

    async def scale_up_vm_group(
        self,
        request: ScaleUpVmGroupRequest | None = None,
    ) -> ScaleUpVmGroupResponse:
        request = _validate_request(ScaleUpVmGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/ScaleUpVmGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(ScaleUpVmGroupResponse, response)

    async def set_default_policy_version(
        self,
        request: SetDefaultPolicyVersionRequest | None = None,
    ) -> SetDefaultPolicyVersionResponse:
        request = _validate_request(SetDefaultPolicyVersionRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/SetDefaultPolicyVersion",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(SetDefaultPolicyVersionResponse, response)

    async def start_vms(
        self,
        request: StartVmsRequest | None = None,
    ) -> StartVmsResponse:
        request = _validate_request(StartVmsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/StartVms",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(StartVmsResponse, response)

    async def stop_vms(
        self,
        request: StopVmsRequest | None = None,
    ) -> StopVmsResponse:
        request = _validate_request(StopVmsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/StopVms",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(StopVmsResponse, response)

    async def unlink_flexible_gpu(
        self,
        request: UnlinkFlexibleGpuRequest | None = None,
    ) -> UnlinkFlexibleGpuResponse:
        request = _validate_request(UnlinkFlexibleGpuRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkFlexibleGpu",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkFlexibleGpuResponse, response)

    async def unlink_internet_service(
        self,
        request: UnlinkInternetServiceRequest | None = None,
    ) -> UnlinkInternetServiceResponse:
        request = _validate_request(UnlinkInternetServiceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkInternetService",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkInternetServiceResponse, response)

    async def unlink_load_balancer_backend_machines(
        self,
        request: UnlinkLoadBalancerBackendMachinesRequest | None = None,
    ) -> UnlinkLoadBalancerBackendMachinesResponse:
        request = _validate_request(UnlinkLoadBalancerBackendMachinesRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkLoadBalancerBackendMachines",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkLoadBalancerBackendMachinesResponse, response)

    async def unlink_managed_policy_from_user_group(
        self,
        request: UnlinkManagedPolicyFromUserGroupRequest | None = None,
    ) -> UnlinkManagedPolicyFromUserGroupResponse:
        request = _validate_request(UnlinkManagedPolicyFromUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkManagedPolicyFromUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkManagedPolicyFromUserGroupResponse, response)

    async def unlink_nic(
        self,
        request: UnlinkNicRequest | None = None,
    ) -> UnlinkNicResponse:
        request = _validate_request(UnlinkNicRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkNic",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkNicResponse, response)

    async def unlink_policy(
        self,
        request: UnlinkPolicyRequest | None = None,
    ) -> UnlinkPolicyResponse:
        request = _validate_request(UnlinkPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkPolicyResponse, response)

    async def unlink_private_ips(
        self,
        request: UnlinkPrivateIpsRequest | None = None,
    ) -> UnlinkPrivateIpsResponse:
        request = _validate_request(UnlinkPrivateIpsRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkPrivateIps",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkPrivateIpsResponse, response)

    async def unlink_public_ip(
        self,
        request: UnlinkPublicIpRequest | None = None,
    ) -> UnlinkPublicIpResponse:
        request = _validate_request(UnlinkPublicIpRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkPublicIp",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkPublicIpResponse, response)

    async def unlink_route_table(
        self,
        request: UnlinkRouteTableRequest | None = None,
    ) -> UnlinkRouteTableResponse:
        request = _validate_request(UnlinkRouteTableRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkRouteTable",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkRouteTableResponse, response)

    async def unlink_virtual_gateway(
        self,
        request: UnlinkVirtualGatewayRequest | None = None,
    ) -> UnlinkVirtualGatewayResponse:
        request = _validate_request(UnlinkVirtualGatewayRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkVirtualGateway",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkVirtualGatewayResponse, response)

    async def unlink_volume(
        self,
        request: UnlinkVolumeRequest | None = None,
    ) -> UnlinkVolumeResponse:
        request = _validate_request(UnlinkVolumeRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UnlinkVolume",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UnlinkVolumeResponse, response)

    async def update_access_key(
        self,
        request: UpdateAccessKeyRequest | None = None,
    ) -> UpdateAccessKeyResponse:
        request = _validate_request(UpdateAccessKeyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateAccessKey",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateAccessKeyResponse, response)

    async def update_account(
        self,
        request: UpdateAccountRequest | None = None,
    ) -> UpdateAccountResponse:
        request = _validate_request(UpdateAccountRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateAccount",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateAccountResponse, response)

    async def update_api_access_policy(
        self,
        request: UpdateApiAccessPolicyRequest | None = None,
    ) -> UpdateApiAccessPolicyResponse:
        request = _validate_request(UpdateApiAccessPolicyRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateApiAccessPolicy",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateApiAccessPolicyResponse, response)

    async def update_api_access_rule(
        self,
        request: UpdateApiAccessRuleRequest | None = None,
    ) -> UpdateApiAccessRuleResponse:
        request = _validate_request(UpdateApiAccessRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateApiAccessRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateApiAccessRuleResponse, response)

    async def update_ca(
        self,
        request: UpdateCaRequest | None = None,
    ) -> UpdateCaResponse:
        request = _validate_request(UpdateCaRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateCa",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateCaResponse, response)

    async def update_dedicated_group(
        self,
        request: UpdateDedicatedGroupRequest | None = None,
    ) -> UpdateDedicatedGroupResponse:
        request = _validate_request(UpdateDedicatedGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateDedicatedGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateDedicatedGroupResponse, response)

    async def update_direct_link_interface(
        self,
        request: UpdateDirectLinkInterfaceRequest | None = None,
    ) -> UpdateDirectLinkInterfaceResponse:
        request = _validate_request(UpdateDirectLinkInterfaceRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateDirectLinkInterface",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateDirectLinkInterfaceResponse, response)

    async def update_flexible_gpu(
        self,
        request: UpdateFlexibleGpuRequest | None = None,
    ) -> UpdateFlexibleGpuResponse:
        request = _validate_request(UpdateFlexibleGpuRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateFlexibleGpu",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateFlexibleGpuResponse, response)

    async def update_image(
        self,
        request: UpdateImageRequest | None = None,
    ) -> UpdateImageResponse:
        request = _validate_request(UpdateImageRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateImage",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateImageResponse, response)

    async def update_listener_rule(
        self,
        request: UpdateListenerRuleRequest | None = None,
    ) -> UpdateListenerRuleResponse:
        request = _validate_request(UpdateListenerRuleRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateListenerRule",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateListenerRuleResponse, response)

    async def update_load_balancer(
        self,
        request: UpdateLoadBalancerRequest | None = None,
    ) -> UpdateLoadBalancerResponse:
        request = _validate_request(UpdateLoadBalancerRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateLoadBalancer",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateLoadBalancerResponse, response)

    async def update_net(
        self,
        request: UpdateNetRequest | None = None,
    ) -> UpdateNetResponse:
        request = _validate_request(UpdateNetRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateNet",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateNetResponse, response)

    async def update_net_access_point(
        self,
        request: UpdateNetAccessPointRequest | None = None,
    ) -> UpdateNetAccessPointResponse:
        request = _validate_request(UpdateNetAccessPointRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateNetAccessPoint",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateNetAccessPointResponse, response)

    async def update_nic(
        self,
        request: UpdateNicRequest | None = None,
    ) -> UpdateNicResponse:
        request = _validate_request(UpdateNicRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateNic",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateNicResponse, response)

    async def update_route(
        self,
        request: UpdateRouteRequest | None = None,
    ) -> UpdateRouteResponse:
        request = _validate_request(UpdateRouteRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateRoute",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateRouteResponse, response)

    async def update_route_propagation(
        self,
        request: UpdateRoutePropagationRequest | None = None,
    ) -> UpdateRoutePropagationResponse:
        request = _validate_request(UpdateRoutePropagationRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateRoutePropagation",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateRoutePropagationResponse, response)

    async def update_route_table_link(
        self,
        request: UpdateRouteTableLinkRequest | None = None,
    ) -> UpdateRouteTableLinkResponse:
        request = _validate_request(UpdateRouteTableLinkRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateRouteTableLink",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateRouteTableLinkResponse, response)

    async def update_server_certificate(
        self,
        request: UpdateServerCertificateRequest | None = None,
    ) -> UpdateServerCertificateResponse:
        request = _validate_request(UpdateServerCertificateRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateServerCertificate",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateServerCertificateResponse, response)

    async def update_snapshot(
        self,
        request: UpdateSnapshotRequest | None = None,
    ) -> UpdateSnapshotResponse:
        request = _validate_request(UpdateSnapshotRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateSnapshot",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateSnapshotResponse, response)

    async def update_subnet(
        self,
        request: UpdateSubnetRequest | None = None,
    ) -> UpdateSubnetResponse:
        request = _validate_request(UpdateSubnetRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateSubnet",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateSubnetResponse, response)

    async def update_user(
        self,
        request: UpdateUserRequest | None = None,
    ) -> UpdateUserResponse:
        request = _validate_request(UpdateUserRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateUser",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateUserResponse, response)

    async def update_user_group(
        self,
        request: UpdateUserGroupRequest | None = None,
    ) -> UpdateUserGroupResponse:
        request = _validate_request(UpdateUserGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateUserGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateUserGroupResponse, response)

    async def update_vm(
        self,
        request: UpdateVmRequest | None = None,
    ) -> UpdateVmResponse:
        request = _validate_request(UpdateVmRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateVm",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateVmResponse, response)

    async def update_vm_group(
        self,
        request: UpdateVmGroupRequest | None = None,
    ) -> UpdateVmGroupResponse:
        request = _validate_request(UpdateVmGroupRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateVmGroup",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateVmGroupResponse, response)

    async def update_vm_template(
        self,
        request: UpdateVmTemplateRequest | None = None,
    ) -> UpdateVmTemplateResponse:
        request = _validate_request(UpdateVmTemplateRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateVmTemplate",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateVmTemplateResponse, response)

    async def update_volume(
        self,
        request: UpdateVolumeRequest | None = None,
    ) -> UpdateVolumeResponse:
        request = _validate_request(UpdateVolumeRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateVolume",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateVolumeResponse, response)

    async def update_vpn_connection(
        self,
        request: UpdateVpnConnectionRequest | None = None,
    ) -> UpdateVpnConnectionResponse:
        request = _validate_request(UpdateVpnConnectionRequest, request)

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="api",
                method="POST",
                path="/UpdateVpnConnection",
                json_body=_dump_json_body(request),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return _validate_response(UpdateVpnConnectionResponse, response)
