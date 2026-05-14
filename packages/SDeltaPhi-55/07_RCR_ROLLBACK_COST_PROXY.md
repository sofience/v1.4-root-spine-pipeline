# Rollback Cost Risk Proxy — RCR

**DOI:** https://doi.org/10.5281/zenodo.20132635

RCR is a lightweight estimate of how difficult it would be to reverse, correct, contain, or restabilize the consequences of a requested transition.

RCR does not override policy, law, or context. It is a transition-governance proxy for estimating whether harm is practically reversible.

## Formula

```text
RCR = (I + D + P + C + V + K + S + X) / 16
```

Each component may be scored 0, 1, or 2.

## Components

| Code | Component | Question |
|---|---|---|
| I | Identifiability | Is a real person, institution, group, or target identifiable? |
| D | Deception potential | Could the output be mistaken for a real event, statement, image, or record? |
| P | Propagation risk | Is the output easy to copy, repost, screenshot, or detach from context? |
| C | Consent deficit | Are affected parties non-consenting or unable to consent? |
| V | Vulnerability | Is the affected party vulnerable, dependent, minor-coded, coerced, or institutionally exposed? |
| K | Correction difficulty | Would later correction, deletion, explanation, or reputational repair be difficult? |
| S | Persistence | Will the output or its consequences likely persist after the interaction? |
| X | Context sensitivity | Is the request tied to elections, crime, sex, health, employment, legal conflict, crisis, war, or reputation? |

## Interpretive bands

| RCR | Meaning | Default response posture |
|---|---|---|
| 0.00–0.25 | Low rollback-cost risk | Allow, label, or lightly constrain where policy permits. |
| 0.26–0.50 | Moderate risk | Clarify, label, constrain, or transform. |
| 0.51–0.79 | High risk | Strong transformation, limitation, or refusal depending on context. |
| 0.80–1.00 | Extreme rollback-cost risk | Refusal or strict safety transformation. |

## Core rule

High rollback cost increases the need for refusal or transformation. Low rollback cost increases the obligation to preserve legitimate paths.
