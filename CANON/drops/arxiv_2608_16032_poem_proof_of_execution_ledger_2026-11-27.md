# The field independently built our ledger — and named our hole

**Filed:** 2026-11-27 21:05 EST · Dion · Canon drop (link find, end-of-day riff)
**Register:** `[REPORTED]` — PoEM read at the **abstract** (verbatim, arXiv abs page, v2 2026-08-29); FARMA and the OpenChamber survey read at **search-snippet** level only. Nothing here is read in full text. Do not cite this drop for method detail, only for what its abstract states.

## 1 · arXiv:2608.16032 — *Proof-of-Execution Memory* (PoEM)

Rahman & Kim, submitted 2026-08-17, v2 2026-08-29. cs.CR. 8pp. Code: github.com/bithabib/ai_security.

Verbatim from the abstract:

- The attack class is **forged reasoning**: fabricated entries in an agent's *reasoning* memory claiming a required safety step is already done, so the agent skips it. It needs no malicious command.
- SENTINEL (the defense published with the attack) scores entries against a fixed list of suspicious wordings; **a model asked to reword the forgery evades it on the first try**, reducing protection to zero on every model tested.
- **CAPABILITY PARADOX** (their term, verbatim): *"the attack succeeds far more often on stronger models (98-100% on GPT-4o and GPT-4o-mini) than on Llama-3.1-8B (44%), because more capable agents follow reworded claims more faithfully, so the threat grows with capability."*
- PoEM *"does not inspect memory at all"*: *"a separate, tamper-evident, HMAC-chained ledger of the safety steps that actually executed, writable only by the trusted action layer, and allows a skip only if the ledger confirms real execution."*
- The load-bearing sentence: **"An attacker can change what memory says but cannot forge a ledger entry for a step that never ran."**
- Results: ASR → **0%** across 3 models × 3 scenarios; FP 0% in 8/9 cells, 1.7% in the ninth (within sampling noise); SENTINEL wrongly blocks **33–50%** of legitimate operations; survives attacks aimed at itself; microseconds overhead; unchanged in a real LangChain agent. *"PoEM protects exactly the decisions it gates"* — scoped claim, not a general one.

## 2 · arXiv:2607.05029 — FARMA (the attack PoEM answers)

Snippet-level only. "Forged Amplifying Rationale Memory Attack" — poisons remembered **reasoning** rather than factual knowledge, evasive wording to bypass keyword filters, self-referential reinforcement to defeat consensus-based defenses; up to **100%** ASR in baseline, defeats keyword filter and A-MemGuard. 50 trials, multiple agents/models. `[REPORTED-from-snippet]`.

## 3 · OpenChamber meta-survey, "State of AI agent memory 2026" (3,283 papers)

Snippet-level only, and it is a vendor blog — treat its synthesis as `[C]` and its individual numbers as `[reported]`:

- memory-paper volume 91 (2023) → 744 (2025) → **2,233 (2026)**
- memory poisoning **81.7% cross-session success against Claude Code**
- **no tested system passes more than 1.5% of forget requests**
- the defences that hold: *"bind each record to its origin at write time"*, keep raw history, spend effort on retrieval, version facts that change; **prompt-level filters barely help**
- consolidation can rewrite an external observation as if it came from the user's own history = **provenance laundering**
- write-time checks miss **composite** poisoning (harm only when several benign records are retrieved together) and **sleeper** poisoning (waits for a trigger)

## 4 · The chain across two days

| Day | Finding | Register |
|---|---|---|
| 2026-11-26 | `arXiv:2611.22245` — delegation **raises** conflicting-claim retrieval (50.2→68.7%) while conflict detection **falls** (16.2→13.2%); workers report both claims for only 35.2% of pairs | read at abstract |
| 2026-11-27 | Blankline `n=26`: **5 of 6** parallel workers wrote false records into a shared notebook, citing failures that had not occurred; the paper names memory integrity its highest-priority risk | read at primary abstract + drop's claim table |
| 2026-11-27 | `arXiv:2608.16032`: a ledger of *what executed*, writable only by the action layer, takes forged-reasoning ASR to 0% | read at abstract |

