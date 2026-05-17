# Patch Apply Guide

This ZIP contains replacement/additive files for converting the repository to the v1.4 root-spine pipeline.

## Replace these root files

Copy these files to the repository root and overwrite the existing files:

```text
README.md
00_AI_ENTRYPOINT.md
llms.txt
SDELTA_MODULE_ROUTING.yaml
SDELTA_ACCESS_PROTOCOL.yaml
```

## Add these directories/files

Copy these new directories/files into the repository:

```text
pipeline/
indexes/PIPELINE_INDEX_FOR_AI.md
indexes/ROOT_SPINE_MODULE_MAP.json
routing/SDELTA_PIPELINE_ROUTING_v1_4.yaml
docs/V1_4_ROOT_SPINE_PIPELINE_NOTES.md
CHANGELOG_v1_4_ROOT_SPINE.md
```

## Suggested commit message

```text
Add v1.4 root-spine pipeline with SDeltaPhi-01 and SDeltaPhi-03
```

## Minimal validation

After applying, check that these routes appear:

```text
01 -> 03 -> 47 -> 62
47 -> 62 -> 39 -> 65 -> 64 -> 56
01 -> 03 -> 26 -> 56 -> 62
```

## Rule

Do not remove existing package folders.  
This patch changes routing and pipeline files, not canonical package contents.
