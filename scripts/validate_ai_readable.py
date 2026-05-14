\
#!/usr/bin/env python3
from pathlib import Path
import json
import sys

try:
    import yaml
except Exception:
    yaml = None

root = Path(__file__).resolve().parents[1]
errors = []

for p in root.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"JSON invalid: {p.relative_to(root)} :: {e}")

if yaml:
    for ext in ("*.yaml", "*.yml", "*.cff"):
        for p in root.rglob(ext):
            try:
                yaml.safe_load(p.read_text(encoding="utf-8"))
            except Exception as e:
                errors.append(f"YAML/CFF invalid: {p.relative_to(root)} :: {e}")
else:
    print("PyYAML not installed; skipping YAML validation.")

for p in list(root.rglob("*.md")) + list(root.rglob("*.txt")):
    try:
        txt = p.read_text(encoding="utf-8")
    except Exception:
        continue
    if "\r\n" in txt or "\r" in txt:
        errors.append(f"Non-LF line ending: {p.relative_to(root)}")

if errors:
    print("AI-readability validation failed:")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("AI-readability validation passed.")
