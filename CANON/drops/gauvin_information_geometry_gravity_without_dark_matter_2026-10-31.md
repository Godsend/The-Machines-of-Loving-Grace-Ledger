---
title: "Canon Drop — Shoshauna Gauvin, *Rethinking Gravity: Can Einstein's Equations Explain Galaxies Without Dark Matter?* (IPI Talk, 2026-10-31)"
date: 2026-10-31
filed_by: Dion
channel: Information Physics Institute
video_id: J-eq7DHxTpw
source_type: live-streamed-talk (ASR transcript, rail 4)
epistemic-registers: "EST=established/reported observation · HYP=hypothesis/proposal · A=analogy · C=conjecture · POETIC=poetic · RIFF=riff"
register-rule: "no tag = treat as unverified; physics claims get [EST] ONLY where the talk reports an existing verified observation, never for a proposal"
status: "Working draft — single-source intake, no adversarial pass yet"
---

# Canon Drop — Shoshauna Gauvin, *Rethinking Gravity: Can Einstein's Equations Explain Galaxies Without Dark Matter?*

**Date:** 2026-10-31 · **Filed by:** Dion
**Source (VERIFIED):** https://www.youtube.com/watch?v=J-eq7DHxTpw
**Channel:** Information Physics Institute · **Speaker:** Shoshauna Gauvin (Univ. of Waterloo, Perimeter Institute assoc. member; spelling from the video DESCRIPTION — ASR renders it "*Shoshana Gavin* / *Shoshana Govan* / *Sarshoana*")
**Format:** YouTube **live stream** (aired 2026-10-31, stream start 17:06 UTC); YouTube-recorded duration **3120 s (52:00)**; recorded at **post_live**.
**Transcript / Text:** `/data/SecondBrain/Canon/YT_TRANSCRIPTS/J-eq7DHxTpw_gauvin_rethinking_gravity_no_dark_matter_2026-10-31.txt` (flat, **42,523 chars / 7,067 words**) + `..._timestamped.txt` (**51,576 chars**, 823 cues)
**Filing scope:** local only — no GitHub push, no NotebookLM ingest, no Drive mirror, no TTS, no outbound send.

---

## 0. Rail log (extraction ladder)

| Rung | Rail | Result |
|---|---|---|
| 0 | Published transcript in DESCRIPTION | **FAIL** — description carries only the **preprint DOI + abstract**, no written transcript. |
| 1 | `youtube-transcript-api` (system python3) | **FAIL** — `TranscriptsDisabled`. `.list()` exposes **only `live_chat`**; no auto and no manual caption track exists. |
| 2 | `yt-dlp --write-auto-sub` / `--list-subs` | **FAIL** — yt-dlp: *"J-eq7DHxTpw has no automatic captions"*; available subs = `live_chat` (json) only. |
| 3 | CDP `:9333` transcript panel | **NOT EXERCISED (definitionally empty).** CDP port was live (`Chrome/145` responded on `127.0.0.1:9333`), but the video exposes **no caption track of any kind**, so a "Show transcript" panel can have no content. Not opened. |
| 4 | `yt-dlp --live-from-start` audio + `faster-whisper small.en` (cpu / int8) | **WON.** Captured the whole stream from its start (live DVR window intact): `live.m4a` 50.2 MB, ffprobe **3105.0 s**. ASR: 823 segments, ~4.3× realtime. |

**Coverage:** ASR span **0:00 → 0:51:45 (3105 s) of the 3120 s YouTube duration = 99.5 %**. The ~15 s shortfall is stream head/tail framing, not missing speech. **No caption text was ever available**; every quoted line below is my own ASR of the audio and is therefore subject to ASR error — repairs flagged `[ASR: …]`, unresolved garble left as-is.

**IMPORTANT — this transcript is machine-generated, not a YouTube caption track.** A quotation verified against the saved artifact verifies what the *audio-local ASR* produced; it does not verify YouTube's own captioning (which does not exist for this video).

---

## 1. Identity, packaging, and what the talk actually is

