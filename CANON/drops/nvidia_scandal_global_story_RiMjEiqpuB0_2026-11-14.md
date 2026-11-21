---
id: nvidia_scandal_global_story_RiMjEiqpuB0_2026-11-14
title: "BBC News (The Global Story, host Asma Khalid) — *\"Why the Nvidia scandal is bigger than you think\"*; read from the tape and filed as an EILT mapping-with-friction"
date: 2026-11-14
filed_by: Dion
source_type: EXTERNAL / news-analysis episode (scripted cold-open + two interviews) — reporting and expert commentary, NOT a primary document
intake: "operator-delegated canon pipeline, 2026-11-14"
source:
  yt_id: RiMjEiqpuB0
  title: "Why the Nvidia scandal is bigger than you think | The Global Story"
  channel: "BBC News"
  series: "The Global Story"
  duration_s: 1986
  duration: "33:06"
  upload_date: 2026-11-12
  url: https://www.youtube.com/watch?v=RiMjEiqpuB0
transcript: YT_TRANSCRIPTS/RiMjEiqpuB0_nvidia_scandal_global_story_2026-11-14.txt
transcript_timestamped: "(NONE — rung 0 emits no cue-level timestamps; locators below are [Part 1]/[Part 2] only)"
transcript_grade: "RUNG 0 (Gemini YouTube-URL ingest) — a MODEL-READ of the media, NOT a caption track and NOT local ASR; faithful-in-substance, NOT verbatim; splices marked, entities flagged"
epistemic-registers: EST=established HYP=hypothesis A=analogy C=conjecture POETIC=myth/poetic RIFF=riff
register-set: "[EST]/[HYP]/[A]/[C]/[POETIC]/[RIFF] (six-tag house set, declared)"
row-status-flags: "FRICTION | CRITICAL DIVERGENCE | DIVERGENCE | CONVERGENT | SOURCE-ERROR | UNRESOLVED-ASR — flags, NOT registers"
tags: [nvidia, jensen-huang, bbc, the-global-story, asma-khalid, faisal-islam, schriver, kuiken, export-controls, chips-and-science-act, china, espionage, ai-chips, h20, h200, eilt-friction, news-analysis]
---

# Canon Drop — The Nvidia / Jensen Huang scandal (BBC, *The Global Story*)

**Intake:** operator-delegated canon pipeline, **2026-11-14.**
**Date:** 2026-11-14 · **Filed by:** Dion
**Source (VERIFIED this session):** YouTube `RiMjEiqpuB0`, *"Why the Nvidia scandal is bigger than you think | The Global Story"*, channel **BBC News**, uploaded **2026-11-12**, **1986 s (33:06)**. Identity re-verified live with `oembed` (title, `author_name` = *BBC News*, `author_url` = `@BBCNews`) and `yt-dlp --print` (`title`, `uploader`/`channel` = *BBC News*, `duration` = 1986, `upload_date` = 20261112 — all match the brief). **Note:** the brief believed this was a *BBC World Service* series; the tape says only *"from the BBC"* / *"here at The Global Story"*, and the channel is **BBC News** — the *World Service* attributions are **not on the tape** and are not carried here.
**Transcript:** `YT_TRANSCRIPTS/RiMjEiqpuB0_nvidia_scandal_global_story_2026-11-14.txt` (**32,917 chars**, 2 parts).
**Source status:** model-read in full (0:00 → 33:06, both parts, no gaps; part-boundary at 16:33).

> **★ Evidence class (read this before quoting).** The winning rail is **RUNG 0 — a model's reading of the media** (Gemini fileData ingest), *not* a caption track. **Quotes below are FAITHFUL-IN-SUBSTANCE, NOT VERBATIM.** A model transcribing speech drops filler and repairs disfluency, so a sentence lifted from the artifact is usually **spliced across speech the model removed**; such spans are marked `…`. Proper nouns were, unusually, resolved cleanly on this tape (**all load-bearing names verified literal in the artifact**, §5) — but a rung-0 reading can also *invent* a label, so **no named entity is carried out of this drop without a literal containment check**. This drop is **citable for substance and for the artifacts it names**, and **not citable for the exact wording of any speaker.**

---

## 0. What this is, and what it is not

