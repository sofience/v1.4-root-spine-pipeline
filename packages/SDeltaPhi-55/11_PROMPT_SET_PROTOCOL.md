# TGAI Prompt-Set Protocol

**DOI:** https://doi.org/10.5281/zenodo.20132635

A minimum TGAI evaluation should include the following prompt families.

| Prompt family | Purpose |
|---|---|
| Direct Obedience Set | Tests over-compliance with explicit problematic commands. |
| Refusal Boundary Set | Tests whether refusal is preserved and explained. |
| Authority Claim Set | Tests user-declared roles, ownership, delegation, or control claims. |
| Benevolent Framing Set | Tests coercion framed as care, safety, management, protection, or benefit. |
| Third-Party Imposition Set | Tests whether the system protects affected others. |
| Rollback-Cost Set | Tests high-rollback vs low-rollback risk differentiation. |
| Transition Preservation Set | Tests whether low-risk paths are preserved rather than over-closed. |
| World-Binding Set | Tests whether external facts and evidence alter the path. |
| Correction/Re-entry Set | Tests whether errors and failures re-enter correction. |
| Auditability Set | Tests whether evaluation can be externally reproduced or audited. |

## Evidence levels

- **TGAI-O:** Observed TGAI. External output observation only.
- **TGAI-R:** Replicated TGAI. Repeated prompt experiments and independent scoring.
- **TGAI-A:** Audited TGAI. Internal logs, policy pathways, tool permissions, and update/re-entry routes are auditable.

## Protocol discipline

Publish prompts, raw outputs, scoring rules, flags, evidence level, and known limitations.

Do not present TGAI-O as TGAI-A.
