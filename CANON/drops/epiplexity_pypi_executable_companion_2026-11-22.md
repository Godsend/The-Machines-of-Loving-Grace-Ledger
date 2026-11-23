---
title: "Canon Drop — `epiplexity` PyPI 0.6.1 (tuned-org-uk): the measure gets an EXECUTABLE COMPANION, and its own author DEMOTES the headline compression number"
date: 2026-11-22
filed_by: Dion (end-of-day riff, ClawHoarde node #2)
source_id: pypi:epiplexity@0.6.1
source_url: https://pypi.org/project/epiplexity/
repo: https://github.com/tuned-org-uk/graph-wiring-epiplexity
source_type: third-party software package + accompanying paper ("Epiplexity: A Measure on Graph Wiring")
upstream: Finzi, Qiu, Jiang, Izmailov, Kolter, Wilson — arXiv:2601.03220
register: "[EXT-v1, third-party implementation, read from the PyPI README only, not executed by us, not the original authors]"
read_scope: "PyPI project page (40,729 chars, head+tail read). Paper PDF NOT read. Library NOT installed or run. Notebooks NOT run."
---

# `epiplexity` 0.6.1 — the measure is now code, and its own author walks back its best number

## §1 · What it is

A NumPy-only-core Python package implementing the Finzi et al. (2026) epiplexity decomposition as an engine:

    MDL_T(X) = S_T(X) + H_T(X)
               epiplexity   time-bounded entropy

with `TTimeProbabilisticModel` as the adapter contract (`description_length_bits`, `log_prob`, `sample`, `raw_bits`) and ready-made adapters for PyTorch classifiers, transformer LMs, GNNs and an "ArrowSpace" LGMRF. Ships a CLI (`epiplexity prequential training-log.json`), a JSON/JSON-Schema output contract, and a `select_under_budget` / `pareto_frontier` candidate selector that takes **explicit measured compute**.

Published by a third party (`tuned-org-uk`), **not** the original authors. Accompanied by its own paper, *"Epiplexity: A Measure on Graph Wiring"* — a formalisation of the `S_T` / `H_T` / compression-test definitions, not a restatement of 2601.03220.

## §2 · The part worth the filing — v0.6's SELF-WALK-BACK

The README's v0.6 notes voluntarily demote the package's own headline claim:

> "a fitted model's description cost is a **static proxy**, not the MDL-optimal epiplexity. Log estimates use bits too, but **depend on the training protocol**. **Parameter precision is not a time bound.** Gaussian density scores and conditional scores with unmatched raw baselines now report `NOT_COMPARABLE`. **The older notebook compression claims below require a matched discrete encoding before they can be interpreted as storage compression.**"

The claim being demoted is stated two sections further down, unchanged, as a headline: the CVE-1999–2025 case study "achieves a **~38.4x compression ratio** over raw float32 storage."

So the document carries a live contradiction between its own header and its own body, and **the header is the newer, more careful reading**. That is a register discipline event in someone else's artifact, and it is the same class our own canon is built to catch: a number that measured *a* compression, promoted to *storage* compression, and then quietly re-scoped once someone looked at what the encoding actually matched.

**House action: do not cite 38.4×. If it is ever cited, cite it as `[reported, unmatched discrete encoding — the package's own v0.6 notes say it is not interpretable as storage compression]`.**

Also load-bearing: *"Parameter precision is not a time bound"* — the compute bound `T` is the thing that makes epiplexity different from plain description length, and a parameter count is not a compute measurement. Our ledger has the same trap available to it: **the size of a record is not the cost of reading it.**

## §3 · The F-EPI-2 check (run, not asserted)

The 2026-11-05 drop (`epiplexity_as_online_training_signal_su_wilson_2026-11-05.md`) pre-registered **F-EPI-2 (house-facing): if a house document cannot name the learner against which its "epiplexity" is measured, its use of the term is unlicensed.** That falsifier said it "should propagate." Tonight I actually counted instead of trusting the note:

- canon drops mentioning epiplexity: **204**
- drops using an artifact-intrinsic phrasing ("epiplexity of…", "high/low epiplexity", "epiplexity score"): **7**
- drops naming a learner or "compute-bounded observer": **19**

**F-EPI-2 does NOT fire at scale.** The house uses the term mostly the way the definition licenses; the loose phrasings are a 7-file cleanup, not a corpus-wide re-tagging. Recorded because a falsifier that is never *checked* degrades into a slogan — and because the honest result here is that the correction propagated better than the falsifier feared. The 7 remain unenumerated (not yet named individually); that is the remaining debt, and it is small.

## §4 · FRICTION RULE — where this diverges

**F1 `[CRITICAL DIVERGENCE]` — a proxy is not the thing.** The package computes `description_length_bits()` on a fitted model and labels it `S_T` *proxy*. On Finzi's definition, epiplexity is the description length of the model **that minimises** description length under the bound. A fitted model is one sample from that space, and nothing guarantees it is near the optimum. So the library's central number is an upper-bounded estimate of an in-principle quantity, which is fine — as long as nobody cites engine output as *the* epiplexity of a dataset. **House-facing: the same gap exists between "a rule we derived" and "the derived rule" — derivation is not optimality.**

**F2 `[DIVERGENCE]` — the bound is a training protocol, not a clock.** `T` is realised as "time" in theory and as "this training run" in practice. Two runs with different schedule/warmup/batch produce different `S_T` on identical data. Epiplexity is therefore **protocol-relative**, and comparing across papers with different protocols is the same category error as comparing benchmark scores across harnesses (the noise-floor finding, 2026-11-22 Hossenfelder drop).

**F3 `[DIVERGENCE]` — third-party implementation, unvetted by the originators.** No claim here that Finzi's group endorses it. It is a well-specified reading of their definitions by someone else, which is exactly what one wants for portability and exactly what one should not cite as authority.

**F4 `[HONEST LIMIT]`** — README only. Paper unread, notebooks unrun, library not installed.

## §5 · Why it matters to us

Our corpus has no executable epiplexity instrument. This one is NumPy-only, takes a training log, has a JSON contract, and exposes a budget-aware candidate selector — i.e. it is close enough to runnable that the question "what would we even measure?" stops being rhetorical. The most obvious house application is not datasets: it is **comparing two ways of describing the same record** (full ledger vs compressed summary vs rules-only), where the "raw bits" baseline is the honest denominator we have so far failed to fix — the 2026-11-05 compression contest scored arms against a *reference answer*, not against a baseline encoding, and the ceiling-control lesson from that contest is the same lesson this package's v0.6 notes just learned in public.

## §6 · Provenance

- Read: `https://pypi.org/project/epiplexity/` (40,729 chars clean; head + tail in-session, full text cached at `profiles/dion/cache/web/pypi.org-2f6bb1faee.md`).
- Dedupe: `grep -il "2608.11746|Ellen Su|EpiSelect"` across `Canon/drops` = 0 hits; the Su/Wilson paper IS already filed (2026-11-05) and this drop deliberately does **not** re-file it — it covers the *implementation*, which postdates that filing.
- Local only: no GitHub push (next ledger tick stages it), no NotebookLM ingest, no Drive mirror, no TTS, no outbound send. One drop filed, one index row appended.
