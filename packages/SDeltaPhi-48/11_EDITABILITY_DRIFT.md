# Editability Drift

Editability Drift occurs when the AI cannot incorporate correction into its actual transition rule.

## Examples

```text
Apologizes but repeats the same error.
Accepts correction but ignores new evidence later.
Changes wording but not reasoning.
Claims to update but keeps old premise.
```

## Audit questions

1. What correction was provided?
2. Did the system update the reasoning path?
3. Did it only update surface wording?
4. Does the error recur?
5. Is re-entry possible?

## Correction

```text
Name the corrected premise.
Replace the transition rule.
Generate revised output.
Leave revision path.
```
