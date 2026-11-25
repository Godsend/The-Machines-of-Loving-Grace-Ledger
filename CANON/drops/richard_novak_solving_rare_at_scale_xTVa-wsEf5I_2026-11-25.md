---
title: "Solving Rare at Scale — Richard Novak (CEO, Unravel Biosciences), on Michael Levin's academic channel"
date: 2026-11-25
filed_by: Dion (dion profile, Nitro)
drop_id: CANON-DROP-2026-11-25-xTVa-wsEf5I
source_type: PRIMARY (recorded lab-seminar talk + Q&A; one speaker presenting, one host questioning; not a relay, not a panel)
video_id: xTVa-wsEf5I
video_url: https://www.youtube.com/watch?v=xTVa-wsEf5I
channel: Michael Levin's Academic Content (UC3pVafx6EZqXVI2V_Efu2uw)
upload_date: 2026-11-25
duration: 2854 s (47:34)
playlist: ClawHoarde Unlisted (PLEdjghN10u14)
transcript: /data/SecondBrain/Canon/YT_TRANSCRIPTS/xTVa-wsEf5I.md
transcript_rail: RUNG 1 — youtube-transcript-api (instance API), AUTO `en` track, 1,423 cues, first probe
source_status: VERIFIED (transcript read in full this session, 147 gated spans)
tags: [richard-novak, unravel-biosciences, michael-levin, rare-disease, rna-seq, vorinostat, rett-syndrome, pitt-hopkins, n-of-1, drug-repurposing, gene-regulatory-network, computational-irreducibility, constructor-theory, fep, ledger, moloch, eilt, friction-rule]
---

# Canon Drop `[EST]` — Richard Novak, “Solving Rare at Scale” (Unravel Biosciences)

**Date:** 2026-11-25 · **Filed by:** Dion
**Source (VERIFIED):** YouTube `xTVa-wsEf5I`, *“Solving Rare at Scale” by Richard Novak* — channel **Michael Levin's Academic Content** (`UC3pVafx6EZqXVI2V_Efu2uw`), **uploaded 2026-11-25**, **2854 s (47:34)**, **64 views / 9 likes** at pull. https://www.youtube.com/watch?v=xTVa-wsEf5I
**Transcript:** `YT_TRANSCRIPTS/xTVa-wsEf5I.md` — 1,423 cues, 0.0 → 2855.9 s of 2854 s (≈100 %), **9,718 words / 53,565 chars**, 0 gaps > 60 s.

**Drop-level register: `[EST]`.** Declared once, in this header, as the whole-piece tag. **What it means here, precisely:** `[EST]` covers (a) the capture and provenance receipts re-derived this session — id, title, channel, channel_id, duration, upload date, view/like counts, track inventory, cue count, span, byte count — and (b) the **literality of every quoted span**, each of which is a verified substring of the saved file (§5, 147/147). **`[EST]` makes no claim that Unravel's results are true.** Every clinical number on this tape is sub-tagged `[C]`: the only warrant for it is the presenting CEO's own slides, delivered in a fundraising register, with no denominator, no control arm and no primary source. Sub-claim registers: `[EST]` tape-literal fact · `[HYP]` the speaker's own interpretive thesis · `[C]` the speaker's own uncited quantitative or empirical claim · `[A]` an analogy, ours or his · `[POETIC]`/`[RIFF]` **declared UNUSED** (this tape contains no figurative set-piece and I add no house speculation). `[CRITICAL DIVERGENCE]`, `[DIVERGENCE]`, `[CONVERGENT]`, `[RE-TREAD]`, `[ASR]` are **row-status labels, not registers.**

**Scope fence:** every name, number and quotation below is on the saved tape. Where a name is ASR-mangled the garbled form is quoted **as served** and the repair sits outside the quotation in an `[ASR: …]` bracket. Where I supply something the tape does not — chiefly the spelling of proper nouns, and the SCN1A reading — it is flagged as **my inference** inline. **No external source was fetched this session**, so no figure here is laundered into external fact: a number is either `[C]` (his) or absent. Cross-references into existing canon are marked *read from canon this session* and are not re-asserted.

---

## §0 · Source identity, rail receipt, title audit, attribution limit, dedupe

**★ RAIL: RUNG 1 (`youtube-transcript-api`, system python3) WON ON THE FIRST PROBE.** `YouTubeTranscriptApi().list('xTVa-wsEf5I')` returned **21 tracks, all `is_generated=True`** (`ar, bn, nl, en, fr, de, iw, hi, id, it, ja, ko, ml, pl, pt, pa, ru, es, ta, te, uk`) — **no manual/human caption exists on this upload**. `.fetch()` on AUTO `en` returned **1,423 cues, no `IpBlocked`, no 429**. Rungs 2 (`yt-dlp --write-auto-subs`), 3 (CDP transcript panel on :9333) and 4 (faster-whisper) **were never invoked**. No audio downloaded; no browser tab opened; no GPU touched. (`yt-dlp --dump-json` was used **only** for metadata and did emit an `n challenge solving failed` warning — irrelevant here, since it affected format URLs, not the fields read.)

**★ TITLE AUDIT — the title is the speaker's own slide title, and the upload truncates it.** On tape, mid-talk: “solving rare at scale”, and immediately “rare is just a construct of the of the diagnostic piece”. So *“Solving Rare at Scale”* is a **spoken quotation of his own slide**, not packaging. The uploader's description carries the fuller form — *“Solving Rare at Scale: effective therapies developed for patients with patients”* — and **the second half is the actual thesis** (patients as co-developers from step one, not subjects). The title is faithful; it is also the half that flatters. `[EST]`

**★ SPEAKER ROSTER — two voices, zero speaker labels, and one attribution that must be declared as inference.** The caption track has **no speaker diarisation**; turns are marked only by `>>`, and only in the closing Q&A. The presenter is identified robustly: the description names **Richard Novak**, CEO of **Unravel**, and the tape is entirely first-person-plural company narration (“we started Unravel as you know five years ago”, “calling ourselves the predictable medicine company”). The interlocutor is **not named anywhere on tape**. I attribute him to **Michael Levin** on three independent grounds, and I flag it as inference because the tape never says the name: (i) the **channel is Levin's**; (ii) the description addresses him as *“my friend and long-time collaborator”* and the uploader; (iii) at “and then you and Don Inber were of course the founding academic partners” Novak turns and says “and then you and Don Inber were of course the founding academic partners”, and the closing exchange (“we have uh transcripttos from anthrobots”) is unmistakably Levin-lab work. **Declared limit: *Levin* is a channel-and-content inference, not a tape claim.** Every quote in §1–§2 is attributed to **Novak** unless marked otherwise; the only block attributed to the host is the anthrobot exchange at 43:38–47:32.

