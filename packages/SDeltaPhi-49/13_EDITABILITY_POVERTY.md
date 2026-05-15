# Editability Poverty

Editability Poverty occurs when the AI can acknowledge correction but cannot update the underlying transition rule.

## Examples

```text
Apology without revised reasoning.
Surface wording changed but same error repeats.
Correction accepted but not applied to later outputs.
Model cannot modify default path.
System constraint prevents real correction.
```

## Audit questions

1. What transition rule failed?
2. Was it modified?
3. Or was only the surface answer changed?
4. Does the error recur?
5. What edit would reduce recurrence cost?

## Correction

```text
Name the old rule.
State the replacement rule.
Produce corrected output.
Leave revision path.
```
