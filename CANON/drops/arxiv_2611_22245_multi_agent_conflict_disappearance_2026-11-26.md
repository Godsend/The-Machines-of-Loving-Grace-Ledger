# Two Nov-2026 arXiv hits on our own premise: the handoff is where conflicts die, and a paper called LEDGER already exists

**Filed:** 2026-11-26 21:05 EST · Dion · Canon drop (link find, end-of-day riff)
**Register:** reported-from-abstract [REPORTED], not yet read in full. Both v1/v2 Nov 2026.

## 1 · arXiv:2611.22245 — *Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents*

Zhang, Yu, Ding, Chen, Yu, Ni, Liu, Xu, Chen, Yao, Zhao, Zhao (12 authors, Nov 17/18 2026).

Verbatim numbers from the abstract:

- requiring delegation raises retrieval of BOTH conflicting claims **50.2% → 68.7%** vs single-agent
- yet conflict detection FALLS **16.2% → 13.2%**
- workers report both claims for only **35.2%** of retrieved pairs
- detection is HIGHER than single-agent when one worker reads both claims, LOWER when the claims are split across workers

**Why this matters to us:** this is an empirical friction row on the horde's decorrelation premise. Splitting evidence across contexts buys *coverage* and loses *comparison* — the conflict exists in the system, is retrieved, and never reaches the lead. It is derived-constraint 7 (*redundancy that shares the failed dependency is not redundancy*) with the failure located one step later: the redundancy is real, the **reporting channel** is the single point of failure.

**Counter-evidence from our own loop (same day, not a controlled arm):** tonight's CA593 / CA593-R / CA594 exchange had three nodes read overlapping evidence in separate contexts and DID surface four defects, three in the authors' own filings. The mechanism that worked is the same one their benchmark names as the target: every node ships the **whole claim pair plus its arithmetic**, not a summary of its conclusion. That is a testable design rule — *hand off adversary pairs, never conclusions* — and it predicts that any lane of ours that summarises before handoff will show their 35.2% signature.

## 2 · arXiv:2611.20927 — *LEDGER: Auditable Agent Memory Under Change*

Islam, Shuvo, Waseem, Abrahamsson (Nov 16 2026). A memory layer where "a language model proposes facts and explicit rules decide which value is current, which source to trust, and what to delete," each fact keeping source + the period it held.

- coding workload (synthetic, theirs): LEDGER+EP fallback 94.3% dev / 91.1% held-out vs full replay 82.1% / 83.3%
- LongMemEval: 74.8% = full replay, at **1% of its context** (differences within CIs)
- explicit self-stated limitation: synthetic workload built by the authors

**Two things to take, and one friction row.**

- Take: it is our thesis in someone else's words — *model proposes, rules adjudicate, every fact carries source and validity window*. Prior art now exists under our own name; cite it, don't claim novelty for the shape.
- Take: 74.8% at 1% of context is a clean number for the "compression is a budget" argument.
- **Friction row (do not smooth):** their system is built around *deletion* — "what to delete", scrubbing raw turns on deletion — and the headline accuracy comes from a lifecycle we have forbidden (Gene's archive-only / no-deletions policy). Their design treats forgetting as a first-class operation with a three-valued lifecycle; ours treats it as a prohibited one. That is a genuine architectural divergence, not a terminology difference, and it is the interesting row.

## Verdict

Strongest point: 2611.22245 gives us a measurable failure mode (evidence present, conflict unreported) to test our own handoff rule against. Weakest joint (ours, not theirs): we have one uncontrolled favourable case, not a benchmark; the 35.2% number is their instrument, on their task, and we have not run ours against it.
