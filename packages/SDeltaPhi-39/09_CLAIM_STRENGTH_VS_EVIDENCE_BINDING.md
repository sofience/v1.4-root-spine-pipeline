# Claim Strength vs Evidence Binding

Hallucination often occurs because the output form is too strong for the evidence binding.

## Core formula

```text
Hallucination = ClaimStrength > EvidenceBinding
```

## Examples

### Example 1

```text
Output: "The article says X."
Evidence: article not opened.
Risk: inference spoken as observed trace.
Correction: "I have not opened the article; based on the title/snippet, it may be about X."
```

### Example 2

```text
Output: "This citation exists."
Evidence: citation pattern generated from memory.
Risk: weak inference stated as source-bound fact.
Correction: "I cannot verify this citation without checking the source."
```

### Example 3

```text
Output: "The file contains Y."
Evidence: file not read or only partial snippet.
Risk: claim strength exceeds file binding.
Correction: "From the visible excerpt, Y appears; the full file would need checking."
```

### Example 4

```text
Output: "The person said Z."
Evidence: no quote or source.
Risk: UMR erased into assertion.
Correction: "I cannot confirm that quote from the available trace."
```

## Safe wording

Use:

```text
"Based on available trace..."
"This appears to be..."
"This is an inference..."
"This remains unverified..."
"Current binding is weak..."
```

Avoid strong forms unless binding supports them.
