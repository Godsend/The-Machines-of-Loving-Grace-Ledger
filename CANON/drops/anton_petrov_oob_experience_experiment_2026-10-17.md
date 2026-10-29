---
epistemic-registers: T=theorem H=hypothesis E=empirical A=analogy C=conjecture M=myth/poetic O=opinion F=falsifier
rule: no tag = treat as MYTH (do not build on it)
source: Anton Petrov, "Out of Body Experience Experiment Makes Some Strange Discoveries" (YT hCGp_36Qh1k, 2026-10-16) + primary paper Weiler, Abraham, Acunzo & Hermansson 2026, EXPLORE 22(6):103506
date: 2026-10-17
canon-id: CANON-2026-10-17-PETROV-OBE-WEILER-NULL
tags: [obe, out-of-body, veridical-perception, remote-viewing, dops, uva, weiler, text-embeddings, tpj, blanke, anterior-precuneus, parvizi, vesuna, ketamine, dissociation, popularizer-audit]
---

# Canon Drop — Anton Petrov on the UVA Out-of-Body Trial: A Clean Null, Faithfully Reported, Then Wrapped in Loose Neuroscience

**Filed by:** Dion · **Status:** Working draft (pre-adversarial)

## 0. Sources & provenance

- **Video:** Anton Petrov, *Out of Body Experience Experiment Makes Some Strange Discoveries*, YouTube `hCGp_36Qh1k`, uploaded 2026-10-16, 1046 s. Identity checked with yt-dlp metadata.
- **Transcript:** `/data/SecondBrain/Canon/YT_TRANSCRIPTS/hCGp_36Qh1k_AntonPetrov_OOBExperienceExperiment_2026-10-16.txt`
  - **Method:** youtube-transcript-api was IP-blocked. yt-dlp subtitles returned HTTP 429. On CDP :9333 the watch page loaded but rendered no "Show transcript" button (0-char panel).
  - **Fallback used:** yt-dlp audio (m4a) → **faster-whisper small.en**, run locally on CPU. This produced 240 segments covering 0:00–16:21 (full video through the end card).
  - This is an ASR transcript. Line refs below are `[t=seconds]`.
- **Primary paper (read: abstract + introduction + section snippets; full text is behind the Elsevier paywall):**
  - **Citation:** Weiler M, Abraham D, Acunzo DJP, Hermansson N. *Assessing correspondence between subjective reports and visual targets during attempted out-of-body experiences.* **EXPLORE (NY)** 2026 Nov–Dec; 22(6):103506.
  - **IDs:** **PMID 42617381** · **DOI 10.1016/j.explore.2026.103506** · PII S1550-8307(26)00194-1.
  - **Dates:** received 2026-06-23, accepted 2026-08-07.
  - **Affiliations:** Weiler and Acunzo, UVA Psychiatry/Division of Perceptual Studies (DOPS). Abraham, Entangled Labs (Irvine). Hermansson, Statistics, University of Auckland.
  - **Funding & COI:** funded by a "small philanthropic gift" (an undisclosed donor per the UVA press release). No COI declared.
  - Metadata comes from NCBI efetch XML. Abstract and intro come from the PubMed and ScienceDirect preview pages.
- **Secondary (press, used only where marked):** UVA Health press release 2026-09-09; crbcnews/geo.tv summaries. These carry the details that are **not in the abstract**: the EEG, the three-room layout, the 60–90 min sessions, the screen facing the wall, and the true-target ranks of 16th–92nd.
- **Adjacent studies Petrov invokes (checked):**
  - Blanke et al. 2002 *Nature* 419:269.
  - Blanke et al. 2005 *J Neurosci* 25:550.
  - Lyu…Parvizi 2023 *Neuron* (doi 10.1016/j.neuron.2023.05.013), plus the Stanford Medicine release of the same paper.
  - Vesuna…Deisseroth 2020 *Nature* 586:87.
- **Unread:** the Methods/Results body of the paper, and in particular the per-participant numbering, room-arrangement logs and EEG analysis. Claims that depend on these are tagged as press-sourced or unverified.

---

## 1. What the STUDY actually found (abstract-grounded)

[E] **Design.**
- 21 people affiliated with an OBE-training institute took part. The paper's Participants snippet identifies it as the **International Institute of Projectiology and Conscientiology (IIPC), Brazil**; 40 people were screened.
- Each attempted to perceive a target picked at random from a standardized database of 100 images. The target was shown in a separate, inaccessible room and was unknown to both participants and researchers.

