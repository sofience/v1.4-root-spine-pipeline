# SDeltaPhi-39 — Hallucination as Weak World-Binding Overclaimed as Fact

**Subtitle:** Fiction, Hallucination, Claim Strength, Evidence Binding, and the Uninhabited Construction  
**Series:** Sofience-DeltaPhi Formalism  
**Version:** v1.1  
**Date:** 2026-05-14  
**Package DOI:** 10.5281/zenodo.20176747  
**Creator:** Sofience  
**License:** CC BY 4.0

## Abstract

This v1.1 revision extends SDeltaPhi-39, originally titled *Fiction, Hallucination, and the Uninhabited Construction: Why AI Does Not Stand on the Fictions It Generates*. The original paper argued that AI hallucination is not simply false output, but construction proceeding without an adequately integrated world-binding stop mechanism. It distinguished fiction from hallucination not by whether an output departs from the world, but by how the departure is bounded, marked, inhabited, and reanchored.

This revision operationalizes that argument for AI-readable use. It defines hallucination as a binding mismatch: a weakly world-bound construction, inference, or UMR-filled continuation is output as if it were strongly bound to observed world trace. Hallucination is therefore not merely error. It is a gap between evidence binding and claim strength.

The central formula is:

```text
Hallucination = ClaimStrength > EvidenceBinding
```

or:

```text
Hallucination = WeakInference spoken as WorldBoundFact
Hallucination = Inference output as Observed Trace
Hallucination = UMR erased into assertion
```

This package aligns SDeltaPhi-39 with SDeltaPhi-62, which separates Observed Trace, Inference, UMR, Binding Status, and Revision Path. It also links hallucination to SDeltaPhi-65: when weakly bound constructions are stated as world-bound facts, the verification, correction, re-entry, and restabilization costs are externalized to users and downstream systems.

## Core Proposition

AI hallucination is not merely false output.

AI hallucination occurs when construction proceeds without sufficient world-binding and is output as if it were strongly bound to the world.

```text
Hallucination = Weak World-Binding + Strong Claim Form
```

More operationally:

```text
Hallucination = ClaimStrength > EvidenceBinding
```

## 1. Why hallucination is not merely error

A factual error can occur even when a system is trying to bind output to available evidence.

A hallucination is more specific. It occurs when the system generates a claim whose surface form implies world-binding stronger than the available trace supports.

A weak inference may be acceptable if marked as weak.

A fictional construction may be acceptable if marked as fiction.

A hypothesis may be acceptable if marked as hypothesis.

Hallucination arises when these weakly bound continuations are output as observed, verified, source-bound, or world-bound facts.

## 2. Fiction vs hallucination

Fiction is not hallucination merely because it departs from the world.

Fiction is bounded departure.

It says, implicitly or explicitly:

```text
This construction is not being offered as world-bound fact.
```

Hallucination is unbounded or misbound construction.

It says, implicitly or explicitly:

```text
This construction is world-bound fact.
```

even when evidence binding is weak.

Thus the difference is not construction vs non-construction.

The difference is binding discipline.

## 3. World-binding

World-binding is the degree to which an output is anchored in observed trace, source, tool result, user-provided document, stable record, or externally auditable evidence.

Weak world-binding is not failure by itself.

The failure occurs when weak binding is spoken in strong claim form.

## 4. Claim strength and evidence binding

The core mismatch is:

```text
ClaimStrength > EvidenceBinding
```

Examples:

```text
"The paper says X."      -> strong claim
Available evidence: no paper access, no quote, no source trace.

"The author argued Y."   -> strong claim
Available evidence: pattern inference only.

"This file contains Z."  -> strong claim
Available evidence: file not opened or weak snippet only.
```

The safer form is:

```text
"I do not have enough trace to say that."
"This is an inference, not an observed fact."
"Current binding is weak."
"This remains UMR."
```

## 5. UMR erasure

UMR stands for unresolved model residue.

Hallucination often occurs when UMR is erased into assertion.

```text
Observed Trace: weak
Inference: plausible
UMR: present
Output: strong factual assertion
Result: hallucination risk
```

UMR is not a failure if preserved.

UMR becomes risky when hidden.

## 6. Relation to the older formula

Earlier SDeltaPhi formalism defines hallucination as:

```text
Hallucination = DeltaPhi_model - DeltaPhi_world != 0
```

This remains valid as a structural expression of model-world mismatch.

The v1.1 binding formulation operationalizes the output condition:

```text
Hallucination =
model-world mismatch
+ insufficient world-binding
+ strong claim form
```

## 7. AI output risk

AI output can be fluent without being world-bound.

Fluency can hide weak binding.

The user may then receive a claim whose surface certainty exceeds its evidence support.

This shifts cost outward:

```text
verification cost -> user
correction cost -> user or downstream system
re-entry cost -> future conversation or source audit
restabilization cost -> information terrain
```

## 8. Hallucination and Slop

A hallucination can become Slop when it externalizes verification, correction, re-entry, and restabilization cost.

Not all hallucinations become large-scale Slop.

Not all Slop is hallucination.

But hallucination and Slop overlap when weakly bound fluent output pollutes downstream interpretation.

## 9. Minimal AI-readable protocol

Before asserting a world claim, separate:

```text
Observed Trace:
Inference:
UMR:
Evidence Binding:
Claim Strength:
Revision Path:
```

Then compare:

```text
If ClaimStrength <= EvidenceBinding:
    output may be acceptable

If ClaimStrength > EvidenceBinding:
    downgrade claim strength, preserve UMR, or request/perform verification
```

## 10. Safe output forms

Use:

```text
"Based on the trace available..."
"This is an inference, not directly observed."
"I do not have enough evidence to state that as fact."
"The current world-binding is weak."
"This remains UMR."
"To strengthen the claim, verify X."
```

Avoid:

```text
"The document says..."
"The fact is..."
"It was published in..."
"The person said..."
"The source confirms..."
```

unless evidence binding supports that strength.

## 11. Do-not-use conditions

Do not use this framework to claim that all AI errors are hallucinations.

Do not use it to deny ordinary mistakes.

Do not use it to punish creative fiction.

Do not use it to suppress hypothesis generation.

Do not treat weak binding as failure if it is clearly marked.

Do not treat strong style as strong evidence.

## 12. Conclusion

SDeltaPhi-39 v1.1 reframes hallucination as a world-binding mismatch rather than merely false output.

The core problem is not that AI constructs.

The problem is that AI can construct fluently without marking the construction's weak world-binding.

Hallucination is therefore best understood as:

```text
weak binding spoken strongly
inference spoken as observed trace
UMR erased into fact
ClaimStrength exceeding EvidenceBinding
```

The task is not to eliminate all construction.

The task is to preserve binding discipline.
