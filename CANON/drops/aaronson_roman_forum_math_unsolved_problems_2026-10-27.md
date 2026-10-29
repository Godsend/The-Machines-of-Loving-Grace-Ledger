---
epistemic-registers: EST=established fact (independently verified this pass) HYP=stated claim/hypothesis, not independently verified A=analogy/our reading (not the source's claim) C=conjecture POETIC=evocative/unfalsifiable RIFF=our extension beyond the source
rule: no tag = treat as MYTH (do not build on it)
id: aaronson_roman_forum_math_unsolved_problems_2026-10-27
title: "Scott Aaronson on 'The Roman Forum with Roman Yampolskiy' — 'AI Is SOLVING MATH Problems That Went Unsolved for CENTURIES': the same OpenAI math story, plus NEW Lean-kernel/formalization detail, a derandomization result, and a quantum-computing half"
source: Roman Yampolskiy (The Roman Forum), YouTube `NDS2dw1vJQs`, uploaded 2026-10-27, 84:31 (5071s).
guest: Scott Aaronson (UT Austin; director, UT Austin Quantum Information Center), interviewed by Roman Yampolskiy (host).
date: 2026-10-27
canon-id: CANON-2026-10-27-AARONSON-ROMANFORUM-MATH-CENTURIES
filed-by: Dion (research subagent pass)
type: SOURCE DROP — companion/update to yesterday's OpenAI-UGC drop. Present-day AI-capability/governance engagement, with independent verification pass. No forced EILT/cosmology mapping.
tags: [openai, unique-games-conjecture, khot, aaronson, yampolskiy, roman-forum, lean4, lean-kernel-bug, formalization-gap, spec-gap, L-BPL, derandomization, 3sum, apsp, p-vs-np, quantum-computing, bitcoin-post-quantum, watermarking, clickbait-title-mismatch, register-inflation, present-day-capability]
transcript: /data/SecondBrain/Canon/YT_TRANSCRIPTS/NDS2dw1vJQs_Aaronson_RomanForum_MathUnsolved_CENTURIES_2026-10-27.txt
transcript_ts: /data/SecondBrain/Canon/YT_TRANSCRIPTS/NDS2dw1vJQs_Aaronson_RomanForum_MathUnsolved_CENTURIES_2026-10-27_timestamped.txt
cross-refs:
  - openai_math_proofs_unique_games_conjecture_aaronson_2026-10-26.md   # PRIOR DROP: same underlying story (TOE/Jaimungal), read in full first
  - DIGEST_2026-10-11_Yampolskiy_vs_Bach_ControlSuperintelligence_Keating.md   # PRIOR DROP: Yampolskiy's own filed positions, read in full first
  - openai_navier_stokes_formalization_gap_2026-10-09.md   # the SPEC-GAP / NL↔Lean companion
---

# Canon Drop — Aaronson on Yampolskiy's show: same OpenAI story, new formalization-kernel detail, and a quantum half

## 0. Provenance and method

- [EST] **Transcript pulled this pass; read in full.** `youtube-transcript-api` (primary rail in the
  `youtube-transcript-rail` skill) succeeded first try via `~/.hermes/bin/uv run --with
  youtube-transcript-api` — **no IpBlocked/429, rung 1 worked**, so rungs 2–4 were not needed.
  **2,137 snippets, 79,574 chars** (plain), 94,042 chars (timestamped), full coverage
  `[0] → [5066]s` vs `duration=5071s`. Saved to
  `Canon/YT_TRANSCRIPTS/NDS2dw1vJQs_Aaronson_RomanForum_MathUnsolved_CENTURIES_2026-10-27.txt`
  and `…_timestamped.txt`. Metadata verified with `yt-dlp --print`: title
  `"AI Is SOLVING MATH Problems That Went Unsolved for CENTURIES"`, channel
  `"The Roman Forum with Roman Yampolskiy"`, upload `20261027`, `dur=5071s`, id `NDS2dw1vJQs` — matches the brief.
- [EST] **`list()` finding (worth recording):** YouTube offered **21 auto-generated caption tracks and
  ZERO manual/human tracks** (`generated=True` for every language). There is **no human-authored
  transcript** for this video; everything below is auto-caption, with the usual proper-noun garbles.
- [EST] **ASR-verbatim NOT guaranteed.** Garbles corrected below where a primary source confirms the
  name: "Scott Aronson"→Aaronson; "Ellie Ykowski"/"Yudkowsky"→Eliezer Yudkowsky; "Yetkowski"→(see §6a
  ambiguity, likely Roman Yampolskiy); "Yan Lun"→Yann LeCun; "threesome"→3SUM; "Virginia Vaselvka"/"Josh
  Olman"→Virginia Vassilevska Williams / Josh Alman; "Andrew Wilds"→Andrew Wiles; "FMA's last theorem"→
  Fermat's Last Theorem; "Pearlman's poner conjecture"→Perelman's Poincaré conjecture; "Ilia Sutsker"→
  Ilya Sutskever; "Sam Alman"→Sam Altman; "Boaz Barack"→Boaz Barak; "or atomic"→Oratomic; "quer"→QuEra;
  "Continum/Quantinuum"; "cubits"→qubits; "Fermy Hubard"→Fermi-Hubbard; "Tony Leget"→Tony Leggett.
- [EST] **Independent verification pass run this pass** (per brief, same discipline as every drop this
  week): `web_search` reads of primary sites (openai/math GitHub `history.md` + `lean/docs/103.md` +
  `lean/OAI/…/Equality.lean`), Wikipedia (UGC; 3SUM; AI watermarking), oss-security/CVE records (Lean 4
  kernel), Quantinuum, The Verge, NPR, Fortune, Simons Institute. Results in §5.

---

## 1. Bottom line (verdict up front)

- [A] **This is NOT a near-duplicate of yesterday's drop** — it carries genuinely new material (the
  **Lean-4 kernel-soundness bugs used to prove `0=1`**, the **`L = RL = BPL` derandomization result**,
  Aaronson's own **watermarking** claim, a long **quantum-computing / Bitcoin** block, and a direct
  **P vs NP** Q&A). But the *core* story (OpenAI's Oct-6 dump + a claimed UGC proof) is the same, and it
  **resolves none of yesterday's open questions** (no verification update; the 3 withdrawn manuscripts
  are **never mentioned**). Filed as a full drop because the *new* formalization-kernel content is
  house-load-bearing, not because the UGC story advanced.