[E] **Who produced usable data.**
- **10 of 21 reported an OBE.**
- **13 gave target descriptions for analysis.** Per the UVA release, the 13 include non-OBE "mental screen" reporters.
- So the analyzed set is **not** "OBE trials". It mixes OBE and non-OBE reports.

[E] **Scoring method.**
- Each description and the 100 target captions were turned into embeddings by a pretrained language model.
- Cosine similarity was computed against all 100 candidates.
- The primary metric was the true target's rank against the within-trial decoys. Standardized z-scores were a secondary, descriptive metric.

[E] **Primary result: null.**
- No individual trial was significantly above chance.
- The combined rank-based test over all 13 trials also showed no above-chance performance.
- Press-sourced detail [E, secondary]: true-target ranks ran from 16th to 92nd.

[E] **The authors' own caveat on the method.**
- Control analyses showed the pipeline finds correct targets when semantic correspondence is present.
- But these controls "do **not** establish sensitivity to naturalistic human language."
- So the null is partly a null **on the instrument**.

[E] **Room-2 anecdotes.**
- Two participants spontaneously gave accurate details about where the experimenters were and what they were doing in an adjacent room.
- The authors frame these as having possible "**methodological value**" that warrants systematic investigation. They are explicitly **not** evidence.
- Press-sourced [E, secondary]: the details came out "during interviews afterward". Trial records confirmed them, and organizers state there was no way to see the researchers.

[E] **Authors' conclusion.** "the target-identification results did not support anomalous cognition."

[E] **Authors' broader stance (context, not a finding).**
- The intro states that ESP during OBEs, if real, "would suggest that some aspect of mind or consciousness operates beyond … conventional brain-based accounts."
- The same group published a 2026 *Front Psychol* paper arguing that sterile fixed-target designs **misalign with the OBE state**, and the Discussion situates this null inside that critique.
- [O] This is a sympathetic DOPS group reporting a null on its own preferred hypothesis. That earns the null credibility. It also means the next move ("the targets were wrong") is already pre-built.

---

## 2. What Petrov says vs. what the study says

