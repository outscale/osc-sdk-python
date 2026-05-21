from pathlib import Path
from typing import Iterable

import ruamel.yaml

from .adapters import PathOperationAdapter
from .ir import Field, Model, Operation


GENERATED_HEADER = '''"""Generated typed OKS client slice.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator
"""
'''


def _annotation(value: str, required: bool) -> str:
    if required or " | None" in value:
        return value
    return value + " | None"


def _field_args(required: bool, alias: str) -> str:
    if required:
        return f"alias={alias!r}"
    return f"default=None, alias={alias!r}"


def _render_model(model: Model) -> str:
    lines = [f"class {model.name}(GeneratedModel):"]
    if not model.fields:
        lines.append("    pass")
        return "\n".join(lines)

    for field in model.fields:
        lines.append(
            f"    {field.name}: {_annotation(field.annotation, field.required)} = Field({_field_args(field.required, field.alias)})"
        )
    return "\n".join(lines)


def render_models(operations: Iterable[Operation], schema_models: Iterable[Model]) -> str:
    models = [_render_model(model) for model in schema_models]
    models.extend(_render_model(operation.request_model) for operation in operations)
    return (
        GENERATED_HEADER
        + "from __future__ import annotations\n\n"
        + "from typing import Any\n\n"
        + "from pydantic import BaseModel, ConfigDict, Field\n\n\n"
        + "class GeneratedModel(BaseModel):\n"
        + "    model_config = ConfigDict(populate_by_name=True, extra=\"allow\")\n\n\n"
        + "\n\n".join(models)
        + "\n"
    )


def _field_dump(field: Field) -> str:
    return f"{field.alias!r}: request.{field.name}"


def render_async_client(operations: list[Operation]) -> str:
    imports = sorted(
        {operation.request_model.name for operation in operations}
        | {operation.response_model for operation in operations}
    )
    model_imports = "\n".join(f"    {name}," for name in imports)
    lines = [
        GENERATED_HEADER,
        "from typing import Any",
        "",
        "from osc_sdk_python.runtime.request import RequestSpec",
        "from .models import (",
        model_imports,
        ")",
        "",
        "",
        "def _dump_json_body(value: Any) -> Any:",
        "    if hasattr(value, \"model_dump\"):",
        "        return value.model_dump(exclude_none=True, by_alias=True)",
        "    return value",
        "",
        "",
        "class AsyncOksTypedMixin:",
    ]
    for operation in operations:
        json_body = (
            f"_dump_json_body(request.{operation.body_field.name})"
            if operation.body_field is not None
            else "None"
        )
        lines.extend(
            [
                f"    async def {operation.method_name}(",
                "        self,",
                f"        request: {operation.request_model.name} | None = None,",
                f"    ) -> {operation.response_model}:",
                "        if request is None:",
                f"            request = {operation.request_model.name}()",
                "",
                "        path_params = {",
            ]
        )
        lines.extend(f"            {_field_dump(field)}," for field in operation.path_fields)
        lines.extend(
            [
                "        }",
                "        query_params = {",
            ]
        )
        lines.extend(f"            {_field_dump(field)}," for field in operation.query_fields)
        lines.extend(
            [
                "        }",
                "        response = await self.call.request(",
                "            RequestSpec(",
                "                service=\"oks\",",
                f"                method=\"{operation.http_method}\",",
                f"                path=\"{operation.path}\",",
                f"                json_body={json_body},",
                "                query_params={",
                "                    key: value",
                "                    for key, value in query_params.items()",
                "                    if value is not None",
                "                },",
                "            ),",
                "            path_params=path_params,",
                "        )",
                f"        return {operation.response_model}.model_validate(response)",
                "",
            ]
        )
    return "\n".join(lines)


def render_init(operations: list[Operation], schema_models: list[Model]) -> str:
    model_names = sorted(
        {model.name for model in schema_models}
        | {operation.request_model.name for operation in operations}
    )
    lines = [
        "from .async_client import AsyncOksTypedMixin",
        "from .models import (",
    ]
    lines.extend(f"    {name}," for name in model_names)
    lines.extend(
        [
            ")",
            "",
            "__all__ = [",
            "    \"AsyncOksTypedMixin\",",
        ]
    )
    lines.extend(f"    {name!r}," for name in model_names)
    lines.append("]\n")
    return "\n".join(lines)


def generate(spec_path: Path, output_dir: Path) -> None:
    yaml = ruamel.yaml.YAML(typ="safe")
    spec = yaml.load(spec_path.read_text())
    adapter = PathOperationAdapter(spec, service="oks")
    operations = adapter.operations()
    schema_models = adapter.schema_models()

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "models.py").write_text(render_models(operations, schema_models))
    (output_dir / "async_client.py").write_text(render_async_client(operations))
    (output_dir / "__init__.py").write_text(render_init(operations, schema_models))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    generate(
        root / "resources" / "oks" / "api.yaml",
        root / "generated" / "oks",
    )


if __name__ == "__main__":
    main()
