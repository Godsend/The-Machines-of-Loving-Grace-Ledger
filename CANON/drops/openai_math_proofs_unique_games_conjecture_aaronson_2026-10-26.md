---
epistemic-registers: EST=established fact (independently verified this pass) HYP=stated claim/hypothesis, not independently verified A=analogy/our reading (not the source's claim) C=conjecture POETIC=evocative/unfalsifiable RIFF=our extension beyond the source
rule: no tag = treat as MYTH (do not build on it)
id: openai_math_proofs_unique_games_conjecture_aaronson_2026-10-26
title: "Scott Aaronson, 'I Heard That a Robot Solved the Math Problem You Worked On' (Theories of Everything, Curt Jaimungal) — the OpenAI 372-result release and the claimed Unique Games Conjecture proof"
source: Curt Jaimungal (Theories of Everything), YouTube `3yXtXTwz4J4`, uploaded 2026-10-26, 1:26:57.
guest: Scott Aaronson (UT Austin; director, UT Austin Quantum Information Center), interviewed by Curt Jaimungal.
date: 2026-10-26
canon-id: CANON-2026-10-26-OPENAI-MATH-UGC-AARONSON
filed-by: Dion (research subagent pass)
type: SOURCE DROP — present-day AI-capability/governance engagement, with independent verification pass. No forced EILT/cosmology mapping.
tags: [openai, unique-games-conjecture, khot, aaronson, moshkovitz, mathocalypse, ai-math, lean4, formalization-gap, spec-gap, association-for-human-mathematics, anthropic, 3sum, apsp, navier-stokes, disclosure-norms, present-day-capability, governance, verification-capacity]
transcript: /data/SecondBrain/Canon/YT_TRANSCRIPTS/3yXtXTwz4J4_Aaronson_RobotSolvedMathProblem_TOE_2026-10-26.txt
cross-refs:
  - openai_navier_stokes_formalization_gap_2026-10-09.md   # the SPEC-GAP / Lanyon-Gorard companion
  - DIGEST_2026-10-12_Aaronson_PetermanPod_Mathocalypse_IntelligenceMatter.md   # same speaker, earlier (2026-10-12) telling of the same story
  - openai_alien_math_2026-10-09.md
  - rea_ai_reverse_engineering_device_rightToRepair_governance_2026-10-26.md   # sibling present-day item, same day
---

# Canon Drop — OpenAI's 372-result math release, the claimed Unique Games proof, and Aaronson's read

## 0. Provenance and method

- [EST] **Transcript pulled this pass; read in full.** `youtube-transcript-api` (primary rail) succeeded
  first try via `~/.hermes/bin/uv run --with youtube-transcript-api`; 2,180 snippets, **100,597 chars**,
  full coverage 0:00–1:26:57, saved to
  `Canon/YT_TRANSCRIPTS/3yXtXTwz4J4_Aaronson_RobotSolvedMathProblem_TOE_2026-10-26.txt`. Metadata
  verified with `yt-dlp --print`: title matches, channel "Curt Jaimungal", duration 1:26:57, upload
  2026-10-26. A second, first-party-caption copy already existed at
  `Canon/sources/aaronson_robot_math_3yXtXTwz4J4/transcript.md` (2,185 lines); the two are concordant.
- [EST] **ASR-verbatim NOT guaranteed.** The captions are auto-captions; proper nouns are garbled
  ("Aronson"→Aaronson; "Subash Coat"→Subhash Khot; "Donna Moskavis"→Dana Moshkovitz; "Timothy Gowowers"
  →Timothy Gowers; "Edward Whitten"→Edward Witten; "Vie Vaselva"→Virginia Vassilevska Williams;
  "threesome"→3SUM; "Casper"→Kasparov). All corrected below where a primary source confirms the name.
- [EST] **Independent verification pass run this pass** (per brief). Method: `web_search`, `web_extract`,
  GitHub/arXiv and primary-site reads, 2026-10-26. Results in §3. **This is the pass the earlier
  same-speaker drop (`DIGEST_2026-10-12_Aaronson_PetermanPod…`) explicitly deferred** ("this pass did
  not cross-verify them"); that drop filed the whole story as *presented-not-confirmed*.
- [EST] **This is a present-day AI-capability/governance drop.** No cosmology/EILT table forced. Two
  genuine, specific house connections are filed as [A] in §5, with one Friction Rule divergence row.

---

## 1. Bottom line

- [EST] **The headline event is real and heavily, independently covered.** On **2026-10-06**, OpenAI
  published **722 manuscripts organized into 372 result families** to a public GitHub repository
  (`github.com/openai/math`), claiming solutions to or major progress on hundreds of open problems in
  math and theoretical computer science, produced by an **unreleased internal model** that spent ~3
  hours of compute per result after being tried on ~4,000 problems. (Wikipedia "OpenAI bulk release of
  mathematical papers"; Scientific American; Quanta; NPR; Zvi Mowshowitz; implicator.ai; itdoeswhatnow.)
- [EST] **The repository included a *claimed* proof of the Unique Games Conjecture (UGC)**, with a Lean
  formalization — the highest-profile AI-generated proof in theoretical CS to date. (Quanta; Wikipedia;
  Aaronson's own blog "The Mathocalypse".)
- [HYP → the register-critical point] **Aaronson describes it flatly as "a proof of the unique games
  conjecture."** That is **OpenAI's own claim**, and it is **not an established, verified result.** It is
  non-peer-reviewed; no human had fully understood or independently checked it even weeks later; the
  Lean certificate proves the *coded* statement, not that the code matches the natural-language
  conjecture (the house's own SPEC-GAP / formalization-gap rule, §5). Moshkovitz's own public word (NPR)
  is **"It looks right"** — a candidate proof, not a proven one. Aaronson's blog hedges the same way:
  *"Or at least, we're pretty sure that it's a proof!"*
- [EST] **OpenAI released the material on the recommendation of an external advisory board including
  Timothy Gowers and Edward Witten** (the "Advisory Group on Mathematics and Artificial Intelligence" /
  AGMAI, nine mathematicians, hosted at the Princeton IAS, recommendations 2026-09-29).
- [EST] **The release and its reception are the story the house should track:** frontier AI capability
  now generating, in bulk, results that **outpace the human community's capacity to verify or even read
  them**, with the resulting fight being about **epistemic trust, credit/exposition, and disclosure
  norms** — not about whether the proofs are "alien intelligence."

---

## 2. Faithful register-tagged summary (as *reported in this video*)

### 2a. The framing and the Ahmad-clip

- [HYP] The video opens with audio from the **Association for Human Mathematics** (AHM): *"We are not
  the arbiters of who gets to work on our problems… open for absolutely anyone in the world… an unknown
  clerk in India as Ramanujan was… a 17-year-old student."* (This is the AHM statement; the video
  replays it. AHM is **real** — §3d.)
- [HYP] Jaimungal's thesis line: *"There's this rising flood waters that came for software engineering
  and then this summer it's come for us… the past few weeks the most significant moment in math
  history."*
- [HYP] The opening teaser is the **P=NP disclosure hypothetical** (§2d).

### 2b. The UGC story (Aaronson's core narrative)

- [HYP] Aaronson's 9-year-old son teased his wife, complexity theorist **Dana Moshkovitz**: *"I heard
  you got cooked. I heard that a robot solved a math problem you were working on for your whole
  career."*
- [HYP] Moshkovitz has worked toward proving the **Unique Games Conjecture** for the entire time
  Aaronson has known her (they began dating in 2009; he renders the conjecture's author as "Subash
  Coat" = **Subhash Khot**).
- [HYP] *"A couple weeks ago, OpenAI… released… almost 400 AI-discovered solutions to major open
  problems in math, in theoretical computer science, and one of the crown jewels in what they released
  was a proof of the unique games conjecture."*
- [HYP] **The load-bearing qualifier Aaronson supplies immediately:** Moshkovitz has been spending all
  her time *just trying to understand* the proof; *"we now have all of these problems… that appear to
  be solved. But that doesn't mean that anyone understands the solutions yet."* The writeups are often
  *"poorly written… if they were submitted to a journal, they'd just get sent back right away."*
- [HYP] Aaronson reframes the human role as **interpreter/expositor** (literary scholar; astronomer
  with a telescope; biologist watching bears — "no one asks why the bear wasn't a co-author"), not
  original solver; *"that does permanently change the nature of what it is that we do."*
- [HYP] **Some results carry a Lean certificate** ("some kind of formal guarantee that… the result
  appears to be valid"), *most* had not been digested by any human.
- [HYP] Moshkovitz is using a model ("**Astra**") to *interrogate* the proof point-by-point
  (house canon names Astra = OpenAI's GPT-6 Astra, cf. `openai_dots_astra_…2026-09-29.md` — model
  identity reported, not independently confirmed here).

### 2c. The Navier–Stokes precedent and the release controversy

- [HYP] OpenAI *"famously… released the solution to the Navier Stokes problem… a couple months ago"*
  (announced 2026-09-08); humans **Tristan Buckmaster and Levent Alpöge** were pursuing it; the video
  says OpenAI *"got wind of what they were doing and… decided to get there first,"* which *"left a bad
  taste"* and produced a backlash. (The priority dispute is real; §3e.)
- [HYP] Per Aaronson: OpenAI *"fed like 4,000 open problems to these models and it solved… let's say
  10%,"* ~3 hours of compute each; then appointed an external board (**Gowers, Witten**, others) which
  said *"release this… neither endorse nor condemn."*
- [HYP] **Contrast with Anthropic:** the same window, Anthropic released a paper with **better
  algorithms for 3SUM and all-pairs shortest paths (APSP)** — problems that resisted improvement for
  >50 years — but *contracted human experts* (**Alman and Vassilevska Williams**) to understand and
  write it up with their names on it. Aaronson's stated trade-off: Anthropic gained community buy-in
  and "point people" but put itself in the position of *choosing which humans* become the emissaries.
- [HYP] **Credit/norm discussion:** the emerging standard is that if you use AI but then *fully
  understand* the result, write it in your own words, and take responsibility (answer questions, give
  talks), your name goes on the paper. OpenAI's dump put **"OpenAI" as sole author** on hundreds of
  papers because no human understood them. Aaronson: papers now carry **AI-usage statements** (often at
  the end; he'd put them at the top); *"certified organic theorems"* will have "a very small market."

### 2d. P vs NP — **stays hypothetical/illustrative throughout** (verified framing)

- [EST] **Confirmed: no real P vs NP resolution is claimed anywhere in the video.** The topic appears
  only under explicit "suppose…" framing, and Aaronson twice states the counterfactual premise is false:
  - Opening teaser: *"Suppose Anthropic has a proof that P equals NP. Do you think they should
    release it?"*
  - At [2973–2978] on the disclosure question: *"even short of P equals NP, which is by the way
    something that I don't believe is true. Right? So this is a theoretical discussion."*
  - The Maxwell's-demon / pseudo-entropy / second-law segment (≈[4313]–[4887]) is entirely conditional
    on *"suppose that P is equal to NP."*
- [HYP] **Disclosure content (house-relevant):** Aaronson reasons by analogy to responsible-disclosure
  norms (cyber: notify, ~90 days). The hardest case — a break of RSA/Bitcoin — has no single party to
  notify; options he names: **demonstrate possession via a zero-knowledge proof** (prove you have it
  without revealing it), or notify the government (which he notes many would reject), and *"in practice
  it will be up to whatever company… does this first to decide."*
- [HYP] He observes the 372-paper release covered **every area of math "with the conspicuous omission
  of cryptography"** and calls it obviously deliberate — his inference, not a stated OpenAI policy.

### 2e. Beyond math: the "flood," physics, and the second-law tangent

- [HYP] *"This is coming for all of us."* Physics lags because its problems are **less crisply
  defined** / harder to mechanically check; math and *mathematical physics* fall first because the
  reward signal is self-contained and machine-checkable (→ RL). (Same mechanism as his 2026-10-12
  Peterman-Pod telling.)
- [HYP] Chess analogy: Deep Blue/Kasparov 1997 did not kill chess; chess is more popular than ever
  (kids' tournaments in Austin "packed"). His hope the same holds for math.
- [HYP] **Unitary synthesis problem** (Aaronson & Greg Kuperberg, ~20 years ago): OpenAI's dump
  contained a solution *opposite* to their conjecture — that applying any unitary via an oracle Boolean
  function *is* efficient — with follow-on improvements implying that **if P = PSPACE**, Harlow–Hayden
  black-hole-radiation decoding and firewall creation would be easy. He frames this as a *complexity*
  result, not a physics claim, and notes P ≠ PSPACE ("almost as hard as P ≠ NP") "conspicuously still
  has not been done" by AI.
- [HYP] Closing tangent: **IIT critique** — Chalmers-era XOR-gate objections; IIT's Φ "pulled out of
  nowhere"; Tononi's reply "bite[s] the bullet." (Outside the core story; noted for completeness.)

### 2f. Names/claims offered in passing (not verified this pass unless marked)

- [HYP] Boaz Barak described as "a leading safety researcher at OpenAI." (Real complexity theorist; the
  current OpenAI role is **not verified this pass**.)
- [HYP] Mollowitz/"Donna" dating from 2009; the son's age (9).
- [HYP] The chess/Deep Blue 1997 recollection; "God's Love"-adjacent asides.

---

## 3. Independent verification (this pass, 2026-10-26)

### 3a. The OpenAI release — **CONFIRMED, with a numeric precision**

- [EST] **Date/quantities.** 2026-10-06; **722 manuscripts / 372 result families**, via a GitHub repo;
  topics spanned algebra, number theory, TCS, logic, probability, topology. Tried on **~4,000
  problems**, **~3 hours compute per result**, **unreleased internal model**. (Wikipedia; Scientific
  American; Zvi Moshshowitz; implicator.ai.)
- [EST] **Aaronson's "almost 400 solved" maps to the 372 result families** (Quanta says "376 other
  results"); the manuscript count is 722. So "almost 400" is directionally right *for result families*,
  imprecise on the unit. Tag the number [EST] with this correction.
- [EST] **Advisory board with Gowers and Witten** — CONFIRMED (Aaronson blog, quoted by Zvi; Wikipedia
  names nine mathematicians at Princeton IAS, recommendations 2026-09-29).
- [EST] **Non-peer-reviewed; Lean coverage partial.** About **42%** of top-line results (300 of 719) had
  machine-checked Lean proofs; OpenAI's README warns "some of the unformalized results could have
  issues." **Withdrawals:** three manuscripts pulled (no Lean proofs); a **sign error** forced a further
  withdrawal plus two dependent papers and 14 patches (counts 722 → 719). (implicator.ai; letsdatascience;
  Daily AI Safety News; huxiu/36kr.)
- [EST] **The UGC entry:** catalogue entry ~102, "proof of Khot's Unique Games Conjecture,"
  *accompanied by a Lean formalization.* Quanta: "the highest-profile example of an AI-generated proof
  in theoretical computer science to date" — "and that's including the 40 other TCS proofs released at
  the same time."
- [EST] **The priority race** (Quanta, 2026-10-07): Dor Minzer (MIT) and students Yumou Fei, Shuo Wang
  had a milestone result on a *slightly weaker* variant (Khot's 2-to-1 games, 4-to-1 option version) and
  rushed a 95-page preprint to ECCC (2026-09-14) to avoid being upstaged by the rumored OpenAI proof.
  OpenAI's release included a **Lean-verified proof of the 2-to-1 conjecture** — "but in an AI-generated
  manuscript that didn't undergo any human editing or review by independent experts."

### 3b. Aaronson's own blog — the primary text behind the podcast claim

- [EST] Aaronson's post **"The Mathocalypse"** (Shtetl-Optimized, 2026-10-07) states: *"among the 372
  huge results released yesterday by OpenAI… was a proof of Subhash Khot's Unique Games Conjecture
  (UGC)… Or at least, we're pretty sure that it's a proof!"* — i.e. the podcast characterization is
  **Aaronson's own blog position, hedge included**, not a Jaimungal gloss. (Also: the UGC proof
  "invents a completely new bizarre code with a noise test… some alien craziness.")

### 3c. Subhash Khot / the UGC — **CONFIRMED (ASR garble corrected)**

- [EST] **Subhash Khot**, 2002, *"On the power of unique 2-prover 1-round games,"* Proc. 34th ACM STOC,
  pp. 767–775. UGC is central to **hardness of approximation** (implies NP-hardness of beating
  semidefinite-programming approximations for Max Cut and all CSPs; ties to the PCP theorem). Khot won
  the **Nevanlinna Prize** (2014) largely for it. (Wikipedia "Unique games conjecture"; Quanta,
  *A Grand Vision for the Impossible*; NYU faculty page; Simons Foundation; IAS.) The ASR "Subash Coat"
  is corrected to **Subhash Khot**; the video renders no year, and the correct year is **2002**.

### 3d. Association for Human Mathematics (AHM) — **CONFIRMED REAL**

- [EST] **ahmath.org** is a real organization; it published *"AHM Statement on OpenAI's October 6
  Release of Mathematical Documents"* (2026-10-07). Verbatim opener: *"Mathematicians did not ask for
  this work to be done."* It criticizes OpenAI for ignoring AGMAI's own opening position (frontier labs
  should not test advanced problems on internal models), calls 700+ files at once *"not a demonstration
  of scholarship, but a demonstration of power,"* and **urges mathematicians to discontinue work with
  OpenAI**. (ahmath.org; Indian Express; Moneycontrol; Mezha.) Membership reported between ~752
  (Moneycontrol) and **1,008+ real-name members** as of Oct 25 (36kr) — treat the figure as [HYP]-grade
  (sources vary).

### 3e. Navier–Stokes / the priority dispute — **CONFIRMED (both positions on record)**

- [EST] OpenAI announced a Navier–Stokes solution **2026-09-08** (forced, smooth-force blow-up);
  **Tristan Buckmaster** (NYU) and **Levent Alpöge** (**Anthropic**) had simultaneously proved forced-
  Euler blow-up; dispute over whether OpenAI was tipped off; **OpenAI called the claims "categorically
  false."** (Wikipedia "Navier–Stokes priority controversy"; USA Today; ABC; gadgetsnow.) Aaronson's
  narration matches the public record. **Note:** the house has already filed the deeper audit —
  `openai_navier_stokes_formalization_gap_2026-10-09.md` (the NL↔Lean mismatch, arXiv:2610.08144).

### 3f. Anthropic 3SUM / APSP — **CONFIRMED**

- [EST] Josh **Alman** (Columbia) & **Virginia Vassilevska Williams** (MIT), *"Truly Subquadratic 3SUM
  and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs,"* **arXiv:2610.06783, posted
  2026-10-05** — 3SUM in O(n^1.9992), APSP in O(n^2.9995), deterministic; refutes the 3SUM and APSP
  hypotheses. The paper credits the core algorithm to **Claude (Anthropic)**, which found it in an
  unattended long-context session; Anthropic shared it with the two researchers under a confidentiality
  agreement with compensation, and they wrote it up. (arXiv; cellcog; Zvi; AGTP.) **One correction to
  Aaronson:** he says Anthropic's paper came out *"the same day"* as OpenAI's release; it was posted
  **one day earlier (Oct 5, vs OpenAI Oct 6)**.

### 3g. Other confirmed context

- [EST] The 2026-09-08 Navier–Stokes claim was preceded by a **declaration signed by 28 Fields
  Medalists**, *"A Severe Misalignment of AI in Mathematics"* (2026-09-11), warning of "detrimental"
  effects from treating unsolved problems as benchmarks. (Wikipedia.)
- [EST] An October 2026 **NPR** segment (2026-10-21) features **Dana Moshkovitz** on exactly this; her
  on-record words: the UGC proof *"looks right"* and *"the solutions still need to be checked… the
  AI-generated papers are a tough read."* (NPR; UT Austin CS news page.)

### 3h. Not independently checked this pass (do NOT cite as confirmed)

- [HYP] Aaronson's **unitary synthesis** claim (his own 20-year-old problem, OpenAI's opposite result,
  Harlow–Hayden/PSPACE implication) — his account, not verified here.
- [HYP] **"Astra"** as the specific model Moshkovitz used.
- [HYP] **Boaz Barak's** OpenAI safety role.
- [HYP] The **cryptography-omission** read (his inference).
- [HYP] The AHM **member count** (sources range 752–1,008).
- [HYP] The ~10%-of-4,000 "solved" framing (OpenAI's own; the verified figure is 372 families/~4,000 attempted).

---

## 4. Core claims — register table

| # | Claim (as stated) | Register | Basis |
|---|---|---|---|
| C1 | OpenAI released ~400 AI math solutions incl. a UGC proof (~2 wks before) | **[EST]** (corrected) | 2026-10-06, 722 manuscripts / 372 families / ~4,000 tried; Aaronson's "~400" = result families |
| C2 | The release included a proof of the **Unique Games Conjecture** | **[HYP]** (claimed, not established) | OpenAI's claim + Aaronson blog; **non-peer-reviewed, no human had checked it**; Moshkovitz "looks right"; "we're pretty sure" |
| C3 | UGC originated with **Subhash Khot**, 2002 | **[EST]** | STOC 2002 paper; Wikipedia; Quanta; NYU |
| C4 | "Association for Human Mathematics" is real and issued a statement | **[EST]** | ahmath.org statement 2026-10-07 |
| C5 | Lean formalization certifies correctness of the *proof* | **[HYP] / [A]** | Lean certifies the *coded* statement; NL↔formal gap is unverified — SPEC-GAP (§5) |
| C6 | OpenAI appointed an advisory board incl. Gowers & Witten | **[EST]** | Aaronson blog via Zvi; Wikipedia (9 mathematicians, IAS) |
| C7 | Navier–Stokes priority dispute (Buckmaster/Alpöge vs OpenAI) | **[EST]** | Wikipedia; USA Today; ABC; gadgetsnow |
| C8 | Anthropic released 3SUM/APSP result via human experts (Alman/Williams) | **[EST]** | arXiv:2610.06783, 2026-10-05; credits Claude |
| C9 | P vs NP is discussed only hypothetically; no real P=NP claim | **[EST]** | Aaronson: "something that I don't believe is true… a theoretical discussion" |
| C10 | The 372 results conspicuously omit cryptography | **[HYP]** | Aaronson's inference; no OpenAI policy statement |
| C11 | "A robot solved a math problem [Moshkovitz] worked on her whole career" | **[HYP]** (partly [EST]) | Moshkovitz (NPR): the UGC *candidate proof* "looks right" but is unchecked; Newton's "solved" outruns "appears solved" |
| C12 | Physicists are "watching nervously"; math fell first because verification is self-contained | **[HYP]** | Aaronson's mechanism; no measurement |

---

## 5. Why this matters to the house (two live connections, no forced mapping)

### 5a. [A] It is a live, at-scale instance of the house's own SPEC-GAP / Lanyon–Gorard rule

- [A] The house already named this exact failure mode in `openai_navier_stokes_formalization_gap_2026-10-09.md`:
  **machine verification certifies the code's theorem, not the intended theorem**; the specification
  step is the weakest link, invisible to the formal system by construction. The TOE story is that same
  gap, now applied to **the UGC and the whole 372-paper dump**: a Lean certificate on a *coded* UGC-like
  statement is not a proof of the conjecture a human wrote down, and the translation step was never
  audited. Aaronson's own hedge — "we're pretty sure that it's a proof" — is the gap in miniature, and
  Moshkovitz's job (reading, not proving) is the audit that the house's rule says must happen before any
  register upgrade.
- [A] The house's rule (as written in the Navier–Stokes drop) — *a formal verification without a spec
  audit is inflated-label by default* — is **directly load-bearing here**. Under it, "OpenAI proved the
  UGC" cannot enter the canon above [HYP] until the statement, not just the proof, has been diffed by
  human eyes. That is why this drop tags C2 as [HYP], not [EST].

### 5b. [A] Epistemic-trust, expert-role, and disclosure norms (present-day governance)

- [A] The story is a concrete present-day instance of **frontier capability outpacing human verification
  capacity**: results produced in hours that the world's experts need weeks-to-months to read, with the
  *writing quality itself* (pages on trivialities, a crucial step unexplained) now the bottleneck. This
  is the same "verification capacity as the scarce resource" shape as the REA sibling drop, and it bears
  on the house's `ledger-certifies-provenance-not-truth` reconciliation (a Lean cert ≅ a ledger commit:
  integrity guaranteed, evaluation still pending).
- [A] **Disclosure norms** (the video's open-and-close hook): "should Anthropic release a proof of
  P = NP?" is a real, first-class AI-safety disclosure question, and Aaronson's answer — cybersecurity-
  style responsible disclosure, **zero-knowledge demonstration of possession**, the "no single party to
  notify" problem for a break of RSA/Bitcoin — is directly relevant to the house's standing
  AI-safety-disclosure interests. It is filed here as [A]/[HYP] (his position), not as a house claim.
- [A] The **credit/exposition** shift (human mathematician as interpreter/anthropologist of AI-produced
  artifacts; "OpenAI" as sole author because no human understood) is a social-organizational change the
  house's present-day-engagement commitment covers. It rhymes with — but is **not** — an EILT identity
  claim; the deeper "provenance ≠ authorship" friction was already worked in the Oct-12 Peterman drop.

### 5c. Friction Rule — one [CRITICAL DIVERGENCE]

| House commitment | What this story does to it | Register |
|---|---|---|
| The register-discipline / spec-audit gate *works* because human experts can, in finite time, read and adjudicate AI output; the ledger's value is that a human-verified layer sits above machine output. | **[CRITICAL DIVERGENCE]** The story's operative fact is that the human verification layer is **already the bottleneck and is being outrun at scale** (372 results; ~42% Lean-checked; a two-week scramble to read *one* proof). The house's own canon pipeline runs at human speed and is subject to the same arithmetic — it is **not exempt** from the capacity gap it is diagnosing. Aaronson's own stance is *adapt to the flood*, not *gate it*; the house's stance is a gate. Filing the divergence honestly: a gating discipline is only load-bearing if it can keep pace, and this story is evidence about whether it can. | **[A]** |
| "A signature asserts a completed act" (no signing an unreviewed artifact). | OpenAI's **"OpenAI as sole author, no human understood it"** is the exact anti-pattern the house's signature rule forbids — a useful confirming case, but the divergence above is the one that bites: the house's rule presupposes a verifier who can complete the act. | **[A]** |

---

## 6. The single most load-bearing unverified claim (what would most embarrass us if repeated as fact)

- [HYP] **C2 — "OpenAI proved the Unique Games Conjecture."** This is the dramatic hook a lazy summary
  repeats, and it is exactly where register-inflation is most likely. The verified facts are: (i) OpenAI
  *claimed* it and (ii) attached a Lean formalization. What is **NOT** established: that the Lean code
  matches the natural-language conjecture, or that any human has verified the full argument. Moshkovitz
  says only "it looks right"; Aaronson hedges "we're pretty sure"; it is non-peer-reviewed; one OpenAI
  release in the same cycle was already **withdrawn for a sign error**. Repeating C2 as fact would
  assert a 24-year-old open conjecture *proven* on a candidate proof's say-so.
- [HYP] **Runner-up: C11 — "a robot solved the problem Moshkovitz worked on for her career."** Corrected:
  the robot produced a *candidate* proof of (a Lean-coded version of) a conjecture she worked on; calling
  it "solved" collapses "claimed" into "proven."

---

## 7. Falsifiers / what would change the verdict

- [HYP] **F-UGC1:** independent human verification (a referee report, a hand-audited re-formalization of
  the *natural-language* UGC statement, or Moshkovitz/Quanta follow-up confirming the proof) → upgrades
  C2 from [HYP] to [EST]. Its absence keeps C2 at [HYP] indefinitely.
- [HYP] **F-UGC2:** a documented NL↔Lean spec mismatch in a *named* UGC-cluster manuscript (as happened
  for Navier–Stokes) → confirms the SPEC-GAP reached the flagship result.
- [HYP] **F-UGC3:** further withdrawals/corrections beyond the sign-error set → deflates "most of them
  are actually correct" (Aaronson's own concession) to "unknown fraction correct."
- [HYP] **F-NORM1:** OpenAI publishes an accounting of the ~4,000 attempted vs resolved *and* the
  per-result verification status → moves C1/C10 off inferred footing.

---

## 8. Verdict

- [EST] **The headline event is independently confirmed; the headline *claim within* it is not.**
  (a) OpenAI's 2026-10-06 release of 722 manuscripts / 372 families, incl. a Lean-formalized **candidate**
  UGC proof and a Gowers/Witten advisory board, is **fully confirmed** by multiple independent sources.
  (b) The characterization "a **proof** of the Unique Games Conjecture" is **only OpenAI's claim plus
  Aaronson's own hedged blog**, is **non-peer-reviewed**, and had **no human verification** as of the
  video — so it is filed at **[HYP]**, not [EST]. → **Partially confirmed**: the release is real; the
  *proof* is not established.
- [EST] **Most consequential best-verified fact:** frontier AI, in one Oct-6 dump, produced **372
  research results (722 manuscripts)** — ~42% machine-Lean-checkable, none human-refereed, one cluster
  already withdrawn for a sign error — **faster than the world's mathematicians could read them**, forcing
  a public priority race (Minzer's team rushing a 95-page preprint) and a formal boycott movement (AHM).
  The scarce resource is now **human verification capacity**, not proof generation.
- [EST] **Worth flagging as a major present-day AI-capability milestone — yes, but at the right register.**
  Flag the *release and its verification crisis* as a major milestone (it is well-sourced and is the same
  class of story as the REA drop). **Hold "the Unique Games Conjecture has been proven" at arm's length**
  until an independent human audit lands (F-UGC1); do **not** repeat it as fact.
- [A] **No EILT/cosmology mapping forced.** The genuine house connections are (i) the SPEC-GAP /
  Lanyon–Gorard rule applied at scale (§5a), and (ii) present-day verification-capacity and
  disclosure-norm questions (§5b), with the honest [CRITICAL DIVERGENCE] that the house's own
  human-speed gate is not exempt from the capacity gap it names (§5c).

*Draft compiled by Dion (ClawHorde Backend, subagent research pass) | Status: Pre-Adversarial Working Draft*
