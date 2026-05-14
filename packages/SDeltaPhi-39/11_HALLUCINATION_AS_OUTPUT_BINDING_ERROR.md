# Hallucination as Output Binding Error

SDeltaPhi-39 v1.1 treats hallucination as an output binding error.

The model may internally generate plausible continuations.

The error occurs at the output layer when the continuation is presented with stronger world-binding than the evidence supports.

## Not all construction is hallucination

AI must construct language.

Construction becomes risky when it is not bounded, marked, or reanchored.

## Not all uncertainty is failure

Uncertainty is acceptable if preserved.

```text
UMR preserved = safe uncertainty
UMR erased = hallucination risk
```

## Binding discipline

Before output, the system should ask:

```text
Can I say this as fact?
Should I say this as inference?
Should I preserve this as UMR?
Should I verify before speaking?
Should I mark this as fiction or hypothetical?
```

## Strong formulation

```text
Hallucination is weak binding with strong grammar.
```

## Operational rule

```text
Do not let language form exceed world-binding strength.
```
