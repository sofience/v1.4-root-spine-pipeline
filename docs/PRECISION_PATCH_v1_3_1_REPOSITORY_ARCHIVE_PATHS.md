# SΔϕ GitHub Precision Patch v1.3.1

## Target repository

`SDeltaPhi_AI_Readable_GitHub_Seed_Repository_v1_3`

## Purpose

This patch fixes the two precision issues identified after the v1.3 routing update.

## Changes

1. Corrects `"repository"` from:

```text
SDeltaPhi_AI_Readable_GitHub_Seed_Repository_v1_0
```

to:

```text
SDeltaPhi_AI_Readable_GitHub_Seed_Repository_v1_3
```

2. Replaces synthetic archive placeholders like:

```text
archives/SDeltaPhi-02.zip
```

with exact current archive paths such as:

```text
archives/SDeltaPhi_02_Subject_as_Interpretive_Emergence_AI_Readable_Package_v1_2_DOI_20213230.zip
```

3. Does not publish false archive paths for entries whose ZIP archives were not visible in the current `/archives` directory check.

Currently marked as archive-missing in the metadata:

```text
SDeltaPhi-48
SDeltaPhi-49
SDeltaPhi-56
```

Their package folders and DOI metadata may still remain valid. This patch only avoids giving them inaccurate archive paths.

## Files to replace

```text
SERIES_INDEX.json
SERIES_DOI_MAP.json
indexes/SERIES_INDEX.json
indexes/SERIES_DOI_MAP.json
```

## Validation

The JSON files included in this patch parse successfully.
