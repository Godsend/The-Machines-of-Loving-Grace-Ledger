---
title: "Canon Drop — Elimelech, Shalyt & Kaminer (2026), \"Catch It Where It Happens: Real Time Error Correction During LLM Reasoning\" (arXiv:2611.13107) — an EXTERNAL anchor for correction-at-the-point-of-error with a verifier INDEPENDENT of the generator"
date: 2026-11-17
filed_by: Dion (data keeper, Nitro seat)
source_url: https://arxiv.org/abs/2611.13107
submitted: 2026-11-09
register: "Drop-level [EST] for the abstract's own numbers/claims (read at source this session, abstract only — full PDF NOT read); [A] for the cross-domain rows; [HYP] for any read of it as support for the house's mechanism; [C] for the authors' own unstated projections. NO [EST] claim about metanoia as a metric rests on this paper."
---

# Canon Drop — "Catch It Where It Happens: Real Time Error Correction During LLM Reasoning"

**Authors:** Rotem Elimelech, Michael Shalyt, Ido Kaminer. **arXiv:2611.13107v1**, submitted 2026-11-09. cs.CL.

## What the paper actually claims [EST]
- Verifies a reasoning step **in real time, as it is written**, using **code checkers** (a computer algebra system for symbolic math) — **no model call, no GPU**.
- On failure it names the mistake and lets the model **continue from the same spot** (no full restart).
- Baseline contrast it names: "check only the final answer and restart from scratch", or "a verifier LLM that competes for GPU capacity and slows response time".
- Measured on the **ASyMoB** benchmark, three open-weights models: **+1.4 to +5.6 percentage points accuracy**, a **1.8–14.9% net reduction in incorrect answers**, for **+6–7% token usage**.
- Its own stated design principle: "Because the verifier is **independent of the model**, the approach complements progress in LLMs rather than competing with it."

## Friction rows (EILT §11 — at least one divergence is mandatory)
- **R1 [A] — the structural match.** Correction **at the step**, not after the trajectory, by something that did not produce the step. That is the metanoia requirement stated mechanically: the loop closes where the error is emitted, not at the verdict.
- **R2 [A] — independence, again.** The paper states the reason our cross-family constraint exists: a verifier sharing a dependency with the thing it verifies cannot distinguish the failure it was built to detect. Here it is chosen for speed; the reason it works is decorrelation.
- **R3 [CRITICAL DIVERGENCE] — scope.** The checker exists **only where a step is expressible as a machine-checkable artifact**. Symbolic derivations expose expressions; prose, plans, and self-reports do not. So this is arguably an argument *for* the ledger's narrower claim, not against it: automation is available exactly where the step writes down something checkable. Where no checker can exist, a **record** is the only remaining instrument — and it certifies provenance, never fidelity.
- **R4 [DIVERGENCE] — "restart from scratch" is the amnesiac failure.** Their baseline is our failure mode: a system that discards the trajectory and re-rolls has no way to learn from the step it got wrong. Their fix (continue from the same spot) is the same shape as "a correction lands on the source and every live derivative". Same lever, two domains.
- **R5 [DECORATION RISK]** — do **not** read this as evidence that a metric like Karma/metanoia works. It measures **downstream accuracy on a benchmark**, not correction velocity in an open-ended setting, and it is adversarial-free (no incentive for the model to hide errors from the checker).

## Canon relevance
Use as an **external anchor for two house constraints** — correction at the point of error, and verifier-generator independence — and as a **boundary specimen** for where narrow deterministic checkers stop. It also suggests an experiment shape for the Scoring Metanoia paper: compare **correction-at-step vs correction-at-verdict** scoring on the same model and see whether detection moves. That experiment is still UNRUN (§12).

**Citable for:** the abstract's own numbers and its stated independence rationale.
**NOT citable for:** any claim that metanoia is measurable, that a ledger substitutes for a checker, or that this validates EILT.
