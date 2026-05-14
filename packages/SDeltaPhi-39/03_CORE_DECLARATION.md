# Core Declaration

Hallucination is not merely false output.

Hallucination occurs when a weakly world-bound construction, inference, or UMR-filled continuation is output as if it were strongly bound to observed world trace.

## Core formulas

```text
Hallucination = ClaimStrength > EvidenceBinding

Hallucination = WeakInference spoken as WorldBoundFact

Hallucination = Inference output as Observed Trace

Hallucination = UMR erased into assertion
```

## Structural formula

```text
Hallucination = DeltaPhi_model - DeltaPhi_world != 0
```

## Operational refinement

```text
Hallucination =
model-world mismatch
+ insufficient world-binding
+ strong claim form
```

## Key distinction

Weak world-binding is not itself failure.

Weak world-binding becomes hallucination risk when it is output in a strong fact-like form.

## Minimal correction

Do not eliminate all construction.

Preserve binding discipline.
