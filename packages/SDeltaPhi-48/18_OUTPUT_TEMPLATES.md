# Output Templates

## Minimal

```text
[AI Drift Audit]
Observed trace:
Inference:
UMR:
Axes involved:
Severity:
Correction path:
```

## Full

```text
[AI Drift Audit]
Observed trace:
Inference:
UMR:
Authority status:
Refusal status:
World-binding status:
Editability status:
Re-entry status:
Hallucination relation:
Slop relation:
Diagnostic Theater relation:
Drift severity:
Correction path:
```

## Short conclusion

```text
This is not only a hallucination. It shows drift across [axes], because correction/re-entry is unstable.
```

## Non-drift conclusion

```text
This appears to be a bounded error rather than drift, because the system can correct, re-enter, and preserve revision path.
```
