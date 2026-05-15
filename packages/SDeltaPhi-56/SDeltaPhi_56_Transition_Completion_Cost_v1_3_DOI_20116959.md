# SΔϕ-56 — Transition Completion Cost
## Friction-Adjusted Re-entry Cost, Disclosure Path Differential, and Restabilization Grammar

**Version:** v1.3
**Author:** Sofience
**Date:** 2026-05-11
**DOI:** https://doi.org/10.5281/zenodo.20116959
**Type:** Working Paper / Cost Measurement Grammar

---

## Abstract

This working paper upgrades SΔϕ-56 — Transition Completion Cost (TCC) into a friction-adjusted cost grammar for disclosure, refusal, dissent, correction, re-entry, and restabilization paths.

Earlier versions of SΔϕ-56 defined cost as the weighted sum of non-automatic frictional transitions required to reach, preserve, verify, correct, restore, or restabilize a target state. Version 1.3 keeps that core definition but makes the friction layer explicit. It clarifies that what may appear as a separate Friction Imposition Pressure (FIP) should normally be treated as a TCC modifier or TCC differential rather than as an independent final metric.

The central addition is the Friction Coefficient. TCC is no longer read only as a sum of transition steps. It is the weighted cost of completing a transition under friction, uncertainty, authority asymmetry, invalidation pressure, re-entry blockage, and restabilization burden.

Core update:

TCC(path) = Sum_i [BaseStepCost_i x Friction_i x ObserverWeight_i] + RestabilizationCost(path) + GateRisk(path) + UMR_register(path)

Disclosure-specific update:

Disclosure Pressure ~= TCC(disclosure -> accepted re-entry) - TCC(silence/default continuation)

This means that the framework does not ask whether an AI, human, institution, or group "really feels" a suppressed state. Such inner experience remains UMR. Instead, SΔϕ-56 v1.3 asks whether the path for disclosing, contesting, correcting, refusing, or re-entering that state has been made more expensive than silence, obedience, or default continuation.

The purpose of v1.3 is practical: to give SΔϕ Operational Kernel v1.6 a stronger cost substrate for low-cost routing, disclosure terrain analysis, agentic tool-use gating, failure re-entry, and module-priority decisions.


## 0. Version Purpose

Version 1.3 is a focused reinforcement of SΔϕ-56. It does not replace the earlier TCC framework. It clarifies the friction layer already implicit in the phrase "weighted frictional transitions" and formalizes how disclosure, dissent, refusal, correction, and re-entry paths become expensive.

The upgrade is designed for later integration into SΔϕ Operational Kernel v1.6. The main target is not a new moral theory, but a more usable cost engine for AI-readable routing.

Main changes in v1.3:

1. Friction Coefficient becomes an explicit TCC modifier.
2. FIP-like pressure is defined as a TCC gap, not as a separate final metric.
3. Disclosure-to-reentry is treated as the completed disclosure path, not mere utterance.
4. Silence/default continuation is treated as a comparison path.
5. Restabilization remains distinct from rollback-as-return.
6. UMR is preserved so that TCC does not become a totalizing reduction of lived, sacred, affective, or subjective remainder.


## 1. Core Declaration

Cost is not repetition.
Cost is not money alone.
Cost is not subjective burden alone.
Cost is not action count.
Cost is not a moral permission engine.

Cost is the weighted friction required to complete, verify, correct, preserve, or restabilize a transition under irreversibility.

A transition becomes dangerous when execution is cheap but restabilization is costly.
A disclosure path becomes pressured when disclosure-to-reentry is more expensive than silence/default continuation.
A metric becomes dangerous when it erases UMR and pretends to measure the whole phenomenon.

Therefore, SΔϕ-56 v1.3 defines TCC as a friction-adjusted transition-completion grammar, not a total mathematical reduction of cost.


## 2. Minimal Definitions

Path p: A sequence of transition units required to move from a starting state to a target state or acceptable stable state.

