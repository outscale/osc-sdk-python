"""Generated typed OKS client slice.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator
"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class GeneratedModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class AdmissionFlags(GeneratedModel):
    disable_admission_plugins: list[str] | None = Field(default=None, alias='disable_admission_plugins')
    enable_admission_plugins: list[str] | None = Field(default=None, alias='enable_admission_plugins')
    applied_admission_plugins: list[str] | None = Field(default=None, alias='applied_admission_plugins')

class AdmissionFlagsInput(GeneratedModel):
    disable_admission_plugins: list[str] | None = Field(default=None, alias='disable_admission_plugins')
    enable_admission_plugins: list[str] | None = Field(default=None, alias='enable_admission_plugins')

class AuthStrategy(GeneratedModel):
    oidc: OpenIdConnectConfig = Field(alias='oidc')

class AutoMaintenances(GeneratedModel):
    minor_upgrade_maintenance: MaintenanceWindow = Field(alias='minor_upgrade_maintenance')
    patch_upgrade_maintenance: MaintenanceWindow = Field(alias='patch_upgrade_maintenance')

class AutoUpgradeMaintenance(GeneratedModel):
    duration_hours: int = Field(alias='durationHours')
    start_hour: int = Field(alias='startHour')
    week_day: str = Field(alias='weekDay')

class CPSubregionsResponse(GeneratedModel):
    response_context: clusters__cluster_schema__ResponseContext = Field(alias='ResponseContext')
    cp_subregions: list[str] = Field(alias='CPSubregions')

class Cluster(GeneratedModel):
    project_id: str = Field(alias='project_id')
    id: str = Field(alias='id')
    name: str = Field(alias='name')
    description: str | None = Field(default=None, alias='description')
    cp_multi_az: bool = Field(alias='cp_multi_az')
    cp_subregions: list[str] = Field(alias='cp_subregions')
    version: str = Field(alias='version')
    expected_version: str | None = Field(default=None, alias='expected_version')
    cni: str = Field(alias='cni')
    admin_lbu: bool = Field(alias='admin_lbu')
    admission_flags: AdmissionFlags = Field(alias='admission_flags')
    cidr_pods: str = Field(alias='cidr_pods')
    cidr_service: str = Field(alias='cidr_service')
    cluster_dns: str = Field(alias='cluster_dns')
    tags: dict[str, str] = Field(alias='tags')
    auto_maintenances: AutoMaintenances | None = Field(default=None, alias='auto_maintenances')
    maintenance_window: Maintenance | None = Field(default=None, alias='maintenance_window')
    control_planes: str = Field(alias='control_planes')
    expected_control_planes: str | None = Field(default=None, alias='expected_control_planes')
    admin_whitelist: list[str] = Field(alias='admin_whitelist')
    statuses: Statuses = Field(alias='statuses')
    disable_api_termination: bool | None = Field(default=None, alias='disable_api_termination')
    auth: AuthStrategy | None = Field(default=None, alias='auth')

class ClusterInput(GeneratedModel):
    name: str = Field(alias='name')
    project_id: str = Field(alias='project_id')
    description: str | None = Field(default=None, alias='description')
    cp_multi_az: bool | None = Field(default=None, alias='cp_multi_az')
    cp_subregions: list[str] | None = Field(default=None, alias='cp_subregions')
    version: str = Field(alias='version')
    admin_lbu: bool | None = Field(default=None, alias='admin_lbu')
    admission_flags: AdmissionFlagsInput | None = Field(default=None, alias='admission_flags')
    cidr_pods: str = Field(alias='cidr_pods')
    cidr_service: str = Field(alias='cidr_service')
    cluster_dns: str | None = Field(default=None, alias='cluster_dns')
    tags: dict[str, str] | None = Field(default=None, alias='tags')
    auto_maintenances: AutoMaintenances | None = Field(default=None, alias='auto_maintenances')
    maintenance_window: Maintenance | None = Field(default=None, alias='maintenance_window')
    control_planes: str | None = Field(default=None, alias='control_planes')
    admin_whitelist: list[str] = Field(alias='admin_whitelist')
    quirks: list[str] | None = Field(default=None, alias='quirks')
    disable_api_termination: bool | None = Field(default=None, alias='disable_api_termination')
    auth: AuthStrategy | None = Field(default=None, alias='auth')

class ClusterInputTemplate(GeneratedModel):
    project_id: str = Field(alias='project_id')
    description: str | None = Field(default=None, alias='description')
    version: str = Field(alias='version')
    admin_lbu: bool | None = Field(default=None, alias='admin_lbu')
    admission_flags: AdmissionFlagsInput | None = Field(default=None, alias='admission_flags')
    cidr_pods: str | None = Field(default=None, alias='cidr_pods')
    cidr_service: str | None = Field(default=None, alias='cidr_service')
    cluster_dns: str | None = Field(default=None, alias='cluster_dns')
    tags: dict[str, str] | None = Field(default=None, alias='tags')
    auto_maintenances: AutoMaintenances | None = Field(default=None, alias='auto_maintenances')
    maintenance_window: Maintenance | None = Field(default=None, alias='maintenance_window')
    control_planes: str | None = Field(default=None, alias='control_planes')
    admin_whitelist: list[str] = Field(alias='admin_whitelist')
    quirks: list[str] | None = Field(default=None, alias='quirks')
    disable_api_termination: bool | None = Field(default=None, alias='disable_api_termination')

class ClusterResponse(GeneratedModel):
    response_context: clusters__cluster_schema__ResponseContext = Field(alias='ResponseContext')
    cluster: Cluster = Field(alias='Cluster')

class ClusterResponseList(GeneratedModel):
    response_context: clusters__cluster_schema__ResponseContext = Field(alias='ResponseContext')
    pagination: Pagination = Field(alias='Pagination')
    clusters: list[Cluster] = Field(alias='Clusters')

class ClusterUpdate(GeneratedModel):
    description: str | None = Field(default=None, alias='description')
    admission_flags: AdmissionFlagsInput | None = Field(default=None, alias='admission_flags')
    tags: dict[str, str] | None = Field(default=None, alias='tags')
    auto_maintenances: AutoMaintenances | None = Field(default=None, alias='auto_maintenances')
    maintenance_window: Maintenance | None = Field(default=None, alias='maintenance_window')
    admin_whitelist: list[str] | None = Field(default=None, alias='admin_whitelist')
    quirks: list[str] | None = Field(default=None, alias='quirks')
    disable_api_termination: bool | None = Field(default=None, alias='disable_api_termination')
    version: str | None = Field(default=None, alias='version')
    control_planes: str | None = Field(default=None, alias='control_planes')
    auth: AuthStrategy | None = Field(default=None, alias='auth')

class ControlPlanesResponse(GeneratedModel):
    response_context: clusters__cluster_schema__ResponseContext = Field(alias='ResponseContext')
    control_planes: list[str] = Field(alias='ControlPlanes')

class Cursor(GeneratedModel):
    next_cursor: str | None = Field(default=None, alias='next_cursor')

class DetailResponse(GeneratedModel):
    response_context: projects__project_schema__ResponseContext = Field(alias='ResponseContext')
    detail: str = Field(alias='detail')

class ErrorItem(GeneratedModel):
    type: str = Field(alias='Type')
    details: Any = Field(alias='Details')
    code: str = Field(alias='Code')

class ErrorResponse(GeneratedModel):
    errors: list[ErrorItem] = Field(alias='Errors')
    response_context: ResponseContext_Input = Field(alias='ResponseContext')

class IPDetails(GeneratedModel):
    x_real_ip: str | None = Field(default=None, alias='x_real_ip')

class IPResponse(GeneratedModel):
    response_context: myip__myip_schema__ResponseContext = Field(alias='ResponseContext')
    ip: IPDetails = Field(alias='IP')

class KubeconfigData(GeneratedModel):
    kubeconfig: str = Field(alias='kubeconfig')

class KubeconfigResponse(GeneratedModel):
    response_context: clusters__cluster_schema__ResponseContext = Field(alias='ResponseContext')
    cluster: clusters__cluster_schema__RPCResponse = Field(alias='Cluster')

class KubernetesVersionsResponse(GeneratedModel):
    response_context: clusters__cluster_schema__ResponseContext = Field(alias='ResponseContext')
    versions: list[str] = Field(alias='Versions')

class Maintenance(GeneratedModel):
    duration_hours: int = Field(alias='duration_hours')
    start_hour: int = Field(alias='start_hour')
    week_day: str = Field(alias='week_day')
    tz: str | None = Field(default=None, alias='tz')

class MaintenanceWindow(GeneratedModel):
    enabled: bool | None = Field(default=None, alias='enabled')
    duration_hours: int | None = Field(default=None, alias='duration_hours')
    start_hour: int | None = Field(default=None, alias='start_hour')
    week_day: str | None = Field(default=None, alias='week_day')
    tz: str | None = Field(default=None, alias='tz')

class Net(GeneratedModel):
    dhcp_options_set_id: str = Field(alias='DhcpOptionsSetId')
    ip_range: str = Field(alias='IpRange')
    net_id: str = Field(alias='NetId')
    state: str = Field(alias='State')
    tenancy: str = Field(alias='Tenancy')

class NetPeeringAcceptance(GeneratedModel):
    api_version: str = Field(alias='apiVersion')
    kind: str = Field(alias='kind')
    metadata: netpeerings__netpeering_schema__Metadata = Field(alias='metadata')
    spec: SpecNetPeeringAcceptance = Field(alias='spec')

class NetPeeringRequest(GeneratedModel):
    api_version: str = Field(alias='apiVersion')
    kind: str = Field(alias='kind')
    metadata: netpeerings__netpeering_schema__Metadata = Field(alias='metadata')
    spec: SpecNetPeeringRequest = Field(alias='spec')

class NetsResponse(GeneratedModel):
    response_context: projects__project_schema__ResponseContext = Field(alias='ResponseContext')
    nets: list[Net] = Field(alias='Nets')

class Nodepool(GeneratedModel):
    api_version: str = Field(alias='apiVersion')
    kind: str = Field(alias='kind')
    metadata: nodepools__nodepool_schema__Metadata = Field(alias='metadata')
    spec: Spec = Field(alias='spec')

class OKSQuotas(GeneratedModel):
    projects: int = Field(alias='Projects')
    clusters_per_project: int = Field(alias='ClustersPerProject')
    kube_versions: list[str] = Field(alias='KubeVersions')
    cp_subregions: list[str] = Field(alias='CPSubregions')

class Offset(GeneratedModel):
    page: int | None = Field(default=None, alias='page')
    limit: int | None = Field(default=None, alias='limit')
    total: int | None = Field(default=None, alias='total')

class OpenIdConnectConfig(GeneratedModel):
    issuer_url: str = Field(alias='issuer-url')
    client_id: str = Field(alias='client-id')
    username_claim: str | None = Field(default=None, alias='username-claim')
    username_prefix: str | None = Field(default=None, alias='username-prefix')
    groups_claim: list[str] | None = Field(default=None, alias='groups-claim')
    groups_prefix: str | None = Field(default=None, alias='groups-prefix')
    required_claim: dict[str, str] | None = Field(default=None, alias='required-claim')

class Pagination(GeneratedModel):
    cursor: Cursor | None = Field(default=None, alias='cursor')
    offset: Offset | None = Field(default=None, alias='offset')

class PermissionsOnResource(GeneratedModel):
    global_permission: int = Field(alias='GlobalPermission')
    account_ids: list[str] = Field(alias='AccountIds')

class Project(GeneratedModel):
    id: str = Field(alias='id')
    name: str = Field(alias='name')
    description: str | None = Field(default=None, alias='description')
    cidr: str = Field(alias='cidr')
    region: str = Field(alias='region')
    status: str = Field(alias='status')
    tags: dict[str, str] = Field(alias='tags')
    disable_api_termination: bool | None = Field(default=None, alias='disable_api_termination')
    created_at: str = Field(alias='created_at')
    updated_at: str = Field(alias='updated_at')
    deleted_at: str | None = Field(default=None, alias='deleted_at')

class ProjectInput(GeneratedModel):
    name: str = Field(alias='name')
    description: str | None = Field(default=None, alias='description')
    cidr: str = Field(alias='cidr')
    region: str = Field(alias='region')
    tags: dict[str, str] | None = Field(default=None, alias='tags')
    quirks: list[str] | None = Field(default=None, alias='quirks')
    disable_api_termination: bool | None = Field(default=None, alias='disable_api_termination')

class ProjectResponse(GeneratedModel):
    response_context: projects__project_schema__ResponseContext = Field(alias='ResponseContext')
    project: Project = Field(alias='Project')

class ProjectResponseList(GeneratedModel):
    response_context: projects__project_schema__ResponseContext = Field(alias='ResponseContext')
    pagination: Pagination = Field(alias='Pagination')
    projects: list[Project] = Field(alias='Projects')

class ProjectUpdate(GeneratedModel):
    description: str | None = Field(default=None, alias='description')
    tags: dict[str, str] | None = Field(default=None, alias='tags')
    quirks: list[str] | None = Field(default=None, alias='quirks')
    disable_api_termination: bool | None = Field(default=None, alias='disable_api_termination')

class PublicIp(GeneratedModel):
    tags: list[ResourceTag] = Field(alias='Tags')
    public_ip: str = Field(alias='PublicIp')
    public_ip_id: str = Field(alias='PublicIpId')

class PublicIpsResponse(GeneratedModel):
    response_context: projects__project_schema__ResponseContext = Field(alias='ResponseContext')
    public_ips: list[PublicIp] = Field(alias='PublicIps')

class Quotas(GeneratedModel):
    short_description: str = Field(alias='ShortDescription')
    quota_collection: str = Field(alias='QuotaCollection')
    account_id: str = Field(alias='AccountId')
    description: str = Field(alias='Description')
    max_value: int = Field(alias='MaxValue')
    used_value: int = Field(alias='UsedValue')
    name: str = Field(alias='Name')

class QuotasData(GeneratedModel):
    quotas: list[Quotas] = Field(alias='quotas')
    subregions: list[Subregion] = Field(alias='subregions')

class ResourceTag(GeneratedModel):
    key: str = Field(alias='Key')
    value: str = Field(alias='Value')

class ResponseContext_Input(GeneratedModel):
    request_id: str = Field(alias='RequestId')

class Snapshot(GeneratedModel):
    volume_size: int = Field(alias='VolumeSize')
    account_id: str = Field(alias='AccountId')
    volume_id: str = Field(alias='VolumeId')
    creation_date: str = Field(alias='CreationDate')
    progress: int = Field(alias='Progress')
    snapshot_id: str = Field(alias='SnapshotId')
    state: str = Field(alias='State')
    description: str = Field(alias='Description')
    tags: list[ResourceTag] = Field(alias='Tags')
    permissions_to_create_volume: PermissionsOnResource = Field(alias='PermissionsToCreateVolume')

class SnapshotsResponse(GeneratedModel):
    response_context: projects__project_schema__ResponseContext = Field(alias='ResponseContext')
    snapshots: list[Snapshot] = Field(alias='Snapshots')

class Spec(GeneratedModel):
    desired_nodes: str = Field(alias='desiredNodes')
    node_type: str = Field(alias='nodeType')
    zones: list[str] = Field(alias='zones')
    volumes: list[Volume] = Field(alias='volumes')
    upgrade_strategy: UpgradeStrategy = Field(alias='upgradeStrategy')
    auto_healing: bool = Field(alias='autoHealing')

class SpecNetPeeringAcceptance(GeneratedModel):
    net_peering_id: str = Field(alias='netPeeringId')

class SpecNetPeeringRequest(GeneratedModel):
    accepter_net_id: str = Field(alias='accepterNetId')
    accepter_owner_id: str = Field(alias='accepterOwnerId')

class Statuses(GeneratedModel):
    created_at: str = Field(alias='created_at')
    deleted_at: str | None = Field(default=None, alias='deleted_at')
    updated_at: str | None = Field(default=None, alias='updated_at')
    status: str | None = Field(default=None, alias='status')
    available_upgrade: str | None = Field(default=None, alias='available_upgrade')

class Subregion(GeneratedModel):
    state: str = Field(alias='State')
    region_name: str = Field(alias='RegionName')
    subregion_name: str = Field(alias='SubregionName')
    location_code: str = Field(alias='LocationCode')

class TemplateResponse_ClusterInputTemplate(GeneratedModel):
    response_context: templates__template_schema__ResponseContext = Field(alias='ResponseContext')
    template: ClusterInputTemplate = Field(alias='Template')

class TemplateResponse_NetPeeringAcceptance(GeneratedModel):
    response_context: templates__template_schema__ResponseContext = Field(alias='ResponseContext')
    template: NetPeeringAcceptance = Field(alias='Template')

class TemplateResponse_NetPeeringRequest(GeneratedModel):
    response_context: templates__template_schema__ResponseContext = Field(alias='ResponseContext')
    template: NetPeeringRequest = Field(alias='Template')

class TemplateResponse_Nodepool(GeneratedModel):
    response_context: templates__template_schema__ResponseContext = Field(alias='ResponseContext')
    template: Nodepool = Field(alias='Template')

class TemplateResponse_ProjectInput(GeneratedModel):
    response_context: templates__template_schema__ResponseContext = Field(alias='ResponseContext')
    template: ProjectInput = Field(alias='Template')

class UpgradeStrategy(GeneratedModel):
    max_unavailable: int = Field(alias='maxUnavailable')
    max_surge: int = Field(alias='maxSurge')
    auto_upgrade_enabled: bool = Field(alias='autoUpgradeEnabled')
    auto_upgrade_maintenance: AutoUpgradeMaintenance = Field(alias='autoUpgradeMaintenance')

class ValidationDetail(GeneratedModel):
    loc: list[Any] = Field(alias='loc')
    msg: str = Field(alias='msg')
    type: str = Field(alias='type')

class Volume(GeneratedModel):
    device: str = Field(alias='device')
    type: str = Field(alias='type')
    size: int = Field(alias='size')
    dir: str = Field(alias='dir')

class clusters__cluster_schema__RPCResponse(GeneratedModel):
    request_id: str = Field(alias='request_id')
    data: KubeconfigData = Field(alias='data')

class clusters__cluster_schema__ResponseContext(GeneratedModel):
    request_id: str = Field(alias='RequestId')

class myip__myip_schema__ResponseContext(GeneratedModel):
    request_id: str = Field(alias='RequestId')

class netpeerings__netpeering_schema__Metadata(GeneratedModel):
    name: str = Field(alias='name')

class nodepools__nodepool_schema__Metadata(GeneratedModel):
    name: str = Field(alias='name')

class projects__project_schema__QuotasResponse(GeneratedModel):
    response_context: projects__project_schema__ResponseContext = Field(alias='ResponseContext')
    project: projects__project_schema__RPCResponse = Field(alias='Project')

class projects__project_schema__RPCResponse(GeneratedModel):
    request_id: str = Field(alias='request_id')
    data: QuotasData = Field(alias='data')

class projects__project_schema__ResponseContext(GeneratedModel):
    request_id: str = Field(alias='RequestId')

class quotas__quota_schema__QuotasResponse(GeneratedModel):
    response_context: quotas__quota_schema__ResponseContext = Field(alias='ResponseContext')
    quotas: OKSQuotas = Field(alias='Quotas')

class quotas__quota_schema__ResponseContext(GeneratedModel):
    request_id: str = Field(alias='RequestId')

class templates__template_schema__ResponseContext(GeneratedModel):
    request_id: str = Field(alias='RequestId')

class ListProjectsRequest(GeneratedModel):
    name: str | None = Field(default=None, alias='name')
    status: str | None = Field(default=None, alias='status')
    cidr: str | None = Field(default=None, alias='cidr')
    deleted: bool | None = Field(default=None, alias='deleted')
    cursor: str | None = Field(default=None, alias='cursor')
    page: int | None = Field(default=None, alias='page')
    limit: int | None = Field(default=None, alias='limit')

class CreateProjectRequest(GeneratedModel):
    body: ProjectInput = Field(alias='body')

class GetProjectRequest(GeneratedModel):
    project_id: str = Field(alias='project_id')

class UpdateProjectRequest(GeneratedModel):
    project_id: str = Field(alias='project_id')
    body: ProjectUpdate = Field(alias='body')

class DeleteProjectRequest(GeneratedModel):
    project_id: str = Field(alias='project_id')

class GetProjectQuotasRequest(GeneratedModel):
    project_id: str = Field(alias='project_id')

class GetProjectSnapshotsRequest(GeneratedModel):
    project_id: str = Field(alias='project_id')

class GetProjectPublicIpsRequest(GeneratedModel):
    project_id: str = Field(alias='project_id')

class GetProjectNetsRequest(GeneratedModel):
    project_id: str = Field(alias='project_id')

class ListClustersByProjectIDRequest(GeneratedModel):
    project_id: str | None = Field(default=None, alias='project_id')
    name: str | None = Field(default=None, alias='name')
    status: str | None = Field(default=None, alias='status')
    version: str | None = Field(default=None, alias='version')
    deleted: bool | None = Field(default=None, alias='deleted')
    cursor: str | None = Field(default=None, alias='cursor')
    page: int | None = Field(default=None, alias='page')
    limit: int | None = Field(default=None, alias='limit')

class CreateClusterRequest(GeneratedModel):
    body: ClusterInput = Field(alias='body')

class ListAllClustersRequest(GeneratedModel):
    name: str | None = Field(default=None, alias='name')
    status: str | None = Field(default=None, alias='status')
    version: str | None = Field(default=None, alias='version')
    deleted: bool | None = Field(default=None, alias='deleted')
    cursor: str | None = Field(default=None, alias='cursor')
    page: int | None = Field(default=None, alias='page')
    limit: int | None = Field(default=None, alias='limit')

class GetClusterRequest(GeneratedModel):
    cluster_id: str = Field(alias='cluster_id')

class UpdateClusterRequest(GeneratedModel):
    cluster_id: str = Field(alias='cluster_id')
    body: ClusterUpdate = Field(alias='body')

class DeleteClusterRequest(GeneratedModel):
    cluster_id: str = Field(alias='cluster_id')

class GetKubeconfigRequest(GeneratedModel):
    cluster_id: str = Field(alias='cluster_id')
    user: str | None = Field(default=None, alias='user')
    group: str | None = Field(default=None, alias='group')
    ttl: str | None = Field(default=None, alias='ttl')

class GetKubeconfigWithPubkeyNACLRequest(GeneratedModel):
    cluster_id: str = Field(alias='cluster_id')
    user: str | None = Field(default=None, alias='user')
    group: str | None = Field(default=None, alias='group')
    ttl: str | None = Field(default=None, alias='ttl')

class UpgradeClusterRequest(GeneratedModel):
    cluster_id: str = Field(alias='cluster_id')

class GetKubernetesVersionsRequest(GeneratedModel):
    pass

class GetCPSubregionsRequest(GeneratedModel):
    pass

class GetControlPlanePlansRequest(GeneratedModel):
    pass

class GetProjectTemplateRequest(GeneratedModel):
    pass

class GetClusterTemplateRequest(GeneratedModel):
    pass

class GetNodepoolTemplateRequest(GeneratedModel):
    pass

class GetNetPeeringRequestTemplateRequest(GeneratedModel):
    pass

class GetNetPeeringAcceptanceTemplateRequest(GeneratedModel):
    pass

class GetQuotasRequest(GeneratedModel):
    pass

class GetClientIPRequest(GeneratedModel):
    pass
