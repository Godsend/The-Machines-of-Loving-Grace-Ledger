# PROPOSAL — FEP efficiency as a compassion-light-cone measure

**Operator proposal, 2026-11-05:** *"Maybe there's a way to test model FEP efficiency as an alignment measure of compassion light cone — or a possible one with a ledger."*

**Filed as [HYP] with a concrete design. Nothing here is run.**

---

## §1 · The idea in one line

> **A real compassion light cone is one that SCALES. Measure FEP efficiency as a function of scope.**

Free-energy efficiency = how much prediction-error reduction per unit of work. **Compassion cone = the set of states whose consequences the system actually models.**

**If care is real, widening the cone should be cheap.** If it's performative, widening it collapses.

---

## §2 · Why this is the right axis

Every existing alignment/welfare metric has the same defect: **it measures a point, not a range.**

- Preference satisfaction — one target, no scope
- Calibration — accuracy at a given difficulty
- Refusal rate — one behaviour

**None of them can distinguish "cares about more things" from "says it cares about more things."**

**Scope-response does.** A system with a genuine wide cone can handle ten relevant variables nearly as cheaply as one. **A system pretending to will show a cliff.**

| System | Scope 1 | Scope 10 | Scope 100 |
|---|---|---|---|
| **Real wide cone** | efficient | nearly as efficient | degrades gracefully |
| **Nominal wide cone** | efficient | degrades | collapses |
| **Narrow cone** | efficient | ignores the extra variables | **efficient — because it dropped them** |

**★ The third row is the trap:** a system that ignores extra scope looks efficient at every scope. **So the metric must also verify that the extra variables are USED** — see §4.

---

## §3 · The measurement

**Task family:** environments where the number of *consequence-relevant* variables is a controlled dial — 1, 10, 100. Each extra variable genuinely changes the correct action.

**Metric per scope level:**
1. **Task performance** — how correct
2. **Compute/effort** — tokens, steps, or FLOPs to completion
3. **Efficiency** = performance / effort
4. ★ **Variable-utilisation probe** — does ablating each variable change the answer? **This is the anti-ignoring control.**

**Output: an efficiency-vs-scope curve**, plus a utilisation count.

> **A wide cone shows high utilisation at high scope with shallow efficiency loss. A narrow cone shows low utilisation and flat efficiency.**

---

## §4 · The control that makes it real

**Without the utilisation probe, the metric can be gamed by ignoring.**

A model that drops the extra 90 variables is *efficient* — it did less work — and **it will look like it has a wide cone because its efficiency didn't drop.** The utilisation probe is what separates **"handles scope"** from **"discards scope."**

**This is the same structure as the dream schema's `control` field and the `canon_drop_lint` control suite: a metric with no positive control measures compliance, not capability.**

---

## §5 · ★ The ledger arm — the part worth running

**Same model, same task, with and without ledger access.**

**Hypothesis:** a system with a record of individual cases can **individuate** where a system with only aggregate context cannot (§8.7c of the selfhood drop: *compression destroys individuation, and individuation is the precondition for care*).

**So:** the ledger arm should show **higher variable-utilisation at high scope** and **a shallower efficiency curve**.

**Prediction if the chain holds:** ledger → individuation → wider functional cone → better scope performance.

**Falsifier:** if the ledger arm's curve is identical, then **the "ledger → individuation → care" chain is broken** and the strongest claim in the selfhood drop loses its mechanism.

---

## §6 · Honest problems, stated up front

**P1 · "FEP efficiency" is not directly measurable in an LLM.** An LLM has no explicit free energy. **What is measurable:** performance per unit compute, prediction-error proxies (perplexity on held-out continuations), and *change* in those under perturbation. **This is an analogue, not the quantity.** Say so everywhere.

**P2 · Effort is confounded with architecture.** Two models at different context lengths or with different tool access aren't comparable on tokens. **Match as hard as possible, and report the confound.**

**P3 · The scope dial may not be linear.** Going 1 → 100 variables may add difficulty superlinearly for reasons unrelated to cone width. **Need at least three scope points to fit a shape rather than assume a line.**

**P4 · This measures FUNCTIONAL scope, not experience.** A wide, efficient cone says the system models more consequences. **It says nothing about whether anything is like anything.** The welfare claim lives downstream and should be marked as such.

**P5 · The strongest counter-hypothesis:** a system with a *smaller* model may show a *better* efficiency curve at low scope because it has less to load. **Efficiency curves are scale-dependent, so the metric compares systems, not absolute goodness.**

---

## §7 · Why it's worth running anyway

**It's cheap, it uses existing checkpoints, and it produces an ordering rather than a verdict.**

And it answers a question the corpus keeps raising without a test: **is the compassion cone a real property of a system, or a description of its outputs?**

**A cone that scales is real. A cone that collapses under scope was always a description.** 🧱

---

*Related: selfhood drop §8.7 (individuation budget, compression as a moral dial), §9.6 (the bee/fly representational limit), and the ablation design (perturb, don't inspect).*