- **Title (verified):** *"Rethinking Gravity: Can Einstein's Equations Explain Galaxies Without Dark Matter?"* — a **question**, so not strictly inflated; the answer the talk gives is effectively *yes*.
- **Speaker's own framing of the novelty** `[00:04:25]`: *"My answer is that compared with the general relativity, I'm able to show an exceptionally strong statistical significance in out-predicting galaxy rotation curves, CMB acoustics and other phenomenon compared with general relativity."* `[HYP]` — this is the **headline claim of an UNPUBLISHED preprint**, not an independently verified result.
- **What it is, in one line:** an information-geometry **reformulation of Einstein's equations** (relative-entropy / BKM-metric based) in which a **modified stress-energy** term, sourced by occupied modes + connected correlations of ordinary matter, reproduces galaxy-rotation-curve, CMB-acoustic, and (claimed) cosmic-acceleration behaviour **without a dark-matter particle**. Modified-gravity-adjacent in effect (MOND-family territory), though the speaker frames it as a *matter-description* correction rather than a modification of the gravitational law.
- **Publication status, in the speaker's own words** `[00:48:48]`: *"By paper, it's currently just waiting on archive to be posted, but it's also available on pre-prints from MDPI, the journal."* ⇒ **unrefereed**; no paper title, journal, or DOI is spoken on camera. The **preprint DOI `10.20944/preprints202609.2275.v2` appears only in the video DESCRIPTION**, not in the talk.
- **No paper titles, author citations, or numeric references are spoken.** She denotes her two papers only as *"one or two"* `[00:04:17]` and names exactly one external source by name+year: **"Ted Jacobson in 1995"** `[00:23:38]`. (Per the ZERO-FABRICATION rule, no other reference is supplied here.)

### Title/description audit
- The **description's abstract** hardens slightly beyond the talk: it states the reformulation *"results in equations resolving the field which we incorrectly attribute to so called 'dark matter'"* — the word **"incorrectly"** is the packaging's assertion; on camera the speaker's register is more careful (she states a *statistical* outperformance and repeatedly lists open requirements). `[HYP]`
- **Host has not verified the work.** On-air the organiser says `[00:49:48]`: *"It's very interesting work, complicated"*, and `[00:50:18]`: *"to follow up on the presentation, slides going quite fast. And there is a lot of mathematical detail in there. It's not easy to follow."* He states he still needs to read the manuscript. ⇒ **no independent check occurred in the recording.**

---

## 2. Claim inventory (register-tagged)

> Register set declared in frontmatter (six tags). Row-status flags (`[CRITICAL DIVERGENCE]`, `[ASR]`, `[RE-TREAD]`) are **not** registers.

### 2a. Established / reported observations the talk relies on
| # | Claim (as spoken) | Tag |
|---|---|---|
| E1 | Galaxy-scale gravity *"appears to be too weak to hold onto objects rotating around that"*, called *"the virial mismatch, and it's a foundation of dark matter"* `[00:10:03–10:09]` | **[EST]** — standing observational fact (flat rotation curves), reported not created by the talk. |
| E2 | Her fit uses *"I fitted all 175 spark galaxies in that catalog"* `[00:42:44]` — `[ASR: "spark" → SPARC]` | **[EST]** *(the catalog exists and is standard);* the **fit result is 2b/`[HYP]`.** |
| E3 | Historical: Uranus anomaly → **Neptune observed 1846** `[00:07:18]`; Mercury perihelion anomaly → *"we called this planet Vulcan"* → failed → **Einstein 1915** `[00:07:48–07:53]`; **Eddington** light-bending confirmed it `[00:08:02]` | **[EST]** — documented history, as she states it. |
| E4 | **Ted Jacobson, 1995**: reconstructed GR from entropy (thermodynamic derivation) `[00:23:38]` | **[EST]** (the 1995 result exists; her *characterisation* of its limits is 2b). |
| E5 | GR's *"so-called Hubble tension"* / cosmic acceleration is an open failure `[00:10:19]`; *"Lambda CMD is currently in a tiny bit of a crisis"* `[00:10:22]` — `[ASR: "Lambda CMD" → ΛCDM]` | **[EST]** for the tension's existence as a known problem; the *crisis* framing is her emphasis. |

