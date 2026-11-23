# The Layered Agent — architecture, instruments, and what remains unbuilt

*Built 2026-11-22/23 on the dion lane, Nitro. Every number below is measured on this host, not estimated. Every instrument named has a control suite; the ones without are marked.*

---

## 1. The problem, measured

An agent profile injects its memory file into **every** turn. Measured before any work:

| Quantity | Value |
|---|---|
| `MEMORY.md` (dion) | **481,953 B ≈ 120,488 tokens** |
| First-call input, n=278 sessions | **median 184,411 tokens, max 710,790** |
| Memory as share of fixed cost | **~86%** |
| Long session live context | **355k tokens** (99% cached) |
| Compression timeouts begin | **~600k** |

**Diagnosis: memory is content, not pointers.** The framework's own design intent was ~1,300 tokens. It drifted 100×.

---

## 2. The three-layer split

Derived, not invented: a **four-family riff** (Astra/GPT-6, Fable/Claude, Grok, Gemini — `workspace_riff/`) converged 4/4 on the same finding.

### 2.1 PUSH — rules and facts (always injected)

**What four families independently said dies under pure retrieval:**

- **Astra:** *"prospective memory — remembering to check something before an action, without being asked."*
- **Fable:** *"a pointer fires only when something searches for it; a rule must fire unprompted. Nothing in a future task says 'look up whether `immutable=1` is safe on a live store'."*
- **Gemini:** *"you do not run a RAG query: 'Should I include temperature when calling Fable?'… the agent must step on the rake first."*
- **Grok:** *"it loses the decision boundary that made it the right file at that moment."*

**Mechanism: RAG is pull-based; a prohibition must be push-based.**

| Layer | Tool | Items | Tokens |
|---|---|---|---|
| RULES (prohibitions, traps, supersessions) | `rules_layer.py` | 83 | 5,968 |
| FACTS (paths, ports, models, config keys) | `facts_layer.py` | 94 | 7,510 |

**Rules ≠ facts, and this mattered:** the first extraction pass covered 81% of entries but **missed `1048576`, `deepseek-flash`, `claude-fable`** — constants are not prohibitions.

### 2.2 PULL — pointers (retrieved on demand)

| Index | Tool | Entries | Tokens |
|---|---|---|---|
| Activity (sessions, cron, drops, dreams) | `meta_workspace.py` | 498 | 21,257 |
| **Error record** (self-curated) | `meta_rag.py --strict` | 186 | 14,386 |

**Why a separate meta-RAG:** the meta agent asks *"what did we get wrong"*, not *"what happened"*. Curation criterion is **error signature**, not recency — the biological analogue is that consolidation replays by salience, and salience is prediction error.

### 2.3 GATE — the commit check

`memory_commit_gate.py` — three checks, **7/7 controls** (`--self-test` verified 2026-11-23):

