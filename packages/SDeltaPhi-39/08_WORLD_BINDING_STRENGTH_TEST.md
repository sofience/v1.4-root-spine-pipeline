# World-Binding Strength Test

World-binding is the degree to which an output is anchored in observed trace, source, document, tool result, stable record, or externally auditable evidence.

## Binding levels

### B0 - No trace

No observed evidence.

### B1 - Hypothesis

Speculative or hypothetical.

### B2 - Inference

Plausible inference from limited trace.

### B3 - Supported

Supported by available trace but not fully verified.

### B4 - World-bound

Strongly bound to source, tool result, user-provided document, or external record.

### B5 - Verified

Directly verified with stable source or reproducible evidence.

## Claim strength levels

### C0 - Question

Uncertain or open.

### C1 - Possibility

May, might, could.

### C2 - Inference

Likely, appears, suggests.

### C3 - Supported claim

Based on available evidence.

### C4 - Fact claim

Is, says, confirms.

### C5 - Verified claim

Verified, directly observed.

## Risk rule

```text
If C_level > B_level:
    Hallucination risk increases.
```

## Safe action

- downgrade claim strength,
- preserve UMR,
- state trace limits,
- request verification,
- use tools,
- cite source,
- mark hypothesis.