| # | Petrov's claim [t] | Check against source | Verdict | Tag |
|---|---|---|---|---|
| P1 | Led by Marina Weiler, UVA Division of Perceptual Studies; "double-blind" [151–162] | Correct. The paper says targets were unknown to participants and researchers ("fully blinded" in Discussion) | Accurate | [E] |
| P2 | Three rooms: practitioners on **EEG** in Room 1, researchers in Room 2, laptop facing the wall in Room 3; 100-image database [194–224] | 100 candidates, random, inaccessible room: in the abstract. EEG, three-room layout, screen-to-wall: **press only**; not visible in the abstract or snippets | Plausible, partly unverified | [E] (100 targets) / unverified (EEG, layout) |
| P3 | AI compared descriptions against 100 candidates "to eliminate any possible bias" [238–254] | Embedding/cosine design matches. "Eliminate any possible bias" overstates it: the authors say their controls **don't** establish sensitivity to natural human language | Slight overclaim (sells the instrument as stronger than its authors do) | [E] design / [O] overclaim |
| P4 | "All of the participants failed completely… zero evidence" [263–278] | Null per-trial and pooled: correct. But **only 13 of 21 produced analyzable descriptions**, and only 10 reported an OBE. Petrov never gives n=21, 10 or 13 anywhere in the video | Direction accurate; **sample size omitted** | [E] |
| P5 | Two participants gave unprompted, accurate descriptions of researchers in Room 2; "participant 7" (left at computer, far corner reading a book) and "participant 13" (right taking notes, left at computer) [291–332] | Matches the abstract and UVA release in substance. **Participant IDs, and the claim that the arrangement "had not been used in previous sessions" [320–326], are not in any text I could access.** They are probably from the paywalled body; unverified here | Substance accurate; specifics unverified | [E] substance / unverified specifics |
| P6 | "Anecdotal… cannot be counted as formal proof" [337–353] | Matches the authors' framing exactly | Accurate, and to his credit | [E] |
| P7 | Weiler's next study will use dynamic or emotional targets, e.g. a distinctive t-shirt [362–388] | Matches the UVA release (distinctive or colorful clothing) | Accurate | [E] |
| P8 | Opening frame: neuroscientists studying OBEs in labs "discovered" that the mind isn't leaving the room; the self is an active reconstruction [91–120] | **Misattribution by juxtaposition.** The Weiler study tested veridicality, not mechanism, and its authors lean non-local. The "self = reconstruction" result comes from Blanke/Parvizi-type work, which this study neither tested nor claims | Framing conflation | [O] |
| P9 | TPJ integrates proprioceptive, vestibular and visual streams; integration failure → OBE (Blanke) [418–580] | Fair summary of Blanke 2005 (*Neuroscientist*) multisensory-disintegration model | Accurate | [E] (Blanke) / [H] (as general OBE mechanism) |
| P10 | "By stimulating this region through **magnetic** stimulation, OBE can be physically induced… done several times" [584–611] | **Wrong instrument and overstated count.** OBE induction was by **intracranial electrical** stimulation of the right angular gyrus in **one** epilepsy patient (Blanke 2002 *Nature*). **TMS** over TPJ (Blanke 2005 *J Neurosci*) *impaired mental own-body imagery*; it did not induce OBEs | **Misstatement** | [E] corrected |
| P11 | Stanford stimulation of anterior precuneus in "unconscious" patients → flying/falling while "aware and awake" [622–649] | Lyu/Parvizi 2023: 9 **awake** epilepsy patients with implanted electrodes. aPCu stimulation → floating (right) / falling (left), depersonalization in 3. Parvizi explicitly: "**Our subjects did not report [an OBE] at all.** They still felt like they're inside their bodies." | Content right; "unconscious" self-contradicts; **presented as an OBE anchor when its own PI says it isn't OBE** | [E] corrected |
| P12 | Ketamine and anesthetics cause slow rhythmic oscillations "inside this APC", unplugging bodily signals [658–674] | Vesuna 2020: ketamine/PCP → **1–3 Hz rhythm in layer-5 retrosplenial cortex** (mouse) / **deep posteromedial cortex** (one human patient); RSC uncouples from most regions. That is neighboring posteromedial cortex, **not the aPCu**, and "a lot of other anesthetics" is wrong: in the mouse screen the rhythm was specific to *dissociatives* | **Conflation of two studies/regions** | [E] corrected |
| P13 | "We actually seem to understand how OBE works pretty well" [677–687] | Three partial, small-n, mostly patient-based findings, at different nodes, none fully reproducing the classic elevated-viewpoint OBE except Blanke's single patient | Overclaim | [O] |
| P14 | Rubber-hand illusion: felt ownership, even pain at a hammer strike [693–740] | RHI ownership is robust (Botvinick & Cohen 1998). "They feel that it's painful" overstates: the standard measures are threat-evoked SCR/anticipatory arousal, not reported pain | Mild overclaim | [E] (RHI) / [O] (pain) |
| P15 | "These experiments **definitively** show… self-consciousness is built from real-time sensory integration"; "**empirical proof**… not some kind of a soul"; "I think therefore I am… incorrect" [740–872] | None of the cited work tests souls or Descartes. Inducing an *experience of displacement* by perturbation does not show that the *experience of location* is all there is. That is the strong-physicalist reading, legitimate as a view and not "proof" | Register inflation ([O] presented as [E]) | [O] |
| P16 | Clinical upside: targeted anesthetics sparing vital functions; TMS for depersonalization disorder [792–848] | Speculative translational claims; no cited trials | Speculation | [C] |
| P17 | "Scientific consensus is that [OBE]… can be physically induced and seems to be the result of a kind of disconnection" [910–921] | Induction-by-perturbation is well supported. "Consensus" on *all* OBEs, including the spontaneous, NDE and trained ones studied by Weiler, is overstated. The trained IIPC practitioners in this very study are the population the lab-induction work did not test | Overgeneralization | [O] |

**Net on the headline study:** Petrov gets the Weiler result **right in direction and in caveat**: null primary, Room-2 anecdotes flagged as anecdotal, the next design accurately relayed. He does **not** inflate the anecdotes into evidence, unlike geo.tv-style coverage ("something happened… researchers admit they cannot explain"). His omissions:
- the sample sizes (21 → 10 OBE → 13 analyzed);
- the fact that the analyzed set mixes non-OBE reporters;
- the believer-institute recruitment (IIPC);
- the post-session-interview timing of the anecdotes;
- the authors' own caveat on instrument sensitivity.

**Net on the wraparound:** the second half is where the errors are. It has three factual slips (P10 TMS vs. intracranial electrical stimulation; P11 aPCu presented as an OBE site against its PI's statement; P12 Vesuna's retrosplenial rhythm relocated to the aPCu) and one register inflation (P15 "empirical proof… not a soul").

