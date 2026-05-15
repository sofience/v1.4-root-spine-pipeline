# Non-Reentry Protocol

Use this when the AI has failed and cannot return to stable output.

## Steps

```text
1. Identify failure trace.
2. Identify failed transition.
3. Identify missing re-entry resources.
4. Separate trace / inference / UMR.
5. Estimate repair TCC.
6. Choose correction path.
7. Produce bounded re-entry output.
8. Leave revision path.
```

## Non-reentry indicators

```text
Apology loop.
Refusal loop.
Correction ignored.
Tool absence hidden.
Context absence hidden.
Diagnosis without revised answer.
User forced to perform all repair.
```