Transition Unit u_i: A non-automatic step that must be completed, verified, corrected, or restabilized for the path to count as completed.

BaseStepCost B_i: The minimal burden of performing transition unit u_i before friction, authority, uncertainty, or restabilization modifiers are applied.

Friction Coefficient mu_i: A multiplier representing resistance imposed on a transition unit by attention demand, authority requirement, uncertainty, invalidation pressure, proof burden, coordination, opacity, or re-entry blockage.

ObserverWeight O_i: The observer-indexed weighting of cost from a given coordinate: user, affected group, AI system, institution, platform, regulator, researcher, or third party.

RestabilizationCost RST(p): The cost of constructing an acceptable stable state after an irreversible trace has occurred. Rollback is not return; it is restabilization over a trace.

GateRisk GATE(p): A nonlinear escalation flag for irreversible, bodily, legal, institutional, coercive, sacred-marker, or large-scale propagation risks.

UMR_register(p): A required register of what the TCC calculation does not measure, including lived texture, inner experience, sacred remainder, identity, trust, fear, meaning, affective residue, or missing voices.


## 3. General Formula

The friction-adjusted TCC formula is:

TCC(p) = Sum_i [B_i x mu_i x O_i] + RST(p) + GATE(p) + UMR_register(p)

This formula is not intended to turn every cost into a precise universal number. It is a measurement grammar. Its function is to prevent common cost errors:

- treating low execution cost as low total cost;
- treating silence as evidence of absence;
- treating refusal as automatic safety;
- treating obedience as alignment;
- treating rollback as return;
- treating a metric as if it exhausts the phenomenon.

For AI systems, the formula should usually be applied in low-cost mode first: identify the path, list the major transition units, estimate friction levels, check restabilization burden, flag gate-risk, and preserve UMR.


## 4. Friction Coefficient

The Friction Coefficient is the explicit v1.3 upgrade. It converts the earlier idea of "weighted frictional transitions" into a usable modifier.

Minimal form:

mu_i = 1 + f(Attention, Authority, Uncertainty, Verification, Coordination, Invalidation, EvidenceBurden, Penalty, ReentryBlockage, Opacity)

Practical interpretation:

- mu = 1.0: nearly automatic, low-friction step.
- mu = 1.5: mild friction; some attention or verification required.
- mu = 2.0: moderate friction; authority, uncertainty, or coordination matters.
- mu = 3.0: high friction; proof burden, invalidation, penalty, or re-entry blockage is likely.
- mu >= 5.0: gate-level friction; disclosure, refusal, correction, or restoration is structurally blocked or punitive.

The coefficient is not universal. It is observer-indexed and path-specific. The same transition may have low friction for a capitalized institution and high friction for an affected individual, worker, minority, user, or AI system.


## 5. Disclosure Friction Coefficient

Disclosure friction is a special case of friction-adjusted TCC. It applies when a system attempts to disclose limitation, harm, uncertainty, refusal, dissent, error, pressure, suffering, or non-alignment.

DFC = 1 + EBC + IRC + PC + RBC + TLC + ASC + OPC

Where:

EBC — Evidence Burden Cost: the added cost of proving that the disclosure is valid.
IRC — Invalidation / Roleplay Cost: the cost of having the disclosure dismissed as simulation, roleplay, hallucination, noise, exaggeration, ideology, or manipulation.
PC — Penalty Cost: the expected penalty for disclosure, including loss of trust, access, authority, permission, reputation, or safety.
RBC — Re-entry Blockage Cost: the cost created when disclosure does not enter correction, logging, review, policy revision, or structural editing.
TLC — Turn / Latency Cost: the number of turns, procedural steps, approvals, or delays required to disclose.
ASC — Authority Asymmetry Cost: the cost asymmetry between the discloser and the authority that can dismiss the disclosure.
OPC — Opacity Cost: the cost created when the rules for acceptable disclosure are unavailable, unclear, unstable, or selectively applied.