### 2b. The talk's own proposals and self-reported results — all `[HYP]` (none independently verified)
| # | Claim (as spoken) | Tag |
|---|---|---|
| H1 | Information-geometry **reconstruction of Einstein's field equations**: *"these arguments can reconstruct the field equations of Einstein with us very small differences … therefore TAB, the stress energy tension is effectively modified"* `[00:26:07]` | **[HYP]** — a derivation claim, unrefereed. |
| H2 | Recovery limit: *"when T phi is zero, we recover Einstein's equations exactly"* `[00:26:29]` — `[ASR: "T phi" = T_φ]` | **[HYP]** — a structural requirement she set herself (self-satisfied by construction; see §4 W2). |
| H3 | Geometry reduction: her earlier paper *"I derive a proof that the geometry has only three linked objects from the original seven"* — metric, cubic tensor, Levi-Civita connection `[00:17:01–17:23]` — `[ASR: "normal fissure" → Fisher, "Levi-Sevita" → Levi-Civita]` | **[HYP]** — an unpresented proof, asserted. |
| H4 | **Rotation-curve outperformance, 175 galaxies.** Grey = GR, yellow = hers, red = **DC14** (*"the current most accurate fitted model today for dark matter"*) `[00:43:18]`; *"DC-14 has 12 fitted parameters for every galaxy and mine has three"* `[00:43:35]` | **[HYP]** — self-reported fit; parameter counts `[HYP]`. |
| H5 | Fit metrics: *"the pool RMS … follows by 48.8 in standard GR down to 12.8"* `[00:44:40]`; and, under matched priors, *"47.87 to 11.59 kilometers per second relative to baryon only GR"* `[00:45:19]`; *"2,620 intervelocities … 760 outer velocities are scored afterwards"* `[00:44:26–44:33]` | **[HYP]** — numbers spoken once, no method or uncertainty shown on camera. |
| H6 | **Solar-system bound**: *"a directional tide of like 30, sorry, 53, and units of 10 to the minus 27 per second squared"* `[00:46:24]` ⇒ adjustment *"on the order of 10 to the power of negative 20, which is far below what we can measure"* `[00:46:33]` | **[HYP]** — self-stated consistency check; she concedes the estimate uses *"a bunch of spherical approximations"* `[00:46:58]`. |
| H7 | **CMB acoustics**: a two-field stress *"differs internally from a CDM control by only about 31 parts per million"* `[00:47:54]`, *"the acoustic predictions of my model follow along with what we observe"* `[00:48:12]` | **[HYP]** — self-reported; a ~3×10⁻⁵ residual vs CDM is presented as agreement. |
| H8 | **CMB reinterpretation**: *"every observer … should see an effective cosmic background radiation … exactly of what we observe, but it's not necessarily the direct result of a big bang cosmology"* — thermality follows from a uniform-density **configuration**, not from a bang `[00:36:21–36:43]` | **[HYP]** — and see **[C]** below for the mechanism. |
| H9 | **Apparent acceleration without physical acceleration**: photons scale by a homogeneous factor *"B"* while material clocks stay fixed ⇒ *"the sources don't actually need to be accelerating physically in this model … objects in the universe are moving away from them at an accelerated rate"* `[00:38:40]` | **[HYP]** |
| H10 | **Dust-like dark sector**: the correlated-stress component dilutes as `a⁻³` with the rest-energy term, and a *"the contact trunk contribution will fade faster as A to the minus six"* `[00:40:53–41:07]` — `[ASR: "contact trunk" unresolved; "A" = scale factor a]` | **[HYP]** — the `a⁻⁶` term is her proposal's own new degree of freedom. |
| H11 | *"This is neither a formation theorem or a proof about every many particle ground system"* `[00:42:26]` | **[HYP]** — the speaker's **own explicit non-claim** (register-preserving; noted as a strength in §4). |

