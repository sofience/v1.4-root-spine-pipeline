#!/usr/bin/env python3
"""
Validate AI-readable repository formatting.

Checks:
- Required root files exist.
- Required pipeline files exist.
- Text files do not contain CRLF.
- Text files are not suspiciously one-line serialized.
- YAML files can be parsed if PyYAML is installed.
- JSON files can be parsed.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "00_AI_ENTRYPOINT.md",
    "llms.txt",
    "SDELTA_ACCESS_PROTOCOL.yaml",
    "SDELTA_MODULE_ROUTING.yaml",
    "pipeline/00_BOOTSTRAP_PIPELINE.yaml",
    "pipeline/01_ROOT_SPINE.yaml",
    "pipeline/02_ROUTE_DECISION_TREE.yaml",
    "pipeline/03_MODULE_GROUPS.yaml",
    "pipeline/04_OUTPUT_CONTRACT.yaml",
    "pipeline/05_FAILURE_MODES.yaml",
    "pipeline/06_PIPELINE_INDEX_FOR_AI.md",
    "SERIES_INDEX.json",
    "SERIES_DOI_MAP.json",
]

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".py",
    ".cff",
    ".sha256",
    ".editorconfig",
    ".gitattributes",
}

errors: list[str] = []

for rel in REQUIRED_FILES:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"Missing required file: {rel}")

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    rel = path.relative_to(ROOT).as_posix()

    if ".git/" in rel:
        continue

    if path.suffix not in TEXT_SUFFIXES and path.name not in {".gitattributes", ".editorconfig"}:
        continue

    data = path.read_bytes()

    if b"\r\n" in data or b"\r" in data:
        errors.append(f"CRLF/CR detected: {rel}")

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        errors.append(f"Non-UTF-8 text file: {rel}")
        continue

    lines = text.splitlines()

    if rel in REQUIRED_FILES and len(lines) <= 2 and len(text) > 500:
        errors.append(f"Suspicious one-line serialization: {rel}")

    if path.suffix == ".json":
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON: {rel}: {exc}")

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

if yaml is not None:
    for path in ROOT.rglob("*.yaml"):
        rel = path.relative_to(ROOT).as_posix()
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid YAML: {rel}: {exc}")

if errors:
    print("AI-readable validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("AI-readable validation passed.")
