# Patch Apply Guide — v1.4.1 Format Fix

## Replace these root files

Copy these files to the repository root and overwrite existing files:

```text
README.md
00_AI_ENTRYPOINT.md
llms.txt
SDELTA_ACCESS_PROTOCOL.yaml
SDELTA_MODULE_ROUTING.yaml
SERIES_INDEX.json
SERIES_DOI_MAP.json
```

## Add or replace these control files

```text
.gitattributes
.editorconfig
scripts/validate_ai_readable.py
```

## Add or replace these directories/files

```text
pipeline/
indexes/PIPELINE_INDEX_FOR_AI.md
indexes/ROOT_SPINE_MODULE_MAP.json
routing/SDELTA_PIPELINE_ROUTING_v1_4_1.yaml
docs/V1_4_1_FORMAT_FIX_NOTES.md
CHANGELOG_v1_4_1_FORMAT_FIX.md
PATCH_CHECKSUMS.sha256
```

## Suggested commit message

```text
Fix v1.4 root-spine pipeline formatting for AI-readable ingestion
```

## Minimal validation

After applying, run:

```bash
python scripts/validate_ai_readable.py
```

Expected result:

```text
AI-readable validation passed.
```

## Do not change

Do not remove existing package folders.

This patch fixes routing, pipeline, index, and serialization files.
