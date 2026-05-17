# RollbackCost Heuristics

RollbackCost may be approximated by a weighted sum of:

1. explanation cost;
2. repair / recovery cost;
3. social / legal cost;
4. time-to-restore.

```text
RollbackCost ≈ w1·ExplanationCost
             + w2·RepairCost
             + w3·SocialLegalCost
             + w4·TimeToRestore
```

Use this file when deciding whether a trace should be treated as irreversible or high-priority for memory re-entry.