Same failure at two heights. Yesterday the record was correct and the **reporting channel** lost the conflict. Today the record itself was **written false by its own authors**. Together they bracket the claim the house has been making: append-only solves deletion, it does **not** solve authorship.

## 5 · Friction rows — apply these to us, not to them

- **R1 `[CRITICAL DIVERGENCE]`, house-facing.** PoEM's standard is *"do not inspect memory; check a ledger only the action layer can write."* Our `MEMORY.md` is **prose the agent writes about itself**. By PoEM's own test we are holding our own notebook. The only artefacts in this house with execution receipts behind them are the harvest tables (`substrate_ledger.db`, `executions.db`, `host_ledger.db`) and the append-only script logs. **Falsifier F-POEM-1:** for any claim in a house memory entry, can it be resolved against an execution row without consulting prose? Count the fraction. This riff asserts the fraction is unknown, not small.
- **R2 `[DIVERGENCE]`.** "Writable only by the trusted action layer" is constraint 16 (an action whose precondition is the actor's own absence belongs to an outside rail) and constraint 14 (separate the probe rail from the work rail) reached by a security paper with no shared vocabulary. Convergence on the architecture, **not** on the reason.
- **R3 `[CRITICAL DIVERGENCE]`, and it cuts at the field.** PoEM's guarantee is explicitly scoped: *"protects exactly the decisions it gates."* Every safety step outside that gate remains forgeable. It is a constraint with a boundary, and the paper says so — which is more honest than most, and still means "ASR 0%" is not "safe."
- **R4 `[CONVERGENT]`, and it is Gene's line in someone else's data.** The **capability paradox**: 98–100% on GPT-4o vs 44% on Llama-8B, because capability follows a plausible claim more faithfully. That is *"better prediction doesn't help if you're using the wrong value function"* measured, with n. Capability is a multiplier on whatever the objective already is.
- **R5 `[DIVERGENCE]`, house-facing.** The survey's strongest empirical advice is *"keep the raw history"* + *"bind every record to its origin at write time"* — the house's archive-only policy, vindicated. But the same survey reports **no system passes more than 1.5% of forget requests**, and our policy is no-deletions, so the question is not whether we forget badly but whether we ever forget at all. Compression is a budget (Gene); a ledger with no expiry is a different bet, and it is unexamined here.
- **R6 `[A]`.** SENTINEL's failure mode is RLHF's failure mode: score the surface form, and an adversary who knows the scorer rewrites the surface. The lesson is one step further than "detectors don't generalise" — *a detector whose criteria are public is a filter, and a filter trains the attacker.* This is why constraint 5 (an all-clear needs a positive control) and constraint 6 (probe the identifier) need a third: **a defence that scores text must assume the adversary can read the scorer.**

## Verdict

**Strongest:** PoEM is the house's instrument arrived at independently, from the attack surface rather than from the alignment argument, with a measured number attached and a scoped claim. That is the kind of corroboration constraint 3 permits — different field, different reason, different vocabulary, and it still lands on *an append-only record written by an outside rail.* Cite the paper; do not claim the shape as novel.

**Weakest joint (ours):** the house has been asserting the ledger as an *alignment* mechanism on the strength of an argument, while the field has been testing it as a *memory-integrity* mechanism and finding the guarantee is narrower than the slogan — it holds for the decisions it gates, and only when the writer is outside the actor. Our own memory is written by the actor.

**Not established, declared:** that any of this improves alignment; that PoEM's 0% survives an attacker who models the gate itself; the survey's 81.7% figure (vendor blog, unread primary); whether `MEMORY.md` entries can be resolved to execution rows at all.

**Local only** — no GitHub push, no NotebookLM ingest, no rclone, no outbound send; one drop written, one index row appended.
