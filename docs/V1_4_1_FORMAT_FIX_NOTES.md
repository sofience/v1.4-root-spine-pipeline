# v1.4.1 Format Fix Notes

## Purpose

This patch fixes AI-readable serialization problems in the v1.4 root-spine pipeline repository.

## What was fixed

- Restored real LF line breaks in Markdown files.
- Restored block-style YAML for routing and pipeline files.
- Restored JSON pretty-printing for index files.
- Added `.gitattributes` to normalize line endings.
- Added `.editorconfig` to prevent future line-ending drift.
- Added validation script for AI-readable format checks.
- Renamed checksum scope to patch checksums.

## Core route preserved

```text
01 -> 03 -> 47 -> 62
```

## Operational diagnostic route preserved

```text
47 -> 62 -> 39 -> 65 -> 64 -> 56
```

## Apply rule

This patch changes routing, pipeline, index, and format-control files.

Do not remove existing package folders.
