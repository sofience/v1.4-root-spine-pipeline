# Revision Path Protocol

A claim is safer when it includes what would change it.

## Revision path asks

1. What new trace would confirm the claim?
2. What new trace would weaken the claim?
3. What source would be authoritative?
4. What observation is missing?
5. What audit would lower UMR?
6. What would convert inference into stronger binding?
7. What would force reclassification?
8. What would make the claim operationally actionable?

## Revision path forms

### Evidence-based

```text
This would change if direct records, logs, citations, or primary documents show otherwise.
```

### User-context based

```text
This would change if the user provides the original file, message, screenshot, or missing context.
```

### Temporal

```text
This would change if the current status has changed since the last verified source.
```

### Operational

```text
This would change if the cost, harm, or transition reversibility differs from the stated assumptions.
```

### Conceptual

```text
This would change if the framework defines the term differently.
```

## Do not close without revision path

Avoid:

```text
This is definitely X.
```

Prefer:

```text
Given the observed trace, X is the strongest current inference. Revision path: Y.
```

## Minimal formula

```text
RevisionReadyClaim = Claim + EvidenceBasis + UMR + RevisionPath
```
