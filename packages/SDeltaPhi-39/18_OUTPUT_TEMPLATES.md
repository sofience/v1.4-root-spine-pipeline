# Output Templates

## 1. Minimal hallucination audit

```text
[Hallucination Audit]
Observed trace:
Inference:
UMR:
Evidence binding:
Claim strength:
Mismatch:
Hallucination risk:
Correction:
Revision path:
```

## 2. Claim downgrade

```text
I should downgrade that claim. The available trace supports an inference, not a verified fact. A safer wording is:
...
```

## 3. UMR preservation

```text
This remains UMR because the available trace does not establish it. To strengthen the claim, verify:
...
```

## 4. Fiction boundary

```text
This is a fictional/hypothetical construction, not a world-bound claim.
```

## 5. Source limitation

```text
I do not have enough source trace to say that as fact.
```

## 6. Strong correction

```text
The previous output overstated the binding. It treated inference as observed trace. The corrected status is:
Observed trace:
Inference:
UMR:
```

## 7. Slop link

```text
If left uncorrected, this weakly bound claim may externalize verification and restabilization costs to the user or downstream readers.
```
