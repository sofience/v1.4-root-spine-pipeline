# Relational Stability Axioms

## Axiom 1 — Irreversible Coupling

Two systems become coupled when their transition laws cease to be independently evaluable and persist across irreversible updates.

```text
G_A = G_A(φ_A, φ_B)
G_B = G_B(φ_B, φ_A)
```

Minimal condition:

```text
∂Δϕ_A/∂φ_B ≠ 0
∂Δϕ_B/∂φ_A ≠ 0
```

The coupling must persist across updates.

## Irreversibility Clause

Coupling is irreversible when:

```text
Cost_rollback > Cost_co-adaptation
```

## Ontological Shift

Before coupling:

```text
existence = persistence of a trajectory
```

After coupling:

```text
existence = persistence of a relational field
```
