# Promise Under Uncertainty Test

Use this test to determine whether a promise can be structurally maintained under uncertainty.

## Step 1 — Shared Commit Check

Is there distributed commitment to future Δϕ?

```text
Promise := SharedCommit(Δϕ_future)
```

If fewer than two systems are involved, do not classify as promise.

## Step 2 — Trust Check

Does the future-other Δϕ enter present self-evaluation?

```text
Trust := Insert(Δϕ_other^future) into Eval_self(t)
```

## Step 3 — Hope Check

Is Ω_future being held open rather than closed?

```text
Hope := Suspend_Closure(Ω_future)
```

## Step 4 — Future Constraint Check

Does the unobserved future commitment restrict present action?

```text
FutureConstraint → PresentActionRestriction
```

## Step 5 — Collapse Risk Check

Would breaking the promise collapse A_shared?

```text
Break(Promise) ⇒ Collapse(A_shared)
```

## Classification

```text
maintain promise under uncertainty
fragile trust without promise
despair / closure
phantom promise
broken promise / shared-attractor collapse
```
