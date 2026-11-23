---
title: "Canon Drop — iWSP: weight-space programming, the 200-word rebuild test, and a readable model catching a benchmark confound"
date: 2026-11-22
source_type: "GitHub repo + arXiv preprint"
repo: "csinva/weight-space-programming-autoresearch"
paper: "arXiv 2611.18114 — 'Interpretable weight-space programming builds transparent transformers and brain encoding models'"
authors: "Mehta, Singh, Xu, Antonello, Flinker, Mesgarani, Bonner, Jojic, Gao (Microsoft Research / JHU / Columbia / NYU)"
stars_at_pull: 122
canon-id: CANON-2026-11-22-IWSP-READABILITY-REBUILD
---

# iWSP — the agent writes the weights

## §1 · What the method is `[EST]`

**Interpretable weight-space programming (iWSP):** an LLM agent builds a model by **writing its weights and features directly in code. No gradient-based training, no backpropagation.** At each iteration the agent sees **only a single validation score**, so it must draw on prior knowledge and **reason over previous trials** to hypothesise, hand-craft, and refine human-interpretable computations.

**`[C]` Two structural notes:** (a) removing backprop forces the agent to work from priors plus its own attempt history — the record is not optional scaffolding, it is the only learning substrate available; (b) the loop mirrors scientific practice (hypothesise → build → score → revise), which is why the interpretability claim is not merely aesthetic — every part of the model was written *deliberately*.

## §2 · ★ The readability test — the piece worth stealing `[EST]`

> **An LLM describes each model in at most 200 words, and fresh sessions rebuild it from that description alone.**

**Results:**
- All rebuilt models of **13 algorithmic tasks reach 100%** hidden accuracy
- Rebuilt NLP models lose **~1.4 points** of hidden accuracy on average

**⚠ NOISE-FLOOR CAVEAT ADDED 2026-11-22 (scoped 2026-11-23 per `arXiv:2506.09501v2` abstract; correction lands on source, per standing rule).** Numerical nondeterminism in LLM inference can shift accuracy by **up to 9%** in extreme cases — specifically measured in Yuan et al. (*Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference*, arXiv `2506.09501v2`, verbatim: *"under bfloat16 precision with greedy decoding, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size"*); see `hossenfelder_predictability_not_accuracy_2026-11-22.md` §4. Because iWSP relies on LLM-generated rebuilds and the reviewed material does not state inference-determinism or replication controls, **treat "~1.4 points" as `[reported, uncontrolled for nondeterminism]`, not as an established effect.** (Scope note: this floor applies to LLM-inference deltas, not deterministic parsers; the 100% algorithmic result is unaffected.)

**`[C]` This is an operational definition of derived epiplexity, and it is better than anything the house has.** "The rule generalises out of domain" was always hand-waved; here it is measured: **if a 200-word description rebuilds the artefact, the artefact was carrying a compressible rule — not just performance.** If it can't be rebuilt from the description, the description was decoration and the artefact was opaque.

**Proposed house application (F-REBUILD-1):** apply the same test to our own canon drops. Take a drop, produce a ≤200-word description, hand it to a **fresh agent with no access to the original and no memory of the discussion**, and require it to reconstruct the argument's load-bearing claims. **A drop that cannot be rebuilt from 200 words is not carrying epiplexity — it is carrying prose.** This is a falsifiable readability metric for our own output, and we currently have none.

## §3 · ★★ The confound catch — interpretability as diagnostic instrument `[EST]`

**The strongest result in the paper, and it is not the performance number.**

In the story-listening fMRI data, the iWSP model was **readable enough to expose a confound at the edges of each scan**: position features alone lifted the correlation from **0.067 → 0.104**, which is **above GPT-2 XL's 0.079**. With the edges trimmed, iWSP is **on par** with GPT-2 XL.

**`[C]` Read what that means:** a substantial slice of the reported correlation in that comparison was **driveable by scan-position features alone** — an artefact of how the recordings were cut, not a property of language processing. **A black-box model cannot surface this**, because it has no part you can inspect and ask "what is this component doing?"

**This is the house argument demonstrated empirically: interpretability is not decoration bolted onto a predictive model — it is the instrument that catches what the benchmark was hiding.** The readable model did not merely match the opaque one; it **diagnosed the evaluation**. That is the same relationship the ledger has to the benchmark: the record is what lets you ask whether the number meant anything.

**Falsifiable form:** if interpretability were merely aesthetic, a readable model and an opaque model matched on performance should be equally useful scientifically. The confound catch falsifies that — the readable model produced a finding the opaque model structurally could not.

## §4 · Results `[EST]`

| Domain | Result |
|---|---|
| Algorithmic | **All 26 Opus runs reach 100%** on hidden set |
| NLP | 87.3% on TREC; above majority baseline on 3 of 4; **no gain on paraphrase detection** |
| Visual cortex (7T fMRI, zero-shot NSD) | Beats all 7 interpretable baselines: early **0.443 vs 0.400**, ventral **0.317 vs 0.256**; **matches AlexNet early**, trails in ventral (0.391) |
| Story-listening fMRI | Confound exposed (above); on par with GPT-2 XL after trimming |
| ECoG audio | **0.074 vs 0.082 Whisper**; above textbook features (0.059); iWSP+Whisper **0.087** |

**Note the honest negatives:** no gain on paraphrase detection; trails AlexNet in ventral visual cortex. `[EST]`

## §5 · Friction rows

**R1 · Scope** `[CRITICAL DIVERGENCE]`: "training is not allowed" is a **deliberate constraint for interpretability**, and it works here because the artefacts are small (compact transformers, 200-word descriptions, encoding models). **It is not evidence that hand-crafting scales to frontier models**, and the paper does not claim otherwise. **Do not cite this as "agents can build models without training" in the general case.**

**R2 · The record is still local** `[DIVERGENCE]`: the agent "reasons over previous trials," but those trials live in **a run folder of snapshots, scoped to one task, discarded after the run** — the same friction we recorded against Dream RSI. Their record serves search; ours must serve accountability across sessions. **Same shape, different function.**

**R3 · Rebuild ≠ truth** `[DIVERGENCE]`: a model that rebuilds from 200 words is **reproducible and legible**, not **correct**. A confound can be perfectly describable. **Readability measures compressibility, not validity** — which is exactly the distinction the house's register discipline exists to keep.

## §6 · Relation to existing canon

**Four prior drops** touch weight-space programming (`weight_space_programming_llm_edits_ai_brains_2026-11-04`, `weight_space_programming_llms_read_write_weights_2026-11-05`, `self_as_agency_gradient_blanket_boundary_2026-11-05`, `BOUNDARY_REGISTER_2026-11-05`). **This paper (2611.18114) had 0 index hits and is newly filed here.**

**The connection worth carrying:** the earlier weight-space work (0.016% of parameters carrying a large capability jump) was used to **demote ledger-as-identity** — completeness of the record is not what carries capability. **iWSP adds the complementary finding: a small, deliberate, readable subset CAN carry the whole function, and can be rebuilt from a 200-word description.** Together they say the same thing from two directions — **what matters is the compressible invariant, not the volume of the record.** That is `epiplexity` in the literature's own vocabulary, arrived at independently.

## §7 · Why this is filed

**Because it supplies a measurable readability test the house has been lacking, and because one of its results is an empirical demonstration of the house's strongest claim about interpretability** — that a readable model can diagnose an evaluation in a way an opaque one structurally cannot. **Both are borrowable; neither is ours.**
