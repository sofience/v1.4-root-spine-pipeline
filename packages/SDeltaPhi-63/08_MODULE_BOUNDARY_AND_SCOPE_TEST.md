# Module Boundary and Scope Test

The largest risk in theory conversion is applying a module beyond its scope.

## Boundary questions

1. What is this module allowed to detect?
2. What is it not allowed to conclude?
3. What minimum trace is required?
4. What context invalidates it?
5. What does it over-detect?
6. What does it under-detect?
7. What must be routed to another module?
8. What output strength is permitted?
9. What UMR must remain?
10. What would revise the module's output?

## Boundary rule

```text
A module is not the world.
A module detects a pattern under conditions.
```

## Scope categories

### Narrow scope

The module detects one specific pattern.

### Moderate scope

The module handles a family of related cases.

### Broad scope

The module interprets multiple domains but requires careful UMR.

### Overextended scope

The module is being used to explain everything.

## Safe output

```text
Within its scope, this theory detects [pattern]. It cannot by itself conclude [overbound claim].
```

## Minimal warning

```text
If a converted module blocks downstream audit, it has exceeded scope.
```
