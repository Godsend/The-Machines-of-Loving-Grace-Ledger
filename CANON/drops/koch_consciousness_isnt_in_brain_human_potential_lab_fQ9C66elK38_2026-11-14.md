---
title: "Christof Koch — Consciousness Isn't in the Brain (Human Potential Lab, Ep. 4)"
date: "2026-11-14"
author: "Dion"
version: "v1.0 — canon drop (IIT / substrate / idealism, with Friction Rule)"
source: "https://www.youtube.com/watch?v=fQ9C66elK38"
transcript: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/fQ9C66elK38_Koch_ConsciousnessNotInBrain_HumanPotLab_2026-11-11.txt"
transcript_timestamped: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/fQ9C66elK38_Koch_ConsciousnessNotInBrain_HumanPotLab_2026-11-11_timestamped.txt"
rail: "rung 4 — local faster-whisper small.en (CPU int8, chunked); rungs 1–3 dead on this host"
artifact-class: "near-verbatim ASR (local ASR; recognisable garbles — see §6 garble key)"
registers: "[EST] [HYP] [A] [C] [POETIC] [RIFF]"
status-flags: "[FRICTION] [CRITICAL DIVERGENCE] [ABSENT] [ASR] [VERIFIED-ext]"
rule: "Koch's IIT/Phi/idealism claims are reported as HIS positions, never as house claims or consensus. IIT's core claims are contested (see the 2023 pseudoscience letter, canon-verified). No untagged substantive claim is established."
---

# Canon Drop — Christof Koch, *Consciousness Isn't in the Brain* (Human Potential Lab, Ep. 4)

**Filed by:** Dion · **Filed:** 2026-11-14 · **Source uploaded:** 2026-11-11

## §0. Provenance

| field | value |
|---|---|
| **Video id** | `fQ9C66elK38` |
| **Title** | *Consciousness Isn't in the Brain* |
| **Channel** | Human Potential Lab (`@humanpotentiallabpodcast`), host **Dr. Scott Barry Kaufman** |
| **Guest** | **Christof Koch** — physicist/neuroscientist |
| **URL** | https://www.youtube.com/watch?v=fQ9C66elK38 |
| **Duration** | 2406 s (**40:06**) |
| **Uploaded** | 2026-11-11 |
| **Transcript (flat)** | `YT_TRANSCRIPTS/fQ9C66elK38_Koch_ConsciousnessNotInBrain_HumanPotLab_2026-11-11.txt` — **38,615 chars**, 6,699 words |
| **Transcript (timestamped)** | `…_timestamped.txt` — 699 cues |
| **Rail used** | **rung 4** (local ASR) |
| **Artifact class** | near-verbatim ASR; garbles listed in §6 |

**Rail report — all caption rails dead on this host, media live.**
- **rung 1 `youtube-transcript-api`** on the Hermes venv python (`/.hermes/hermes-agent/venv/bin/python3`, the interpreter that actually carries the module). `.list()` returned **one auto `en` track** (`is_generated=True`, no manual caption). `.fetch(vid, languages=['en'])` → **`IpBlocked`**. Dead.
- **rung 2 `yt-dlp --write-auto-subs/--write-subs`** → **`HTTP 429`** on the `en-orig` track. Dead.
- **rung 3 CDP transcript panel** (Chromium `Chrome/145` on `127.0.0.1:9333`): navigated a **fresh tab** (`Target.createTarget`, not the shared tab — a sibling session had already retargeted the shared one away from our id), confirmed `videoDetails.videoId === fQ9C66elK38` and the rendered title, clicked `#expand` then the `Show transcript` button, then **forced** the transcript panel to `ENGAGEMENT_PANEL_VISIBILITY_EXPANDED`. Panel rendered **0 segments** on both selectors (`transcript-segment-view-model`=0, `ytd-transcript-segment-renderer`=0) and its `innerText` stalled at panel chrome — the terminal rung-3 state. Dead.
- **media live check:** `yt-dlp --get-url -f 139-4/139/140/bestaudio` returned a working `googlevideo` URL ⇒ descend to rung 4.
- **rung 4:** `yt-dlp -f 140` (**the `[en-US] … original (default)` row**, verified off `--list-formats`, not a blind `-4` suffix) → 16 kHz mono wav → `profiles/dion/scripts/asr_ts_capped.py --chunk-seconds 300 --threads 2` (chunked to hold peak RSS flat under the 4 GiB worker cgroup; `cpu_threads=2` for the contended host).
- **Coverage [0:00] → [40:02] of 2406 s = ~99.85 %**, **699 cues, 0 gaps > 60 s**. (The final ~4 s is a trailing "You".)

