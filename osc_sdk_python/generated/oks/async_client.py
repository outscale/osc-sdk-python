"""Generated typed OKS client slice.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator

    python -m osc_sdk_python.codegen.generator oks osc
"""

from typing import Any

from pydantic import TypeAdapter, ValidationError

from osc_sdk_python.exceptions import SdkResponseError, SdkValidationError
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


class AsyncOksTypedMixin:
    async def list_projects(
        self,
        request: ListProjectsRequest | None = None,
    ) -> ProjectResponseList:
        request = _validate_request(ListProjectsRequest, request)

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
        return _validate_response(ProjectResponseList, response)

    async def create_project(
        self,
        request: CreateProjectRequest | None = None,
    ) -> ProjectResponse:
        request = _validate_request(CreateProjectRequest, request)

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
        return _validate_response(ProjectResponse, response)

    async def get_project(
        self,
        request: GetProjectRequest | None = None,
    ) -> ProjectResponse:
        request = _validate_request(GetProjectRequest, request)

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
        return _validate_response(ProjectResponse, response)

    async def update_project(
        self,
        request: UpdateProjectRequest | None = None,
    ) -> ProjectResponse:
        request = _validate_request(UpdateProjectRequest, request)

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
        return _validate_response(ProjectResponse, response)

    async def delete_project(
        self,
        request: DeleteProjectRequest | None = None,
    ) -> DetailResponse:
        request = _validate_request(DeleteProjectRequest, request)

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
        return _validate_response(DetailResponse, response)

    async def get_project_quotas(
        self,
        request: GetProjectQuotasRequest | None = None,
    ) -> projects__project_schema__QuotasResponse:
        request = _validate_request(GetProjectQuotasRequest, request)

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
        return _validate_response(projects__project_schema__QuotasResponse, response)

    async def get_project_snapshots(
        self,
        request: GetProjectSnapshotsRequest | None = None,
    ) -> SnapshotsResponse:
        request = _validate_request(GetProjectSnapshotsRequest, request)

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
        return _validate_response(SnapshotsResponse, response)

    async def get_project_public_ips(
        self,
        request: GetProjectPublicIpsRequest | None = None,
    ) -> PublicIpsResponse:
        request = _validate_request(GetProjectPublicIpsRequest, request)

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
        return _validate_response(PublicIpsResponse, response)

    async def get_project_nets(
        self,
        request: GetProjectNetsRequest | None = None,
    ) -> NetsResponse:
        request = _validate_request(GetProjectNetsRequest, request)

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
        return _validate_response(NetsResponse, response)

    async def list_clusters_by_project_id(
        self,
        request: ListClustersByProjectIDRequest | None = None,
    ) -> ClusterResponseList:
        request = _validate_request(ListClustersByProjectIDRequest, request)

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
        return _validate_response(ClusterResponseList, response)

    async def create_cluster(
        self,
        request: CreateClusterRequest | None = None,
    ) -> ClusterResponse:
        request = _validate_request(CreateClusterRequest, request)

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
        return _validate_response(ClusterResponse, response)

    async def list_all_clusters(
        self,
        request: ListAllClustersRequest | None = None,
    ) -> ClusterResponseList:
        request = _validate_request(ListAllClustersRequest, request)

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
        return _validate_response(ClusterResponseList, response)

    async def get_cluster(
        self,
        request: GetClusterRequest | None = None,
    ) -> ClusterResponse:
        request = _validate_request(GetClusterRequest, request)

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
        return _validate_response(ClusterResponse, response)

    async def update_cluster(
        self,
        request: UpdateClusterRequest | None = None,
    ) -> ClusterResponse:
        request = _validate_request(UpdateClusterRequest, request)

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
        return _validate_response(ClusterResponse, response)

    async def delete_cluster(
        self,
        request: DeleteClusterRequest | None = None,
    ) -> DetailResponse:
        request = _validate_request(DeleteClusterRequest, request)

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
        return _validate_response(DetailResponse, response)

    async def get_kubeconfig(
        self,
        request: GetKubeconfigRequest | None = None,
    ) -> KubeconfigResponse:
        request = _validate_request(GetKubeconfigRequest, request)

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
        return _validate_response(KubeconfigResponse, response)

    async def get_kubeconfig_with_pubkey_nacl(
        self,
        request: GetKubeconfigWithPubkeyNACLRequest | None = None,
    ) -> KubeconfigResponse:
        request = _validate_request(GetKubeconfigWithPubkeyNACLRequest, request)

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
        return _validate_response(KubeconfigResponse, response)

    async def upgrade_cluster(
        self,
        request: UpgradeClusterRequest | None = None,
    ) -> ClusterResponse:
        request = _validate_request(UpgradeClusterRequest, request)

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
        return _validate_response(ClusterResponse, response)

    async def get_kubernetes_versions(
        self,
        request: GetKubernetesVersionsRequest | None = None,
    ) -> KubernetesVersionsResponse:
        _ = request

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
        return _validate_response(KubernetesVersionsResponse, response)

    async def get_cp_subregions(
        self,
        request: GetCPSubregionsRequest | None = None,
    ) -> CPSubregionsResponse:
        _ = request

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
        return _validate_response(CPSubregionsResponse, response)

    async def get_control_plane_plans(
        self,
        request: GetControlPlanePlansRequest | None = None,
    ) -> ControlPlanesResponse:
        _ = request

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
        return _validate_response(ControlPlanesResponse, response)

    async def get_project_template(
        self,
        request: GetProjectTemplateRequest | None = None,
    ) -> TemplateResponse_ProjectInput:
        _ = request

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
        return _validate_response(TemplateResponse_ProjectInput, response)

    async def get_cluster_template(
        self,
        request: GetClusterTemplateRequest | None = None,
    ) -> TemplateResponse_ClusterInputTemplate:
        _ = request

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
        return _validate_response(TemplateResponse_ClusterInputTemplate, response)

    async def get_nodepool_template(
        self,
        request: GetNodepoolTemplateRequest | None = None,
    ) -> TemplateResponse_Nodepool:
        _ = request

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
        return _validate_response(TemplateResponse_Nodepool, response)

    async def get_net_peering_request_template(
        self,
        request: GetNetPeeringRequestTemplateRequest | None = None,
    ) -> TemplateResponse_NetPeeringRequest:
        _ = request

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
        return _validate_response(TemplateResponse_NetPeeringRequest, response)

    async def get_net_peering_acceptance_template(
        self,
        request: GetNetPeeringAcceptanceTemplateRequest | None = None,
    ) -> TemplateResponse_NetPeeringAcceptance:
        _ = request

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
        return _validate_response(TemplateResponse_NetPeeringAcceptance, response)

    async def get_quotas(
        self,
        request: GetQuotasRequest | None = None,
    ) -> quotas__quota_schema__QuotasResponse:
        _ = request

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
        return _validate_response(quotas__quota_schema__QuotasResponse, response)

    async def get_client_ip(
        self,
        request: GetClientIPRequest | None = None,
    ) -> IPResponse:
        _ = request

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
        return _validate_response(IPResponse, response)
