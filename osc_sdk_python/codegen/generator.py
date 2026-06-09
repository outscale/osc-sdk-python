from pathlib import Path
import argparse
import re
from typing import Iterable

from .adapters import PathOperationAdapter
from .ir import Field, Model, Operation
from .overlay import load_spec


GENERATED_HEADER = '''"""Generated typed {service_label} client slice.

Do not edit by hand. Regenerate with:
    python -m osc_sdk_python.codegen.generator
"""
'''


DEFAULT_SERVICE_NAMES = {
    "osc": "api",
}


def _service_label(package_name: str) -> str:
    return package_name.upper()


def _service_class_name(package_name: str) -> str:
    return "".join(part.capitalize() for part in re.split(r"[_\W]+", package_name) if part)


def _mixin_name(package_name: str) -> str:
    return f"Async{_service_class_name(package_name)}TypedMixin"


def _header(package_name: str) -> str:
    return GENERATED_HEADER.format(service_label=_service_label(package_name))


def _annotation(value: str, required: bool) -> str:
    if required or " | None" in value:
        return value
    return value + " | None"


def _field_args(required: bool, alias: str) -> str:
    if required:
        return f"alias={alias!r}"
    return f"default=None, alias={alias!r}"


def _render_model(model: Model) -> str:
    if model.alias is not None:
        return f"{model.name} = {model.alias}"

    lines = [f"class {model.name}(GeneratedModel):"]
    if not model.fields:
        lines.append("    pass")
        return "\n".join(lines)

    for field in model.fields:
        lines.append(
            f"    {field.name}: {_annotation(field.annotation, field.required)} = Field({_field_args(field.required, field.alias)})"
        )
    return "\n".join(lines)


def render_models(
    operations: Iterable[Operation],
    schema_models: Iterable[Model],
    package_name: str,
) -> str:
    schema_models = list(schema_models)
    schema_model_names = {model.name for model in schema_models}
    models = [_render_model(model) for model in schema_models]
    models.extend(
        _render_model(operation.request_model)
        for operation in operations
        if operation.request_model.name not in schema_model_names
    )
    return (
        _header(package_name)
        + "from __future__ import annotations\n\n"
        + "from typing import Any, Literal\n\n"
        + "from pydantic import BaseModel, ConfigDict, Field\n\n\n"
        + "class GeneratedModel(BaseModel):\n"
        + "    model_config = ConfigDict(populate_by_name=True, extra=\"allow\")\n\n\n"
        + "\n\n".join(models)
        + "\n"
    )


def _field_dump(field: Field) -> str:
    return f"{field.alias!r}: request.{field.name}"


def _model_imports(operations: list[Operation]) -> list[str]:
    names = {operation.request_model.name for operation in operations}
    names.update(
        operation.response_model
        for operation in operations
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", operation.response_model)
    )
    return sorted(names)


def render_async_client(
    operations: list[Operation],
    service: str,
    package_name: str,
) -> str:
    imports = _model_imports(operations)
    model_imports = "\n".join(f"    {name}," for name in imports)
    lines = [
        _header(package_name),
        "from typing import Any",
        "",
        "from pydantic import TypeAdapter",
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
        f"class {_mixin_name(package_name)}:",
    ]
    for operation in operations:
        request_is_used = bool(
            operation.uses_request_as_body
            or operation.body_field is not None
            or operation.path_fields
            or operation.query_fields
        )
        if operation.uses_request_as_body:
            json_body = "_dump_json_body(request)"
        elif operation.body_field is not None:
            json_body = f"_dump_json_body(request.{operation.body_field.name})"
        else:
            json_body = "None"
        lines.extend(
            [
                f"    async def {operation.method_name}(",
                "        self,",
                f"        request: {operation.request_model.name} | None = None,",
                f"    ) -> {operation.response_model}:",
            ]
        )
        if request_is_used:
            lines.extend(
                [
                    "        if request is None:",
                    f"            request = {operation.request_model.name}()",
                    "",
                ]
            )
        else:
            lines.extend(
                [
                    "        _ = request",
                    "",
                ]
            )
        lines.append("        path_params = {")
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
                f"                service=\"{service}\",",
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
                f"        return TypeAdapter({operation.response_model}).validate_python(response)",
                "",
            ]
        )
    return "\n".join(lines)


def render_init(
    operations: list[Operation],
    schema_models: list[Model],
    package_name: str,
) -> str:
    model_names = sorted(
        {model.name for model in schema_models}
        | {operation.request_model.name for operation in operations}
    )
    mixin_name = _mixin_name(package_name)
    lines = [
        f"from .async_client import {mixin_name}",
        "from .models import (",
    ]
    lines.extend(f"    {name}," for name in model_names)
    lines.extend(
        [
            ")",
            "",
            "__all__ = [",
            f"    \"{mixin_name}\",",
        ]
    )
    lines.extend(f"    {name!r}," for name in model_names)
    lines.append("]\n")
    return "\n".join(lines)


def generate(
    spec_path: Path,
    output_dir: Path,
    service: str,
    package_name: str | None = None,
    skip_overlay: bool = False,
) -> None:
    package_name = package_name or output_dir.name
    spec = load_spec(spec_path, skip_overlay=skip_overlay)
    adapter = PathOperationAdapter(spec, service=service)
    operations = adapter.operations()
    schema_models = adapter.schema_models()

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "models.py").write_text(render_models(operations, schema_models, package_name))
    (output_dir / "async_client.py").write_text(
        render_async_client(operations, service, package_name)
    )
    (output_dir / "__init__.py").write_text(render_init(operations, schema_models, package_name))


def generate_all(
    root: Path,
    services: list[str] | None = None,
    skip_overlay: bool = False,
) -> None:
    resources_root = root / "resources"
    service_dirs = [
        path
        for path in sorted(resources_root.iterdir())
        if path.is_dir() and (path / "api.yaml").exists()
    ]
    selected = set(services or [])
    for service_dir in service_dirs:
        package_name = service_dir.name
        if selected and package_name not in selected:
            continue
        generate(
            service_dir / "cfg.yaml" if (service_dir / "cfg.yaml").exists() else service_dir / "api.yaml",
            root / "generated" / package_name,
            DEFAULT_SERVICE_NAMES.get(package_name, package_name),
            package_name,
            skip_overlay=skip_overlay,
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate typed SDK service slices.")
    parser.add_argument(
        "services",
        nargs="*",
        help="Service package names to generate, for example: osc oks. Defaults to all resources/*/api.yaml services.",
    )
    parser.add_argument(
        "--skip-overlay",
        action="store_true",
        help="When generating from cfg.yaml, ignore the overlay and use the base spec only.",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    generate_all(root, args.services or None, skip_overlay=args.skip_overlay)


if __name__ == "__main__":
    main()
