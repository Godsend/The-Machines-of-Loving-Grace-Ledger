---
title: "Experiment — does 'research taste' appear in our own correction record?"
date: 2026-11-22
type: "internal experiment / measurement"
instrument: "profiles/dion/scripts/taste_vs_epistemics.py"
corpus: "CANON_CORRECTIONS_FEED.md — 438 corrections (generated 2026-11-20)"
registers: "[EST]=measured here; [C]=commentator inference; [HYP]=hypothesis"
canon-id: CANON-2026-11-22-TASTE-VS-EPISTEMICS-EXPERIMENT
---

# Does "research taste" appear in our own record?

**Origin:** Gene, 2026-11-21 — *"they focus on 'taste' over right epistemics and I don't know how you even define 'taste' is it a string or matrix"*, then *"only genious in hind sight."*

**Purpose:** the wider discourse (Dream RSI, Hassabis, the "research taste" bottleneck) treats taste as the load-bearing faculty. Test the answerable version against a corpus we already have.

## §1 · What was NOT run, and why `[C]`

The tempting design — score drops on epistemics, see which were later corrected — **is confounded and was deliberately rejected:**

1. **Marker presence is not outcome.** `RETRACTED` occurs in 82 drops, mostly because drops *discuss* retractions.
2. **Corrections-attracted inversely measures rigor.** A careful drop attracts more scrutiny; more corrections can mean *more* rigor, not less.

**A clean-looking number from that design would have been meaningless.** Recorded here so it is not attempted again.

## §2 · What WAS run `[EST]`

Error-category distribution across the 438-entry correction feed. Keyword classification, reproducible via `taste_vs_epistemics.py`.

| Category | Count | Share |
|---|---|---|
| **MECH-register** (wrong strength / tag mismatch / downgrade) | **134** | **31%** |
| JUDGMENT (category error, withdrawal, re-description, refinement) | 61 | 14% |
| MECH-provenance (repeat claim, already-on-file) | 27 | 6% |
| NOT-A-CORRECTION (falsifier statements, verdicts, status) | 27 | 6% |
| MECH-attribution (ASR, metadata-only, surname) | 24 | 5% |
| MECH-scope (out of date, scoped to toy model) | 12 | 3% |

- Keyword-tagged: **235 / 438 (53.7%)** — 44% untagged, so ratios are indicative, not exact `[EST]`
- Contains a **mechanical** marker: **178 (40.6%)**
- Contains a **judgment** marker: **61 (13.9%)**
- **Ratio ≈ 3:1 mechanical to judgment** `[EST]`

## §3 · The headline `[EST]`

> **`taste` appears 0 times in 438 recorded corrections.**

**Every correction in the feed is attributable to a specific, articulable reason, attached to a file and a line number.** Not one is recorded as "the judgment was wrong and we can't say why."

**And the single largest category is REGISTER — 31%, roughly one in three.** The dominant failure mode in this canon is not being wrong about the world; it is **stating a claim at a strength its evidence does not license.** That is precisely what a register checklist catches mechanically, and it is the house's own instrument.

## §4 · What this does and does not show `[C]`

**Shows:** the epistemics scorecard *describes* the errors we catch. It is not decorative — it is coextensive with the correction record.

**Does not show:** that a checklist would have caught these *in advance* (a mechanical marker proves the error was *describable* in checklist terms, not that a checklist would have flagged it early). And it cannot show anything about taste's hit rate.

**Three limits, stated because they bound every number above:**

1. **SELF-SELECTED** — the feed holds errors we *caught*. Errors we missed are invisible by construction. This cannot measure a total error rate.
2. **SURVIVORSHIP APPLIES TO US TOO** — we cannot score the taste-catches nobody recorded, because nobody recorded them.
3. **KEYWORD CLASSIFICATION IS NOT JUDGMENT** — 44% of entries are untagged by these patterns.

## §5 · The finding that survives the limits `[C]`

Limit 2 is not a flaw in the method — **it is the result.**

**Epistemics leaves a trail: 438 receipted corrections, each with a file, a line, and a reason. Taste leaves none.** Not one entry.

**Therefore the asymmetry is not "taste is wrong and epistemics is right." It is: an unobservable variable cannot be load-bearing in a verification story.** If taste is doing real work, it is currently doing it **silently** — and a silent faculty is indistinguishable from a faculty that isn't there, which is the same failure class as a watchdog that is silent when healthy.

**Falsifier (pre-registered, F-TASTE-1):** to defeat this, produce a set of decisions where (a) a taste judgment was recorded *at the time, blind to outcome*, (b) a mechanical epistemics score was also recorded, and (c) taste out-predicts the score. **Nobody has produced such a set, for this canon or any other we are aware of.** Until someone does, taste is an unmeasured variable occupying a measured variable's slot.

**Companion:** the AlphaGo move-37 framing (§8 of `google_dream_rsi_reviewer_taste_conflation_0r5d9yAoeJ4_2026-11-21.md`) — move 37 was genius only *after* the score settled it, and the "intuition" that produced it was a compression of a game record, not a faculty.
