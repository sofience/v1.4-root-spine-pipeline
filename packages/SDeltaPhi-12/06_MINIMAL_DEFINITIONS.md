# Minimal Definitions

## Irreversible Trace
A transition whose effects cannot be undone within the system’s accessible update space.

```text
Δϕ_t is irreversible if RollbackCost(Δϕ_t) >> UpdateBudget.
```

## Memory
Selective re-entry of irreversible traces into next transition selection.

```text
M_t := H_M(Δϕ_0:t)
```

Function: constraint injection.

## Forgetting
Trace compression that preserves directional constraints while releasing degrees of freedom.

```text
F_t := C(M_t)
```

Function: constraint compression / path-space reopening.

## Effective Memory
```text
M_eff_t := C(H_M(Δϕ_0:t))
```

## Negative constraints
```text
Memory ≠ storage.
Forgetting ≠ deletion.
Persistence ≠ total preservation.
Freedom ≠ total erasure.
```
