import pytest

from osc_sdk_python.runtime.request import RequestSpec


def test_resolved_path_replaces_and_quotes_path_parameters():
    spec = RequestSpec(service="oks", method="GET", path="/projects/{project_id}")

    assert spec.resolved_path({"project_id": "project/one"}) == "/projects/project%2Fone"


def test_resolved_path_raises_when_path_parameter_is_missing():
    spec = RequestSpec(
        service="oks",
        method="GET",
        path="/projects/{project_id}/clusters/{cluster_id}",
    )

    with pytest.raises(
        ValueError,
        match="Missing path parameter\\(s\\): cluster_id, project_id",
    ):
        spec.resolved_path()
