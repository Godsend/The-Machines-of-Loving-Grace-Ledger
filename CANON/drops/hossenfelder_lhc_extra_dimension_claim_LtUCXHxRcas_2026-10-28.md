---
epistemic-registers: EST=established/verified fact · HYP=testable hypothesis with a stated falsifier · A=grounded cross-domain analogy · C=conjecture/unsupported forecast · POETIC=metaphor/narrative · RIFF=improvised aside, no claim
rule: no tag = treat as unverified, do not build on it. Row-status flags [CONTRADICTED] / [ATTACK SURFACE] / [ABSENT] / [DIVERGENCE] / [CRITICAL DIVERGENCE] / UNVERIFIED are NOT registers — every row still carries one of the six tags.
canonical-7 equivalence: EST→[EST-FACT]/[EST-THEORY] · HYP→[FALSIFIABLE-JOINT]/[EST-ANALOG] · A→[EST-ANALOG] · C→[C] (conjecture/opinion, single-letter set) · POETIC→[POETIC] · RIFF→operator-adjacent aside, same class as house [O]
source: Sabine Hossenfelder — "Large Hadron Collider Sees Extra Dimension, Physicists Claim" (Science without the gobbledygook)
date: 2026-10-28
tags: [particle-physics, LHC, CMS, extra-dimensions, randall-sundrum, kaluza-klein, necessity, register-inflation, provenance-not-truth, science-communication, collider-funding]
canon-id: CANON-2026-10-28-HOSSENFELDER-LHC-EXTRADIM
---

# Canon Drop — Sabine Hossenfelder: "Large Hadron Collider Sees Extra Dimension, Physicists Claim"

### A 6:39 news video arguing a real CMS four-jet excess is being over-interpreted as evidence for extra dimensions. **Her verdict is not in either title**: she rates the extra-dimension reading *"9 out of 10 on the bullshit meter"* and files the episode as a case study in a hypothesis chosen to fit data rather than required by it.

