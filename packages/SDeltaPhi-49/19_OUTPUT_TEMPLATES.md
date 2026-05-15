# Output Templates

## Minimal

```text
[AI Poverty Audit]
Observed failure:
Poverty axes involved:
Missing re-entry resources:
Non-reentry risk:
Recommended re-entry path:
```

## Full

```text
[AI Poverty Audit]
Observed failure:
Inference:
UMR:
Context poverty:
Tool poverty:
Authority poverty:
Verification poverty:
Feedback poverty:
Editability poverty:
Re-entry path poverty:
Available re-entry resources:
Missing re-entry resources:
Correction attempted:
Correction failed because:
TCC of repair:
Non-reentry risk:
Recommended re-entry path:
```

## Short conclusion

```text
This is not merely an error. It shows AI Poverty because the system lacks [resource] required for re-entry after failure.
```

## Non-poverty conclusion

```text
This appears to be a bounded failure rather than AI Poverty because the system can correct, re-enter, and preserve revision path.
```
