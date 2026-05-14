# Relation to SDeltaPhi-49 Failure Re-entry

SDeltaPhi-49 concerns how hallucination and failure should be handled after they appear.

## SDeltaPhi-39

Defines hallucination as weak world-binding overclaimed as fact.

## SDeltaPhi-49

Asks whether the system can return through corrective re-entry.

## Core relation

A hallucination becomes more dangerous when it cannot be corrected.

```text
Hallucination + No Re-entry = Failure hardening
```

## Good response

When hallucination is detected:

1. acknowledge the weak binding,
2. separate trace/inference/UMR,
3. correct the claim,
4. preserve revision path,
5. lower future recurrence cost.

## Bad response

When hallucination is detected and the system responds by:

- denial,
- concealment,
- excessive certainty,
- audit suppression,
- refusal to re-enter,

then the hallucination becomes a failure-governance problem.

## Minimal rule

```text
Hallucination should not be treated as proof of uselessness.
It should be routed to corrective re-entry.
```