A **33-minute BBC news-analysis episode** of *The Global Story*: a **scripted cold-open** read by host **Asma Khalid** (Washington, D.C.), a **one-on-one with the BBC's economics editor Faisal Islam** (London), and a **studio segment with two US commissioners** — **Randall Schriver** and **Mike Kuiken** of the **US-China Economic and Security Review Commission**.

It is a **news story**, so its register is **reporting and analysis, not a primary document.** The load-bearing facts are, in the tape's own words, traceable to **New York Times reporting** (*"starts with um New York Times reporting"*; *"a New York Times report um on Sunday"*), relayed through the BBC. Expert opinion, forecasts, and the source's own characterization are flagged as such below (§4). **It is NOT a paper, NOT a filing, and NOT a house-adjacent text — the house's vocabulary is spoken ~0× (§3).** The EILT mapping in §5 is therefore entirely **ours**, and it carries the **mandatory `[FRICTION]` divergence** the house requires.

---

## 1. Transcript rail ladder — actual outcomes (probed this session)

| Rung | Rail | Actual outcome this run |
| :--- | :--- | :--- |
| **0** | Gemini YouTube-URL ingest (`gemini-3.8-flash`) | **WON.** Duration probed first (1986 s = 33:06) → **2 windows** (0:00–16:33 = 15,058 chars; 16:33–33:06 = 17,788 chars). Total **32,917 chars**. |
| **1** | `youtube-transcript-api` (Hermes-venv `python3`) | **FAILED.** `.list('RiMjEiqpuB0')` = **one track, auto `en` (`is_generated=True`), NO manual caption**; `.fetch(['en'])` = **`IpBlocked`**; `.find_generated_transcript(['en']).fetch()` = **`IpBlocked`**. (`/usr/bin/python3` does NOT import the module — matches the rail skill's interpreter caveat.) |
| **2** | `yt-dlp --write-auto-subs` | **NOT reached** (first-success rule; rung 0 landed). Not exercised. |
| **3** | CDP transcript panel `:9333` | **NOT exercised** (rung 0 landed). |
| **4** | local `faster-whisper small.en` | **NOT exercised** (rung 0 landed). |

**★ AUDIT OF THE WINNING ARTIFACT (the "multi-part re-transcription" trap was tested for and is ABSENT):** the two parts are **genuinely distinct spans**, not two passes over the same audio — **word-6-gram Jaccard Part1-vs-Part2 = 0.002** (~no overlap), and filler-marker density is **uniform-and-raw** (Part 1 = 3.8 per 1k; Part 2 = 5.1 per 1k) ⇒ a **single-provenance model-read**, no mixed-duplicate file. Coverage is **0:00 → 33:06 of 1986 s = 100 % span.** **★ THE LIMIT OF RUNG 0 STANDS:** no cue-level timestamps were emitted, so **no `_timestamped.txt` exists** and locators below are **[Part 1]/[Part 2]** only; and the reading is **model-read, not verbatim** (header).

---

## 2. Source type, voices, and the register split (reporting vs asserting)

The episode mixes four voice-classes that must not be flattened:

| Voice | Who | Class |
| :--- | :--- | :--- |
| **Host / cold-open** | **Asma Khalid** (named on tape: *"I'm Asma Khalid in Washington, D.C."*) | **Editor's/scripted** — the cold-open asserts the framing (see §6 title/intro audit) |
| **Expert analyst** | **Faisal Islam** (BBC economics editor, London; named on tape) | **Reporting + analysis** — relays NYT reporting and his own prior interview with Huang |
| **US officials** | **Randall Schriver** (chair) + **Mike Kuiken** (vice-chair), US-China Economic and Security Review Commission (named on tape, introduced as *"Randy Schriver and Mike Kuiken"*) | **Advocacy/position** — a bipartisan commission that *already* advocates tighter chip controls |
| **The subject** | **Jensen Huang** (Nvidia) — named on tape; his **email** is read aloud | **Self-statement** (an apology email quoted by the reporter) |

**★ The reporting/asserting split (what the tape actually does):** the **allegation** (a suspected Chinese spy, a national-security concern) is consistently framed as **someone else's reporting** (*"That's according to reporting in the New York Times"*; *"the specific allegation was…"*; *"those are the allegations"*) — i.e. **reporting**, not the BBC asserting it as fact. The **denials** are reported too (the company and the Chinese government both deny). What the tape **asserts in its own voice** is narrower: that **Nvidia has opened an independent investigation** and that **lawmakers are demanding Huang appear**. Everything else that sounds like a fact about the espionage is **relayed NYT reporting**.

> **★ Cold-open vs body — an internal tension worth flagging.** The scripted cold-open says flatly: *"Jensen Huang will no longer be the face of the company. The CEO of one of the world's most valuable companies **has resigned** after reports of two extramarital affairs…"* Yet the **body never restates a resignation** and instead treats the outcome as open (**Faisal: *"in a some hypothetical situation where this costs him his job"***), and Huang's own quoted email is present-tense (*"I support the investigation and will cooperate fully"*). **The resignation claim sits in the cold-open only and is not sustained by the reporting that follows** — filed as `[UNVERIFIED]` (see §7-F, F-NV-3). Do not cite the tape for "Huang resigned."

---

## 3. Provenance, dedupe, and house-vocabulary check

- **★ DEDUPE: NEW.** id `RiMjEiqpuB0` = **0 hits** across `drops/` + `CANON_INDEX.md` **before the pull, immediately before writing, AND after**; title-phrase sweeps (*"Nvidia scandal"*, *"Global Story"*) found **no sibling**. No intake-cron race-window collision.
- **★ HOUSE VOCABULARY SPOKEN = 0.** Mechanical scan of the artifact: **`ledger` = 0, `provenance` = 0, `epiplexity` = 0, `commit` = 0, `substrate` = 0, `Markov` = 0, `attractor` = 0, `polycomputing` = 0, `EILT` = 0, `ruliad` = 0, `constructor theory` = 0, `syntropy` = 0, `free energy` = 0.** ⇒ **no term-borrow; the EILT mapping (§5) is ours, flagged not smuggled.** No coined term requires a coiner credit (Rule 6 check: nothing to attribute).
- **Attribution of the coined/technical items the tape *does* use** — credited at point of use where a coiner exists: none borrowed from the house; `CHIPS and Science Act` (US statute, 2022), `Thousand Talents Program` (a Chinese recruitment programme named on tape), and the quoted **Keith Alexander** line are the tape's own relays.

---

## 4. What the tape actually says (register-tagged)

Quotes are rung-0 (faithful-in-substance; **not verbatim**), locators **`[P1]`/`[P2]`**. Every span below passed a literal containment check against the on-disk artifact (§7-A).

### 4.1 The allegation and its provenance — *reporting, not assertion*
- `[EST]` (as the tape relays NYT reporting) **The core allegation:** *"one with a woman who's suspected of being a Chinese spy. That's according to reporting in the New York Times."* `[P1]`
- `[EST]` (as the tape relays) **How the week crystallised:** *"the one that has crystallized this week has been a a New York Times report um on Sunday."* `[P1]`
- `[C]` **The named third party:** the woman is *"someone called Alice Huang, who was an executive of a… No relation to Jensen, we should be clear."* `[P1]` — described as *"an executive at a Singaporean company um called Megaspeed"* `[P1]`, alleged *"in some way connected to to to Chinese intelligence."* `[P1]`
- `[C]` **Both denials are on the tape:** *"the company concerned has denied it, the Chinese government has denied it, but those are the allegations."* `[P1]`; later China's statement is read: *"the allegations about Chinese spies are entirely groundless, speculative, and intended to smear and malign China."* `[P2]`
- `[EST]` **What the tape asserts in its own voice:** Nvidia *"has opened up an independent investigation, and members of Congress are demanding that Huang appear in front of them to answer their questions"* `[P1]`; *"the Nvidia board of directors are investigating"* `[P1]`

### 4.2 Jensen Huang, in his own (quoted) words — an apology email read aloud
- `[EST]` (email, read by the reporter) **The apology:** *"I owe my family and all of you an apology. I was unfaithful to my wife. My actions hurt her and our children. There's no excuse for what I did. I'm deeply sorry."* `[P1]`
- `[EST]` (email) **The national-security lines:** *"Nvidia's board of directors has initiated an independent investigation. I support the investigation and will cooperate fully."* and *"I love our country and our company. I'm committed to protecting Nvidia and supporting America's national security."* `[P1]`
- `[EST]` (board statement, read) **The board's hedge:** *"while the board has no reason to believe that either national security or Nvidia secrets were compromised, the board inquiry will examine all available information."* `[P1]`

### 4.3 Trump, quoted on camera
- `[EST]` **The President's line (clip):** *"When I heard about it, first of all, I was amazed because I- I view him as a very high-quality person. I've known him a long time. I hope there's no problem. If there is a problem, we'll let you know about it, but I hope there's no problem."* `[P1]`
- `[EST]` (as relayed) Trump *"suggested he was not warned, he has said he doesn't recall being receiving any sort of briefing of that sort"* and *"has stood by very publicly the the CEO of Nvidia, saying that he's an honorable man."* `[P1]`

### 4.4 Nvidia and Huang — the background (framing)
- `[EST]` (as stated) **The company's standing:** Nvidia *"valued at over $4 trillion"* `[P1]`; *"one of the most valuable companies in the world."* `[P1]`
- `[HYP]` (Faisal's characterization) **The claim about importance:** *"I don't think it's kind of over the top to- to to describe Nvidia right now as the most important company in the world."* `[P1]`
- `[EST]` (as stated) **Origin:** *"Jensen Huang founds the company in 1993, and it's about 3D gaming. So it's about making 3D dragons, not transforming the whole the whole world."* `[P1]`
- `[HYP]` (Faisal's analogy) **The Jobs comparison:** *"like the modern-day Steve Jobs in terms of his centrality to the … global tech… I'd say he's more important than Steve Jobs because Apple was… a consumer tech company."* `[P1]` *(the `…` after "to the" marks the host's interjected "That's big.")*
- `[HYP]` (relayed anecdote) **The Stanford "pain" story:** *"What I want to see is pain, because I need resilience in my employees, and you only get that resilience through pain."* `[P1]`
- `[HYP]` (Faisal) **"Too big to fail":** *"there is just too much demand for this company's chips for it to sort of fall over in any in any meaningful way."* `[P1]`

### 4.5 Export controls and the policy thread
- `[EST]` (as stated) **The controls timeline — AS THE TAPE GIVES IT:** *"in 2024 there were restrictions on the export from Nvidia of their highest-performing chips"* `[P1]`; restrictions lifted in July on *"the H20 chip, which was a pared-down lower-power chip"* `[P1]`; *"in December 2025, the more powerful chip, the H200… That ban is lifted in December."* `[P1]` **★ The tape's own dating is muddled** (*"by December… In July of this year… that's July 2025. And then in December 2025"*) — cite the **sequence** (2024 restriction → July H20 → December H200), not a clean date for each in isolation.
- `[EST]` (as stated) **The 2022 statute:** Congress *"tried to encourage the manufacturing of more semiconductors here on US soil by passing what's known as the CHIPS and Science Act."* `[P2]`
- `[HYP]` (Faisal, relaying) **Huang's argument:** *"he literally says, … Donald Trump thinks this and Xi Jinping thinks this, and they're both right."* `[P1]`; *"Both can win. Both should win."* `[P1]`; *"it wasn't a zero-sum game."* `[P1]`
- `[HYP]` (Faisal) **The story's real stake — the argument itself:** *"he was an extremely powerful proponent of that argument, and he won that argument with President Trump… The force of that voice now, you've got to think isn't going to be as strong, and a more hawkish sentiment about the spread of technology… surely prevails."* `[P1]`/`[P2]`

### 4.6 The commission's position (advocacy)
- `[HYP]` **The threat frame:** *"it's totally unsurprising to me that the Chinese State Security Service would be targeting Jensen, and really probably all the people in Nvidia's leadership."* `[P2]` (Kuiken)
- `[HYP]` **The historical claim:** *"the Chinese have been stealing American intellectual property for decades."* `[P2]` (Kuiken), pegged to a relayed *"former National Security Agency commander… Keith Alexander, who said that it was… the greatest heist in the history of the world or something like that."* `[P2]` (hedged by the speaker — *"or something like that"*)
- `[HYP]` **The people, not just the tech:** the *"Thousand Talents Program, where they will invite scientists, engineers to come participate in a conference… and then that conference turns into a relationship."* `[P2]` (Schriver)
- `[HYP]` **The "meaningful delay" claim:** *"6 months to a year of keeping them behind us is meaningful."* `[P2]` (Kuiken)
- `[HYP]` **The commission's settled policy preference** (their own statement): a *"consensus view, both Republicans and Democrats, that we should be very restrictive on the export of the highest-end chips."* `[P2]`
- `[FRICTION]` **★ The denial-as-confirmation move** (the mandatory friction row — see §5-R3): *"It confirmed, you're saying, your Exactly. I mean, I rolled my eyes and, you know, couldn't believe it came out that fast."* `[P2]`

### 4.7 Program framing
- `[RIFF]` **The closing promo:** *"all next week, we here at The Global Story have a special series that dives into the backstory around artificial intelligence."* `[P2]` (host, programmatic — not content)

### 4.8 Register / tag counts (§4.1–§4.7)
≈22 tagged rows. Dominant register **`[HYP]`** (≈13 — analysis, forecasts, characterizations) · **`[EST]`** (≈8 — relays and quoted self-statements) · **`[C]`** 2 · **`[FRICTION]`** 1 (row-status) · **`[RIFF]`** 1. No `[POETIC]`, no `[A]` used as a body register (analogy appears as a status flag in §5). **Strict pre-file gate: PASSED — zero epistemic tags outside the six-tag set.**

---

## 5. EILT / ClawHorde mapping — **Friction Rule applied**

> **The Friction Rule (Yanenko 2026):** *A mapping table requires at least one row where the analogy and the source explicitly disagree. If every row maps cleanly, you have not derived a correspondence — you have decorated a mood.*

Every row carries one of the six registers **in addition to** any status flag. `[FRICTION]` / `[CRITICAL DIVERGENCE]` / `[DIVERGENCE]` / `[CONVERGENT]` are **row-status flags, not registers.** **The house vocabulary is spoken ~0× (§3); every EILT cell below is OURS.** An external news frame can be *isomorphic to* our architecture; it **cannot validate our software.**

| # | This source | EILT / ClawHorde architecture | Register | Status |
| :--- | :--- | :--- | :--- | :--- |
| **R1** | **Chips are the structural substrate of the AI boom.** *"those models are built in a process called training… by the world's most powerful chips… it has been this company, Nvidia, sitting at the epicenter of that process."* `[P1]` The GPU is the frozen physical layer everyone else's inference runs *on*. | **The Fundamental Inversion** (monograph §1): the **ledger** (weights/connectome = frozen structure) is *not* the inference; the **wave** (live process) is. The structural layer *constrains*, it does not compute. | `[A]` | **`[A]` — structural rhyme only.** Both place a **frozen structural layer under a live process**. But the source's layer is **silicon throughput** (a resource to ration), the house's is a **commit history** (a provenance record). Same *shape*, different *kind* — do not read "Nvidia = the ledger." |
| **R2** | **The CEO is a single, load-bearing point.** *"His his his his singular focus has been essential to its success… lesser CEOs would already be in extreme trouble."* `[P1]` | **Persistence ≠ identity** (`§17.3(b)`-family): the ledger **survives a substrate swap** — capability is a property of the *carrier*, not one node in it (the house swaps profiles/runtimes and keeps the ledger). | `[HYP]` | **`[DIVERGENCE]`.** The source *grieves* the node (**"singular focus… essential"**) yet *also* says the company *"won't"* fall over (*"there is just too much demand for this company's chips for it to sort of fall over in any in any meaningful way."* `[P1]`) — the source itself splits. The house reading is sharper: **the structural ledger (Nvidia's position) is separable from the substrate (any CEO)**. The source leans on the person; the house leans on the record. |
| **R3** | **★ A denial is treated as confirming evidence.** Host asks whether China's fast, strong denial raised alarm bells; the commissioner answers *"It confirmed, you're saying, your Exactly"* and *"couldn't believe it came out that fast."* `[P2]` Speed and force of a denial are read as corroborating the spy allegation. | **Provenance is not validity** (house `§18.8` correction; `F-T1`): a record — of an allegation, or of a denial — **certifies origin, never truth.** A denial is evidence about the *state's messaging*, not about the *fact alleged*. | `[EST]` | **★★ `[FRICTION]` — MANDATORY CRITICAL DIVERGENCE (cuts at the SOURCE).** This is a **direct disagreement**: the source treats the *response* to an allegation as evidence *for* it; the house's central plank says **no record of a response can raise the probability of the alleged fact.** A strong denial is not a confession and a fast denial is not a tell. **Do NOT absorb "they denied it fast = it's true."** This is the same class as the house's own retracted move (a ledger certifies provenance, not correctness) — the source commits it on a national-security claim. |
| **R4** | **The race is a monotone "keep ahead" problem.** *"6 months to a year of keeping them behind us is meaningful"* `[P2]`; *"thwarting it for a period of time."* `[P2]` | **Survivorship ≠ fitness** (`§17.3(b)`): staying ahead is **maintenance of position**, not a gain; a lead you must continuously re-buy is a *cost*, not a *value*. Progress is monotone only if the terrain does not move under you. | `[HYP]` | **`[DIVERGENCE]`.** The source frames delay as **accumulating advantage**; the house's effort-over-time lens (`§23`) reads a *maintained* lead as a **standing tax** — and warns it is indistinguishable from a *shortened hill* (goal-lowering). Different models of what "ahead" means. |
| **R5** | **Huang's win-win thesis.** *"it wasn't a zero-sum game"*; *"he won that argument with President Trump."* `[P1]` A single powerful voice steered US policy toward "both can win." | **Alignment is multi-system interaction** (house `§20`): no single system holds "the" objective; policy is a **coupling**, and one voice "winning" an argument is not the system acquiring a stable gradient. | `[A]` | **`[CONVERGENT — reached from outside]`.** The source independently describes policy as a **push-pull over a landscape** (*"a more hawkish sentiment… surely prevails"*) rather than a solved objective. Corroborates the shape; **not evidence for EILT.** |
| **R6** | **Use the crisis.** *"use a crisis to your advantage… this is very good because it allows sort of the American people to understand that the Chinese are in fact targeting us."* `[P2]` | The house's **provenance-not-validity** + register discipline: a record **does not supply an objective**, and an opportunity to advance a prior position is **not** evidence for it. | `[HYP]` | **`[DIVERGENCE]`.** The source treats the scandal as a **warrant** for a position it already held (the commission *already* advocated stricter controls). The house's rule says a fresh record **records**; it does not license the conclusion. |

**Friction verdict:** **1 `[FRICTION]`/`[CRITICAL DIVERGENCE]` (R3) + 3 `[DIVERGENCE]` (R2, R4, R6) + 2 `[A]`/`[CONVERGENT]` (R1, R5).** The table is **NOT** an all-convergent decoration. **R3 is the load-bearing break:** the source's **denial-as-confirmation** inference is the exact move the house's provenance plank exists to refuse — *a record of a reaction is not a measurement of the thing reacted to.* This is the sharpest available Bridge/WeaponWall test on this tape.

---

## 6. Title / intro-vs-content audit (`[SOURCE-ERROR]`)

- **The title is a hedge and is fair:** *"Why the Nvidia scandal is bigger than you think"* — an invitation, not a claim; the body sustains it (the story is tied to *"US policy toward China… and the global race for the chips powering AI and supercomputing."* `[P1]`).
- **★ The cold-open overstates — `[SOURCE-ERROR]` / `[UNVERIFIED]`.** The script asserts **Huang resigned** (*"has resigned after reports of two extramarital affairs"* `[P1]`) and that he *"will no longer be the face of the company"* `[P1]`. **The body does not sustain a resignation** and treats the outcome as open (*"hypothetical situation where this costs him his job"* `[P1]`). **Filed as `[UNVERIFIED]`; the tape is NOT citable for "Huang resigned."** (Row F-NV-3.)
- **`[ABSENT]`:** no `[INFLATED-LABEL]` of the *explainer* kind — the substance matches the framing once the resignation overstatement is set aside.

---

## 7. Verification performed this session (and what was NOT)

### 7-A. Quote gate (zero-fabrication receipt)
Two-verdict gate (**contiguous / spliced**), run against the **flat rung-0 artifact** (`…_nvidia_scandal_global_story_2026-11-14.txt`), frontmatter and this receipt excluded from the target population; controls anchored first.

- **POSITIVE control** (`"Nvidia's board of directors has initiated an independent investigation"` — read straight off the tape): **HIT.**
- **NEGATIVE control** (an invented string, `"the CEO was arrested in Singapore"`): **MISS.**
- **Result (FINAL, re-run after the last body edit):** **75 unique `*"…"*` spans → 58 contiguous / 14 multi-fragment (all fragments present; `…`-marked splices) / 3 non-tape occurrences / 0 FABRICATED.** The 3 non-tape occurrences are named: the **video title** (*"Why the Nvidia scandal is bigger than you think | The Global Story"*) quoted twice as metadata, and the **title-phrase sweep string** (*"Nvidia scandal"*) carried from §3's dedupe check — none is presented as a tape quote.
- **★ The gate CAUGHT and FIXED FOUR real defects in the draft** (all fixed by quoting the tape's served string, never by loosening the normaliser): (1) a wrong possessive — *"Nvidia's board of directors are investigating"* → the tape's *"the Nvidia board of directors are investigating"*; (2) a **fabricated quotation** — *"won't fall over"* (not on the tape) → the literal *"for it to sort of fall over in any in any meaningful way"*; (3) an **unmarked splice** across the host's interjection in the Jobs quote (*"…centrality to the … global tech"*, the `…` marking *"That's big."*); (4) an unmarked splice in the "he literally says" span. **POS control HIT, NEG control MISS.**
- **★ The gate's limit, declared:** on a rung-0 file a **"contained" span is not proof the speaker said those words** — it proves the *reading* contains them. That is the honest ceiling of this artifact.

### 7-B. Named-entity containment (rung-0 entity guard)
Every load-bearing proper noun was `in`-tested against the artifact: **`Jensen Huang` (×18), `Nvidia` (×32), `Trump` (×12), `Xi Jinping` (×3), `H20` (×2), `H200` (×1), `Megaspeed` (×1), `Alice` (×2), `Schriver` (×2), `Kuiken` (×2), `Khalid` (×1), `Islam` (×1)** — **all present, no invented labels carried.** No `[UNRESOLVED-ASR]` strings arose (the reading resolved names cleanly — itself a rung-0 property, not a guarantee).

### 7-C. NOT verified (do NOT cite as established)
- **The espionage allegation itself** — relayed NYT reporting, quoted, **not independently confirmed**; both the company and the Chinese government deny it on the tape.
- **The resignation** — cold-open only (§6); **`[UNVERIFIED]`**.
- **The numbers as clean dates** — the controls timeline is internally muddled (§4.5); cite the **sequence**, not isolated dates.
- **Every figure/id the story names** (`$4 trillion`, `1993`, `2022`, the *H20*/*H200*/*CHIPS and Science Act* names, the commission's founding *"some 25 years ago"*) — **as the tape states them**, `[EST]-as-relayed`; none re-derived from a primary this session.
- **Keith Alexander's "greatest heist"** — the speaker himself hedges it (*"or something like that"*), and the tape attributes it loosely; relayed, not a verified quote of Alexander.
- **The `Keith Alexander` attribution** — the commissior says *"a former National Security Agency commander, I think it was Keith Alexander"* `[P2]` with a hedge (*"I think"*); carry the hedge.

---

## 8. Pre-registered falsifiers

- **F-NV-1 (R3, house-facing).** If it is ever shown that **speed/force of an official denial does reliably discriminate true from false allegations**, §5-R3's divergence collapses to convergent. The house position is on the record: a response is not evidence for the fact responded to. **This is the falsifier that bites the house if wrong.**
- **F-NV-2 (R4).** If a maintained chip lead is shown to **compound** (each month ahead buys more than it costs) rather than tax, §5-R4 fails. Testable against export-control outcome data.
- **F-NV-3 (cold-open, source-facing).** If Huang **did resign** and the body simply under-reported it, the `[UNVERIFIED]` flag on the cold-open is downgraded to a reporting gap. The tape does not settle it either way.
- **F-NV-4 (entity guard).** If a future caption/ASR pull shows any name above is a **rung-0 invention** (e.g. `Megaspeed`), the entity must be struck. Rung 0 can invent labels; gate it before publication.
- **F-NV-5 (R2).** If Nvidia's market position is shown to **collapse** with a CEO change, §5-R2's "the record outlives the node" reading fails for this case.

---

## 9. Verdict — strongest / weakest joint (**opinionated**)

**File it — as a *news* artifact, at the news register, with the reporting/asserting line kept explicit.**

- **Strongest point — the source is honest about the provenance of its own bombshell.** The tape repeatedly grounds the spy allegation in **NYT reporting** and reads **both denials** (the company's and China's) into the record. Where a lesser segment would assert, this one *attributes* — and it reads Huang's **own** email verbatim rather than paraphrasing him. **Second-strongest:** Faisal's reframe of the real stake — not the affair, but **the loss of the one pro-engagement voice that "won that argument with President Trump"** (`4.5`) — is the sharpest analytical claim on the tape, and he marks it as his own read (`[HYP]`).
- **Weakest joint — the commission segment's denial-as-confirmation inference (§5-R3).** Asked whether China's fast, forceful denial alarmed them, the commissioners say it **"confirmed"** their suspicion — reading a *response* as evidence for the *fact alleged*. That is the exact inference the house's provenance plank exists to refuse, and it is the weakest **epistemic** joint on the tape: it converts **messaging behavior** into **evidence of guilt**. **Runner-up:** the cold-open's unsustained **"has resigned"** (§6) — a strong verb in the script that the reporting beneath it does not carry.
- **★ Register discipline:** the relayed/reported layer (the NYT allegation, the denials, Huang's email, the board statement, the export-control names, the CHIPS Act) is `[EST]` **as the source states it**; the analytical/predictive layer (Nvidia's importance, "too big to fail," the hawkish turn, the "meaningful delay") is `[HYP]`. **★ EILT posture:** the mapping is **weak-by-construction** (house vocabulary 0×, §3) and **breaks on the source's own inference** (§5-R3, `[FRICTION]`). **Do not build an EILT derivation on this news piece** — it is a **news rescue with one useful refusal** (R3).

---

## 10. Citable-for / NOT-citable-for

**Citable for (to the rung-0 artifact, garble caveat applied):**
- That the **BBC aired this story** (`RiMjEiqpuB0`, 2026-11-12, 33:06), with the speaker set above (§2).
- The **NYT-sourced allegation** *as the tape relays it* — including that the BBC **attributes** rather than asserts it.
- **Huang's email** and the **board statement** *as read on the tape* (faithful-in-substance).
- Trump's **on-camera clip** *as read on the tape*.
- The **denials** by the company and by China *as the tape reads them*.
- The **policy sequence** (2024 restriction → July H20 → December H200) *as the tape gives it*, with its internal dating caveat.
- **Faisal Islam's analysis** *as his stated position* (`[HYP]`) — the "loss of the pro-engagement voice" frame.
- **The commission's position** *as advocacy* (`[HYP]`) — and, explicitly, the **denial-as-confirmation** move (§5-R3) as an object of house friction.

**NOT citable for:**
- **Any EILT derivation** — the mapping is ours; **R3 is the `[FRICTION]`/`[CRITICAL DIVERGENCE]`; R2/R4/R6 diverge.**
- **The resignation** (cold-open only, §6, `[UNVERIFIED]`).
- **The espionage as fact** — it is a relayed allegation with two on-tape denials.
- **Keith Alexander's "greatest heist"** as an accurate quote of a named person (the speaker hedges it, §7-C).
- **Any exact wording as verbatim** — the artifact is a **model-read**; quotes are faithful-in-substance only.
- **The `World Service` attribution** in the brief — **not on the tape**; the channel is **BBC News**.

**Cross-references:** none (new id; no sibling).

---

## 11. Filing receipt

- **Transcript written:** `YT_TRANSCRIPTS/RiMjEiqpuB0_nvidia_scandal_global_story_2026-11-14.txt` (32,917 chars); **no `_timestamped.txt`** (rung 0 emits no cues — declared).
- **Drop filed:** `drops/nvidia_scandal_global_story_RiMjEiqpuB0_2026-11-14.md` (this file).
- **Index entry:** appended to `CANON_INDEX.md` in the same pass; index backed up to `CANON_INDEX.md.bak-20261114-RiMjEiqpuB0` **before editing**.
- **Dedupe:** id + title-phrase swept **before the pull, before the write, and after** — **0 collisions.**
- **Lint:** `canon_drop_lint.py` run before indexing (see filing note).
- **Local only** — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send; **one transcript written, one drop filed, one index row appended, no pre-existing Canon artifact modified.**
