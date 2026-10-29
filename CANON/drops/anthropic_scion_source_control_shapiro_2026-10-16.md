---
title: Anthropic Scion — replacing Git because agents outgrew it
source: https://www.anthropic.com/engineering/redesigning-source-control
secondary: "David Shapiro, \"Anthropic Scion is INSANE\", YouTube 3199TC7Pt_o, 2026-10-16, 10:43, 39,388 views"
date: 2026-10-16
kind: canon-drop
register: E (empirical — first-party engineering post, published numbers)
tags: [scion, anthropic, source-control, git, ledger, eilt, monoid, agentic-scaling, post-labor, coordination]
---

# Anthropic Scion — replacing Git because agents outgrew it

**Primary source:** Anthropic engineering, *"Redesigning source control at Anthropic,"* published **2026-10-13** (updated 2026-10-15 to add prior-art credit). First-party, with numbers.
**Secondary:** David Shapiro, `3199TC7Pt_o` (2026-10-16, 10:43) — the post-labor framing. Local ASR, 153 segments.
**Pipeline note:** the canonical transcript for `3199TC7Pt_o` was **not** in `Canon/YT_TRANSCRIPTS/` at pull; the *Anthropic post* is the citation of record here, not the video.

## What happened

Anthropic **fully migrated its monorepo off git in five months**, replacing it with an in-house VCS called **Scion** (plus a code-review surface, **Antique**, code search, and an IAM layer). Team: **seven people.**

**The driver is the number that matters:**

- May 2026: **~2,500** merged changes/day.
- September 2026: **>30,000** merged changes/day — **12× in four months.**
- `main` history ≈ **100 GB**; a *compressed* working copy **>25 GB**.
- **~25 million** CI checkouts/day. Fetched naively: **>600 PB of git traffic/day.**
- At peak they ran **several hundred internal git mirrors** — still not enough.

Their words for the cause: *"the properties that make git excellent for distributed, offline work were actively undermining our ability to scale."* **Git assumes clients may be offline. Anthropic's clients are agents and CI jobs, which are always online.** The design assumption inverted.

## The architecture (the part that matters to us)

- **Unit of work = "changeset"** — *an entry in a write-ahead log*: the list of files changed relative to its first parent, plus content-addressed pointers to compressed blobs. **Created server-side, available everywhere instantly.** No packfiles, no locking, no cross-server coordination.
- **Refs are discouraged** except `main` and release branches, *"because global state that every server has to agree on is a looming scaling problem."* Moving a ref is a **compare-and-swap on a single Spanner row**.
- **★ "Derived data."** A changeset records only what changed, so it can't answer *who last edited a line*. Blame, path history, and skip lists are built **recursively from the changesets** — *"everything that isn't directly part of the changeset."* Three stated benefits: new derived types are cheap to add; each can be computed eagerly or deferred; and **the client never sees the internals, so the server can optimize them freely.**
- **No fully materialized copy of the repo exists anywhere, even on the server.** All data is content-addressed — *"a piece of data never changes once it's stored"* — so any server can cache it without checking with the others. Servers are *"essentially large caches that can also compute derived data on the fly."*
- **★ Commit cost scales with the change, not the repo.** Stated requirement: *"the cost of creating a commit … has to scale with the size of the change, not the overall size of the repo, or the server can't keep up."*
- **The working copy is optional.** All source-control queries are exposed as RPC/API, so many CI jobs need **no checkout at all** — automated bisect and revert pipelines exist because of this. Sparse and virtualized checkouts fall out for free: *"the client simply doesn't ask for trees it doesn't want."*

**Measured results:** **200× less CPU/memory** than the git mirror fleet; CI checkout **minutes → seconds**; **25% of CI CPU reclaimed**; cache hit rates **>99%** across three tiers (local daemon → regional → Spanner).

**Prior art, credited** (the Oct-15 update): Google's **Piper** and Meta's **Sapling** — specifically **Mononoke**'s **Bonsai** data model, which *"pioneered many of the techniques we use in Scion."*

**Status:** **closed source.** Anthropic is explicit: *"by no means a suitable replacement for git for general use,"* only sensible at monorepo scale. They intend to push the *ideas* upstream (server-side RPCs, better-composing sparse/shallow, alternative negotiation) to GitHub/GitLab/OSS.

**The recursion, stated by them:** *"Claude's ability to write code was both what put us in this situation in the first place and how we were able to quickly build a high-quality, scalable system to deal with it."* Per Shapiro: every engineer on the team says Claude codes better than they do; their job became understanding how the systems fit, making design decisions, and **often just telling Claude no**. Review changed from line-by-line to **intent-checking**; the **global lock on the merge queue was dropped** so changes merge concurrently; Claude fixes merge conflicts *"faster than a human could even spot it."*

## ★★ Why this matters to EILT — the convergence is not loose

**Scion is an append-only ledger of acts, with everything else derived.** That is EILT's structure, shipped to production by Anthropic:

| EILT claim | Scion, in practice |
|---|---|
| Coordination is an **append-only record of acts** | changesets, literally *an entry in a write-ahead log* |
| The ledger certifies **that** something was written, not truth | "derived data" is computed *from* the log and is explicitly non-authoritative |
| Immutability of committed entries | *"a piece of data never changes once it's stored"* (content-addressed) |
| Recovery **without return** (monoid, not group) | refs are a CAS on one row; you never roll back to a pristine state — you append |
| Minimise the state that requires **global agreement** | refs discouraged *precisely because* they're global agreement cost |
| **Marginal cost of an act scales with the act** | cost of a commit must scale with the *change*, not the *repo* |

**And the corpus's own rule fires again:** *the optimised variable is not the variable that matters.* Git's **offline capability** was its prized design virtue for two decades — and the instant the clients stopped being humans who go offline, that virtue became **pure overhead**. Same shape as everything else in this batch.

Shapiro's economics layer adds a second convergence — **post-labor arrives as *compaction*, not layoffs**: output grows while headcount stays flat or shrinks. Seven people absorbed a 12× load increase. His rule — ***"automate the coordination before you fire the coordinators"*** — is the coordination-cost framing EILT is built on. His framing device is **Solow's Paradox** and the **productivity J-curve** (factories swapped steam engines for one big electric motor and kept the shafts and belts, so no gains for decades). *"Don't pave the cow paths."*

## Flags

- **All performance figures are Anthropic's own**, unaudited and unverifiable externally (closed source). Treat 200× / >99% / 25% as vendor-reported.
- **Shapiro is a commentator with a strong prior** (post-labor economics is his thesis). His *framing* is useful; his *numbers* are Anthropic's, restated.
- **Do not cite the video as primary** — the Anthropic post carries the specifics. The video adds the post-labor interpretation and the "tell Claude no" detail, which the post supports more mildly.
- ASR: *"Anthropik"*, *"Anthropics"* → Anthropic; *"Solo's Paradox"* → **Solow's Paradox**; *"mono repo"* → monorepo; *"agented coating"*/"agentic coat" → agentic coding.
- **Prior-art dispute exists** — some coverage framed Scion as uncredited reimplementation of Meta's 2018 Mononoke work. Anthropic's Oct-15 update **credits it explicitly**, which resolves the strongest version of that claim.
