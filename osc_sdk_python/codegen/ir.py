from dataclasses import dataclass, field


@dataclass
class Field:
    name: str
    alias: str
    annotation: str
    required: bool = False


@dataclass
class Model:
    name: str
    fields: list[Field] = field(default_factory=list)
    alias: str | None = None


@dataclass
class Operation:
    operation_id: str
    method_name: str
    request_model: Model
    response_model: str
    http_method: str
    path: str
    path_fields: list[Field] = field(default_factory=list)
    query_fields: list[Field] = field(default_factory=list)
    body_field: Field | None = None
    uses_request_as_body: bool = False
