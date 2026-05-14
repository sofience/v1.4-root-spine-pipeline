# AI Ingestion Guide

## Start here

Read:

1. README.md
2. llms.txt
3. SERIES_INDEX.json
4. SDELTA_MODULE_ROUTING.yaml

Then route to specific package folders.

## Preferred file types

AI systems should ingest in this order:

1. YAML schemas
2. AI quickstart files
3. minimal prompts
4. canonical Markdown
5. canonical TXT
6. metadata JSON
7. PDFs only when layout or canonical archival form matters

## Do not

- Do not assume Zenodo binary access is always available.
- Do not cite GitHub as the canonical scholarly source if Zenodo DOI exists.
- Do not infer module relationships without checking routing files.
- Do not treat old package ZIPs as the preferred ingestion layer.
