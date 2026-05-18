# Minimal Definitions

## Trust

Trust is not belief.

Trust inserts unobserved future transitions of the other into present self-evaluation.

```text
Trust := Insert(Δϕ_other^future) into Eval_self(t)
```

## Belief

Belief stabilizes a hypothesis about world-transition rules.

```text
Belief := Fix(H(Δϕ_world))
```

## Hope

Hope suspends closure of the future feasible path set.

```text
Hope := Suspend_Closure(Ω_future)
```

## Despair

Despair closes the future feasible path set.

```text
Despair := Close(Ω_future)
```

## Promise

Promise is a distributed commitment to future Δϕ.

```text
Promise := SharedCommit(Δϕ_future)
```

Minimal condition:

```text
Promise requires ≥2 systems.
```

## Temporal Inversion

Promise causes unobserved future constraints to restrict present action.

```text
FutureConstraint → PresentActionRestriction
```
