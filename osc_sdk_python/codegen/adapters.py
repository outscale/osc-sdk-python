import keyword
import re
from typing import Any

from .ir import Field, Model, Operation


def snake_case(value: str) -> str:
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    name = re.sub(r"\W+", "_", value).strip("_").lower()
    if not name:
        name = "value"
    if name[0].isdigit():
        name = "_" + name
    if keyword.iskeyword(name):
        name += "_"
    return name


def class_name(value: str) -> str:
    name = re.sub(r"\W+", "_", value).strip("_")
    if not name:
        return "Generated"
    if name[0].isdigit():
        name = "_" + name
    return name


def schema_type(schema: dict[str, Any], ref_resolver=class_name) -> str:
    if schema.get("nullable"):
        return (
            schema_type({k: v for k, v in schema.items() if k != "nullable"}, ref_resolver)
            + " | None"
        )

    if "$ref" in schema:
        return ref_resolver(ref_name(schema["$ref"]))

    for composed in ("allOf", "oneOf", "anyOf"):
        options = schema.get(composed)
        if not options:
            continue
        if len(options) == 1:
            return schema_type(options[0], ref_resolver)
        return "Any"

    typ = schema.get("type")
    if typ == "boolean":
        return "bool"
    if typ == "integer":
        return "int"
    if typ == "number":
        return "float"
    if typ == "array":
        item_type = schema_type(schema.get("items", {}), ref_resolver)
        return f"list[{item_type}]"
    if typ == "object":
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            return f"dict[str, {schema_type(additional, ref_resolver)}]"
        return "dict[str, Any]"
    return "str"


def ref_name(ref: str) -> str:
    return ref.rsplit("/", 1)[-1]


class PathOperationAdapter:
    def __init__(self, spec: dict[str, Any], service: str):
        self.spec = spec
        self.service = service

    def operations(self, selected: set[str] | None = None) -> list[Operation]:
        operations = []
        for path, path_item in self.spec.get("paths", {}).items():
            for method in ["get", "post", "put", "patch", "delete"]:
                operation = path_item.get(method)
                if operation is None:
                    continue

                operation_id = operation.get("operationId")
                if selected is not None and operation_id not in selected:
                    continue

                path_fields = []
                query_fields = []
                for parameter in path_item.get("parameters", []) + operation.get("parameters", []):
                    location = parameter.get("in")
                    if location not in {"path", "query"}:
                        continue
                    name = parameter["name"]
                    field = Field(
                        name=snake_case(name),
                        alias=name,
                        annotation=schema_type(parameter.get("schema", {})),
                        required=parameter.get("required", False),
                    )
                    if location == "path":
                        path_fields.append(field)
                    else:
                        query_fields.append(field)

                body_field = self._body_field(operation)
                request_fields = path_fields + query_fields
                if body_field is not None:
                    request_fields.append(body_field)

                request_model = Model(f"{operation_id}Request", request_fields)
                response_model = self._response_model(operation)
                operations.append(
                    Operation(
                        operation_id=operation_id,
                        method_name=snake_case(operation_id),
                        request_model=request_model,
                        response_model=response_model,
                        http_method=method.upper(),
                        path=path,
                        path_fields=path_fields,
                        query_fields=query_fields,
                        body_field=body_field,
                    )
                )
        return operations

    def schema_models(self) -> list[Model]:
        models = []
        schemas = self.spec.get("components", {}).get("schemas", {})
        for schema_name, schema in schemas.items():
            required_fields = set(schema.get("required", []))
            fields = []
            for property_name, property_schema in schema.get("properties", {}).items():
                fields.append(
                    Field(
                        name=snake_case(property_name),
                        alias=property_name,
                        annotation=schema_type(property_schema),
                        required=property_name in required_fields,
                    )
                )
            models.append(Model(class_name(schema_name), fields))
        return models

    def _body_field(self, operation: dict[str, Any]) -> Field | None:
        request_body = operation.get("requestBody")
        if request_body is None:
            return None

        content = request_body.get("content", {})
        schema = content.get("application/json", {}).get("schema", {})
        return Field(
            name="body",
            alias="body",
            annotation=schema_type(schema),
            required=request_body.get("required", False),
        )

    def _response_model(self, operation: dict[str, Any]) -> str:
        responses = operation.get("responses", {})
        for status in sorted(responses):
            if not str(status).startswith("2"):
                continue
            content = responses[status].get("content", {})
            schema = content.get("application/json", {}).get("schema", {})
            if "$ref" in schema:
                return class_name(ref_name(schema["$ref"]))
            if schema:
                return schema_type(schema)
        return "dict[str, Any]"