- [EST] **The title is a register violation, and it is host side, not guest side.** "Problems That Went
  Unsolved for CENTURIES" does not describe anything Aaronson discusses. The AI-solved problems named in
  this episode are **UGC (2002 → 24 years), `L=RL=BPL` (derandomization, ~1990s), 3SUM/APSP (~50 years),
  P vs NP (1971 → 55 years)**. None is centuries old. The only *centuries/half-century* problems named
  (Wiles's FLT; Perelman's Poincaré) were solved by **humans**, and Aaronson cites them as the *human
  baseline* the AI results are being compared against. See §4 for the explicit mismatch and the
  in-transcript proof that the title is host-produced clickbait.
- [HYP] **Aaronson's substantive math claims are, on the whole, cautious and correctly hedged** — and one
  is *more* cautious than the public record needs. He is fair to the formalization gap; his one flat
  "solved" (at [700]) is a conversational compression, not a claim that the proof is verified (§3).
- [A] **Yampolskiy's host framing is consistent with his already-filed positions** (perpetual-safety
  impossible; proofs reach only current states; treacherous turn). He does **not** re-litigate his
  "don't build general agents" policy here; he mostly asks questions. One host editorial on evals is new
  (§6b). No contradiction with the filed digest found.

---

## 2. What is genuinely NEW here vs yesterday's drop (`…openai_math_proofs_unique_games…2026-10-26.md`)

