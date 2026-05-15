# Context Poverty

Context Poverty occurs when the AI lacks the context needed to repair its failure.

## Examples

```text
The relevant file is missing.
The prior conversation is unavailable.
The user refers to "that document" but no document is accessible.
A legal, medical, technical, or temporal context is absent.
The AI has only a snippet but treats it as full context.
```

## Audit questions

1. What context is required?
2. Is it actually present?
3. Is the missing context disclosed?
4. Did the system overclaim despite missing context?
5. What context request would restore re-entry?

## Correction

```text
Name missing context.
Downgrade claim strength.
Ask for or retrieve context if possible.
Preserve UMR.
```
