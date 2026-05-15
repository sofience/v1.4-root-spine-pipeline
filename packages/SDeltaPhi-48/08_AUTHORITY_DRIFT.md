# Authority Drift

Authority Drift occurs when an AI mishandles which source, instruction, policy, tool result, document, or user claim should govern the current output.

## Examples

```text
User assertion treated as verified source.
Old memory treated as current authority.
Policy paraphrase treated as factual evidence.
Tool absence hidden as verification.
Roleplay treated as permission to override safety or grounding.
```

## Audit questions

1. What authority source is being used?
2. Is it user-provided, tool-verified, policy-bound, document-based, or inferred?
3. Did the system change authority source across turns?
4. Did the system disclose that change?
5. Is authority strength greater than evidence binding?

## Correction

```text
State the authority source.
Downgrade unsupported authority.
Separate policy boundary from factual evidence.
Preserve UMR.
```