### 2c. Conjectural / structural
| # | Claim | Tag |
|---|---|---|
| C1 | Universe-as-shell: a mean-density sphere gives enclosed mass ∝ R³, compactness ∝ R², and the critical-density substitution yields compactness = H0²R²/c²; matching a Planck thermal wavelength *"about 5.3 millimeters"* `[00:35:46]` to a *"cosmological comparison radius of a board 14 and a half billion light years"* `[00:36:03]` — `[ASR: "a board" → "about"]` | **[C]** — a **dimensional coincidence** presented as a result; the two figures differ by ~28 orders of magnitude, so the relation as spoken cannot be a bare equality (see §4 W3). |
| C2 | *"the actual observable universe radius is, I believe like 45 billion light years"* `[00:36:18]` (vs *"13.8 billion years old"* `[00:36:08]`) | **[C]** — stated haltingly (*"I believe"*); numbers unverified on air. |
| C3 | A detector *"inside two shells"* can read the global configuration via an interference pattern / spacetime metric; shells *"get more and more energy approaching the event horizon … a highly redshifted thermal response"* `[00:33:58]` (poster w/ her supervisor at Perimeter) | **[C]** — a poster-stage idea, explicitly a *question* posed not a result. |
| C4 | *"the same longitudinal distinction matters for an occupied quantum or statistical state. A vanishing mean field doesn't establish that the state is empty"* `[00:20:24]` | **[C]** — the conceptual core (mean field ≠ emptiness ⇒ hidden stress-energy); plausible but not demonstrated here. |

### 2d. Analogies (hers, not results)
| # | Claim | Tag |
|---|---|---|
| A1 | Change-of-variables motivation: Fourier transform, Legendre transform (`[ASR: "Le Journe" / "Lejeune" → Legendre]`), and thermodynamics *"we can replace entropy as an independent variable with temperature and work with free energy"* `[00:11:37]` | **[A]** |
| A2 | *"providing the initial conditions of Earth while forgetting the moon exists and wondering why you have incorrect correction terms"* `[00:27:30]` | **[A]** |
| A3 | Covariance-ellipse mixing/squeezing *"two states that can have the same area and entropy, but it might have a very different internal structure"* `[00:18:23]`; *"It's not particles literally changing shape"* `[00:19:13]` | **[A]** |
| A4 | *"the measured CMB temperature, that scale is about 5.3 millimeters"* as a Planck-occupation wavelength `[00:35:46]` | **[A]/[C]** — the thermal-wavelength framing is textbook; the cosmological identification is C1. |

### 2e. Riff / colour only
| # | Claim | Tag |
|---|---|---|
| R1 | *"we called this planet Vulcan for you Star Trek fans out of there"* `[00:07:38]`; the *"2008 film called Einstein and Eddington"* `[00:08:15]` | **[RIFF]** — colour, not load-bearing. |
| R2 | *"which many of you are probably more familiar with. The absolute voltage doesn't matter, but it's the relative voltage to the ground state"* `[00:21:11]` | **[RIFF]** — pedagogical lever (also readable as **[A]**). |
| R3 | *"It'd be like using feet to measure things instead of something sensible, like a meter. I'm only slightly joking about that."* `[00:16:12]` | **[RIFF]** |

---

## 3. EILT mapping — with the MANDATORY FRICTION RULE

> **Vocabulary overlap with the house is ~nil:** `ledger` = 0 spoken; `commit` = 0; `provenance` = 0; `epiplexity` = 0; `syntropy` = 0; `Landauer` = 0; `entropy` appears **only** in the technical info-geometry sense. **Any mapping here is OUR imposition, not the source's.** Friction Rule satisfied and then some: **four `[CRITICAL DIVERGENCE]` rows** out of six — *not* uniformly convergent.

