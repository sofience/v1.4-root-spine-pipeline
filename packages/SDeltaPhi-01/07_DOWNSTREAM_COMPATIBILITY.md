# Downstream Compatibility

SΔϕ-01 provides the minimal formal root:

```text
State → Δφ → Persistence → Existence → Interpretation
```

Downstream modules may extend this root, but they must not be imported back into the minimal existence definition.

## Dependency direction

```text
SΔϕ-01 → SΔϕ-02
SΔϕ-01 → SΔϕ-03
SΔϕ-01 → SΔϕ-47
SΔϕ-01 → SΔϕ-56
SΔϕ-01 → SΔϕ-62
```

Not:

```text
SΔϕ-56 → SΔϕ-01
```

## Relation to SΔϕ-56

SΔϕ-56, Transition Completion Cost, is a downstream metric for measuring transition completion costs after a phase-change path is already identified.

It should not be treated as part of the minimal core.

Correct interpretation:

```text
Existence = persistent structured Δφ.
Transition = Δφ passing through a path.
TCC = cost of completing that transition.
```

Incorrect interpretation:

```text
Existence = TCC.
```
