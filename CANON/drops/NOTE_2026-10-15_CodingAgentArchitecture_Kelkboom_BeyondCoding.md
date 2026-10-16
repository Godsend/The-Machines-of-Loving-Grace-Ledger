# NOTE — Coding-Agent Harness Architecture: Carlos Kelkboom's Rules vs. This House

**Date filed:** 2026-10-15 · **Filed by:** Dion (subagent pass) · **Type:** PRACTICAL engineering note — deliberately **shorter and doer than a theory digest**; no EILT mapping, no friction table beyond the engineering delta.

**Source:** *"Lead Architect Reveals His Rules for Coding Agents"* — Beyond Coding podcast (host Patrick Akil), guest **Carlos Kelkboom** (lead architect; "Beyond Coding").
`https://youtu.be/mkN4uRZYPfs` · `upload_date = 20261014` · `duration = 4523s` (~75:23) · `view_count = 36,857` at filing (`[VERIFIED]`, yt-dlp metadata this session).

**Why filed (the framing question).** This is our own domain: a multi-agent fleet with subagent delegation, cron jobs, a Markdown canon ledger, and a live efficiency effort. Four claims in the brief (one-shot > iterative; main agent touches no files; scaffold before sub-agents; a distributed Markdown + indexed-search graph for **progressive context disclosure**) map directly onto work already in flight here, especially the **CA143 depth-indexed drill-back scope**. The point of the note is not "what Kelkboom believes" but **what, if anything, this house should change.**

**Register vocabulary (declared — 2026-10-13/14 cycle):** `[VERIFIED]` confirmed against a primary source this session · `[QUOTE, Lxxx-yyy]` direct transcript quote (file: `transcript_numbered.txt`, L0001–L1361) · `[EST]` established in external literature, checked inline · `[HYP]` speculation · `[CONTRA]` cuts against a claim, ours included · `[ATTACK SURFACE]` worth adversarial pressure · `[RIFF]` Dion's extension.

**Status:** Working draft, pre-adversarial. Not canonical until a cross-node pass + Gene sign-off. **GitHub sync deliberately left PAUSED** — `sync-ledger-to-github.sh` not touched, not run.

**Standing debt:** **F-GB1 was DISCHARGED 2026-10-14.** Not re-asserted. This note earns no present-day-harm receipt and claims none.

---

## 0. Transcript method

**`youtube-transcript-api` worked FIRST-TRY** (v-rail below). State which rail per the brief:

- `yt-dlp` metadata: **OK** (`--skip-download --dump-json`, exit 0). Note the same run logged `WARNING … unable to extract yt initial data … re-fetching using API` — the metadata still arrived.
- **Transcript: `youtube-transcript-api` succeeded first-try** — human-authored EN track present (`en`, `is_generated=False`), **1361 segments, 66,744 chars**, full coverage `00:00:00→01:15:20` (last caption end 4522s vs metadata duration 4523s). CDP not needed. This is the predicted rail (API first-try where yt-dlp subtitle download 429s on a shared IP).
- Transcript cached as `transcript_raw.json`, `transcript.txt`, `transcript_numbered.txt` in `…/cache/scratch/kelkboom/`.

---

## 1. His rules — what they are, the evidence he gives, principle vs preference

