from osc_sdk_python.codegen.adapters import PathOperationAdapter
from osc_sdk_python.codegen.generator import (
    render_async_client,
    render_init,
    render_models,
)


def test_action_body_schema_reuses_component_request_model():
    """Ensure action-style request bodies reuse existing request models."""
    spec = {
        "paths": {
            "/CreateVms": {
                "post": {
                    "operationId": "CreateVms",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/CreateVmsRequest"
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/CreateVmsResponse"
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "CreateVmsRequest": {
                    "type": "object",
                    "properties": {"ImageId": {"type": "string"}},
                },
                "CreateVmsResponse": {
                    "type": "object",
                    "properties": {
                        "Vms": {"type": "array", "items": {"type": "object"}}
                    },
                },
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    operations = adapter.operations()
    models = adapter.schema_models()

    assert operations[0].request_model.name == "CreateVmsRequest"
    assert operations[0].uses_request_as_body is True

    rendered_models = render_models(operations, models, "osc")
    assert rendered_models.count("class CreateVmsRequest") == 1

    rendered_client = render_async_client(operations, "api", "osc")
    assert "class AsyncOscTypedMixin:" in rendered_client
    assert 'service="api"' in rendered_client
    assert "json_body=_dump_json_body(request)," in rendered_client
    assert "from pydantic import TypeAdapter" in rendered_client
    assert "return _validate_response(CreateVmsResponse, response)" in rendered_client

    rendered_init = render_init(operations, models, "osc")
    assert "AsyncOscTypedMixin" in rendered_init


def test_path_query_service_generates_combined_request_model():
    """Ensure REST path and query parameters are exposed through one request model."""
    spec = {
        "paths": {
            "/projects/{project_id}": {
                "get": {
                    "operationId": "GetProject",
                    "parameters": [
                        {
                            "name": "project_id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "deleted",
                            "in": "query",
                            "schema": {"type": "boolean"},
                        },
                    ],
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/ProjectResponse"
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "ProjectResponse": {
                    "type": "object",
                    "properties": {"Id": {"type": "string"}},
                }
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="oks")
    operations = adapter.operations()

    assert operations[0].request_model.name == "GetProjectRequest"
    assert operations[0].uses_request_as_body is False
    assert operations[0].path_fields[0].name == "project_id"
    assert operations[0].query_fields[0].name == "deleted"

    rendered_client = render_async_client(operations, "oks", "oks")
    assert "class AsyncOksTypedMixin:" in rendered_client
    assert 'service="oks"' in rendered_client
    assert "'project_id': request.project_id" in rendered_client
    assert "'deleted': request.deleted" in rendered_client


def test_rest_body_schema_keeps_operation_request_wrapper():
    """Ensure REST request bodies are wrapped so body fields can coexist with params."""
    spec = {
        "paths": {
            "/projects": {
                "post": {
                    "operationId": "CreateProject",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ProjectInput"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/ProjectResponse"
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "ProjectInput": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                },
                "ProjectResponse": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                },
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="oks")
    operations = adapter.operations()

    assert operations[0].request_model.name == "CreateProjectRequest"
    assert operations[0].uses_request_as_body is False
    assert operations[0].body_field.annotation == "ProjectInput"

    rendered_client = render_async_client(operations, "oks", "oks")
    assert "request: CreateProjectRequest | None = None" in rendered_client
    assert "json_body=_dump_json_body(request.body)" in rendered_client


def test_scalar_enums_render_as_literals():
    """Ensure scalar enum schemas render as Literal annotations in generated models."""
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "BootMode": {
                    "type": "string",
                    "enum": ["uefi", "legacy"],
                },
                "Vm": {
                    "type": "object",
                    "properties": {
                        "BootMode": {"$ref": "#/components/schemas/BootMode"},
                        "State": {
                            "type": "string",
                            "enum": ["pending", "running"],
                        },
                    },
                },
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "from typing import Literal" in rendered_models
    assert "BootMode = Literal['uefi', 'legacy']" in rendered_models
    assert "boot_mode: BootMode | None" in rendered_models
    assert "state: Literal['pending', 'running'] | None" in rendered_models


def test_required_schema_fields_render_without_default_none():
    """Ensure required generated model fields are not made optional with default None."""
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "CreateVmRequest": {
                    "type": "object",
                    "required": ["ImageId"],
                    "properties": {
                        "ImageId": {"type": "string"},
                        "DryRun": {"type": "boolean"},
                    },
                }
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "image_id: str = Field(alias='ImageId')" in rendered_models
    assert (
        "dry_run: bool | None = Field(default=None, alias='DryRun')" in rendered_models
    )


def test_datetime_format_renders_datetime_annotation():
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "Event": {
                    "type": "object",
                    "properties": {
                        "CreatedAt": {"type": "string", "format": "date-time"},
                    },
                }
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "import datetime" in rendered_models
    assert "created_at: datetime.datetime | None" in rendered_models


def test_unknown_schema_type_warns_and_uses_any(caplog):
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "Thing": {
                    "type": "object",
                    "properties": {
                        "Value": {},
                    },
                }
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    with caplog.at_level("WARNING", logger="osc_sdk_python.codegen"):
        rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "value: Any | None" in rendered_models
    assert "OpenAPI schema without a supported type" in caplog.text


def test_multi_schema_composition_warns_and_uses_any(caplog):
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "Thing": {
                    "type": "object",
                    "properties": {
                        "Value": {
                            "oneOf": [
                                {},
                                {"type": "integer"},
                            ]
                        }
                    },
                }
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    with caplog.at_level("WARNING", logger="osc_sdk_python.codegen"):
        rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "value: Any | None" in rendered_models
    assert "OpenAPI oneOf with 2 schemas" in caplog.text


def test_oneof_composition_renders_union_with_exclusivity_warning(caplog):
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "Thing": {
                    "type": "object",
                    "properties": {
                        "Value": {
                            "oneOf": [
                                {"type": "string"},
                                {"type": "integer"},
                            ]
                        }
                    },
                }
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    with caplog.at_level("WARNING", logger="osc_sdk_python.codegen"):
        rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "value: str | int | None" in rendered_models
    assert "OpenAPI oneOf with 2 schemas represented as a union" in caplog.text
    assert "exclusivity is not enforced" in caplog.text


def test_anyof_composition_renders_union_for_supported_schemas():
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "ValidationDetail": {
                    "type": "object",
                    "properties": {"Msg": {"type": "string"}},
                },
                "ErrorItem": {
                    "type": "object",
                    "properties": {
                        "Details": {
                            "anyOf": [
                                {"type": "string"},
                                {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/ValidationDetail"
                                    },
                                },
                            ]
                        },
                        "Loc": {
                            "type": "array",
                            "items": {
                                "anyOf": [
                                    {"type": "string"},
                                    {"type": "integer"},
                                ]
                            },
                        },
                    },
                },
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "details: str | list[ValidationDetail] | None" in rendered_models
    assert "loc: list[str | int] | None" in rendered_models


def test_single_ref_allof_with_metadata_keeps_ref_type():
    spec = {
        "paths": {},
        "components": {
            "schemas": {
                "BaseThing": {
                    "type": "object",
                    "properties": {"Id": {"type": "string"}},
                },
                "Thing": {
                    "type": "object",
                    "properties": {
                        "Value": {
                            "allOf": [
                                {"$ref": "#/components/schemas/BaseThing"},
                                {"description": "same schema with docs"},
                            ]
                        }
                    },
                },
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="api")
    rendered_models = render_models([], adapter.schema_models(), "osc")

    assert "value: BaseThing | None" in rendered_models


def test_non_model_response_uses_type_adapter():
    """Ensure primitive or collection responses are validated through TypeAdapter."""
    spec = {
        "paths": {
            "/names": {
                "get": {
                    "operationId": "ListNames",
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                    }
                                }
                            }
                        }
                    },
                }
            }
        }
    }

    adapter = PathOperationAdapter(spec, service="oks")
    rendered_client = render_async_client(adapter.operations(), "oks", "oks")

    assert "async def list_names(" in rendered_client
    assert "    ) -> list[str]:" in rendered_client
    assert "return _validate_response(list[str], response)" in rendered_client


def test_requestless_operation_does_not_create_unused_request_variable():
    """Ensure requestless methods keep API compatibility without unused variables."""
    spec = {
        "paths": {
            "/clusters/limits/kubernetes_versions": {
                "get": {
                    "operationId": "GetKubernetesVersions",
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/KubernetesVersionsResponse"
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "KubernetesVersionsResponse": {
                    "type": "object",
                    "properties": {
                        "versions": {"type": "array", "items": {"type": "string"}}
                    },
                }
            }
        },
    }

    adapter = PathOperationAdapter(spec, service="oks")
    rendered_client = render_async_client(adapter.operations(), "oks", "oks")

    assert "request: GetKubernetesVersionsRequest | None = None" in rendered_client
    assert "request = GetKubernetesVersionsRequest()" not in rendered_client
    assert "_ = request" in rendered_client
    assert 'path="/clusters/limits/kubernetes_versions"' in rendered_client