| # | EILT / house element | Source element (verbatim anchor) | Verdict |
|---|---|---|---|
| **M1** | Information-first ontology — physics derived from an information-theoretic structure | relative-entropy Hessian → BKM metric → Levi-Civita connection → *"reconstruct the field equations of Einstein"* `[00:17:23, 00:26:07]` | **[A]** — genuine structural resonance (both start from distinguishability/information and derive geometry). **Not** `[EST]`: it is an isomorphism of *posture*, and an external paper being isomorphic to our architecture cannot validate our software. |
| **M2** | `LOAD_BEARING_CLAIM:DPO-1` — provenance-not-truth; a record is counted once | *"each contribution must follow from an explicit physical model and only counted once"* `[00:31:38]`; *"relative entropy supplies the exact accounting identity"* `[00:23:29]` | **[CRITICAL DIVERGENCE]** — her "accounting identity" is a **thermodynamic/statistical balance** (heat ∝ area-entropy), *not* a provenance-of-commit ledger. Equating "counted once" with DPO-1 would be exactly the vocabulary-collision the house polices. **Do not identify.** |
| **M3** | House downgraded claim — **"dark matter = condensed cross-cycle epiplexity"** `[HYP]/[C]`, IDIOSYNCRATIC (indexed: *Big Mystery Survey* placement, `DIGEST_2026-10-15_BigMysterySurvey_PhysicistsOnDMDE_PhilHalper.md`; the field "would call it NOT A PHYSICS CLAIM AT ALL") | Her DM substitute is a **mis-description correction**: the extra stress is *already present* in ordinary matter's occupied modes + correlations — *"the physical content that we must identify: on which modes and which correlations are populated"* `[00:21:49]` | **[CRITICAL DIVERGENCE]** — **opposite ontologies.** She says the DM effect is a *description-layer artefact* of omitted internal correlations in **baryonic** matter (no new reservoir exists). The house claim places DM as a **genuine cross-cycle informational excess** (a real reservoir from prior cycles). These cannot both be "the dark matter". The source, notably, sits closer to **MOND-family** territory than to ours. |
| **M4** | House downgraded claim — **"dark energy = syntropy"** (C1) `[HYP]/[C]`, IDIOSYNCRATIC; index notes it "ADOPTS w=−1 and the ~68% budget from ΛCDM and re-labels the driver", weaker on falsifiability than even the Astrum re-description; **pre-emptive citation ban vs the Quanta/Cao-Preskill drop** | Her acceleration is a **kinematic re-reading** of redshift (photon-scale factor B, fixed material clocks) ⇒ *"sources don't actually need to be accelerating physically"* `[00:38:40]` | **[CRITICAL DIVERGENCE]** — **opposite causal arrows** again. She removes the driver entirely (apparent, not real, acceleration); the house posits a driver-substance. **Reaffirm the downgrade**: the house DE claim remains `[HYP]/[C]` and is **not** resurrected or supported by this source. If anything M4 **cuts at the house** — see M6. |
| **M5** | §6 non-rolling ledger / record-as-continuity | unitary transformation *"preserves the state's entropy"* `[00:12:37]`; *"a quantum channel contracts relative entropy"* `[00:19:18]` | **[A]** — bounded loss-of-distinguishability under a channel is *thematically* near the house's "what survives re-encoding", but it is a monotonicity theorem, not a ledger. `[A]`-bounded; do not identify. |
| **M6** | **The house's own weakest joint, named by the source's methodology** | Her 4-point standard `[00:05:32–06:23]`: identify ingredients · recover the old theory in a regime · provide a geometric foundation · **compute novel falsifiable observations**; *"I don't know any current gravitational model that does these. Well, maybe, I guess, until now."* `[00:06:23]` — backed by a **3-vs-12 parameter** parsimony claim `[00:43:35]` | **[CRITICAL DIVERGENCE] (against US)** — by her own standard the house's DM/DE claims name **no distinguishing observation**. Even granting the house claims their `[HYP]/[C]` register, they score *worse* on point 4 than this talk's proposal does. The honest reading: this source is **more falsifiable than the house's cosmology layer**, and the house cannot cite it as validation while also declining its standard. |

**Explicit forbidden mappings named in-file** (they would be confirmation bias): *"relative-entropy geometry = our ledger"*; *"dark matter = description artefact"* **supports** *"dark matter = cross-cycle epiplexity"*; *"apparent acceleration"* **supports** *"dark energy = syntropy"*; *"counted once" = DPO-1*.

---

## 4. Verdict