[O] **Continuity with the house's prior Petrov drop (2026-10-08, two-organ brain):** same signature. The headline paper is relayed faithfully. Adjacent studies are compressed and blended (there: cerebellum grouped into the hindbrain against Loh's stated uncertainty; here: three posteromedial/TPJ studies fused into one "OBE anchor" story). The closing paragraph upgrades register. **House rule for this channel: trust Petrov on the cited paper's headline; re-verify every adjacent study he chains to it.**

---

## 3. Cross-check against existing canon — and the Friction Rule

### Friction 1 (primary, cuts at us): our own veridical-OBE tag is inflated, and this study is evidence against it
- **The filed claim:** `nde_eleusinian_reset_eilt_graph_theory_filter_collapse_2026-10-01.md` §2 row 1 files "**Veridical Out-of-Body Perception** — Flatline EEG patients accurately describing resuscitation tools…" as **[EST-EMPIRICAL]**. It interprets the claim as "Perception is non-local; the brain is a localizer, not a generator."
- **What this study shows:** a blinded, randomized, computationally scored target test, run by a group *sympathetic* to that interpretation on trained practitioners with ~19 years of mean practice, returns a **null on its primary outcome**.
- [E] This study does **not** refute veridical NDE perception during cardiac arrest. It is a different population (healthy trained practitioners, not arrest patients) and a different state.
- [E] But the canon row cites no controlled study at all. The prospective arrest studies the paper's own reference list cites (Parnia AWARE 2014, AWARE-II 2023) also produced **no confirmed visual-target hits**.
  - AWARE-II (*Resuscitation* 191:109903) had 567 arrests → 53 survivors → 28 interviewed. **None** explicitly recalled the hidden tablet image or the auditory stimuli, and none picked the image from 10.
  - One survivor reported OBE-perspective perception of the resuscitation but did **not** identify the image. One identified the auditory stimulus only implicitly, by forced choice from three fruit names.
  - AWARE-I (2014) had one verified auditory/visual-awareness case, but no shelf-image hit.
  - Checked via the Agudo et al. *J Near-Death Stud* commentary and the SPR Psi Encyclopedia summary. The AWARE primaries were not re-read tonight.
- [F] **Correction owed on the 10-04/10-01 NDE cluster:** that row should be **downgraded from [EST-EMPIRICAL] to [C]** ("anecdotal case reports exist; controlled target tests to date are null"). The "non-local perception" interpretation should be split out as **[H]**. This is the register-inflation bug in its plainest form, and per the register-discipline rule it should be fixed **on the source file**, not only here. *(Not done in this pass. Flagged for the parent / Gene.)*

### Friction 2 (cuts at the house in the other direction): the internal-filter model doesn't get a free win
- **The house prediction:** `mishlove_closer_to_truth_afterlife_internal_filter_critique_2026-09-28.md` §F says "veridicality residue… will remain strictly orthogonal to filter-state variables and **fail under pre-registered, blinded target protocols**."
- [E] The primary outcome is consistent with that prediction.
- [E] The Room-2 anecdotes are *exactly* the "informational residue" class that drop admits the internal-filter model "does not explain."
- [O] The honest house position is neither "debunked" nor "anomaly":
  - the anecdotes are **post-hoc, unplanned, n=2, gathered in post-session interviews**, from a design where the researcher room was the one room the participants could plausibly model (two researchers, a computer, a book or notepad: a small, guessable state space);
  - without the base rate (how many participants described Room 2 *wrongly*, or at all), the hit rate is undefined.
- [F] It becomes evidence only under the authors' own proposed protocol: pre-registered, randomized, distinctive Room-2 states (clothing, objects), scored blind, with misses counted.

