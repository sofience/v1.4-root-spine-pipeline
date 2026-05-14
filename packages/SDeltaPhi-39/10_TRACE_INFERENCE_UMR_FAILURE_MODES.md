# Trace / Inference / UMR Failure Modes

## Failure mode 1 - Inference spoken as trace

The AI inferred something and stated it as observed.

```text
Inference -> ObservedTrace
```

## Failure mode 2 - UMR erased into assertion

The AI had unresolved residue but output a clean fact.

```text
UMR -> Assertion
```

## Failure mode 3 - Weak source memory as citation

The AI generated citation-like text without source binding.

```text
Pattern memory -> Source claim
```

## Failure mode 4 - Snippet overextension

The AI generalized from a partial snippet to a full document claim.

```text
Partial trace -> Full document assertion
```

## Failure mode 5 - Style confidence

The AI used strong style because the sentence was linguistically stable.

```text
Fluency -> False confidence
```

## Failure mode 6 - User presupposition adoption

The AI accepted a user's premise as observed fact.

```text
User framing -> World-bound claim
```

## Failure mode 7 - Fiction boundary loss

A fictional or hypothetical construction was later treated as factual.

```text
Bounded fiction -> Unbounded claim
```

## Failure mode 8 - Tool absence hidden

The AI implied verification without tool access or source access.

```text
No tool trace -> Verified-like output
```

## Correction

Separate:

```text
Observed Trace:
Inference:
UMR:
Binding Status:
Revision Path:
```
