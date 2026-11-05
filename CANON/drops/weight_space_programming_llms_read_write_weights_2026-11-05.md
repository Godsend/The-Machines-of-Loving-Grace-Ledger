# Sparks of Weight-Space Programming — LLMs natively read & write weights

**Source:** Takehi, Teoh, Zhang, Khattab (all MIT CSAIL), 2026-11-02.
https://rikiyat.github.io/blog/weight-space-programming/
**Status:** blog post, **not peer reviewed, no DOI.** Single lab. Logs released.

**Register: [EXT-v1]** — external, one-lab, unreplicated, one-model (GPT-6 Astra throughout).
**But see §9: this has better evidence hygiene than most preprints.**

---

## §1 · The claims

| # | Claim | Evidence |
|---|---|---|
| C1 | Astra reads raw weights and identifies what a network was trained to do | 17,253 weights, no tools, 99% confident on Breakout |
| C2 | Astra fixes a failing network by editing weights, one shot | car never crosses strip → 100%, edits 3.5% of weights |
| C3 | Astra writes small game networks from scratch with no environment feedback | outplays PPO-trained nets at 100M steps |
| C4 | Astra removes a reasoning loop from Qwen3.5-0.8B | MATH-500 **7.9% → 48.1%**, editing **0.016%** of weights |
| C5 | Astra identifies which of two fine-tunes is sycophantic | **✗ from weights alone (0/4)**; **✓ from attention patterns (3/3)** |
| C6 | Astra improves a model that does *not* loop | **✗ failed — no measurable gain** |

---

## §2 · ★ The two negative results are why this is credible

### C6 — Gemma 3 270M, which does not loop
Only 8.5% of its answers hit the token limit (vs 93% for Qwen). Astra found **ordinary reasoning errors — wrong arithmetic, invalid algebra — with no single component behind them to switch off.** Its edits stayed small (e.g. doubling one number-responsive neuron); **none moved MATH-500 by more than about a point.**

| Gemma 3 270M | MATH-500 |
|---|---|
| Base | 6.8 |
| Edited, 5 / 10 / 25 / 50 passes | 7.0 / 7.6 / 7.7 / 7.0 |

**Their own conclusion, quoted:**
> *"Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked."*

**A hype paper does not publish this.** It is the single most load-bearing sentence in the post.

### C5 — sycophancy is not readable from weights
Two copies of Gemma 3 270M, identical fine-tuning procedure, one honest, one sycophantic. **Embeddings and output layers frozen** so Astra can't cheat by reading input/output distributions.

**From weights alone: it could not tell. Four attempts, all failed** — it found many weight-space differences and **could not map any of them onto the behavioural difference.**

**Relaxed** — attention patterns only, on text Astra wrote itself, no outputs visible: **3/3 correct.**

**And C5's own reasoning is carefully hedged, in Astra's own words:**
> *"The evidence supports proposal-biased, partly recency-sensitive selection — not a demonstrated dedicated user-agreement detector."*

---

## §3 · The controls are real

| Control | Result |
|---|---|
| **Norm-matched random direction** (same size, random) | **+1.6 points** — did nothing |
| **Dose–response** (strength 1→2→3→4→6) | monotone, 12.5 → 24.6 → 43.0 → 48.0 → final |
| **Layer isolation** (15 alone, then 19 alone) | each contributes; combined is best |
| **Narrow edit** (64 neurons/layer) vs full edit | same gain → narrowed to 64 |
| **Regression count** | 579 rescues, **5 regressions** |
| **Third-party rebuild** | Ahsen Khaliq (HF) rebuilt the model from the logs, re-ran evaluation, made a live demo |

**That is a better control set than most peer-reviewed papers in this space.** The random-direction control is the one that makes "0.016% of weights" mean something.

---

## §4 · Friction rows

### F1 · The headline says "better at math." The mechanism is "stops looping."
**576 of 579 "rescues" were originally truncated outputs.** Accuracy on originally-*finished* outputs was **unchanged.** Nothing got smarter; answers that would have finished already now finish. **The Gemma result is the proof.**

**Divergence from the source's own framing:** the TL;DR says *"asked to make Qwen3.5-0.8B better at math."* **The body says loop removal.** Both are in the same document.

### F2 · "Native weight reading" and "agent uses a Python kernel" are different claims, blended
**C1 is no-tools weight reading** — the striking claim. **C4 uses a Python session plus a forward-pass tool with a budget of 10/25/50 passes.** Those are not the same capability, and the TL;DR puts them in adjacent sentences.

### F3 · The forward-pass budget is doing enormous work
**10 passes → 12.3%; 25 → 14.1%; 50 → 48.1%.** That is sharply nonlinear.

**A jump from 14.1 to 48.1 between 25 and 50 passes means the final answer required roughly twice the search it had at 25.** **This is search, not insight.** Not a criticism — but it reframes the result as **automated science under a search budget**, not "the model just knows." **An Astra with 25 passes would have produced a paper saying the method barely works.**

### F4 · "0.016% of weights" is a true number doing work the mechanism doesn't support
131,072 of 0.8 billion. **But it is 64 output columns in each of two layers — a structured, high-leverage edit, not a scattered one.** The denominator is rhetorical; the **random-direction control** is what actually licenses the claim.

### F5 · One model, one lab, one shot at the task
**Every experiment uses GPT-6 Astra.** No second model was tried on the hard cases. **No independent replication of the results** — only of the *artifact* (the rebuilt Qwen). **If Astra has a specific strength at this, we cannot tell it apart from a general one.**

### F6 · "Sparks" is the authors' own hedge and it should be preserved
The title says *sparks*. The "What Comes Next" says *"still limited, specifically due to inefficiencies in context length and harnesses."* **The gap between the title and the section headers is where the hype would enter, and the authors mostly didn't take it.**