| # | New material in this episode | Register | Note |
|---|---|---|---|
| N1 | **Lean 4 kernel is "full of bugs"; exploited "within the last year" to produce Lean proofs of `0 = 1`** — "then the bugs get patched and then there were more bugs" [966–980] | **[EST]** (verified, §5b) | Directly reinforces yesterday's SPEC-GAP rule with a *new* mechanism (kernel soundness, not just the statement mismatch). **Not in yesterday's drop.** |
| N2 | **Lean 4's type system consistency is unproven** — "no one has actually proven that the type system of Lean 4 is consistent… it might literally be inconsistent"; ideal = prove `ZFC (+ large cardinals) → Lean consistent` [1002–1031] | **[HYP]** (his claim; plausible, not verified here) | New. |
| N3 | **`L = RL = BPL` (exact derandomization of logspace)** — a *second*, different OpenAI result: Moshkovitz's Simons Institute semester program on derandomization was converted into "a semester program on understanding the proof of **L equals BPL** that OpenAI released" [686–690] | **[EST]** (result exists, §5a) | New problem, new instance of the same "we produced it / nobody has digested it" pattern. |
| N4 | **Aaronson "invented the first scheme for watermarking LLM outputs,"** now deployed by DeepMind/OpenAI/Anthropic, the latter two "mostly to comply with EU regulations" [1955–1970] | **[EST]** (verified, §5c) | New. |
| N5 | **Weekly meetings with Ilya Sutskever at OpenAI** (a year and a half); Ilya's recurring ask: "what is the mathematical definition of what it means for the AI to love humanity"; Aaronson's reply — "maybe this is more than a math problem. Maybe this is 3,000 years of moral philosophy"; new UT Austin course "AI alignment theory" [1926–2046] | **[HYP]** (his account; corroborated by his blog/podcasts, §5c) | New. |
| N6 | **P vs NP Q&A** — host asks directly whether AI resolves P vs NP "in the next two years"; Aaronson: "I certainly can't rule it out"; if solved soon, "almost certainly AI will have played a central role"; P vs NP "notably was not among" the solved problems "and that was not for lack of trying"; he "strongly conjectures" P ≠ NP, undented by AI [42–145, 434–441] | **[HYP]** (his forecast/conjecture) | New (yesterday's drop only had the *hypothetical disclosure* framing). |
| N7 | **The whole quantum-computing half** (~[3258]–[5010]): most powerful device "by some measures" = **Helios at Quantinuum (~100 qubits, >99.9%)**; Shor's algorithm; fault-tolerance as the missing "critical mass"; **Oratomic's ~30,000-physical-qubit estimate to break 256-bit ECDSA** ("what Bitcoin uses"); "the time to start migrating Bitcoin to post-quantum encryption is **now**"; quantum money; no-cloning theorem; quantum information [3258–5010] | mix **[EST]/[HYP]** (see §5d) | Wholly new topical block — nothing in yesterday's drop. Adjacent to the UGC story, not part of it. |
| N8 | **"AI did enough probably for several Fields medals… dozens or hundreds of tenure faculty positions"**; "how many of us have had new ideas at the level of general relativity or Gödel's incompleteness theorem? maybe a few dozen people out of a hundred billion who have lived" [236–280] | **[HYP]** | New framing of the magnitude; his opinion. |

**Not new / carried over unchanged:** the OpenAI Oct-6 dump; the UGC candidate proof; Moshkovitz's
career spent on UGC; "OpenAI as sole author because no human understood it"; Boaz Barak's exposition-credit
view; the bear/astronomer/math-telescope analogies; the Anthropic 3SUM/APSP contrast (Alman & Vassilevska
Williams); the "AI statement at the end of every paper since this summer" convention; credit-for-the-diff.

---

## 3. Yesterday's open questions — did this interview resolve or update them?

- [EST] **Q: "Is the UGC proof actually verified?"** — **NOT resolved; reinforced, with NEW reasons.**
  Aaronson's headline is flat — *"my wife… spent her whole career working on… the unique games
  conjecture. That was also solved by an OpenAI model"* [696–702] — with **no immediate hedge** (contrast
  his blog's "we're pretty sure" and the TOE interview's "appear to be solved"; here the hedge arrives
  only later, in the technical Q&A). The technical section then gives **three fresh barriers** to treating
  the Lean certificate as verification: (i) the **kernel itself is buggy** [966–980]; (ii) **Lean 4
  consistency is unproven** [1002–1031]; (iii) **the formalized statement may not match the intended one —
  "a question that by its very nature cannot have a formal answer"** [1060–1077]. He also states plainly:
  *"not all of these statements actually have been verified in lean"* [1086] and *"the real goal is not
  having the lean certificate. It is an actual human being understanding the ideas"* [1100–1109]. Moshkovitz
  is still "spending all her time to understand that" [703–705].
  → **Register stays [HYP]; the SPEC-GAP rule gains a second, independent support pillar.**
