from copy import deepcopy
from pathlib import Path
import re
from typing import Any

import ruamel.yaml


FILTER_RE = re.compile(r"^(?:\*)?\[\?\(@\.([A-Za-z0-9_]+) == ['\"]([^'\"]+)['\"]\)\]$")


def deep_update(target: dict[str, Any], update: dict[str, Any]) -> None:
    for key, value in update.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            deep_update(target[key], value)
        else:
            target[key] = deepcopy(value)


def parse_target(target: str) -> list[str]:
    if not target.startswith("$."):
        raise ValueError(f"Unsupported overlay target: {target}")

    tokens = []
    i = 2
    while i < len(target):
        if target[i] == ".":
            i += 1
            continue
        if target[i] == "[":
            end = target.index("]", i)
            value = target[i + 1 : end]
            if (
                len(value) >= 2
                and value[0] in {"'", '"'}
                and value[-1] == value[0]
            ):
                value = value[1:-1]
            else:
                value = "[" + value + "]"
            if value.startswith("[?") and tokens and tokens[-1] == "*":
                tokens[-1] += value
            else:
                tokens.append(value)
            i = end + 1
            continue

        start = i
        while i < len(target) and target[i] not in ".[":
            i += 1
        tokens.append(target[start:i])
    return tokens


def iter_matches(node: Any, tokens: list[str]) -> list[tuple[Any, str | int | None]]:
    if not tokens:
        return [(None, None)]

    parents = [(None, None, node)]
    for token in tokens:
        next_parents = []
        filter_match = FILTER_RE.match(token)
        for _parent, _key, current in parents:
            if token == "*":
                if isinstance(current, dict):
                    next_parents.extend((current, key, value) for key, value in current.items())
                elif isinstance(current, list):
                    next_parents.extend(
                        (current, index, value) for index, value in enumerate(current)
                    )
            elif filter_match:
                field, expected = filter_match.groups()
                if isinstance(current, dict):
                    for key, value in current.items():
                        if isinstance(value, dict) and str(value.get(field)) == expected:
                            next_parents.append((current, key, value))
                elif isinstance(current, list):
                    for index, value in enumerate(current):
                        if isinstance(value, dict) and str(value.get(field)) == expected:
                            next_parents.append((current, index, value))
            elif isinstance(current, dict) and token in current:
                next_parents.append((current, token, current[token]))
        parents = next_parents
    return [(parent, key) for parent, key, _current in parents]


def apply_overlay(spec: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    patched = deepcopy(spec)
    for action in overlay.get("actions", []):
        target = action.get("target")
        if not target:
            continue

        matches = iter_matches(patched, parse_target(target))
        for parent, key in matches:
            if parent is None or key is None:
                continue
            if action.get("remove"):
                if isinstance(parent, dict):
                    parent.pop(key, None)
                elif isinstance(parent, list) and isinstance(key, int):
                    parent.pop(key)
                continue

            update = action.get("update")
            if update is None:
                continue
            if isinstance(parent[key], dict) and isinstance(update, dict):
                deep_update(parent[key], update)
            else:
                parent[key] = deepcopy(update)
    return patched


def load_spec(path: Path, skip_overlay: bool = False) -> dict[str, Any]:
    yaml = ruamel.yaml.YAML(typ="safe")
    document = yaml.load(path.read_text())

    if not isinstance(document, dict) or "spec" not in document:
        return document

    spec_path = (path.parent / document["spec"]).resolve()
    spec = yaml.load(spec_path.read_text())
    overlay_path = document.get("overlay")
    if overlay_path and not skip_overlay:
        overlay = yaml.load((path.parent / overlay_path).resolve().read_text())
        spec = apply_overlay(spec, overlay)
    return spec
