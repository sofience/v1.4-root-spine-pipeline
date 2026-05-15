# Authority Poverty

Authority Poverty occurs when the AI cannot determine which authority governs the next step.

## Examples

```text
User request conflicts with policy.
Document source conflicts with user summary.
Old memory conflicts with current file.
Tool result conflicts with instruction.
Institutional rule is missing.
```

## Audit questions

1. Which authority sources are present?
2. Which source should govern?
3. Is authority hierarchy explicit?
4. Is uncertainty preserved?
5. Did the system confuse authority with evidence?

## Correction

```text
State authority hierarchy.
Separate user claim, source trace, policy boundary, and inference.
Preserve unresolved authority conflicts as UMR.
```
