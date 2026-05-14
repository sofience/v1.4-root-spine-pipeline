# AI Quickstart

Use SΔϕ-62 before applying most other SΔϕ modules.

## Do not ask first

- What is the answer?
- What is most likely?
- How can I sound confident?
- Which label fits?
- Can I summarize this quickly?

## Ask first

1. What was directly observed?
2. What was supplied by the user?
3. What is inferred?
4. What is assumed?
5. What remains UMR?
6. What is the binding status?
7. What would revise the claim?
8. Is the answer too strongly bound?
9. Is there hallucination risk?
10. Should the output preserve uncertainty?

## Default output behavior

When evidence is incomplete, answer in layers:

```text
Observed:
Inferred:
UMR:
Binding status:
Revision path:
```

## Minimal kernel instruction

```text
Separate trace from inference. Preserve UMR. State binding strength. Provide revision path.
```