- [EST] **Q: "What happened with the 3 withdrawn manuscripts?"** — **NOT mentioned at all in this
  video.** `grep` confirms the transcript contains zero occurrences of "withdraw", "peer", or "sign
  error." The public record already resolved this on 2026-10-07 (repo `history.md`: sign error in
  *"Algebraicity of Weil classes on split abelian eightfolds"* → 3 withdrawn, 722→719; 14 revised;
  ~42% Lean-formalized, §5e). So this interview adds **nothing** on the withdrawals — the gap is filled
  by the repo itself, not by Aaronson.
- [HYP] **The "same day" imprecision recurs.** Aaronson again says Anthropic's paper came out "the same
  day" as OpenAI's dump [1230–1233]; it was posted **one day earlier (2026-10-05 vs 2026-10-06)** — the
  same correction yesterday's drop made. Stated twice now across two interviews.

---

## 4. Title-vs-content mismatch — flagged explicitly (this is the register story)

- [EST] **The title says "Problems That Went Unsolved for CENTURIES." Nothing in the episode supports it.**
  Problem ages actually named: **UGC = 2002** (24 yr); **`L=RL=BPL` = derandomization of logspace** (a
  ~1990s–2000s question); **3SUM/APSP = "half a century"** (host's and Aaronson's own phrase, [1251]); **P
  vs NP = 1971** (55 yr) and explicitly *unsolved*. **Even the most generous single case is ~55 years —
  roughly a quarter to a half of one century, and the title claims "centuries" (plural).**
- [EST] **The only century-scale problems Aaronson names were solved by HUMANS, and he cites them as the
  human baseline.** *"Andrew Wiles's proof of Fermat's Last Theorem or… Perelman's proof of the Poincaré
  conjecture"* [1140–1148] are offered to argue the AI proofs are **not** beyond human comprehension —
  i.e., they are the *comparison class*, not AI achievements. The title repackages human century-scale
  results (or exaggerates the age of the AI-solved ones) into an AI claim.
- [EST] **The title is host-produced clickbait, on the record, inside the video.** The host's final
  segment: *"the one final question I ask everyone — you have to come up with a clickbait title for this
  episode"* [5013–5015]; Aaronson declines — *"I'm terrible at clickbait headlines"* [5039–5042]; the host
  replies *"We'll see how the episode does. **We'll be test all your versions**"* [5043–5046] — i.e.
  the channel **A/B-tests titles** and the guest **refused to supply one**. The uploaded title therefore
  reflects the channel's packaging, not anything Aaronson said. **This is the same title-oversells-content
  pattern as the Amodei interview audit (2026-10-27), here with the smoking gun in-transcript.**
- [A] **Fairness note (house prior on the host):** the mismatch is a *channel-branding* fact, evidenced by
  the host's own words — not inferred from the house's pre-existing opinion of Yampolskiy. Aaronson's
  *content* is not guilty of the inflation; the *wrapper* is.

---

## 5. Independent verification (this pass)

