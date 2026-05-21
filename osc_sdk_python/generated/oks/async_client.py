"""Generated typed OKS client slice.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator
"""

from typing import Any

from osc_sdk_python.runtime.request import RequestSpec
from .models import (
    CPSubregionsResponse,
    ClusterResponse,
    ClusterResponseList,
    ControlPlanesResponse,
    CreateClusterRequest,
    CreateProjectRequest,
    DeleteClusterRequest,
    DeleteProjectRequest,
    DetailResponse,
    GetCPSubregionsRequest,
    GetClientIPRequest,
    GetClusterRequest,
    GetClusterTemplateRequest,
    GetControlPlanePlansRequest,
    GetKubeconfigRequest,
    GetKubeconfigWithPubkeyNACLRequest,
    GetKubernetesVersionsRequest,
    GetNetPeeringAcceptanceTemplateRequest,
    GetNetPeeringRequestTemplateRequest,
    GetNodepoolTemplateRequest,
    GetProjectNetsRequest,
    GetProjectPublicIpsRequest,
    GetProjectQuotasRequest,
    GetProjectRequest,
    GetProjectSnapshotsRequest,
    GetProjectTemplateRequest,
    GetQuotasRequest,
    IPResponse,
    KubeconfigResponse,
    KubernetesVersionsResponse,
    ListAllClustersRequest,
    ListClustersByProjectIDRequest,
    ListProjectsRequest,
    NetsResponse,
    ProjectResponse,
    ProjectResponseList,
    PublicIpsResponse,
    SnapshotsResponse,
    TemplateResponse_ClusterInputTemplate,
    TemplateResponse_NetPeeringAcceptance,
    TemplateResponse_NetPeeringRequest,
    TemplateResponse_Nodepool,
    TemplateResponse_ProjectInput,
    UpdateClusterRequest,
    UpdateProjectRequest,
    UpgradeClusterRequest,
    projects__project_schema__QuotasResponse,
    quotas__quota_schema__QuotasResponse,
)


