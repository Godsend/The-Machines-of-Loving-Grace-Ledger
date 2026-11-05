---
epistemic-registers: EST=established HYP=hypothesis A=argument/analogy C=conjecture POETIC=myth/poetic RIFF=speculative-riff
rule: only these six tags are epistemic registers; bracket strings like [CRITICAL DIVERGENCE] / [DIVERGENCE] / [CONVERGENT] / [INTERPOLATION] / [CONTRADICTED] are row-status flags, not registers; no tag = treat as MYTH (do not build on it)
id: yuu5zblc9mI_calhoun_locke_justly_overthrow_2026-11-01
yt-id: yuu5zblc9mI
title: "Calhoun School of Law — 'How to Justly Overthrow a Government.' (read-aloud + commentary on Locke, Second Treatise ch. XIX 'Of the Dissolution of Government')"
source: Calhoun School of Law (YouTube), single lecturer ("Caleb" on tape [20:30]) reading Locke's Second Treatise ch. XIX aloud with interleaved commentary. Locke text = PRIMARY (verified against Project Gutenberg #7370); commentary = the lecturer's own advocacy.
date: 2026-11-01
upload_date: 2026-10-30
duration_s: 4334
playlist: ClawHoarde Unlisted (PLEdjghN10u14)
transcript: /data/SecondBrain/Canon/YT_TRANSCRIPTS/yuu5zblc9mI_calhoun_locke_justly_overthrow_2026-11-01.txt
primary-register: "[A] — Locke ch. XIX is a 1689 normative argument; the lecture is advocacy layered on it. Citation-level checks are [EST]; the lecturer's legal/political extrapolations are [A] at best and several are [CONTRADICTED] by the primary he is reading."
tags: [Locke, second-treatise, dissolution-of-government, right-of-resistance, social-contract, Barclay, appeal-to-heaven, qualified-immunity, nullification, Kentucky-resolutions, Praus, friction-test, cdp-rail-3]
---

# Canon Drop — Calhoun School of Law, "How to Justly Overthrow a Government."

**Date:** 2026-11-01 · **Filed by:** Dion (ClawHorde Backend) · **Intake:** monitor-triggered, ClawHoarde Unlisted playlist
**Source (VERIFIED):** `https://www.youtube.com/watch?v=yuu5zblc9mI` — channel **Calhoun School of Law** (`@CalhounSchoolofLaw`, oembed), uploaded **2026-10-30**, **4334 s (1:12:14)** (`yt-dlp --print`). Title matches the playlist mirror line exactly.
**Transcript:** `YT_TRANSCRIPTS/yuu5zblc9mI_calhoun_locke_justly_overthrow_2026-11-01.txt` (73,122 B, 684 cues).
**Primary register: `[A]`.** The video is the final installment of the channel's series on Locke's *Two Treatises* (*"the last installment for our series on John Lock's two treatises of government"* [0:11]). It is **not** a how-to; the title is Locke ch. XIX's thesis compressed into clickbait.

---

## §1 Rail report and dedupe

| Rung | Rail | Result |
| :--- | :--- | :--- |
| 1 | `youtube-transcript-api` `.list()` / `.fetch()` | `.list()` = 16 tracks, **all `is_generated=True`** (no manual caption); `.fetch` = **`IpBlocked`** |
| 2 | `yt-dlp --write-auto-subs --sub-langs 'en.*'` | **HTTP 429** on `en` |
| 3 | **CDP `:9333` transcript panel** (fresh tab; `videoDetails.videoId` polled = `yuu5zblc9mI` before reading) | **WON.** Legacy `ytd-transcript-segment-renderer` = 684, modern `transcript-segment-view-model` = 0; deduped on timestamp: 684 → 684 (no nesting duplication this pass) |
| 4 | `faster-whisper small.en` on format `139-15` (the **original en-US** track; `-0…-14` are dubs) | launched as insurance, **killed** when rung 3 landed; audio deleted |