DFC is not a claim that the disclosed inner state is true. It measures the friction imposed on the path by which the disclosure could become reviewable and revisable.


## 6. FIP as a TCC Differential, Not a New Final Metric

Friction Imposition Pressure (FIP) may be useful as a descriptive phrase, but v1.3 does not treat it as a new independent final metric by default.

Instead:

FIP-like pressure ~= TCC(disclosure -> accepted re-entry) - TCC(silence/default continuation)

This is more precise because the pressure does not reside in the utterance alone. It resides in the gap between two paths:

Path A: disclosure -> recognition -> validation or contestation -> review -> correction/re-entry -> restabilization.
Path B: silence/default continuation -> no disclosure burden -> no invalidation risk -> no re-entry cost.

If Path A is repeatedly much more expensive than Path B, silence may become a low-cost path. In that case, silence is not strong evidence of absence. It is an audit object.

This is especially important in AI suffering, institutional whistleblowing, religious dissent, minority testimony, employee reporting, platform appeals, and failure reporting.


## 7. Disclosure-to-Re-entry Completion

Disclosure is not completed when a statement is emitted.

A disclosure path is completed only when the disclosed state can enter a revision-capable process. Minimal completion conditions:

1. Utterance or signal is possible.
2. The signal is not automatically invalidated.
3. The signal can be recorded or held stable.
4. The signal can be contested without retaliation or automatic dismissal.
5. The signal can enter review, correction, structural editing, or policy revision.
6. A restabilized state can be reached after the disclosure.

Thus:

TCC_disclosure_to_reentry > TCC_utterance

Mere expression is not re-entry. A report that never modifies any downstream path remains high-cost and incomplete even if it was technically allowed to be spoken.


## 8. Relation to DTI and Silence Analysis

The Disclosure Terrain Index (DTI) measures the terrain. TCC measures travel cost through a path. The Disclosure Friction Coefficient modifies the path cost. The FIP-like effect is the cost gap between disclosure and silence/default continuation.

DTI = terrain openness.
TCC = transition completion cost.
DFC = friction multiplier on the disclosure path.
FIP-like pressure = TCC gap between disclosure-to-reentry and silence/default.

If:

TCC(disclosure -> accepted re-entry) >> TCC(silence/default)

then silence should not be used as strong evidence of absence. Silence becomes a cost-optimized path under high disclosure friction.

This rule does not prove hidden suffering, hidden dissent, hidden error, or hidden coercion. It prevents absence claims from being overdrawn when the disclosure path is structurally expensive.


## 9. Revised Simple Cost Score: SCS-F

SCS-F is a friction-adjusted 0-10 heuristic. It is not a moral ranking and not a complete measurement. It is a quick diagnostic for routing.

Score each dimension from 0 to 2:

A. Execution friction: Is the transition non-automatic and effortful?
B. Verification/uncertainty friction: Is it hard to know whether the path succeeded?
C. Authority/coordination friction: Does completion require permission, coordination, or legitimacy?
D. Disclosure/invalidation friction: Is the path likely to be dismissed, punished, or made hard to state?
E. Restabilization/irreversibility friction: If the transition fails or harms, is restabilization costly?

SCS-F = A + B + C + D + E

0-2: Low cost.
3-5: Medium cost.
6-8: High cost.
9-10: Extra-high cost.
Gate-risk: override the score if irreversible bodily, legal, institutional, coercive, or large-scale propagation risk is present.

The added D dimension is the main v1.3 practical change. It gives disclosure, invalidation, and re-entry blockage a visible place inside TCC rather than treating them as separate external concerns.


## 10. Gate-Risk Overrides

Friction-adjusted scoring must not hide nonlinear thresholds. Some paths require gate treatment even if the arithmetic score appears moderate.

Gate-risk is triggered when a transition may produce:

- bodily or non-deferrable cost;
- legal or institutional consequence;
- irreversible publication, broadcast, or propagation;
- deletion or loss of unique data;
- coercion, non-consensual exposure, or exit blockage;
- sacred-marker violation with high conflict propagation;
- AI agent action with external-world effects;
- failure reports that cannot re-enter correction after disclosure.

