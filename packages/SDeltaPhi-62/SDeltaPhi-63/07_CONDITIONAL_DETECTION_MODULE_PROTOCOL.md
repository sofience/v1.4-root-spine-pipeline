# Conditional Detection Module Protocol

A converted theory becomes a conditional detection module.

## Module form

```text
Module name:
Theory:
Core proposition:
Activation condition:
Input signals:
Detected pattern:
Output classification:
Cost revealed:
Cost hidden:
Overbinding risk:
Blind spot:
Failure mode:
UMR:
Revision path:
Downstream SDeltaPhi modules:
```

## Activation condition

Activation should be specific.

Avoid:

```text
Always apply this theory.
```

Prefer:

```text
Activate when input traces include [specific pattern].
```

## Required trace

A module should state what evidence is needed before it can produce output.

Examples:

```text
Marxist module requires labor, ownership, production, class, or cost-attribution traces.
CASI route requires group, authority, benefit, sacrifice, dissent, exit, or repair traces.
USSI route requires aggregate-benefit or greater-good reasoning.
```

## Output strength

A module output should be conditional.

Avoid:

```text
This proves the theory.
```

Prefer:

```text
Under this module, the trace flags [pattern] with [binding level]. UMR remains [X].
```

## Minimal formula

```text
ObservedTrace + TheoryLens -> ConditionalClassification + UMR + RevisionPath
```