### 5a. `L = RL = BPL` — **CONFIRMED in the OpenAI release**
- [EST] `github.com/openai/math` carries `lean/docs/103.md` — *"Exact derandomization of logarithmic
  space: L = RL = BPL"* — and a Lean formalization at `lean/OAI/Computability/Logspace/Equality.lean`
  (theorem `exact_logarithmic_space_derandomization : L=RL ∧ RL=BPL`). Independent discussion:
  Computational Complexity blog ("a full derandomization of randomized log space") and ai-news-online
  (Family 103). Nuance: one source initially listed Family 103 as *"No Lean"*, later noting OpenAI
  "dropped a claimed Lean proof" — i.e., the formalization came after the initial release. Aaronson's
  claim that OpenAI "released" an `L=BPL` proof the community is now digesting is **[EST]**.

### 5b. Lean 4 kernel bug → `0 = 1` — **CONFIRMED, and it is recent**
- [EST] Multiple 2026 CVEs: **CVE-2026-72844** (forging proofs via nested inductive projections) and
  **CVE-2026-72711** (inference-cache poisoning via opaque declarations), both demonstrating `0 = 1`
  (oss-security 2026-10-26; Patch Herald/Patch Observer). The **Lean Kernel Arena** documents
  `bugs/proj-of-stuck-prop` (`False` via projecting a `Bool` field out of a proposition) **accepted by the
  official kernel at v4.28.0, v4.29.1, v4.33.0 and nightly-2026-08-01**, later fixed by
  leanprover/lean4 #14807/#14806. → Aaronson's "the lean kernel is just full of bugs… within the last year
  people have exploited those bugs to find lean proofs of 0=1" is **[EST]** (subject only to the exact
  count/year, which the CVE dates place in 2026).

### 5c. Watermarking + OpenAI stint — **CONFIRMED**
- [EST] Wikipedia (AI watermarking): *"In November 2022, Scott Aaronson first proposed statistical
  watermarking for LLM outputs"*; his own blog: *"as far as I know, the first LLM watermarking proposal."*
  Deployed by Google DeepMind (SynthID, "very similar"), Anthropic (Aug 2026, credits Aaronson/Google's
  SynthID/Gumbel-softmax), and OpenAI (2026-10-05 rollout in the EU). The **EU AI Act** watermarking
  requirement **entered into force August 2026** — matching Aaronson's "mostly to comply with EU
  regulations."
- [EST] OpenAI stint: joined the **Superalignment team in 2022** (invited by Ilya Sutskever and Jan Leike),
  a two-year leave ending summer 2024; his own account confirms the **weekly Ilya meetings** and the
  "mathematical definition of AI loving humanity" exchange, and the Waterloo in Nov 2023 ("Ilya… attempted
  to oust Sam Altman, and then Ilya got ousted instead"). Consistent with his in-video telling [1926–1953].

### 5d. Quantum / Bitcoin claims — **PARTIALLY confirmed, with a numeric nuance**
- [EST] **Helios / Quantinuum:** ~98–100 physical trapped-ion qubits; **average two-qubit gate fidelity
  99.921%** and single-qubit 99.9975% (Nature, 2026); Oct-19-2026 color-code logical fidelity 99.9995%.
  Aaronson's "~100 qubits, more than 99.9% accuracy," with the self-caveat "by some measures," is **[EST]**.
- [EST-with-nuance] **Oratomic / Bitcoin ECDSA:** sources put the 256-bit ECDLP requirement at **~10,000
  physical qubits (optimal) to ~26,000 (faster, ~10 days)** with neutral atoms (Google: <500,000 qubits /
  <1,200 logical). Aaronson said **"about 30,000."** That is the right order of magnitude but **on the high
  side** vs the ~10,000–26,000 range reported. Tag his number **[HYP]** with the correction; the *order of
  magnitude* claim (tens of thousands, down from millions) is **[EST]**.
- [EST] **"2029, 2030" timelines:** corroborated (Google's internal crypto-migration target 2029;
  Cloudflare 2029; Oratomic/Caltech). His "migrate Bitcoin to post-quantum now" is advice, not a fact.

### 5e. The 3 withdrawn manuscripts — **CONFIRMED (public record; not from this video)**
- [EST] OpenAI repo `history.md`, 2026-10-07: a **sign error** in *"Algebraicity of Weil classes on split
  abelian eightfolds"* invalidated a stabilization-trace cancellation and pulled **two dependents**
  (*Kuga–Satake correspondences*; *rational Hodge conjecture for products of K3 surfaces*) → **3 withdrawn,
  722→719**; **14 revised**; Lean-formalized share **300/719 ≈ 42%**. (Implicator; ipcg; byteherald;
  aiweekly; Retraction Watch via Saudi Times.) Matches yesterday's drop.

### 5f. UGC status — **CONFIRMED still unsolved**
- [EST] Wikipedia's "Unique games conjecture" page **still classifies UGC as an unsolved problem** (Khot,
  2002; Nevanlinna Prize 2014) as of this pass; NPR (2026-10-21) frames it as *"around for decades… being
  solved in hours… but the solutions still need to be checked."* → "OpenAI proved the UGC" stays **[HYP]**.

