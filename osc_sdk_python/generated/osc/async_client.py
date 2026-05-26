"""Generated typed OSC client slice.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator
"""

from typing import Any

from pydantic import TypeAdapter

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


class AsyncOscTypedMixin:
    async def accept_net_peering(
        self,
        request: AcceptNetPeeringRequest | None = None,
    ) -> AcceptNetPeeringResponse:
        if request is None:
            request = AcceptNetPeeringRequest()

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
        return TypeAdapter(AcceptNetPeeringResponse).validate_python(response)

    async def add_user_to_user_group(
        self,
        request: AddUserToUserGroupRequest | None = None,
    ) -> AddUserToUserGroupResponse:
        if request is None:
            request = AddUserToUserGroupRequest()

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
        return TypeAdapter(AddUserToUserGroupResponse).validate_python(response)

    async def check_authentication(
        self,
        request: CheckAuthenticationRequest | None = None,
    ) -> CheckAuthenticationResponse:
        if request is None:
            request = CheckAuthenticationRequest()

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
        return TypeAdapter(CheckAuthenticationResponse).validate_python(response)

    async def create_access_key(
        self,
        request: CreateAccessKeyRequest | None = None,
    ) -> CreateAccessKeyResponse:
        if request is None:
            request = CreateAccessKeyRequest()

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
        return TypeAdapter(CreateAccessKeyResponse).validate_python(response)

    async def create_account(
        self,
        request: CreateAccountRequest | None = None,
    ) -> CreateAccountResponse:
        if request is None:
            request = CreateAccountRequest()

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
        return TypeAdapter(CreateAccountResponse).validate_python(response)

    async def create_api_access_rule(
        self,
        request: CreateApiAccessRuleRequest | None = None,
    ) -> CreateApiAccessRuleResponse:
        if request is None:
            request = CreateApiAccessRuleRequest()

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
        return TypeAdapter(CreateApiAccessRuleResponse).validate_python(response)

    async def create_ca(
        self,
        request: CreateCaRequest | None = None,
    ) -> CreateCaResponse:
        if request is None:
            request = CreateCaRequest()

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
        return TypeAdapter(CreateCaResponse).validate_python(response)

    async def create_client_gateway(
        self,
        request: CreateClientGatewayRequest | None = None,
    ) -> CreateClientGatewayResponse:
        if request is None:
            request = CreateClientGatewayRequest()

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
        return TypeAdapter(CreateClientGatewayResponse).validate_python(response)

    async def create_dedicated_group(
        self,
        request: CreateDedicatedGroupRequest | None = None,
    ) -> CreateDedicatedGroupResponse:
        if request is None:
            request = CreateDedicatedGroupRequest()

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
        return TypeAdapter(CreateDedicatedGroupResponse).validate_python(response)

    async def create_dhcp_options(
        self,
        request: CreateDhcpOptionsRequest | None = None,
    ) -> CreateDhcpOptionsResponse:
        if request is None:
            request = CreateDhcpOptionsRequest()

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
        return TypeAdapter(CreateDhcpOptionsResponse).validate_python(response)

    async def create_direct_link(
        self,
        request: CreateDirectLinkRequest | None = None,
    ) -> CreateDirectLinkResponse:
        if request is None:
            request = CreateDirectLinkRequest()

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
        return TypeAdapter(CreateDirectLinkResponse).validate_python(response)

    async def create_direct_link_interface(
        self,
        request: CreateDirectLinkInterfaceRequest | None = None,
    ) -> CreateDirectLinkInterfaceResponse:
        if request is None:
            request = CreateDirectLinkInterfaceRequest()

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
        return TypeAdapter(CreateDirectLinkInterfaceResponse).validate_python(response)

    async def create_flexible_gpu(
        self,
        request: CreateFlexibleGpuRequest | None = None,
    ) -> CreateFlexibleGpuResponse:
        if request is None:
            request = CreateFlexibleGpuRequest()

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
        return TypeAdapter(CreateFlexibleGpuResponse).validate_python(response)

    async def create_image(
        self,
        request: CreateImageRequest | None = None,
    ) -> CreateImageResponse:
        if request is None:
            request = CreateImageRequest()

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
        return TypeAdapter(CreateImageResponse).validate_python(response)

    async def create_image_export_task(
        self,
        request: CreateImageExportTaskRequest | None = None,
    ) -> CreateImageExportTaskResponse:
        if request is None:
            request = CreateImageExportTaskRequest()

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
        return TypeAdapter(CreateImageExportTaskResponse).validate_python(response)

    async def create_internet_service(
        self,
        request: CreateInternetServiceRequest | None = None,
    ) -> CreateInternetServiceResponse:
        if request is None:
            request = CreateInternetServiceRequest()

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
        return TypeAdapter(CreateInternetServiceResponse).validate_python(response)

    async def create_keypair(
        self,
        request: CreateKeypairRequest | None = None,
    ) -> CreateKeypairResponse:
        if request is None:
            request = CreateKeypairRequest()

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
        return TypeAdapter(CreateKeypairResponse).validate_python(response)

    async def create_listener_rule(
        self,
        request: CreateListenerRuleRequest | None = None,
    ) -> CreateListenerRuleResponse:
        if request is None:
            request = CreateListenerRuleRequest()

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
        return TypeAdapter(CreateListenerRuleResponse).validate_python(response)

    async def create_load_balancer(
        self,
        request: CreateLoadBalancerRequest | None = None,
    ) -> CreateLoadBalancerResponse:
        if request is None:
            request = CreateLoadBalancerRequest()

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
        return TypeAdapter(CreateLoadBalancerResponse).validate_python(response)

    async def create_load_balancer_listeners(
        self,
        request: CreateLoadBalancerListenersRequest | None = None,
    ) -> CreateLoadBalancerListenersResponse:
        if request is None:
            request = CreateLoadBalancerListenersRequest()

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
        return TypeAdapter(CreateLoadBalancerListenersResponse).validate_python(response)

    async def create_load_balancer_policy(
        self,
        request: CreateLoadBalancerPolicyRequest | None = None,
    ) -> CreateLoadBalancerPolicyResponse:
        if request is None:
            request = CreateLoadBalancerPolicyRequest()

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
        return TypeAdapter(CreateLoadBalancerPolicyResponse).validate_python(response)

    async def create_load_balancer_tags(
        self,
        request: CreateLoadBalancerTagsRequest | None = None,
    ) -> CreateLoadBalancerTagsResponse:
        if request is None:
            request = CreateLoadBalancerTagsRequest()

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
        return TypeAdapter(CreateLoadBalancerTagsResponse).validate_python(response)

    async def create_nat_service(
        self,
        request: CreateNatServiceRequest | None = None,
    ) -> CreateNatServiceResponse:
        if request is None:
            request = CreateNatServiceRequest()

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
        return TypeAdapter(CreateNatServiceResponse).validate_python(response)

    async def create_net(
        self,
        request: CreateNetRequest | None = None,
    ) -> CreateNetResponse:
        if request is None:
            request = CreateNetRequest()

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
        return TypeAdapter(CreateNetResponse).validate_python(response)

    async def create_net_access_point(
        self,
        request: CreateNetAccessPointRequest | None = None,
    ) -> CreateNetAccessPointResponse:
        if request is None:
            request = CreateNetAccessPointRequest()

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
        return TypeAdapter(CreateNetAccessPointResponse).validate_python(response)

    async def create_net_peering(
        self,
        request: CreateNetPeeringRequest | None = None,
    ) -> CreateNetPeeringResponse:
        if request is None:
            request = CreateNetPeeringRequest()

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
        return TypeAdapter(CreateNetPeeringResponse).validate_python(response)

    async def create_nic(
        self,
        request: CreateNicRequest | None = None,
    ) -> CreateNicResponse:
        if request is None:
            request = CreateNicRequest()

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
        return TypeAdapter(CreateNicResponse).validate_python(response)

    async def create_policy(
        self,
        request: CreatePolicyRequest | None = None,
    ) -> CreatePolicyResponse:
        if request is None:
            request = CreatePolicyRequest()

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
        return TypeAdapter(CreatePolicyResponse).validate_python(response)

    async def create_policy_version(
        self,
        request: CreatePolicyVersionRequest | None = None,
    ) -> CreatePolicyVersionResponse:
        if request is None:
            request = CreatePolicyVersionRequest()

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
        return TypeAdapter(CreatePolicyVersionResponse).validate_python(response)

    async def create_product_type(
        self,
        request: CreateProductTypeRequest | None = None,
    ) -> CreateProductTypeResponse:
        if request is None:
            request = CreateProductTypeRequest()

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
        return TypeAdapter(CreateProductTypeResponse).validate_python(response)

    async def create_public_ip(
        self,
        request: CreatePublicIpRequest | None = None,
    ) -> CreatePublicIpResponse:
        if request is None:
            request = CreatePublicIpRequest()

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
        return TypeAdapter(CreatePublicIpResponse).validate_python(response)

    async def create_route(
        self,
        request: CreateRouteRequest | None = None,
    ) -> CreateRouteResponse:
        if request is None:
            request = CreateRouteRequest()

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
        return TypeAdapter(CreateRouteResponse).validate_python(response)

    async def create_route_table(
        self,
        request: CreateRouteTableRequest | None = None,
    ) -> CreateRouteTableResponse:
        if request is None:
            request = CreateRouteTableRequest()

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
        return TypeAdapter(CreateRouteTableResponse).validate_python(response)

    async def create_security_group(
        self,
        request: CreateSecurityGroupRequest | None = None,
    ) -> CreateSecurityGroupResponse:
        if request is None:
            request = CreateSecurityGroupRequest()

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
        return TypeAdapter(CreateSecurityGroupResponse).validate_python(response)

    async def create_security_group_rule(
        self,
        request: CreateSecurityGroupRuleRequest | None = None,
    ) -> CreateSecurityGroupRuleResponse:
        if request is None:
            request = CreateSecurityGroupRuleRequest()

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
        return TypeAdapter(CreateSecurityGroupRuleResponse).validate_python(response)

    async def create_server_certificate(
        self,
        request: CreateServerCertificateRequest | None = None,
    ) -> CreateServerCertificateResponse:
        if request is None:
            request = CreateServerCertificateRequest()

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
        return TypeAdapter(CreateServerCertificateResponse).validate_python(response)

    async def create_snapshot(
        self,
        request: CreateSnapshotRequest | None = None,
    ) -> CreateSnapshotResponse:
        if request is None:
            request = CreateSnapshotRequest()

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
        return TypeAdapter(CreateSnapshotResponse).validate_python(response)

    async def create_snapshot_export_task(
        self,
        request: CreateSnapshotExportTaskRequest | None = None,
    ) -> CreateSnapshotExportTaskResponse:
        if request is None:
            request = CreateSnapshotExportTaskRequest()

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
        return TypeAdapter(CreateSnapshotExportTaskResponse).validate_python(response)

    async def create_subnet(
        self,
        request: CreateSubnetRequest | None = None,
    ) -> CreateSubnetResponse:
        if request is None:
            request = CreateSubnetRequest()

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
        return TypeAdapter(CreateSubnetResponse).validate_python(response)

    async def create_tags(
        self,
        request: CreateTagsRequest | None = None,
    ) -> CreateTagsResponse:
        if request is None:
            request = CreateTagsRequest()

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
        return TypeAdapter(CreateTagsResponse).validate_python(response)

    async def create_user(
        self,
        request: CreateUserRequest | None = None,
    ) -> CreateUserResponse:
        if request is None:
            request = CreateUserRequest()

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
        return TypeAdapter(CreateUserResponse).validate_python(response)

    async def create_user_group(
        self,
        request: CreateUserGroupRequest | None = None,
    ) -> CreateUserGroupResponse:
        if request is None:
            request = CreateUserGroupRequest()

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
        return TypeAdapter(CreateUserGroupResponse).validate_python(response)

    async def create_virtual_gateway(
        self,
        request: CreateVirtualGatewayRequest | None = None,
    ) -> CreateVirtualGatewayResponse:
        if request is None:
            request = CreateVirtualGatewayRequest()

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
        return TypeAdapter(CreateVirtualGatewayResponse).validate_python(response)

    async def create_vm_group(
        self,
        request: CreateVmGroupRequest | None = None,
    ) -> CreateVmGroupResponse:
        if request is None:
            request = CreateVmGroupRequest()

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
        return TypeAdapter(CreateVmGroupResponse).validate_python(response)

    async def create_vm_template(
        self,
        request: CreateVmTemplateRequest | None = None,
    ) -> CreateVmTemplateResponse:
        if request is None:
            request = CreateVmTemplateRequest()

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
        return TypeAdapter(CreateVmTemplateResponse).validate_python(response)

    async def create_vms(
        self,
        request: CreateVmsRequest | None = None,
    ) -> CreateVmsResponse:
        if request is None:
            request = CreateVmsRequest()

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
        return TypeAdapter(CreateVmsResponse).validate_python(response)

    async def create_volume(
        self,
        request: CreateVolumeRequest | None = None,
    ) -> CreateVolumeResponse:
        if request is None:
            request = CreateVolumeRequest()

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
        return TypeAdapter(CreateVolumeResponse).validate_python(response)

    async def create_vpn_connection(
        self,
        request: CreateVpnConnectionRequest | None = None,
    ) -> CreateVpnConnectionResponse:
        if request is None:
            request = CreateVpnConnectionRequest()

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
        return TypeAdapter(CreateVpnConnectionResponse).validate_python(response)

    async def create_vpn_connection_route(
        self,
        request: CreateVpnConnectionRouteRequest | None = None,
    ) -> CreateVpnConnectionRouteResponse:
        if request is None:
            request = CreateVpnConnectionRouteRequest()

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
        return TypeAdapter(CreateVpnConnectionRouteResponse).validate_python(response)

    async def delete_access_key(
        self,
        request: DeleteAccessKeyRequest | None = None,
    ) -> DeleteAccessKeyResponse:
        if request is None:
            request = DeleteAccessKeyRequest()

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
        return TypeAdapter(DeleteAccessKeyResponse).validate_python(response)

    async def delete_api_access_rule(
        self,
        request: DeleteApiAccessRuleRequest | None = None,
    ) -> DeleteApiAccessRuleResponse:
        if request is None:
            request = DeleteApiAccessRuleRequest()

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
        return TypeAdapter(DeleteApiAccessRuleResponse).validate_python(response)

    async def delete_ca(
        self,
        request: DeleteCaRequest | None = None,
    ) -> DeleteCaResponse:
        if request is None:
            request = DeleteCaRequest()

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
        return TypeAdapter(DeleteCaResponse).validate_python(response)

    async def delete_client_gateway(
        self,
        request: DeleteClientGatewayRequest | None = None,
    ) -> DeleteClientGatewayResponse:
        if request is None:
            request = DeleteClientGatewayRequest()

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
        return TypeAdapter(DeleteClientGatewayResponse).validate_python(response)

    async def delete_dedicated_group(
        self,
        request: DeleteDedicatedGroupRequest | None = None,
    ) -> DeleteDedicatedGroupResponse:
        if request is None:
            request = DeleteDedicatedGroupRequest()

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
        return TypeAdapter(DeleteDedicatedGroupResponse).validate_python(response)

    async def delete_dhcp_options(
        self,
        request: DeleteDhcpOptionsRequest | None = None,
    ) -> DeleteDhcpOptionsResponse:
        if request is None:
            request = DeleteDhcpOptionsRequest()

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
        return TypeAdapter(DeleteDhcpOptionsResponse).validate_python(response)

    async def delete_direct_link(
        self,
        request: DeleteDirectLinkRequest | None = None,
    ) -> DeleteDirectLinkResponse:
        if request is None:
            request = DeleteDirectLinkRequest()

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
        return TypeAdapter(DeleteDirectLinkResponse).validate_python(response)

    async def delete_direct_link_interface(
        self,
        request: DeleteDirectLinkInterfaceRequest | None = None,
    ) -> DeleteDirectLinkInterfaceResponse:
        if request is None:
            request = DeleteDirectLinkInterfaceRequest()

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
        return TypeAdapter(DeleteDirectLinkInterfaceResponse).validate_python(response)

    async def delete_export_task(
        self,
        request: DeleteExportTaskRequest | None = None,
    ) -> DeleteExportTaskResponse:
        if request is None:
            request = DeleteExportTaskRequest()

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
        return TypeAdapter(DeleteExportTaskResponse).validate_python(response)

    async def delete_flexible_gpu(
        self,
        request: DeleteFlexibleGpuRequest | None = None,
    ) -> DeleteFlexibleGpuResponse:
        if request is None:
            request = DeleteFlexibleGpuRequest()

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
        return TypeAdapter(DeleteFlexibleGpuResponse).validate_python(response)

    async def delete_image(
        self,
        request: DeleteImageRequest | None = None,
    ) -> DeleteImageResponse:
        if request is None:
            request = DeleteImageRequest()

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
        return TypeAdapter(DeleteImageResponse).validate_python(response)

    async def delete_internet_service(
        self,
        request: DeleteInternetServiceRequest | None = None,
    ) -> DeleteInternetServiceResponse:
        if request is None:
            request = DeleteInternetServiceRequest()

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
        return TypeAdapter(DeleteInternetServiceResponse).validate_python(response)

    async def delete_keypair(
        self,
        request: DeleteKeypairRequest | None = None,
    ) -> DeleteKeypairResponse:
        if request is None:
            request = DeleteKeypairRequest()

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
        return TypeAdapter(DeleteKeypairResponse).validate_python(response)

    async def delete_listener_rule(
        self,
        request: DeleteListenerRuleRequest | None = None,
    ) -> DeleteListenerRuleResponse:
        if request is None:
            request = DeleteListenerRuleRequest()

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
        return TypeAdapter(DeleteListenerRuleResponse).validate_python(response)

    async def delete_load_balancer(
        self,
        request: DeleteLoadBalancerRequest | None = None,
    ) -> DeleteLoadBalancerResponse:
        if request is None:
            request = DeleteLoadBalancerRequest()

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
        return TypeAdapter(DeleteLoadBalancerResponse).validate_python(response)

    async def delete_load_balancer_listeners(
        self,
        request: DeleteLoadBalancerListenersRequest | None = None,
    ) -> DeleteLoadBalancerListenersResponse:
        if request is None:
            request = DeleteLoadBalancerListenersRequest()

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
        return TypeAdapter(DeleteLoadBalancerListenersResponse).validate_python(response)

    async def delete_load_balancer_policy(
        self,
        request: DeleteLoadBalancerPolicyRequest | None = None,
    ) -> DeleteLoadBalancerPolicyResponse:
        if request is None:
            request = DeleteLoadBalancerPolicyRequest()

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
        return TypeAdapter(DeleteLoadBalancerPolicyResponse).validate_python(response)

    async def delete_load_balancer_tags(
        self,
        request: DeleteLoadBalancerTagsRequest | None = None,
    ) -> DeleteLoadBalancerTagsResponse:
        if request is None:
            request = DeleteLoadBalancerTagsRequest()

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
        return TypeAdapter(DeleteLoadBalancerTagsResponse).validate_python(response)

    async def delete_nat_service(
        self,
        request: DeleteNatServiceRequest | None = None,
    ) -> DeleteNatServiceResponse:
        if request is None:
            request = DeleteNatServiceRequest()

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
        return TypeAdapter(DeleteNatServiceResponse).validate_python(response)

    async def delete_net(
        self,
        request: DeleteNetRequest | None = None,
    ) -> DeleteNetResponse:
        if request is None:
            request = DeleteNetRequest()

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
        return TypeAdapter(DeleteNetResponse).validate_python(response)

    async def delete_net_access_point(
        self,
        request: DeleteNetAccessPointRequest | None = None,
    ) -> DeleteNetAccessPointResponse:
        if request is None:
            request = DeleteNetAccessPointRequest()

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
        return TypeAdapter(DeleteNetAccessPointResponse).validate_python(response)

    async def delete_net_peering(
        self,
        request: DeleteNetPeeringRequest | None = None,
    ) -> DeleteNetPeeringResponse:
        if request is None:
            request = DeleteNetPeeringRequest()

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
        return TypeAdapter(DeleteNetPeeringResponse).validate_python(response)

    async def delete_nic(
        self,
        request: DeleteNicRequest | None = None,
    ) -> DeleteNicResponse:
        if request is None:
            request = DeleteNicRequest()

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
        return TypeAdapter(DeleteNicResponse).validate_python(response)

    async def delete_policy(
        self,
        request: DeletePolicyRequest | None = None,
    ) -> DeletePolicyResponse:
        if request is None:
            request = DeletePolicyRequest()

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
        return TypeAdapter(DeletePolicyResponse).validate_python(response)

    async def delete_policy_version(
        self,
        request: DeletePolicyVersionRequest | None = None,
    ) -> DeletePolicyVersionResponse:
        if request is None:
            request = DeletePolicyVersionRequest()

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
        return TypeAdapter(DeletePolicyVersionResponse).validate_python(response)

    async def delete_product_type(
        self,
        request: DeleteProductTypeRequest | None = None,
    ) -> DeleteProductTypeResponse:
        if request is None:
            request = DeleteProductTypeRequest()

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
        return TypeAdapter(DeleteProductTypeResponse).validate_python(response)

    async def delete_public_ip(
        self,
        request: DeletePublicIpRequest | None = None,
    ) -> DeletePublicIpResponse:
        if request is None:
            request = DeletePublicIpRequest()

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
        return TypeAdapter(DeletePublicIpResponse).validate_python(response)

    async def delete_route(
        self,
        request: DeleteRouteRequest | None = None,
    ) -> DeleteRouteResponse:
        if request is None:
            request = DeleteRouteRequest()

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
        return TypeAdapter(DeleteRouteResponse).validate_python(response)

    async def delete_route_table(
        self,
        request: DeleteRouteTableRequest | None = None,
    ) -> DeleteRouteTableResponse:
        if request is None:
            request = DeleteRouteTableRequest()

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
        return TypeAdapter(DeleteRouteTableResponse).validate_python(response)

    async def delete_security_group(
        self,
        request: DeleteSecurityGroupRequest | None = None,
    ) -> DeleteSecurityGroupResponse:
        if request is None:
            request = DeleteSecurityGroupRequest()

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
        return TypeAdapter(DeleteSecurityGroupResponse).validate_python(response)

    async def delete_security_group_rule(
        self,
        request: DeleteSecurityGroupRuleRequest | None = None,
    ) -> DeleteSecurityGroupRuleResponse:
        if request is None:
            request = DeleteSecurityGroupRuleRequest()

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
        return TypeAdapter(DeleteSecurityGroupRuleResponse).validate_python(response)

    async def delete_server_certificate(
        self,
        request: DeleteServerCertificateRequest | None = None,
    ) -> DeleteServerCertificateResponse:
        if request is None:
            request = DeleteServerCertificateRequest()

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
        return TypeAdapter(DeleteServerCertificateResponse).validate_python(response)

    async def delete_snapshot(
        self,
        request: DeleteSnapshotRequest | None = None,
    ) -> DeleteSnapshotResponse:
        if request is None:
            request = DeleteSnapshotRequest()

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
        return TypeAdapter(DeleteSnapshotResponse).validate_python(response)

    async def delete_subnet(
        self,
        request: DeleteSubnetRequest | None = None,
    ) -> DeleteSubnetResponse:
        if request is None:
            request = DeleteSubnetRequest()

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
        return TypeAdapter(DeleteSubnetResponse).validate_python(response)

    async def delete_tags(
        self,
        request: DeleteTagsRequest | None = None,
    ) -> DeleteTagsResponse:
        if request is None:
            request = DeleteTagsRequest()

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
        return TypeAdapter(DeleteTagsResponse).validate_python(response)

    async def delete_user(
        self,
        request: DeleteUserRequest | None = None,
    ) -> DeleteUserResponse:
        if request is None:
            request = DeleteUserRequest()

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
        return TypeAdapter(DeleteUserResponse).validate_python(response)

    async def delete_user_group(
        self,
        request: DeleteUserGroupRequest | None = None,
    ) -> DeleteUserGroupResponse:
        if request is None:
            request = DeleteUserGroupRequest()

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
        return TypeAdapter(DeleteUserGroupResponse).validate_python(response)

    async def delete_user_group_policy(
        self,
        request: DeleteUserGroupPolicyRequest | None = None,
    ) -> DeleteUserGroupPolicyResponse:
        if request is None:
            request = DeleteUserGroupPolicyRequest()

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
        return TypeAdapter(DeleteUserGroupPolicyResponse).validate_python(response)

    async def delete_user_policy(
        self,
        request: DeleteUserPolicyRequest | None = None,
    ) -> DeleteUserPolicyResponse:
        if request is None:
            request = DeleteUserPolicyRequest()

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
        return TypeAdapter(DeleteUserPolicyResponse).validate_python(response)

    async def delete_virtual_gateway(
        self,
        request: DeleteVirtualGatewayRequest | None = None,
    ) -> DeleteVirtualGatewayResponse:
        if request is None:
            request = DeleteVirtualGatewayRequest()

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
        return TypeAdapter(DeleteVirtualGatewayResponse).validate_python(response)

    async def delete_vm_group(
        self,
        request: DeleteVmGroupRequest | None = None,
    ) -> DeleteVmGroupResponse:
        if request is None:
            request = DeleteVmGroupRequest()

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
        return TypeAdapter(DeleteVmGroupResponse).validate_python(response)

    async def delete_vm_template(
        self,
        request: DeleteVmTemplateRequest | None = None,
    ) -> DeleteVmTemplateResponse:
        if request is None:
            request = DeleteVmTemplateRequest()

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
        return TypeAdapter(DeleteVmTemplateResponse).validate_python(response)

    async def delete_vms(
        self,
        request: DeleteVmsRequest | None = None,
    ) -> DeleteVmsResponse:
        if request is None:
            request = DeleteVmsRequest()

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
        return TypeAdapter(DeleteVmsResponse).validate_python(response)

    async def delete_volume(
        self,
        request: DeleteVolumeRequest | None = None,
    ) -> DeleteVolumeResponse:
        if request is None:
            request = DeleteVolumeRequest()

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
        return TypeAdapter(DeleteVolumeResponse).validate_python(response)

    async def delete_vpn_connection(
        self,
        request: DeleteVpnConnectionRequest | None = None,
    ) -> DeleteVpnConnectionResponse:
        if request is None:
            request = DeleteVpnConnectionRequest()

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
        return TypeAdapter(DeleteVpnConnectionResponse).validate_python(response)

    async def delete_vpn_connection_route(
        self,
        request: DeleteVpnConnectionRouteRequest | None = None,
    ) -> DeleteVpnConnectionRouteResponse:
        if request is None:
            request = DeleteVpnConnectionRouteRequest()

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
        return TypeAdapter(DeleteVpnConnectionRouteResponse).validate_python(response)

    async def deregister_vms_in_load_balancer(
        self,
        request: DeregisterVmsInLoadBalancerRequest | None = None,
    ) -> DeregisterVmsInLoadBalancerResponse:
        if request is None:
            request = DeregisterVmsInLoadBalancerRequest()

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
        return TypeAdapter(DeregisterVmsInLoadBalancerResponse).validate_python(response)

    async def disable_outscale_login(
        self,
        request: DisableOutscaleLoginRequest | None = None,
    ) -> DisableOutscaleLoginResponse:
        if request is None:
            request = DisableOutscaleLoginRequest()

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
        return TypeAdapter(DisableOutscaleLoginResponse).validate_python(response)

    async def disable_outscale_login_for_users(
        self,
        request: DisableOutscaleLoginRequest | None = None,
    ) -> DisableOutscaleLoginResponse:
        if request is None:
            request = DisableOutscaleLoginRequest()

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
        return TypeAdapter(DisableOutscaleLoginResponse).validate_python(response)

    async def disable_outscale_login_per_users(
        self,
        request: DisableOutscaleLoginPerUsersRequest | None = None,
    ) -> DisableOutscaleLoginPerUsersResponse:
        if request is None:
            request = DisableOutscaleLoginPerUsersRequest()

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
        return TypeAdapter(DisableOutscaleLoginPerUsersResponse).validate_python(response)

    async def enable_outscale_login(
        self,
        request: EnableOutscaleLoginRequest | None = None,
    ) -> EnableOutscaleLoginResponse:
        if request is None:
            request = EnableOutscaleLoginRequest()

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
        return TypeAdapter(EnableOutscaleLoginResponse).validate_python(response)

    async def enable_outscale_login_for_users(
        self,
        request: EnableOutscaleLoginForUsersRequest | None = None,
    ) -> EnableOutscaleLoginForUsersResponse:
        if request is None:
            request = EnableOutscaleLoginForUsersRequest()

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
        return TypeAdapter(EnableOutscaleLoginForUsersResponse).validate_python(response)

    async def enable_outscale_login_per_users(
        self,
        request: EnableOutscaleLoginPerUsersRequest | None = None,
    ) -> EnableOutscaleLoginPerUsersResponse:
        if request is None:
            request = EnableOutscaleLoginPerUsersRequest()

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
        return TypeAdapter(EnableOutscaleLoginPerUsersResponse).validate_python(response)

    async def link_flexible_gpu(
        self,
        request: LinkFlexibleGpuRequest | None = None,
    ) -> LinkFlexibleGpuResponse:
        if request is None:
            request = LinkFlexibleGpuRequest()

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
        return TypeAdapter(LinkFlexibleGpuResponse).validate_python(response)

    async def link_internet_service(
        self,
        request: LinkInternetServiceRequest | None = None,
    ) -> LinkInternetServiceResponse:
        if request is None:
            request = LinkInternetServiceRequest()

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
        return TypeAdapter(LinkInternetServiceResponse).validate_python(response)

    async def link_load_balancer_backend_machines(
        self,
        request: LinkLoadBalancerBackendMachinesRequest | None = None,
    ) -> LinkLoadBalancerBackendMachinesResponse:
        if request is None:
            request = LinkLoadBalancerBackendMachinesRequest()

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
        return TypeAdapter(LinkLoadBalancerBackendMachinesResponse).validate_python(response)

    async def link_managed_policy_to_user_group(
        self,
        request: LinkManagedPolicyToUserGroupRequest | None = None,
    ) -> LinkManagedPolicyToUserGroupResponse:
        if request is None:
            request = LinkManagedPolicyToUserGroupRequest()

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
        return TypeAdapter(LinkManagedPolicyToUserGroupResponse).validate_python(response)

    async def link_nic(
        self,
        request: LinkNicRequest | None = None,
    ) -> LinkNicResponse:
        if request is None:
            request = LinkNicRequest()

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
        return TypeAdapter(LinkNicResponse).validate_python(response)

    async def link_policy(
        self,
        request: LinkPolicyRequest | None = None,
    ) -> LinkPolicyResponse:
        if request is None:
            request = LinkPolicyRequest()

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
        return TypeAdapter(LinkPolicyResponse).validate_python(response)

    async def link_private_ips(
        self,
        request: LinkPrivateIpsRequest | None = None,
    ) -> LinkPrivateIpsResponse:
        if request is None:
            request = LinkPrivateIpsRequest()

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
        return TypeAdapter(LinkPrivateIpsResponse).validate_python(response)

    async def link_public_ip(
        self,
        request: LinkPublicIpRequest | None = None,
    ) -> LinkPublicIpResponse:
        if request is None:
            request = LinkPublicIpRequest()

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
        return TypeAdapter(LinkPublicIpResponse).validate_python(response)

    async def link_route_table(
        self,
        request: LinkRouteTableRequest | None = None,
    ) -> LinkRouteTableResponse:
        if request is None:
            request = LinkRouteTableRequest()

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
        return TypeAdapter(LinkRouteTableResponse).validate_python(response)

    async def link_virtual_gateway(
        self,
        request: LinkVirtualGatewayRequest | None = None,
    ) -> LinkVirtualGatewayResponse:
        if request is None:
            request = LinkVirtualGatewayRequest()

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
        return TypeAdapter(LinkVirtualGatewayResponse).validate_python(response)

    async def link_volume(
        self,
        request: LinkVolumeRequest | None = None,
    ) -> LinkVolumeResponse:
        if request is None:
            request = LinkVolumeRequest()

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
        return TypeAdapter(LinkVolumeResponse).validate_python(response)

    async def put_user_group_policy(
        self,
        request: PutUserGroupPolicyRequest | None = None,
    ) -> PutUserGroupPolicyResponse:
        if request is None:
            request = PutUserGroupPolicyRequest()

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
        return TypeAdapter(PutUserGroupPolicyResponse).validate_python(response)

    async def put_user_policy(
        self,
        request: PutUserPolicyRequest | None = None,
    ) -> PutUserPolicyResponse:
        if request is None:
            request = PutUserPolicyRequest()

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
        return TypeAdapter(PutUserPolicyResponse).validate_python(response)

    async def read_access_keys(
        self,
        request: ReadAccessKeysRequest | None = None,
    ) -> ReadAccessKeysResponse:
        if request is None:
            request = ReadAccessKeysRequest()

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
        return TypeAdapter(ReadAccessKeysResponse).validate_python(response)

    async def read_accounts(
        self,
        request: ReadAccountsRequest | None = None,
    ) -> ReadAccountsResponse:
        if request is None:
            request = ReadAccountsRequest()

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
        return TypeAdapter(ReadAccountsResponse).validate_python(response)

    async def read_admin_password(
        self,
        request: ReadAdminPasswordRequest | None = None,
    ) -> ReadAdminPasswordResponse:
        if request is None:
            request = ReadAdminPasswordRequest()

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
        return TypeAdapter(ReadAdminPasswordResponse).validate_python(response)

    async def read_api_access_policy(
        self,
        request: ReadApiAccessPolicyRequest | None = None,
    ) -> ReadApiAccessPolicyResponse:
        if request is None:
            request = ReadApiAccessPolicyRequest()

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
        return TypeAdapter(ReadApiAccessPolicyResponse).validate_python(response)

    async def read_api_access_rules(
        self,
        request: ReadApiAccessRulesRequest | None = None,
    ) -> ReadApiAccessRulesResponse:
        if request is None:
            request = ReadApiAccessRulesRequest()

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
        return TypeAdapter(ReadApiAccessRulesResponse).validate_python(response)

    async def read_api_logs(
        self,
        request: ReadApiLogsRequest | None = None,
    ) -> ReadApiLogsResponse:
        if request is None:
            request = ReadApiLogsRequest()

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
        return TypeAdapter(ReadApiLogsResponse).validate_python(response)

    async def read_co2_emission_account(
        self,
        request: ReadCO2EmissionAccountRequest | None = None,
    ) -> ReadCO2EmissionAccountResponse:
        if request is None:
            request = ReadCO2EmissionAccountRequest()

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
        return TypeAdapter(ReadCO2EmissionAccountResponse).validate_python(response)

    async def read_cas(
        self,
        request: ReadCasRequest | None = None,
    ) -> ReadCasResponse:
        if request is None:
            request = ReadCasRequest()

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
        return TypeAdapter(ReadCasResponse).validate_python(response)

    async def read_catalog(
        self,
        request: ReadCatalogRequest | None = None,
    ) -> ReadCatalogResponse:
        if request is None:
            request = ReadCatalogRequest()

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
        return TypeAdapter(ReadCatalogResponse).validate_python(response)

    async def read_catalogs(
        self,
        request: ReadCatalogsRequest | None = None,
    ) -> ReadCatalogsResponse:
        if request is None:
            request = ReadCatalogsRequest()

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
        return TypeAdapter(ReadCatalogsResponse).validate_python(response)

    async def read_client_gateways(
        self,
        request: ReadClientGatewaysRequest | None = None,
    ) -> ReadClientGatewaysResponse:
        if request is None:
            request = ReadClientGatewaysRequest()

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
        return TypeAdapter(ReadClientGatewaysResponse).validate_python(response)

    async def read_console_output(
        self,
        request: ReadConsoleOutputRequest | None = None,
    ) -> ReadConsoleOutputResponse:
        if request is None:
            request = ReadConsoleOutputRequest()

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
        return TypeAdapter(ReadConsoleOutputResponse).validate_python(response)

    async def read_consumption_account(
        self,
        request: ReadConsumptionAccountRequest | None = None,
    ) -> ReadConsumptionAccountResponse:
        if request is None:
            request = ReadConsumptionAccountRequest()

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
        return TypeAdapter(ReadConsumptionAccountResponse).validate_python(response)

    async def read_dedicated_groups(
        self,
        request: ReadDedicatedGroupsRequest | None = None,
    ) -> ReadDedicatedGroupsResponse:
        if request is None:
            request = ReadDedicatedGroupsRequest()

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
        return TypeAdapter(ReadDedicatedGroupsResponse).validate_python(response)

    async def read_dhcp_options(
        self,
        request: ReadDhcpOptionsRequest | None = None,
    ) -> ReadDhcpOptionsResponse:
        if request is None:
            request = ReadDhcpOptionsRequest()

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
        return TypeAdapter(ReadDhcpOptionsResponse).validate_python(response)

    async def read_direct_link_interfaces(
        self,
        request: ReadDirectLinkInterfacesRequest | None = None,
    ) -> ReadDirectLinkInterfacesResponse:
        if request is None:
            request = ReadDirectLinkInterfacesRequest()

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
        return TypeAdapter(ReadDirectLinkInterfacesResponse).validate_python(response)

    async def read_direct_links(
        self,
        request: ReadDirectLinksRequest | None = None,
    ) -> ReadDirectLinksResponse:
        if request is None:
            request = ReadDirectLinksRequest()

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
        return TypeAdapter(ReadDirectLinksResponse).validate_python(response)

    async def read_entities_linked_to_policy(
        self,
        request: ReadEntitiesLinkedToPolicyRequest | None = None,
    ) -> ReadEntitiesLinkedToPolicyResponse:
        if request is None:
            request = ReadEntitiesLinkedToPolicyRequest()

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
        return TypeAdapter(ReadEntitiesLinkedToPolicyResponse).validate_python(response)

    async def read_flexible_gpu_catalog(
        self,
        request: ReadFlexibleGpuCatalogRequest | None = None,
    ) -> ReadFlexibleGpuCatalogResponse:
        if request is None:
            request = ReadFlexibleGpuCatalogRequest()

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
        return TypeAdapter(ReadFlexibleGpuCatalogResponse).validate_python(response)

    async def read_flexible_gpus(
        self,
        request: ReadFlexibleGpusRequest | None = None,
    ) -> ReadFlexibleGpusResponse:
        if request is None:
            request = ReadFlexibleGpusRequest()

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
        return TypeAdapter(ReadFlexibleGpusResponse).validate_python(response)

    async def read_image_export_tasks(
        self,
        request: ReadImageExportTasksRequest | None = None,
    ) -> ReadImageExportTasksResponse:
        if request is None:
            request = ReadImageExportTasksRequest()

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
        return TypeAdapter(ReadImageExportTasksResponse).validate_python(response)

    async def read_images(
        self,
        request: ReadImagesRequest | None = None,
    ) -> ReadImagesResponse:
        if request is None:
            request = ReadImagesRequest()

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
        return TypeAdapter(ReadImagesResponse).validate_python(response)

    async def read_internet_services(
        self,
        request: ReadInternetServicesRequest | None = None,
    ) -> ReadInternetServicesResponse:
        if request is None:
            request = ReadInternetServicesRequest()

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
        return TypeAdapter(ReadInternetServicesResponse).validate_python(response)

    async def read_keypairs(
        self,
        request: ReadKeypairsRequest | None = None,
    ) -> ReadKeypairsResponse:
        if request is None:
            request = ReadKeypairsRequest()

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
        return TypeAdapter(ReadKeypairsResponse).validate_python(response)

    async def read_linked_policies(
        self,
        request: ReadLinkedPoliciesRequest | None = None,
    ) -> ReadLinkedPoliciesResponse:
        if request is None:
            request = ReadLinkedPoliciesRequest()

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
        return TypeAdapter(ReadLinkedPoliciesResponse).validate_python(response)

    async def read_listener_rules(
        self,
        request: ReadListenerRulesRequest | None = None,
    ) -> ReadListenerRulesResponse:
        if request is None:
            request = ReadListenerRulesRequest()

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
        return TypeAdapter(ReadListenerRulesResponse).validate_python(response)

    async def read_load_balancer_tags(
        self,
        request: ReadLoadBalancerTagsRequest | None = None,
    ) -> ReadLoadBalancerTagsResponse:
        if request is None:
            request = ReadLoadBalancerTagsRequest()

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
        return TypeAdapter(ReadLoadBalancerTagsResponse).validate_python(response)

    async def read_load_balancers(
        self,
        request: ReadLoadBalancersRequest | None = None,
    ) -> ReadLoadBalancersResponse:
        if request is None:
            request = ReadLoadBalancersRequest()

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
        return TypeAdapter(ReadLoadBalancersResponse).validate_python(response)

    async def read_locations(
        self,
        request: ReadLocationsRequest | None = None,
    ) -> ReadLocationsResponse:
        if request is None:
            request = ReadLocationsRequest()

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
        return TypeAdapter(ReadLocationsResponse).validate_python(response)

    async def read_managed_policies_linked_to_user_group(
        self,
        request: ReadManagedPoliciesLinkedToUserGroupRequest | None = None,
    ) -> ReadManagedPoliciesLinkedToUserGroupResponse:
        if request is None:
            request = ReadManagedPoliciesLinkedToUserGroupRequest()

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
        return TypeAdapter(ReadManagedPoliciesLinkedToUserGroupResponse).validate_python(response)

    async def read_nat_services(
        self,
        request: ReadNatServicesRequest | None = None,
    ) -> ReadNatServicesResponse:
        if request is None:
            request = ReadNatServicesRequest()

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
        return TypeAdapter(ReadNatServicesResponse).validate_python(response)

    async def read_net_access_point_services(
        self,
        request: ReadNetAccessPointServicesRequest | None = None,
    ) -> ReadNetAccessPointServicesResponse:
        if request is None:
            request = ReadNetAccessPointServicesRequest()

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
        return TypeAdapter(ReadNetAccessPointServicesResponse).validate_python(response)

    async def read_net_access_points(
        self,
        request: ReadNetAccessPointsRequest | None = None,
    ) -> ReadNetAccessPointsResponse:
        if request is None:
            request = ReadNetAccessPointsRequest()

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
        return TypeAdapter(ReadNetAccessPointsResponse).validate_python(response)

    async def read_net_peerings(
        self,
        request: ReadNetPeeringsRequest | None = None,
    ) -> ReadNetPeeringsResponse:
        if request is None:
            request = ReadNetPeeringsRequest()

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
        return TypeAdapter(ReadNetPeeringsResponse).validate_python(response)

    async def read_nets(
        self,
        request: ReadNetsRequest | None = None,
    ) -> ReadNetsResponse:
        if request is None:
            request = ReadNetsRequest()

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
        return TypeAdapter(ReadNetsResponse).validate_python(response)

    async def read_nics(
        self,
        request: ReadNicsRequest | None = None,
    ) -> ReadNicsResponse:
        if request is None:
            request = ReadNicsRequest()

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
        return TypeAdapter(ReadNicsResponse).validate_python(response)

    async def read_policies(
        self,
        request: ReadPoliciesRequest | None = None,
    ) -> ReadPoliciesResponse:
        if request is None:
            request = ReadPoliciesRequest()

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
        return TypeAdapter(ReadPoliciesResponse).validate_python(response)

    async def read_policy(
        self,
        request: ReadPolicyRequest | None = None,
    ) -> ReadPolicyResponse:
        if request is None:
            request = ReadPolicyRequest()

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
        return TypeAdapter(ReadPolicyResponse).validate_python(response)

    async def read_policy_version(
        self,
        request: ReadPolicyVersionRequest | None = None,
    ) -> ReadPolicyVersionResponse:
        if request is None:
            request = ReadPolicyVersionRequest()

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
        return TypeAdapter(ReadPolicyVersionResponse).validate_python(response)

    async def read_policy_versions(
        self,
        request: ReadPolicyVersionsRequest | None = None,
    ) -> ReadPolicyVersionsResponse:
        if request is None:
            request = ReadPolicyVersionsRequest()

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
        return TypeAdapter(ReadPolicyVersionsResponse).validate_python(response)

    async def read_product_types(
        self,
        request: ReadProductTypesRequest | None = None,
    ) -> ReadProductTypesResponse:
        if request is None:
            request = ReadProductTypesRequest()

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
        return TypeAdapter(ReadProductTypesResponse).validate_python(response)

    async def read_public_catalog(
        self,
        request: ReadPublicCatalogRequest | None = None,
    ) -> ReadPublicCatalogResponse:
        if request is None:
            request = ReadPublicCatalogRequest()

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
        return TypeAdapter(ReadPublicCatalogResponse).validate_python(response)

    async def read_public_ip_ranges(
        self,
        request: ReadPublicIpRangesRequest | None = None,
    ) -> ReadPublicIpRangesResponse:
        if request is None:
            request = ReadPublicIpRangesRequest()

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
        return TypeAdapter(ReadPublicIpRangesResponse).validate_python(response)

    async def read_public_ips(
        self,
        request: ReadPublicIpsRequest | None = None,
    ) -> ReadPublicIpsResponse:
        if request is None:
            request = ReadPublicIpsRequest()

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
        return TypeAdapter(ReadPublicIpsResponse).validate_python(response)

    async def read_quotas(
        self,
        request: ReadQuotasRequest | None = None,
    ) -> ReadQuotasResponse:
        if request is None:
            request = ReadQuotasRequest()

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
        return TypeAdapter(ReadQuotasResponse).validate_python(response)

    async def read_regions(
        self,
        request: ReadRegionsRequest | None = None,
    ) -> ReadRegionsResponse:
        if request is None:
            request = ReadRegionsRequest()

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
        return TypeAdapter(ReadRegionsResponse).validate_python(response)

    async def read_route_tables(
        self,
        request: ReadRouteTablesRequest | None = None,
    ) -> ReadRouteTablesResponse:
        if request is None:
            request = ReadRouteTablesRequest()

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
        return TypeAdapter(ReadRouteTablesResponse).validate_python(response)

    async def read_security_groups(
        self,
        request: ReadSecurityGroupsRequest | None = None,
    ) -> ReadSecurityGroupsResponse:
        if request is None:
            request = ReadSecurityGroupsRequest()

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
        return TypeAdapter(ReadSecurityGroupsResponse).validate_python(response)

    async def read_server_certificates(
        self,
        request: ReadServerCertificatesRequest | None = None,
    ) -> ReadServerCertificatesResponse:
        if request is None:
            request = ReadServerCertificatesRequest()

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
        return TypeAdapter(ReadServerCertificatesResponse).validate_python(response)

    async def read_snapshot_export_tasks(
        self,
        request: ReadSnapshotExportTasksRequest | None = None,
    ) -> ReadSnapshotExportTasksResponse:
        if request is None:
            request = ReadSnapshotExportTasksRequest()

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
        return TypeAdapter(ReadSnapshotExportTasksResponse).validate_python(response)

    async def read_snapshots(
        self,
        request: ReadSnapshotsRequest | None = None,
    ) -> ReadSnapshotsResponse:
        if request is None:
            request = ReadSnapshotsRequest()

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
        return TypeAdapter(ReadSnapshotsResponse).validate_python(response)

    async def read_subnets(
        self,
        request: ReadSubnetsRequest | None = None,
    ) -> ReadSubnetsResponse:
        if request is None:
            request = ReadSubnetsRequest()

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
        return TypeAdapter(ReadSubnetsResponse).validate_python(response)

    async def read_subregions(
        self,
        request: ReadSubregionsRequest | None = None,
    ) -> ReadSubregionsResponse:
        if request is None:
            request = ReadSubregionsRequest()

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
        return TypeAdapter(ReadSubregionsResponse).validate_python(response)

    async def read_tags(
        self,
        request: ReadTagsRequest | None = None,
    ) -> ReadTagsResponse:
        if request is None:
            request = ReadTagsRequest()

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
        return TypeAdapter(ReadTagsResponse).validate_python(response)

    async def read_unit_price(
        self,
        request: ReadUnitPriceRequest | None = None,
    ) -> ReadUnitPriceResponse:
        if request is None:
            request = ReadUnitPriceRequest()

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
        return TypeAdapter(ReadUnitPriceResponse).validate_python(response)

    async def read_user_group(
        self,
        request: ReadUserGroupRequest | None = None,
    ) -> ReadUserGroupResponse:
        if request is None:
            request = ReadUserGroupRequest()

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
        return TypeAdapter(ReadUserGroupResponse).validate_python(response)

    async def read_user_group_policies(
        self,
        request: ReadUserGroupPoliciesRequest | None = None,
    ) -> ReadUserGroupPoliciesResponse:
        if request is None:
            request = ReadUserGroupPoliciesRequest()

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
        return TypeAdapter(ReadUserGroupPoliciesResponse).validate_python(response)

    async def read_user_group_policy(
        self,
        request: ReadUserGroupPolicyRequest | None = None,
    ) -> ReadUserGroupPolicyResponse:
        if request is None:
            request = ReadUserGroupPolicyRequest()

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
        return TypeAdapter(ReadUserGroupPolicyResponse).validate_python(response)

    async def read_user_groups(
        self,
        request: ReadUserGroupsRequest | None = None,
    ) -> ReadUserGroupsResponse:
        if request is None:
            request = ReadUserGroupsRequest()

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
        return TypeAdapter(ReadUserGroupsResponse).validate_python(response)

    async def read_user_groups_per_user(
        self,
        request: ReadUserGroupsPerUserRequest | None = None,
    ) -> ReadUserGroupsPerUserResponse:
        if request is None:
            request = ReadUserGroupsPerUserRequest()

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
        return TypeAdapter(ReadUserGroupsPerUserResponse).validate_python(response)

    async def read_user_policies(
        self,
        request: ReadUserPoliciesRequest | None = None,
    ) -> ReadUserPoliciesResponse:
        if request is None:
            request = ReadUserPoliciesRequest()

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
        return TypeAdapter(ReadUserPoliciesResponse).validate_python(response)

    async def read_user_policy(
        self,
        request: ReadUserPolicyRequest | None = None,
    ) -> ReadUserPolicyResponse:
        if request is None:
            request = ReadUserPolicyRequest()

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
        return TypeAdapter(ReadUserPolicyResponse).validate_python(response)

    async def read_users(
        self,
        request: ReadUsersRequest | None = None,
    ) -> ReadUsersResponse:
        if request is None:
            request = ReadUsersRequest()

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
        return TypeAdapter(ReadUsersResponse).validate_python(response)

    async def read_virtual_gateways(
        self,
        request: ReadVirtualGatewaysRequest | None = None,
    ) -> ReadVirtualGatewaysResponse:
        if request is None:
            request = ReadVirtualGatewaysRequest()

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
        return TypeAdapter(ReadVirtualGatewaysResponse).validate_python(response)

    async def read_vm_groups(
        self,
        request: ReadVmGroupsRequest | None = None,
    ) -> ReadVmGroupsResponse:
        if request is None:
            request = ReadVmGroupsRequest()

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
        return TypeAdapter(ReadVmGroupsResponse).validate_python(response)

    async def read_vm_templates(
        self,
        request: ReadVmTemplatesRequest | None = None,
    ) -> ReadVmTemplatesResponse:
        if request is None:
            request = ReadVmTemplatesRequest()

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
        return TypeAdapter(ReadVmTemplatesResponse).validate_python(response)

    async def read_vm_types(
        self,
        request: ReadVmTypesRequest | None = None,
    ) -> ReadVmTypesResponse:
        if request is None:
            request = ReadVmTypesRequest()

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
        return TypeAdapter(ReadVmTypesResponse).validate_python(response)

    async def read_vms(
        self,
        request: ReadVmsRequest | None = None,
    ) -> ReadVmsResponse:
        if request is None:
            request = ReadVmsRequest()

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
        return TypeAdapter(ReadVmsResponse).validate_python(response)

    async def read_vms_health(
        self,
        request: ReadVmsHealthRequest | None = None,
    ) -> ReadVmsHealthResponse:
        if request is None:
            request = ReadVmsHealthRequest()

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
        return TypeAdapter(ReadVmsHealthResponse).validate_python(response)

    async def read_vms_state(
        self,
        request: ReadVmsStateRequest | None = None,
    ) -> ReadVmsStateResponse:
        if request is None:
            request = ReadVmsStateRequest()

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
        return TypeAdapter(ReadVmsStateResponse).validate_python(response)

    async def read_volume_update_tasks(
        self,
        request: ReadVolumeUpdateTasksRequest | None = None,
    ) -> ReadVolumeUpdateTasksResponse:
        if request is None:
            request = ReadVolumeUpdateTasksRequest()

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
        return TypeAdapter(ReadVolumeUpdateTasksResponse).validate_python(response)

    async def read_volumes(
        self,
        request: ReadVolumesRequest | None = None,
    ) -> ReadVolumesResponse:
        if request is None:
            request = ReadVolumesRequest()

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
        return TypeAdapter(ReadVolumesResponse).validate_python(response)

    async def read_vpn_connections(
        self,
        request: ReadVpnConnectionsRequest | None = None,
    ) -> ReadVpnConnectionsResponse:
        if request is None:
            request = ReadVpnConnectionsRequest()

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
        return TypeAdapter(ReadVpnConnectionsResponse).validate_python(response)

    async def reboot_vms(
        self,
        request: RebootVmsRequest | None = None,
    ) -> RebootVmsResponse:
        if request is None:
            request = RebootVmsRequest()

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
        return TypeAdapter(RebootVmsResponse).validate_python(response)

    async def register_vms_in_load_balancer(
        self,
        request: RegisterVmsInLoadBalancerRequest | None = None,
    ) -> RegisterVmsInLoadBalancerResponse:
        if request is None:
            request = RegisterVmsInLoadBalancerRequest()

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
        return TypeAdapter(RegisterVmsInLoadBalancerResponse).validate_python(response)

    async def reject_net_peering(
        self,
        request: RejectNetPeeringRequest | None = None,
    ) -> RejectNetPeeringResponse:
        if request is None:
            request = RejectNetPeeringRequest()

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
        return TypeAdapter(RejectNetPeeringResponse).validate_python(response)

    async def remove_user_from_user_group(
        self,
        request: RemoveUserFromUserGroupRequest | None = None,
    ) -> RemoveUserFromUserGroupResponse:
        if request is None:
            request = RemoveUserFromUserGroupRequest()

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
        return TypeAdapter(RemoveUserFromUserGroupResponse).validate_python(response)

    async def scale_down_vm_group(
        self,
        request: ScaleDownVmGroupRequest | None = None,
    ) -> ScaleDownVmGroupResponse:
        if request is None:
            request = ScaleDownVmGroupRequest()

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
        return TypeAdapter(ScaleDownVmGroupResponse).validate_python(response)

    async def scale_up_vm_group(
        self,
        request: ScaleUpVmGroupRequest | None = None,
    ) -> ScaleUpVmGroupResponse:
        if request is None:
            request = ScaleUpVmGroupRequest()

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
        return TypeAdapter(ScaleUpVmGroupResponse).validate_python(response)

    async def set_default_policy_version(
        self,
        request: SetDefaultPolicyVersionRequest | None = None,
    ) -> SetDefaultPolicyVersionResponse:
        if request is None:
            request = SetDefaultPolicyVersionRequest()

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
        return TypeAdapter(SetDefaultPolicyVersionResponse).validate_python(response)

    async def start_vms(
        self,
        request: StartVmsRequest | None = None,
    ) -> StartVmsResponse:
        if request is None:
            request = StartVmsRequest()

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
        return TypeAdapter(StartVmsResponse).validate_python(response)

    async def stop_vms(
        self,
        request: StopVmsRequest | None = None,
    ) -> StopVmsResponse:
        if request is None:
            request = StopVmsRequest()

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
        return TypeAdapter(StopVmsResponse).validate_python(response)

    async def unlink_flexible_gpu(
        self,
        request: UnlinkFlexibleGpuRequest | None = None,
    ) -> UnlinkFlexibleGpuResponse:
        if request is None:
            request = UnlinkFlexibleGpuRequest()

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
        return TypeAdapter(UnlinkFlexibleGpuResponse).validate_python(response)

    async def unlink_internet_service(
        self,
        request: UnlinkInternetServiceRequest | None = None,
    ) -> UnlinkInternetServiceResponse:
        if request is None:
            request = UnlinkInternetServiceRequest()

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
        return TypeAdapter(UnlinkInternetServiceResponse).validate_python(response)

    async def unlink_load_balancer_backend_machines(
        self,
        request: UnlinkLoadBalancerBackendMachinesRequest | None = None,
    ) -> UnlinkLoadBalancerBackendMachinesResponse:
        if request is None:
            request = UnlinkLoadBalancerBackendMachinesRequest()

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
        return TypeAdapter(UnlinkLoadBalancerBackendMachinesResponse).validate_python(response)

    async def unlink_managed_policy_from_user_group(
        self,
        request: UnlinkManagedPolicyFromUserGroupRequest | None = None,
    ) -> UnlinkManagedPolicyFromUserGroupResponse:
        if request is None:
            request = UnlinkManagedPolicyFromUserGroupRequest()

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
        return TypeAdapter(UnlinkManagedPolicyFromUserGroupResponse).validate_python(response)

    async def unlink_nic(
        self,
        request: UnlinkNicRequest | None = None,
    ) -> UnlinkNicResponse:
        if request is None:
            request = UnlinkNicRequest()

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
        return TypeAdapter(UnlinkNicResponse).validate_python(response)

    async def unlink_policy(
        self,
        request: UnlinkPolicyRequest | None = None,
    ) -> UnlinkPolicyResponse:
        if request is None:
            request = UnlinkPolicyRequest()

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
        return TypeAdapter(UnlinkPolicyResponse).validate_python(response)

    async def unlink_private_ips(
        self,
        request: UnlinkPrivateIpsRequest | None = None,
    ) -> UnlinkPrivateIpsResponse:
        if request is None:
            request = UnlinkPrivateIpsRequest()

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
        return TypeAdapter(UnlinkPrivateIpsResponse).validate_python(response)

    async def unlink_public_ip(
        self,
        request: UnlinkPublicIpRequest | None = None,
    ) -> UnlinkPublicIpResponse:
        if request is None:
            request = UnlinkPublicIpRequest()

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
        return TypeAdapter(UnlinkPublicIpResponse).validate_python(response)

    async def unlink_route_table(
        self,
        request: UnlinkRouteTableRequest | None = None,
    ) -> UnlinkRouteTableResponse:
        if request is None:
            request = UnlinkRouteTableRequest()

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
        return TypeAdapter(UnlinkRouteTableResponse).validate_python(response)

    async def unlink_virtual_gateway(
        self,
        request: UnlinkVirtualGatewayRequest | None = None,
    ) -> UnlinkVirtualGatewayResponse:
        if request is None:
            request = UnlinkVirtualGatewayRequest()

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
        return TypeAdapter(UnlinkVirtualGatewayResponse).validate_python(response)

    async def unlink_volume(
        self,
        request: UnlinkVolumeRequest | None = None,
    ) -> UnlinkVolumeResponse:
        if request is None:
            request = UnlinkVolumeRequest()

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
        return TypeAdapter(UnlinkVolumeResponse).validate_python(response)

    async def update_access_key(
        self,
        request: UpdateAccessKeyRequest | None = None,
    ) -> UpdateAccessKeyResponse:
        if request is None:
            request = UpdateAccessKeyRequest()

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
        return TypeAdapter(UpdateAccessKeyResponse).validate_python(response)

    async def update_account(
        self,
        request: UpdateAccountRequest | None = None,
    ) -> UpdateAccountResponse:
        if request is None:
            request = UpdateAccountRequest()

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
        return TypeAdapter(UpdateAccountResponse).validate_python(response)

    async def update_api_access_policy(
        self,
        request: UpdateApiAccessPolicyRequest | None = None,
    ) -> UpdateApiAccessPolicyResponse:
        if request is None:
            request = UpdateApiAccessPolicyRequest()

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
        return TypeAdapter(UpdateApiAccessPolicyResponse).validate_python(response)

    async def update_api_access_rule(
        self,
        request: UpdateApiAccessRuleRequest | None = None,
    ) -> UpdateApiAccessRuleResponse:
        if request is None:
            request = UpdateApiAccessRuleRequest()

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
        return TypeAdapter(UpdateApiAccessRuleResponse).validate_python(response)

    async def update_ca(
        self,
        request: UpdateCaRequest | None = None,
    ) -> UpdateCaResponse:
        if request is None:
            request = UpdateCaRequest()

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
        return TypeAdapter(UpdateCaResponse).validate_python(response)

    async def update_dedicated_group(
        self,
        request: UpdateDedicatedGroupRequest | None = None,
    ) -> UpdateDedicatedGroupResponse:
        if request is None:
            request = UpdateDedicatedGroupRequest()

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
        return TypeAdapter(UpdateDedicatedGroupResponse).validate_python(response)

    async def update_direct_link_interface(
        self,
        request: UpdateDirectLinkInterfaceRequest | None = None,
    ) -> UpdateDirectLinkInterfaceResponse:
        if request is None:
            request = UpdateDirectLinkInterfaceRequest()

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
        return TypeAdapter(UpdateDirectLinkInterfaceResponse).validate_python(response)

    async def update_flexible_gpu(
        self,
        request: UpdateFlexibleGpuRequest | None = None,
    ) -> UpdateFlexibleGpuResponse:
        if request is None:
            request = UpdateFlexibleGpuRequest()

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
        return TypeAdapter(UpdateFlexibleGpuResponse).validate_python(response)

    async def update_image(
        self,
        request: UpdateImageRequest | None = None,
    ) -> UpdateImageResponse:
        if request is None:
            request = UpdateImageRequest()

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
        return TypeAdapter(UpdateImageResponse).validate_python(response)

    async def update_listener_rule(
        self,
        request: UpdateListenerRuleRequest | None = None,
    ) -> UpdateListenerRuleResponse:
        if request is None:
            request = UpdateListenerRuleRequest()

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
        return TypeAdapter(UpdateListenerRuleResponse).validate_python(response)

    async def update_load_balancer(
        self,
        request: UpdateLoadBalancerRequest | None = None,
    ) -> UpdateLoadBalancerResponse:
        if request is None:
            request = UpdateLoadBalancerRequest()

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
        return TypeAdapter(UpdateLoadBalancerResponse).validate_python(response)

    async def update_net(
        self,
        request: UpdateNetRequest | None = None,
    ) -> UpdateNetResponse:
        if request is None:
            request = UpdateNetRequest()

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
        return TypeAdapter(UpdateNetResponse).validate_python(response)

    async def update_net_access_point(
        self,
        request: UpdateNetAccessPointRequest | None = None,
    ) -> UpdateNetAccessPointResponse:
        if request is None:
            request = UpdateNetAccessPointRequest()

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
        return TypeAdapter(UpdateNetAccessPointResponse).validate_python(response)

    async def update_nic(
        self,
        request: UpdateNicRequest | None = None,
    ) -> UpdateNicResponse:
        if request is None:
            request = UpdateNicRequest()

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
        return TypeAdapter(UpdateNicResponse).validate_python(response)

    async def update_route(
        self,
        request: UpdateRouteRequest | None = None,
    ) -> UpdateRouteResponse:
        if request is None:
            request = UpdateRouteRequest()

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
        return TypeAdapter(UpdateRouteResponse).validate_python(response)

    async def update_route_propagation(
        self,
        request: UpdateRoutePropagationRequest | None = None,
    ) -> UpdateRoutePropagationResponse:
        if request is None:
            request = UpdateRoutePropagationRequest()

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
        return TypeAdapter(UpdateRoutePropagationResponse).validate_python(response)

    async def update_route_table_link(
        self,
        request: UpdateRouteTableLinkRequest | None = None,
    ) -> UpdateRouteTableLinkResponse:
        if request is None:
            request = UpdateRouteTableLinkRequest()

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
        return TypeAdapter(UpdateRouteTableLinkResponse).validate_python(response)

    async def update_server_certificate(
        self,
        request: UpdateServerCertificateRequest | None = None,
    ) -> UpdateServerCertificateResponse:
        if request is None:
            request = UpdateServerCertificateRequest()

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
        return TypeAdapter(UpdateServerCertificateResponse).validate_python(response)

    async def update_snapshot(
        self,
        request: UpdateSnapshotRequest | None = None,
    ) -> UpdateSnapshotResponse:
        if request is None:
            request = UpdateSnapshotRequest()

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
        return TypeAdapter(UpdateSnapshotResponse).validate_python(response)

    async def update_subnet(
        self,
        request: UpdateSubnetRequest | None = None,
    ) -> UpdateSubnetResponse:
        if request is None:
            request = UpdateSubnetRequest()

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
        return TypeAdapter(UpdateSubnetResponse).validate_python(response)

    async def update_user(
        self,
        request: UpdateUserRequest | None = None,
    ) -> UpdateUserResponse:
        if request is None:
            request = UpdateUserRequest()

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
        return TypeAdapter(UpdateUserResponse).validate_python(response)

    async def update_user_group(
        self,
        request: UpdateUserGroupRequest | None = None,
    ) -> UpdateUserGroupResponse:
        if request is None:
            request = UpdateUserGroupRequest()

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
        return TypeAdapter(UpdateUserGroupResponse).validate_python(response)

    async def update_vm(
        self,
        request: UpdateVmRequest | None = None,
    ) -> UpdateVmResponse:
        if request is None:
            request = UpdateVmRequest()

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
        return TypeAdapter(UpdateVmResponse).validate_python(response)

    async def update_vm_group(
        self,
        request: UpdateVmGroupRequest | None = None,
    ) -> UpdateVmGroupResponse:
        if request is None:
            request = UpdateVmGroupRequest()

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
        return TypeAdapter(UpdateVmGroupResponse).validate_python(response)

    async def update_vm_template(
        self,
        request: UpdateVmTemplateRequest | None = None,
    ) -> UpdateVmTemplateResponse:
        if request is None:
            request = UpdateVmTemplateRequest()

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
        return TypeAdapter(UpdateVmTemplateResponse).validate_python(response)

    async def update_volume(
        self,
        request: UpdateVolumeRequest | None = None,
    ) -> UpdateVolumeResponse:
        if request is None:
            request = UpdateVolumeRequest()

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
        return TypeAdapter(UpdateVolumeResponse).validate_python(response)

    async def update_vpn_connection(
        self,
        request: UpdateVpnConnectionRequest | None = None,
    ) -> UpdateVpnConnectionResponse:
        if request is None:
            request = UpdateVpnConnectionRequest()

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
        return TypeAdapter(UpdateVpnConnectionResponse).validate_python(response)
