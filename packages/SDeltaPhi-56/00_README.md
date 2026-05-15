# SΔϕ-56 — Transition Completion Cost v1.3

DOI: https://doi.org/10.5281/zenodo.20116959

This package provides the v1.3 upgrade of SΔϕ-56. It reinforces Transition Completion Cost (TCC) with explicit Friction Coefficients, Disclosure Friction, and Disclosure-to-Re-entry TCC Differential.

Core rule:

```text
Do not create a separate sovereign FIP metric by default.
Treat FIP-like pressure as the TCC gap between disclosure-to-reentry and silence/default continuation.
```

Use this record as the cost substrate for later SΔϕ Operational Kernel v1.6 routing.

Recommended starting files:

1. `01_AI_QUICKSTART.md`
2. `02_AI_MINIMAL_PROMPT.txt`
3. `machine/sdelta_phi_56_tcc_v1_3.tcc_formula.json`
4. `machine/sdelta_phi_56_tcc_v1_3.friction_coefficients.yaml`
5. `machine/sdelta_phi_56_tcc_v1_3.scoring_rubric.yaml`