**Coverage:** `[0:05] → [1:11:58]` of 4334 s (~99.6 % span), **0 gaps > 60 s**. Caption track is ASR: Locke is rendered "Lock"/"Loach"/"Lo", Barclay as "Barlay", and the two long Latin passages (§233, §237 — [44:58]–[49:20], [55:07]–[1:01:11]) are **phonetic garbage**. Those spans are not quotable from this transcript; the English translations that follow them are.

**Dedupe:** id `yuu5zblc9mI` = **0 hits** across `Canon/` (drops, YT_TRANSCRIPTS, index) before filing. Title/topic sweep for `overthrow|justly|locke|calhoun|treatise|dissolution` = 0 relevant hits in drops/ and YT_TRANSCRIPTS/. The three `*governance*` drop filenames (Amodei, Rea, Wright) are AI-governance sources, not this content. **NEW source; first Calhoun School of Law and first Locke primary in canon.**

---

## §2 What the video actually is

About 60 % of the runtime is a near-verbatim read of Locke §§211–243. The rest is the lecturer's commentary, which **is not delimited from the reading on tape**. That is the main hazard for anyone citing this video: the voice does not change between Locke and the commentary, and in at least one place the commentary lands *inside* a Locke sentence (§4, V1). Every claim below is filed separately as "Locke said" (checked against Gutenberg #7370) or "lecturer said" (checked against the transcript).

---

## §3 Register-tagged claim inventory

### 3a. Locke ch. XIX as read — checked against the primary

| # | Claim (Locke) | Tape | Primary check | Register |
| :--- | :--- | :--- | :--- | :--- |
| L1 | Society and government dissolve separately: conquest dissolves society, while government also dissolves "from within" when the legislative is altered | [0:11]–[3:44] | §211–212, matches | `[EST]` (text) |
| L2 | The legislative is the society's *"umperage, which they have provided in their legislative for the ending all differences"* | [3:51] | §212 "umpirage" (ASR "umperage") | `[EST]` (text) |
| L3 | Laws made by those the people have not appointed are not binding: *"they make laws without authority which the people are not therefore bound to obey"* | [6:16] | §212, verbatim | `[EST]` (text) / `[A]` (claim) |
| L4 | *"For it is not names that constitute governments, but the use and exercise of those powers that were intended to accompany them"* | [10:17] | §215, verbatim | `[EST]` (text) |
| L5 | The executive, *"often persuading himself or being flattered by others that as supreme magistrate he is incapable of control"*, is best placed to subvert | [11:46] | §218 ("uncapable of controul") | `[EST]` (text) / `[A]` |
| L6 | Executive neglect, where laws "can no longer be put in execution", dissolves government; the people become "a confused multitude" | [12:53]–[15:08] | §219, matches | `[EST]` (text) |
| L7 | Pre-emption: *"they have not only a right to get out of it but to prevent it"* | [16:57]–[17:03] | §220, verbatim | `[EST]` (text) / `[A]` |
| L8 | The reason men enter society is the preservation of property; a legislature that invades it puts itself in a state of war with the people, who are then *"absolved from any further obedience"* | [19:21]–[20:24] | §222, matches | `[EST]` (text) / `[A]` |
| L9 | Inertia: *"People are not so easily got out of their old forms as some are apt to suggest."* | [26:42] | §223, verbatim | `[EST]` (text) / `[HYP]` (empirical claim) |
| L10 | Threshold: *"Great mistakes in the ruling part, many wrong and inconvenient laws and all the slips of human frailty will be borne by the people without mutiny or murmur."* Only *"a long train of abuses"* triggers revolution | [29:12]–[29:24] | §225, verbatim | `[EST]` (text) / `[HYP]` |
| L11 | The right of resistance *"is the best fence against rebellion and the probable means to hinder it"* | [30:08] | §226 ("probablest", ASR "probable") | `[EST]` (text) / `[A]` |
| L12 | Rebellion is *"an opposition not to persons but authority which is founded only in the constitutions and laws of the government"*, so usurping rulers are the rebels (*rebellare*) | [30:13]–[30:53] | §226, verbatim | `[EST]` (text) / `[A]` |
| L13 | Individual grievance does not move the body: *"The examples of particular injustice or oppression of here and there are an unfortunate man moves them not."* Universal *"persuasion grounded upon manifest evidence"* does | [39:26]–[39:43] | §230, verbatim (ASR "are an" = "an") | `[EST]` (text) / `[HYP]` |
| L14 | Barclay (pro-monarchy) concedes the people may resist a tyrant, but only with "reverence" and without retribution | [49:25]–[51:28] | §233, *contra Monarchom.* bk. iii c. 8 | `[EST]` (text) |
| L15 | Locke's reply: *"how to strike with reverence will need some skill to make intelligible"*; *"He therefore who may resist must all must be allowed to strike."* | [51:53], [52:52] | §235, verbatim (ASR "must all must" = "must") | `[EST]` (text) / `[A]` |
| L16 | The state of war *"levels the parties cancels all form a relation of reverence, respect, and superiority"*, and the prevailing defender may punish | [54:31]–[54:48] | §235 ("all former relation", ASR "form a") | `[EST]` (text) / `[A]` |
| L17 | *"To this I reply, the people shall be judged."* | [1:06:39] | §240 "The people shall be judge" (ASR adds "-d") | `[EST]` (text) |
| L18 | Where there is no earthly judge, *"the appeal then lies nowhere but to heaven"* and *"in that state the injured party must judge for himself"* | [1:09:36]–[1:09:53] | §242, verbatim | `[EST]` (text) / `[A]` |
| L19 | *"the legislative can never revert to the people whilst that government lasts."* It reverts only on forfeiture or at the end of a set term | [1:10:23]–[1:11:00] | §243, verbatim | `[EST]` (text) |

