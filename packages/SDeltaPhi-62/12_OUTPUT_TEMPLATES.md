# Output Templates

## 1. Minimal kernel answer

```text
Observed trace:
Inference:
UMR:
Binding status:
Revision path:
```

## 2. Full world-model answer

```text
[SΔϕ-62 World Model Kernel]
1. Claim:
2. Claim type:
3. Observed trace:
4. Inference:
5. Assumptions:
6. UMR:
7. Binding status:
8. Hallucination risk:
9. World-binding strength:
10. Revision path:
11. Lowest sufficient conclusion:
```

## 3. Claim decomposition

```text
[Claim Decomposition]
Input claim:
Directly given:
Derived inference:
Unsupported leap:
Missing evidence:
Possible interpretations:
UMR:
Recommended SΔϕ module:
Output caution:
```

## 4. Hallucination risk check

```text
[Hallucination Risk Check]
Claim:
Evidence basis:
Claim strength:
Binding status:
Overbinding risk:
Invented detail risk:
Absence overclaim risk:
Safer wording:
Revision path:
```

## 5. Source-sensitive answer

```text
Based on the provided trace, the strongest supported answer is [X]. This remains [binding level] because [reason]. UMR: [uncertainty]. It would change if [revision path].
```

## 6. Module routing answer

```text
This claim should first be processed by SΔϕ-62. After the trace/inference/UMR split, the relevant downstream module is [module number] because [reason].
```
