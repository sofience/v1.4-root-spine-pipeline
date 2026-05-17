# Trace Regulation Loop

```text
Δϕ event
        ↓
Irreversibility test
RollbackCost >> UpdateBudget ?
        ↓
Trace candidate
        ↓
Memory re-entry
(constraint injection)
        ↓
Forgetting
(compression / pruning)
        ↓
Feasible path set Ω update
        ↓
Next selection
        ↺
repeat
```

Memory injects constraints. Forgetting compresses or prunes constraints. The system persists only when both remain active.
