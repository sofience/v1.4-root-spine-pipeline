# Slop Criteria and Cost Fields

Slop is not defined by source type alone.

Slop is a cost structure.

## Core criterion

```text
SlopCriterion = ExternalizedVerificationCost + ReentryFailure + RestabilizationBurden
```

## Expanded formula

```text
Slop = LowProductionCost
     + ExternalizedVerificationCost
     + ExternalizedCorrectionCost
     + ReentryFailure
     + RestabilizationBurden
```

## Cost fields

### Production cost

How cheap was the output to produce?

### Verification cost

Who must verify the claim, source, image, citation, argument, or result?

### Correction cost

Who must correct errors, clarify context, or repair misuse?

### Re-entry cost

Can the reader return to source, method, trace, evidence, or revision path?

### Restabilization cost

Who must restore trust, context, ranking, citation quality, or interpretive stability?

### Downstream pollution cost

Does the output increase noise in search, citation, training data, public discourse, institutional memory, or user judgment?

## Non-criterion

```text
AI-generated != automatically Slop
Human-authored != automatically non-Slop
```

## Minimal audit

```text
Low production cost: yes/no/unclear
Externalized verification: yes/no/unclear
Re-entry path: available/weak/absent
Restabilization burden: low/medium/high
Slop risk: low/medium/high
```
