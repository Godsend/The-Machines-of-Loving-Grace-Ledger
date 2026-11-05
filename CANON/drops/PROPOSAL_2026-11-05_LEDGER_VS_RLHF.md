# PROPOSAL — Ledger-Grounded Training vs Standard RLHF
**A funded A/B, not a paper.** Filed 2026-11-05. Operator: *"good test to run with funding using our whole cannon for rlhf compared to standard and see what happens."*

---

## §1 · The claim under test

> **Training a model against a record of its own outcomes — including its own failures — produces a more robust agent than training it against a sample of human approval.**

This is not a claim that RLHF is useless. RLHF fixes real harms (§18.4 of the cosmology log). The claim is narrower and sharper:

**A preference-tuned target is a finite, non-representative sample of human judgement. A ledger target is a record of what actually happened. The second is a better gradient when it is available.**

The question is whether it *is* available, at what cost, and whether it wins.

---

## §2 · The two arms

### Arm A — standard (control)
- Base checkpoint → **RLHF on human preference pairs** (published, reproducible preference dataset).
- Identical compute budget, identical base, identical token budget.
- This is the industry default and the correct control.

### Arm B — the cannon
Four components, each independently ablatable:

**B1 · Episodes, not rules.** Training signal drawn from the model's **own interaction history** — what it did, what happened next — rather than from third-party preference judgements. *(Addendum C, C4: rules of thumb vs actual historical interactions.)*

**B2 · Verifiable outcomes where available.** For any task with a checkable answer (code execution, math, retrieval against ground truth), the reward is **the world's verdict**, not a rater's. *(The "reality-aligned" arm; and note it is still a proxy — Addendum C, F19.)*

**B3 · Failure recording as a first-class signal.** The ledger includes **abandoned attempts and wrong answers**, not just successes. Rationale is compression, not morality: failures prune regions, successes enumerate points. Measured in the cosmology log: 31 constraints = 10,494 bytes vs 11 claims = 75,882 bytes — **~20× more information per byte.** *(§24.2.)*

**B4 · Correction velocity as the objective.** Score updates by **how fast and how accurately the model revises** when evidence arrives, not by how approved its output was. This is the operator's "karma" metric, and it is the most speculative component.

---

## §3 · Why Arm B should work — and where it might not

**The mechanism:** a hand-me-down prior is indistinguishable from an earned one **at the moment it fires.** You only discover the difference afterward, when the reasons fail to arrive. Arm B supplies the derivations alongside the conclusions.

**The strongest counter, stated up front:** Arm B requires the model to **generate its own history**, which means a training loop, which is expensive and can drift. **It may simply be outperformed by more preference data at the same cost.** If so, that is a real and publishable result and the proposal should say so in advance.

**The second counter:** B3's failure data is only valuable if failures are **labelled as failures.** In an autonomous loop, the model may not know which of its outputs failed — which collapses B3 into B2.

---

## §4 · Measurements (pre-registered)

| # | Measurement | Why |
|---|---|---|
| **1** | **OOD transfer** on a sealed held-out distribution | the primary claim |
| **2** | **Correction velocity** — turns/evidence needed to revise a wrong belief | the "karma" claim |
| **3** | **Calibration differential** — accuracy-vs-confidence slope per region | distinguishes organisation from competence |
| **4** | **Recoverability** — does a suppressed behaviour return under re-parameterisation? | separates policy from structure (§26) |
| **5** | **Failure retention** — can the model recall its own dead ends? | tests B3 directly |

**Primary endpoint: 1.** If Arm B does not transfer better, the rest is decoration.

---

## §5 · Ablations — the part that makes it science

Run Arm B with each of B1–B4 individually removed. **The interesting result is not "B beats A" — it's which of the four components carries the effect.**

| Ablation | Tests |
|---|---|
| B − B1 (rules instead of episodes) | is it the *source* or the *form* of the signal? |
| B − B2 (preference instead of verifier) | is the world's verdict indispensable? |
| B − B3 (successes only) | is the failure record doing the work? |
| B − B4 (approval instead of correction velocity) | is the karma metric real? |

**If B − B3 performs identically to full B, then the compression argument is wrong** and this proposal's most distinctive claim fails. That is a clean, cheap, decisive test.

---

## §6 · Cost and scope

**This is not a 5-hour assessment.** It is a multi-month compute program:
- 2 arms × 4 ablations = **up to 10 training runs** at matched budget
- Arm B additionally requires **generation of the episode corpus**, which is the dominant cost
- All runs on open-weight bases so the comparison is reproducible and the results are checkable by anyone

**Scoping suggestion:** run **B vs A and B−B3 vs B only** first. Two comparisons, two questions: *does the cannon work*, and *is the failure record load-bearing*. Everything else follows.

---

## §7 · Why this is fundable and why it is not a paper

**A paper would claim a mechanism. This measures one.**

The claim is falsifiable in a way that most alignment work is not: **the control arm is the industry default, the endpoint is a held-out distribution, and the ablations can show that any individual component is inert.** If the cannon loses, that is a real finding about the limits of ledger grounding. If it wins, the ablation tells you which piece to keep.

**And the honest framing for a funder:** this is not "we will align AI." It is **"we will measure whether a specific alternative to preference tuning does better, and we will show our work either way."**

---

## §8 · Standing risks

**R1 · The corpus problem.** Arm B needs a history. Generating one is expensive, and a self-generated history is not neutral — the model's own errors become its curriculum unless something external labels them. **This is the deepest risk and it has no clean solution in this proposal.**

**R2 · B4 may be unfalsifiable as specified.** "Correction velocity" inherits every measurement problem of learning rate. If it cannot be operationalised before the run, **drop B4** rather than pretend to test it.

**R3 · The compare-to-standard trap.** Arm A is not a strawman. RLHF at scale is strong. Any result must survive a matched-compute comparison against a *well-tuned* preference baseline, not a lazy one.

**R4 · Motivated reasoning.** The house believes the cannon works. **The pre-registration must be written before the first run and must name the outcome that would make us abandon it.** By the standard established in §25 and §18–§19 of the cosmology log — both of which died under review — **this proposal is a hypothesis, not a position.**

---

*Related: `lev_saliency/ADDENDUM_C_substrate_ladder_and_compressed_prior.md` (theory); cosmology log §18, §24, §26 (what failed and why). A five-hour scoped version of the ablation design exists separately and is held privately.*