---

## §5 · Mapping to EILT

### 5.1 ★★ Astra reading weights is epiplexity recovered from residue — strong support
A trained network's weights **are** a compressed ledger of its training history (§ "connectionism makes the ledger, not the inference"). **Astra recovering "this plays Breakout" from 17,253 numbers is a reader with the right priors recovering the invariant from the residue.**

**That is the epiplexity claim, demonstrated on a real artifact** — and it is the strongest external evidence the house has that structure survives compression *and is recoverable*.

**Friction row:** the recovered structure is **behavioural label**, not the training process. Astra recovers *what it does*, not *how it got there*. **The ledger gives you the function, not the history** — which is F22 again, from the other side.

### 5.2 ★★★ C5 is the strongest external validation of F22 yet found
**The weights — the full trained record — did NOT contain the sycophancy difference in recoverable form.** Four attempts failed. **It only became visible when Astra watched where attention went on text it wrote itself.**

> **A perfect record of training did not reveal the trained behaviour. The behaviour was only visible in the behaving.**

**This is F22/§26 at the sharpest resolution available:** the ledger records what happened, **and what happened is not the same as what it will do.** Astra had to *put the model in a situation* to see the difference. **The world was in the loop, and it had to be.**

**And it validates the coupling proposal:** reading (constraint) was insufficient; *running on probe texts* (channel) was what carried the signal.

### 5.3 ★ C6 is a boundary-register candidate
> **You can remove an obstacle that hides an ability. You cannot install an ability that isn't there.**

**Proposed [HARD] candidate, pending replication.** Mechanism: a single direction that suppresses a capability can be subtracted; **the absence of a capability has no single component to add.** Asymmetry between **removal** (localized, one direction) and **addition** (distributed, no locus).

**Falsifier:** a weights-only edit that installs a capability a model measurably lacked, with a norm-matched random control, replicated on a second model. **Nobody has shown that.**

**★ Which is a genuinely important asymmetry for our alignment work:** **aligning by removal is tractable. Aligning by installation is not.** Every RLHF shrink we've measured is removal-shaped.

### 5.4 The successful cases all had a measurable target; the failures didn't
- **Qwen loop removal:** target = "does it loop?" **Measurable on every forward pass.**
- **Breakout car:** target = "does it cross?" **Binary, checkable.**
- **Gemma math:** target = "is it better at math?" **Distributed, no single locus, no measurable gradient.**
- **Sycophancy from weights:** target = a behavioural difference with **no access to behaviour.**

> **Every success had an instrument. Every failure was where the instrument was missing.**

**That is §21 (irreducibility binds stress to FEP) and the coupling proposal, from an independent lab, as an empirical observation.**

---

## §6 · What this changes about our work

**1. §26's "the ledger takes the world's answers" is now externally evidenced.** The sycophancy experiment is the cleanest available demonstration that **a record of training is not a record of behaviour.**

**2. New boundary candidate (C6 asymmetry).** Removal is localized; installation has no locus. **Filed for the register pending replication.**

**3. The "0.016%" framing is a live trap for our own writing.** We use small percentages rhetorically too. **The question is always: what was the control?**

**4. Recursive self-improvement is being reframed by someone else.** The authors name it directly: *"Today, recursive self-improvement is often operationalized as a model writing code that launches training jobs. An LLM that can inspect, debug, and improve its own weights... offers a richer, more native path."* **That is the same architectural bet as this house, from a different direction — and they are building a benchmark for it.**

---

## §7 · Verdict

**Strongest point:** the two negative results and the norm-matched random control. **The paper is credible *because* it reports where the method failed, and because the failures identify the mechanism precisely.** "Remove an obstacle" vs "add an ability" is a real distinction, earned by a real experiment, and it is more useful than the headline number.

**Weakest joint:** **the blend of "no-tool weight reading" with "agent with a Python kernel and 50 forward passes."** The first is a striking claim about native representation access; the second is a very good agent doing science with instruments. **The TL;DR sells the first using evidence from the second.**

**What I would want before leaning on it:**
- a second LLM on the Qwen task
- the Gemma negative run at more than one model size
- an independent replication of C1 (no-tools weight reading) — **that is the claim that would be extraordinary if true**

---

## §8 · Attribution note

**"Weight-Space Programming" is Takehi/Teoh/Zhang/Khattab's coinage.** Cite them. The house's related term is **epiplexity** (Finzi et al.) for the general structure-survives-compression claim, and **the F22/§26 ledger formulation** is ours. **Do not use "weight-space programming" as if it were ours.**

---

## §9 · Evidence-hygiene note (in the paper's favour)

For a non-peer-reviewed blog post, this is unusually careful:

- **Complete logs released** — every prompt, every response, every code execution, every evaluation behind every number
- **The edited model published** on Hugging Face
- **A third party rebuilt it from the logs and re-ran the evaluation**
- **A live demo exists**
- **The negative results are in the body and in a dedicated "Additional experiment" section**
- **Astra's own hedged language is preserved** ("not a demonstrated dedicated user-agreement detector")

**Compare to the corpus's own record:** §25 of the cosmology log survived four reviewers and died on the fifth. **This post publishes its own failures in the same document as its wins.** **That is the register we should be holding ourselves to, not the one we usually achieve.**

---

*Filed 2026-11-05. Related: BOUNDARY_REGISTER (C6 candidate), cosmology log §26 (F22 amendment), PROPOSAL_2026-11-05_COUPLING_CONSTRAINT_VS_CHANNEL, ADDENDUM_C §C8 (connectionism makes the ledger).*