| # | Rule | Evidence he gives | Principle or preference? |
|---|------|-------------------|--------------------------|
| R1 | **Agents fail at iterative change, excel at one-shot.** Go as big as possible in a single well-specified run rather than many small edits. | "Agents I found are bad at making changes and are good at doing it one shot … almost like their training is a one shot training and not an iterative development training" `[QUOTE, L1104-1106]`; `[QUOTE, L0001]`. Cites **SlopCodeBench** as the measurement (§2). Concrete scar: a compiler "list system" he asked to be reviewed — "he said it was implemented five times" `[QUOTE, L0341-0342]`. | **Principle** — but grounded in a benchmark + one personal scar, and hedged ("that is what I've seen"). |
| R2 | **The conversational/main agent never touches files.** It teaches, asks, and — only above a confidence gate — spawns sub-agents that do the work. | "the agent you talk to doesn't change any code, doesn't change anything on your file system … for the work it spawns out some agents" `[QUOTE, L1053-1056]`; "only if the agent is confident above 90% that it knows what I want … ask me to spin up sub agents … don't start unless you're so incredibly confident" `[QUOTE, L1084-1092]`. Origin story: a game-engine agent offered to *implement* a tangentially-mentioned idea (John Cleese's open/closed creativity modes) mid-conversation — "that was such an eye-opening moment of, wow, it's focused on only one thing" `[QUOTE, L1069-1073]`. | **Principle** (separation of the conversational loop from the work loop), mechanised with a **local Gemma confidence gate** — the gate is a **preference/implementation choice**. |
| R3 | **Scaffold manually before delegating** — create the files, folder structure, types, and function signatures by hand first. | "I now scaffold the code. So I still create the files in the directory structure … class names or some function names or a function signature … because I do that, I guide the agents to implementing it the way I want" `[QUOTE, L0223-0230]`; "I scaffold deeper and further than I would advise people to do … I put markdown files in the project to explain what the boundaries are" `[QUOTE, L0764-0769]`; lexer/token-signature example `[QUOTE, L0775-0785]`. Cost: "20 minutes, 30 minutes, sometimes an hour" `[QUOTE, L0237-0238]`. Failure it prevents: "agents are really good at brute forcing a solution one way, but they forget how it fits into the rest of the application … code duplication … God objects" `[QUOTE, L0231-0236]`. | **Principle** (put the design decisions in place before the agent acts). The *depth* ("deeper than I would advise") is his **preference**, he says so. |
| R4 | **Progressive context disclosure over a distributed Markdown graph.** Nodes = Markdown files; edges = front-matter metadata; look at a diff/commit before the full code; drill deeper on demand. | "I design my scaffold, my harness in the same style as I build a social network … connections … nodes of information … a one liner or a commit hash … rank how well that information fits … goes deeper and deeper" `[QUOTE, L0984-0997]`; "I always let my eyes look at a commit a diff before I let it look at the full code" `[QUOTE, L0998-0999]`; "markdown files for the nodes and for the edges with a factorized index search and keyword search in the header of the markdown in the front matter" `[QUOTE, L1029-1031]`. Explicitly **not** a graph DB: "I don't put it in a graph database because I want it to stay distributed" `[QUOTE, L1026-1027]`. | **Principle** (index cheaply, disclose progressively, keep it distributed). The *choice of Markdown+front-matter search over a graph DB* is a **preference**. |
| R5 | **Throw away generated code the moment you don't understand it** — a comprehension gate, not a code review. | "And I throw it away. If I don't like it. If I don't understand it, I throw it away" `[QUOTE, L1139-1141]`; "I always do the work in a work tree … I don't even try to go much deeper than that, because I know that if I don't understand it, it has not continued in the scaffold that I gave it … it will bite me later" `[QUOTE, L1151-1157]`; "if I'm not able to look at the code and see all of the things that I assumed should be there to be there, I just throw it out, do it again" `[QUOTE, L1160-1162]`. | **Principle** (own what you absorb). Treated in §3. |
| R6 | **Code is cheap: parallel worktrees + a merge-best agent.** | "I just make three branches and let three agents work in those three branches … then I ask a fourth agent, compare what they did and only merge the good parts" `[QUOTE, L0749-0753]`; "code is cheap, so iterate fast, throw away often and just redo" `[QUOTE, L0747-0748]`. | **Preference** (a good pattern, not a universal rule). |
| R7 | **Abolish the heap / dynamic memory; want a 3-phase deterministic language.** | "I think the heap just needs to go completely. We don't need pointers, we don't need dynamic memory" `[QUOTE, L0387-0390]`; three-phase language sketch `[QUOTE, L0391-0409]`. | **[HYP]** — a language-design thesis offered with **no evidence** in-episode. Out of scope for a harness note; logged, not adopted. |

---

## 2. Does "SlopCodeBench" verify? — **YES, it is a real benchmark.**

`[VERIFIED]` against primary sources this session:
- **arXiv 2603.24755** — *"SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks."* Abstract: **36 problems, 196 checkpoints**, agents repeatedly extend **their own** prior code; measures **structural erosion** (rising in 77% of trajectories) and **verbosity** (75.5%); **best agent passes 14.8% of checkpoints**; "no agent fully solves any problem end-to-end."
- **www.scbench.ai** — v1.0 leaderboard, "36 problems · 196 checkpoints · 19 models."
- **GitHub `SprocketLab/slop-code-bench`** (SCBench) — open, community-driven; problem definitions in a separate `scb-problems` repo / Harbor dataset.
- **Snorkel AI leaderboard** (`snorkel.ai/leaderboard/slopcode-bench/`) — tracks Strict / Iso / Core solve %, erosion, verbosity.

**His number matches the paper.** He attributes the pointer to **Dex Horthy** (who "coined the term context engineering"): "he told me about this benchmark, which is called Slop Code Bench … it was 15% out of 100%" `[QUOTE, L1109-1118]` — the arXiv abstract says **14.8%**. So the citation is not fabricated; his recollection of the *model* he saw it on is imprecise ("sole 6.0 … or even 5.6" `[QUOTE, L1117-1118]`), which is an ordinary ASR/memory artefact, not a manufactured source. **Flag no fabrication here.** (House note: the house has caught fabricated citations before — CA114, 2026-10-07, and the 2026-06-01 class — so this one was checked rather than assumed.)

One honest scope note: the benchmark measures **his R1 exactly** and nothing else; it does **not** measure R2–R6. R3–R6 remain *one practitioner's preferences*, not benchmark-backed.

---

## 3. THE COMPARISON — his rules vs. what this house actually does

| # | Axis | Kelkboom | This house (as-built) | Verdict |
|---|------|----------|-----------------------|---------|
| 1 | **One-shot vs iterative work** | One-shot big run > many small iterative edits; benchmarked (SCBench). | Does **both**: cron jobs are inherently iterative/repeated; subagent delegation is a **bounded one-shot brief**. Our own pain is on the **iterative** side — reply-leg truncation ("truncated after 4 continuations", CA23/25/28) and the Sonnet-5.5 false "too large" rejection. | **SHOULD ADOPT (as an explicit default).** Our brief-as-one-shot is already the shape; the change is to *name* multi-turn iterative edits as the failure-prone path and prefer a fresh bounded one-shot over patching a long context. |
| 2 | **Who touches files** | Conversational main agent is **read-only**; only spawned sub-agents write; a Gemma confidence gate decides when to spawn. | Sub-agents do the work (this pass is one). But **no read-only main**: the authoritative writer *is* the parent, because the **canon ledger is single-writer truth** and derived indexes (Honcho, qdrant) are caches over it. | **ALREADY CONSIDERED — adopting only in part.** Take the **gate** ("plan/ask before acting"; don't let the conversational loop silently commit) — it is good discipline. **Reject the blanket no-write main**: a read-only main conflicts with ledger single-writer truth. Decouple the two objects: *conversation* need not write, *ledger authority* must. |
| 3 | **Scaffolding before delegation** | Creates files, folders, types, signatures, boundary Markdown by hand first (20–60 min). | The subagent brief **is** a scaffold: exact deliverable path, numbered required work, constraints, register vocabulary, allowed/forbidden operations. It is not byte-scaffolding (no pre-created file tree/signatures) because our deliverable is prose+ledger, not a compiled tree. | **ALREADY DOING** (intent-scaffold, not file-scaffold). The transferable tightening: have the brief also pre-declare the **artifact skeleton** (required section headers for a note; interface/signature for code) — the brief already lists required sections, so this is a small, free extension. |
| 4 | **Progressive context disclosure vs flat compaction** | Depth-indexed graph over Markdown nodes/edges; commit/diff before full code; drill deeper on demand. | **Flat-summary baseline.** No depth-indexed DAG, no drill-back primitive (CA143, 2026-10-13: "we are the flat-summary baseline"). A minimal **depth-indexed summaries + bounded-budget drill-back** (D0/D1/D2) was **scoped** against the compaction call-site. | **ALREADY CONSIDERED (scoped, not rejected).** This is the direct overlap, and it is **independent external corroboration** that drill-back over an index (not one flat summary) is the right shape. No new work needed — it reinforces the CA143 scope. |
| 5 | **Context/indexing architecture** | Markdown nodes + front-matter keyword/factorized index; **distributed; explicitly no graph DB**. | Markdown canon ledger + derived cache indexes; ledger is append-only single-writer truth, indexes are disposable caches. | **ALREADY DOING — and he validates the choice.** Same philosophy reached independently: keep truth in Markdown, keep indexes derived/cheap, avoid a heavyweight graph store. Log as agreement, not as a change. |
| 6 | **Code/artifact-understanding as a gate** | Discard anything you can't immediately recognise against your expectations. | Strong **provenance** gate: CA46 — "a filed artifact may contain only claims re-derived from a source read this session"; register discipline (no tag = treat as MYTH); register labels are a *sharpener, not a shield*. | **ALREADY DOING — but on a different criterion.** Ours is a **derivation** gate (can I re-derive it?); his is a **comprehension** gate (do I recognise it?). See §4. Adopt the comprehension half for *running components*, which our provenance gate does not currently cover. |
| 7 | **Parallelism: worktrees + merge-best** | 3 branches × 3 agents, a 4th agent merges the good parts. | Different objects: canon drops are single-writer (no merge-best); the fleet parallelises by profile/seat, not by git worktree. | **NOT APPLICABLE to canon drops; SHOULD ADOPT for the code repo (ClawHoarde)** — worktree-per-agent + a reconciler agent is a real pattern for code PRs, and this house already has a `merge-reconciler` seat, so the machinery exists. |

---

## 4. "Throw away code you don't understand" — the honest treatment

**Is it the same principle as our CA46 anti-fabrication rule? — Same family, DIFFERENT gate. Say so plainly.**

- **Shared principle:** *do not absorb an artifact you cannot independently account for.* His is the code case; CA46 is the claim case. Both refuse the vibe-coding move of letting an unaccounted-for artifact pass into the durable record.
- **Different criterion:** his gate is **comprehension** — "if I don't understand it … it has not continued in the scaffold … it will bite me later" `[QUOTE, L1154-1157]`. Our gate is **provenance** — "a filed artifact may contain only claims re-derived from a source read this session" (CA46, reiterated 2026-10-07 in the CA114 correction). You can *understand* code that is still wrong; you can re-derive a fact you don't "understand." The criteria are not interchangeable.
- **Where ours is stricter, and where it is weaker:**
  - *Stricter:* ours is falsifiable and auditable (a receipt or it didn't happen); his is a taste gate ("if I don't like it") that does not scale and cannot be audited across a fleet.
  - *Weaker — the actionable gap:* the house has **run components it did not understand**. The cache-deficit root cause was an **out-of-date provider plugin at 37.6% cache vs 96–98% on other lanes** — a component in the request path that nobody could account for, exactly his "it will bite me later." Our *claims* are gated; our *running system surface* is not. That is his rule pointing at a real hole in ours.
- **Verdict:** not the same rule — **the same principle, a complementary gate.** Adopt the comprehension half **for the live system** (see §6), keep provenance as the ledger's law.

---

## 5. Friction table

| # | Friction | Kelkboom | This house |
|---|----------|----------|------------|
| F1 | **Disposability** | "Code is cheap … throw away often" `[QUOTE, L0747]`. | **Append-only ledger:** a canon claim is corrected in place, never thrown away. Code may be disposable; *claims and receipts are not.* `[CONTRA]` |
| F2 | **What "understanding" gates** | Immediate recognition against expectations — **comprehension**. | Re-derivation from a source read this session — **provenance**. Neither subsumes the other; §4. |
| F3 | **Read-only main vs single-writer truth** | Conversational main never writes the filesystem. | The authoritative writer *is* the parent/ledger — a fully read-only main would break single-writer truth. Adopt the **gate**, not the **blanket**. `[CONTRA]` |
| F4 | **Scale of manual scaffolding** | Hand-scaffolds 20–60 min per project; "deeper than I would advise." | A fleet cannot hand-scaffold every job; scaling manual scaffolding is a **human bottleneck**. The house's analogue (the brief) must stay automatable. `[ATTACK SURFACE]` |
| F5 | **Benchmark scope** | SCBench measures **R1 only**; R3–R6 are preferences. | Do not import R3–R6 as if benchmark-backed — that would be **register inflation** (a preference wearing an evidence costume). `[CONTRA]` |
| F6 | **Abolish-the-heap** | Offered with zero evidence; a language-design thesis. | Out of scope for a harness note; log `[HYP]`, do not adopt. `[RIFF]` |

---

## 6. Verdict — what this house should actually change

**Two concrete adoptions; one reinforcement; one do-not-adopt.**

1. **ADOPT (engineering, free): make the bounded one-shot brief the *named* default for delegated code work, and treat long multi-turn iterative edits as the failure-prone path.** Corroborated three ways — SlopCodeBench (`[VERIFIED]`, §2), our own continuation-truncation losses (CA23/25/28), and the Sonnet-5.5 false-rejection. Concretely: when a job needs many edits, prefer closing the context and reopening a fresh bounded brief over extending the loop. The brief format already embodies this; the change is to stop treating iterative patching as the safe path. **Cost: documentation + one habit. Owner: horde/CA process.**

2. **ADOPT (closes the honest gap from §4): extend the artifact-understanding gate from *claims* to *running components*.** CA46 governs what we *file*; nothing governs what we *run*. Any component in the request path that we cannot account for should be flagged the way an unverified claim is flagged — the cache-deficit provider plugin (37.6% vs 96–98%) is the worked example of what the missing gate costs. **Cost: one checklist item ("can I account for every component in this path?"). Owner: horde-system-audit.**

3. **REINFORCE, do not re-open: keep the scoped CA143 drill-back work as scoped.** Kelkboom's progressive-context-disclosure harness is **independent corroboration** that depth-indexed drill-back over an index — not one flat summary — is the right shape. It adds conviction, not new scope. **No new work.**

4. **DO NOT ADOPT: abolish-the-heap / 3-phase deterministic language.** A language-design thesis with no evidence in-episode; out of scope for a harness engineering note. `[HYP]`.

**One-line answer to the framing question:** his most transferable contributions here are not the exotic ones (distributed graph, heap abolition) — they are the two cheap disciplines our own gaps already pointed at: **prefer one-shot over iterative-patch** and **gate on comprehension of what you run, not just provenance of what you file.**

---

*Filed by Dion, subagent pass. Register tags applied inline. F-GB1 discharged 2026-10-14 — not re-asserted. GitHub sync left PAUSED. A note, not a digest: shorter by design.*