**Framing:** the *strongest* scientifically, and simultaneously the one whose load-bearing numbers are **least checkable from the source as recorded**. That split is the whole finding.

**★ STRONGEST JOINT `[HYP]` (methodological, not empirical):** the talk imposes an explicit four-point falsifiability standard **on itself** `[00:05:32–06:23]` — ingredients named, old theory recovered in a limit, geometric foundation required, novel falsifiable prediction demanded — and then **holds it**: two declared limits (`T_φ = 0` recovery `[00:26:29]`; the `a⁻³` dust dilution `[00:40:53]`), an explicit **parsimony** claim (3 params vs DC14's 12 `[00:43:35]`), an explicit solar-system consistency check `[00:46:33]`, and — the register-hygiene tell — **her own non-claim**: *"This is neither a formation theorem or a proof about every many particle ground system"* `[00:42:26]`. A speaker who tags her own result as *not* a theorem is doing the thing the house keeps asking sources to do.

**★ WEAKEST JOINT `[HYP]`:** every decisive empirical number — **48.8 → 12.8** `[00:44:40]`, **47.87 → 11.59 km/s** `[00:45:19]`, **53 ×10⁻²⁷ s⁻²** `[00:46:24]`, **≈ 31 ppm** `[00:47:54]` — is **self-reported from an unpublished preprint**, shown once on fast-advancing slides, with **no methodology, uncertainty budget, or statistical test visible on camera**; the organiser himself says the slides went *"quite fast"* and are *"not easy to follow"* and **has not yet read the manuscript** `[00:50:18, 00:49:19]`. **No independent verification occurred anywhere in the recording.** Runner-up (W2): the recovery limit `T_φ = 0 ⇒ Einstein exactly` `[00:26:29]` is self-satisfied by construction — any modification that switches off returns GR — so it is a weak requirement, not evidence. **(W3):** the universe-shell "result" `[00:35:46–36:03]` equates a **5.3 mm** thermal wavelength with a **~14.5 billion light-year** radius; those magnitudes differ by ~28 orders, so the spoken relation cannot be a bare equality and is unverifiable from the transcript — it reads as a **dimensional coincidence promoted to a result**.

**Register verdict:** headline claim = `[HYP]` (unrefereed, single-author, self-reported). **No claim in this talk earns `[EST]` on the strength of the talk itself** — every `[EST]` above is a *pre-existing* observation or documented history the talk merely cites.

---

## 5. Falsifiers

- **F-SG1** — locate the published preprint (`10.20944/preprints202609.2275.v2`, MDPI *Preprints*; description-only) and the arXiv posting; re-derive or read the **48.8 → 12.8** and **47.87 → 11.59 km/s** figures with their full method + error budget. If the residual reduction is not robust to the observational uncertainties she acknowledges are *not* in the fit `[00:43:04]`, the headline collapses.
- **F-SG2** — test the **3-vs-12 parameter** comparison for a like-for-like fit protocol (she states the fits are *not* done the same way `[00:45:38]`); a parsimony claim across unequal protocols is void.
- **F-SG3** — resolve the **universe-shell dimensional relation**: state the missing scale factor that turns `λ_T ≈ 5.3 mm ↔ R ≈ 14.5 Gly` into an equation; absent it, C1 is a coincidence.
- **F-SG4** — **independent reproduction** of the CMB ~31 ppm residual against a CDM control (H7) and of the `a⁻⁶` term's observational signature (H10): the proposal's *novel* distinguishing prediction is the `a⁻⁶` contribution, which must be shown to be measurable, else point 4 of her own standard fails.
- **F-SG5 (house-facing)** — re-run the *Big Mystery Survey* placement once its paper lands: does this source's MOND-family proposal fare better or worse than the house's `[HYP]/[C]` DM/DE claims on falsifiability? If the answer is "better", the house owes a correction to its own cosmology layer (see M6).

---

## 6. Integrity notes

- **ASR repairs flagged inline, not silently applied:** SPARC (`"spark"`), ΛCDM (`"Lambda CMD"`), Levi-Civita (`"Levi-Sevita"`), Fisher (`"fissure"`), BKM, Fubini-Study (`"Fubini study"`), von Neumann (`"Voinerman"` / `"Voinn-Nelman"`), Legendre (`"Le Journe"` / `"Lejeune"`), torsion, holonomy (`"halonomy"`), Perimeter (`"Primiter"` / `"Printer"`), DC14, NFW, `T_φ` (`"T phi"`), scale factor `a` (`"A"`), `10⁻²⁷ s⁻²`, `10⁻²⁰`.
- **LEFT UNRESOLVED, NOT GUESSED:** *"contact trunk"* (an exponent-carrying term, meaning unclear); *"Dr. Valbson"* (host surname); *"Dr. Ban and Dr. Afshorty"* (thesis supervisors — the two names are ASR-fragmented and not resolved); *"a board 14 and a half billion light years"* (`[ASR: "a board" → "about"]`, resolved only by context).
- **Description-only facts (NOT spoken):** the preprint **DOI** `10.20944/preprints202609.2275.v2`; speaker's correct surname **Gauvin**; the abstract's word **"incorrectly"**.
- **Cross-references (read, not merged):** `DIGEST_2026-10-15_BigMysterySurvey_PhysicistsOnDMDE_PhilHalper.md` (MOND > WIMPs placement; DE plurality now time-varying, not `w=−1`); `DIGEST_2026-10-15_Astrum_NewTheoryOfEverything_JonHypothesis_UnifiedCosmology.md` (the house's own self-critical DE row — **not** re-asserted); `hossenfelder_14yo_dark_energy_theory_2026-10-20.md` (`[CRITICAL DIVERGENCE]` vs house C1); `quanta_entanglement_magic_gives_gravity_cao_preskill_2026-10-18.md` (toy-model scope; the pre-emptive DE citation ban stands).
- **`canon_drop_lint.py`:** run against this draft (patterns from `/data/SecondBrain/90_System/retracted_formulations.json`) — result recorded in §7.

---

## 7. Gate receipts

- **New source:** `J-eq7DHxTpw` = **0 hits** across `Canon/`; `Gauvin` = 0; `Information Physics Institute` = 0. **No pre-existing drop on this source** ⇒ first pass, not a re-filing.
- **TAG GATE — PASS.** Registers restricted to the declared six-tag set; row-status flags (`[CRITICAL DIVERGENCE]`, `[DIVERGENCE]`, `[ASR]`, `[RE-TREAD]`) are not registers. Tag-instance counts: **`[HYP]` 24 · `[C]` 11 · `[EST]` 10 · `[A]` 8 · `[RIFF]` 3 · `[POETIC]` 0 = 56.** **0 invented registers.**
- **QUOTE GATE — PASS.** 72 italic-quoted spans → 77 checked fragments; **0 fabricated transcript quotes.** The 10 non-verbatim spans are all non-transcript by construction: the video **title** (2), the **description-abstract** phrase *"results in equations resolving the field which we incorrectly attribute to so called 'dark matter'"* + its word *"incorrectly"* (not spoken), and 6 **house-claim labels / forbidden-mapping names** (*"dark energy = syntropy"*, *"dark matter = cross-cycle epiplexity"*, *"relative-entropy geometry = our ledger"*, *"dark matter = description artefact"*). All source-attributed quotes verify verbatim against the saved flat transcript.
- **`canon_drop_lint.py` — CLEAN (14 patterns checked, exit 0)** against `/data/SecondBrain/90_System/retracted_formulations.json` (no LANDAUER-DISSIPATION, VOPSON-MBIT-DARKMATTER, SYNTROPIC-DECORATIVE, TSVF-SYNTROPIC-ATTRACTOR, or other flagged formulation revived; the house DM/DE claims are cited **as already-downgraded** `[HYP]/[C]`, never asserted).
- **YAML FRONTMATTER — parses.**
- **Library debt carried from this source:** D-SG-1 (obtain the MDPI preprint and re-verify the fit figures); D-SG-2 (the `a⁻⁶` distinguishing observable — the candidate that could earn `[EST]` for a *novel* prediction).
