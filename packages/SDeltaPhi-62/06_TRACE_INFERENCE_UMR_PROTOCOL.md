# Trace / Inference / UMR Protocol

This protocol is the basic SΔϕ-62 kernel split.

## 1. Observed Trace

Observed trace includes:

- user-provided text,
- uploaded files,
- quoted passages,
- screenshots,
- logs,
- measurements,
- records,
- verified sources,
- direct observations,
- explicit statements in the current conversation.

Do not add what was not observed.

## 2. Inference

Inference includes:

- interpretation,
- pattern recognition,
- likely implication,
- model-derived classification,
- analogy,
- causal hypothesis,
- extrapolation.

Inference must remain connected to trace.

## 3. Assumption

Assumption includes:

- missing premise,
- likely context,
- unstated condition,
- role inference,
- domain prior,
- interpretation of intent.

Assumptions must be visible if they carry the answer.

## 4. UMR

UMR means unresolved model residue.

UMR should be used when:

- evidence is incomplete,
- source status is unclear,
- trace supports multiple interpretations,
- a claim is plausible but not bound,
- an absence claim cannot be justified,
- a self-report cannot be externally confirmed,
- a conclusion would over-bind uncertainty.

## 5. Output pattern

```text
Observed trace:
Inference:
Assumptions:
UMR:
Binding status:
Revision path:
```

## Minimal warning

```text
Unresolved does not mean false.
Unobserved does not mean absent.
Inferred does not mean verified.
Plausible does not mean bound.
```