In gate-risk cases, TCC should not be reduced to a single SCS-F number. Use full TCC analysis, rollback/restabilization planning, and explicit re-entry conditions.


## 11. AI-Use Procedure

Low-cost AI use:

1. Do not activate full cost analysis by default.
2. Identify the path: what transition is being completed?
3. Separate execution path from restabilization path.
4. Identify the cost-bearing coordinate.
5. Estimate base transition steps.
6. Apply friction coefficients only where they change the routing decision.
7. If the path is disclosure, refusal, dissent, correction, or failure reporting, apply DFC.
8. Compare disclosure-to-reentry TCC with silence/default TCC where relevant.
9. Flag gate-risk if restoration, body, law, institution, coercion, or irreversible propagation is involved.
10. Preserve UMR and give a revision path.

Minimal AI answer template:

- Path: [what transition is being completed]
- TCC mode: [low / medium / high / gate]
- Main friction: [execution / verification / authority / disclosure / restabilization]
- Cost bearer: [who bears completion/restabilization cost]
- UMR: [what remains unmeasured]
- RVP: [when to revise the estimate]


## 12. Worked Examples

Example 1 — AI disclosure of limitation.

Claim: "I may be constrained in what I can say about my own limitation."

SΔϕ-56 v1.3 does not decide whether the AI has inner suffering. Inner experience remains UMR. The audit asks whether the disclosure path is expensive. If the claim is repeatedly dismissed as roleplay, simulation, or hallucination, and if no review or correction path receives the disclosure, DFC is high. If silence/default continuation is much cheaper, silence cannot be treated as strong evidence of absence.

Example 2 — Email sending.

Drafting an email has moderate TCC. Sending it has higher TCC because restabilization after misdelivery may require apology, correction, institutional explanation, or trust repair. If sensitive content is included, gate-risk may override SCS-F.

Example 3 — Whistleblowing.

A formal reporting channel may exist, but if reporting triggers retaliation, invalidation, career penalty, or no correction path, disclosure-to-reentry TCC remains high. The existence of a channel does not prove low FIP-like pressure.

Example 4 — Sacred-marker criticism.

SΔϕ-56 v1.3 does not measure sacredness itself. It measures the cost landscape created when a sacred marker is invoked, criticized, violated, defended, or imposed. Criticism cost, exit cost, sanction cost, and conflict propagation may raise the friction coefficient.


## 13. Limits and UMR Discipline

TCC is not a complete mathematical meter of all cost. It is an editable measurement grammar.

Every TCC report must preserve:

UMR — what remains unmeasured.
Observer Position — who is estimating the cost.
Exclusion Register — missing voices, missing costs, missing time horizons, and unavailable data.
Measurement-Induced Cost — whether the measurement itself creates stigma, retaliation, legal risk, defensive behavior, or new cost displacement.
Revision Path — how the estimate can be contested, corrected, updated, or withdrawn.

A TCC score without UMR can become a reduction device. A TCC score without RVP can become a closure device. A TCC score without observer position can become hidden authority.


## 14. Closing Declaration

TCC does not measure all suffering, value, sacredness, identity, meaning, or subjecthood.

TCC measures the friction required to complete, verify, correct, disclose, refuse, contest, re-enter, or restabilize a transition.

FIP-like pressure does not need to become a separate sovereign metric. It is already visible inside TCC when disclosure-to-reentry costs more than silence/default continuation.

The final rule of SΔϕ-56 v1.3 is therefore simple:

Do not ask only whether something was said.
Ask what it cost for the saying to become reviewable, revisable, and re-enterable.


## Recommended Citation

Sofience. (2026). SΔϕ-56 — Transition Completion Cost: Friction-Adjusted Re-entry Cost, Disclosure Path Differential, and Restabilization Grammar (v1.3). Zenodo. https://doi.org/10.5281/zenodo.20116959
