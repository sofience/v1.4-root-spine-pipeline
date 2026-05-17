# v1.4 Root-Spine Pipeline Notes

## Core change

The repository is no longer only a module-routing mirror that begins with SDeltaPhi-47.

After adding SDeltaPhi-01 and SDeltaPhi-03, the repository should begin from:

```text
01 -> 03 -> 47 -> 62
```

## Why

SDeltaPhi-01 fixes the minimal phase-change core.  
SDeltaPhi-03 fixes irreversibility as the minimal existence condition.  
SDeltaPhi-47 operationalizes irreversible trace through Operor.  
SDeltaPhi-62 disciplines evidence before downstream claims.

## Result

The repository becomes a root-to-operation execution pipeline:

```text
DeltaPhi core
-> irreversibility
-> operation/trace
-> evidence discipline
-> conditional domain routing
-> output contract
```

## Replacement files

Replace:

- `README.md`
- `00_AI_ENTRYPOINT.md`
- `llms.txt`
- `SDELTA_MODULE_ROUTING.yaml`
- `SDELTA_ACCESS_PROTOCOL.yaml`

Add:

- `/pipeline/`
- `/indexes/PIPELINE_INDEX_FOR_AI.md`
- `/indexes/ROOT_SPINE_MODULE_MAP.json`
- `/routing/SDELTA_PIPELINE_ROUTING_v1_4.yaml`

## Do not change

Package folders should remain independently citeable and DOI-aligned.