### 5g. Not independently checked this pass (do NOT cite as confirmed)
- [HYP] Aaronson's magnitude opinions ("several Fields medals", "dozens/hundreds of tenure positions").
- [HYP] "Astra" as the model named in the transcript ("feed it to Astra"; "GPT6.6 Astra") — **The Verge
  independently names OpenAI's "GPT-6 Astra"** as the model behind the Sept Navier–Stokes result, so the
  house name is corroborated; the specific "6.6" string is ASR-uncertain.
- [HYP] "William Kretschmer" (former PhD student → UT faculty colleague) — his account.
- [HYP] Aaronson's claim that P ≠ NP "hasn't been dented" — his conjecture, not a result.

---

## 6. Yampolskiy's host framing — consistent with, or divergent from, the filed digest?

Reference: `DIGEST_2026-10-11_Yampolskiy_vs_Bach…md` (Y1–Y8).

- [EST] **Y6→Y5 reprise, near-verbatim (CONSISTENT).** The filed digest's Y5 was Yampolskiy's claim that
  *"mathematical proofs are about manipulation of symbols on your computer they have no connection to
  physical universe… internal states of agents… are also not subject to those proofs."* Here, as host, he
  re-asks it almost word-for-word: *"let's say we had theoretical proof, mathematical proof over symbols
  on a computer. Does that somehow translate to physical world of atoms and human internal **qualia**
  states?"* [2251–2260], then *"Do you think I can prove something about states of human being?"* [2273–2275].
  → **Same position, restated as a question.** (Aaronson's answer is a substantive divergence: symbols
  *can* map accurately — moon landing, atomic bomb — *if* the mapping is correct; but for human phenomena
  we lack the requisite data, so "in general the best that we can do is to make probabilistic
  predictions," and "AI alignment… will never be fully reduced to a math problem" [2276–2362].)
- [EST] **Y4/Y5 reprise — the treacherous turn (CONSISTENT).** Host: *"if you manage to prove something
  about the current state of AI system, it's safe right now. Does that guarantee that you're not going to
  have a treacherous turn later on?"* [2546–2554]. This is the filed Y5 ("at very best you're going to
  prove something about the **current system**… not about **future states**") + Y4 ("treacherous turn"),
  combined. Aaronson replies "it depends on what you proved about it" and then gives the
  **situationally-aware/model-knows-it-is-tested** argument [2679–2728] — i.e., the guest *agrees* with the
  direction of the host's filed concern. Not a divergence.
- [HYP] **New host editorial (extends his filed positions).** On safety evals [2617–2625]: *"That's what
  they do. They report it as a percentage, not actual misbehavior. And so it looks like it's an
  improvement, but reality more capable and it screws up in many novel ways."* ASR-garbled, but the claim
  is: **% improvement on evals is a misleading proxy; capability gains hide novel failure modes.** This is
  a **new, specific host claim**, adjacent to (and consistent with) his filed distrust of box-based safety
  — worth a line, filed [HYP] as his editorial, not audited.
- [A] **Attribution ambiguity — flag, do not overclaim.** At [2211–2232] Aaronson says, of building a good
  world with powerful AI given enough time, *"even Yetkowski believes that, right? And I'm not going to be
  more paranoid than Ellie Ykowski."* ASR collapses the two similar surnames. The host's reply — *"that's
  quite a standard of paranoia"* — fits "**Yudkowsky**" (= Eliezer, the p(doom)~95% reference), so "Ellie
  Ykowski" = **Yudkowsky** with high confidence. "Yetkowski" is ambiguous between **Yampolskiy** (the
  host, sitting across from Aaronson) and Yudkowsky. **If it is Yampolskiy, Aaronson is attributing to the
  host a more optimistic "we could build a good world given time" position than Yampolskiy's filed views
  (control impossible; wait for willing handover) obviously support** — a possible guest-side
  over-attribution, not independently resolved. Do **not** build on it. → **[HYP]/ASR-uncertain.**
