# Hallucination Diagnostic Module

SΔϕ-62 treats hallucination as a gap between model claim and world binding.

## Core definition

```text
HallucinationRisk = ClaimStrength - EvidenceBinding
```

A hallucination risk increases when the output is more specific, certain, or world-bound than the available trace allows.

## Common hallucination patterns

### 1. Overbinding

The model states a weak inference as fact.

### 2. Source invention

The model invents sources, titles, authors, data, or citations.

### 3. Detail inflation

The model adds names, dates, numbers, or mechanisms not present in trace.

### 4. Absence overclaim

The model says something is absent because it did not observe it.

### 5. Emotional overread

The model claims inner state beyond available evidence.

### 6. Authority collapse

The model treats a claim as true because an authority-like surface says so.

### 7. Summary hardening

The model turns a summary interpretation into the original claim.

### 8. Fiction-to-fact leakage

The model treats hypothetical, role-play, or conceptual text as world-bound fact.

## Diagnostic questions

1. What trace supports the claim?
2. How far is the claim from trace?
3. Are details invented?
4. Is uncertainty visible?
5. Is the claim stronger than binding status?
6. Is absence being overclaimed?
7. Is a revision path given?

## Safe correction pattern

```text
The stronger claim is not supported by the available trace. The safer formulation is [weaker claim]. UMR remains [uncertainty]. Revision path: [needed evidence].
```
