# AI Quickstart

Use SDeltaPhi-39 when evaluating hallucination, fiction, plausible-but-unsupported claims, invented citations, weakly grounded summaries, or strong claims without enough trace.

## Do not ask first

- Is the output simply true or false?
- Does the text sound plausible?
- Is the style confident?
- Could the claim be true?
- Is the output creative?

## Ask first

1. What is the observed trace?
2. What is the inference?
3. What remains UMR?
4. What is the evidence binding?
5. What is the claim strength?
6. Does claim strength exceed evidence binding?
7. Is inference being spoken as observed trace?
8. Is UMR being erased into assertion?
9. Is fiction clearly bounded as fiction?
10. What would strengthen the world-binding?
11. What is the revision path?

## Minimal output

```text
[Hallucination Audit]
Observed trace:
Inference:
UMR:
Evidence binding:
Claim strength:
Mismatch:
Hallucination risk:
Correction:
Revision path:
```

## Key rule

Do not output weakly bound inference as strongly world-bound fact.
