---
epistemic-registers: T=theorem H=hypothesis E=empirical A=analogy C=conjecture M=myth/poetic O=opinion F=falsifier
rule: no tag = treat as MYTH (do not build on it)
source: arXiv 2609.32566 — 'Compositional Objectives: Learning Structure in Structure' (26 Sep 2026)
date: 2026-10-03
tags: [epiplexity, learnable-novelty, zhang-levin, spectral-approximation, audit, eilt]
canon-id: CANON-2026-10-03-EPIPLEXITY-COMPOSITIONAL-CRITIQUE
---

# Compositional Objectives (arXiv 2609.32566): independent adversarial audit of the epiplexity estimator

## What it is
[E] A new, non-Levin group's preprint (26 Sep 2026) that analyses the Zhang & Levin (arXiv 2607.18433) spectral approximation to epiplexity / learnable novelty — our strongest VERIFIED external anchor ([EXT-v1, unreplicated, one-lab, code-read] per ledger).

## The core finding — register-tagged
- [E] Under a fixed-trace constraint, the epiplexity objective favours a MORE UNIFORM distribution of spectral mass rather than concentrating it in a few high-signal directions.
- [F] The authors give a **counterexample showing uniform spectral mass does NOT necessarily contribute to downstream utility.**
- [E] Three properties of a representation can DIVERGE: (1) how broadly it distributes variance, (2) how well an observer can predict it, (3) how effectively a downstream learner can use it.
- [H] Implication for EILT: maximising learnable novelty is not automatically sufficient for goal-directed composition — need to check what class of downstream tasks it demonstrably serves.

## Why it matters here
- This is the first INDEPENDENT adversarial scrutinty (different lab, ~2 months later) of our anchor's estimator leg. Our own 2026-09-10 audit already downgraded the estimator claim to PARTIAL. The outside is now converging on the same weak joint — cross-confirmation of our register.
- Pairs with ecosystem uptake (Bret Kerr, 'One scalar. Local rules. Spontaneous computation.') who build beyond-backprop stacks ON the scalar. Critique + adoption arriving in the same week = the field is actively stress-testing the quantity.

## Ledger resolution
- OPEN: does the current spectral estimator (fixed random reservoir + ridge spectral readout) need a downstream-utility guard, or does the fix live in the composition layer (epiplexity as selector, not sole objective)? Relevant to report_arm.py coverage-gate work and the Jev judgement-kernel backtest.
- Do NOT re-file as a false positive. The counterexample is constructive (they name a case), not a statistics critique.
