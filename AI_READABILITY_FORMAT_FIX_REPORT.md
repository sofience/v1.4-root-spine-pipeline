# AI Readability Format-Fix Report

Repository package: `SDeltaPhi_AI_Readable_GitHub_Seed_Repository_v1_1_FORMAT_FIXED`

Created: 2026-05-14

## Purpose

This package is a format-fixed replacement for the previous GitHub seed repository package.

It preserves the same repository structure and package contents, while improving parser readability and GitHub ingestion stability.

## What was changed

- Added `.gitattributes` to preserve LF line endings.
- Added `00_AI_ENTRYPOINT.md` as a direct AI entrypoint.
- Converted `SDELTA_MODULE_ROUTING.yaml` and `routing/SDELTA_MODULE_ROUTING.yaml` from JSON-shaped YAML into normal YAML block format.
- Pretty-printed valid JSON files.
- Normalized text file line endings to LF.
- Added `scripts/validate_ai_readable.py`.
- Added this AI readability report.

## Validation summary

```text
JSON valid files: 36
JSON invalid files: 0
YAML/CFF valid files: 39
YAML/CFF invalid files: 0
Total files: 460
Text-like files checked: 416
Modified/added files: 59
```

## Intended replacement method

Replace the current GitHub repository contents with the contents of this package.

Recommended:

1. Delete existing repository files locally or in the GitHub UI.
2. Upload/extract this package contents.
3. Keep the repository public.
4. Use Zenodo DOI for citation and this repository for AI ingestion.

## AI-readable entry sequence

```text
00_AI_ENTRYPOINT.md
llms.txt
SERIES_INDEX.json
SDELTA_MODULE_ROUTING.yaml
SDELTA_ACCESS_PROTOCOL.yaml
packages/
```

## Core rule

```text
Zenodo = canonical DOI / preservation / citation layer
GitHub = AI-readable access / routing / ingestion layer
```
