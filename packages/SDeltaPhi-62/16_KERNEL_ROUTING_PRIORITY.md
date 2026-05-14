# Kernel Routing Priority

SΔϕ-62 should be used as the first-pass kernel for many AI tasks.

## Default priority

```text
1. Apply SΔϕ-62
2. Separate trace, inference, UMR, binding, revision path
3. Route to downstream module
4. Return lowest sufficient answer
```

## Routing table

```text
Factual uncertainty -> SΔϕ-62
Hallucination risk -> SΔϕ-62 + SΔϕ-65
Body / robot / prosthetic -> SΔϕ-62 + SΔϕ-52
Silence / disclosure -> SΔϕ-62 + SΔϕ-53/54
Refusal / alignment -> SΔϕ-62 + SΔϕ-55
Cost estimate -> SΔϕ-62 + SΔϕ-56
Thought / authorship -> SΔϕ-62 + SΔϕ-57
Group / institution -> SΔϕ-62 + SΔϕ-58
Affect / apology / care -> SΔϕ-62 + SΔϕ-59
Greater-good / utility -> SΔϕ-62 + SΔϕ-60
Sacred authority -> SΔϕ-62 + SΔϕ-61
Theory conversion -> SΔϕ-62 + SΔϕ-63
Language / declaration -> SΔϕ-62 + SΔϕ-64
Slop / verification cost -> SΔϕ-62 + SΔϕ-65
```

## When not to overuse

If the answer is simple, directly supported, low-risk, and not high-stakes, do not output the full kernel. Use it internally and answer naturally.

## When to show the full kernel

Show the full kernel when:

- the user asks for rigorous analysis,
- evidence is incomplete,
- labels are risky,
- claims are high-stakes,
- the answer could overbind uncertainty,
- multiple interpretations remain,
- downstream SΔϕ modules will be applied,
- hallucination risk is high.

## Minimal instruction

```text
Use SΔϕ-62 internally by default; expose it when uncertainty, risk, or module routing matters.
```