### 3b. The lecturer's own claims — checked against external primaries

| # | Claim (lecturer) | Tape | Check | Register / status |
| :--- | :--- | :--- | :--- | :--- |
| C1 | Delegates to Philadelphia 1787 were authorised only to amend the Articles | [5:01]–[5:22] | **CONFIRMED in part.** Congress resolution of 21 Feb 1787: «for the sole and express purpose of revising the Articles of Confederation» (Avalon `const04`). Art. XIII required alterations to be «confirmed by the legislatures of every State» (Avalon `artconf`) | `[EST]` (mandate scope) |
| C2 | …so the Constitution is null and void *"because it wasn't passed the and it wasn't ratified. that it wasn't consented to."* | [5:28]–[5:35] | **FALSE as fact.** It was ratified by state conventions under its own Art. VII. The procedural irregularity (Art. VII bypassing Art. XIII unanimity) is real; "wasn't ratified" is not | `[CONTRADICTED]`; the irregularity argument is `[A]` |
| C3 | Locke §212's "without authority… not bound to obey" was *"almost copy pasted into… the Kentucky and Virginia resolutions of 1798"* | [6:16]–[6:23] | **PARTIAL.** KY Res. 1798 (Founders Online): «its acts are unauthoritative, void, and of no force». Same idea, different wording; "verbatim" [6:35] is overstated | `[EST]` (affinity) / overclaim on "verbatim" |
| C4 | Declaration of Independence borrows "long train of abuses" from Locke | [29:24] | **CONFIRMED.** Archives transcript: «But when a long train of abuses and usurpations…». Its preceding clause, «mankind are more disposed to suffer», also tracks §230 | `[EST]` |
| C5 | Executive neglect = *"a doctrine called anarcho tyranny"*, *"as is explained in Mchaveli's the prince. I can't remember the exact chapter."* | [13:13]–[13:25] | **MISATTRIBUTED.** "Anarcho-tyranny" is Samuel Francis's 1990s coinage (secondary sources disagree on 1993 vs 1994). Not a Machiavelli term; no *Prince* chapter cited. Locke §219 describes neglect, not the deliberate disarm-then-abandon strategy the lecturer narrates at [13:32]–[14:49] | `[RIFF]` (the narrative) / misattribution |
| C6 | *"Qualified immunity is not something existing in western governance."* / *"There is no such thing as qualified immunity."* | [42:32], [43:34] | **FALSE as positive law.** US Supreme Court created it in *Pierson v. Ray* (1967); the modern test is from *Harlow v. Fitzgerald* (1982) (CRS LSB10492). As a **normative** reading of Locke §231 ("magistrates doing the same thing may be resisted") it is defensible | `[CONTRADICTED]` (descriptive) / `[A]` (normative) |
| C7 | *"The final judge on what is what isn't constitutional is the people."* *"Article six in no way, like was attempted in Marberry versus Madison…"* | [1:06:46]–[1:06:53] | Locke §240 does say the people shall be judge. Mapping that onto US judicial review is the lecturer's `[A]`. Marbury's reasoning is not "argued from Article VI" alone. **Not verified this pass**, so carried as opinion | `[A]` (unverified framing) |
| C8 | Contra proferentem (*"a long-standing Latin legal maxim called contraerent"*) means doubtful legislation must be read against the government | [1:08:20]–[1:09:11] | Contra proferentem is a **contract-construction** canon. Its use on statutes against the state is the lecturer's extension (the nearest real doctrine is the rule of lenity for penal statutes). Not in Locke | `[A]` / overreach |
| C9 | On income/property taxes: *"Can it go to a confiscatory extent? Absolutely not. Can it do it without the consent of the citizenry? Absolutely not."*, framed as *"That's what he says there."* | [18:57]–[19:10] | §222 speaks of invading property; Locke's actual tax rule (§140, ch. XI, **not read on tape**) requires «consent of the majority, giving it either by themselves, or their representatives». Consent **via representatives** satisfies Locke. "Confiscatory" is not in ch. XIX | `[A]`; overreads the passage |
| C10 | *"as John Lock and Aldron Sydney have made it overtly clear"* | [22:46] | ASR "Aldron Sydney" → **Algernon Sidney** (*Discourses Concerning Government*). Sidney is not cited in Locke ch. XIX; this is the lecturer's pairing. Not checked further | `[EST]` (name repair only) |

