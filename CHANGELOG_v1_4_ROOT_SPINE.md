# Changelog — v1.4 Root-Spine Pipeline

Date: 2026-05-17

## Added

- SDeltaPhi-01 as root minimal phase-change core.
- SDeltaPhi-03 as root irreversibility axiom layer.
- `/pipeline/` execution pipeline.
- Root route: `01 -> 03 -> 47 -> 62`.
- Restoration/irreversibility route: `01 -> 03 -> 26 -> 56 -> 62`.
- Root spine map under `/indexes/ROOT_SPINE_MODULE_MAP.json`.

## Changed

- Minimal AI boot route changed from:

```text
47 -> 62 -> 39 -> 65 -> 64 -> 56
```

to:

```text
01 -> 03 -> 47 -> 62
```

- The old route is preserved as the operational diagnostic route.

## Preserved

- Zenodo remains the canonical citation layer.
- GitHub remains the AI-readable ingestion/routing layer.
- SDeltaPhi-56 remains a downstream cost underlayer, not a root definition.