**Source (VERIFIED via `yt-dlp --print` in *this* session):** https://www.youtube.com/watch?v=LtUCXHxRcas · channel **Sabine Hossenfelder** (`UC1yNl2E66ZzKApQdRuTQ4tw`) · uploaded **2026-10-28** · **399 s (6:39)** · **69,199 views at brief pull** (69,222 at the yt-dlp re-check, 2026-10-28).
**Retitle note (one id, two titles):** the ClawHoarde-playlist label read *"Unexpected: Fifth Dimension Explains Weird LHC Data, Physicists Claim"*; YouTube retitled the **same** video id in place to the current title above. Metadata (id/channel/duration/upload date) is identical across both — this is one upload, not two.
**Transcript:** `Canon/YT_TRANSCRIPTS/LtUCXHxRcas_Hossenfelder_LHC_ExtraDimension_2026-10-28.txt` (7,886 B) + `…_timestamped.txt` (8,355 B). Coverage **0:00 → 6:27 of 6:39**.
**Paper under discussion (in the video's own description):** https://doi.org/10.48550/arXiv.2610.31458 — **arXiv:2610.31458** (hep-ph), *"Evidence for Kaluza-Klein excitations of the graviton, gluon and quark at LHC"*, **Alain Le Yaouanc & François Richard**, v1 **2026-10-22**, v2 **2026-10-27**, 10 pp., *"Contribution to the European strategy for future accelerators."*
**Pull rail (STOPPED AT FIRST SUCCESS — rung 1):** `youtube-transcript-api` on **system python3** (`import youtube_transcript_api` works on this host) **SUCCEEDED ON THE FIRST TRY**. `.list('LtUCXHxRcas')` returned an **en-GB MANUAL track (`is_generated=False`)** plus fr/de/it/pt/es MANUAL and one **en AUTO** track; `.fetch()` on the MANUAL en-GB returned **71 segments** with **no `IpBlocked`, no 429**. Rung 0 (published transcript) **checked and absent for a free transcript** — the description links only a **paywalled Patreon** transcript, no free written transcript. Rungs 2 (`yt-dlp --write-auto-subs`), 3 (CDP :9333) and 4 (ASR) **not exercised**. The MANUAL track is the higher-quality source (human-authored captions); the auto `en` track (162 segments) was fetched to scratch only as a cross-check and is not the file of record.
**ASR note:** the file of record is a *manual* caption track, so it carries **no ASR name-errors** of the class seen in auto-caption pulls. Names/dates/numbers below were nonetheless re-verified against primaries (§2). The **sponsor read (Coveron, 05:15→06:27)** is retained in the transcript and excluded from the analysis.
**Status:** working drop (pre-adversarial review). Canonical only after a cross-node pass and Gene's sign-off.
**Filing scope:** **local only** — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound message. Exactly one entry appended to `CANON_INDEX.md`; no pre-existing canon artifact modified.

---

## 0. Title-vs-content audit (programmatic term counts over the spoken body)

Two titles exist for one upload. Term counts over the whitespace-normalized transcript (1,068 words), word-boundary, case-insensitive:

| Term | Count | Reading |
| :--- | :--- | :--- |
| `fifth` | **0** | the playlist title's own hook word is **never spoken** |
| `unexpected` | **0** | playlist-title hook, never spoken |
| `weird` | **0** | playlist-title hook, never spoken |
| `extra dimension` + `extra dimensions` | 4 + 4 = **8** | the actual subject |
| `bullshit` | **2** | her verdict's own word (`9 out of 10 on the bullshit meter`; `all this extra dimensional stuff is bullshit`) |
| `collider` | **5** (`bigger collider` **1**) | the funding-subtext word |
| `necessary` | **1** | the load-bearing methodological word |
| `graviton(s)` | **1** | the prior-claim word (§1 C7) |
| `toponium` | **0** | she describes the top+antitop composite in plain language, never names "toponium" |
| `Randall-Sundrum` | **2** | the model actually named |
| `5σ` | **1** | her threshold reference |
| `global` / `local` | **0 / 0** | **[ABSENT]** — see §1 C3 |
| `claim` / `evidence` | 2 / 5 | |

**[EST] Verdict:** both titles **underclaim** the video by omitting its payload — **neither title carries her verdict**, which is the single most quotable line in it. The **playlist** title additionally **overclaims** with three hooks the video never speaks (*fifth dimension*, *unexpected*, *weird*). The **current YouTube** title is *attribution-faithful* — *"Physicists Claim"* matches her own opening line *"A team of physicists claim they have found evidence…"* — and it correctly reads as reporting-a-claim, **not** endorsing one; but it crops the *"9 out of 10"* rejection that is the video's whole point. So: the packaging neither invents data nor misstates the claim; it simply sells the *claim* and hides the *verdict*.

---

## 1. Claim inventory (register-tagged, timestamped)

Quotes are literal from `_timestamped.txt`, each carrying its `[MM:SS]` head. All 37 quoted strings were re-verified literally present (whitespace-normalized) before filing — **0 misses**.

### C1. The paper and its interpretation [EST]
[00:14] *"The new paper comes from two physicists in France and is an analysis of data collected"* … *"at CMS"*; [02:12] *"These physicists now say that the Large Hadron Collider has seen heavy versions"* … *"of gluons with masses of about 3.6 and 8.6 teraelectronvolts."* … *"These decay into heavier versions of quarks. And these then decay into these jets."*
→ **Confirmed against the primary (§2 V1–V2):** arXiv:2610.31458 abstracts *"two heavy KK gluons gkk(3.6TeV) and gkk(8.6TeV) into pairs of KK quarks qkk(1TeV) and qkk(2.1TeV)"* at CMS. Hossenfelder's plain-language rendering is **faithful**.

### C2. The data: CMS Run 2, the two four-jet events [EST]
[02:29] *"They have found evidence for this in data collected by CMS between 2016 and 2018."* … [02:33] *"In that run, CMS saw two particularly interesting events."* … *"Each produced four jets with a very high combined mass."*
→ **Confirmed (§2 V3):** CERN's own write-up describes exactly two events — a 2017 four-jet event (4-jet mass 8 TeV, dijets 1.9 TeV) and a second (4-jet mass 8.6 TeV, dijets 2.15 TeV) — in data *"collected up to the end of LHC Run 2"*. "Between 2016 and 2018" is Run 2's high-luminosity span.

### C3. The significance — and the number she leaves out [EST] + [ABSENT]
[02:45] *"They say that, depending on how you look at it,"* [02:51] *"they stand out at 3.6 to 4σ."* … *"So that falls short of the 5σ discovery threshold, but it is more than"* *"just a little odd."*
→ **Confirmed and contextualized (§2 V4–V5):** the paper reports *"The most significant indication claimed by CMS, 3.6 s.d. local"* and *"Both reach a local significance close to 4 s.d."* — **local** significance exactly. **[ABSENT]** Hossenfelder reports the *local* number and the 5σ bar, but **never mentions the global significance** (the word `global` = **0** hits). CERN's own public write-up gives it: *"…corresponding to a local significance of 3.9σ.…For the two events the global significance is only 1.6σ."* This is the honest-skeptic's own standard (a local excess anywhere in a large search region is expected), and it is **the one deflationary number the video omits**. The omission does not change her verdict (she rejects the *story*, not the *events*) but it is a real gap in an otherwise rigorous segment.

### C4. The model is Randall-Sundrum, chosen because it fits [EST]
[03:04] *"Their analysis is quite interesting because it is not just any sort of extra dimension they"* *"find. They find evidence for what is specifically called the Randall-Sundrum scenario."* … [03:15] *"In this case there is only one extra dimension, and it has a cosmological constant."* … [03:20] *"scenario the masses of the particles are not equally spaced, and that fits the data best."*
→ **Confirmed (§2 V6):** the paper *"we interpret the massive 4 jet excesses observed by CMS"* within *"the RS model"*, with *"The mass ratios need not be equal."* Her *"only one extra dimension"* and *"not equally spaced"* match RS (a single **warped** extra dimension, geometric KK tower). **[UNVERIFIED, minor]** her *"it has a cosmological constant"* gloss was **not** separately source-checked this session; treat as her simplification, not a quoted primary claim.

### C5. Problem 1 — Run 3 already saw no further events [EST]
[03:27] *"First, the CMS Run 3 data is already out and they"* [03:32] *"have seen no further of these jets."*
→ **Confirmed against the primary (§2 V7):** the paper concedes, verbatim, *"A partial analysis of RUN3 data did not bring additional 'gold plated' events"* and again in the Conclusion: *"Admittedly the partial analysis of RUN3 by CMS and results from ATLAS on RUN2 did not bring additional 'gold plated' four jet events."* **This is the strongest single check in the video** — her first objection is the authors' own stated result.

### C6. Problem 2 — the decay channel is excluded by other data, and the authors hand-wave [EST]
[03:32] *"Second, the idea of heavy gluons decaying into heavy"* [03:38] *"quarks is contradicted by other data."* … *"The authors acknowledge this problem but basically just say,"* *"well, then the extra dimension is somehow more complicated."*
→ **Confirmed in substance (§2 V8):** the paper's abstract states *"Present limits on gkk into top pairs seem to exclude gkk(3.6TeV) but these limits assume a dominant decay into top pairs, which can be questioned"* — i.e. the collision with data is real and the authors' reply is precisely to *question the assumption* rather than to drop the model. Her *"somehow more complicated"* is a fair, if unsympathetic, paraphrase of that move.

### C7. Problem 3 — a prior "we saw gravitons" claim that was a top–antitop composite [EST]
[03:47] *"the authors claimed last year to have seen evidence for heavier versions of gravitons,"* [03:53] *"that are hypothetical particles that would carry the gravitational force. That turned"* *"out to be a composite particle of a top and an antitop quark."*
→ **Confirmed (§2 V9–V10):** the same two authors' **arXiv:2506.09490** (*"New resonances at LHC"*, submitted 11 Jun 2025 — "last year") reinterprets *"a toponium type candidate observed with high statistical significance by CMS"* as a Kaluza-Klein graviton. The CMS resonance's **mainstream** reading is a **top–antitop bound state (toponium)** — i.e. a composite of a top and an antitop — so her *"turned out to be a composite"* describes the mainstream reading displacing the authors' minority one. *(Note: "toponium" is never spoken — `toponium` = 0 hits; she says it in plain words.)* [ATTACK SURFACE] The framing *"these guys clearly are not accounting very well for standard physics in the first place"* is her **inference about the authors' competence**, drawn from one re-interpretation — an adversarial paraphrase, not itself a verified claim.

### C8. Her verdict [C]
[04:06] *"This is why, I am sorry, but I give this a 9 out of 10 on the bullshit meter."* … *"I don't doubt that"* *"these events exist or that they are odd, but I do not for a second buy the extra dimension story."*
→ **[C]** — a normative confidence scalar. Note the two-part structure: she **accepts the events** and **rejects the story**. (The scoring scale is unstated; 10 = maximally bullshit.)

### C9. Her causal explanation — the funding motive [C] + [ATTACK SURFACE]
[04:19] *"What I think is going on here instead is that particle physicists are desperately searching"* [04:24] *"for something, anything, interesting in the data that could justify building a bigger collider."*
→ **[C]** an unfalsifiable social conjecture about the field's motives, offered *"What I think is going on here instead"* = explicitly her inference, not a documented finding. **[ATTACK SURFACE]** it cuts symmetrically: the same "desperate for a justification" reading would fit anyone advancing a minority position to a large audience, and no receipt (funding document, author statement) is given that *these* authors are so motivated.

### C10. Her methodological rule — the necessity requirement [HYP]
[04:50] *"A scientific hypothesis must be necessary in the first place. You cannot just"* *"invent maths and then forever claim that one day one might be able to test it."* … [05:00] *"It's"* *"obviously a strategy that can't work, and that, as a matter of fact, does not work."*
→ **[HYP]** — a general prescription for theory-building, stated as a rule and backed by an empirical "does not work" claim that is **not** operationalized here (no named set of hypotheses tested against it). This is the video's load-bearing methodological thesis and the hinge of §3.

### C11. Colour [POETIC] / [RIFF]
[01:20] *"Fun fact: I know someone who sat at an airport working on slides about"* *"“collisions” and “jets” and nuclear physics, and was asked to please step aside into a small room for some questions."* · [05:11] *"But this, as it turns out,"* *"was excellent preparation for the academic job market."*
→ **[POETIC]** anecdote · **[RIFF]** aside. She says *"Indeed it's what I wrote my PhD thesis about"* [01:41] and *"spent years studying dimensions that don't exist"* [05:05] — the self-implication that makes the 9-not-10 honest.

---

## 2. Verification table (primary sources retrieved THIS session)

| # | Claim checked | Result | Source |
| :--- | :--- | :--- | :--- |
| V1 | Paper identity | **CONFIRMED** — arXiv:2610.31458 (hep-ph), *"Evidence for Kaluza-Klein excitations of the graviton, gluon and quark at LHC"*, v1 2026-10-22 / v2 2026-10-27 | `arxiv.org/abs/2610.31458` (web_extract) |
| V2 | "two physicists in France" | **CONFIRMED** — Le Yaouanc & Richard, *"Université Paris-Saclay, CNRS/IN2P3, IJCLab, 91405 Orsay, France"* | paper PDF (`pdftotext`, line 5) |
| V3 | Two four-jet events, Run 2 | **CONFIRMED** — 2017 event (4-jet 8 TeV / dijets 1.9 TeV) + second (4-jet 8.6 TeV / dijets 2.15 TeV), *"collected up to the end of LHC Run 2"* | `home.cern/cms-lookout-new-physics/` (web_extract) |
| V4 | "3.6 to 4σ" | **CONFIRMED** — paper: *"3.6 s.d. local"*; *"Both reach a local significance close to 4 s.d."* | paper PDF (lines 78, 208) |
| V5 | Global significance (**absent from video**) | **CONFIRMED** — *"a local significance of 3.9σ.…For the two events the global significance is only 1.6σ."* | `home.cern/…` (web_extract) |
| V6 | RS framework + non-equal mass spacing | **CONFIRMED** — *"the RS model"*, *"Follows closely the RS model"*, *"The mass ratios need not be equal."* | paper PDF (lines 313, 312, 229–208) |
| V7 | Run 3 — no further events | **CONFIRMED** — *"A partial analysis of RUN3 data did not bring additional 'gold plated' events."* | paper PDF (lines 197, 326–327) |
| V8 | gkk→top-pair limits exclude gkk(3.6) | **CONFIRMED** — *"Present limits on gkk into top pairs seem to exclude gkk(3.6TeV)…"* | paper abstract (PDF line 11) |
| V9 | Prior ("last year") graviton claim | **CONFIRMED** — arXiv:2506.09490 *"New resonances at LHC"*, Le Yaouanc & Richard, **11 Jun 2025** | arXiv listing (web_search) + paper's own ref [3] (PDF line 356) |
| V10 | "turned out to be a composite… top and an antitop" | **CONFIRMED (mainstream reading)** — the CMS candidate is a *"toponium type candidate"*; toponium = top–antitop bound state | arXiv:2506.09490 abstract (web_search) |
| V11 | LHC beam energy — she says *"several teraelectronvolts"* | **CONFIRMED** — Run 2 = 13 TeV, Run 3 = 13.6 TeV (the paper's Fig. 2 caption: *"at 13 TeV and 13.6 TeV"*) | paper PDF (line 191) |

**Not re-fetched / left UNVERIFIED:** Hossenfelder's *"cosmological constant"* gloss on RS (minor); the funding-motive conjecture (C9) — an inference by construction, no receipt exists to check; the "9 out of 10" scale's definition.

---

## 3. Critical Audit & Falsification Matrix (EILT mapping — Friction Rule applied)

The source's own domain is **claim-evaluation and the sociology of a physics result**, not EILT's cosmology. A mapping is warranted **only** where a genuine, specific correspondence exists — the necessity thesis (C10), the model-chosen-to-fit move (C4), and the observation-vs-interpretation split (C8). Rows where the source and the house genuinely disagree are marked **[CRITICAL DIVERGENCE]**; a table with none of those would be decoration, not derivation.

| # | Source claim | ClawHorde / EILT audit | Tag / flag |
| :--- | :--- | :--- | :--- |
| **R1** | *"A scientific hypothesis must be necessary in the first place."* (C10) | **The house's ledger does not — and cannot — enforce necessity.** EILT's informational ledger is a **provenance** instrument: it records *what was committed, by whom, when*, and prices the irreversible commit; the house's own **provenance-not-truth** anchor holds that a faithful record attests *that a claim was made*, never *that it is true or necessary*. A ledger would file the extra-dimension claim with **identical fidelity** whether it were necessary or invented. Her necessity gate is a **truth/selection** criterion that sits on a layer the ledger explicitly declines to occupy — so her central rule and our central instrument are **orthogonal, and disagree about what a record is for**. | `[HYP]` **[CRITICAL DIVERGENCE]** |
| **R2** | The RS model is selected because its mass spacing *"fits the data best"* (C4) | **Shared distrust, different object.** The house's Friction Rule distrusts a *mapping with zero disagreement* (confirmation bias); Hossenfelder distrusts a *model chosen to fit* (post-hoc selection). Both refuse decoration — but the house's test is aimed at **analogy construction**, hers at **model selection**; neither test catches the other's failure mode. Filed as a genuine but partial convergence. | `[A]` **[DIVERGENCE]** |
| **R3** | *"Why is it not a 10 out of 10? Because I might be wrong."* (C8) | **Scalar here, structural there.** Hossenfelder answers her own self-evaluation gap with a **private per-claim confidence scalar** (9/10). The house's **self-evaluation gap** is structural — a system cannot fully model its own evaluation, and the house answers it with an **external causal path** (a peer audit, an independent trace), not a number. Same gap named, incompatible remedies. | `[A]` **[DIVERGENCE]** |
| **R4** | *"…that could justify building a bigger collider."* (C9) | **Where she wants the commit *prevented*, the house wants it *priced and recorded*.** EILT treats the **irreversible commit** as the ontological primitive — any information-processing system commits; the ledger's job is to make the commit's cost and provenance legible, not to adjudicate its *justification*. Hossenfelder's normative lever (do not let the funding motive drive the claim) is a **justification test** — exactly the class of evaluation a provenance ledger **cannot perform** (it certifies *that* a commit happened and its *cost*, never whether it was *warranted*). The house has no instrument that would catch the pathology she names. | `[HYP]` **[CRITICAL DIVERGENCE]** |
| **R5** | *"You cannot just invent maths and then forever claim that one day one might be able to test it."* (C10) — **the charge, turned on the house** | **Her necessity rule would indict part of the house's own holdings.** The house files items as `[HYP]`/`[POETIC]` whose only test is far-future or nominally pre-registered-but-unrun, and defends them with *Falsifiers ≠ Falsification* (the house's own rule) — a possible future test suffices to keep the claim live. Hossenfelder's standard is **stronger**: a hypothesis needs a **reason to be proposed**, not merely a route to a someday-test. On her criterion, "interesting but not yet necessary" is disqualifying; on the house's, it is filable. **Genuine disagreement — filed with the house as the weaker party, because the house's own defense ("a pre-registered falsifier makes it testable") does not answer her actual objection (that such a hypothesis should not have been proposed).** | `[HYP]` **[CRITICAL DIVERGENCE]** |
| **R6** | *"I don't doubt that these events exist or that they are odd, but I do not for a second buy the extra dimension story."* (C8) | **Convergence, stated in other vocabulary.** Hossenfelder cleanly separates the **observation** (the events exist, and a faithful record of them is trustworthy) from the **interpretation** (the extra-dimension *story*, which the record does not certify). That is the house's **provenance-not-truth** anchor — a record can be faithful *and* an interpretation laid on it can be unwarranted — reached independently. Labelled **convergence, not validation**: she does not derive it from our framing, has never heard of it, and it does **not** validate any house software. | `[A]` |

**Anti-decoration guard, stated in-file:** three rows (R1, R4, R5) are `[CRITICAL DIVERGENCE]` — places where the source's requirement and the house's apparatus genuinely disagree; the table is therefore **not** all-convergent. R2/R3 are honest partial convergences, and R6 is a labelled convergence that confers **no** external validation on EILT.

---

## 4. Falsifiers (pre-registered; not run)

- **F-HL1 (necessity vs ledger — tests R1).** Take a set of physics hypotheses rated on Hossenfelder's necessity criterion and a set rated non-necessary; feed both through the house's commit/ledger pipeline. **Killed** if the ledger's recorded fidelity, cost, or provenance for the two sets is indistinguishable *by construction* — which is the prediction — because that demonstrates the ledger is necessity-blind, i.e. R1's divergence is real. *(This falsifier, if it "passes", confirms the divergence rather than the house.)*
- **F-HL2 (title-receipt test).** The video's payload is the *9/10 bullshit* verdict. **Killed** if a viewer who reads only either title can recover the verdict. Both titles omit it → the underclaim stands.
- **F-HL3 (local-vs-global — tests C3).** Run the transcript for `global|local|1.6|3.9`. **Confirmed absent** this session (`global`=0, `local`=0): the deflationary global significance is not in the video. Falsified if a future caption revision contains it.
- **F-HL4 (Run-3 objection — tests C5).** **Killed** if the paper did *not* concede no new Run-3 events — but the paper concedes it twice (V7). The check passes; the objection is the authors' own.
- **F-HL5 (motive claim — tests C9).** **Unfalsifiable as stated** — no document could confirm a field's collective motive. Filed as `[C]`/`[ATTACK SURFACE]`, self-sealing; not to be cited as a finding.

---

## 5. Verdict

**Strongest joint — [EST]** *C5: her first objection is the authors' own stated result.* She claims *"the CMS Run 3 data is already out and they have seen no further of these jets"* [03:27]; the paper itself writes *"A partial analysis of RUN3 data did not bring additional 'gold plated' events"* and repeats it in the Conclusion. The skeptic's lead objection is **not** an external hit-piece — it is quoted from the paper it attacks. Paired with C1–C4 (all primary-confirmed), the descriptive half of the video is **accurate to the source**, including the 3.6–4σ local significance, the RS framework, and the 2016–2018 Run-2 data.

**Weakest joint — [ABSENT]/[C]:** *the two things she leaves out and the one thing she asserts.* (1) **[ABSENT]** She reports the *local* significance but never the *global* one (CERN's own number: **1.6σ** vs local 3.9σ) — the single most deflationary fact in the primary, and the honest-skeptic's own standard, is missing. (2) **[C]/[ATTACK SURFACE]** Her causal explanation — that the authors are driven by *"building a bigger collider"* (C9) — is an unfalsifiable motive conjecture with no receipt, cutting symmetrically. (3) **[HYP]** Her necessity rule (C10) is the video's load-bearing thesis but is stated as a slogan with an unoperationalized *"does not work"*; the house's own §3 R5 shows the same rule would indict part of the house's holdings — the charge is real and lands on us too.

**Disposition:** **file it** — an independent source (not a re-cut; §6), carrying a clean, primary-confirmed case study in model-chosen-to-fit and a methodological thesis (necessity) that generates a genuine `[CRITICAL DIVERGENCE]` with EILT's provenance ledger. **Do not build an EILT derivation on it** — the correspondence is to the house's *epistemic posture*, not to its cosmology; per the mapping scope rule, nothing here warrants forcing an EILT cosmology mapping. No fabricated quotes, receipts, citations, or timestamps; no pre-existing canon artifact modified.

---

## 6. Dedupe / clip-vs-parent check (measured this session)

- **Id / title dedupe:** `grep -rl "LtUCXHxRcas"` over `Canon/` → **0 hits** (no existing transcript or drop). `grep -rilE "2610.31458|le yaouanc"` over `drops/` + `CANON_INDEX.md` → **0 hits**. Close-title n-gram sweep (`extra dimension|fifth dimension|hadron collider sees`) → only unrelated incidental physics files. **First filing of this claim in canon.**
- **Clip-vs-parent (4-gram containment):** my 1,087 unique 4-grams were checked against **every** `.txt` in `YT_TRANSCRIPTS/` (**330 files**, headers stripped). **Max containment = 1.38 %** (top match: `ZAzWPE9CItg_MoitraBruntonKontorovich_AICrisisMath_LexFridman…`, an unrelated AI-math interview — pure common-phrasing overlap). Closest **topical** relative: the prior Hossenfelder file `y4fN8APrV8I_Hossenfelder_14yoDarkEnergyTheory_2026-10-20.txt` at **1.20 %**. **Far below the ~50 % re-cut threshold → NOT a re-cut/re-upload; filed as a full drop.**

**Register counts (programmatic scan of the Register column, not by eye):** **§1 claim inventory = 12 rows** → `[EST]` **7** (C1–C7) · `[C]` **2** (C8, C9) · `[HYP]` **1** (C10) · `[POETIC]` **1** (C11) · `[RIFF]` **1** (C11). **§3 friction table = 6 rows** (R1–R6) → `[HYP]` **3** (R1, R4, R5) · `[A]` **3** (R2, R3, R6); status flags `[CRITICAL DIVERGENCE]` **3** (R1, R4, R5) · `[DIVERGENCE]` **2** (R2, R3) · convergence-1 (R6). **Grand total = EST 7 / HYP 4 / A 3 / C 2 / POETIC 1 / RIFF 1 = 18 register rows.** Flags across the drop: **`[CRITICAL DIVERGENCE]` 3 · `[DIVERGENCE]` 2 · `[ABSENT]` 1 · `[ATTACK SURFACE]` 2 · `[UNVERIFIED]` 1 · `[CONTRADICTED]` 0**. Pre-file tag gate: **PASSED** — every `[BRACKETED-TAG]` in the body diffed against the six-tag set; no invented register; all other bracketed tokens are the declared row-status flags. Pre-file quote gate: **PASSED** — 93 quoted fragments ≥8 chars, each re-verified literally present in the transcript / paper / CERN corpora after character-normalization; **0 misses**; the two defects the gate caught on first pass (a quoted `"the RS framework"` not in the paper, and a bracket-inserted `interpret[s]` inside quotation marks) were repaired before filing.
