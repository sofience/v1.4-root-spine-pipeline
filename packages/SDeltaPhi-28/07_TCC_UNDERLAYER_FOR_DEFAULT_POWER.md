# TCC Underlayer for Default Power

SDeltaPhi-28 is strengthened by SDeltaPhi-56 Transition Completion Cost.

A default path is not merely the option selected in advance.

It is the path with the lowest transition completion cost.

## Core formula

```text
DefaultPath = argmin TCC(P_i)
```

## Default power formula

```text
DefaultPower = TCC(P_alt) - TCC(P_default)
```

The larger the gap, the stronger the default power.

## Invisible fixation condition

```text
InvisibleFixation occurs when:

FormalChoice = true
but
TCC(P_alt) >> TCC(P_default)
```

## TCC components

TCC of a path may include:

- discovery cost,
- understanding cost,
- selection cost,
- switching cost,
- setup cost,
- maintenance cost,
- error recovery cost,
- social friction cost,
- institutional friction cost,
- restoration cost,
- re-entry cost.

## Alternative path TCC

```text
TCC(P_alt)
= C_discovery
+ C_switch
+ C_learning
+ C_maintenance
+ C_repair
+ C_social_friction
+ C_restabilization
```

## Practical editability

A non-default path remains formally available only if its TCC remains practically bearable.

If TCC(non-default) rises beyond practical editability, formal choice remains but real editability collapses.

## Strong definition

Default power is the power to lower the TCC of one continuation while raising, hiding, or leaving unaddressed the TCC of alternatives.

## Key sentence

SDeltaPhi-28 says what default power is.

SDeltaPhi-56 explains why it becomes operationally binding.
