"""Generated typed OSC client slice.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator
"""
from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class GeneratedModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class AcceptNetPeeringRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_peering_id: str = Field(alias='NetPeeringId')

class AcceptNetPeeringResponse(GeneratedModel):
    net_peering: NetPeering | None = Field(default=None, alias='NetPeering')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class AccepterNet(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    ip_range: str | None = Field(default=None, alias='IpRange')
    net_id: str | None = Field(default=None, alias='NetId')

class AccessKey(GeneratedModel):
    access_key_id: str | None = Field(default=None, alias='AccessKeyId')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    expiration_date: str | None = Field(default=None, alias='ExpirationDate')
    last_modification_date: str | None = Field(default=None, alias='LastModificationDate')
    state: str | None = Field(default=None, alias='State')
    tag: str | None = Field(default=None, alias='Tag')

class AccessKeySecretKey(GeneratedModel):
    access_key_id: str | None = Field(default=None, alias='AccessKeyId')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    expiration_date: str | None = Field(default=None, alias='ExpirationDate')
    last_modification_date: str | None = Field(default=None, alias='LastModificationDate')
    secret_key: str | None = Field(default=None, alias='SecretKey')
    state: str | None = Field(default=None, alias='State')
    tag: str | None = Field(default=None, alias='Tag')

class AccessLog(GeneratedModel):
    is_enabled: bool | None = Field(default=None, alias='IsEnabled')
    osu_bucket_name: str | None = Field(default=None, alias='OsuBucketName')
    osu_bucket_prefix: str | None = Field(default=None, alias='OsuBucketPrefix')
    publication_interval: int | None = Field(default=None, alias='PublicationInterval')

class Account(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    additional_emails: list[str] | None = Field(default=None, alias='AdditionalEmails')
    city: str | None = Field(default=None, alias='City')
    company_name: str | None = Field(default=None, alias='CompanyName')
    country: str | None = Field(default=None, alias='Country')
    customer_id: str | None = Field(default=None, alias='CustomerId')
    email: str | None = Field(default=None, alias='Email')
    first_name: str | None = Field(default=None, alias='FirstName')
    job_title: str | None = Field(default=None, alias='JobTitle')
    last_name: str | None = Field(default=None, alias='LastName')
    mobile_number: str | None = Field(default=None, alias='MobileNumber')
    outscale_login_allowed: bool | None = Field(default=None, alias='OutscaleLoginAllowed')
    phone_number: str | None = Field(default=None, alias='PhoneNumber')
    state_province: str | None = Field(default=None, alias='StateProvince')
    vat_number: str | None = Field(default=None, alias='VatNumber')
    zip_code: str | None = Field(default=None, alias='ZipCode')

class ActionsOnNextBoot(GeneratedModel):
    secure_boot: SecureBootAction | None = Field(default=None, alias='SecureBoot')

class AddUserToUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_group_name: str = Field(alias='UserGroupName')
    user_group_path: str | None = Field(default=None, alias='UserGroupPath')
    user_name: str = Field(alias='UserName')
    user_path: str | None = Field(default=None, alias='UserPath')

class AddUserToUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ApiAccessPolicy(GeneratedModel):
    max_access_key_expiration_seconds: int | None = Field(default=None, alias='MaxAccessKeyExpirationSeconds')
    require_trusted_env: bool | None = Field(default=None, alias='RequireTrustedEnv')

class ApiAccessRule(GeneratedModel):
    api_access_rule_id: str | None = Field(default=None, alias='ApiAccessRuleId')
    ca_ids: list[str] | None = Field(default=None, alias='CaIds')
    cns: list[str] | None = Field(default=None, alias='Cns')
    description: str | None = Field(default=None, alias='Description')
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')

class ApplicationStickyCookiePolicy(GeneratedModel):
    cookie_name: str | None = Field(default=None, alias='CookieName')
    policy_name: str | None = Field(default=None, alias='PolicyName')

class BackendVmHealth(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    state: str | None = Field(default=None, alias='State')
    state_reason: str | None = Field(default=None, alias='StateReason')
    vm_id: str | None = Field(default=None, alias='VmId')

class BlockDeviceMappingCreated(GeneratedModel):
    bsu: BsuCreated | None = Field(default=None, alias='Bsu')
    device_name: str | None = Field(default=None, alias='DeviceName')

class BlockDeviceMappingImage(GeneratedModel):
    bsu: BsuToCreate | None = Field(default=None, alias='Bsu')
    device_name: str | None = Field(default=None, alias='DeviceName')
    virtual_device_name: str | None = Field(default=None, alias='VirtualDeviceName')

class BlockDeviceMappingVmCreation(GeneratedModel):
    bsu: BsuToCreate | None = Field(default=None, alias='Bsu')
    device_name: str | None = Field(default=None, alias='DeviceName')
    no_device: str | None = Field(default=None, alias='NoDevice')
    virtual_device_name: str | None = Field(default=None, alias='VirtualDeviceName')

class BlockDeviceMappingVmUpdate(GeneratedModel):
    bsu: BsuToUpdateVm | None = Field(default=None, alias='Bsu')
    device_name: str | None = Field(default=None, alias='DeviceName')
    no_device: str | None = Field(default=None, alias='NoDevice')
    virtual_device_name: str | None = Field(default=None, alias='VirtualDeviceName')

BootMode = Literal['uefi', 'legacy']

class BsuCreated(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    link_date: str | None = Field(default=None, alias='LinkDate')
    state: str | None = Field(default=None, alias='State')
    volume_id: str | None = Field(default=None, alias='VolumeId')

class BsuToCreate(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    iops: int | None = Field(default=None, alias='Iops')
    snapshot_id: str | None = Field(default=None, alias='SnapshotId')
    volume_size: int | None = Field(default=None, alias='VolumeSize')
    volume_type: str | None = Field(default=None, alias='VolumeType')

class BsuToUpdateVm(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    volume_id: str | None = Field(default=None, alias='VolumeId')

class CO2CategoryDistribution(GeneratedModel):
    category: str | None = Field(default=None, alias='Category')
    value: float | None = Field(default=None, alias='Value')

class CO2EmissionEntry(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    category_distribution: list[CO2CategoryDistribution] | None = Field(default=None, alias='CategoryDistribution')
    factor_distribution: list[CO2FactorDistribution] | None = Field(default=None, alias='FactorDistribution')
    month: str | None = Field(default=None, alias='Month')
    paying_account_id: str | None = Field(default=None, alias='PayingAccountId')
    value: float | None = Field(default=None, alias='Value')

class CO2FactorDistribution(GeneratedModel):
    factor: str | None = Field(default=None, alias='Factor')
    value: float | None = Field(default=None, alias='Value')

class Ca(GeneratedModel):
    ca_fingerprint: str | None = Field(default=None, alias='CaFingerprint')
    ca_id: str | None = Field(default=None, alias='CaId')
    description: str | None = Field(default=None, alias='Description')

class Catalog(GeneratedModel):
    entries: list[CatalogEntry] | None = Field(default=None, alias='Entries')

class CatalogEntry(GeneratedModel):
    category: str | None = Field(default=None, alias='Category')
    flags: str | None = Field(default=None, alias='Flags')
    operation: str | None = Field(default=None, alias='Operation')
    service: str | None = Field(default=None, alias='Service')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    title: str | None = Field(default=None, alias='Title')
    type: str | None = Field(default=None, alias='Type')
    unit_price: float | None = Field(default=None, alias='UnitPrice')

class Catalogs(GeneratedModel):
    entries: list[CatalogEntry] | None = Field(default=None, alias='Entries')
    from_date: str | None = Field(default=None, alias='FromDate')
    state: Literal['CURRENT', 'OBSOLETE'] | None = Field(default=None, alias='State')
    to_date: str | None = Field(default=None, alias='ToDate')

class CheckAuthenticationRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    login: str = Field(alias='Login')
    password: str = Field(alias='Password')

class CheckAuthenticationResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ClientGateway(GeneratedModel):
    bgp_asn: int | None = Field(default=None, alias='BgpAsn')
    client_gateway_id: str | None = Field(default=None, alias='ClientGatewayId')
    connection_type: str | None = Field(default=None, alias='ConnectionType')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class ConsumptionEntry(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    category: str | None = Field(default=None, alias='Category')
    from_date: str | None = Field(default=None, alias='FromDate')
    operation: str | None = Field(default=None, alias='Operation')
    paying_account_id: str | None = Field(default=None, alias='PayingAccountId')
    price: float | None = Field(default=None, alias='Price')
    resource_id: str | None = Field(default=None, alias='ResourceId')
    service: str | None = Field(default=None, alias='Service')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    title: str | None = Field(default=None, alias='Title')
    to_date: str | None = Field(default=None, alias='ToDate')
    type: str | None = Field(default=None, alias='Type')
    unit_price: float | None = Field(default=None, alias='UnitPrice')
    value: float | None = Field(default=None, alias='Value')

class CreateAccessKeyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    expiration_date: str | None = Field(default=None, alias='ExpirationDate')
    tag: str | None = Field(default=None, alias='Tag')
    user_name: str | None = Field(default=None, alias='UserName')

class CreateAccessKeyResponse(GeneratedModel):
    access_key: AccessKeySecretKey | None = Field(default=None, alias='AccessKey')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateAccountRequest(GeneratedModel):
    additional_emails: list[str] | None = Field(default=None, alias='AdditionalEmails')
    city: str = Field(alias='City')
    company_name: str = Field(alias='CompanyName')
    country: str = Field(alias='Country')
    customer_id: str = Field(alias='CustomerId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    email: str = Field(alias='Email')
    first_name: str = Field(alias='FirstName')
    job_title: str | None = Field(default=None, alias='JobTitle')
    last_name: str = Field(alias='LastName')
    mobile_number: str | None = Field(default=None, alias='MobileNumber')
    phone_number: str | None = Field(default=None, alias='PhoneNumber')
    state_province: str | None = Field(default=None, alias='StateProvince')
    vat_number: str | None = Field(default=None, alias='VatNumber')
    zip_code: str = Field(alias='ZipCode')

class CreateAccountResponse(GeneratedModel):
    account: Account | None = Field(default=None, alias='Account')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateApiAccessRuleRequest(GeneratedModel):
    ca_ids: list[str] | None = Field(default=None, alias='CaIds')
    cns: list[str] | None = Field(default=None, alias='Cns')
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')

class CreateApiAccessRuleResponse(GeneratedModel):
    api_access_rule: ApiAccessRule | None = Field(default=None, alias='ApiAccessRule')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateCaRequest(GeneratedModel):
    ca_pem: str = Field(alias='CaPem')
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class CreateCaResponse(GeneratedModel):
    ca: Ca | None = Field(default=None, alias='Ca')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateClientGatewayRequest(GeneratedModel):
    bgp_asn: int = Field(alias='BgpAsn')
    connection_type: str = Field(alias='ConnectionType')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    public_ip: str = Field(alias='PublicIp')

class CreateClientGatewayResponse(GeneratedModel):
    client_gateway: ClientGateway | None = Field(default=None, alias='ClientGateway')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateDedicatedGroupRequest(GeneratedModel):
    cpu_generation: int = Field(alias='CpuGeneration')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    name: str = Field(alias='Name')
    subregion_name: str = Field(alias='SubregionName')

class CreateDedicatedGroupResponse(GeneratedModel):
    dedicated_group: DedicatedGroup | None = Field(default=None, alias='DedicatedGroup')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateDhcpOptionsRequest(GeneratedModel):
    domain_name: str | None = Field(default=None, alias='DomainName')
    domain_name_servers: list[str] | None = Field(default=None, alias='DomainNameServers')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    log_servers: list[str] | None = Field(default=None, alias='LogServers')
    ntp_servers: list[str] | None = Field(default=None, alias='NtpServers')

class CreateDhcpOptionsResponse(GeneratedModel):
    dhcp_options_set: DhcpOptionsSet | None = Field(default=None, alias='DhcpOptionsSet')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateDirectLinkInterfaceRequest(GeneratedModel):
    direct_link_id: str = Field(alias='DirectLinkId')
    direct_link_interface: DirectLinkInterface = Field(alias='DirectLinkInterface')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class CreateDirectLinkInterfaceResponse(GeneratedModel):
    direct_link_interface: DirectLinkInterfaces | None = Field(default=None, alias='DirectLinkInterface')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateDirectLinkRequest(GeneratedModel):
    bandwidth: str = Field(alias='Bandwidth')
    direct_link_name: str = Field(alias='DirectLinkName')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    location: str = Field(alias='Location')

class CreateDirectLinkResponse(GeneratedModel):
    direct_link: DirectLink | None = Field(default=None, alias='DirectLink')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateFlexibleGpuRequest(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    generation: str | None = Field(default=None, alias='Generation')
    model_name: str = Field(alias='ModelName')
    subregion_name: str = Field(alias='SubregionName')

class CreateFlexibleGpuResponse(GeneratedModel):
    flexible_gpu: FlexibleGpu | None = Field(default=None, alias='FlexibleGpu')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateImageExportTaskRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    image_id: str = Field(alias='ImageId')
    osu_export: OsuExportToCreate = Field(alias='OsuExport')

class CreateImageExportTaskResponse(GeneratedModel):
    image_export_task: ImageExportTask | None = Field(default=None, alias='ImageExportTask')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateImageRequest(GeneratedModel):
    architecture: str | None = Field(default=None, alias='Architecture')
    block_device_mappings: list[BlockDeviceMappingImage] | None = Field(default=None, alias='BlockDeviceMappings')
    boot_modes: list[BootMode] | None = Field(default=None, alias='BootModes')
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    file_location: str | None = Field(default=None, alias='FileLocation')
    image_name: str | None = Field(default=None, alias='ImageName')
    no_reboot: bool | None = Field(default=None, alias='NoReboot')
    product_codes: list[str] | None = Field(default=None, alias='ProductCodes')
    root_device_name: str | None = Field(default=None, alias='RootDeviceName')
    source_image_id: str | None = Field(default=None, alias='SourceImageId')
    source_region_name: str | None = Field(default=None, alias='SourceRegionName')
    tpm_mandatory: bool | None = Field(default=None, alias='TpmMandatory')
    vm_id: str | None = Field(default=None, alias='VmId')

class CreateImageResponse(GeneratedModel):
    image: Image | None = Field(default=None, alias='Image')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateInternetServiceRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class CreateInternetServiceResponse(GeneratedModel):
    internet_service: InternetService | None = Field(default=None, alias='InternetService')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateKeypairRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    keypair_name: str = Field(alias='KeypairName')
    public_key: str | None = Field(default=None, alias='PublicKey')

class CreateKeypairResponse(GeneratedModel):
    keypair: KeypairCreated | None = Field(default=None, alias='Keypair')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateListenerRuleRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    listener: LoadBalancerLight = Field(alias='Listener')
    listener_rule: ListenerRuleForCreation = Field(alias='ListenerRule')
    vm_ids: list[str] = Field(alias='VmIds')

class CreateListenerRuleResponse(GeneratedModel):
    listener_rule: ListenerRule | None = Field(default=None, alias='ListenerRule')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateLoadBalancerListenersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    listeners: list[ListenerForCreation] = Field(alias='Listeners')
    load_balancer_name: str = Field(alias='LoadBalancerName')

class CreateLoadBalancerListenersResponse(GeneratedModel):
    load_balancer: LoadBalancer | None = Field(default=None, alias='LoadBalancer')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateLoadBalancerPolicyRequest(GeneratedModel):
    cookie_expiration_period: int | None = Field(default=None, alias='CookieExpirationPeriod')
    cookie_name: str | None = Field(default=None, alias='CookieName')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')
    policy_name: str = Field(alias='PolicyName')
    policy_type: str = Field(alias='PolicyType')

class CreateLoadBalancerPolicyResponse(GeneratedModel):
    load_balancer: LoadBalancer | None = Field(default=None, alias='LoadBalancer')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateLoadBalancerRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    listeners: list[ListenerForCreation] = Field(alias='Listeners')
    load_balancer_name: str = Field(alias='LoadBalancerName')
    load_balancer_type: str | None = Field(default=None, alias='LoadBalancerType')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    security_groups: list[str] | None = Field(default=None, alias='SecurityGroups')
    subnets: list[str] | None = Field(default=None, alias='Subnets')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class CreateLoadBalancerResponse(GeneratedModel):
    load_balancer: LoadBalancer | None = Field(default=None, alias='LoadBalancer')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateLoadBalancerTagsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_names: list[str] = Field(alias='LoadBalancerNames')
    tags: list[ResourceTag] = Field(alias='Tags')

class CreateLoadBalancerTagsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateNatServiceRequest(GeneratedModel):
    client_token: str | None = Field(default=None, alias='ClientToken')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    public_ip_id: str = Field(alias='PublicIpId')
    subnet_id: str = Field(alias='SubnetId')

class CreateNatServiceResponse(GeneratedModel):
    nat_service: NatService | None = Field(default=None, alias='NatService')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateNetAccessPointRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_id: str = Field(alias='NetId')
    route_table_ids: list[str] | None = Field(default=None, alias='RouteTableIds')
    service_name: str = Field(alias='ServiceName')

class CreateNetAccessPointResponse(GeneratedModel):
    net_access_point: NetAccessPoint | None = Field(default=None, alias='NetAccessPoint')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateNetPeeringRequest(GeneratedModel):
    accepter_net_id: str = Field(alias='AccepterNetId')
    accepter_owner_id: str | None = Field(default=None, alias='AccepterOwnerId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    source_net_id: str = Field(alias='SourceNetId')

class CreateNetPeeringResponse(GeneratedModel):
    net_peering: NetPeering | None = Field(default=None, alias='NetPeering')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateNetRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    ip_range: str = Field(alias='IpRange')
    tenancy: str | None = Field(default=None, alias='Tenancy')

class CreateNetResponse(GeneratedModel):
    net: Net | None = Field(default=None, alias='Net')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateNicRequest(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    private_ips: list[PrivateIpLight] | None = Field(default=None, alias='PrivateIps')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    subnet_id: str = Field(alias='SubnetId')

class CreateNicResponse(GeneratedModel):
    nic: Nic | None = Field(default=None, alias='Nic')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreatePolicyRequest(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    document: str = Field(alias='Document')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    path: str | None = Field(default=None, alias='Path')
    policy_name: str = Field(alias='PolicyName')

class CreatePolicyResponse(GeneratedModel):
    policy: Policy | None = Field(default=None, alias='Policy')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreatePolicyVersionRequest(GeneratedModel):
    document: str = Field(alias='Document')
    policy_orn: str = Field(alias='PolicyOrn')
    set_as_default: bool | None = Field(default=None, alias='SetAsDefault')

class CreatePolicyVersionResponse(GeneratedModel):
    policy_version: PolicyVersion | None = Field(default=None, alias='PolicyVersion')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateProductTypeRequest(GeneratedModel):
    description: str = Field(alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vendor: str | None = Field(default=None, alias='Vendor')

class CreateProductTypeResponse(GeneratedModel):
    product_type: ProductType | None = Field(default=None, alias='ProductType')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreatePublicIpRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class CreatePublicIpResponse(GeneratedModel):
    public_ip: PublicIp | None = Field(default=None, alias='PublicIp')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateRouteRequest(GeneratedModel):
    destination_ip_range: str = Field(alias='DestinationIpRange')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    gateway_id: str | None = Field(default=None, alias='GatewayId')
    nat_service_id: str | None = Field(default=None, alias='NatServiceId')
    net_peering_id: str | None = Field(default=None, alias='NetPeeringId')
    nic_id: str | None = Field(default=None, alias='NicId')
    route_table_id: str = Field(alias='RouteTableId')
    vm_id: str | None = Field(default=None, alias='VmId')

class CreateRouteResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    route_table: RouteTable | None = Field(default=None, alias='RouteTable')

class CreateRouteTableRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_id: str = Field(alias='NetId')

class CreateRouteTableResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    route_table: RouteTable | None = Field(default=None, alias='RouteTable')

class CreateSecurityGroupRequest(GeneratedModel):
    description: str = Field(alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_id: str | None = Field(default=None, alias='NetId')
    security_group_name: str = Field(alias='SecurityGroupName')

class CreateSecurityGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    security_group: SecurityGroup | None = Field(default=None, alias='SecurityGroup')

class CreateSecurityGroupRuleRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    flow: str = Field(alias='Flow')
    from_port_range: int | None = Field(default=None, alias='FromPortRange')
    ip_protocol: str | None = Field(default=None, alias='IpProtocol')
    ip_range: str | None = Field(default=None, alias='IpRange')
    rules: list[SecurityGroupRule] | None = Field(default=None, alias='Rules')
    security_group_account_id_to_link: str | None = Field(default=None, alias='SecurityGroupAccountIdToLink')
    security_group_id: str = Field(alias='SecurityGroupId')
    security_group_name_to_link: str | None = Field(default=None, alias='SecurityGroupNameToLink')
    to_port_range: int | None = Field(default=None, alias='ToPortRange')

class CreateSecurityGroupRuleResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    security_group: SecurityGroup | None = Field(default=None, alias='SecurityGroup')

class CreateServerCertificateRequest(GeneratedModel):
    body: str = Field(alias='Body')
    chain: str | None = Field(default=None, alias='Chain')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    name: str = Field(alias='Name')
    path: str | None = Field(default=None, alias='Path')
    private_key: str = Field(alias='PrivateKey')

class CreateServerCertificateResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    server_certificate: ServerCertificate | None = Field(default=None, alias='ServerCertificate')

class CreateSnapshotExportTaskRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    osu_export: OsuExportToCreate = Field(alias='OsuExport')
    snapshot_id: str = Field(alias='SnapshotId')

class CreateSnapshotExportTaskResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    snapshot_export_task: SnapshotExportTask | None = Field(default=None, alias='SnapshotExportTask')

class CreateSnapshotRequest(GeneratedModel):
    client_token: str | None = Field(default=None, alias='ClientToken')
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    file_location: str | None = Field(default=None, alias='FileLocation')
    snapshot_size: int | None = Field(default=None, alias='SnapshotSize')
    source_region_name: str | None = Field(default=None, alias='SourceRegionName')
    source_snapshot_id: str | None = Field(default=None, alias='SourceSnapshotId')
    volume_id: str | None = Field(default=None, alias='VolumeId')

class CreateSnapshotResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    snapshot: Snapshot | None = Field(default=None, alias='Snapshot')

class CreateSubnetRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    ip_range: str = Field(alias='IpRange')
    net_id: str = Field(alias='NetId')
    subregion_name: str | None = Field(default=None, alias='SubregionName')

class CreateSubnetResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    subnet: Subnet | None = Field(default=None, alias='Subnet')

class CreateTagsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    resource_ids: list[str] = Field(alias='ResourceIds')
    tags: list[ResourceTag] = Field(alias='Tags')

class CreateTagsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class CreateUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    path: str | None = Field(default=None, alias='Path')
    user_group_name: str = Field(alias='UserGroupName')

class CreateUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user_group: UserGroup | None = Field(default=None, alias='UserGroup')

class CreateUserRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    path: str | None = Field(default=None, alias='Path')
    user_email: str | None = Field(default=None, alias='UserEmail')
    user_name: str = Field(alias='UserName')

class CreateUserResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user: User | None = Field(default=None, alias='User')

class CreateVirtualGatewayRequest(GeneratedModel):
    connection_type: str = Field(alias='ConnectionType')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class CreateVirtualGatewayResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    virtual_gateway: VirtualGateway | None = Field(default=None, alias='VirtualGateway')

class CreateVmGroupRequest(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    positioning_strategy: Literal['attract', 'no-strategy', 'repulse'] | None = Field(default=None, alias='PositioningStrategy')
    security_group_ids: list[str] = Field(alias='SecurityGroupIds')
    subnet_id: str = Field(alias='SubnetId')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vm_count: int = Field(alias='VmCount')
    vm_group_name: str = Field(alias='VmGroupName')
    vm_template_id: str = Field(alias='VmTemplateId')

class CreateVmGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_group: VmGroup | None = Field(default=None, alias='VmGroup')

class CreateVmTemplateRequest(GeneratedModel):
    cpu_cores: int = Field(alias='CpuCores')
    cpu_generation: str = Field(alias='CpuGeneration')
    cpu_performance: Literal['medium', 'high', 'highest'] | None = Field(default=None, alias='CpuPerformance')
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    image_id: str = Field(alias='ImageId')
    keypair_name: str | None = Field(default=None, alias='KeypairName')
    ram: int = Field(alias='Ram')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vm_template_name: str = Field(alias='VmTemplateName')

class CreateVmTemplateResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_template: VmTemplate | None = Field(default=None, alias='VmTemplate')

class CreateVmsRequest(GeneratedModel):
    actions_on_next_boot: ActionsOnNextBoot | None = Field(default=None, alias='ActionsOnNextBoot')
    block_device_mappings: list[BlockDeviceMappingVmCreation] | None = Field(default=None, alias='BlockDeviceMappings')
    boot_mode: BootMode | None = Field(default=None, alias='BootMode')
    boot_on_creation: bool | None = Field(default=None, alias='BootOnCreation')
    bsu_optimized: bool | None = Field(default=None, alias='BsuOptimized')
    client_token: str | None = Field(default=None, alias='ClientToken')
    deletion_protection: bool | None = Field(default=None, alias='DeletionProtection')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    image_id: str = Field(alias='ImageId')
    keypair_name: str | None = Field(default=None, alias='KeypairName')
    max_vms_count: int | None = Field(default=None, alias='MaxVmsCount')
    min_vms_count: int | None = Field(default=None, alias='MinVmsCount')
    nested_virtualization: bool | None = Field(default=None, alias='NestedVirtualization')
    nics: list[NicForVmCreation] | None = Field(default=None, alias='Nics')
    performance: Literal['medium', 'high', 'highest'] | None = Field(default=None, alias='Performance')
    placement: Placement | None = Field(default=None, alias='Placement')
    private_ips: list[str] | None = Field(default=None, alias='PrivateIps')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    security_groups: list[str] | None = Field(default=None, alias='SecurityGroups')
    subnet_id: str | None = Field(default=None, alias='SubnetId')
    tpm_enabled: bool | None = Field(default=None, alias='TpmEnabled')
    user_data: str | None = Field(default=None, alias='UserData')
    vm_initiated_shutdown_behavior: str | None = Field(default=None, alias='VmInitiatedShutdownBehavior')
    vm_type: str | None = Field(default=None, alias='VmType')

class CreateVmsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vms: list[Vm] | None = Field(default=None, alias='Vms')

class CreateVolumeRequest(GeneratedModel):
    client_token: str | None = Field(default=None, alias='ClientToken')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    iops: int | None = Field(default=None, alias='Iops')
    size: int | None = Field(default=None, alias='Size')
    snapshot_id: str | None = Field(default=None, alias='SnapshotId')
    subregion_name: str = Field(alias='SubregionName')
    volume_type: str | None = Field(default=None, alias='VolumeType')

class CreateVolumeResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    volume: Volume | None = Field(default=None, alias='Volume')

class CreateVpnConnectionRequest(GeneratedModel):
    client_gateway_id: str = Field(alias='ClientGatewayId')
    connection_type: str = Field(alias='ConnectionType')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    static_routes_only: bool | None = Field(default=None, alias='StaticRoutesOnly')
    virtual_gateway_id: str = Field(alias='VirtualGatewayId')

class CreateVpnConnectionResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vpn_connection: VpnConnection | None = Field(default=None, alias='VpnConnection')

class CreateVpnConnectionRouteRequest(GeneratedModel):
    destination_ip_range: str = Field(alias='DestinationIpRange')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vpn_connection_id: str = Field(alias='VpnConnectionId')

class CreateVpnConnectionRouteResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DedicatedGroup(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    cpu_generation: int | None = Field(default=None, alias='CpuGeneration')
    dedicated_group_id: str | None = Field(default=None, alias='DedicatedGroupId')
    name: str | None = Field(default=None, alias='Name')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    vm_ids: list[str] | None = Field(default=None, alias='VmIds')

class DeleteAccessKeyRequest(GeneratedModel):
    access_key_id: str = Field(alias='AccessKeyId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_name: str | None = Field(default=None, alias='UserName')

class DeleteAccessKeyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteApiAccessRuleRequest(GeneratedModel):
    api_access_rule_id: str = Field(alias='ApiAccessRuleId')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DeleteApiAccessRuleResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteCaRequest(GeneratedModel):
    ca_id: str = Field(alias='CaId')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DeleteCaResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteClientGatewayRequest(GeneratedModel):
    client_gateway_id: str = Field(alias='ClientGatewayId')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DeleteClientGatewayResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteDedicatedGroupRequest(GeneratedModel):
    dedicated_group_id: str = Field(alias='DedicatedGroupId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    force: bool | None = Field(default=None, alias='Force')

class DeleteDedicatedGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteDhcpOptionsRequest(GeneratedModel):
    dhcp_options_set_id: str = Field(alias='DhcpOptionsSetId')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DeleteDhcpOptionsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteDirectLinkInterfaceRequest(GeneratedModel):
    direct_link_interface_id: str = Field(alias='DirectLinkInterfaceId')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DeleteDirectLinkInterfaceResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteDirectLinkRequest(GeneratedModel):
    direct_link_id: str = Field(alias='DirectLinkId')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DeleteDirectLinkResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteExportTaskRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    export_task_id: str = Field(alias='ExportTaskId')

class DeleteExportTaskResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteFlexibleGpuRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    flexible_gpu_id: str = Field(alias='FlexibleGpuId')

class DeleteFlexibleGpuResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteImageRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    image_id: str = Field(alias='ImageId')

class DeleteImageResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteInternetServiceRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    internet_service_id: str = Field(alias='InternetServiceId')

class DeleteInternetServiceResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteKeypairRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    keypair_id: str | None = Field(default=None, alias='KeypairId')
    keypair_name: str | None = Field(default=None, alias='KeypairName')

class DeleteKeypairResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteListenerRuleRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    listener_rule_name: str = Field(alias='ListenerRuleName')

class DeleteListenerRuleResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteLoadBalancerListenersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')
    load_balancer_ports: list[int] = Field(alias='LoadBalancerPorts')

class DeleteLoadBalancerListenersResponse(GeneratedModel):
    load_balancer: LoadBalancer | None = Field(default=None, alias='LoadBalancer')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteLoadBalancerPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')
    policy_name: str = Field(alias='PolicyName')

class DeleteLoadBalancerPolicyResponse(GeneratedModel):
    load_balancer: LoadBalancer | None = Field(default=None, alias='LoadBalancer')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteLoadBalancerRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')

class DeleteLoadBalancerResponse(GeneratedModel):
    load_balancer: LoadBalancer | None = Field(default=None, alias='LoadBalancer')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteLoadBalancerTagsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_names: list[str] = Field(alias='LoadBalancerNames')
    tags: list[ResourceLoadBalancerTag] = Field(alias='Tags')

class DeleteLoadBalancerTagsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteNatServiceRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    nat_service_id: str = Field(alias='NatServiceId')

class DeleteNatServiceResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteNetAccessPointRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_access_point_id: str = Field(alias='NetAccessPointId')

class DeleteNetAccessPointResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteNetPeeringRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_peering_id: str = Field(alias='NetPeeringId')

class DeleteNetPeeringResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteNetRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_id: str = Field(alias='NetId')

class DeleteNetResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteNicRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    nic_id: str = Field(alias='NicId')

class DeleteNicResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeletePolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_orn: str = Field(alias='PolicyOrn')

class DeletePolicyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeletePolicyVersionRequest(GeneratedModel):
    policy_orn: str = Field(alias='PolicyOrn')
    version_id: str = Field(alias='VersionId')

class DeletePolicyVersionResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteProductTypeRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    force: bool | None = Field(default=None, alias='Force')
    product_type_id: str = Field(alias='ProductTypeId')

class DeleteProductTypeResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeletePublicIpRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    public_ip_id: str | None = Field(default=None, alias='PublicIpId')

class DeletePublicIpResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteRouteRequest(GeneratedModel):
    destination_ip_range: str = Field(alias='DestinationIpRange')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    route_table_id: str = Field(alias='RouteTableId')

class DeleteRouteResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    route_table: RouteTable | None = Field(default=None, alias='RouteTable')

class DeleteRouteTableRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    route_table_id: str = Field(alias='RouteTableId')

class DeleteRouteTableResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteSecurityGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    security_group_id: str | None = Field(default=None, alias='SecurityGroupId')
    security_group_name: str | None = Field(default=None, alias='SecurityGroupName')

class DeleteSecurityGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteSecurityGroupRuleRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    flow: str = Field(alias='Flow')
    from_port_range: int | None = Field(default=None, alias='FromPortRange')
    ip_protocol: str | None = Field(default=None, alias='IpProtocol')
    ip_range: str | None = Field(default=None, alias='IpRange')
    rules: list[SecurityGroupRule] | None = Field(default=None, alias='Rules')
    security_group_account_id_to_unlink: str | None = Field(default=None, alias='SecurityGroupAccountIdToUnlink')
    security_group_id: str = Field(alias='SecurityGroupId')
    security_group_name_to_unlink: str | None = Field(default=None, alias='SecurityGroupNameToUnlink')
    to_port_range: int | None = Field(default=None, alias='ToPortRange')

class DeleteSecurityGroupRuleResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    security_group: SecurityGroup | None = Field(default=None, alias='SecurityGroup')

class DeleteServerCertificateRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    name: str = Field(alias='Name')

class DeleteServerCertificateResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteSnapshotRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    snapshot_id: str = Field(alias='SnapshotId')

class DeleteSnapshotResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteSubnetRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    subnet_id: str = Field(alias='SubnetId')

class DeleteSubnetResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteTagsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    resource_ids: list[str] = Field(alias='ResourceIds')
    tags: list[ResourceTag] = Field(alias='Tags')

class DeleteTagsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteUserGroupPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_name: str = Field(alias='PolicyName')
    user_group_name: str = Field(alias='UserGroupName')
    user_group_path: str | None = Field(default=None, alias='UserGroupPath')

class DeleteUserGroupPolicyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    force: bool | None = Field(default=None, alias='Force')
    path: str | None = Field(default=None, alias='Path')
    user_group_name: str = Field(alias='UserGroupName')

class DeleteUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteUserPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_name: str = Field(alias='PolicyName')
    user_name: str = Field(alias='UserName')

class DeleteUserPolicyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteUserRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_name: str = Field(alias='UserName')

class DeleteUserResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteVirtualGatewayRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    virtual_gateway_id: str = Field(alias='VirtualGatewayId')

class DeleteVirtualGatewayResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteVmGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_group_id: str = Field(alias='VmGroupId')

class DeleteVmGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteVmTemplateRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_template_id: str = Field(alias='VmTemplateId')

class DeleteVmTemplateResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteVmsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_ids: list[str] = Field(alias='VmIds')

class DeleteVmsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vms: list[VmState] | None = Field(default=None, alias='Vms')

class DeleteVolumeRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    volume_id: str = Field(alias='VolumeId')

class DeleteVolumeResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteVpnConnectionRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vpn_connection_id: str = Field(alias='VpnConnectionId')

class DeleteVpnConnectionResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeleteVpnConnectionRouteRequest(GeneratedModel):
    destination_ip_range: str = Field(alias='DestinationIpRange')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vpn_connection_id: str = Field(alias='VpnConnectionId')

class DeleteVpnConnectionRouteResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DeregisterVmsInLoadBalancerRequest(GeneratedModel):
    backend_vm_ids: list[str] = Field(alias='BackendVmIds')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')

class DeregisterVmsInLoadBalancerResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DhcpOptionsSet(GeneratedModel):
    default: bool | None = Field(default=None, alias='Default')
    dhcp_options_set_id: str | None = Field(default=None, alias='DhcpOptionsSetId')
    domain_name: str | None = Field(default=None, alias='DomainName')
    domain_name_servers: list[str] | None = Field(default=None, alias='DomainNameServers')
    log_servers: list[str] | None = Field(default=None, alias='LogServers')
    ntp_servers: list[str] | None = Field(default=None, alias='NtpServers')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class DirectLink(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    bandwidth: str | None = Field(default=None, alias='Bandwidth')
    direct_link_id: str | None = Field(default=None, alias='DirectLinkId')
    direct_link_name: str | None = Field(default=None, alias='DirectLinkName')
    location: str | None = Field(default=None, alias='Location')
    region_name: str | None = Field(default=None, alias='RegionName')
    state: str | None = Field(default=None, alias='State')

class DirectLinkInterface(GeneratedModel):
    bgp_asn: int = Field(alias='BgpAsn')
    bgp_key: str | None = Field(default=None, alias='BgpKey')
    client_private_ip: str | None = Field(default=None, alias='ClientPrivateIp')
    direct_link_interface_name: str = Field(alias='DirectLinkInterfaceName')
    outscale_private_ip: str | None = Field(default=None, alias='OutscalePrivateIp')
    virtual_gateway_id: str = Field(alias='VirtualGatewayId')
    vlan: int = Field(alias='Vlan')

class DirectLinkInterfaces(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    bgp_asn: int | None = Field(default=None, alias='BgpAsn')
    bgp_key: str | None = Field(default=None, alias='BgpKey')
    client_private_ip: str | None = Field(default=None, alias='ClientPrivateIp')
    direct_link_id: str | None = Field(default=None, alias='DirectLinkId')
    direct_link_interface_id: str | None = Field(default=None, alias='DirectLinkInterfaceId')
    direct_link_interface_name: str | None = Field(default=None, alias='DirectLinkInterfaceName')
    interface_type: str | None = Field(default=None, alias='InterfaceType')
    location: str | None = Field(default=None, alias='Location')
    mtu: int | None = Field(default=None, alias='Mtu')
    outscale_private_ip: str | None = Field(default=None, alias='OutscalePrivateIp')
    state: str | None = Field(default=None, alias='State')
    virtual_gateway_id: str | None = Field(default=None, alias='VirtualGatewayId')
    vlan: int | None = Field(default=None, alias='Vlan')

class DisableOutscaleLoginForUsersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DisableOutscaleLoginForUsersResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DisableOutscaleLoginPerUsersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_names: list[str] = Field(alias='UserNames')

class DisableOutscaleLoginPerUsersResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class DisableOutscaleLoginRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class DisableOutscaleLoginResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class EnableOutscaleLoginForUsersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class EnableOutscaleLoginForUsersResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class EnableOutscaleLoginPerUsersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_names: list[str] = Field(alias='UserNames')

class EnableOutscaleLoginPerUsersResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class EnableOutscaleLoginRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class EnableOutscaleLoginResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ErrorResponse(GeneratedModel):
    errors: list[Errors] | None = Field(default=None, alias='Errors')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class Errors(GeneratedModel):
    code: str | None = Field(default=None, alias='Code')
    details: str | None = Field(default=None, alias='Details')
    type: str | None = Field(default=None, alias='Type')

class FiltersAccessKeys(GeneratedModel):
    access_key_ids: list[str] | None = Field(default=None, alias='AccessKeyIds')
    states: list[str] | None = Field(default=None, alias='States')

class FiltersApiAccessRule(GeneratedModel):
    api_access_rule_ids: list[str] | None = Field(default=None, alias='ApiAccessRuleIds')
    ca_ids: list[str] | None = Field(default=None, alias='CaIds')
    cns: list[str] | None = Field(default=None, alias='Cns')
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')

class FiltersApiLog(GeneratedModel):
    query_access_keys: list[str] | None = Field(default=None, alias='QueryAccessKeys')
    query_api_names: list[str] | None = Field(default=None, alias='QueryApiNames')
    query_call_names: list[str] | None = Field(default=None, alias='QueryCallNames')
    query_date_after: str | None = Field(default=None, alias='QueryDateAfter')
    query_date_before: str | None = Field(default=None, alias='QueryDateBefore')
    query_ip_addresses: list[str] | None = Field(default=None, alias='QueryIpAddresses')
    query_user_agents: list[str] | None = Field(default=None, alias='QueryUserAgents')
    request_ids: list[str] | None = Field(default=None, alias='RequestIds')
    response_status_codes: list[int] | None = Field(default=None, alias='ResponseStatusCodes')

class FiltersCa(GeneratedModel):
    ca_fingerprints: list[str] | None = Field(default=None, alias='CaFingerprints')
    ca_ids: list[str] | None = Field(default=None, alias='CaIds')
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')

class FiltersCatalogs(GeneratedModel):
    current_catalog_only: bool | None = Field(default=None, alias='CurrentCatalogOnly')
    from_date: str | None = Field(default=None, alias='FromDate')
    to_date: str | None = Field(default=None, alias='ToDate')

class FiltersClientGateway(GeneratedModel):
    bgp_asns: list[int] | None = Field(default=None, alias='BgpAsns')
    client_gateway_ids: list[str] | None = Field(default=None, alias='ClientGatewayIds')
    connection_types: list[str] | None = Field(default=None, alias='ConnectionTypes')
    public_ips: list[str] | None = Field(default=None, alias='PublicIps')
    states: list[str] | None = Field(default=None, alias='States')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersDedicatedGroup(GeneratedModel):
    cpu_generations: list[int] | None = Field(default=None, alias='CpuGenerations')
    dedicated_group_ids: list[str] | None = Field(default=None, alias='DedicatedGroupIds')
    names: list[str] | None = Field(default=None, alias='Names')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')

class FiltersDhcpOptions(GeneratedModel):
    default: bool | None = Field(default=None, alias='Default')
    dhcp_options_set_ids: list[str] | None = Field(default=None, alias='DhcpOptionsSetIds')
    domain_name_servers: list[str] | None = Field(default=None, alias='DomainNameServers')
    domain_names: list[str] | None = Field(default=None, alias='DomainNames')
    log_servers: list[str] | None = Field(default=None, alias='LogServers')
    ntp_servers: list[str] | None = Field(default=None, alias='NtpServers')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersDirectLink(GeneratedModel):
    direct_link_ids: list[str] | None = Field(default=None, alias='DirectLinkIds')

class FiltersDirectLinkInterface(GeneratedModel):
    direct_link_ids: list[str] | None = Field(default=None, alias='DirectLinkIds')
    direct_link_interface_ids: list[str] | None = Field(default=None, alias='DirectLinkInterfaceIds')

class FiltersFlexibleGpu(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    flexible_gpu_ids: list[str] | None = Field(default=None, alias='FlexibleGpuIds')
    generations: list[str] | None = Field(default=None, alias='Generations')
    model_names: list[str] | None = Field(default=None, alias='ModelNames')
    states: list[str] | None = Field(default=None, alias='States')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    tags: list[Tag] | None = Field(default=None, alias='Tags')
    vm_ids: list[str] | None = Field(default=None, alias='VmIds')

class FiltersImage(GeneratedModel):
    account_aliases: list[str] | None = Field(default=None, alias='AccountAliases')
    account_ids: list[str] | None = Field(default=None, alias='AccountIds')
    architectures: list[str] | None = Field(default=None, alias='Architectures')
    block_device_mapping_delete_on_vm_deletion: bool | None = Field(default=None, alias='BlockDeviceMappingDeleteOnVmDeletion')
    block_device_mapping_device_names: list[str] | None = Field(default=None, alias='BlockDeviceMappingDeviceNames')
    block_device_mapping_snapshot_ids: list[str] | None = Field(default=None, alias='BlockDeviceMappingSnapshotIds')
    block_device_mapping_volume_sizes: list[int] | None = Field(default=None, alias='BlockDeviceMappingVolumeSizes')
    block_device_mapping_volume_types: list[str] | None = Field(default=None, alias='BlockDeviceMappingVolumeTypes')
    boot_modes: list[BootMode] | None = Field(default=None, alias='BootModes')
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')
    file_locations: list[str] | None = Field(default=None, alias='FileLocations')
    hypervisors: list[str] | None = Field(default=None, alias='Hypervisors')
    image_ids: list[str] | None = Field(default=None, alias='ImageIds')
    image_names: list[str] | None = Field(default=None, alias='ImageNames')
    permissions_to_launch_account_ids: list[str] | None = Field(default=None, alias='PermissionsToLaunchAccountIds')
    permissions_to_launch_global_permission: bool | None = Field(default=None, alias='PermissionsToLaunchGlobalPermission')
    product_code_names: list[str] | None = Field(default=None, alias='ProductCodeNames')
    product_codes: list[str] | None = Field(default=None, alias='ProductCodes')
    root_device_names: list[str] | None = Field(default=None, alias='RootDeviceNames')
    root_device_types: list[str] | None = Field(default=None, alias='RootDeviceTypes')
    secure_boot: bool | None = Field(default=None, alias='SecureBoot')
    states: list[str] | None = Field(default=None, alias='States')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    tpm_mandatory: bool | None = Field(default=None, alias='TpmMandatory')
    virtualization_types: list[str] | None = Field(default=None, alias='VirtualizationTypes')

class FiltersInternetService(GeneratedModel):
    internet_service_ids: list[str] | None = Field(default=None, alias='InternetServiceIds')
    link_net_ids: list[str] | None = Field(default=None, alias='LinkNetIds')
    link_states: list[str] | None = Field(default=None, alias='LinkStates')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersKeypair(GeneratedModel):
    keypair_fingerprints: list[str] | None = Field(default=None, alias='KeypairFingerprints')
    keypair_ids: list[str] | None = Field(default=None, alias='KeypairIds')
    keypair_names: list[str] | None = Field(default=None, alias='KeypairNames')
    keypair_types: list[str] | None = Field(default=None, alias='KeypairTypes')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersListenerRule(GeneratedModel):
    listener_rule_names: list[str] | None = Field(default=None, alias='ListenerRuleNames')

class FiltersLoadBalancer(GeneratedModel):
    load_balancer_names: list[str] | None = Field(default=None, alias='LoadBalancerNames')
    states: list[str] | None = Field(default=None, alias='States')

class FiltersNatService(GeneratedModel):
    client_tokens: list[str] | None = Field(default=None, alias='ClientTokens')
    nat_service_ids: list[str] | None = Field(default=None, alias='NatServiceIds')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    states: list[str] | None = Field(default=None, alias='States')
    subnet_ids: list[str] | None = Field(default=None, alias='SubnetIds')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersNet(GeneratedModel):
    dhcp_options_set_ids: list[str] | None = Field(default=None, alias='DhcpOptionsSetIds')
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')
    is_default: bool | None = Field(default=None, alias='IsDefault')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    states: list[str] | None = Field(default=None, alias='States')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersNetAccessPoint(GeneratedModel):
    net_access_point_ids: list[str] | None = Field(default=None, alias='NetAccessPointIds')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    service_names: list[str] | None = Field(default=None, alias='ServiceNames')
    states: list[str] | None = Field(default=None, alias='States')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersNetPeering(GeneratedModel):
    accepter_net_account_ids: list[str] | None = Field(default=None, alias='AccepterNetAccountIds')
    accepter_net_ip_ranges: list[str] | None = Field(default=None, alias='AccepterNetIpRanges')
    accepter_net_net_ids: list[str] | None = Field(default=None, alias='AccepterNetNetIds')
    expiration_dates: list[str] | None = Field(default=None, alias='ExpirationDates')
    net_peering_ids: list[str] | None = Field(default=None, alias='NetPeeringIds')
    source_net_account_ids: list[str] | None = Field(default=None, alias='SourceNetAccountIds')
    source_net_ip_ranges: list[str] | None = Field(default=None, alias='SourceNetIpRanges')
    source_net_net_ids: list[str] | None = Field(default=None, alias='SourceNetNetIds')
    state_messages: list[str] | None = Field(default=None, alias='StateMessages')
    state_names: list[str] | None = Field(default=None, alias='StateNames')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersNic(GeneratedModel):
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')
    is_source_dest_check: bool | None = Field(default=None, alias='IsSourceDestCheck')
    link_nic_delete_on_vm_deletion: bool | None = Field(default=None, alias='LinkNicDeleteOnVmDeletion')
    link_nic_device_numbers: list[int] | None = Field(default=None, alias='LinkNicDeviceNumbers')
    link_nic_link_nic_ids: list[str] | None = Field(default=None, alias='LinkNicLinkNicIds')
    link_nic_states: list[str] | None = Field(default=None, alias='LinkNicStates')
    link_nic_vm_account_ids: list[str] | None = Field(default=None, alias='LinkNicVmAccountIds')
    link_nic_vm_ids: list[str] | None = Field(default=None, alias='LinkNicVmIds')
    link_public_ip_account_ids: list[str] | None = Field(default=None, alias='LinkPublicIpAccountIds')
    link_public_ip_link_public_ip_ids: list[str] | None = Field(default=None, alias='LinkPublicIpLinkPublicIpIds')
    link_public_ip_public_dns_names: list[str] | None = Field(default=None, alias='LinkPublicIpPublicDnsNames')
    link_public_ip_public_ip_ids: list[str] | None = Field(default=None, alias='LinkPublicIpPublicIpIds')
    link_public_ip_public_ips: list[str] | None = Field(default=None, alias='LinkPublicIpPublicIps')
    mac_addresses: list[str] | None = Field(default=None, alias='MacAddresses')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    nic_ids: list[str] | None = Field(default=None, alias='NicIds')
    private_dns_names: list[str] | None = Field(default=None, alias='PrivateDnsNames')
    private_ips_link_public_ip_account_ids: list[str] | None = Field(default=None, alias='PrivateIpsLinkPublicIpAccountIds')
    private_ips_link_public_ip_public_ips: list[str] | None = Field(default=None, alias='PrivateIpsLinkPublicIpPublicIps')
    private_ips_primary_ip: bool | None = Field(default=None, alias='PrivateIpsPrimaryIp')
    private_ips_private_ips: list[str] | None = Field(default=None, alias='PrivateIpsPrivateIps')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    security_group_names: list[str] | None = Field(default=None, alias='SecurityGroupNames')
    states: list[str] | None = Field(default=None, alias='States')
    subnet_ids: list[str] | None = Field(default=None, alias='SubnetIds')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersProductType(GeneratedModel):
    product_type_ids: list[str] | None = Field(default=None, alias='ProductTypeIds')

class FiltersPublicIp(GeneratedModel):
    link_public_ip_ids: list[str] | None = Field(default=None, alias='LinkPublicIpIds')
    nic_account_ids: list[str] | None = Field(default=None, alias='NicAccountIds')
    nic_ids: list[str] | None = Field(default=None, alias='NicIds')
    placements: list[str] | None = Field(default=None, alias='Placements')
    private_ips: list[str] | None = Field(default=None, alias='PrivateIps')
    public_ip_ids: list[str] | None = Field(default=None, alias='PublicIpIds')
    public_ips: list[str] | None = Field(default=None, alias='PublicIps')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    vm_ids: list[str] | None = Field(default=None, alias='VmIds')

class FiltersQuota(GeneratedModel):
    collections: list[str] | None = Field(default=None, alias='Collections')
    quota_names: list[str] | None = Field(default=None, alias='QuotaNames')
    quota_types: list[str] | None = Field(default=None, alias='QuotaTypes')
    short_descriptions: list[str] | None = Field(default=None, alias='ShortDescriptions')

class FiltersReadImageExportTask(GeneratedModel):
    image_ids: list[str] | None = Field(default=None, alias='ImageIds')
    task_ids: list[str] | None = Field(default=None, alias='TaskIds')

class FiltersReadVolumeUpdateTask(GeneratedModel):
    task_ids: list[str] | None = Field(default=None, alias='TaskIds')
    volume_ids: list[str] | None = Field(default=None, alias='VolumeIds')

class FiltersRouteTable(GeneratedModel):
    link_route_table_ids: list[str] | None = Field(default=None, alias='LinkRouteTableIds')
    link_route_table_link_route_table_ids: list[str] | None = Field(default=None, alias='LinkRouteTableLinkRouteTableIds')
    link_route_table_main: bool | None = Field(default=None, alias='LinkRouteTableMain')
    link_subnet_ids: list[str] | None = Field(default=None, alias='LinkSubnetIds')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    route_creation_methods: list[str] | None = Field(default=None, alias='RouteCreationMethods')
    route_destination_ip_ranges: list[str] | None = Field(default=None, alias='RouteDestinationIpRanges')
    route_destination_service_ids: list[str] | None = Field(default=None, alias='RouteDestinationServiceIds')
    route_gateway_ids: list[str] | None = Field(default=None, alias='RouteGatewayIds')
    route_nat_service_ids: list[str] | None = Field(default=None, alias='RouteNatServiceIds')
    route_net_peering_ids: list[str] | None = Field(default=None, alias='RouteNetPeeringIds')
    route_states: list[str] | None = Field(default=None, alias='RouteStates')
    route_table_ids: list[str] | None = Field(default=None, alias='RouteTableIds')
    route_vm_ids: list[str] | None = Field(default=None, alias='RouteVmIds')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersSecurityGroup(GeneratedModel):
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')
    inbound_rule_account_ids: list[str] | None = Field(default=None, alias='InboundRuleAccountIds')
    inbound_rule_from_port_ranges: list[int] | None = Field(default=None, alias='InboundRuleFromPortRanges')
    inbound_rule_ip_ranges: list[str] | None = Field(default=None, alias='InboundRuleIpRanges')
    inbound_rule_protocols: list[str] | None = Field(default=None, alias='InboundRuleProtocols')
    inbound_rule_security_group_ids: list[str] | None = Field(default=None, alias='InboundRuleSecurityGroupIds')
    inbound_rule_security_group_names: list[str] | None = Field(default=None, alias='InboundRuleSecurityGroupNames')
    inbound_rule_to_port_ranges: list[int] | None = Field(default=None, alias='InboundRuleToPortRanges')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    outbound_rule_account_ids: list[str] | None = Field(default=None, alias='OutboundRuleAccountIds')
    outbound_rule_from_port_ranges: list[int] | None = Field(default=None, alias='OutboundRuleFromPortRanges')
    outbound_rule_ip_ranges: list[str] | None = Field(default=None, alias='OutboundRuleIpRanges')
    outbound_rule_protocols: list[str] | None = Field(default=None, alias='OutboundRuleProtocols')
    outbound_rule_security_group_ids: list[str] | None = Field(default=None, alias='OutboundRuleSecurityGroupIds')
    outbound_rule_security_group_names: list[str] | None = Field(default=None, alias='OutboundRuleSecurityGroupNames')
    outbound_rule_to_port_ranges: list[int] | None = Field(default=None, alias='OutboundRuleToPortRanges')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    security_group_names: list[str] | None = Field(default=None, alias='SecurityGroupNames')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersServerCertificate(GeneratedModel):
    paths: list[str] | None = Field(default=None, alias='Paths')

class FiltersService(GeneratedModel):
    service_ids: list[str] | None = Field(default=None, alias='ServiceIds')
    service_names: list[str] | None = Field(default=None, alias='ServiceNames')

class FiltersSnapshot(GeneratedModel):
    account_aliases: list[str] | None = Field(default=None, alias='AccountAliases')
    account_ids: list[str] | None = Field(default=None, alias='AccountIds')
    client_tokens: list[str] | None = Field(default=None, alias='ClientTokens')
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')
    from_creation_date: str | None = Field(default=None, alias='FromCreationDate')
    permissions_to_create_volume_account_ids: list[str] | None = Field(default=None, alias='PermissionsToCreateVolumeAccountIds')
    permissions_to_create_volume_global_permission: bool | None = Field(default=None, alias='PermissionsToCreateVolumeGlobalPermission')
    progresses: list[int] | None = Field(default=None, alias='Progresses')
    snapshot_ids: list[str] | None = Field(default=None, alias='SnapshotIds')
    states: list[str] | None = Field(default=None, alias='States')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    to_creation_date: str | None = Field(default=None, alias='ToCreationDate')
    volume_ids: list[str] | None = Field(default=None, alias='VolumeIds')
    volume_sizes: list[int] | None = Field(default=None, alias='VolumeSizes')

class FiltersSnapshotExportTask(GeneratedModel):
    snapshot_ids: list[str] | None = Field(default=None, alias='SnapshotIds')
    task_ids: list[str] | None = Field(default=None, alias='TaskIds')

class FiltersSubnet(GeneratedModel):
    available_ips_counts: list[int] | None = Field(default=None, alias='AvailableIpsCounts')
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    states: list[str] | None = Field(default=None, alias='States')
    subnet_ids: list[str] | None = Field(default=None, alias='SubnetIds')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')

class FiltersSubregion(GeneratedModel):
    region_names: list[str] | None = Field(default=None, alias='RegionNames')
    states: list[str] | None = Field(default=None, alias='States')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')

class FiltersTag(GeneratedModel):
    keys: list[str] | None = Field(default=None, alias='Keys')
    resource_ids: list[str] | None = Field(default=None, alias='ResourceIds')
    resource_types: list[str] | None = Field(default=None, alias='ResourceTypes')
    values: list[str] | None = Field(default=None, alias='Values')

class FiltersUserGroup(GeneratedModel):
    path_prefix: str | None = Field(default=None, alias='PathPrefix')
    user_group_ids: list[str] | None = Field(default=None, alias='UserGroupIds')

class FiltersUsers(GeneratedModel):
    user_ids: list[str] | None = Field(default=None, alias='UserIds')

class FiltersVirtualGateway(GeneratedModel):
    connection_types: list[str] | None = Field(default=None, alias='ConnectionTypes')
    link_net_ids: list[str] | None = Field(default=None, alias='LinkNetIds')
    link_states: list[str] | None = Field(default=None, alias='LinkStates')
    states: list[str] | None = Field(default=None, alias='States')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    virtual_gateway_ids: list[str] | None = Field(default=None, alias='VirtualGatewayIds')

class FiltersVm(GeneratedModel):
    architectures: list[str] | None = Field(default=None, alias='Architectures')
    block_device_mapping_delete_on_vm_deletion: bool | None = Field(default=None, alias='BlockDeviceMappingDeleteOnVmDeletion')
    block_device_mapping_device_names: list[str] | None = Field(default=None, alias='BlockDeviceMappingDeviceNames')
    block_device_mapping_link_dates: list[str] | None = Field(default=None, alias='BlockDeviceMappingLinkDates')
    block_device_mapping_states: list[str] | None = Field(default=None, alias='BlockDeviceMappingStates')
    block_device_mapping_volume_ids: list[str] | None = Field(default=None, alias='BlockDeviceMappingVolumeIds')
    boot_modes: list[BootMode] | None = Field(default=None, alias='BootModes')
    client_tokens: list[str] | None = Field(default=None, alias='ClientTokens')
    creation_dates: list[str] | None = Field(default=None, alias='CreationDates')
    image_ids: list[str] | None = Field(default=None, alias='ImageIds')
    is_source_dest_checked: bool | None = Field(default=None, alias='IsSourceDestChecked')
    keypair_names: list[str] | None = Field(default=None, alias='KeypairNames')
    launch_numbers: list[int] | None = Field(default=None, alias='LaunchNumbers')
    lifecycles: list[str] | None = Field(default=None, alias='Lifecycles')
    net_ids: list[str] | None = Field(default=None, alias='NetIds')
    nic_account_ids: list[str] | None = Field(default=None, alias='NicAccountIds')
    nic_descriptions: list[str] | None = Field(default=None, alias='NicDescriptions')
    nic_is_source_dest_checked: bool | None = Field(default=None, alias='NicIsSourceDestChecked')
    nic_link_nic_delete_on_vm_deletion: bool | None = Field(default=None, alias='NicLinkNicDeleteOnVmDeletion')
    nic_link_nic_device_numbers: list[int] | None = Field(default=None, alias='NicLinkNicDeviceNumbers')
    nic_link_nic_link_nic_dates: list[str] | None = Field(default=None, alias='NicLinkNicLinkNicDates')
    nic_link_nic_link_nic_ids: list[str] | None = Field(default=None, alias='NicLinkNicLinkNicIds')
    nic_link_nic_states: list[str] | None = Field(default=None, alias='NicLinkNicStates')
    nic_link_nic_vm_account_ids: list[str] | None = Field(default=None, alias='NicLinkNicVmAccountIds')
    nic_link_nic_vm_ids: list[str] | None = Field(default=None, alias='NicLinkNicVmIds')
    nic_link_public_ip_account_ids: list[str] | None = Field(default=None, alias='NicLinkPublicIpAccountIds')
    nic_link_public_ip_link_public_ip_ids: list[str] | None = Field(default=None, alias='NicLinkPublicIpLinkPublicIpIds')
    nic_link_public_ip_public_ip_ids: list[str] | None = Field(default=None, alias='NicLinkPublicIpPublicIpIds')
    nic_link_public_ip_public_ips: list[str] | None = Field(default=None, alias='NicLinkPublicIpPublicIps')
    nic_mac_addresses: list[str] | None = Field(default=None, alias='NicMacAddresses')
    nic_net_ids: list[str] | None = Field(default=None, alias='NicNetIds')
    nic_nic_ids: list[str] | None = Field(default=None, alias='NicNicIds')
    nic_private_ips_link_public_ip_account_ids: list[str] | None = Field(default=None, alias='NicPrivateIpsLinkPublicIpAccountIds')
    nic_private_ips_link_public_ip_ids: list[str] | None = Field(default=None, alias='NicPrivateIpsLinkPublicIpIds')
    nic_private_ips_primary_ip: bool | None = Field(default=None, alias='NicPrivateIpsPrimaryIp')
    nic_private_ips_private_ips: list[str] | None = Field(default=None, alias='NicPrivateIpsPrivateIps')
    nic_security_group_ids: list[str] | None = Field(default=None, alias='NicSecurityGroupIds')
    nic_security_group_names: list[str] | None = Field(default=None, alias='NicSecurityGroupNames')
    nic_states: list[str] | None = Field(default=None, alias='NicStates')
    nic_subnet_ids: list[str] | None = Field(default=None, alias='NicSubnetIds')
    nic_subregion_names: list[str] | None = Field(default=None, alias='NicSubregionNames')
    platforms: list[str] | None = Field(default=None, alias='Platforms')
    private_ips: list[str] | None = Field(default=None, alias='PrivateIps')
    product_codes: list[str] | None = Field(default=None, alias='ProductCodes')
    public_ips: list[str] | None = Field(default=None, alias='PublicIps')
    reservation_ids: list[str] | None = Field(default=None, alias='ReservationIds')
    root_device_names: list[str] | None = Field(default=None, alias='RootDeviceNames')
    root_device_types: list[str] | None = Field(default=None, alias='RootDeviceTypes')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    security_group_names: list[str] | None = Field(default=None, alias='SecurityGroupNames')
    state_reason_codes: list[int] | None = Field(default=None, alias='StateReasonCodes')
    state_reason_messages: list[str] | None = Field(default=None, alias='StateReasonMessages')
    state_reasons: list[str] | None = Field(default=None, alias='StateReasons')
    subnet_ids: list[str] | None = Field(default=None, alias='SubnetIds')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    tenancies: list[str] | None = Field(default=None, alias='Tenancies')
    tpm_enabled: bool | None = Field(default=None, alias='TpmEnabled')
    vm_ids: list[str] | None = Field(default=None, alias='VmIds')
    vm_security_group_ids: list[str] | None = Field(default=None, alias='VmSecurityGroupIds')
    vm_security_group_names: list[str] | None = Field(default=None, alias='VmSecurityGroupNames')
    vm_state_codes: list[int] | None = Field(default=None, alias='VmStateCodes')
    vm_state_names: list[str] | None = Field(default=None, alias='VmStateNames')
    vm_types: list[str] | None = Field(default=None, alias='VmTypes')

class FiltersVmGroup(GeneratedModel):
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    subnet_ids: list[str] | None = Field(default=None, alias='SubnetIds')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    vm_counts: list[int] | None = Field(default=None, alias='VmCounts')
    vm_group_ids: list[str] | None = Field(default=None, alias='VmGroupIds')
    vm_group_names: list[str] | None = Field(default=None, alias='VmGroupNames')
    vm_template_ids: list[str] | None = Field(default=None, alias='VmTemplateIds')

class FiltersVmTemplate(GeneratedModel):
    cpu_cores: list[int] | None = Field(default=None, alias='CpuCores')
    cpu_generations: list[str] | None = Field(default=None, alias='CpuGenerations')
    cpu_performances: list[str] | None = Field(default=None, alias='CpuPerformances')
    descriptions: list[str] | None = Field(default=None, alias='Descriptions')
    image_ids: list[str] | None = Field(default=None, alias='ImageIds')
    keypair_names: list[str] | None = Field(default=None, alias='KeypairNames')
    rams: list[int] | None = Field(default=None, alias='Rams')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    vm_template_ids: list[str] | None = Field(default=None, alias='VmTemplateIds')
    vm_template_names: list[str] | None = Field(default=None, alias='VmTemplateNames')

class FiltersVmType(GeneratedModel):
    bsu_optimized: bool | None = Field(default=None, alias='BsuOptimized')
    ephemerals_types: list[str] | None = Field(default=None, alias='EphemeralsTypes')
    eths: list[int] | None = Field(default=None, alias='Eths')
    gpus: list[int] | None = Field(default=None, alias='Gpus')
    memory_sizes: list[float] | None = Field(default=None, alias='MemorySizes')
    vcore_counts: list[int] | None = Field(default=None, alias='VcoreCounts')
    vm_type_names: list[str] | None = Field(default=None, alias='VmTypeNames')
    volume_counts: list[int] | None = Field(default=None, alias='VolumeCounts')
    volume_sizes: list[int] | None = Field(default=None, alias='VolumeSizes')

class FiltersVmsState(GeneratedModel):
    maintenance_event_codes: list[str] | None = Field(default=None, alias='MaintenanceEventCodes')
    maintenance_event_descriptions: list[str] | None = Field(default=None, alias='MaintenanceEventDescriptions')
    maintenance_events_not_after: list[str] | None = Field(default=None, alias='MaintenanceEventsNotAfter')
    maintenance_events_not_before: list[str] | None = Field(default=None, alias='MaintenanceEventsNotBefore')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    vm_ids: list[str] | None = Field(default=None, alias='VmIds')
    vm_states: list[str] | None = Field(default=None, alias='VmStates')

class FiltersVolume(GeneratedModel):
    client_tokens: list[str] | None = Field(default=None, alias='ClientTokens')
    creation_dates: list[str] | None = Field(default=None, alias='CreationDates')
    link_volume_delete_on_vm_deletion: bool | None = Field(default=None, alias='LinkVolumeDeleteOnVmDeletion')
    link_volume_device_names: list[str] | None = Field(default=None, alias='LinkVolumeDeviceNames')
    link_volume_link_dates: list[str] | None = Field(default=None, alias='LinkVolumeLinkDates')
    link_volume_link_states: list[str] | None = Field(default=None, alias='LinkVolumeLinkStates')
    link_volume_vm_ids: list[str] | None = Field(default=None, alias='LinkVolumeVmIds')
    snapshot_ids: list[str] | None = Field(default=None, alias='SnapshotIds')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    volume_ids: list[str] | None = Field(default=None, alias='VolumeIds')
    volume_sizes: list[int] | None = Field(default=None, alias='VolumeSizes')
    volume_states: list[str] | None = Field(default=None, alias='VolumeStates')
    volume_types: list[str] | None = Field(default=None, alias='VolumeTypes')

class FiltersVpnConnection(GeneratedModel):
    bgp_asns: list[int] | None = Field(default=None, alias='BgpAsns')
    client_gateway_ids: list[str] | None = Field(default=None, alias='ClientGatewayIds')
    connection_types: list[str] | None = Field(default=None, alias='ConnectionTypes')
    route_destination_ip_ranges: list[str] | None = Field(default=None, alias='RouteDestinationIpRanges')
    states: list[str] | None = Field(default=None, alias='States')
    static_routes_only: bool | None = Field(default=None, alias='StaticRoutesOnly')
    tag_keys: list[str] | None = Field(default=None, alias='TagKeys')
    tag_values: list[str] | None = Field(default=None, alias='TagValues')
    tags: list[str] | None = Field(default=None, alias='Tags')
    virtual_gateway_ids: list[str] | None = Field(default=None, alias='VirtualGatewayIds')
    vpn_connection_ids: list[str] | None = Field(default=None, alias='VpnConnectionIds')

class FlexibleGpu(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    flexible_gpu_id: str | None = Field(default=None, alias='FlexibleGpuId')
    generation: str | None = Field(default=None, alias='Generation')
    model_name: str | None = Field(default=None, alias='ModelName')
    state: str | None = Field(default=None, alias='State')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    tags: list[Tag] | None = Field(default=None, alias='Tags')
    vm_id: str | None = Field(default=None, alias='VmId')

class FlexibleGpuCatalog(GeneratedModel):
    generations: list[str] | None = Field(default=None, alias='Generations')
    max_cpu: int | None = Field(default=None, alias='MaxCpu')
    max_ram: int | None = Field(default=None, alias='MaxRam')
    model_name: str | None = Field(default=None, alias='ModelName')
    v_ram: int | None = Field(default=None, alias='VRam')

class HealthCheck(GeneratedModel):
    check_interval: int = Field(alias='CheckInterval')
    healthy_threshold: int = Field(alias='HealthyThreshold')
    path: str | None = Field(default=None, alias='Path')
    port: int = Field(alias='Port')
    protocol: str = Field(alias='Protocol')
    timeout: int = Field(alias='Timeout')
    unhealthy_threshold: int = Field(alias='UnhealthyThreshold')

class Image(GeneratedModel):
    account_alias: str | None = Field(default=None, alias='AccountAlias')
    account_id: str | None = Field(default=None, alias='AccountId')
    architecture: str | None = Field(default=None, alias='Architecture')
    block_device_mappings: list[BlockDeviceMappingImage] | None = Field(default=None, alias='BlockDeviceMappings')
    boot_modes: list[BootMode] | None = Field(default=None, alias='BootModes')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    description: str | None = Field(default=None, alias='Description')
    file_location: str | None = Field(default=None, alias='FileLocation')
    image_id: str | None = Field(default=None, alias='ImageId')
    image_name: str | None = Field(default=None, alias='ImageName')
    image_type: str | None = Field(default=None, alias='ImageType')
    permissions_to_launch: PermissionsOnResource | None = Field(default=None, alias='PermissionsToLaunch')
    product_codes: list[str] | None = Field(default=None, alias='ProductCodes')
    root_device_name: str | None = Field(default=None, alias='RootDeviceName')
    root_device_type: str | None = Field(default=None, alias='RootDeviceType')
    secure_boot: bool | None = Field(default=None, alias='SecureBoot')
    state: str | None = Field(default=None, alias='State')
    state_comment: StateComment | None = Field(default=None, alias='StateComment')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    tpm_mandatory: bool | None = Field(default=None, alias='TpmMandatory')

class ImageExportTask(GeneratedModel):
    comment: str | None = Field(default=None, alias='Comment')
    image_id: str | None = Field(default=None, alias='ImageId')
    osu_export: OsuExportImageExportTask | None = Field(default=None, alias='OsuExport')
    progress: int | None = Field(default=None, alias='Progress')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    task_id: str | None = Field(default=None, alias='TaskId')

class InlinePolicy(GeneratedModel):
    body: str | None = Field(default=None, alias='Body')
    name: str | None = Field(default=None, alias='Name')

class InternetService(GeneratedModel):
    internet_service_id: str | None = Field(default=None, alias='InternetServiceId')
    net_id: str | None = Field(default=None, alias='NetId')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class Keypair(GeneratedModel):
    keypair_fingerprint: str | None = Field(default=None, alias='KeypairFingerprint')
    keypair_id: str | None = Field(default=None, alias='KeypairId')
    keypair_name: str | None = Field(default=None, alias='KeypairName')
    keypair_type: str | None = Field(default=None, alias='KeypairType')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class KeypairCreated(GeneratedModel):
    keypair_fingerprint: str | None = Field(default=None, alias='KeypairFingerprint')
    keypair_id: str | None = Field(default=None, alias='KeypairId')
    keypair_name: str | None = Field(default=None, alias='KeypairName')
    keypair_type: str | None = Field(default=None, alias='KeypairType')
    private_key: str | None = Field(default=None, alias='PrivateKey')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class LinkFlexibleGpuRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    flexible_gpu_id: str = Field(alias='FlexibleGpuId')
    vm_id: str = Field(alias='VmId')

class LinkFlexibleGpuResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkInternetServiceRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    internet_service_id: str = Field(alias='InternetServiceId')
    net_id: str = Field(alias='NetId')

class LinkInternetServiceResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkLoadBalancerBackendMachinesRequest(GeneratedModel):
    backend_ips: list[str] | None = Field(default=None, alias='BackendIps')
    backend_vm_ids: list[str] | None = Field(default=None, alias='BackendVmIds')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')

class LinkLoadBalancerBackendMachinesResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkManagedPolicyToUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_orn: str = Field(alias='PolicyOrn')
    user_group_name: str = Field(alias='UserGroupName')

class LinkManagedPolicyToUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkNic(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    device_number: int | None = Field(default=None, alias='DeviceNumber')
    link_nic_id: str | None = Field(default=None, alias='LinkNicId')
    state: str | None = Field(default=None, alias='State')
    vm_account_id: str | None = Field(default=None, alias='VmAccountId')
    vm_id: str | None = Field(default=None, alias='VmId')

class LinkNicLight(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    device_number: int | None = Field(default=None, alias='DeviceNumber')
    link_nic_id: str | None = Field(default=None, alias='LinkNicId')
    state: str | None = Field(default=None, alias='State')

class LinkNicRequest(GeneratedModel):
    device_number: int = Field(alias='DeviceNumber')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    nic_id: str = Field(alias='NicId')
    vm_id: str = Field(alias='VmId')

class LinkNicResponse(GeneratedModel):
    link_nic_id: str | None = Field(default=None, alias='LinkNicId')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkNicToUpdate(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    link_nic_id: str | None = Field(default=None, alias='LinkNicId')

class LinkPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_orn: str = Field(alias='PolicyOrn')
    user_name: str = Field(alias='UserName')

class LinkPolicyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkPrivateIpsRequest(GeneratedModel):
    allow_relink: bool | None = Field(default=None, alias='AllowRelink')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    nic_id: str = Field(alias='NicId')
    private_ips: list[str] | None = Field(default=None, alias='PrivateIps')
    secondary_private_ip_count: int | None = Field(default=None, alias='SecondaryPrivateIpCount')

class LinkPrivateIpsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkPublicIp(GeneratedModel):
    link_public_ip_id: str | None = Field(default=None, alias='LinkPublicIpId')
    public_dns_name: str | None = Field(default=None, alias='PublicDnsName')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    public_ip_account_id: str | None = Field(default=None, alias='PublicIpAccountId')
    public_ip_id: str | None = Field(default=None, alias='PublicIpId')

class LinkPublicIpLightForVm(GeneratedModel):
    public_dns_name: str | None = Field(default=None, alias='PublicDnsName')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    public_ip_account_id: str | None = Field(default=None, alias='PublicIpAccountId')

class LinkPublicIpRequest(GeneratedModel):
    allow_relink: bool | None = Field(default=None, alias='AllowRelink')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    nic_id: str | None = Field(default=None, alias='NicId')
    private_ip: str | None = Field(default=None, alias='PrivateIp')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    public_ip_id: str | None = Field(default=None, alias='PublicIpId')
    vm_id: str | None = Field(default=None, alias='VmId')

class LinkPublicIpResponse(GeneratedModel):
    link_public_ip_id: str | None = Field(default=None, alias='LinkPublicIpId')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkRouteTable(GeneratedModel):
    link_route_table_id: str | None = Field(default=None, alias='LinkRouteTableId')
    main: bool | None = Field(default=None, alias='Main')
    net_id: str | None = Field(default=None, alias='NetId')
    route_table_id: str | None = Field(default=None, alias='RouteTableId')
    subnet_id: str | None = Field(default=None, alias='SubnetId')

class LinkRouteTableRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    route_table_id: str = Field(alias='RouteTableId')
    subnet_id: str = Field(alias='SubnetId')

class LinkRouteTableResponse(GeneratedModel):
    link_route_table_id: str | None = Field(default=None, alias='LinkRouteTableId')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkVirtualGatewayRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_id: str = Field(alias='NetId')
    virtual_gateway_id: str = Field(alias='VirtualGatewayId')

class LinkVirtualGatewayResponse(GeneratedModel):
    net_to_virtual_gateway_link: NetToVirtualGatewayLink | None = Field(default=None, alias='NetToVirtualGatewayLink')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkVolumeRequest(GeneratedModel):
    device_name: str = Field(alias='DeviceName')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_id: str = Field(alias='VmId')
    volume_id: str = Field(alias='VolumeId')

class LinkVolumeResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class LinkedPolicy(GeneratedModel):
    creation_date: str | None = Field(default=None, alias='CreationDate')
    last_modification_date: str | None = Field(default=None, alias='LastModificationDate')
    orn: str | None = Field(default=None, alias='Orn')
    policy_id: str | None = Field(default=None, alias='PolicyId')
    policy_name: str | None = Field(default=None, alias='PolicyName')

class LinkedVolume(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    device_name: str | None = Field(default=None, alias='DeviceName')
    state: str | None = Field(default=None, alias='State')
    vm_id: str | None = Field(default=None, alias='VmId')
    volume_id: str | None = Field(default=None, alias='VolumeId')

class Listener(GeneratedModel):
    backend_port: int | None = Field(default=None, alias='BackendPort')
    backend_protocol: str | None = Field(default=None, alias='BackendProtocol')
    load_balancer_port: int | None = Field(default=None, alias='LoadBalancerPort')
    load_balancer_protocol: str | None = Field(default=None, alias='LoadBalancerProtocol')
    policy_names: list[str] | None = Field(default=None, alias='PolicyNames')
    server_certificate_id: str | None = Field(default=None, alias='ServerCertificateId')

class ListenerForCreation(GeneratedModel):
    backend_port: int = Field(alias='BackendPort')
    backend_protocol: str | None = Field(default=None, alias='BackendProtocol')
    load_balancer_port: int = Field(alias='LoadBalancerPort')
    load_balancer_protocol: str = Field(alias='LoadBalancerProtocol')
    server_certificate_id: str | None = Field(default=None, alias='ServerCertificateId')

class ListenerRule(GeneratedModel):
    action: str | None = Field(default=None, alias='Action')
    host_name_pattern: str | None = Field(default=None, alias='HostNamePattern')
    listener_id: int | None = Field(default=None, alias='ListenerId')
    listener_rule_id: int | None = Field(default=None, alias='ListenerRuleId')
    listener_rule_name: str | None = Field(default=None, alias='ListenerRuleName')
    path_pattern: str | None = Field(default=None, alias='PathPattern')
    priority: int | None = Field(default=None, alias='Priority')
    vm_ids: list[str] | None = Field(default=None, alias='VmIds')

class ListenerRuleForCreation(GeneratedModel):
    action: str | None = Field(default=None, alias='Action')
    host_name_pattern: str | None = Field(default=None, alias='HostNamePattern')
    listener_rule_name: str = Field(alias='ListenerRuleName')
    path_pattern: str | None = Field(default=None, alias='PathPattern')
    priority: int = Field(alias='Priority')

class LoadBalancer(GeneratedModel):
    access_log: AccessLog | None = Field(default=None, alias='AccessLog')
    application_sticky_cookie_policies: list[ApplicationStickyCookiePolicy] | None = Field(default=None, alias='ApplicationStickyCookiePolicies')
    backend_ips: list[str] | None = Field(default=None, alias='BackendIps')
    backend_vm_ids: list[str] | None = Field(default=None, alias='BackendVmIds')
    dns_name: str | None = Field(default=None, alias='DnsName')
    health_check: HealthCheck | None = Field(default=None, alias='HealthCheck')
    listeners: list[Listener] | None = Field(default=None, alias='Listeners')
    load_balancer_name: str | None = Field(default=None, alias='LoadBalancerName')
    load_balancer_sticky_cookie_policies: list[LoadBalancerStickyCookiePolicy] | None = Field(default=None, alias='LoadBalancerStickyCookiePolicies')
    load_balancer_type: str | None = Field(default=None, alias='LoadBalancerType')
    net_id: str | None = Field(default=None, alias='NetId')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    secured_cookies: bool | None = Field(default=None, alias='SecuredCookies')
    security_groups: list[str] | None = Field(default=None, alias='SecurityGroups')
    source_security_group: SourceSecurityGroup | None = Field(default=None, alias='SourceSecurityGroup')
    state: str | None = Field(default=None, alias='State')
    subnets: list[str] | None = Field(default=None, alias='Subnets')
    subregion_names: list[str] | None = Field(default=None, alias='SubregionNames')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class LoadBalancerLight(GeneratedModel):
    load_balancer_name: str = Field(alias='LoadBalancerName')
    load_balancer_port: int = Field(alias='LoadBalancerPort')

class LoadBalancerStickyCookiePolicy(GeneratedModel):
    cookie_expiration_period: int | None = Field(default=None, alias='CookieExpirationPeriod')
    policy_name: str | None = Field(default=None, alias='PolicyName')

class LoadBalancerTag(GeneratedModel):
    key: str | None = Field(default=None, alias='Key')
    load_balancer_name: str | None = Field(default=None, alias='LoadBalancerName')
    value: str | None = Field(default=None, alias='Value')

class Location(GeneratedModel):
    code: str | None = Field(default=None, alias='Code')
    name: str | None = Field(default=None, alias='Name')

class Log(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    call_duration: int | None = Field(default=None, alias='CallDuration')
    query_access_key: str | None = Field(default=None, alias='QueryAccessKey')
    query_api_name: str | None = Field(default=None, alias='QueryApiName')
    query_api_version: str | None = Field(default=None, alias='QueryApiVersion')
    query_call_name: str | None = Field(default=None, alias='QueryCallName')
    query_date: str | None = Field(default=None, alias='QueryDate')
    query_header_raw: str | None = Field(default=None, alias='QueryHeaderRaw')
    query_header_size: int | None = Field(default=None, alias='QueryHeaderSize')
    query_ip_address: str | None = Field(default=None, alias='QueryIpAddress')
    query_payload_raw: str | None = Field(default=None, alias='QueryPayloadRaw')
    query_payload_size: int | None = Field(default=None, alias='QueryPayloadSize')
    query_user_agent: str | None = Field(default=None, alias='QueryUserAgent')
    request_id: str | None = Field(default=None, alias='RequestId')
    response_size: int | None = Field(default=None, alias='ResponseSize')
    response_status_code: int | None = Field(default=None, alias='ResponseStatusCode')

class MaintenanceEvent(GeneratedModel):
    code: str | None = Field(default=None, alias='Code')
    description: str | None = Field(default=None, alias='Description')
    not_after: str | None = Field(default=None, alias='NotAfter')
    not_before: str | None = Field(default=None, alias='NotBefore')

class MinimalPolicy(GeneratedModel):
    id: str | None = Field(default=None, alias='Id')
    name: str | None = Field(default=None, alias='Name')
    orn: str | None = Field(default=None, alias='Orn')

class NatService(GeneratedModel):
    client_token: str | None = Field(default=None, alias='ClientToken')
    nat_service_id: str | None = Field(default=None, alias='NatServiceId')
    net_id: str | None = Field(default=None, alias='NetId')
    public_ips: list[PublicIpLight] | None = Field(default=None, alias='PublicIps')
    state: str | None = Field(default=None, alias='State')
    subnet_id: str | None = Field(default=None, alias='SubnetId')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class Net(GeneratedModel):
    dhcp_options_set_id: str | None = Field(default=None, alias='DhcpOptionsSetId')
    ip_range: str | None = Field(default=None, alias='IpRange')
    net_id: str | None = Field(default=None, alias='NetId')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    tenancy: str | None = Field(default=None, alias='Tenancy')

class NetAccessPoint(GeneratedModel):
    net_access_point_id: str | None = Field(default=None, alias='NetAccessPointId')
    net_id: str | None = Field(default=None, alias='NetId')
    route_table_ids: list[str] | None = Field(default=None, alias='RouteTableIds')
    service_name: str | None = Field(default=None, alias='ServiceName')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class NetPeering(GeneratedModel):
    accepter_net: AccepterNet | None = Field(default=None, alias='AccepterNet')
    expiration_date: str | None = Field(default=None, alias='ExpirationDate')
    net_peering_id: str | None = Field(default=None, alias='NetPeeringId')
    source_net: SourceNet | None = Field(default=None, alias='SourceNet')
    state: NetPeeringState | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class NetPeeringState(GeneratedModel):
    message: str | None = Field(default=None, alias='Message')
    name: str | None = Field(default=None, alias='Name')

class NetToVirtualGatewayLink(GeneratedModel):
    net_id: str | None = Field(default=None, alias='NetId')
    state: str | None = Field(default=None, alias='State')

class Nic(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    description: str | None = Field(default=None, alias='Description')
    is_source_dest_checked: bool | None = Field(default=None, alias='IsSourceDestChecked')
    link_nic: LinkNic | None = Field(default=None, alias='LinkNic')
    link_public_ip: LinkPublicIp | None = Field(default=None, alias='LinkPublicIp')
    mac_address: str | None = Field(default=None, alias='MacAddress')
    net_id: str | None = Field(default=None, alias='NetId')
    nic_id: str | None = Field(default=None, alias='NicId')
    private_dns_name: str | None = Field(default=None, alias='PrivateDnsName')
    private_ips: list[PrivateIp] | None = Field(default=None, alias='PrivateIps')
    security_groups: list[SecurityGroupLight] | None = Field(default=None, alias='SecurityGroups')
    state: str | None = Field(default=None, alias='State')
    subnet_id: str | None = Field(default=None, alias='SubnetId')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class NicForVmCreation(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    description: str | None = Field(default=None, alias='Description')
    device_number: int | None = Field(default=None, alias='DeviceNumber')
    nic_id: str | None = Field(default=None, alias='NicId')
    private_ips: list[PrivateIpLight] | None = Field(default=None, alias='PrivateIps')
    secondary_private_ip_count: int | None = Field(default=None, alias='SecondaryPrivateIpCount')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    subnet_id: str | None = Field(default=None, alias='SubnetId')

class NicLight(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    description: str | None = Field(default=None, alias='Description')
    is_source_dest_checked: bool | None = Field(default=None, alias='IsSourceDestChecked')
    link_nic: LinkNicLight | None = Field(default=None, alias='LinkNic')
    link_public_ip: LinkPublicIpLightForVm | None = Field(default=None, alias='LinkPublicIp')
    mac_address: str | None = Field(default=None, alias='MacAddress')
    net_id: str | None = Field(default=None, alias='NetId')
    nic_id: str | None = Field(default=None, alias='NicId')
    private_dns_name: str | None = Field(default=None, alias='PrivateDnsName')
    private_ips: list[PrivateIpLightForVm] | None = Field(default=None, alias='PrivateIps')
    security_groups: list[SecurityGroupLight] | None = Field(default=None, alias='SecurityGroups')
    state: str | None = Field(default=None, alias='State')
    subnet_id: str | None = Field(default=None, alias='SubnetId')

class OsuApiKey(GeneratedModel):
    api_key_id: str | None = Field(default=None, alias='ApiKeyId')
    secret_key: str | None = Field(default=None, alias='SecretKey')

class OsuExportImageExportTask(GeneratedModel):
    disk_image_format: str = Field(alias='DiskImageFormat')
    osu_bucket: str = Field(alias='OsuBucket')
    osu_manifest_url: str | None = Field(default=None, alias='OsuManifestUrl')
    osu_prefix: str | None = Field(default=None, alias='OsuPrefix')

class OsuExportSnapshotExportTask(GeneratedModel):
    disk_image_format: str = Field(alias='DiskImageFormat')
    osu_bucket: str = Field(alias='OsuBucket')
    osu_prefix: str | None = Field(default=None, alias='OsuPrefix')

class OsuExportToCreate(GeneratedModel):
    disk_image_format: str = Field(alias='DiskImageFormat')
    osu_api_key: OsuApiKey | None = Field(default=None, alias='OsuApiKey')
    osu_bucket: str = Field(alias='OsuBucket')
    osu_manifest_url: str | None = Field(default=None, alias='OsuManifestUrl')
    osu_prefix: str | None = Field(default=None, alias='OsuPrefix')

class PermissionsOnResource(GeneratedModel):
    account_ids: list[str] | None = Field(default=None, alias='AccountIds')
    global_permission: bool | None = Field(default=None, alias='GlobalPermission')

class PermissionsOnResourceCreation(GeneratedModel):
    additions: PermissionsOnResource | None = Field(default=None, alias='Additions')
    removals: PermissionsOnResource | None = Field(default=None, alias='Removals')

class Phase1Options(GeneratedModel):
    dpd_timeout_action: str | None = Field(default=None, alias='DpdTimeoutAction')
    dpd_timeout_seconds: int | None = Field(default=None, alias='DpdTimeoutSeconds')
    ike_versions: list[str] | None = Field(default=None, alias='IkeVersions')
    phase1_dh_group_numbers: list[int] | None = Field(default=None, alias='Phase1DhGroupNumbers')
    phase1_encryption_algorithms: list[str] | None = Field(default=None, alias='Phase1EncryptionAlgorithms')
    phase1_integrity_algorithms: list[str] | None = Field(default=None, alias='Phase1IntegrityAlgorithms')
    phase1_lifetime_seconds: int | None = Field(default=None, alias='Phase1LifetimeSeconds')
    replay_window_size: int | None = Field(default=None, alias='ReplayWindowSize')
    startup_action: str | None = Field(default=None, alias='StartupAction')

class Phase2Options(GeneratedModel):
    phase2_dh_group_numbers: list[int] | None = Field(default=None, alias='Phase2DhGroupNumbers')
    phase2_encryption_algorithms: list[str] | None = Field(default=None, alias='Phase2EncryptionAlgorithms')
    phase2_integrity_algorithms: list[str] | None = Field(default=None, alias='Phase2IntegrityAlgorithms')
    phase2_lifetime_seconds: int | None = Field(default=None, alias='Phase2LifetimeSeconds')
    pre_shared_key: str | None = Field(default=None, alias='PreSharedKey')

class Placement(GeneratedModel):
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    tenancy: str | None = Field(default=None, alias='Tenancy')

class Policy(GeneratedModel):
    creation_date: str | None = Field(default=None, alias='CreationDate')
    description: str | None = Field(default=None, alias='Description')
    is_linkable: bool | None = Field(default=None, alias='IsLinkable')
    last_modification_date: str | None = Field(default=None, alias='LastModificationDate')
    orn: str | None = Field(default=None, alias='Orn')
    path: str | None = Field(default=None, alias='Path')
    policy_default_version_id: str | None = Field(default=None, alias='PolicyDefaultVersionId')
    policy_id: str | None = Field(default=None, alias='PolicyId')
    policy_name: str | None = Field(default=None, alias='PolicyName')
    resources_count: int | None = Field(default=None, alias='ResourcesCount')

class PolicyEntities(GeneratedModel):
    accounts: list[MinimalPolicy] | None = Field(default=None, alias='Accounts')
    groups: list[MinimalPolicy] | None = Field(default=None, alias='Groups')
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    items_count: int | None = Field(default=None, alias='ItemsCount')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    max_results_truncated: bool | None = Field(default=None, alias='MaxResultsTruncated')
    users: list[MinimalPolicy] | None = Field(default=None, alias='Users')

class PolicyVersion(GeneratedModel):
    body: str | None = Field(default=None, alias='Body')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    default_version: bool | None = Field(default=None, alias='DefaultVersion')
    version_id: str | None = Field(default=None, alias='VersionId')

class PrivateIp(GeneratedModel):
    is_primary: bool | None = Field(default=None, alias='IsPrimary')
    link_public_ip: LinkPublicIp | None = Field(default=None, alias='LinkPublicIp')
    private_dns_name: str | None = Field(default=None, alias='PrivateDnsName')
    private_ip: str | None = Field(default=None, alias='PrivateIp')

class PrivateIpLight(GeneratedModel):
    is_primary: bool | None = Field(default=None, alias='IsPrimary')
    private_ip: str | None = Field(default=None, alias='PrivateIp')

class PrivateIpLightForVm(GeneratedModel):
    is_primary: bool | None = Field(default=None, alias='IsPrimary')
    link_public_ip: LinkPublicIpLightForVm | None = Field(default=None, alias='LinkPublicIp')
    private_dns_name: str | None = Field(default=None, alias='PrivateDnsName')
    private_ip: str | None = Field(default=None, alias='PrivateIp')

class ProductType(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    product_type_id: str | None = Field(default=None, alias='ProductTypeId')
    vendor: str | None = Field(default=None, alias='Vendor')

class PublicIp(GeneratedModel):
    link_public_ip_id: str | None = Field(default=None, alias='LinkPublicIpId')
    nic_account_id: str | None = Field(default=None, alias='NicAccountId')
    nic_id: str | None = Field(default=None, alias='NicId')
    private_ip: str | None = Field(default=None, alias='PrivateIp')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    public_ip_id: str | None = Field(default=None, alias='PublicIpId')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vm_id: str | None = Field(default=None, alias='VmId')

class PublicIpLight(GeneratedModel):
    public_ip: str | None = Field(default=None, alias='PublicIp')
    public_ip_id: str | None = Field(default=None, alias='PublicIpId')

class PutUserGroupPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_document: str = Field(alias='PolicyDocument')
    policy_name: str = Field(alias='PolicyName')
    user_group_name: str = Field(alias='UserGroupName')
    user_group_path: str | None = Field(default=None, alias='UserGroupPath')

class PutUserGroupPolicyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class PutUserPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_document: str = Field(alias='PolicyDocument')
    policy_name: str = Field(alias='PolicyName')
    user_name: str = Field(alias='UserName')

class PutUserPolicyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class Quota(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    description: str | None = Field(default=None, alias='Description')
    max_value: int | None = Field(default=None, alias='MaxValue')
    name: str | None = Field(default=None, alias='Name')
    quota_collection: str | None = Field(default=None, alias='QuotaCollection')
    short_description: str | None = Field(default=None, alias='ShortDescription')
    used_value: int | None = Field(default=None, alias='UsedValue')

class QuotaTypes(GeneratedModel):
    quota_type: str | None = Field(default=None, alias='QuotaType')
    quotas: list[Quota] | None = Field(default=None, alias='Quotas')

class ReadAccessKeysRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersAccessKeys | None = Field(default=None, alias='Filters')
    tag: str | None = Field(default=None, alias='Tag')
    user_name: str | None = Field(default=None, alias='UserName')

class ReadAccessKeysResponse(GeneratedModel):
    access_keys: list[AccessKey] | None = Field(default=None, alias='AccessKeys')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadAccountsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class ReadAccountsResponse(GeneratedModel):
    accounts: list[Account] | None = Field(default=None, alias='Accounts')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadAdminPasswordRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_id: str = Field(alias='VmId')

class ReadAdminPasswordResponse(GeneratedModel):
    admin_password: str | None = Field(default=None, alias='AdminPassword')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_id: str | None = Field(default=None, alias='VmId')

class ReadApiAccessPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class ReadApiAccessPolicyResponse(GeneratedModel):
    api_access_policy: ApiAccessPolicy | None = Field(default=None, alias='ApiAccessPolicy')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadApiAccessRulesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersApiAccessRule | None = Field(default=None, alias='Filters')

class ReadApiAccessRulesResponse(GeneratedModel):
    api_access_rules: list[ApiAccessRule] | None = Field(default=None, alias='ApiAccessRules')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadApiLogsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersApiLog | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')
    with_: With | None = Field(default=None, alias='With')

class ReadApiLogsResponse(GeneratedModel):
    logs: list[Log] | None = Field(default=None, alias='Logs')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadCO2EmissionAccountRequest(GeneratedModel):
    from_month: str = Field(alias='FromMonth')
    overall: bool | None = Field(default=None, alias='Overall')
    to_month: str = Field(alias='ToMonth')

class ReadCO2EmissionAccountResponse(GeneratedModel):
    co2_emission_entries: list[CO2EmissionEntry] | None = Field(default=None, alias='CO2EmissionEntries')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    unit: str | None = Field(default=None, alias='Unit')
    value: float | None = Field(default=None, alias='Value')

class ReadCasRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersCa | None = Field(default=None, alias='Filters')

class ReadCasResponse(GeneratedModel):
    cas: list[Ca] | None = Field(default=None, alias='Cas')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadCatalogRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class ReadCatalogResponse(GeneratedModel):
    catalog: Catalog | None = Field(default=None, alias='Catalog')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadCatalogsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersCatalogs | None = Field(default=None, alias='Filters')

class ReadCatalogsResponse(GeneratedModel):
    catalogs: list[Catalogs] | None = Field(default=None, alias='Catalogs')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadClientGatewaysRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersClientGateway | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadClientGatewaysResponse(GeneratedModel):
    client_gateways: list[ClientGateway] | None = Field(default=None, alias='ClientGateways')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadConsoleOutputRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_id: str = Field(alias='VmId')

class ReadConsoleOutputResponse(GeneratedModel):
    console_output: str | None = Field(default=None, alias='ConsoleOutput')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_id: str | None = Field(default=None, alias='VmId')

class ReadConsumptionAccountRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    from_date: str = Field(alias='FromDate')
    overall: bool | None = Field(default=None, alias='Overall')
    show_price: bool | None = Field(default=None, alias='ShowPrice')
    show_resource_details: bool | None = Field(default=None, alias='ShowResourceDetails')
    to_date: str = Field(alias='ToDate')

class ReadConsumptionAccountResponse(GeneratedModel):
    consumption_entries: list[ConsumptionEntry] | None = Field(default=None, alias='ConsumptionEntries')
    currency: str | None = Field(default=None, alias='Currency')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadDedicatedGroupsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersDedicatedGroup | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadDedicatedGroupsResponse(GeneratedModel):
    dedicated_groups: list[DedicatedGroup] | None = Field(default=None, alias='DedicatedGroups')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadDhcpOptionsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersDhcpOptions | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadDhcpOptionsResponse(GeneratedModel):
    dhcp_options_sets: list[DhcpOptionsSet] | None = Field(default=None, alias='DhcpOptionsSets')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadDirectLinkInterfacesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersDirectLinkInterface | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadDirectLinkInterfacesResponse(GeneratedModel):
    direct_link_interfaces: list[DirectLinkInterfaces] | None = Field(default=None, alias='DirectLinkInterfaces')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadDirectLinksRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersDirectLink | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadDirectLinksResponse(GeneratedModel):
    direct_links: list[DirectLink] | None = Field(default=None, alias='DirectLinks')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadEntitiesLinkedToPolicyRequest(GeneratedModel):
    entities_type: list[Literal['ACCOUNT', 'USER', 'GROUP']] | None = Field(default=None, alias='EntitiesType')
    first_item: int | None = Field(default=None, alias='FirstItem')
    policy_orn: str = Field(alias='PolicyOrn')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadEntitiesLinkedToPolicyResponse(GeneratedModel):
    policy_entities: PolicyEntities | None = Field(default=None, alias='PolicyEntities')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadFlexibleGpuCatalogRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class ReadFlexibleGpuCatalogResponse(GeneratedModel):
    flexible_gpu_catalog: list[FlexibleGpuCatalog] | None = Field(default=None, alias='FlexibleGpuCatalog')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadFlexibleGpusRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersFlexibleGpu | None = Field(default=None, alias='Filters')

class ReadFlexibleGpusResponse(GeneratedModel):
    flexible_gpus: list[FlexibleGpu] | None = Field(default=None, alias='FlexibleGpus')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadImageExportTasksRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersReadImageExportTask | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadImageExportTasksResponse(GeneratedModel):
    image_export_tasks: list[ImageExportTask] | None = Field(default=None, alias='ImageExportTasks')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadImagesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersImage | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadImagesResponse(GeneratedModel):
    images: list[Image] | None = Field(default=None, alias='Images')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadInternetServicesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersInternetService | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadInternetServicesResponse(GeneratedModel):
    internet_services: list[InternetService] | None = Field(default=None, alias='InternetServices')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadKeypairsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersKeypair | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadKeypairsResponse(GeneratedModel):
    keypairs: list[Keypair] | None = Field(default=None, alias='Keypairs')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadLinkedPoliciesFilters(GeneratedModel):
    path_prefix: str | None = Field(default=None, alias='PathPrefix')

class ReadLinkedPoliciesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: ReadLinkedPoliciesFilters | None = Field(default=None, alias='Filters')
    first_item: int | None = Field(default=None, alias='FirstItem')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')
    user_name: str = Field(alias='UserName')

class ReadLinkedPoliciesResponse(GeneratedModel):
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    max_results_truncated: bool | None = Field(default=None, alias='MaxResultsTruncated')
    policies: list[LinkedPolicy] | None = Field(default=None, alias='Policies')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadListenerRulesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersListenerRule | None = Field(default=None, alias='Filters')

class ReadListenerRulesResponse(GeneratedModel):
    listener_rules: list[ListenerRule] | None = Field(default=None, alias='ListenerRules')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadLoadBalancerTagsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_names: list[str] = Field(alias='LoadBalancerNames')

class ReadLoadBalancerTagsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    tags: list[LoadBalancerTag] | None = Field(default=None, alias='Tags')

class ReadLoadBalancersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersLoadBalancer | None = Field(default=None, alias='Filters')

class ReadLoadBalancersResponse(GeneratedModel):
    load_balancers: list[LoadBalancer] | None = Field(default=None, alias='LoadBalancers')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadLocationsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadLocationsResponse(GeneratedModel):
    locations: list[Location] | None = Field(default=None, alias='Locations')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadManagedPoliciesLinkedToUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersUserGroup | None = Field(default=None, alias='Filters')
    first_item: int | None = Field(default=None, alias='FirstItem')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')
    user_group_name: str = Field(alias='UserGroupName')

class ReadManagedPoliciesLinkedToUserGroupResponse(GeneratedModel):
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    max_results_truncated: bool | None = Field(default=None, alias='MaxResultsTruncated')
    policies: list[LinkedPolicy] | None = Field(default=None, alias='Policies')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadNatServicesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersNatService | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadNatServicesResponse(GeneratedModel):
    nat_services: list[NatService] | None = Field(default=None, alias='NatServices')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadNetAccessPointServicesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersService | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadNetAccessPointServicesResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    services: list[Service] | None = Field(default=None, alias='Services')

class ReadNetAccessPointsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersNetAccessPoint | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadNetAccessPointsResponse(GeneratedModel):
    net_access_points: list[NetAccessPoint] | None = Field(default=None, alias='NetAccessPoints')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadNetPeeringsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersNetPeering | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadNetPeeringsResponse(GeneratedModel):
    net_peerings: list[NetPeering] | None = Field(default=None, alias='NetPeerings')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadNetsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersNet | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadNetsResponse(GeneratedModel):
    nets: list[Net] | None = Field(default=None, alias='Nets')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadNicsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersNic | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadNicsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    nics: list[Nic] | None = Field(default=None, alias='Nics')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadPoliciesFilters(GeneratedModel):
    only_linked: bool | None = Field(default=None, alias='OnlyLinked')
    path_prefix: str | None = Field(default=None, alias='PathPrefix')
    scope: Literal['LOCAL', 'OWS'] | None = Field(default=None, alias='Scope')

class ReadPoliciesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: ReadPoliciesFilters | None = Field(default=None, alias='Filters')
    first_item: int | None = Field(default=None, alias='FirstItem')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadPoliciesResponse(GeneratedModel):
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    max_results_truncated: bool | None = Field(default=None, alias='MaxResultsTruncated')
    policies: list[Policy] | None = Field(default=None, alias='Policies')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadPolicyRequest(GeneratedModel):
    policy_orn: str = Field(alias='PolicyOrn')

class ReadPolicyResponse(GeneratedModel):
    policy: Policy | None = Field(default=None, alias='Policy')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadPolicyVersionRequest(GeneratedModel):
    policy_orn: str = Field(alias='PolicyOrn')
    version_id: str = Field(alias='VersionId')

class ReadPolicyVersionResponse(GeneratedModel):
    policy_version: PolicyVersion | None = Field(default=None, alias='PolicyVersion')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadPolicyVersionsRequest(GeneratedModel):
    first_item: int | None = Field(default=None, alias='FirstItem')
    policy_orn: str = Field(alias='PolicyOrn')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadPolicyVersionsResponse(GeneratedModel):
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    policy_versions: list[PolicyVersion] | None = Field(default=None, alias='PolicyVersions')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadProductTypesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersProductType | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadProductTypesResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    product_types: list[ProductType] | None = Field(default=None, alias='ProductTypes')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadPublicCatalogRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class ReadPublicCatalogResponse(GeneratedModel):
    catalog: Catalog | None = Field(default=None, alias='Catalog')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadPublicIpRangesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadPublicIpRangesResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    public_ips: list[str] | None = Field(default=None, alias='PublicIps')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadPublicIpsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersPublicIp | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadPublicIpsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    public_ips: list[PublicIp] | None = Field(default=None, alias='PublicIps')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadQuotasRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersQuota | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadQuotasResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    quota_types: list[QuotaTypes] | None = Field(default=None, alias='QuotaTypes')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadRegionsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')

class ReadRegionsResponse(GeneratedModel):
    regions: list[Region] | None = Field(default=None, alias='Regions')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadRouteTablesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersRouteTable | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadRouteTablesResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    route_tables: list[RouteTable] | None = Field(default=None, alias='RouteTables')

class ReadSecurityGroupsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersSecurityGroup | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadSecurityGroupsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    security_groups: list[SecurityGroup] | None = Field(default=None, alias='SecurityGroups')

class ReadServerCertificatesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersServerCertificate | None = Field(default=None, alias='Filters')

class ReadServerCertificatesResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    server_certificates: list[ServerCertificate] | None = Field(default=None, alias='ServerCertificates')

class ReadSnapshotExportTasksRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersSnapshotExportTask | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadSnapshotExportTasksResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    snapshot_export_tasks: list[SnapshotExportTask] | None = Field(default=None, alias='SnapshotExportTasks')

class ReadSnapshotsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersSnapshot | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadSnapshotsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    snapshots: list[Snapshot] | None = Field(default=None, alias='Snapshots')

class ReadSubnetsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersSubnet | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadSubnetsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    subnets: list[Subnet] | None = Field(default=None, alias='Subnets')

class ReadSubregionsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersSubregion | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadSubregionsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    subregions: list[Subregion] | None = Field(default=None, alias='Subregions')

class ReadTagsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersTag | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadTagsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    tags: list[Tag] | None = Field(default=None, alias='Tags')

class ReadUnitPriceRequest(GeneratedModel):
    operation: str = Field(alias='Operation')
    service: str = Field(alias='Service')
    type: str = Field(alias='Type')

class ReadUnitPriceResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    unit_price_entry: UnitPriceEntry | None = Field(default=None, alias='UnitPriceEntry')

class ReadUserGroupPoliciesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    first_item: int | None = Field(default=None, alias='FirstItem')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')
    user_group_name: str = Field(alias='UserGroupName')
    user_group_path: str | None = Field(default=None, alias='UserGroupPath')

class ReadUserGroupPoliciesResponse(GeneratedModel):
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    max_results_truncated: bool | None = Field(default=None, alias='MaxResultsTruncated')
    policies: list[InlinePolicy] | None = Field(default=None, alias='Policies')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadUserGroupPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_name: str = Field(alias='PolicyName')
    user_group_name: str = Field(alias='UserGroupName')
    user_group_path: str | None = Field(default=None, alias='UserGroupPath')

class ReadUserGroupPolicyResponse(GeneratedModel):
    policy: InlinePolicy | None = Field(default=None, alias='Policy')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    path: str | None = Field(default=None, alias='Path')
    user_group_name: str = Field(alias='UserGroupName')

class ReadUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user_group: UserGroup | None = Field(default=None, alias='UserGroup')
    users: list[User] | None = Field(default=None, alias='Users')

class ReadUserGroupsPerUserRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_name: str = Field(alias='UserName')
    user_path: str | None = Field(default=None, alias='UserPath')

class ReadUserGroupsPerUserResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user_groups: list[UserGroup] | None = Field(default=None, alias='UserGroups')

class ReadUserGroupsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersUserGroup | None = Field(default=None, alias='Filters')
    first_item: int | None = Field(default=None, alias='FirstItem')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadUserGroupsResponse(GeneratedModel):
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    max_results_truncated: bool | None = Field(default=None, alias='MaxResultsTruncated')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user_groups: list[UserGroup] | None = Field(default=None, alias='UserGroups')

class ReadUserPoliciesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_name: str = Field(alias='UserName')

class ReadUserPoliciesResponse(GeneratedModel):
    policy_names: list[str] | None = Field(default=None, alias='PolicyNames')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadUserPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_name: str = Field(alias='PolicyName')
    user_name: str = Field(alias='UserName')

class ReadUserPolicyResponse(GeneratedModel):
    policy_document: str | None = Field(default=None, alias='PolicyDocument')
    policy_name: str | None = Field(default=None, alias='PolicyName')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user_name: str | None = Field(default=None, alias='UserName')

class ReadUsersRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersUsers | None = Field(default=None, alias='Filters')
    first_item: int | None = Field(default=None, alias='FirstItem')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadUsersResponse(GeneratedModel):
    has_more_items: bool | None = Field(default=None, alias='HasMoreItems')
    max_results_limit: int | None = Field(default=None, alias='MaxResultsLimit')
    max_results_truncated: bool | None = Field(default=None, alias='MaxResultsTruncated')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    users: list[User] | None = Field(default=None, alias='Users')

class ReadVirtualGatewaysRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVirtualGateway | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadVirtualGatewaysResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    virtual_gateways: list[VirtualGateway] | None = Field(default=None, alias='VirtualGateways')

class ReadVmGroupsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVmGroup | None = Field(default=None, alias='Filters')

class ReadVmGroupsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_groups: list[VmGroup] | None = Field(default=None, alias='VmGroups')

class ReadVmTemplatesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVmTemplate | None = Field(default=None, alias='Filters')

class ReadVmTemplatesResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_templates: list[VmTemplate] | None = Field(default=None, alias='VmTemplates')

class ReadVmTypesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVmType | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadVmTypesResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_types: list[VmType] | None = Field(default=None, alias='VmTypes')

class ReadVmsHealthRequest(GeneratedModel):
    backend_vm_ids: list[str] | None = Field(default=None, alias='BackendVmIds')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')

class ReadVmsHealthResponse(GeneratedModel):
    backend_vm_health: list[BackendVmHealth] | None = Field(default=None, alias='BackendVmHealth')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ReadVmsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVm | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadVmsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vms: list[Vm] | None = Field(default=None, alias='Vms')

class ReadVmsStateRequest(GeneratedModel):
    all_vms: bool | None = Field(default=None, alias='AllVms')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVmsState | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadVmsStateResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_states: list[VmStates] | None = Field(default=None, alias='VmStates')

class ReadVolumeUpdateTasksRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersReadVolumeUpdateTask | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadVolumeUpdateTasksResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    volume_update_tasks: list[VolumeUpdateTask] | None = Field(default=None, alias='VolumeUpdateTasks')

class ReadVolumesRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVolume | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadVolumesResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    volumes: list[Volume] | None = Field(default=None, alias='Volumes')

class ReadVpnConnectionsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    filters: FiltersVpnConnection | None = Field(default=None, alias='Filters')
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    results_per_page: int | None = Field(default=None, alias='ResultsPerPage')

class ReadVpnConnectionsResponse(GeneratedModel):
    next_page_token: str | None = Field(default=None, alias='NextPageToken')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vpn_connections: list[VpnConnection] | None = Field(default=None, alias='VpnConnections')

class RebootVmsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_ids: list[str] = Field(alias='VmIds')

class RebootVmsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class Region(GeneratedModel):
    endpoint: str | None = Field(default=None, alias='Endpoint')
    region_name: str | None = Field(default=None, alias='RegionName')

class RegisterVmsInLoadBalancerRequest(GeneratedModel):
    backend_vm_ids: list[str] = Field(alias='BackendVmIds')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')

class RegisterVmsInLoadBalancerResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class RejectNetPeeringRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_peering_id: str = Field(alias='NetPeeringId')

class RejectNetPeeringResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class RemoveUserFromUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    user_group_name: str = Field(alias='UserGroupName')
    user_group_path: str | None = Field(default=None, alias='UserGroupPath')
    user_name: str = Field(alias='UserName')
    user_path: str | None = Field(default=None, alias='UserPath')

class RemoveUserFromUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ResourceLoadBalancerTag(GeneratedModel):
    key: str = Field(alias='Key')

class ResourceTag(GeneratedModel):
    key: str = Field(alias='Key')
    value: str = Field(alias='Value')

class ResponseContext(GeneratedModel):
    request_id: str | None = Field(default=None, alias='RequestId')

class Route(GeneratedModel):
    creation_method: str | None = Field(default=None, alias='CreationMethod')
    destination_ip_range: str | None = Field(default=None, alias='DestinationIpRange')
    destination_service_id: str | None = Field(default=None, alias='DestinationServiceId')
    gateway_id: str | None = Field(default=None, alias='GatewayId')
    nat_service_id: str | None = Field(default=None, alias='NatServiceId')
    net_access_point_id: str | None = Field(default=None, alias='NetAccessPointId')
    net_peering_id: str | None = Field(default=None, alias='NetPeeringId')
    nic_id: str | None = Field(default=None, alias='NicId')
    state: str | None = Field(default=None, alias='State')
    vm_account_id: str | None = Field(default=None, alias='VmAccountId')
    vm_id: str | None = Field(default=None, alias='VmId')

class RouteLight(GeneratedModel):
    destination_ip_range: str | None = Field(default=None, alias='DestinationIpRange')
    route_type: str | None = Field(default=None, alias='RouteType')
    state: str | None = Field(default=None, alias='State')

class RoutePropagatingVirtualGateway(GeneratedModel):
    virtual_gateway_id: str | None = Field(default=None, alias='VirtualGatewayId')

class RouteTable(GeneratedModel):
    link_route_tables: list[LinkRouteTable] | None = Field(default=None, alias='LinkRouteTables')
    net_id: str | None = Field(default=None, alias='NetId')
    route_propagating_virtual_gateways: list[RoutePropagatingVirtualGateway] | None = Field(default=None, alias='RoutePropagatingVirtualGateways')
    route_table_id: str | None = Field(default=None, alias='RouteTableId')
    routes: list[Route] | None = Field(default=None, alias='Routes')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class ScaleDownVmGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_group_id: str = Field(alias='VmGroupId')
    vm_subtraction: int = Field(alias='VmSubtraction')

class ScaleDownVmGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class ScaleUpVmGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_addition: int = Field(alias='VmAddition')
    vm_group_id: str = Field(alias='VmGroupId')

class ScaleUpVmGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

SecureBootAction = Literal['enable', 'disable', 'setup-mode', 'none', 'restore-factory-keys']

class SecurityGroup(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    description: str | None = Field(default=None, alias='Description')
    inbound_rules: list[SecurityGroupRule] | None = Field(default=None, alias='InboundRules')
    net_id: str | None = Field(default=None, alias='NetId')
    outbound_rules: list[SecurityGroupRule] | None = Field(default=None, alias='OutboundRules')
    security_group_id: str | None = Field(default=None, alias='SecurityGroupId')
    security_group_name: str | None = Field(default=None, alias='SecurityGroupName')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class SecurityGroupLight(GeneratedModel):
    security_group_id: str | None = Field(default=None, alias='SecurityGroupId')
    security_group_name: str | None = Field(default=None, alias='SecurityGroupName')

class SecurityGroupRule(GeneratedModel):
    from_port_range: int | None = Field(default=None, alias='FromPortRange')
    ip_protocol: str | None = Field(default=None, alias='IpProtocol')
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')
    security_group_rule_id: str | None = Field(default=None, alias='SecurityGroupRuleId')
    security_groups_members: list[SecurityGroupsMember] | None = Field(default=None, alias='SecurityGroupsMembers')
    service_ids: list[str] | None = Field(default=None, alias='ServiceIds')
    to_port_range: int | None = Field(default=None, alias='ToPortRange')

class SecurityGroupsMember(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    security_group_id: str | None = Field(default=None, alias='SecurityGroupId')
    security_group_name: str | None = Field(default=None, alias='SecurityGroupName')

class ServerCertificate(GeneratedModel):
    expiration_date: str | None = Field(default=None, alias='ExpirationDate')
    id: str | None = Field(default=None, alias='Id')
    name: str | None = Field(default=None, alias='Name')
    orn: str | None = Field(default=None, alias='Orn')
    path: str | None = Field(default=None, alias='Path')
    upload_date: str | None = Field(default=None, alias='UploadDate')

class Service(GeneratedModel):
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')
    service_id: str | None = Field(default=None, alias='ServiceId')
    service_name: str | None = Field(default=None, alias='ServiceName')

class SetDefaultPolicyVersionRequest(GeneratedModel):
    policy_orn: str = Field(alias='PolicyOrn')
    version_id: str = Field(alias='VersionId')

class SetDefaultPolicyVersionResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class Snapshot(GeneratedModel):
    account_alias: str | None = Field(default=None, alias='AccountAlias')
    account_id: str | None = Field(default=None, alias='AccountId')
    client_token: str | None = Field(default=None, alias='ClientToken')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    description: str | None = Field(default=None, alias='Description')
    permissions_to_create_volume: PermissionsOnResource | None = Field(default=None, alias='PermissionsToCreateVolume')
    progress: int | None = Field(default=None, alias='Progress')
    snapshot_id: str | None = Field(default=None, alias='SnapshotId')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    volume_id: str | None = Field(default=None, alias='VolumeId')
    volume_size: int | None = Field(default=None, alias='VolumeSize')

class SnapshotExportTask(GeneratedModel):
    comment: str | None = Field(default=None, alias='Comment')
    osu_export: OsuExportSnapshotExportTask | None = Field(default=None, alias='OsuExport')
    progress: int | None = Field(default=None, alias='Progress')
    snapshot_id: str | None = Field(default=None, alias='SnapshotId')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    task_id: str | None = Field(default=None, alias='TaskId')

class SourceNet(GeneratedModel):
    account_id: str | None = Field(default=None, alias='AccountId')
    ip_range: str | None = Field(default=None, alias='IpRange')
    net_id: str | None = Field(default=None, alias='NetId')

class SourceSecurityGroup(GeneratedModel):
    security_group_account_id: str | None = Field(default=None, alias='SecurityGroupAccountId')
    security_group_name: str | None = Field(default=None, alias='SecurityGroupName')

class StartVmsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    vm_ids: list[str] = Field(alias='VmIds')

class StartVmsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vms: list[VmState] | None = Field(default=None, alias='Vms')

class StateComment(GeneratedModel):
    state_code: str | None = Field(default=None, alias='StateCode')
    state_message: str | None = Field(default=None, alias='StateMessage')

class StopVmsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    force_stop: bool | None = Field(default=None, alias='ForceStop')
    vm_ids: list[str] = Field(alias='VmIds')

class StopVmsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vms: list[VmState] | None = Field(default=None, alias='Vms')

class Subnet(GeneratedModel):
    available_ips_count: int | None = Field(default=None, alias='AvailableIpsCount')
    ip_range: str | None = Field(default=None, alias='IpRange')
    map_public_ip_on_launch: bool | None = Field(default=None, alias='MapPublicIpOnLaunch')
    net_id: str | None = Field(default=None, alias='NetId')
    state: str | None = Field(default=None, alias='State')
    subnet_id: str | None = Field(default=None, alias='SubnetId')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')

class Subregion(GeneratedModel):
    location_code: str | None = Field(default=None, alias='LocationCode')
    region_name: str | None = Field(default=None, alias='RegionName')
    state: str | None = Field(default=None, alias='State')
    subregion_name: str | None = Field(default=None, alias='SubregionName')

class Tag(GeneratedModel):
    key: str | None = Field(default=None, alias='Key')
    resource_id: str | None = Field(default=None, alias='ResourceId')
    resource_type: str | None = Field(default=None, alias='ResourceType')
    value: str | None = Field(default=None, alias='Value')

class UnitPriceEntry(GeneratedModel):
    currency: str | None = Field(default=None, alias='Currency')
    operation: str | None = Field(default=None, alias='Operation')
    service: str | None = Field(default=None, alias='Service')
    type: str | None = Field(default=None, alias='Type')
    unit: str | None = Field(default=None, alias='Unit')
    unit_price: float | None = Field(default=None, alias='UnitPrice')

class UnlinkFlexibleGpuRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    flexible_gpu_id: str = Field(alias='FlexibleGpuId')

class UnlinkFlexibleGpuResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkInternetServiceRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    internet_service_id: str = Field(alias='InternetServiceId')
    net_id: str = Field(alias='NetId')

class UnlinkInternetServiceResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkLoadBalancerBackendMachinesRequest(GeneratedModel):
    backend_ips: list[str] | None = Field(default=None, alias='BackendIps')
    backend_vm_ids: list[str] | None = Field(default=None, alias='BackendVmIds')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    load_balancer_name: str = Field(alias='LoadBalancerName')

class UnlinkLoadBalancerBackendMachinesResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkManagedPolicyFromUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_orn: str = Field(alias='PolicyOrn')
    user_group_name: str = Field(alias='UserGroupName')

class UnlinkManagedPolicyFromUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkNicRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    link_nic_id: str = Field(alias='LinkNicId')

class UnlinkNicResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    policy_orn: str = Field(alias='PolicyOrn')
    user_name: str = Field(alias='UserName')

class UnlinkPolicyResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkPrivateIpsRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    nic_id: str = Field(alias='NicId')
    private_ips: list[str] = Field(alias='PrivateIps')

class UnlinkPrivateIpsResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkPublicIpRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    link_public_ip_id: str | None = Field(default=None, alias='LinkPublicIpId')
    public_ip: str | None = Field(default=None, alias='PublicIp')

class UnlinkPublicIpResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkRouteTableRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    link_route_table_id: str = Field(alias='LinkRouteTableId')

class UnlinkRouteTableResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkVirtualGatewayRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_id: str = Field(alias='NetId')
    virtual_gateway_id: str = Field(alias='VirtualGatewayId')

class UnlinkVirtualGatewayResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UnlinkVolumeRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    force_unlink: bool | None = Field(default=None, alias='ForceUnlink')
    volume_id: str = Field(alias='VolumeId')

class UnlinkVolumeResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateAccessKeyRequest(GeneratedModel):
    access_key_id: str = Field(alias='AccessKeyId')
    clear_expiration_date: bool | None = Field(default=None, alias='ClearExpirationDate')
    clear_tag: bool | None = Field(default=None, alias='ClearTag')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    expiration_date: str | None = Field(default=None, alias='ExpirationDate')
    state: str | None = Field(default=None, alias='State')
    tag: str | None = Field(default=None, alias='Tag')
    user_name: str | None = Field(default=None, alias='UserName')

class UpdateAccessKeyResponse(GeneratedModel):
    access_key: AccessKey | None = Field(default=None, alias='AccessKey')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateAccountRequest(GeneratedModel):
    additional_emails: list[str] | None = Field(default=None, alias='AdditionalEmails')
    city: str | None = Field(default=None, alias='City')
    company_name: str | None = Field(default=None, alias='CompanyName')
    country: str | None = Field(default=None, alias='Country')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    email: str | None = Field(default=None, alias='Email')
    first_name: str | None = Field(default=None, alias='FirstName')
    job_title: str | None = Field(default=None, alias='JobTitle')
    last_name: str | None = Field(default=None, alias='LastName')
    mobile_number: str | None = Field(default=None, alias='MobileNumber')
    phone_number: str | None = Field(default=None, alias='PhoneNumber')
    state_province: str | None = Field(default=None, alias='StateProvince')
    vat_number: str | None = Field(default=None, alias='VatNumber')
    zip_code: str | None = Field(default=None, alias='ZipCode')

class UpdateAccountResponse(GeneratedModel):
    account: Account | None = Field(default=None, alias='Account')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateApiAccessPolicyRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    max_access_key_expiration_seconds: int = Field(alias='MaxAccessKeyExpirationSeconds')
    require_trusted_env: bool = Field(alias='RequireTrustedEnv')

class UpdateApiAccessPolicyResponse(GeneratedModel):
    api_access_policy: ApiAccessPolicy | None = Field(default=None, alias='ApiAccessPolicy')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateApiAccessRuleRequest(GeneratedModel):
    api_access_rule_id: str = Field(alias='ApiAccessRuleId')
    ca_ids: list[str] | None = Field(default=None, alias='CaIds')
    cns: list[str] | None = Field(default=None, alias='Cns')
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    ip_ranges: list[str] | None = Field(default=None, alias='IpRanges')

class UpdateApiAccessRuleResponse(GeneratedModel):
    api_access_rule: ApiAccessRule | None = Field(default=None, alias='ApiAccessRule')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateCaRequest(GeneratedModel):
    ca_id: str = Field(alias='CaId')
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')

class UpdateCaResponse(GeneratedModel):
    ca: Ca | None = Field(default=None, alias='Ca')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateDedicatedGroupRequest(GeneratedModel):
    dedicated_group_id: str = Field(alias='DedicatedGroupId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    name: str = Field(alias='Name')

class UpdateDedicatedGroupResponse(GeneratedModel):
    dedicated_group: DedicatedGroup | None = Field(default=None, alias='DedicatedGroup')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateDirectLinkInterfaceRequest(GeneratedModel):
    direct_link_interface_id: str = Field(alias='DirectLinkInterfaceId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    mtu: Literal[1500] = Field(alias='Mtu')

class UpdateDirectLinkInterfaceResponse(GeneratedModel):
    direct_link_interface: DirectLinkInterfaces | None = Field(default=None, alias='DirectLinkInterface')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateFlexibleGpuRequest(GeneratedModel):
    delete_on_vm_deletion: bool | None = Field(default=None, alias='DeleteOnVmDeletion')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    flexible_gpu_id: str = Field(alias='FlexibleGpuId')

class UpdateFlexibleGpuResponse(GeneratedModel):
    flexible_gpu: FlexibleGpu | None = Field(default=None, alias='FlexibleGpu')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateImageRequest(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    image_id: str = Field(alias='ImageId')
    permissions_to_launch: PermissionsOnResourceCreation | None = Field(default=None, alias='PermissionsToLaunch')
    product_codes: list[str] | None = Field(default=None, alias='ProductCodes')

class UpdateImageResponse(GeneratedModel):
    image: Image | None = Field(default=None, alias='Image')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateListenerRuleRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    host_pattern: str | None = Field(default=None, alias='HostPattern')
    listener_rule_name: str = Field(alias='ListenerRuleName')
    path_pattern: str | None = Field(default=None, alias='PathPattern')

class UpdateListenerRuleResponse(GeneratedModel):
    listener_rule: ListenerRule | None = Field(default=None, alias='ListenerRule')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateLoadBalancerRequest(GeneratedModel):
    access_log: AccessLog | None = Field(default=None, alias='AccessLog')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    health_check: HealthCheck | None = Field(default=None, alias='HealthCheck')
    load_balancer_name: str = Field(alias='LoadBalancerName')
    load_balancer_port: int | None = Field(default=None, alias='LoadBalancerPort')
    policy_names: list[str] | None = Field(default=None, alias='PolicyNames')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    secured_cookies: bool | None = Field(default=None, alias='SecuredCookies')
    security_groups: list[str] | None = Field(default=None, alias='SecurityGroups')
    server_certificate_id: str | None = Field(default=None, alias='ServerCertificateId')

class UpdateLoadBalancerResponse(GeneratedModel):
    load_balancer: LoadBalancer | None = Field(default=None, alias='LoadBalancer')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateNetAccessPointRequest(GeneratedModel):
    add_route_table_ids: list[str] | None = Field(default=None, alias='AddRouteTableIds')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_access_point_id: str = Field(alias='NetAccessPointId')
    remove_route_table_ids: list[str] | None = Field(default=None, alias='RemoveRouteTableIds')

class UpdateNetAccessPointResponse(GeneratedModel):
    net_access_point: NetAccessPoint | None = Field(default=None, alias='NetAccessPoint')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateNetRequest(GeneratedModel):
    dhcp_options_set_id: str = Field(alias='DhcpOptionsSetId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    net_id: str = Field(alias='NetId')

class UpdateNetResponse(GeneratedModel):
    net: Net | None = Field(default=None, alias='Net')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateNicRequest(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    link_nic: LinkNicToUpdate | None = Field(default=None, alias='LinkNic')
    nic_id: str = Field(alias='NicId')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')

class UpdateNicResponse(GeneratedModel):
    nic: Nic | None = Field(default=None, alias='Nic')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateRoutePropagationRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    enable: bool = Field(alias='Enable')
    route_table_id: str = Field(alias='RouteTableId')
    virtual_gateway_id: str = Field(alias='VirtualGatewayId')

class UpdateRoutePropagationResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    route_table: RouteTable | None = Field(default=None, alias='RouteTable')

class UpdateRouteRequest(GeneratedModel):
    destination_ip_range: str = Field(alias='DestinationIpRange')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    gateway_id: str | None = Field(default=None, alias='GatewayId')
    nat_service_id: str | None = Field(default=None, alias='NatServiceId')
    net_peering_id: str | None = Field(default=None, alias='NetPeeringId')
    nic_id: str | None = Field(default=None, alias='NicId')
    route_table_id: str = Field(alias='RouteTableId')
    vm_id: str | None = Field(default=None, alias='VmId')

class UpdateRouteResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    route_table: RouteTable | None = Field(default=None, alias='RouteTable')

class UpdateRouteTableLinkRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    link_route_table_id: str = Field(alias='LinkRouteTableId')
    route_table_id: str = Field(alias='RouteTableId')

class UpdateRouteTableLinkResponse(GeneratedModel):
    link_route_table_id: str | None = Field(default=None, alias='LinkRouteTableId')
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')

class UpdateServerCertificateRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    name: str = Field(alias='Name')
    new_name: str | None = Field(default=None, alias='NewName')
    new_path: str | None = Field(default=None, alias='NewPath')

class UpdateServerCertificateResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    server_certificate: ServerCertificate | None = Field(default=None, alias='ServerCertificate')

class UpdateSnapshotRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    permissions_to_create_volume: PermissionsOnResourceCreation = Field(alias='PermissionsToCreateVolume')
    snapshot_id: str = Field(alias='SnapshotId')

class UpdateSnapshotResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    snapshot: Snapshot | None = Field(default=None, alias='Snapshot')

class UpdateSubnetRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    map_public_ip_on_launch: bool = Field(alias='MapPublicIpOnLaunch')
    subnet_id: str = Field(alias='SubnetId')

class UpdateSubnetResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    subnet: Subnet | None = Field(default=None, alias='Subnet')

class UpdateUserGroupRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    new_path: str | None = Field(default=None, alias='NewPath')
    new_user_group_name: str | None = Field(default=None, alias='NewUserGroupName')
    path: str | None = Field(default=None, alias='Path')
    user_group_name: str = Field(alias='UserGroupName')

class UpdateUserGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user_group: UserGroup | None = Field(default=None, alias='UserGroup')
    users: list[User] | None = Field(default=None, alias='Users')

class UpdateUserRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    new_path: str | None = Field(default=None, alias='NewPath')
    new_user_email: str | None = Field(default=None, alias='NewUserEmail')
    new_user_name: str | None = Field(default=None, alias='NewUserName')
    user_name: str = Field(alias='UserName')

class UpdateUserResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    user: User | None = Field(default=None, alias='User')

class UpdateVmGroupRequest(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vm_group_id: str = Field(alias='VmGroupId')
    vm_group_name: str | None = Field(default=None, alias='VmGroupName')
    vm_template_id: str | None = Field(default=None, alias='VmTemplateId')

class UpdateVmGroupResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_group: VmGroup | None = Field(default=None, alias='VmGroup')

class UpdateVmRequest(GeneratedModel):
    actions_on_next_boot: ActionsOnNextBoot | None = Field(default=None, alias='ActionsOnNextBoot')
    block_device_mappings: list[BlockDeviceMappingVmUpdate] | None = Field(default=None, alias='BlockDeviceMappings')
    bsu_optimized: bool | None = Field(default=None, alias='BsuOptimized')
    deletion_protection: bool | None = Field(default=None, alias='DeletionProtection')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    is_source_dest_checked: bool | None = Field(default=None, alias='IsSourceDestChecked')
    keypair_name: str | None = Field(default=None, alias='KeypairName')
    nested_virtualization: bool | None = Field(default=None, alias='NestedVirtualization')
    performance: Literal['medium', 'high', 'highest'] | None = Field(default=None, alias='Performance')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    user_data: str | None = Field(default=None, alias='UserData')
    vm_id: str = Field(alias='VmId')
    vm_initiated_shutdown_behavior: str | None = Field(default=None, alias='VmInitiatedShutdownBehavior')
    vm_type: str | None = Field(default=None, alias='VmType')

class UpdateVmResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm: Vm | None = Field(default=None, alias='Vm')

class UpdateVmTemplateRequest(GeneratedModel):
    description: str | None = Field(default=None, alias='Description')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vm_template_id: str = Field(alias='VmTemplateId')
    vm_template_name: str | None = Field(default=None, alias='VmTemplateName')

class UpdateVmTemplateResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vm_template: VmTemplate | None = Field(default=None, alias='VmTemplate')

class UpdateVolumeRequest(GeneratedModel):
    dry_run: bool | None = Field(default=None, alias='DryRun')
    iops: int | None = Field(default=None, alias='Iops')
    size: int | None = Field(default=None, alias='Size')
    volume_id: str = Field(alias='VolumeId')
    volume_type: str | None = Field(default=None, alias='VolumeType')

class UpdateVolumeResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    volume: Volume | None = Field(default=None, alias='Volume')

class UpdateVpnConnectionRequest(GeneratedModel):
    client_gateway_id: str | None = Field(default=None, alias='ClientGatewayId')
    dry_run: bool | None = Field(default=None, alias='DryRun')
    virtual_gateway_id: str | None = Field(default=None, alias='VirtualGatewayId')
    vpn_connection_id: str = Field(alias='VpnConnectionId')
    vpn_options: VpnOptions | None = Field(default=None, alias='VpnOptions')

class UpdateVpnConnectionResponse(GeneratedModel):
    response_context: ResponseContext | None = Field(default=None, alias='ResponseContext')
    vpn_connection: VpnConnection | None = Field(default=None, alias='VpnConnection')

class User(GeneratedModel):
    creation_date: str | None = Field(default=None, alias='CreationDate')
    last_modification_date: str | None = Field(default=None, alias='LastModificationDate')
    outscale_login_allowed: bool | None = Field(default=None, alias='OutscaleLoginAllowed')
    path: str | None = Field(default=None, alias='Path')
    user_email: str | None = Field(default=None, alias='UserEmail')
    user_id: str | None = Field(default=None, alias='UserId')
    user_name: str | None = Field(default=None, alias='UserName')

class UserGroup(GeneratedModel):
    creation_date: str | None = Field(default=None, alias='CreationDate')
    last_modification_date: str | None = Field(default=None, alias='LastModificationDate')
    name: str | None = Field(default=None, alias='Name')
    orn: str | None = Field(default=None, alias='Orn')
    path: str | None = Field(default=None, alias='Path')
    user_group_id: str | None = Field(default=None, alias='UserGroupId')

class VgwTelemetry(GeneratedModel):
    accepted_route_count: int | None = Field(default=None, alias='AcceptedRouteCount')
    last_state_change_date: str | None = Field(default=None, alias='LastStateChangeDate')
    outside_ip_address: str | None = Field(default=None, alias='OutsideIpAddress')
    state: str | None = Field(default=None, alias='State')
    state_description: str | None = Field(default=None, alias='StateDescription')

class VirtualGateway(GeneratedModel):
    connection_type: str | None = Field(default=None, alias='ConnectionType')
    net_to_virtual_gateway_links: list[NetToVirtualGatewayLink] | None = Field(default=None, alias='NetToVirtualGatewayLinks')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    virtual_gateway_id: str | None = Field(default=None, alias='VirtualGatewayId')

class Vm(GeneratedModel):
    actions_on_next_boot: ActionsOnNextBoot | None = Field(default=None, alias='ActionsOnNextBoot')
    architecture: str | None = Field(default=None, alias='Architecture')
    block_device_mappings: list[BlockDeviceMappingCreated] | None = Field(default=None, alias='BlockDeviceMappings')
    boot_mode: BootMode | None = Field(default=None, alias='BootMode')
    bsu_optimized: bool | None = Field(default=None, alias='BsuOptimized')
    client_token: str | None = Field(default=None, alias='ClientToken')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    deletion_protection: bool | None = Field(default=None, alias='DeletionProtection')
    hypervisor: str | None = Field(default=None, alias='Hypervisor')
    image_id: str | None = Field(default=None, alias='ImageId')
    is_source_dest_checked: bool | None = Field(default=None, alias='IsSourceDestChecked')
    keypair_name: str | None = Field(default=None, alias='KeypairName')
    launch_number: int | None = Field(default=None, alias='LaunchNumber')
    nested_virtualization: bool | None = Field(default=None, alias='NestedVirtualization')
    net_id: str | None = Field(default=None, alias='NetId')
    nics: list[NicLight] | None = Field(default=None, alias='Nics')
    os_family: str | None = Field(default=None, alias='OsFamily')
    performance: str | None = Field(default=None, alias='Performance')
    placement: Placement | None = Field(default=None, alias='Placement')
    private_dns_name: str | None = Field(default=None, alias='PrivateDnsName')
    private_ip: str | None = Field(default=None, alias='PrivateIp')
    product_codes: list[str] | None = Field(default=None, alias='ProductCodes')
    public_dns_name: str | None = Field(default=None, alias='PublicDnsName')
    public_ip: str | None = Field(default=None, alias='PublicIp')
    reservation_id: str | None = Field(default=None, alias='ReservationId')
    root_device_name: str | None = Field(default=None, alias='RootDeviceName')
    root_device_type: str | None = Field(default=None, alias='RootDeviceType')
    security_groups: list[SecurityGroupLight] | None = Field(default=None, alias='SecurityGroups')
    state: str | None = Field(default=None, alias='State')
    state_reason: str | None = Field(default=None, alias='StateReason')
    subnet_id: str | None = Field(default=None, alias='SubnetId')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    tpm_enabled: bool | None = Field(default=None, alias='TpmEnabled')
    user_data: str | None = Field(default=None, alias='UserData')
    vm_id: str | None = Field(default=None, alias='VmId')
    vm_initiated_shutdown_behavior: str | None = Field(default=None, alias='VmInitiatedShutdownBehavior')
    vm_type: str | None = Field(default=None, alias='VmType')

class VmGroup(GeneratedModel):
    creation_date: str | None = Field(default=None, alias='CreationDate')
    description: str | None = Field(default=None, alias='Description')
    positioning_strategy: Literal['attract', 'no-strategy', 'repulse'] | None = Field(default=None, alias='PositioningStrategy')
    security_group_ids: list[str] | None = Field(default=None, alias='SecurityGroupIds')
    state: Literal['available', 'deleted', 'deleting', 'pending', 'scaling down', 'scaling up'] | None = Field(default=None, alias='State')
    subnet_id: str | None = Field(default=None, alias='SubnetId')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vm_count: int | None = Field(default=None, alias='VmCount')
    vm_group_id: str | None = Field(default=None, alias='VmGroupId')
    vm_group_name: str | None = Field(default=None, alias='VmGroupName')
    vm_ids: list[str] | None = Field(default=None, alias='VmIds')
    vm_template_id: str | None = Field(default=None, alias='VmTemplateId')

class VmState(GeneratedModel):
    current_state: str | None = Field(default=None, alias='CurrentState')
    previous_state: str | None = Field(default=None, alias='PreviousState')
    vm_id: str | None = Field(default=None, alias='VmId')

class VmStates(GeneratedModel):
    maintenance_events: list[MaintenanceEvent] | None = Field(default=None, alias='MaintenanceEvents')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    vm_id: str | None = Field(default=None, alias='VmId')
    vm_state: str | None = Field(default=None, alias='VmState')

class VmTemplate(GeneratedModel):
    cpu_cores: int = Field(alias='CpuCores')
    cpu_generation: str = Field(alias='CpuGeneration')
    cpu_performance: Literal['medium', 'high', 'highest'] | None = Field(default=None, alias='CpuPerformance')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    description: str | None = Field(default=None, alias='Description')
    image_id: str = Field(alias='ImageId')
    keypair_name: str | None = Field(default=None, alias='KeypairName')
    ram: int = Field(alias='Ram')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vm_template_id: str = Field(alias='VmTemplateId')
    vm_template_name: str = Field(alias='VmTemplateName')

class VmType(GeneratedModel):
    bsu_optimized: bool | None = Field(default=None, alias='BsuOptimized')
    ephemerals_type: str | None = Field(default=None, alias='EphemeralsType')
    eth: int | None = Field(default=None, alias='Eth')
    gpu: int | None = Field(default=None, alias='Gpu')
    max_private_ips: int | None = Field(default=None, alias='MaxPrivateIps')
    memory_size: float | None = Field(default=None, alias='MemorySize')
    vcore_count: int | None = Field(default=None, alias='VcoreCount')
    vm_type_name: str | None = Field(default=None, alias='VmTypeName')
    volume_count: int | None = Field(default=None, alias='VolumeCount')
    volume_size: int | None = Field(default=None, alias='VolumeSize')

class Volume(GeneratedModel):
    client_token: str | None = Field(default=None, alias='ClientToken')
    creation_date: str | None = Field(default=None, alias='CreationDate')
    iops: int | None = Field(default=None, alias='Iops')
    linked_volumes: list[LinkedVolume] | None = Field(default=None, alias='LinkedVolumes')
    size: int | None = Field(default=None, alias='Size')
    snapshot_id: str | None = Field(default=None, alias='SnapshotId')
    state: str | None = Field(default=None, alias='State')
    subregion_name: str | None = Field(default=None, alias='SubregionName')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    task_id: str | None = Field(default=None, alias='TaskId')
    volume_id: str | None = Field(default=None, alias='VolumeId')
    volume_type: str | None = Field(default=None, alias='VolumeType')

class VolumeUpdate(GeneratedModel):
    origin: VolumeUpdateParameters | None = Field(default=None, alias='Origin')
    target: VolumeUpdateParameters | None = Field(default=None, alias='Target')

class VolumeUpdateParameters(GeneratedModel):
    iops: int | None = Field(alias='Iops')
    size: int = Field(alias='Size')
    volume_type: str = Field(alias='VolumeType')

class VolumeUpdateTask(GeneratedModel):
    comment: str | None = Field(default=None, alias='Comment')
    completion_date: str | None = Field(default=None, alias='CompletionDate')
    progress: int | None = Field(default=None, alias='Progress')
    start_date: str | None = Field(default=None, alias='StartDate')
    state: str | None = Field(default=None, alias='State')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    task_id: str | None = Field(default=None, alias='TaskId')
    volume_id: str | None = Field(default=None, alias='VolumeId')
    volume_update: VolumeUpdate | None = Field(default=None, alias='VolumeUpdate')

class VpnConnection(GeneratedModel):
    client_gateway_configuration: str | None = Field(default=None, alias='ClientGatewayConfiguration')
    client_gateway_id: str | None = Field(default=None, alias='ClientGatewayId')
    connection_type: str | None = Field(default=None, alias='ConnectionType')
    routes: list[RouteLight] | None = Field(default=None, alias='Routes')
    state: str | None = Field(default=None, alias='State')
    static_routes_only: bool | None = Field(default=None, alias='StaticRoutesOnly')
    tags: list[ResourceTag] | None = Field(default=None, alias='Tags')
    vgw_telemetries: list[VgwTelemetry] | None = Field(default=None, alias='VgwTelemetries')
    virtual_gateway_id: str | None = Field(default=None, alias='VirtualGatewayId')
    vpn_connection_id: str | None = Field(default=None, alias='VpnConnectionId')
    vpn_options: VpnOptions | None = Field(default=None, alias='VpnOptions')

class VpnOptions(GeneratedModel):
    phase1_options: Phase1Options | None = Field(default=None, alias='Phase1Options')
    phase2_options: Phase2Options | None = Field(default=None, alias='Phase2Options')
    tunnel_inside_ip_range: str | None = Field(default=None, alias='TunnelInsideIpRange')

class With(GeneratedModel):
    account_id: bool | None = Field(default=None, alias='AccountId')
    call_duration: bool | None = Field(default=None, alias='CallDuration')
    query_access_key: bool | None = Field(default=None, alias='QueryAccessKey')
    query_api_name: bool | None = Field(default=None, alias='QueryApiName')
    query_api_version: bool | None = Field(default=None, alias='QueryApiVersion')
    query_call_name: bool | None = Field(default=None, alias='QueryCallName')
    query_date: bool | None = Field(default=None, alias='QueryDate')
    query_header_raw: bool | None = Field(default=None, alias='QueryHeaderRaw')
    query_header_size: bool | None = Field(default=None, alias='QueryHeaderSize')
    query_ip_address: bool | None = Field(default=None, alias='QueryIpAddress')
    query_payload_raw: bool | None = Field(default=None, alias='QueryPayloadRaw')
    query_payload_size: bool | None = Field(default=None, alias='QueryPayloadSize')
    query_user_agent: bool | None = Field(default=None, alias='QueryUserAgent')
    request_id: bool | None = Field(default=None, alias='RequestId')
    response_size: bool | None = Field(default=None, alias='ResponseSize')
    response_status_code: bool | None = Field(default=None, alias='ResponseStatusCode')
