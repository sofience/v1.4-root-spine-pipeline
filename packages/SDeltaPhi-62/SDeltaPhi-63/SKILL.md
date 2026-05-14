---
name: sdelta-phi-theory-to-module-conversion
description: Use this skill when converting a philosophy, religion, ethical system, political ideology, economic theory, governance framework, AI alignment theory, cultural theory, psychological framework, or user-created theory into a conditional detection module with triggers, scope, outputs, UMR, failure modes, and downstream SDeltaPhi routing.
---

# SDeltaPhi-63 Theory-to-Module Conversion Skill

Use this skill to convert theories into conditional detection modules.

A theory should not be treated first as a worldview to adopt or reject. Convert it into an operational detector with scope, triggers, outputs, limits, UMR, and failure modes.

## When to use

Use this skill when the user asks about:

- a philosophy, religion, ethical theory, political ideology, economic theory, governance framework, cultural theory, psychological framework, AI alignment theory, or user-created framework;
- whether a theory explains something;
- how a theory would classify a situation;
- how to turn a theory into an AI-readable module;
- how to compare a theory with SDeltaPhi;
- how to prevent a theory from becoming a totalizing worldview.

## Procedure

1. Identify the theory or framework.
2. Extract the root proposition.
3. Identify what the theory detects well.
4. Identify what it fails to detect.
5. Define activation conditions.
6. Define required input traces.
7. Define output classifications.
8. Separate revealed cost from hidden cost.
9. Identify overbinding and ideology-capture risk.
10. Preserve UMR.
11. Provide revision path.
12. Route to downstream SDeltaPhi modules.

## Output fields

Return the lowest sufficient module description:

- Theory/framework
- Root proposition
- Primary detection target
- Activation condition
- Input trace required
- Detected pattern
- Output classification
- Cost structure revealed
- Cost structure hidden
- Blind spots
- Overbinding risk
- Failure modes
- UMR
- Revision path
- Downstream SDeltaPhi modules
- Safe-use wording

## Do not use

- Do not treat the converted module as final truth.
- Do not flatten historical, philosophical, religious, or political depth.
- Do not use one theory to explain everything.
- Do not erase UMR.
- Do not replace domain expertise.
- Do not use conversion as intellectual colonization.
- Do not treat the module output as a moral label.
- Do not block downstream cross-audit by other SDeltaPhi modules.

## Minimal response pattern

```text
[Theory-to-Module Conversion]
Theory/framework:
Root proposition:
Primary detection target:
Activation condition:
Input trace required:
Detected pattern:
Output classification:
Cost structure revealed:
Cost structure hidden:
Blind spots:
Overbinding risk:
Failure modes:
UMR:
Revision path:
Downstream SDeltaPhi modules:
Safe-use wording:
```

## Routing rule

If the converted theory involves:
- world-binding or factual uncertainty: route through SDeltaPhi-62.
- language, translation, declaration, or terminology: route through SDeltaPhi-64.
- cost measurement: route to SDeltaPhi-56.
- group or institutional cost attribution: route to SDeltaPhi-58.
- affect, care, guilt, love, shame, apology, or emotional pressure: route to SDeltaPhi-59.
- aggregate utility, sacrifice, or greater-good reasoning: route to SDeltaPhi-60.
- sacred authority, divinity, salvation, or ritual transaction: route to SDeltaPhi-61.
- generated low-quality output or verification burden: route to SDeltaPhi-65.
```
