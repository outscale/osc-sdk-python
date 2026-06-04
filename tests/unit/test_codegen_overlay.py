from pathlib import Path
import shutil
from uuid import uuid4

from osc_sdk_python.codegen.overlay import apply_overlay, load_spec


def test_overlay_updates_wildcard_schema_property():
    spec = {
        "components": {
            "schemas": {
                "Vm": {
                    "type": "object",
                    "properties": {
                        "State": {"type": "string"},
                    },
                }
            }
        }
    }
    overlay = {
        "actions": [
            {
                "target": "$.components.schemas.Vm.*.State",
                "update": {"enum": ["pending", "running"]},
            }
        ]
    }

    patched = apply_overlay(spec, overlay)

    assert patched["components"]["schemas"]["Vm"]["properties"]["State"]["enum"] == [
        "pending",
        "running",
    ]


def test_overlay_removes_targeted_key():
    spec = {
        "components": {
            "schemas": {
                "ReadVmsRequest": {
                    "properties": {
                        "NextPageToken": {"type": "string", "format": "uuid"},
                    }
                }
            }
        }
    }
    overlay = {
        "actions": [
            {
                "target": "$.components.schemas.*.*.NextPageToken.format",
                "remove": True,
            }
        ]
    }

    patched = apply_overlay(spec, overlay)

    assert "format" not in patched["components"]["schemas"]["ReadVmsRequest"][
        "properties"
    ]["NextPageToken"]


def test_overlay_updates_quoted_path_key():
    spec = {
        "paths": {
            "/DeleteSecurityGroup": {
                "post": {
                    "responses": {},
                }
            }
        }
    }
    overlay = {
        "actions": [
            {
                "target": '$.paths["/DeleteSecurityGroup"].post.responses',
                "update": {"409": {"description": "Conflict"}},
            }
        ]
    }

    patched = apply_overlay(spec, overlay)

    assert patched["paths"]["/DeleteSecurityGroup"]["post"]["responses"]["409"] == {
        "description": "Conflict"
    }


def test_overlay_filters_matching_children():
    spec = {
        "components": {
            "schemas": {
                "CreateVmsRequest": {
                    "properties": {
                        "Nics": {"type": "array"},
                        "ImageId": {"type": "string"},
                    }
                }
            }
        }
    }
    overlay = {
        "actions": [
            {
                "target": "$.components.schemas.CreateVmsRequest.*.*[?(@.type == 'array')]",
                "update": {"x-rs-type-skip-optional-pointer": True},
            }
        ]
    }

    patched = apply_overlay(spec, overlay)

    assert patched["components"]["schemas"]["CreateVmsRequest"]["properties"]["Nics"][
        "x-rs-type-skip-optional-pointer"
    ]
    assert "x-rs-type-skip-optional-pointer" not in patched["components"]["schemas"][
        "CreateVmsRequest"
    ]["properties"]["ImageId"]


def test_cfg_loads_spec_and_applies_overlay():
    tmp_path = Path("tests/unit") / f".overlay-{uuid4().hex}"
    tmp_path.mkdir()
    try:
        (tmp_path / "api.yaml").write_text(
            """
components:
  schemas:
    Vm:
      type: object
      properties:
        State:
          type: string
"""
        )
        (tmp_path / "patch.yaml").write_text(
            """
actions:
  - target: $.components.schemas.Vm.*.State
    update:
      enum:
        - pending
"""
        )
        cfg = tmp_path / "cfg.yaml"
        cfg.write_text(
            """
spec: ./api.yaml
overlay: ./patch.yaml
"""
        )

        spec = load_spec(cfg)

        assert spec["components"]["schemas"]["Vm"]["properties"]["State"]["enum"] == [
            "pending"
        ]
    finally:
        shutil.rmtree(tmp_path, ignore_errors=True)