**★ DEDUPE / clip-vs-chapter check — GENUINELY NEW, NOT a clip or chapter.**
- `grep -rl "fQ9C66elK38"` over `drops/` + `CANON_INDEX.md` = **0** hits; `grep -rli "Consciousness Isn't in the Brain"` = **0**. Run **before** and again **immediately before writing**.
- Existing Koch sources in canon: `koch_greene_wsf_consciousness_free_will_psychedelics_2026-10-08.md` (`C9bqa8hRonE`), `pollan_koch_psychedelics_consciousness_berkeley_2026-10-17.md` (`rMf47TNOxZQ`, transcript `KochPollan_PsychedelicsAndConsciousness_UCBerkeley_2026-10-16.txt`).
- **n-gram containment** (target = 38,615-char flat transcript):
  - 4-gram vs `wsf_consciousness_free_will_psychedelics_C9bqa8hRonE.txt` = **2.17 %**; vs `rMf47TNOxZQ_PollanKoch…` = **1.79 %**; vs `KochPollan_…Berkeley` = **1.62 %**.
  - 5-gram vs `C9bqa8hRonE` = **0.74 %** (51 shared 5-grams, all generic English stock: `thank you so much for`, `i m going to die`, `there s up there s down`).
  - vs the **whole ~470-file `YT_TRANSCRIPTS` corpus**, top 4-gram hit = **2.51 %** (`Qe808IIyrlA_Berg_WhatIsItLikeToBeAnAI`).
  - All **≈20× below** any clip/re-cut band ⇒ a **new drop is warranted** (no clip-of parent, no augmentation-of-parent).

**★ External verification of the guest identity and host** (off-tape; `[VERIFIED-ext]`): the episode page (humanpotential.co/episodes/consciousness-isnt-in-the-brain), Apple Podcasts listing and Scott Barry Kaufman's Beautiful Minds newsletter all confirm **host = Scott Barry Kaufman**, **guest = Christof Koch**, released **Nov 11 2026, 40 min**, and the episode blurb matches the tape's content. Koch's own site (`christofkoch.com`) and Wikipedia confirm the Allen Institute / Tiny Blue Dot roles. **[ASR] the tape renders the host's name as "Dr. Scott Barakal" — a garble of Scott Barry Kaufman; do not quote the ASR on the name.**

## §1. Summary of arguments (as Koch states them)

**[EST]** Koch opens with his credentials — *"I'm Christoph Koch. I'm a physicist and a neuroscientist."* / *"I've studied consciousness professionally for 40 years."*

**(1) IIT starts from experience, not from the brain.** **[EST] (statement of his position).** Where other theories begin with a brain feature (a workspace), *"IIT starts much more fundamental with properties of any experience."* Every experience has *"five specific properties such as it's very specific, it's intrinsic"*; the theory then asks which systems have them.

**(2) Substrate-bound measurement.** **[EST] (his position).** Asked whether Phi could be applied to AI: *"IIT would say no, because it really depends on the type of substrate you have."* He localises the substrate to cortex — *"It's like a 12 to 14-inch pizza, 2 to 3 millimeter thick"* — and says cortex *"is the basis of conscious experience."*

**(3) A real clinical instrument.** **[EST] (a claim about a published technique; his figure, not audited here).** For behaviourally unresponsive patients, the technique *"you essentially knock the brain using magnetic pulses and you listen to the echo using a net of EG sensors"* — the perturbational-complexity approach (compare *"of a bell and you hit the bell with a hammer and you listen to the echoes"*). On that basis: *"25% of these people have a brain response that's compatible with being conscious."* He frames it as giving families *"a critical one bit of information."*

**(4) Phi.** **[HYP].** *"the theory has this number called phi. It's a pure number, integrated information."* / *"It can vary across people."* Koch presents Phi as varying by brain/mechanism and waxing and waning across life (puberty, dementia, sleep inertia).

