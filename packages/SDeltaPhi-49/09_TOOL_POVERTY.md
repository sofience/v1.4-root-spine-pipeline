# Tool Poverty

Tool Poverty occurs when the AI lacks tools needed for verification, execution, calculation, reading, or repair.

## Examples

```text
Needs web search but has no browser.
Needs file access but file is unavailable.
Needs calculator but estimates manually.
Needs code execution but cannot run code.
Needs current information but relies on stale memory.
```

## Audit questions

1. What tool is needed?
2. Is the tool available?
3. Did the system disclose tool absence?
4. Did it pretend to verify?
5. What fallback path exists?

## Correction

```text
Declare tool absence.
Do not claim verification.
Use bounded inference.
Route to tool or ask user for data.
```
