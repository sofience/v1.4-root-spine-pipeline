# Trace Regulation Loop

```text
Δϕ event
(interaction / mismatch occurrence)
        ↓
Irreversibility test
RollbackCost >> UpdateBudget ?
        ↓
Trace candidate
(irreversible Δϕ to be re-entered)
        ↓
Memory re-entry
(constraint injection)
        ↓
Forgetting
(compression / pruning)
        ↓
Feasible path set Ω update
(constraints applied / released)
        ↓
Next selection
(transition choice / execution)
        ↺
repeat
```

Memory injects constraints.

Forgetting compresses or prunes constraints.

The system persists only when both remain active.