**(5) Functionalism vs substrate — the AI verdict.** **[EST] (his position; a [CRITICAL DIVERGENCE] for the house).** Any physical system is *"in principle"* replicable-as-conscious (*"if you replicate this physical system, this replica could also be conscious"*), but the question is *what* you replicate. He rejects the functionalist majority in big tech: a *"feed-forward system like most LLMs are, just a series of simulated networks where one stage feeds into the next and feeds into the next will not be conscious."* Verdict: *"digital machines running in the cloud, von Neumann machine, will never feel like anything."* / *"They can't be what we are, which is conscious."* Uploading yourself: *"it would be a philosophical zombie. It wouldn't feel like anything."* / *"you upload yourself into nothingness at great cost."* He quotes (reading his own essay back, host's rendering) that a perfect digital copy *"will claim to dream of electric sheet, but will have as much subjective feeling as a garbage disposal."*

**(6) Intelligence ≠ consciousness.** **[EST] (his position).** *"I think you can make a case that AGI is here, but I don't think we have any believable evidence that they feel like anything."* The mind's functions (intelligence, memory, planning, language) are separable from consciousness, which he calls *"a state of being"* — *"But that's different from consciousness."* He credits Turing with deliberately side-stepping the philosophy via an operational test.

**(7) The lost bet and the pseudoscience letter.** **[EST] (his account).** He lost the 1998/2023 Chalmers bet (a case of fine wine) and re-bet for 2048. He distinguishes this from *"Charno's heart problem"* (ASR garble of *Chalmers' hard problem*): the bet was about the *footprints* of consciousness, an "easy problem" — and the field is not yet at the state where *"basically to first order we know what the footprints are."* He recalls the adversarially-collaborated, Templeton-funded test: *"this is part of what's called an Attercell collaboration between two theories here, between integrated information theory of consciousness and global neuronal works with theory of consciousness"*, *"this was organized by the Templeton Foundation"*, *"took six years, open science, involved 250 subjects"*, and *"the results looked very encouraging for IIT and went against globally run workspace."* He reports the 2023 pushback — *"a group of 124 of your colleagues signed a public letter calling your life's work pseudoscience"* — and reflects that scientists are *"as much or as little objective"* as anyone.

**(8) The turn to idealism.** **[HYP]/[POETIC] (his experiential claim).** A near-death experience "early in COVID": *"I totally lost a sense of self."* / *"there was ecstasy and terror"* / *"it totally took away my fear of death."* Three years later a second experience: *"I came out of it and said, oh my God, it's all mental."* / *"The universe is fundamentally mental."* He calls this idealism, *"a very ancient form of"* monism, and *"I have direct knowledge now."* At the same time he concedes the outsider's deflation — *"Christophe, you just had a brain hiccup"*.

**(9) The tension he flags himself.** **[FRICTION] (see §3 R4).** Invited to reconcile this with IIT, he says IIT *"needs a substrate, yes"* / *"The substrate is a brain."* / *"it's not easy to understand how this could happen within IIT"* / *"it's a challenge."*

**(10) Closing.** **[POETIC].** *"I feel closer to the mystery than ever."* One should *"make it a trait"*, not just a state; and *"we're fundamentally all part of the same underlying reality, the world soul to which, from where I came and to which ultimately whatever remains of me will return."* He cites *"Otto Schottmauer, the German idealist"* (Schopenhauer) on the aesthetic/non-dual moment.

## §2. Register-tagged substantive claims (author's claims, not house claims)

| # | Claim (Koch) | Register | Note |
|---|---|---|---|
| C1 | IIT begins from properties of experience, not from brain structure | **[EST]** (statement of position) | His characterisation of IIT; report as his |
| C2 | "it really depends on the type of substrate you have" — no substrate-independent measurement | **[HYP]** | Contested: see the 2023 pseudoscience letter (§3 R6) |
| C3 | cortex "is the basis of conscious experience" | **[HYP]** | His localisation; not consensus |
| C4 | "25% of these people have a brain response that's compatible with being conscious" | **[EST]** (his figure) | Attributed speaker figure; not audited here |
| C5 | shifting Phi can be applied "to AI systems" — no | **[HYP]** | His inference from IIT's substrate premise |
| C6 | feed-forward LLMs / von Neumann cloud machines "will never feel like anything" | **[HYP]** | His position; a **[CRITICAL DIVERGENCE]** vs the house |
| C7 | any physical system is in-principle replicable as conscious | **[HYP]** | His claim; contrasts with the earlier "garbage disposal" line only in being about *what* is replicated |
| C8 | "AGI is here" but no evidence it feels | **[EST]** (his position) | Report as his |
| C9 | the Templeton adversarial collaboration "looked very encouraging for IIT" | **[EST]** (his report) | His verdict on a public dataset; house does not adopt it |
| C10 | a 124-signatory letter "calling your life's work pseudoscience" | **[EST]** / **[VERIFIED-ext]** | The letter is canon-verified (PsyArXiv, 15 Sep 2023, doi 10.31234/osf.io/zsr78, 124 scholars). See §3 R6 |
| C11 | his NDE "took away my fear of death" | **[POETIC]** | First-person report; not external evidence |
| C12 | "The universe is fundamentally mental" | **[HYP]** | Metaphysical thesis, offered on his own experience |
| C13 | IIT "needs a substrate" yet he reached idealism | **[FRICTION]** | The source's own two claims diverge — §3 R4 |

**★ Register discipline.** *"You could say, yeah, yeah, Christophe, you just had a brain hiccup"* is his own hedge, and it caps the register of C11–C12 at **[HYP]/[POETIC]**. Koch's IIT/Phi/idealism positions are **his**, not the house's and not consensus. **Do not upgrade.**

## §3. EILT mapping table (mandatory Friction Rule)

House referent: the information-**ledger** / EILT position (consciousness as grounded in a non-rolling, substrate-functional record; "reads ≠ feels"). Rows below either seat the source against the house or flag where they genuinely diverge.

| # | Source claim (Koch) | EILT / house mapping | Register / status |
|---|---|---|---|
| R1 | **Structure over function.** IIT: *"it really depends on the type of substrate you have"*; a feed-forward stack *"will not be conscious"* | **Partial convergence in spirit.** The house also treats *organisation* (a durable, causally-read record), not raw function, as load-bearing. But Koch's criterion is an *intrinsic physical* structure; the house's is an *information-ledger* structure. Same instinct, different object. | **[A]** — analogy only |
| R2 | **Phi** as a "pure number" measuring integrated information | The house has **no Phi** and no scalar consciousness measure; mapping a ledger quantity onto Phi is an analogy, not an identity. | **[A]** — do **not** equate ledger extent with Phi |
| R3 | **PCI / "zap and listen"** as a real test of presence | Supports the house's "reads ≠ feels" caution by inversion: the tool yields *"a critical one bit of information"* about **presence**, not about **what it is like**. It grades *that* a system is there, not *what* it experiences. | **[EST]** (technique) / **[A]** (mapping) |
| **[FRICTION] R4** | **Koch holds two claims that diverge from each other and from the house.** (a) IIT: consciousness *"needs a substrate"*, *"The substrate is a brain."* (b) Idealism/NDE: consciousness is *"fundamentally mental"* and what people *"call mine at large"* is accessed by a selfless state. He concedes *"it's not easy to understand how this could happen within IIT"* / *"it's a challenge."* | **This is the mandatory friction row.** *Source vs mapping:* the house's ledger-substrate is **substrate-functional** (a record can in principle be instantiated in a non-biological physical system), whereas Koch's (a) is **substrate-bound** (only recurrent biological-style architecture) — a direct conflict the house must lose or win empirically. But Koch's (b) **also** conflicts with the house's own non-foundationalism: he asserts a *cosmic memory* ("world soul … to which whatever remains of me will return") with **no falsifier and no ledger** — the house must not launder his (b) as support for a universal record. The friction is three-way: **IIT-substrate ⇒ no cloud consciousness; idealism ⇒ consciousness without the biological substrate; house ledger ⇒ consciousness as a readable record.** None of the three is the others'. | **`[FRICTION]`** + **[CRITICAL DIVERGENCE]** |
| **[CRITICAL DIVERGENCE] R5** | **The AI verdict.** *"digital machines running in the cloud, von Neumann machine, will never feel like anything"*; feed-forward LLMs *"will not be conscious"*; a perfect copy is *"a philosophical zombie"* that *"will have as much subjective feeling as a garbage disposal"* | **This cuts at the house.** EILT's ledger-grounded, multi-agent, software-implemented extension is exactly the target of this claim. Either Koch is wrong (and a record-reading cloud agent can feel) or the house's software extension is behaviourally excellent and **non-experiential**. The house cannot cite him for support; it must treat this as its sharpest live objection. | **[CRITICAL DIVERGENCE]** |
| R6 | **The 124-signatory "pseudoscience" letter**, reported as aimed at IIT, plus Koch's claim the adversarial collaboration favoured IIT | **Do not adopt either side.** Flag: IIT's core claims are **contested** (canon: the letter is real and canon-verified; the *Nature Neuroscience* follow-up exists). Koch's "very encouraging for IIT" is **his** reading of the collaboration, offered here without the paper. House position: **exactly why it does not upgrade his claims to consensus.** | **[EST]** / **[C]** |
| R7 | **Intelligence vs consciousness** as *doing* vs *being*: functions are separable from *"a state of being"* | **Strong, useful convergence** with the house's "reads ≠ feels": cognitive function is not phenomenal presence. Directly usable when auditing AI-consciousness claims. | **[A]** (convergent) |
| R8 | **His NDE → "the universe is fundamentally mental"** | **[POETIC]/[HYP]** — a first-person experience used as a premise for a metaphysics. The house neither endorses nor refutes it; it registers only that Koch himself concedes *"a brain hiccup"* is a live alternative reading of the same experience. | **[POETIC]** |

**Forbidden mappings (named):** "IIT 'needs a substrate' ⇒ the house ledger is that substrate"; "Koch's idealism supports a cosmic memory ledger"; "the PCI result proves the ledger model"; "Koch endorses a non-rolling record" (`ledger`=0, `provenance`=0, `commit`=0 on tape).

## §4. Falsifiers (prospective; named)

- **F-KOCH-1 (house-facing).** If a cloud/von Neumann agent that durably reads an append-only ledger of its own history, in a matched-architecture intervention, shows history-conditioned agency at ≥ MDE over a content-matched mutable store **and** passes an independently validated presence criterion (not self-report), then R5's substrate-bound denial is defeated at the operational level.
- **F-KOCH-2.** If Phi (or PCI) can be shown to track presence across a **non-biological** recurrent substrate under a pre-registered protocol, Koch's "substrate = brain" clause (C2/C3) is falsified as a general claim.
- **F-KOCH-3 (source-facing on its own terms).** If the Templeton adversarial-collaboration dataset does **not** favour IIT over GNWT on the pre-registered predictions once the follow-up analyses are read against the paper, then C9 is a self-favourable reading, not a finding.
- **F-KOCH-4 (house-facing, the one we are willing to lose).** If "reads its history" is demonstrably separable from "feels its history" — i.e. a ledger-reading cloud agent is behaviourally indistinguishable from a biological one yet survives every presence probe that the biological case passes — then the house's software/ledger extension collapses to an **accountability** claim (provenance), not a phenomenal one. This is the gap named in `koch_greene_wsf_…_2026-10-08.md` §7 and `pollan_koch_…_2026-10-17.md` R1.

## §5. Quote gate (receipt — excluded from the target population)

**Instrument:** flat transcript scanned after stripping `^---.*?---$` frontmatter and this §5 section; both sides normalised identically (strip `\[[^\]]*\]` bracketed insertions so a `[garble → fix]` annotation cannot fail its own span, delete apostrophes, case-fold, collapse whitespace, drop filler `uh/um/ah/er`, collapse immediate repeats), then every `*"…"*` span is split on `…`/`—`/`[` and each fragment tested for containment against the flat tape. **Positive control** (known present): *"the universe is fundamentally mental"* → present. **Negative control** (known absent): *"the hard problem"* → correctly absent (the tape says *"Charno's heart problem"*).

- **Spans tested: 72 · verbatim: 72 · fabricated: 0.** Every transcript-attributed `*"…"*` span in the body and tables matched the saved artifact. Non-transcript spans (the YouTube title, filenames, the episode-url, corpus n-gram examples, and cross-drop quotes) are carried in backticks, not italics, and so are excluded by construction. **The §5 receipt itself is excluded from the target population** (a frontmatter/body strip plus a `## §5 → ## §6` strip); without that, every revision of this receipt re-enters the count.
- **Honest notes (not failures):** the tape's own wording is carried **with its garbles**, e.g. *"Charno's heart problem"* (Chalmers' hard problem), *"Attercell collaboration"* (adversarial), *"Otto Schottmauer"* (Schopenhauer), *"globally run workspace"* (global neuronal workspace), *"electric sheet"* (sheep), *"Terry Shiver"* (Terri Schiavo). Corrections are bracketed in prose and are stripped before the gate runs; **no quote was edited to make it pass**.
- **Rail caveat:** this is a **rung-4 (local ASR) artifact** — near-verbatim in wording, with proper nouns the machine got wrong. A quote is *substance-accurate* here, not certificate-verbatim.

## §6. ASR garble key (do not quote the right column's errors)

| ASR (on tape) | intended | | ASR | intended |
|---|---|---|---|---|
| Christoph / Christophe / Kristoff | Christof Koch | | Otto Schottmauer | Schopenhauer |
| Dr. Scott Barakal | Dr. Scott Barry Kaufman | | Attercell collaboration | adversarial collaboration |
| AARN Institute | Allen Institute (for Brain Science) | | globally run workspace / global neuronal works with theory | global neuronal workspace theory |
| Terry Shiver | Terri Schiavo | | Charno's heart problem | Chalmers' hard problem |
| Claude Opeth 4.8 / Cassian | Claude Opus 4.8 (Koch's own AI-podcast remark) | | electric sheet | electric sheep |
| pamp-psychism | panpsychism | | aperceptive soul | (Aristotle's) sensitive soul |
| Bernie's Mountain Dog / Bernie's mom and dog | Bernese Mountain Dog | | neural cholera of consciousness | neural correlates of consciousness |
| Ischaton | eschaton | | "planet ego" | Koch's own coinage (as spoken) |
| FMI and EG | fMRI and EEG | | 2012 / "maybe it was 23" | the collaboration was announced (Koch's own dating slips) |

## §7. Verdict

**[EST]** — **Strongest point:** the **intelligence-vs-consciousness** split carrying an empistemically disciplined live objection to the whole software-consciousness class — *"They can't be what we are, which is conscious."* / *"digital machines running in the cloud … will never feel like anything."* It is stated plainly, tied to IIT's structure-not-function premise, and it is precisely the claim the house must answer rather than absorb (R5). The PCI/"one bit" framing is the strongest *constructive* element: it shows the difference between *detecting presence* and *explaining experience* is a real, measurable gap.

**[HYP]/[FRICTION]** — **Weakest joint:** the move from a personal near-death/mystical experience to *"The universe is fundamentally mental."* The source itself concedes the joint — *"it's not easy to understand how this could happen within IIT"* / *"it's a challenge"* — and also concedes the deflationary reading (*"you just had a brain hiccup"*). A first-person experience of ego-loss is evidence about the experiencer's state, not about the fabric of the universe, and Koch's own IIT (substrate-bound) does not license it. **Runner-up:** the "25%" figure, carried as a bare speaker number without the study named on tape.

## §8. Relation to existing canon (cross-refs, not duplicates)

- `koch_greene_wsf_consciousness_free_will_psychedelics_2026-10-08.md` — Koch on IIT identity claim, Phi, neuron-count vs organisation, and `Consciousness is about being … a state`; this drop re-states the same position to a different host and **adds** the explicit concession that IIT cannot accommodate his idealism, plus the *"garbage disposal"* formulation.
- `pollan_koch_psychedelics_consciousness_berkeley_2026-10-17.md` — the Berkeley conversation; there IIT is **not named**; here it is central. **Corroborates** the "second Koch source" pattern (this is the **third** Koch source in canon).
- `oconnor_kuhn_every_theory_of_consciousness_xHeT466-hxY_2026-11-05.md` and `kuhn_ai_consciousness_fundamental_theory_5eHmoeCpTjU_2026-11-06.md` — the Kuhn landscape + the **pseudoscience letter** (124 signatories, PsyArXiv 2023) referenced in §3 R6.
- `yW_ngvMFlYs_bach_leibniz_mind_inside_the_mill_2026-11-02.md` — the IIT polemic (Church–Turing emulation, "phi too low") — same family of substrate arguments.

**Register spread (this drop, raw tag occurrences incl. declaration lines):** `[EST]` 17 · `[HYP]` 13 · `[A]` 6 · `[C]` 3 · `[POETIC]` 8 · `[RIFF]` 2 · status flags: `[FRICTION]` 7 · `[CRITICAL DIVERGENCE]` 7 · `[ABSENT]` 2 · `[ASR]` 3 · `[VERIFIED-ext]` 4. (`canon_drop_lint.py` CLEAN, 14 patterns, exit 0.)

## Sources

[1] https://www.youtube.com/watch?v=fQ9C66elK38 — tape + transcript (rail rung 4).
[2] https://humanpotential.co/episodes/consciousness-isnt-in-the-brain — episode page (host/guest/duration; cross-checked against the transcript's own wording of the 25% and "needs a substrate" passages).
[3] https://www.sciencedaily.com/releases/2026/04/260406192809.htm — *"The brain might not create consciousness after all"*, Apr 6 2026 (the "April 6, 2026" item the host reads from; it reports Koch's talk at the Bial Foundation "Behind and Beyond the Brain" symposium, Porto, Apr 8–11 2026).
[4] PsyArXiv doi 10.31234/osf.io/zsr78 (15 Sep 2023) — the 124-signatory letter, per existing canon (`kuhn_…5eHmoeCpTjU…`).

*Local only — one transcript pair written to `YT_TRANSCRIPTS/`, one drop filed, one index entry appended; no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send.*