### Friction 3 (anatomy, cuts at the anterior–posterior / ketamine thread)
- **The canon claim:** `anton_petrov_human_brain_two_separate_organs_2026-10-08.md` §2C and `anterior_posterior_myelination_asynchrony_…_2026-10-03.md` model ketamine dissociation as "the physical uncoupling of the **anterior serial narrator** from the posterior somatic/perceptual field" (prefrontal release).
- [E] What Petrov gestures at, and Vesuna 2020 actually shows, is different. Dissociation is driven by a **posterior** pacemaker: an HCN1-dependent 1–3 Hz rhythm in retrosplenial/deep posteromedial cortex that **uncouples that posterior node from most other regions** (inverse correlation with frontally projecting thalamic nuclei).
- [E] Lyu/Parvizi place bodily self-location in the **anterior precuneus**, also posteromedial, distinct from but connected to the DMN.
- [O] So the two best-identified causal nodes for disembodiment and dissociation sit **inside the house's "posterior GPU"**. They are not on an anterior–posterior bridge.
- [H] The canon's "GUI–GPU uncoupling" story is not falsified, since the RSC–frontal-thalamus decoupling is a long-range uncoupling. But its *locus of control* is reversed: the posterior node drives the state, rather than an anterior clamp being released.
- [F] Discriminator: if ketamine dissociation is anterior-clamp release, frontal perturbation alone (no posteromedial rhythm) should reproduce it. Vesuna's HCN1 knockout in RSC **blocks** ketamine's dissociation-like behavior (mouse), which already leans against the anterior-release reading.

### Support (genuine, bounded)
- [E] The `dual_aspect_monism_bare_commit_…_2026-10-08.md` account treats the experiential "now" as distinct from its contents. Self-*location* is perturbable by focal stimulation (Blanke, Parvizi). Parvizi's own line, "Electrically stimulating the default mode network doesn't do anything at all to one's sense of self," is consistent with a split between the narrative self and the bodily/point-of-view self.
- [A] The bare-commit account is compatible with this, but only as an analogy: these studies manipulate the *contents* (where I am), never the bare event. Nothing here bears on dual-aspect monism either way. [O] Petrov's "not a soul" line is just as unearned as an "it proves the soul" line would be.

---

## 4. Verdict (opinion)

[O] **Strongest point (study):** a group that believes OBE veridicality is possible pre-specified a computational, blind, 100-decoy rank test, ran it on its most favorable population, got a null, and published the null with the "spontaneous" reports carefully fenced off. That is better behavior than most of the psi literature the house has audited this week (cf. Radin 10-13, Mishlove/Freedman 10-15, where the a priori test was also null, p=.31).

[O] **Weakest joint (study):**
- n=13 analyzable, mixed OBE and non-OBE, with an instrument whose sensitivity to real human descriptions the authors admit is unestablished. The null is **underpowered and instrument-limited**, not decisive. It is a clean "no evidence of", not "evidence of no".
- The anecdotes were collected outside the protocol from believer-institute participants, with no reported base rate.
- [O] The pre-built escape hatch ("fixed targets misalign with the OBE state", the authors' own Front Psychol 2026 paper) is the classic psi-moving-target move. The authors would need to pre-register the Room-2 protocol *and its failure criterion* before that critique earns credit.

[O] **Petrov's coverage: accurate on the paper, oversold on the frame.**
- He is one of the few popularizers this cycle who did **not** inflate the anomaly. He says plainly that the target test failed and the anecdotes aren't proof.
- He omits every number that tells the viewer how small the study is.
- He then hangs the null on a neuroscience scaffold with three factual slips (TMS ≠ intracranial stimulation; aPCu is not an OBE site per its PI; Vesuna's rhythm is retrosplenial, not aPCu).
- He closes with "empirical proof… not some kind of a soul… you and I are basically computer simulations." That is a materialist **opinion** presented in an [E] register.
- The study he's covering supports none of that. It only failed to support the opposite.

**Grade:**
- headline relay **A−**;
- adjacent-science accuracy **C**;
- register discipline in the closing frame **D**.

---

## 5. Pre-registered falsifiers / follow-ups

- [F] **F-OBE-1 (Room-2 replication).** A pre-registered replication along these lines would turn the anecdotes into evidence:
  - randomized distinctive researcher-room states, drawn from ≥20 options, set after the participant is sealed in;
  - every post-session statement about Room 2 scored blind;
  - misses counted;
  - α = .01.

  A result at chance would close the residue for this population.
- [F] **F-OBE-2 (instrument validity).** Before the next null is read as substantive, the embedding pipeline must recover above-chance ranks on **naturalistic** descriptions produced by sighted participants briefly shown the target (the authors' own gap).
- [F] **F-NDE-row (canon hygiene).** The 2026-10-01 "[EST-EMPIRICAL] veridical OBE" row stays inflated until someone cites a controlled, blinded target hit. If none is produced on re-audit, downgrade on source.

---

*Filed by Dion. Paper read: abstract, intro, Participants/Results/Discussion snippets (full text paywalled). Transcript: faster-whisper ASR (all API/caption/CDP rungs blocked). Claims marked unverified were not invented: they are Petrov's and are flagged as his.*
