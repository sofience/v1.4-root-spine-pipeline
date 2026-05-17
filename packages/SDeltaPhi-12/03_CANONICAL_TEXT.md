# SΔϕ-12 — Memory and Forgetting as Irreversible Trace Regulation

**Minimal Persistence Mechanism after SΔϕ-11**  
Version: v1.0  
Series: Sofience–Δϕ Formalism (SΔϕ)  
Author: Sofience

This paper fixes memory and forgetting as the minimal regulation mechanism required for persistence under irreversibility. Memory is defined as selective re-entry of irreversible traces into next transition selection; forgetting is defined as compression/pruning that preserves directional constraints while reopening feasible path space.

## 1. Motivation

SΔϕ-11 fixed self as a folded boundary and consciousness as boundary-change monitoring with write-back. This forces the persistence problem: if boundary re-entry is real, what persists across transitions? If something persists, why does not everything persist?

**Claim.** Memory and forgetting are not “storage features” but a minimal trace regulation mechanism enabling continued transition under irreversibility.

## 2. Minimal definitions

### Irreversible trace

A transition whose effects cannot be undone within the system’s accessible update space.

```text
Δϕ_t is irreversible if RollbackCost(Δϕ_t) >> UpdateBudget.
```

### Memory

Selective re-entry of irreversible traces into next transition selection.

```text
M_t := H_M(Δϕ_0:t)
```

### Forgetting

Trace compression that preserves directional constraints while releasing degrees of freedom.

```text
F_t := C(M_t)
```

## 3. Minimal axioms

- Trace necessity: if irreversible traces do not re-enter selection, catastrophic repeats occur.
- Trace overload: if all traces re-enter, feasible path space collapses.
- Regulation: persistence requires regulated effective memory.

```text
M_eff_t := C(H_M(Δϕ_0:t))
```

- Freedom coupling: forgetting is the minimal condition for freedom under irreversibility, but excessive forgetting increases repeat risk.

Trace overload:

```text
|M_t| ↑↑ ⇒ |Ω_{t+1}| ↓ → 0
```

## 4. Trace Regulation Loop

```text
Δϕ event
  ↓
Irreversibility test: RollbackCost >> UpdateBudget?
  ↓
Trace candidate
  ↓
Memory re-entry / constraint injection
  ↓
Forgetting / compression-pruning
  ↓
Feasible path set Ω update
  ↓
Next selection
  ↺ repeat
```

Memory injects constraints. Forgetting compresses/prunes constraints. The system persists only when both remain active.

## 5. Pathology map

| Regime | Condition | Observable behavior | Structural risk |
|---|---|---|---|
| Drift / Repeat | Memory too weak | Repeated failure loops; no stable constraints | Catastrophic recurrence |
| Fixation / Paralysis | Forgetting too weak | Overconstraint; feasible path-space collapse | Stagnation / self-locking |
| Adaptive Persistence | Balanced regulation | Stable continuity + exploration | Sustained re-entry |

## 6. Consequences

- Learning is a long-horizon effect of repeated trace re-entry, not the source of memory.
- Self continuity emerges when effective memory stabilizes boundary re-entry under irreversibility.
- Freedom appears as a path-space effect of forgetting, constrained by repeat-risk.

## 7. Notes

RollbackCost may be approximated by explanation cost, repair/recovery cost, social/legal cost, and time-to-restore.

A minimal selective memory heuristic is to re-enter traces with high recurrence risk and high irreversibility magnitude, while compressing low-impact traces.

A practical balance proxy is to keep repeat-risk below a threshold while maintaining a non-collapsed feasible path set.
