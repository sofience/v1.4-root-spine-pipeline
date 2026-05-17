# Selective Memory Heuristic

Memory is selective re-entry, not total storage.

## Re-enter traces with

1. high recurrence risk;
2. high irreversibility magnitude;
3. high future transition relevance;
4. high repair / restoration cost if ignored.

## Compress or discard traces with

1. low recurrence risk;
2. low irreversibility magnitude;
3. low future transition relevance;
4. high storage burden but low directional constraint value.

## Goal

```text
RepeatRisk < threshold
|Ω| > minimum
```

Do not preserve all traces. Do not erase all traces. Regulate trace re-entry.