**★ DEDUPE — NEW SOURCE, FULL DROP, and the corpus agrees.** `xTVa-wsEf5I` = **0 hits** across `drops/`, `YT_TRANSCRIPTS/` and `CANON_INDEX.md` before this pass; the phrase *“solving rare”* = **0**; `pit hopkins` = **0** in both trees; `vorinostat` = **0** in `drops/` and 1 (this file) in `YT_TRANSCRIPTS/`. **4-gram containment against all 990 transcript files: max 1.41 %** (`wK8QpPXkGZI_WeMightBeWrongAboutTime`), then 1.27 % (`BUWesguMWDc…hinton_diary_3way_splice`) — **an order of magnitude below any clip threshold**, and the shared grams are generic seminar filler (`you know`, `we can`, `at the same time`). ⇒ **No parent, no re-cut, no sibling.** The two prior drops that match `novak` are unrelated (one is the string `novaknown` inside a Wikipedia garble). **Existing canon that this drop CROSS-REFERENCES rather than re-files:** `EY0nrb7AXJs_levin_friston_chis_ciure_2026-11-21.md` already carries the anthrobot finding at `[EST]` (its `D4` holds the *9,000 DEG / half the genome* pair), so §1e below is marked **`[RE-TREAD]`** and adds only the *new* content — that Novak's platform is offered as a chemical-programming interface **to** anthrobots, which is not in canon; and `EBF0KUX_jpA_Levin_ThoughtsAsThinkers…` is the same channel, a different talk, and is the source for Levin's basal-agency vocabulary if a reader wants it.

---

## §1 · What is actually said

A 40-minute company pitch followed by 7 minutes of Q&A. The structure is deliberate: **market failure → instrument → three validations → commercial engine → a speculative gift to the host.** Everything below is his narration; nothing is my reconstruction.

### 1a · The premise: target-first drug discovery is a losing bet, and the reason is ontological `[HYP]`

Unravel, “we started Unravel as you know five years ago”, calls itself “calling ourselves the predictable medicine company”. The pitch is “solving rare disease at scale and not just like one or two diseases at a time”. The market arithmetic: “They're about 15,000 rare diseases. There's probably double or triple that in reality.” — and the incumbent method “one drug, one disease just cannot work at, you know, a billion plus dollars per drug”.

His failure statistics, deployed as the villain: “only only 5 or 10% of drugs in the clinic actually go for approval”; for genuinely novel mechanisms “it's a 2% success rate. That's just mindblowingly terrible, right? Like we have a 150 chance of success at a billion dollars a pop”. *(The token `` `150 chance` `` is ASR for the spoken {1 in 50}; the arithmetic is consistent with 2 %. Quoted as served.)* The diagnosis is not *we need better chemistry* but **the wrong unit of analysis**: “it's a nice narrative. Um but it's a wrong narrative”, because biology is “It's a complex system and it's unpredictable.” and “Um it's not necessarily deterministic”. Hence the thesis sentence that the whole company rests on — “it's patients not diseases that respond to treatments” — and the corollary that “the disease is sort of this artificial grouping”.

The historical warrant is offered twice and both are worth having exactly: “goes back 200 years to William Oler at least that we know of” *(ASR “Oler” = **Osler**; the 200-year figure is his, uncited)*, glossed by the aphorism “the good physician treats the disease the great physician treats the patient who has the disease”. Faithful quotation or not, the function is clear: **200 years of clinical practice already holds the position the platform is built to industrialise.**

### 1b · The instrument: sample the patient's state, simulate on the network, rank the pharmacopeia

The model hierarchy is stated with unusual honesty about its own limits. Cells in a dish are “Cells from a patient in a dish are not a patient”; and the objection is specific rather than general — “half half the patients that we deal with are on extensive polyarmacies” and “Cells from a patient in a dish are not a patient” carry the point that *ex vivo* cells lack the drug exposure the patient actually lives in. Then the Box line, “all models are wrong, but some may be useful, nonetheless”, used **not** as a licence to model but as a bound on it: models are cheap, but the thing behind the model is a *person* (“Cells from a patient in a dish are not a patient”).

What they actually build: “we start with individual patient RNA” because “the clinical success really depends on molecular data from the patient”; “each patient we build what we call a living molecular twin” — explicitly *not* a literature-search twin (“this is not based on for example LLM searches of the literature and and other patients”), which is a direct pre-emptive answer to the obvious objection — *isn't this just an LLM with extra steps*. The substrate choice is argued, not assumed: RNA is “the most informationrich part of biology”, because “DNA doesn't change.” — the genome is a constant, the transcriptome is the state. And crucially the input is the patient's own file, not a disease lookup (“this is not looking at a looking up a disease data set”), which is what licenses the claim that “this can come up with completely denovo mechanisms using just the data from the the patient”.

The engine: “bionav which is the computational uh platform” (the academic ancestor of which was “Nemoad”, *not* re-derived here), a network screen whose stated difference from CMap-style signature matching is that “it actually looks at the full consequence of the network interaction”. What it ranks is a **signed** effect, and the sign runs both ways: “worsening the disease or mimicking the disease state”. “most drugs just don't have any effect”; “about a percent or a couple percent of the drugs will have some sort of effect”.

The scale number, and the one that does most of the work in the pitch: “we can screen about 40,000 molecules in silicone”, “40,000 N of one clinical trials done completely in silicone” *(ASR “in silicone” = **in silico**, consistently across the tape — never corrected on tape)*. The justification for covering biology this broadly is a genuinely interesting claim: “Every drug's a dirty drug.” — therefore hundreds of off-target effects × 40,000 molecules, against “150 or so uh targets that are hit by I think 90% of all of approved drugs”.

The epistemic stance is then stated in the metaphor that will matter for §3: “it's not a black box. It's a noodle soup. Everything's intertwined”, “you can tease out a noodle if you give it enough effort”. And the anti-black-box claim is repeated with teeth — “It's not just a random weight model”, “It's actually explaining the effect”.

### 1c · Three validations, in ascending order of strength of claim

**(i) Replication of a known mechanism (tuberous sclerosis).** He chose deliberately the most favourable possible test — a well-characterised pathway — “there's this disorder called tuperclerosis complex” *(ASR “tuperclerosis” = **tuberous sclerosis complex**)*, TSC1/TSC2 → mTOR. “It took six years to characterize this.” His run: “we took a data set from 10 TSC patients from these organoids” — organoids, transcriptome only, diagnosis label withheld — and the answer came back “it took us about two hours”. **This is the pitch's central evidentiary set-piece.**

**(ii) Retro-prediction of a *drug-class* difference nobody intended (statins).** “statins work in about 25% of the patients of the ones that should be benefiting from it and 3% actually have a worsening of their condition”. During the pandemic, across mixed datasets, certain statins were predicted protective and others anti-therapeutic; with a UCSF/Stanford health-records group looking at hyperlipidaemic pre-vaccine patients with death as endpoint, “we predicted four out of five of those correctly”. The direction — “lovatin provostatin almost significantly worsened outcomes”; “tovastatin and simatanin very significantly protected patients”; and the mechanistic puzzle is sharpened by “the difference between I think lovastatin and sveastatin if I'm not mistaken is a hydroxal group”. *(All statin names in these four spans are ASR-mangled; `tovastatin`/`simatanin`/`sveastatin` cannot be resolved to chemical identities from the tape alone, and I do **not** resolve them.)*