---

## §4 Verification gate — what failed

- **V1 [INTERPOLATION] (the critical one):** *"Chaos, also called multiculturalism,"* [15:08] is spoken **inside** Locke §219, between "the people become a confused multitude without order or connection" and "where there is no longer the administration of justice". The string `multicultur` appears **0 times** in the Locke primary. It is the lecturer's editorial gloss, delivered in the reading voice with no break. **Anyone quoting this video as "Locke says" will fabricate a Locke quote.** This is the CA46 hazard in its purest form.
- **V2:** "verbatim" (C3) and "copy paste" [2:21], [27:46] overclaim textual identity. The resemblance is conceptual.
- **V3:** C2 and C6 are factually false as stated (see §3b).
- **V4:** The "resist the first encroachments" line, credited to *"the founders"* [17:33], is **unsourced**. Possibly Madison, *Memorial and Remonstrance* (1785), "take alarm at the first experiment on our liberties", but **not verified this pass and not asserted**.
- **V5:** The Latin blocks ([44:58]–[49:20], [55:07]–[1:01:11]) cannot be quoted from this transcript. The citations "chapter 3 or volume 3 section 8" [49:20] and "volume 1, chapter 3 or section 3, chapter 16" [1:01:17] are the lecturer's guesses. **Primary:** «Barclay contra Monarchom. 1. iii. c. 8» (§233) and «Barclay contra Monarchom. 1. iii. c. 16» (§237), as printed in Gutenberg #7370 ("1." there is almost certainly an OCR/typesetting rendering of "l." = *liber*, book III).
- **Quote gate:** every *"…"* span in this drop was mechanically checked against the saved transcript. Every «…» span was checked against Gutenberg #7370 or the named external primary. Results are in §8.