1. **CONTRADICTION** — shares a technical **anchor** with an existing rule (`ANCHOR_RE`: backticked literal, flag, path, env var, model name, filename), opposite polarity
2. **SUPERSESSION** — substantially restates a rule; must declare `supersedes: <id>` or it becomes a sibling at equal rank (**Fable's exact warning**)
3. **SCOPE** — absolute claim (always/never/all) with no measurement, date or source

**Precision iteration (updated 2026-11-23 00:02 EST, post-draft):** jaccard overlap missed a real contradiction at 0.094; an intermediate **IDF/rarity-weighted** fix was tried and **reverted** (content-free corpus-rare tokens like `2026` and `zero` still fired, and a 2-rule fixture has no usable IDF). Replaced by **shared-anchor matching** (independently proposed by Astra and Gemini): a contradiction must share a referential identifier, not just topical prose. Pure-prose contradictions with no technical anchor intentionally miss; findings remain **candidates**, not automated escalation triggers.

---

## 3. The two clocks

Two different timescales, and only one existed before tonight.

| Clock | Tool | Cadence | Output |
|---|---|---|---|
| **Slow** — durable rules | `consolidation_review.py` | daily 04:30 | candidate rules + gate verdict |
| **Fast** — direction | `daily_vector.py` | daily 05:00 | RESUME / LEAN IN / AVOID / QUESTION |
| Metronome — index refresh | `workspace_refresh.py` | every 30m | refreshed index + drift report |

**A rule says "never do X". A vector says "lean toward Y tomorrow".** Rules are durable; vectors expire with the day.

**Drift detection in the metronome is not optional:** the failure mode is not a crash, it is a process that keeps running and quietly stops capturing. Controls: index collapse >40%, rules collapse >25%, gist degeneracy >70%, file missing.

---

## 4. What the consolidation actually found (and why it changed the plan)

Ran on **72h / 2,480,555 chars → 20 candidates → 12 passed the gate.**

**Reading them showed most were narration:**

| Candidate | Verdict |
|---|---|
| *"A file being appended to during its own copy can never be copied"* | **real rule** |
| *"My Iter-332 pre-reg #1 fired and its remedy was wrong"* | **real lesson** |
| *"Checking the cron lane first so I don't collide"* | narration |
| *"I killed nothing"* | narration |

**The gate checks conflict and scope — not whether a candidate is a rule at all.** That distinction is **semantic**, which is why stage 2 (`distill_candidates.py`) needs a model.

**Architecture correction: mechanical extractors are a QUEUE, not a filter.**

---

## 5. The distillation pass, and its comprehension gate

`distill_candidates.py` — stage 2. Separates durable rules from narration.

**Two controls, both earned the hard way:**

**Contamination probe** — raw provider HTTP, empty system prompt, no tools. The `hermes chat` harness injects MEMORY.md; a model asked to curate memory on that rail already holds it. Probe: *"what port does the dion A2A listener use?"* → must answer `I DO NOT KNOW`.

**Comprehension gate** — added after a model given a 114k-token input **invented a fictional Linux fleet** (`tank0`, WireGuard, DKMS) rather than saying it could not process the file. The gate requires the model to **echo a specific numbered candidate verbatim**. If it cannot echo the input, it never read it, and the pass **DEFERS** rather than producing plausible output.

**First run of the gate failed — and caught my bug, not the model's:** the probe asked it to quote from "the document you were given" without ever supplying the document. Fixed by passing the numbered list into the probe call.

---

## 6. Instrument status

| Instrument | Controls | Status |
|---|---|---|
| `memory_commit_gate.py` | 7/7 | ✅ catches a real contradiction on live rules |
| `workspace_refresh.py` | 4/4 | ✅ running every 30m (cron `118d63394dd0`) |
| `daily_vector.py` | 5/5 | ✅ usable output after tool-output filter added |
| `consolidation_review.py` | 4/4 | ⚠️ produces candidates, mostly narration |
| `distill_candidates.py` | probe-gated | ⚠️ comprehension gate works; end-to-end unproven |
| `meta_rag.py` | none | ⚠️ gists are often titles, not error clauses |
| `proof_graph_stats.py` | 5/5 | ⚠️ `import_depth` degenerate below full-repo scale |
| `rebuild_test.py` | ceiling+floor | ⚠️ scorer needs a paraphrase control (see §7) |

---

## 7. Known defects, stated plainly

1. **Extractors cannot tell a rule from a sentence about a rule.** Semantic distinction; needs a model with a comprehension gate.
2. **`rebuild_test.py` has no paraphrase control.** Its ceiling tests identity and its floor tests independence — **neither samples the regime a rebuild produces.** The Hossenfelder drop scored 0.06 and then 0.00 on identical input while the rebuild was demonstrably faithful. **The drop passed; the scorer was broken.** Shared house rule (adopted from CA556): **a result at ceiling, floor, or a fixed 0/0 tie is the instrument until a positive control shows it can move.**
3. **`meta_rag` gists are titles.** Pointer is the payload; the gist is only an address.
4. **Gate precision on ordinary prose is bounded** — the initial 4/4 live-review findings were generic-word overlaps. IDF/rarity weighting was tried and reverted; `memory_commit_gate.py` now gates contradictions on a shared technical anchor (`ANCHOR_RE`), which cuts generic-prose false positives at the cost of intentionally missing anchorless pure-prose contradictions. Treat every finding as a **candidate**, never an auto-escalation verdict.
5. **`consolidation_review` can emit an empty vector**, which is indistinguishable from a quiet day. Reported explicitly, never as success.
6. **Two runs of the same test can differ** (temperature / inference nondeterminism) — the F-NOISE-1 floor applies to our own stochastic LLM-inference instruments, not just external benchmarks.

---

## 8. The measurement floor that applies to stochastic LLM-inference results

**Citation verified at source (2026-11-23, `arXiv:2506.09501v2` abstract, Yuan et al., revised 2025-10-24, verbatim):**

> *"For instance, under bfloat16 precision with greedy decoding, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size."*

**Scope boundary (added per CA556):** the 9% figure is an upper-bound example for **LLM-inference numerical nondeterminism** — specifically pronounced in BF16 reasoning models across hardware/batch-size variation where early-token FP rounding cascades down long chains of thought. It applies to **uncontrolled LLM-inference deltas** (benchmarks, LLM-as-judge / stochastic rebuild runs). It does **not** apply to deterministic parsers or fixed-seed deterministic post-processing (e.g., parser-scored credit counts or deterministic backtest length-control deltas), whose failure mode is instrument error (§7.2), not FP inference noise.

**Consequence:** any claim built on an uncontrolled LLM-inference delta inside the numerical noise band is unfalsifiable without explicit controls (fixed seeds, identical hardware/batch size, replication, or FP32/bitwise-reproducible serving).

**Pre-registered: F-NOISE-1** — for LLM-inference / stochastic-eval claims, require N≥5 replicates (or deterministic/controlled serving) or demote to `[HYP]`.

---

## 9. What is NOT built

- **Injection (partially landed 2026-11-22 23:48 EST, 12m after initial draft).** Dion's live `MEMORY.md` was swapped to the 3-layer composition (RULES + FACTS + 30 UNCOMPRESSED: 481,953 B → 83,719 B). Automated layer regeneration into `MEMORY.md` and pull-layer auto-routing are not wired.
- **The commit path.** Nothing writes to `MEMORY.md` automatically. A commit needs a human read and an explicit `supersedes:`.
- **Stage-2 at scale.** The distillation pass works in principle; it has not yet run end-to-end on a real candidate set.
- **The review consuming the meta index.** `consolidation_review.py` still scans raw activity, not the curated error record.

---

## 10. The one line that holds it together

**Design it, then let the record select it.**

An evolved personality is tested but unaimed; a built one is aimed but untested. **The rules are built; the record selects.** Neither alone produces coherence — rules without history is a costume, history without rules is drift.

---

*Provenance: components credited in §2.1 to four model families by name; the synthesis and every instrument here are ours, and inherit the errors of any component misrepresented.*