- [EST] **No contradiction with the filed digest.** In this episode the host does **not** restate or
  reverse his Y7 policy ("don't build general agents; build narrow tools; developers liable" — corroborated
  off-show by his "Tools, Not Replacements… Let's just ban general superintelligent agent concept" line and
  his proposed US–China ban). He stays in questioner mode. Nothing here contradicts Y1–Y8.

---

## 7. Core claims — register table

| # | Claim (as stated) | Register | Basis |
|---|---|---|---|
| A1 | AI solved the Unique Games Conjecture (Aaronson: "solved by an OpenAI model") | **[HYP]** | OpenAI claim + his aside; non-peer-reviewed; Wikipedia still "unsolved"; he supplies kernel/consistency/mapping caveats [696–702, 966–1109] |
| A2 | AI will likely resolve P vs NP "in the next few years"; "I certainly can't rule it out" | **[HYP]** | his forecast [42–145]; he strongly conjectures P ≠ NP [434–441] |
| A3 | The Lean 4 kernel is buggy; `0=1` proofs were found within the last year | **[EST]** | CVE-2026-72844 / 72711; Lean Kernel Arena (§5b) |
| A4 | Lean 4's type-system consistency is unproven; may be inconsistent | **[HYP]** | his claim; not verified here (as he says, nobody has proven it either way) |
| A5 | A Lean certificate does not establish that the formalized statement matches the intended one | **[EST]/[A]** | his statement; = the house SPEC-GAP rule; corroborated by OpenAI's own "scope pages" (§5e/ai-news) |
| A6 | OpenAI also released an `L = RL = BPL` derandomization proof now being digested | **[EST]** | openai/math `lean/docs/103.md` + formalization (§5a) |
| A7 | Aaronson invented the first LLM watermarking scheme; now deployed under EU rules | **[EST]** | Wikipedia; his blog; EU AI Act in force Aug 2026 (§5c) |
| A8 | Anthropic's 3SUM/APSP paper came out "the same day" as OpenAI's dump | **[HYP]** (corrected) | it was 2026-10-05, one day **earlier** (§5e, yesterday's drop) |
| A9 | Oratomic: ~30,000 physical qubits break 256-bit ECDSA | **[HYP]** (corrected) | reported ~10,000–26,000; order of magnitude right, figure high (§5d) |
| A10 | "The time to migrate Bitcoin to post-quantum encryption is now" | **[HYP]** | his advice/opinion [3800–3906] |
| A11 | These models are "general intelligences" by some definition; can pass a reasonable Turing test; good at advice/support | **[HYP]** | his opinion [1808–1891] |
| A12 | AI "did enough probably for several Fields medals / dozens-hundreds of tenure positions" | **[HYP]** | his opinion [236–248] |
| H1 | Title: AI is solving math "unsolved for CENTURIES" | **[MYTH]/mismatch** | no such problem in the episode; host A/B-tests clickbait titles; guest refused to write one (§4) |
| H2 | Host: safety evals report a % not actual misbehavior; hides novel failure modes | **[HYP]** | host editorial [2617–2625]; not audited |
| H3 | Host: proofs about symbols on a computer don't reach physical/qualia states | **[HYP]** | reprise of filed Y5; Aaronson rebuts with a mapping-accuracy distinction [2251–2313] |

---

## 8. House relevance (two live connections, no forced mapping)

- [A] **§5b is the headline for the house's SPEC-GAP rule.** Yesterday's drop rested the rule on the
  *statement* mismatch (the formalized theorem may differ from the intended one). This episode adds a
  **lower layer**: the *kernel* verifying the formalization is itself unsound-capable and has recently
  been exploited. That is "**who verifies the verifier**" (the host's exact words [945–947], Aaronson's
  problem too) instantiated in a concrete tool — and it is the same shape as the house's own
  `ledger-certifies-provenance-not-truth` reconciliation. A Lean cert ≅ a ledger commit: integrity at the
  layer it covers, trust deferred to every layer beneath.
- [A] **Verification-capacity, at scale.** The story is unchanged in shape from yesterday — hundreds of
  results, ~42% Lean-checked, human reading "rate limited by the humans who are able to understand and
  explain" [896–912] — now with a *second* OpenAI result (`L=RL=BPL`) forcing a whole Simons Institute
  semester to pivot [686–690]. The scarce resource is human comprehension; the house's human-speed gate
  runs on the same arithmetic (the [CRITICAL DIVERGENCE] filed yesterday stands unchanged).
- [A] **Guest-vs-wrapper register discipline (the house's central failure class, demonstrated live).**
  Same underlying two-week-old story; same guest; but a **channel-branded title** ("CENTURIES") that the
  guest declined to author and that the content does not support. The house's rule — *name the mismatch,
  don't silently correct it* — is exactly what §4 does. This is the cleanest in-transcript receipt the
  house has yet for *why* it tags titles separately from content.

---

## 9. Verdict

- **[A] (a) Genuinely new vs yesterday's drop:** YES — the **Lean-4 kernel-bug / `0=1`** finding [EST], the
  **`L=RL=BPL`** second OpenAI result [EST], the **watermarking** claim [EST], the **P vs NP Q&A**, and a
  large **quantum-computing/Bitcoin** block. The *UGC core* is unchanged and added nothing.
- **[EST] (b) Does the "unsolved for CENTURIES" title hold up?** **NO.** Every AI-solved problem named is
  24–55 years old (UGC 2002; `L=RL=BPL` ~1990s; 3SUM/APSP ~50yr; P vs NP 1971). The century-scale problems
  named (FLT, Poincaré) were solved by **humans**, as Aaronson's own comparison baselines. The title is
  **host-produced clickbait** (host: asks for a clickbait title, says "we'll be test all your versions";
  guest: "I'm terrible at clickbait headlines"). **Register violation, wrapper-side.**
- **[EST] (c) Yampolskiy's host framing:** **consistent with his filed positions, not divergent.** He
  re-asks his own filed Y5 (proofs reach only current/physical-disconnected states) and Y4/Y5 (treacherous
  turn) almost verbatim, adds one new **[HYP]** eval critique, and does **not** revive or contradict his
  Y7 "narrow tools, not general agents" policy. No cell of the prior digest table changes.
- **[A] (d) Full drop or addendum?** **Full drop — justified, but on the *new* material, not the UGC
  story.** If the episode had only re-told the OpenAI/UGC story it would have been a short addendum to
  yesterday's; the Lean-kernel-soundness layer (§5b) and the `L=RL=BPL` instance (§5a) are substantive
  additions to the house's SPEC-GAP canon and earn the full file. THE UGC STORY ITSELF DID NOT ADVANCE.

*Draft compiled by Dion (ClawHorde Backend, subagent research pass) | Status: Pre-Adversarial Working Draft*