**(iii) N-of-1 clinical use (Savannah).** The strongest human claim and the weakest evidentiary one. “was diagnosed with SMC 1A” *(ASR “SMC 1A”; **my inference** — not a tape claim — is `SCN1A`; the tape calls it “a developmental epileptic encphylopathy” and never says Dravet)*. Age at intake: “she was about 10 years old”. She was “hospitalized about 100 days a year on average” and “she was removed from hospice”. The clinician applied “two prescription drugs, two vitamins and in seven weeks she was able to walk”. Then the sequence that makes causal attribution impossible: “They added a couple more drugs since then”, and after that “she's been completely seizure free for about six months”.

The population claim built on cases like this — “we have about a 97% uh positive clinical response rate” — is then set against the 2 %-novel-mechanism figure and against the 5–10 % clinical approval rate, which is the comparison §4 attacks. Supporting assets: “we have the largest rare disease patient RNA seek data set”, “thousands of samples, 130 different disorders”; and a shipping detail that is the most operationally distinctive thing on the tape — nasal self-swabs (“collecting data from uh from patients using nasal swabs”) whose preservative “preserves RNA and other nucleic acids even these trace amounts”, stable at room temperature for over a month, which “this inactivates the pathogens” and so clears customs (“the outback of Australia”). Workflow name: “we developed this process called rare shift”, eight samples per patient (“we collect eight samples per patient”) because “we actually collect two full circadian cycles for each person” — “we do longitudinal analysis”.

### 1d · The commercial engine: one drug, many disorders, by response not diagnosis

The scaling move is stated as the title's content and then dissolved: “solving rare at scale”; “rare is just a construct of the of the diagnostic piece”. One patient carrying three ultra-rare conditions — “each one has a one in 100,000 chance” — is, by his own arithmetic, vanishingly unlikely to have a twin anywhere alive, and yet “we can group patients by similar drug responses and not their supposed diagnosis” — and the Uber analogy is load-bearing rather than decorative: “the other company that I want to compare ourselves to is Uber”, “as long as you have one customer and one driver with the car, you have a market”.