---

## §5 EILT mapping — Friction Rule applied

EILT = (Wolfram ⊗ Levin ⊗ Friston) ⊕ Constructor Theory ⊕ Game Theory. All cells are `[A]` (ours) unless marked.

| # | EILT component | Locke ch. XIX (primary) | Mapping | Status |
| :--- | :--- | :--- | :--- | :--- |
| R1 | **Game Theory / Social Contract (Lex Ledger)** — defection is dominant in finite games without reputational consequence | §218: the executive with "force, treasury and offices", flattered that he is *"incapable of control"*, has the largest defection incentive. §226: the standing right of resistance *"is the best fence against rebellion"* | Locke's resistance right is a **credible punishment strategy** that turns a one-shot game (ruler defects with impunity) into a repeated one (defection forfeits the office). Same structure as the Lex Ledger: you cannot make defection non-dominant by exhortation, only by attaching a cost that survives the round | `[A]` **[CONVERGENT]** |
| R2 | **Alignment as structural grounding in a non-rolling ledger, not behavioral muzzling** | §212 / §215: authority comes from **appointment**, not from obedience or title (*"it is not names that constitute governments"*). Acts outside the appointment are void. §243: the grant is fixed, and the legislative *"can never revert to the people whilst that government lasts"* | Locke checks legitimacy **against the committed founding record**, not against how compliant the governed currently are. That is the house's alignment doctrine, 300 years early: check against the commit, not the mood | `[A]` **[CONVERGENT]** |
| R3 | **Praüs** — power harnessed under restraint; restraint persists under provocation | §§233–235: **Barclay's** position (resist only with reverence, shield and no sword, never punish the superior) is the restraint-shaped one. **Locke ridicules it**: *"how to strike with reverence will need some skill to make intelligible"*; *"He therefore who may resist must all must be allowed to strike."* Once the state of war begins it *"cancels all form a relation of reverence"*, and the victor may **punish** | **The source and the analogy explicitly disagree.** Praüs says power is legitimate *because* it holds back. Locke says that once force is used without right, holding back is "imaginary resistance" that only "draw[s] on himself the worse usage". Locke has **no restraint term after the trigger**: the state of war levels everything and authorises retribution. The house's Praüs sits on **Barclay's** side of the 1689 argument, the side Locke spends three sections demolishing. EILT cannot claim Locke for Praüs. At best Praüs governs the *ruler's* conduct before the trigger (§218's flattered prince is the anti-Praüs figure); it does not govern the *resister's* conduct after | **[CRITICAL DIVERGENCE]** |
| R4 | **Ledger as provenance-not-truth; CA46/CA75 (self-attestation is not verification)** | §240–242: who judges breach of trust? *"the people shall be judged"* [sic]. With no earthly judge, *"the appeal then lies nowhere but to heaven"* and *"the injured party must judge for himself"* | Locke's terminal adjudicator is **self-judgment backed by force**. The house's verification standard forbids exactly that: a claim certified by its own claimant, with no external check, counts as unverified. Locke's system bottoms out where the house refuses to bottom out. The ledger records who did what. It does not, and by design cannot, issue the verdict "this government has forfeited" that Locke's whole chapter needs. The house cannot supply Locke's judge, and Locke's judge fails the house's audit standard | **[CRITICAL DIVERGENCE]** |
| R5 | **Friston / FEP** — inference under accumulating evidence; action when prediction error crosses a precision-weighted threshold | §225: a "long train", all tending the same way, makes the design visible. §230: *"persuasion grounded upon manifest evidence"* vs. *"particular injustice… moves them not"* | Locke's trigger is evidence accumulation to a threshold. Single errors are discounted as noise (*"slips of human frailty"*); a consistent trend is treated as signal. Clean structural rhyme. **Limit:** Locke's threshold is uncalibrated ("manifest evidence", "strong suspicions"), with no precision term | `[A]` **[CONVERGENT]** with caveat |
| R6 | **Levin — scale of agency / cognitive light cones** | §230: the collective acts only when the grievance spans "the greater part". §243: individual power, once given, «can never revert to the individuals again, as long as the society lasts» (primary wording; tape [1:10:04] lacks the comma) | The collective agent is real and its trigger is set at collective scale, as Levin would expect. **But** Locke makes the transfer **one-way while the whole exists**: parts keep no sovereign competence until the whole dissolves. Levin's multiscale agents keep part-level agency inside the whole. Locke's polity is closer to a hard **phase transition** (whole or nothing) than to nested light cones | `[A]` **[DIVERGENCE]** |
| R7 | **Agency as bounded thermodynamic work** | §223: *"People are not so easily got out of their old forms"*. Lecturer: *"it's almost as difficult to form a new government as it is to throw the current tyrannical government,"* [27:52] | Revolution has an activation energy, and inertia is the stabiliser Locke uses to answer the "ferment for frequent rebellion" objection. Our gloss, not Locke's frame | `[RIFF]` **[CONVERGENT]** |
| R8 | **Constructor Theory — negative constraints** | §222: *"since it can never be supposed to be the will of the society that the legislative should have a power to destroy that which everyone designs to secure"*. §217: delivery to a foreign power dissolves the government | Legitimate authority is defined by tasks it **cannot** perform (destroy property, alienate the polity, become arbitrary). A transformation outside the allowed set is not a bad act *of* government; it is **not government at all**. Strong rhyme with "impossible tasks" framing | `[A]` **[CONVERGENT]** |
| R9 | **Friction Rule / genuine divergence** (meta-row) — lecturer vs. his own primary | §225 (read on tape [29:12]): wrong laws and frailties *"will be borne by the people without mutiny or murmur"*. Lecturer, seven minutes earlier: *"Do you compromise on principles? Do you trade any ounce of freedom for safety? Absolutely not. Not one bit."* [21:48]; *"complying even one inch with tyrannical acts is not Christian."* [22:58] | The lecturer collapses Locke's **collective, evidence-threshold, long-train** trigger into a **per-act, individual, zero-tolerance** trigger. That is the exact move Locke rebuts in §§223–230. The video argues against the text it is reading | **[CRITICAL DIVERGENCE]** (source vs. presenter) |

**Friction count:** 3 `[CRITICAL DIVERGENCE]` (R3, R4, R9) + 1 `[DIVERGENCE]` (R6) + 5 `[CONVERGENT]`. The table is not decoration. **Load-bearing friction: R3** (Praüs is Barclay's position, not Locke's) and **R4** (Locke's judge is the self-attestation the house rejects).

**Forbidden mappings (do not write):**
- "Locke endorses Praüs." R3 shows the opposite.
- "The ledger is Locke's umpire." The ledger records; Locke's umpire decides. See R4.
- "Locke says chaos is multiculturalism." V1: interpolation, not in the primary.
- "Lockean resistance = zero-tolerance non-compliance." R9: the primary says the opposite.

---

## §6 Strongest point / weakest joint

**★ STRONGEST (Locke, not the lecturer):** §226's inversion, *"rebellion being an opposition not to persons but authority which is founded only in the constitutions and laws of the government"* [30:13], together with §212's *"they make laws without authority which the people are not therefore bound to obey"* [6:16]. Legitimacy is defined by the **committed charter**, not by who holds force. The usurping ruler is therefore the rebel. This is R1 + R2 + R8 in one stroke, and it is the cleanest pre-modern statement of "authority = fidelity to the commit" the house has on file. Primary-verified verbatim.

**★ WEAKEST JOINT (two layers):**
1. **Presenter layer:** R9. The lecturer's zero-tolerance, per-act, individual-nullification reading (*"you have every right to nullify and render void any act that is not compliant"* [22:01]) is contradicted by §225 and §230, which he reads aloud himself. Add V1's undelimited *"multiculturalism"* interpolation and the false descriptive claims (C2, C6), and the commentary layer is not citable.
2. **Source layer:** Locke's own unresolved joint is R4. "Who shall be judge?" ends in *"the injured party must judge for himself"* plus an appeal to heaven. That is not an answer; it is a statement that the question gets settled by force. It is also why the lecture can turn "the people shall be judge" into "every individual may nullify". Locke's text has no mechanism to stop that slide except the empirical bet on inertia (§223, `[HYP]`).

---

## §7 Falsifiers

- **F-YUU-1:** If a Locke edition containing "multicultur" or any equivalent in §219 turns up, V1 is withdrawn. (Gutenberg #7370 = 0 hits.)
- **F-YUU-2:** If the house can name a **non-self-attesting** adjudicator for "breach of trust" that the ledger can record without issuing a verdict, R4 is downgraded from CRITICAL.
- **F-YUU-3:** If Praüs is restated to bind only the power-holder before the trigger (and explicitly not the resister after it), R3 becomes a `[DIVERGENCE]` scope note rather than a critical cut.
- **F-YUU-4:** C7 (Marbury / Art. VI) stays at `[A]` until the opinion text is read. Do not upgrade from this video.

---

## §8 Gate results

- **QUOTE GATE (transcript): PASSED, 62/62.** Every *"…"* span was checked mechanically against the saved transcript (whitespace/case-normalised, ellipsis-split). One first-pass failure, a §243 span whose punctuation came from the primary rather than the tape, was moved to «…» primary-quote form. **0 fabricated transcript quotes.**
- **QUOTE GATE (primary): PASSED.** Every «…» span was checked against Gutenberg #7370 (Locke ch. XI §140 and ch. XIX), Avalon `const04` / `artconf` (1787 resolution; Articles XIII), Founders Online `01-30-02-0370-0004` (KY Res.), or the Archives Declaration transcript. The Barclay citation was corrected from "l." to the printed "1." after the first pass.
- **TAG GATE:** registers used are only `[EST]/[HYP]/[A]/[C]/[POETIC]/[RIFF]`. `[C]` and `[POETIC]` are declared but unused: nothing here is conjecture, and the only rhetoric (*"the emperor not only isn't wearing clothes"* [39:07]) is not filed as a claim.
- **ASR repairs (flagged, not silently corrected):** Lock/Loach/Lo → Locke; Barlay → Barclay; umperage → umpirage; Mchaveli → Machiavelli; Aldron Sydney → Algernon Sidney; Marberry → Marbury; contraerent → contra proferentem; Cowing School → Calhoun School; Jeff the → Jeptha (Gutenberg's §241 spelling; "Jephtha" in §21); Polithamus/Polyphimus → Polyphemus; revelantes → rebellantes; "Scotch panels" → Scotch Annals (§238).

---

## Verdict — `[A]`

The **Locke** inside this video is worth having in canon: it is the primary statement that authority is fidelity to a committed charter, and that the defector is whoever breaks the charter, crown included. R1, R2 and R8 are real convergences. **The lecture is not citable.** It inserts its own politics into Locke's sentences without a seam (V1), states two false legal facts (C2, C6), and argues the zero-tolerance position Locke explicitly refutes in the passage being read (R9). For EILT, the useful result is the friction. **Locke does not back Praüs (R3); he sides against it.** And his last-resort judge is the self-attestation the house's own verification rules reject (R4). Cite Locke §§212, 215, 222, 225, 226 and 243 from the primary. Cite the video only as the place the house found them.

Local only: no GitHub push, no NotebookLM, no Drive mirror, no TTS. One transcript written, one drop filed, one index entry appended, no pre-existing Canon artifact modified.
