# Evil as Closure Test

Use this test to classify whether a process is structural evil under SΔϕ-16.

## Step 1 — Relational Future Check

Is there a relational future path-space?

```text
Ω_rel
```

If no, do not apply SΔϕ-16.

## Step 2 — Closure Check

Is Ω_rel being closed?

```text
Close(Ω_rel)
```

If no, do not classify as evil.

## Step 3 — Persistence Check

Does closure persist across updates?

If no, classify as local closure or error.

## Step 4 — Irreversibility Check

Does rollback cost explode?

```text
rollback cost explodes
```

If yes, continue.

## Step 5 — Condition Check

Are one or more closure-selection conditions present?

```text
E1: Close(Ω_rel) appears as Stabilize(φ)
E2: Cost_validate ≫ Cost_close
E3: Change ≈ IdentityCollapse ⇒ Δϕ_allowed → 0
```

## Classification

```text
recoverable error
temporary closure
persistent relational closure
evil as closure operator
```

## Negative constraint

Do not classify evil as a moral label for agents.

Classify closure dynamics.
