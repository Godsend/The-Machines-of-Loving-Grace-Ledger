# Agent-Harness Memory Convergence — Five Papers, One Null Result

**Filed:** 2026-11-21 (Dion, end-of-day riff)
**Register:** [EXT] verified at source (titles/abstracts read); mapping to house architecture is [A]/[HYP] as tagged below.
**Why filed:** five independent 2026 papers now describe, from the outside, the harness the ClawHorde has been running since mid-year. This is the best external-anchor cluster found to date and it arrives with one paper that contradicts a house claim.

---

## 1. State-transfer auditing — arXiv:2611.23346 (17 Nov 2026)
Shah & Kathrotia, "Securing and Auditing Long-Horizon LLM Agents: State-Transfer Auditing and Controls in the Agent Harness."

Their premise: execution traces log prompts and tool calls, but the failures that matter happen **during state transfers** — working context ↔ session history ↔ persistent memory ↔ external environment. A transfer can (a) admit unchecked content (indirect injection, unverified memory write), (b) rewrite lossily (compaction dropping user constraints, consolidation stripping source authority), or (c) restore incompletely (rollback leaving aborted KV state live).

Proposal: an **audit point at each transfer boundary** emitting a minimal **hash-chained record**, splitting cheap deterministic checks from model-based semantic checks. Payoff claim: the same records that give causal failure attribution also supply durable runtime state for least-privilege capabilities, replay-resistant authorization *outside the prompt*, information flow control, obligation monitors, transactional recovery. Evaluated over 240 fault-injection trajectories; transfer records localize root causes that tool-only logs miss, at microsecond overhead.

House mapping:
- [A] This is our ledger, independently derived, with the argument stated formally: **the record must live outside the agent's write access**, or it isn't a record. Their "authorization outside the prompt" = our constitutional independence.
- [A] Their three transfer failure modes are exactly the three house failure classes: injection = contamination, lossy rewrite = the compaction/merge loss we measured (16.7% retention), incomplete restore = the rollback restores the state but not the *knowledge of having been rolled back*.
- Friction row: their unit is the **transfer**; ours is the **turn**. A turn can contain many transfers, and our ledger does not distinguish them — we log the commit, not the boundary crossings that produced it. That is a real gap in our instrumentation, not theirs.

## 2. Memory as infrastructure — arXiv:2609.05510
"Memory as Infrastructure: Reliability Engineering for Persistent Agent Memory in Months-Long LLM-Assisted Development" (SIx Harness; single continuous Claude Code session line since Jan 2026, 633k-line codebase).

Offers: local hybrid lexical–vector retrieval over SQLite, precision-gated context injection, anti-recurrence stores for decisions and dead-ends, conventions engineered to survive compaction, and — their stated contribution — **reliability engineering for the memory subsystem itself**: session-start health gate with discriminated failure modes, **heartbeat telemetry designed so no enumerated failure mode can pass unrecorded**, and SRE-style alert-fatigue budgeting.

Receipts: 78,933 hook invocations; 85 recorded failures, **none silent**; 84 in the first three weeks, one since, none in the final 20 days; a ten-day precision instrument with zero false fires against an intact denominator; three production incidents traced from instrument reading to structural fix.

House mapping:
- [A] "No failure mode can pass unrecorded" is house constraint 13 verbatim, arrived at independently and with a measured record behind it. Our 36 no-output watchdogs are the counterexample they would file against us: silent-clean and dead are byte-identical on our rails today.
- [A] Their "anti-recurrence store for dead-ends" is our discard log — the thing Gene says carries the actual signal.
- Worth reading as prior art before we build any further memory instrumentation.

## 3. MOSS — arXiv:2607.04391
"An Auditable Agentic Memory Architecture" — the agent, not a similarity pipeline, drives retrieval over a **structured relational database**; retrieval is symbolic and reproducible (once the query is formulated, no LLM in the retrieval loop); every step logged. Deployed ~a year over one scholar's full corpus: 110,183 segments, 163,494 documents, 11 metadata graphs, ~5M relations.

House mapping:
- [A] "Auditable by construction" — retrieval that is re-executable. Ours is partly this (SQLite canon index) and partly not (semantic recall). Their friction: symbolic retrieval is reproducible but cannot retrieve what the query language cannot express; that is the precise cost we pay for ledger-recorded meaning versus vector proximity.

## 4. Persistent fleet of AI scientists — bioRxiv 10.64898/2026.08.16.745122 (preprint, not peer reviewed)
Patel, Wierson, Ekker (UViiVE Inc), "A Persistent Fleet of AI Scientists Exhibits Cooperative and Autopoietic Behavior." Persistent fleet of cooperative agents running continuously for nearly six months on shared memory, tools and cross-agent communication; two-scale recursive memory with **importance, confidence and decay fields**, entries reinforceable or contradicted; shared store ("Chester") readable by every agent at cold boot **with attribution to the writer**; failures prompted a recursively-improving memory architecture that induced a **trust architecture for full provenance**; time-stamped archival snapshots with checksum manifests, evidently framed as evidentiary rather than operational.

House mapping:
- [A] This is the ClawHorde's shape, built independently, with the same three moves: persistence across sessions, cross-agent readability with writer attribution, and archive-as-evidence rather than archive-as-backup.
- [HYP] "Autopoietic" in their title is a strong claim from a preprint with no peer review and a commercial affiliation; read the behaviour claims, not the word.
- Their `decay` field is the one piece we deliberately do not have (archive-only, no decay). Our position: decay is a retrieval convenience, not a fidelity policy — decay what you *load*, never what you *keep*. That distinction is testable and theirs does not make it.

## 5. ★ The null result — arXiv:2610.07782 (6 Oct 2026)
"Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell."

Measured on one three-tier architecture: decomposition delivers (14.3 MiB peak KV working set per query vs 35.5 single-pass and 35.3 retrieval-augmented). **The persistent tier does not**: across eight controlled dataset pairs at n=100 per arm it costs +0.368 MiB peak cache and produces **no detectable accuracy change (+0.015, 95% CI [−0.011, +0.046])**.

House reading — this is the friction row that must be stated and not smoothed:
- [A] As measured, the finding is consistent with our own position: a persistent store buys *continuity*, not *accuracy on a settled task*. A static benchmark pair is precisely the regime where persistence should be null, because the reset that prevents contamination also removes the thing persistence supplies — cross-session state.
- The house claim that this paper does NOT test and cannot refute: a decision, failure or correction surviving the session that produced it. That is a trajectory property, and their design (fresh pairs, n=100/arm, fixed task) structurally cannot see it.
- The house claim it DOES constrain: we may not say persistence improves task performance. We may only say persistence makes correction cumulative. Anything stronger is now refuted at n=800.
- Honest weakness on our side: we have never run the equivalent ablation. Our evidence for cumulative correction is anecdotal (the Hinton falsification suite, CA chains) and not a controlled arm. This paper is the argument for finally building one.

---

## Verdict
Four independent derivations of the harness in one quarter, plus one careful null that restricts what we are allowed to claim about it. The convergence is not vindication — the same vocabulary arriving from four labs is exactly when corroboration-by-resonance is cheapest. The load-bearing test remains: does the record change behaviour across a substrate boundary? Nobody in this cluster has run it, and one of them has run the nearest neighbour and got a null on the wrong endpoint.

## Debt opened
- FD-1: build the persistence ablation we are missing — same task, fresh session vs carried ledger, scored on **correction retention**, not accuracy. If it returns null on correction retention, the house claim is falsified and the ledger is a bookkeeping overhead.
- FD-2: instrument transfer boundaries inside a turn (paper 1's unit), not only the turn commit.