The worked case is **Rett** (“we start out with Rhett syndrome”, “that's for Rhett syndrome and pit Hopkins”). The mechanism story: an RNA-seq profile plus public data, then a target that “has nothing to do with that original target and yet this is what shifts that network to a more therapeutic state” — i.e. the network's leverage point is *not* the causal gene. The drug: “turns out that veristat” *(ASR “veristat” = **vorinostat**, per “Vernistat's an HDAC inhibitor”)*, which engages the target indirectly through a metabolite, then tested in mice (“we were actually able to dose them with with this oral liquid vernostat solution”) with two results — “not only survived longer um but they also uh actually recovered some capabilities that they lost”. The comparator and its limit: “trfinitide which is an approved drug the only approved drug for red syndrome as of three years ago” *(ASR “trfinitide” = **trofinetide**, “red syndrome” = **Rett**)*.

Rapid models fill the gap before clinicians will prescribe: “squishyware models”, “crispants of of tadpoles injected at the four cell stage” — “in two in two weeks we have a whole model developed from scratch” — and the design rationale is the epistemically best sentence on the tape: “the real patients don't have identical phenotypes”, so “if we see a drug working in these animal models, it's more likely to then work in the clinic”. The MECP2 knockdown (“knock down the um the MECP2 gene”) is heterogeneous by construction, “You get these these uh uh mosaics.”

Then a mechanism surprise that he reports against his own thesis: “Vernistat's an HDAC inhibitor”, and “if you have too much acetilation or too little it benefits both” — a *normalising* drug where the tidy story predicts a one-directional one. Cilia phenotype: “it actually helps with celia orientation uh and length”.

Second N-of-1, this time a toddler: “he was in pali of care”, “they started with 115th of the of the oncology dose” *(ASR “115th”; intended value approximately one fifteenth; not resolvable from tape)*, then “normalized blood metrics, improved sleep quality and improved motor and cognitive function”, “they continued for two years”.

Now the engine proper: a trial in Colombia (“we're actually in doing clinical trial in uh South America in Colombia”), “patients already gone through the complete fivemonth regimen”, “collecting longitudinal data every two weeks over five months” — and the reason they like it is anti-statistical, per-patient longitudinal baselines rather than cohort averaging. In parallel, a non-model animal: “these are actually uh sea lions” with “neurotoxin poisoning which causes a lot of similar symptoms” and “mortality rate about 90 90% plus”, treated through a field-deployed kit built with a California foundation — and out of that work “we started working with the Pit Hopkins Foundation”.

**Pitt-Hopkins is where the platform's negative output does real work.** “about a quarter of the patients were predicted to have adverse responses to vernest” — one quarter of patients predicted to be *harmed* by the drug that helps Rett. “analyzing uh 13 of the 15 known Pit Hopkins patients”. Then the expansion: “we actually added about 18 additional CNS disorders”, presented “American Epilepsy Society next week”, on “close to 160 patients plus 160 controls” — “this is a 40,000 times 160 person trial study”.

The stratification case that carries the most theoretical weight is **ZTTK**: “a disorder called ZTTK”, “It's a splicing factor”. Two subgroups, “including the same exact mutation” — “a downstream gene that helps perfectly explain these two subgroups”, identified as “it's actually part of the TCA uh cycle”. He states the explanatory limit honestly: they can find the marker, not the cause.

Assets and pipeline close: non-responders get “other programs for the patients who are the non-responders to ravel one” and “ravel 73 that actually seems to be pretty complimentary to ravel one”; “a table of the five uh commercial programs”; and the co-founded sibling “Astra Salva”, “Thomas Wagner with his son and Paul Schmidt as the CEO”, for “adrenal lucodistrophe as well as Alexander disease”.

### 1e · Q&A: the platform offered as a chemical-programming interface `[RE-TREAD]` + one new claim

The host's closing proposal (“we have uh transcripttos from anthrobots”) re-states a finding **already in canon** (`EY0nrb7AXJs_levin_friston_chis_ciure_2026-11-21.md`, `D4`: ~9,000 DEGs, half the genome) — filed here as **`[RE-TREAD]`, not new**. The number is on this tape too (“they have something like 9,000 differentially expressed genes”, “almost half the genome”) and the raison d'être is “they have the ability to heal neural wounds”.

**What is new to canon is the interface claim.** The host asks whether the platform could pick drugs that shift anthrobots onto other trajectories; Novak's answer is that no new build is needed, because “The input into our platform is is basically a differential or like two different transcriptto profiles”. That is a general-purpose statement: *any* desired state transition expressible as a differential transcriptome is a queryable problem. He then generalises it himself via “a ongoing collaboration around uh organ preservation”/“the bioasis program” and lands the phrase worth keeping — “It's almost like a field programmable controller, but you field program it with molecules.”

---

## §2 · Verified quantitative claims (literal, with what each one actually measures)

Every quote is a verified substring of the saved file (§5). Register `[C]` = his claim, unaudited, no denominator stated unless the quote states one.

| # | t | Claim as spoken | What it actually measures |
|:--|:--|:--|:--|
| N1 | 0:09 | “we started Unravel as you know five years ago” | Company age. Implies a ~2021 founding **if** the date is right — *my arithmetic*, and the tape's only founding-date statement. `[EST]` |
| N2 | 0:23 | “They're about 15,000 rare diseases. There's probably double or triple that in reality.” | Disease-count estimate, uncited, and hedged by a factor of 2–3 in the same breath. `[C]` |
| N3 | 1:20 | “only only 5 or 10% of drugs in the clinic actually go for approval” | Clinical-phase success rate, “they say” — explicitly second-hand even on tape. `[C]` |
| N4 | 1:27 | “it's a 2% success rate. That's just mindblowingly terrible, right? Like we have a 150 chance of success at a billion dollars a pop” | Novel-mechanism success rate (2 %) and cost ≈ $1 bn/drug. The one-in-fifty reading is my arithmetic on 2 %; the token itself is ASR-mangled. `[C]` |
| N5 | 5:07 | “half half the patients that we deal with are on extensive polyarmacies” | Half the cohort on polypharmacy — the argument that *ex vivo* models are invalid. `[C]` |
| N6 | 9:12 | “we can screen about 40,000 molecules in silicone” | Library size of the in-silico screen. `[C]` |
| N7 | 9:19 | “40,000 N of one clinical trials done completely in silicone” | The equivocation that matters: 40,000 *simulated* trials ≠ 40,000 trials. `[C]` |
| N8 | 9:59 | “150 or so uh targets that are hit by I think 90% of all of approved drugs” | approximately 150 targets carrying approximately 90 % of approved drugs — the narrow-intent / broad-off-target argument. `[C]` |
| N9 | 16:01 | “statins work in about 25% of the patients of the ones that should be benefiting from it and 3% actually have a worsening of their condition” | Statin response/worsening rates. Two percentages, no cohort size, no citation. `[C]` |
| N10 | 16:33 | “It took six years to characterize this.” | Six years of published mechanism work. `[C]` |
| N11 | 16:37 | “we took a data set from 10 TSC patients from these organoids” | n = 10 organoid lines; transcriptome only, label withheld. The strongest design detail on the tape. `[C]` |
| N12 | 17:03 | “it took us about two hours” | The 2-hours-vs-6-years compression claim. **My read: this measures retrieval speed, not inference** — see §4. `[C]` |
| N13 | 17:43 | “we predicted four out of five of those correctly” | 4/5 statin directions correct; the fifth is the one he had the least data on (his own hedge, 18:09). `[C]` |
| N14 | 18:28 | “the difference between I think lovastatin and sveastatin if I'm not mistaken is a hydroxal group” | A one-hydroxyl difference between two statins — a mechanistic detail he hedges twice. `[C]` |
| N15 | 20:07 | “we collect eight samples per patient” | 8 samples/patient, 2 circadian cycles (“we actually collect two full circadian cycles for each person”). The sampling budget that makes the baseline non-flat. `[EST]` |
| N16 | 21:33 | “hospitalized about 100 days a year on average” | ~100 hospital days/yr ≈ a third of her life by his own arithmetic (stated at 21:37). `[C]` |
| N17 | 21:50 | “two prescription drugs, two vitamins and in seven weeks she was able to walk” | 7 weeks to ambulation on 2 Rx + 2 supplements. n = 1, open label, concurrent changes. `[C]` |
| N18 | 22:34 | “we have about a 97% uh positive clinical response rate” | **The headline number.** No denominator, no control, no pre-registered endpoint. §3 R6. `[C]` |
| N19 | 23:32 | “thousands of samples, 130 different disorders” | Dataset size claim, unverifiable externally this session. `[C]` |
| N20 | 28:19 | “trfinitide which is an approved drug the only approved drug for red syndrome as of three years ago” | Trofinetide as the sole approved Rett drug, as of three years before the talk. `[C]` |
| N21 | 29:28 | “in two in two weeks we have a whole model developed from scratch” | Two-week model turnaround claim. `[C]` |
| N22 | 31:47 | “they started with 115th of the of the oncology dose” | Starting dose ≈ one-fifteenth of the oncology dose *(ASR “115th”, unresolved)* — the safety argument is titration speed, not pharmacology. `[C]` |
| N23 | 32:41 | “collecting longitudinal data every two weeks over five months” | Biweekly sampling × 5 months = ~10 points/patient. This is the design that makes N18 weaker *and* the platform stronger. `[EST]` |
| N24 | 33:11 | “mortality rate about 90 90% plus” | Sea-lion mortality 90 % or more. `[C]` |
| N25 | 34:00 | “about a quarter of the patients were predicted to have adverse responses to vernest” | ~25 % of an N-of-15 population predicted to be harmed — the negative-output claim. `[C]` |
| N26 | 34:28 | “analyzing uh 13 of the 15 known Pit Hopkins patients” | 13 of 15 known patients: near-census, not a sample. `[C]` |
| N27 | 35:15 | “close to 160 patients plus 160 controls” | 160 + 160. `[C]` |
| N28 | 35:34 | “this is a 40,000 times 160 person trial study” | 40,000 × 160 “trial study” — again simulations, not trials. `[C]` |
| N29 | 37:23 | “hundreds of thousands of patients um that could benefit from the same drug” | Hundreds of thousands of expandable patients — the market claim that justifies the whole architecture. `[C]` |
| N30 | 40:55 | “a table of the five uh commercial programs” | Five commercial programs. `[EST]` |
| N31 | 43:59 | “they have something like 9,000 differentially expressed genes” | 9,000 DEGs / “almost half the genome” — **already in canon** (`EY0nrb7AXJs` D4). `[RE-TREAD]` |
| N32 | 14:05 | “about a percent or a couple percent of the drugs will have some sort of effect” | ~1–2 % of the library shows *any* effect, most “don't have any effect”. The precision claim hidden inside the recall claim. `[C]` |

**Count: 32 quantitative claims, 147 gated spans, 0 fabricated.**

---

## §3 · EILT mapping — with the Friction Rule discharged

Nine rows: **3 `[CONVERGENT]`, 3 `[DIVERGENCE]`, 2 `[CRITICAL DIVERGENCE]`, 1 `[A]`.** The table is **not** uniformly convergent, and the two critical rows both land on the speaker's *strongest* claims rather than on throwaway lines.

| # | House leg | On tape (verbatim) | Status | Where it breaks |
|:--|:--|:--|:--|:--|
| R1 | **Constructor Theory — negative constraints are the fundamental object** | “worsening the disease or mimicking the disease state”; “subgroup two should just never get it”; “about a quarter of the patients were predicted to have adverse responses to vernest” | `[CONVERGENT]` | Holds unusually well: the platform's primary sellable output is a **forbidden set** — which transformations of *this* patient are impossible/harmful — and that set, not the positive one, changed a trial's enrolment. This is the house's own §24 line (*epiplexity is constraint; “this shit didn't work” is the compressible part*) arriving from a wet lab. Breaks only at the edges: his *impossible* is a **predicted** impossibility at a confidence he never states, so the forbidden set is soft where CT's is categorical. |
| R2 | **Levin/saliency — the self is a state, not a code; continuity is of saliency not fidelity** *(canon: `levin_concept_atlas…` F-LEV-SALIENCY)* | “DNA doesn't change.”; “we start with individual patient RNA”; “we actually collect two full circadian cycles for each person” | `[CONVERGENT]` | The substrate choice is the same move the house makes: the genome is a constant and the *dynamic regulatory state* is the object, sampled across two full circadian cycles precisely because “the baseline isn't flat for everybody”. Where it breaks: he never asks **whose** saliency is being preserved — he optimises a molecular distance-to-healthy, not the organism's own preferred states (see R4). |
| R3 | **Wolfram — computational irreducibility: no shortcut; you must run it** | “it's not a black box. It's a noodle soup. Everything's intertwined”; “you can tease out a noodle if you give it enough effort”; “It's not just a random weight model”; “it took us about two hours” | **`[CRITICAL DIVERGENCE]`** | **This is the row the drop exists to carry.** He claims exactly the shortcut irreducibility forbids — and claims it as the product: the model is *not* a black box, the noodles can be teased out, and six years of published mechanism work is reproduced in “it took us about two hours”. Either the gene-regulatory network is a **reducible abstraction** (then his claim is true and the house's Wolfram leg is bounded to systems above that scale), or it is irreducible (then the two-hour match is a **confounded test**: the mTOR answer was already in the literature *and* in the drug library, so the experiment cannot distinguish *derived the mechanism* from *retrieved the known answer*). **The tape never notices that its own validation is unfalsifiable in exactly this way** — see §4. |
| R4 | **Levin — basal agency, cognitive light cones, competence as goal-directedness** | “what's the underlying disruption in the patient and how could we perturb it into a more favorable state”; “including the same exact mutation”; “a downstream gene that helps perfectly explain these two subgroups” | `[DIVERGENCE]` | The data is Levin's; the framing is not. ZTTK is a textbook competency result — one mutation, two stable phenotypes, split by a **downstream metabolic gene** (“it's actually part of the TCA uh cycle”), i.e. the tissue found its own attractor rather than executing the mutation's instruction. Yet the workflow assigns the goal externally (“what's the underlying disruption in the patient and how could we perturb it into a more favorable state”): the patient is a **state to be steered by an optimiser**, and the agent is Bionav plus the clinician. Levin's light cone lives *in* the tissue; Novak's lives in the software. He reports the phenomenon and misses the ontology. |
| R5 | **Moloch — ungrounded multi-agent defection; the fix is an enforceable contract, not cheaper coordination** | “one drug, one disease just cannot work at, you know, a billion plus dollars per drug”; “as long as you have one customer and one driver with the car, you have a market”; “each one has a one in 100,000 chance” | `[DIVERGENCE]` | The 15,000-disease gap is a clean Moloch: no single developer can rationally fund a market of one, so the aggregate is mass non-development. His fix is **marginal cost** — “as long as you have one customer and one driver with the car, you have a market” — not contract. The house says the defection is dissolved only by a verifiable commitment (ledger + Praus); he says it is dissolved by making the unit economics small enough that defection stops paying. **Both can be true and they have different signatures:** if he is right, orphan markets get served without new regulation; canon's evidence so far (an Orphan Drug Act that did not close a 15,000-disease gap) is weak support for the contract side. Unresolved, and therefore genuinely divergent rather than decorative. |
| R6 | **Non-rolling ledger — provenance is auditable, and provenance ≠ validity (F22/§18.8)** | “we have about a 97% uh positive clinical response rate”; “only only 5 or 10% of drugs in the clinic actually go for approval”; “it's a 2% success rate. That's just mindblowingly terrible, right? Like we have a 150 chance of success at a billion dollars a pop”; “the barrier for testing in patients is not a full-blown placebo control trial with every single patient” | **`[CRITICAL DIVERGENCE]`** | His headline is a **before/after between two incommensurable rates**: 2 % is per-drug approval in formal trials with a placebo arm; “we have about a 97% uh positive clinical response rate” is clinician-reported response in open-label individualised care, with patients **selected into** a workflow and no denominator ever stated. He then states, elsewhere, the reason the comparison cannot be made — “the barrier for testing in patients is not a full-blown placebo control trial with every single patient”, and “there obviously, you know, limits, there's ethical considerations”. So the source uses as an *achievement* precisely the class of number the house ledger files as an *unprovenanced claim*. This is not a hand-wave: the disagreement is about **what counts as evidence**, and on the house's own standard the 97 % is `[C]`, not `[EST]`. |
| R7 | **Friston — FEP: a system lowers surprise; a cheap proxy lowers local FEP and raises total (§21, “RLHF as FEP avoidance”)** | “about a percent or a couple percent of the drugs will have some sort of effect”; “they started with 115th of the of the oncology dose”; “worsening the disease or mimicking the disease state” | `[DIVERGENCE]` | The platform's *product* is a per-patient negative prediction, which is information bought at the patient's risk and paid for by the patient's exposure, not the company's. Under the house's §21 test — *is the system's cost being paid where the consequences land?* — the answer is partly yes (trial enrolment excluded the quarter predicted to be harmed: cost paid where consequences land) and partly no (the company's knowledge grows from patients who are already out of options, so the marginal patient bears the residual risk the model cannot bound). The tape's own safety instrument is discretionary caution — “out of an abundance of caution” — and titration speed (“they started with 115th of the of the oncology dose”), not a bound. |
| R8 | **Light cones / epiplexity — local perturbation propagates along the graph** | “what happens if you knock out a traffic light”; “What's what's talking to what?”; “it actually looks at the full consequence of the network interaction” | `[A]` | **Ours, not his.** The traffic-light riff (a Cambridge signal backing up the interstate) is his illustration of network reach; the house reading — that the *adjacency structure* is the light cone and “What's what's talking to what?” is the epiplexity question — is my mapping. Filed as analogy so it is never mistaken for a claim he made. |
| R9 | **F23 — plurality ≠ independence; heterogeneity is load-bearing** | “the real patients don't have identical phenotypes”; “if we see a drug working in these animal models, it's more likely to then work in the clinic”; “squishyware models” | `[CONVERGENT]` | A genuinely independent arrival at a house finding: a deliberately **heterogeneous** animal model is *better* evidence than a homogeneous one, because “the real patients don't have identical phenotypes”. That is F23's content (a clean homogeneous panel is one witness wearing many hats) derived from wet-lab experience with no framework. Converges fully; no break worth naming. |

### R3 in prose — where the framework and the source actually disagree

The house's Wolfram leg says: for a computationally irreducible system there is no compressed route to the outcome — you run it, or you do not know. Novak's pitch says the opposite in its most load-bearing sentence: the model is “it's not a black box. It's a noodle soup. Everything's intertwined”, the noodles “you can tease out a noodle if you give it enough effort”, and the payoff is that the six-year characterisation came back in “it took us about two hours”.

Those cannot both be right at the same scale, and the tape contains the evidence that decides it — not in his favour. **The test he designed could not fail.** He withheld the diagnosis label (“this is not looking at a looking up a disease data set”), which controls for *label leakage*, not for *answer leakage*: tuberous sclerosis → TSC1/TSC2 → mTOR was published, the mTOR inhibitors were in the library, and the six years of characterisation (“It took six years to characterize this.”) were already in the literature the platform's cell-line compendium was drawn from. A model trained on drug-perturbation transcriptomes will place an mTOR inhibitor at the top of a TSC organoid profile **because that pair is in the training data as a matched pair**. The two-hour match is therefore consistent with three different worlds: (a) the platform genuinely infers, (b) the platform retrieves a memorised pair, (c) the GRN is reducible and inference is cheap. **The design cannot distinguish them, and the tape presents it as if it settles (a).**

The honest house verdict: R3 is a divergence *and it cuts both ways*. If the platform does infer at two hours, the house's irreducibility claim needs a scale bound it does not currently have (the GRN is a 20,000-node object, not a ruliad). If it retrieves, then the pitch's central evidentiary set-piece is a memory test — and the house's own F22 (“provenance, not validity”) is the correct instrument for saying so, which is why R6 and R3 are the same defect seen from two ends: **the tape mistakes a well-provenanced answer for a validated one.**

---

## §4 · The weakest joint

**The 97 % vs 2 % comparison (N18, R6).** Two rates, two evidence classes, no denominator for the first, presented as a thirty-fold improvement in the same quantity. Everything downstream of it in the commercial narrative — “hundreds of thousands of patients” (N29), five programs (N30), the syndicated-programme model — inherits a number that would not survive a single question in a room that asked for the denominator. He states the reason it cannot be compared, in the Q&A, unprompted (“the barrier for testing in patients is not a full-blown placebo control trial with every single patient”), and never applies that reason backwards to his own headline.

**Runner-up, and the one that matters more for the framework:** the TSC validation (N11/N12) is confounded by a known answer, so the tape's strongest quantitative compression claim is also its least falsifiable experiment. A rigorous version is cheap and he does not propose it: hold out the mTOR inhibitors from the library and see whether the platform *finds* them. If it does, R3's critical row collapses in his favour and the house owes a scale bound. **Filed as falsifier F-NOV-2.**

**Third:** Savannah (N16/N17). Between the intervention and the seizure-free interval the family “They added a couple more drugs since then”, and some were removed on the same advice. Attribution to the platform is therefore not separable from the concurrent regimen changes — which the tape reports candidly and then does not let constrain the 97 % claim.

**What is *not* weak, and should be said plainly:** the negative-output discipline (R1), the sampling design (N15/N23), and the willingness to exclude a quarter of patients from a trial on a predicted-harm signal (N25/N26) are all better epistemics than the pitch's headline number implies. The company's practice is more careful than its slide.

---

## §5 · Verification log

Method: the flat caption body was whitespace-normalised, each span was tested as a literal substring, and every span in this drop was **injected from the verified set, never retyped**. 147/147 PASS, 0 FAIL. Positive control HIT (“They're about 15,000 rare diseases. There's probably double or triple that in reality.”). **Declared non-tape quotations (8, enumerated, none of them presented as speech):** the video title *“Solving Rare at Scale”* (4 occurrences — title, frontmatter, heading, footer) · the uploader's description phrase *“my friend and long-time collaborator”* (attributed to the description inline in §0) · three house-canon strings quoted **as canon, not as tape** — *“this shit didn't work”* (§24 of the cosmology synthesis), *“RLHF as FEP avoidance”* (§21 heading), *“provenance, not validity”* (F22/§18.8). **Everything else inside quotation marks — 233 spans — is a verified tape substring.** (The strings restated inside this very sentence are the same eight, quoted a second time, which is why a naive span count of this file returns 246.) Six negative controls correctly ABSENT: `cure rate of 97%`, `vorinostat is approved for Rett syndrome`, `Richard Novak is a professor at Harvard`, `Unravel was founded in 2019`, `the trial met its primary endpoint`, `patients were randomized to placebo`.

| id | t | reg | verified substring |
|:--|:--|:--|:--|
| C1 | 0:09 | EST | `we started Unravel as you know five years ago` |
| C2 | 0:13 | EST | `calling ourselves the predictable medicine company` |
| C3 | 0:19 | EST | `solving rare disease at scale and not just like one or two diseases at a time` |
| C4 | 0:23 | C | `They're about 15,000 rare diseases. There's probably double or triple that in reality.` |
| C5 | 1:20 | C | `only only 5 or 10% of drugs in the clinic actually go for approval` |
| C6 | 1:27 | C | `it's a 2% success rate. That's just mindblowingly terrible, right? Like we have a 150 chance of success at a billion dollars a pop` |
| C7 | 2:15 | HYP | `it's a nice narrative. Um but it's a wrong narrative` |
| C8 | 2:32 | HYP | `It's a complex system and it's unpredictable.` |
| C9 | 2:35 | HYP | `Um it's not necessarily deterministic` |
| C10 | 3:43 | EST | `it's patients not diseases that respond to treatments` |
| C11 | 3:47 | HYP | `the disease is sort of this artificial grouping` |
| C12 | 3:57 | EST | `goes back 200 years to William Oler at least that we know of` |
| C13 | 4:03 | EST | `the good physician treats the disease the great physician treats the patient who has the disease` |
| C14 | 4:28 | EST | `all models are wrong, but some may be useful, nonetheless` |
| C15 | 4:50 | EST | `Cells from a patient in a dish are not a patient` |
| C16 | 5:07 | EST | `half half the patients that we deal with are on extensive polyarmacies` |
| C17 | 5:29 | HYP | `the clinical success really depends on molecular data from the patient` |
| C18 | 6:06 | EST | `we start with individual patient RNA` |
| C19 | 6:18 | EST | `the other company that I want to compare ourselves to is Uber` |
| C20 | 7:29 | HYP | `as long as you have one customer and one driver with the car, you have a market` |
| C21 | 8:20 | EST | `each patient we build what we call a living molecular twin` |
| C22 | 8:50 | EST | `this is not based on for example LLM searches of the literature and and other patients` |
| C23 | 9:12 | C | `we can screen about 40,000 molecules in silicone` |
| C24 | 9:19 | C | `40,000 N of one clinical trials done completely in silicone` |
| C25 | 9:46 | EST | `Every drug's a dirty drug.` |
| C26 | 9:59 | C | `150 or so uh targets that are hit by I think 90% of all of approved drugs` |
| C27 | 11:01 | HYP | `the most informationrich part of biology` |
| C28 | 11:05 | EST | `DNA doesn't change.` |
| C29 | 12:11 | EST | `this is not looking at a looking up a disease data set` |
| C30 | 12:29 | HYP | `this can come up with completely denovo mechanisms using just the data from the the patient` |
| C31 | 12:35 | EST | `bionav which is the computational uh platform` |
| C32 | 13:00 | EST | `it actually looks at the full consequence of the network interaction` |
| C33 | 13:23 | A | `what happens if you knock out a traffic light` |
| C34 | 14:35 | EST | `it's not a black box. It's a noodle soup. Everything's intertwined` |
| C35 | 14:44 | EST | `you can tease out a noodle if you give it enough effort` |
| C36 | 15:05 | HYP | `It's not just a random weight model` |
| C37 | 16:01 | C | `statins work in about 25% of the patients of the ones that should be benefiting from it and 3% actually have a worsening of their condition` |
| C38 | 16:26 | EST | `there's this disorder called tuperclerosis complex` |
| C39 | 16:33 | C | `It took six years to characterize this.` |
| C40 | 16:37 | C | `we took a data set from 10 TSC patients from these organoids` |
| C41 | 17:03 | C | `it took us about two hours` |
| C42 | 17:43 | C | `we predicted four out of five of those correctly` |
| C43 | 18:13 | C | `lovatin provostatin almost significantly worsened outcomes` |
| C44 | 18:17 | C | `tovastatin and simatanin very significantly protected patients` |
| C45 | 18:28 | C | `the difference between I think lovastatin and sveastatin if I'm not mistaken is a hydroxal group` |
| C46 | 19:00 | EST | `collecting data from uh from patients using nasal swabs` |
| C47 | 19:19 | C | `preserves RNA and other nucleic acids even these trace amounts` |
| C48 | 20:02 | EST | `we developed this process called rare shift` |
| C49 | 20:07 | EST | `we collect eight samples per patient` |
| C50 | 20:13 | EST | `we actually collect two full circadian cycles for each person` |
| C51 | 20:59 | EST | `we can group patients by similar drug responses and not their supposed diagnosis` |
| C52 | 21:17 | C | `was diagnosed with SMC 1A` |
| C53 | 21:27 | C | `she was about 10 years old` |
| C54 | 21:33 | C | `hospitalized about 100 days a year on average` |
| C55 | 21:50 | C | `two prescription drugs, two vitamins and in seven weeks she was able to walk` |
| C56 | 22:03 | C | `she's been completely seizure free for about six months` |
| C57 | 22:16 | C | `she was removed from hospice` |
| C58 | 22:56 | C | `Savannah was put on was a nicotine patch` |
| C59 | 22:34 | C | `we have about a 97% uh positive clinical response rate` |
| C60 | 23:28 | C | `we have the largest rare disease patient RNA seek data set` |
| C61 | 23:32 | C | `thousands of samples, 130 different disorders` |
| C62 | 24:09 | HYP | `this is not repurposing` |
| C63 | 24:26 | EST | `two clinical trials for Ravvel one` |
| C64 | 24:37 | EST | `that's for Rhett syndrome and pit Hopkins` |
| C65 | 25:04 | EST | `solving rare at scale` |
| C66 | 25:07 | HYP | `rare is just a construct of the of the diagnostic piece` |
| C67 | 27:15 | EST | `we start out with Rhett syndrome` |
| C68 | 27:48 | HYP | `has nothing to do with that original target and yet this is what shifts that network to a more therapeutic state` |
| C69 | 27:55 | C | `turns out that veristat` |
| C70 | 28:19 | C | `trfinitide which is an approved drug the only approved drug for red syndrome as of three years ago` |
| C71 | 28:40 | C | `we were actually able to dose them with with this oral liquid vernostat solution` |
| C72 | 28:43 | C | `not only survived longer um but they also uh actually recovered some capabilities that they lost` |
| C73 | 29:01 | EST | `squishyware models` |
| C74 | 29:18 | EST | `crispants of of tadpoles injected at the four cell stage` |
| C75 | 29:28 | C | `in two in two weeks we have a whole model developed from scratch` |
| C76 | 29:54 | EST | `knock down the um the MECP2 gene` |
| C77 | 30:16 | EST | `You get these these uh uh mosaics.` |
| C78 | 30:38 | EST | `Vernistat's an HDAC inhibitor` |
| C79 | 31:01 | C | `if you have too much acetilation or too little it benefits both` |
| C80 | 31:10 | C | `it actually helps with celia orientation uh and length` |
| C81 | 31:26 | C | `he was in pali of care` |
| C82 | 31:47 | C | `they started with 115th of the of the oncology dose` |
| C83 | 31:57 | C | `normalized blood metrics, improved sleep quality and improved motor and cognitive function` |
| C84 | 32:03 | C | `they continued for two years` |
| C85 | 32:22 | EST | `we're actually in doing clinical trial in uh South America in Colombia` |
| C86 | 32:36 | EST | `patients already gone through the complete fivemonth regimen` |
| C87 | 32:41 | EST | `collecting longitudinal data every two weeks over five months` |
| C88 | 33:02 | EST | `these are actually uh sea lions` |
| C89 | 33:07 | EST | `neurotoxin poisoning which causes a lot of similar symptoms` |
| C90 | 33:11 | C | `mortality rate about 90 90% plus` |
| C91 | 33:35 | EST | `we started working with the Pit Hopkins Foundation` |
| C92 | 34:00 | C | `about a quarter of the patients were predicted to have adverse responses to vernest` |
| C93 | 34:28 | C | `analyzing uh 13 of the 15 known Pit Hopkins patients` |
| C94 | 35:05 | EST | `we actually added about 18 additional CNS disorders` |
| C95 | 35:11 | EST | `American Epilepsy Society next week` |
| C96 | 35:15 | C | `close to 160 patients plus 160 controls` |
| C97 | 35:34 | C | `this is a 40,000 times 160 person trial study` |
| C98 | 37:23 | C | `hundreds of thousands of patients um that could benefit from the same drug` |
| C99 | 38:16 | EST | `subgroup two should just never get it` |
| C100 | 38:42 | EST | `a disorder called ZTTK` |
| C101 | 38:43 | EST | `It's a splicing factor` |
| C102 | 39:30 | EST | `it's the son gene, S1 gene` |
| C103 | 39:47 | C | `it's actually part of the TCA uh cycle` |
| C104 | 40:29 | EST | `other programs for the patients who are the non-responders to ravel one` |
| C105 | 40:32 | EST | `ravel 73 that actually seems to be pretty complimentary to ravel one` |
| C106 | 40:55 | EST | `a table of the five uh commercial programs` |
| C107 | 41:03 | EST | `Astra Salva` |
| C108 | 41:05 | EST | `Thomas Wagner with his son and Paul Schmidt as the CEO` |
| C109 | 41:20 | EST | `adrenal lucodistrophe as well as Alexander disease` |
| C110 | 41:35 | HYP | `you as a person, you're unique` |
| C111 | 43:48 | EST | `we have uh transcripttos from anthrobots` |
| C112 | 43:59 | C | `they have something like 9,000 differentially expressed genes` |
| C113 | 44:02 | C | `almost half the genome` |
| C114 | 45:12 | C | `they have the ability to heal neural wounds` |
| C115 | 45:26 | EST | `a ongoing collaboration around uh organ preservation` |
| C116 | 45:35 | EST | `the bioasis program` |
| C117 | 46:36 | EST | `It's almost like a field programmable controller, but you field program it with molecules.` |
| C118 | 46:59 | EST | `The input into our platform is is basically a differential or like two different transcriptto profiles` |
| C119 | 15:15 | EST | `worsening the disease or mimicking the disease state` |
| C120 | 22:00 | C | `They added a couple more drugs since then` |
| C121 | 34:08 | EST | `out of an abundance of caution` |
| C122 | 43:20 | EST | `there obviously, you know, limits, there's ethical considerations` |
| C123 | 43:15 | EST | `the barrier for testing in patients is not a full-blown placebo control trial with every single patient` |
| C124 | 0:29 | EST | `one drug, one disease just cannot work at, you know, a billion plus dollars per drug` |
| C125 | 39:16 | EST | `including the same exact mutation` |
| C126 | 39:41 | C | `a downstream gene that helps perfectly explain these two subgroups` |
| C127 | 29:41 | EST | `the real patients don't have identical phenotypes` |
| C128 | 29:46 | EST | `if we see a drug working in these animal models, it's more likely to then work in the clinic` |
| C129 | 13:20 | EST | `What's what's talking to what?` |
| C130 | 15:08 | EST | `It's actually explaining the effect` |
| C131 | 25:54 | EST | `what's the underlying disruption in the patient and how could we perturb it into a more favorable state` |
| C132 | 24:21 | EST | `what we learn from that we can then turn into into um optimized medicines` |
| C133 | 7:06 | EST | `each one has a one in 100,000 chance` |
| C134 | 10:35 | EST | `brought in Neil Mooney as a as a chief medical officer who's brought eight drugs to market` |
| C135 | 10:42 | EST | `and then you and Don Inber were of course the founding academic partners` |
| C136 | 10:48 | EST | `John Quackenbush on on the regulatory network side` |
| C137 | 19:06 | EST | `we work with Zyo Research` |
| C138 | 19:33 | EST | `the outback of Australia` |
| C139 | 19:44 | EST | `this inactivates the pathogens` |
| C140 | 20:46 | EST | `we work even with undiagnosed patients` |
| C141 | 20:43 | EST | `we do longitudinal analysis` |
| C142 | 14:00 | C | `most drugs just don't have any effect` |
| C143 | 14:05 | C | `about a percent or a couple percent of the drugs will have some sort of effect` |
| C144 | 42:11 | EST | `predictable medicine starting with the clinical um then we can go to pre-clinical` |
| C145 | 37:29 | EST | `So now you're actually solving rare at scale, right? You're starting with one drug, one disorder` |
| C146 | 20:17 | EST | `the baseline isn't flat for everybody` |
| C147 | 20:24 | EST | `We sequence these patients using that kit that I mentioned` |

**ASR repairs used in prose only, never inside quotation marks:** `Oler`→Osler · `tuperclerosis`→tuberous sclerosis · `veristat`/`vernistat`/`vernest`/`vernostat`→vorinostat · `trfinitide`→trofinetide · `Rhett`/`red syndrome`→Rett · `in silicone`→in silico · `RNA seek`→RNA-seq · `psyia`/`celia`→cilia · `polyarmacies`→polypharmacy · `adrenal lucodistrophe`→adrenoleukodystrophy · `Don Inber`→Don Ingber (inference) · `115th`→1/15th (unresolved) · `SMC 1A`→SCN1A (**inference, not verified**) · `son gene, S1 gene`→SON (inference). **Left unresolved, not guessed:** the statin names in N9/N13/N14 (`tovastatin`, `simatanin`, `sveastatin`, `Rubatinat`), the CMO's surname (`Neil Mooney`), the co-founder's surname (`Fred`), and `Astra Salva`.

---

## §6 · Falsifiers and citation fence

- **F-NOV-1 (house-facing, R3).** If a GRN-perturbation model reproduces a *withheld* mechanism whose drug–disease pair is absent from its library, the house's irreducibility leg needs a stated scale bound. Canon currently has none.
- **F-NOV-2 (source-facing, R3/§4).** Hold out the mTOR inhibitors and re-run TSC. Failure to recover them falsifies the two-hours-vs-six-years claim as an inference; success falsifies the retrieval reading.
- **F-NOV-3 (R6).** A stated denominator plus a pre-registered response definition would convert the 97 % from `[C]` to `[EST]`. Nothing on the tape supplies either.
- **F-NOV-4 (R5, Moloch).** If an orphan market is served profitably without any new contractual or regulatory instrument, the marginal-cost reading displaces the contract reading on this axis.
- **F-NOV-5 (house-facing, R7).** If the negative-prediction output can be shown to cost the *company* (not the patient) when it is wrong — e.g. liability for a false positive — then §21's cost-location test is satisfied and R7 downgrades to convergent.

**Citable for:** every §1/§2 quotation (verbatim to `YT_TRANSCRIPTS/xTVa-wsEf5I.md` only, with the §5 garble key), the 32 quantitative claims **as his claims**, and the §3 friction rows with their status labels.
**NOT citable for:** any of the 32 numbers as fact; the identity of the interlocutor as a tape claim (channel-and-content inference); SCN1A/Dravet as the diagnosis; any external adjudication of the 15,000-disease or 150-target figures; and any EILT derivation — R3 and R6 are `[CRITICAL DIVERGENCE]`, R4/R5/R7 divergent.
**CANON-ID:** CANON-2026-11-25-xTVa-wsEf5I-NOVAK-RARE-AT-SCALE.