def _dump_json_body(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(exclude_none=True, by_alias=True)
    return value


class AsyncOksTypedMixin:
    async def list_projects(
        self,
        request: ListProjectsRequest | None = None,
    ) -> ProjectResponseList:
        if request is None:
            request = ListProjectsRequest()

        path_params = {
        }
        query_params = {
            'name': request.name,
            'status': request.status,
            'cidr': request.cidr,
            'deleted': request.deleted,
            'cursor': request.cursor,
            'page': request.page,
            'limit': request.limit,
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/projects",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ProjectResponseList.model_validate(response)

    async def create_project(
        self,
        request: CreateProjectRequest | None = None,
    ) -> ProjectResponse:
        if request is None:
            request = CreateProjectRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="POST",
                path="/projects",
                json_body=_dump_json_body(request.body),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ProjectResponse.model_validate(response)

    async def get_project(
        self,
        request: GetProjectRequest | None = None,
    ) -> ProjectResponse:
        if request is None:
            request = GetProjectRequest()

        path_params = {
            'project_id': request.project_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/projects/{project_id}",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ProjectResponse.model_validate(response)

    async def update_project(
        self,
        request: UpdateProjectRequest | None = None,
    ) -> ProjectResponse:
        if request is None:
            request = UpdateProjectRequest()

        path_params = {
            'project_id': request.project_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="PATCH",
                path="/projects/{project_id}",
                json_body=_dump_json_body(request.body),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ProjectResponse.model_validate(response)

    async def delete_project(
        self,
        request: DeleteProjectRequest | None = None,
    ) -> DetailResponse:
        if request is None:
            request = DeleteProjectRequest()

        path_params = {
            'project_id': request.project_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="DELETE",
                path="/projects/{project_id}",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return DetailResponse.model_validate(response)

    async def get_project_quotas(
        self,
        request: GetProjectQuotasRequest | None = None,
    ) -> projects__project_schema__QuotasResponse:
        if request is None:
            request = GetProjectQuotasRequest()

        path_params = {
            'project_id': request.project_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/projects/{project_id}/quotas",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return projects__project_schema__QuotasResponse.model_validate(response)

    async def get_project_snapshots(
        self,
        request: GetProjectSnapshotsRequest | None = None,
    ) -> SnapshotsResponse:
        if request is None:
            request = GetProjectSnapshotsRequest()

        path_params = {
            'project_id': request.project_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/projects/{project_id}/snapshots",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return SnapshotsResponse.model_validate(response)

    async def get_project_public_ips(
        self,
        request: GetProjectPublicIpsRequest | None = None,
    ) -> PublicIpsResponse:
        if request is None:
            request = GetProjectPublicIpsRequest()

        path_params = {
            'project_id': request.project_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/projects/{project_id}/public_ips",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return PublicIpsResponse.model_validate(response)

    async def get_project_nets(
        self,
        request: GetProjectNetsRequest | None = None,
    ) -> NetsResponse:
        if request is None:
            request = GetProjectNetsRequest()

        path_params = {
            'project_id': request.project_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/projects/{project_id}/nets",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return NetsResponse.model_validate(response)

    async def list_clusters_by_project_id(
        self,
        request: ListClustersByProjectIDRequest | None = None,
    ) -> ClusterResponseList:
        if request is None:
            request = ListClustersByProjectIDRequest()

        path_params = {
        }
        query_params = {
            'project_id': request.project_id,
            'name': request.name,
            'status': request.status,
            'version': request.version,
            'deleted': request.deleted,
            'cursor': request.cursor,
            'page': request.page,
            'limit': request.limit,
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/clusters",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ClusterResponseList.model_validate(response)

    async def create_cluster(
        self,
        request: CreateClusterRequest | None = None,
    ) -> ClusterResponse:
        if request is None:
            request = CreateClusterRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="POST",
                path="/clusters",
                json_body=_dump_json_body(request.body),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ClusterResponse.model_validate(response)

    async def list_all_clusters(
        self,
        request: ListAllClustersRequest | None = None,
    ) -> ClusterResponseList:
        if request is None:
            request = ListAllClustersRequest()

        path_params = {
        }
        query_params = {
            'name': request.name,
            'status': request.status,
            'version': request.version,
            'deleted': request.deleted,
            'cursor': request.cursor,
            'page': request.page,
            'limit': request.limit,
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/clusters/all",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ClusterResponseList.model_validate(response)

    async def get_cluster(
        self,
        request: GetClusterRequest | None = None,
    ) -> ClusterResponse:
        if request is None:
            request = GetClusterRequest()

        path_params = {
            'cluster_id': request.cluster_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/clusters/{cluster_id}",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ClusterResponse.model_validate(response)

    async def update_cluster(
        self,
        request: UpdateClusterRequest | None = None,
    ) -> ClusterResponse:
        if request is None:
            request = UpdateClusterRequest()

        path_params = {
            'cluster_id': request.cluster_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="PATCH",
                path="/clusters/{cluster_id}",
                json_body=_dump_json_body(request.body),
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ClusterResponse.model_validate(response)

    async def delete_cluster(
        self,
        request: DeleteClusterRequest | None = None,
    ) -> DetailResponse:
        if request is None:
            request = DeleteClusterRequest()

        path_params = {
            'cluster_id': request.cluster_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="DELETE",
                path="/clusters/{cluster_id}",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return DetailResponse.model_validate(response)

    async def get_kubeconfig(
        self,
        request: GetKubeconfigRequest | None = None,
    ) -> KubeconfigResponse:
        if request is None:
            request = GetKubeconfigRequest()

        path_params = {
            'cluster_id': request.cluster_id,
        }
        query_params = {
            'user': request.user,
            'group': request.group,
            'ttl': request.ttl,
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/clusters/{cluster_id}/kubeconfig",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return KubeconfigResponse.model_validate(response)

    async def get_kubeconfig_with_pubkey_nacl(
        self,
        request: GetKubeconfigWithPubkeyNACLRequest | None = None,
    ) -> KubeconfigResponse:
        if request is None:
            request = GetKubeconfigWithPubkeyNACLRequest()

        path_params = {
            'cluster_id': request.cluster_id,
        }
        query_params = {
            'user': request.user,
            'group': request.group,
            'ttl': request.ttl,
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="POST",
                path="/clusters/{cluster_id}/kubeconfig",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return KubeconfigResponse.model_validate(response)

    async def upgrade_cluster(
        self,
        request: UpgradeClusterRequest | None = None,
    ) -> ClusterResponse:
        if request is None:
            request = UpgradeClusterRequest()

        path_params = {
            'cluster_id': request.cluster_id,
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="PATCH",
                path="/clusters/{cluster_id}/upgrade",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ClusterResponse.model_validate(response)

    async def get_kubernetes_versions(
        self,
        request: GetKubernetesVersionsRequest | None = None,
    ) -> KubernetesVersionsResponse:
        if request is None:
            request = GetKubernetesVersionsRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/clusters/limits/kubernetes_versions",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return KubernetesVersionsResponse.model_validate(response)

    async def get_cp_subregions(
        self,
        request: GetCPSubregionsRequest | None = None,
    ) -> CPSubregionsResponse:
        if request is None:
            request = GetCPSubregionsRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/clusters/limits/cp_subregions",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return CPSubregionsResponse.model_validate(response)

    async def get_control_plane_plans(
        self,
        request: GetControlPlanePlansRequest | None = None,
    ) -> ControlPlanesResponse:
        if request is None:
            request = GetControlPlanePlansRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/clusters/limits/control_plane_plans",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return ControlPlanesResponse.model_validate(response)

    async def get_project_template(
        self,
        request: GetProjectTemplateRequest | None = None,
    ) -> TemplateResponse_ProjectInput:
        if request is None:
            request = GetProjectTemplateRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/templates/project",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return TemplateResponse_ProjectInput.model_validate(response)

    async def get_cluster_template(
        self,
        request: GetClusterTemplateRequest | None = None,
    ) -> TemplateResponse_ClusterInputTemplate:
        if request is None:
            request = GetClusterTemplateRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/templates/cluster",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return TemplateResponse_ClusterInputTemplate.model_validate(response)

    async def get_nodepool_template(
        self,
        request: GetNodepoolTemplateRequest | None = None,
    ) -> TemplateResponse_Nodepool:
        if request is None:
            request = GetNodepoolTemplateRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/templates/nodepool",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return TemplateResponse_Nodepool.model_validate(response)

    async def get_net_peering_request_template(
        self,
        request: GetNetPeeringRequestTemplateRequest | None = None,
    ) -> TemplateResponse_NetPeeringRequest:
        if request is None:
            request = GetNetPeeringRequestTemplateRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/templates/netpeeringrequest",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return TemplateResponse_NetPeeringRequest.model_validate(response)

    async def get_net_peering_acceptance_template(
        self,
        request: GetNetPeeringAcceptanceTemplateRequest | None = None,
    ) -> TemplateResponse_NetPeeringAcceptance:
        if request is None:
            request = GetNetPeeringAcceptanceTemplateRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/templates/netpeeringacceptance",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return TemplateResponse_NetPeeringAcceptance.model_validate(response)

    async def get_quotas(
        self,
        request: GetQuotasRequest | None = None,
    ) -> quotas__quota_schema__QuotasResponse:
        if request is None:
            request = GetQuotasRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/quotas",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return quotas__quota_schema__QuotasResponse.model_validate(response)

    async def get_client_ip(
        self,
        request: GetClientIPRequest | None = None,
    ) -> IPResponse:
        if request is None:
            request = GetClientIPRequest()

        path_params = {
        }
        query_params = {
        }
        response = await self.call.request(
            RequestSpec(
                service="oks",
                method="GET",
                path="/myip",
                json_body=None,
                query_params={
                    key: value
                    for key, value in query_params.items()
                    if value is not None
                },
            ),
            path_params=path_params,
        )
        return IPResponse.model_validate(response)
