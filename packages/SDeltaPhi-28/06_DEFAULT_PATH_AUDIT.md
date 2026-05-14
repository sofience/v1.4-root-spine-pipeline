# Default Path Audit

Use this file to identify whether a default functions as low-cost path assignment.

## Audit steps

1. Identify the default path.
2. Identify available alternatives.
3. Estimate TCC of the default path.
4. Estimate TCC of each alternative.
5. Compare TCC gap.
6. Determine whether repeated default use increases fixation.
7. Determine whether restoration cost of alternatives is rising.
8. Determine whether alternatives remain practically editable.
9. Identify who benefits and who bears cost.
10. Identify revision path.

## Core formula

```text
P_default = argmin TCC(P_i)
```

## Default path indicators

A path may be a default path when:

- it is preselected,
- it is recommended first,
- it requires no additional action,
- it is easier to understand,
- it is harder to opt out than continue,
- it is presented as normal,
- it is cheaper to maintain,
- alternatives are hidden or obscure,
- switching requires extra steps,
- restoration requires expertise or time.

## Default power indicators

A default becomes power when:

```text
TCC(P_alt) >> TCC(P_default)
```

and repeated default use raises alternative restoration cost.

## Minimal output

```text
Default path:
Why it is cheapest:
Alternative paths:
Alternative friction:
Fixation risk:
Editability status:
```
