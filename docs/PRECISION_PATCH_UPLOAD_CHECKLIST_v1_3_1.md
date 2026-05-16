# Precision Patch v1.3.1 Upload Checklist

Replace these files:

```text
SERIES_INDEX.json
SERIES_DOI_MAP.json
indexes/SERIES_INDEX.json
indexes/SERIES_DOI_MAP.json
docs/PRECISION_PATCH_v1_3_1_REPOSITORY_ARCHIVE_PATHS.md
```

After upload, verify:

```text
1. Root SERIES_INDEX.json repository == SDeltaPhi_AI_Readable_GitHub_Seed_Repository_v1_3
2. indexes/SERIES_INDEX.json matches root SERIES_INDEX.json
3. Root SERIES_DOI_MAP.json repository == SDeltaPhi_AI_Readable_GitHub_Seed_Repository_v1_3
4. indexes/SERIES_DOI_MAP.json matches root SERIES_DOI_MAP.json
5. SERIES_DOI_MAP.json uses exact long archive filenames, not short placeholders
6. SDeltaPhi-48, SDeltaPhi-49, SDeltaPhi-56 do not contain false archive paths unless their archives are later uploaded
```
