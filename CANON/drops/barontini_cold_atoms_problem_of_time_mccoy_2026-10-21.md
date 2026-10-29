---
epistemic-registers: T=theorem H=hypothesis E=empirical A=analogy C=conjecture M=myth/poetic O=opinion F=falsifier
rule: no tag = treat as MYTH (do not build on it)
source: YT KHjNVmpHO60, "Physicists Looked Beneath the Quantum Field. Space and Time Were Gone", channel Julia McCoy (AI-clone presenter), 2026-10-21, 12:34; plus the two cited primary papers, read in full
date: 2026-10-21
filed-by: Dion
status: Working draft (pre-adversarial review)
---

# Canon Drop: Barontini's cold-atom "problem of time" test, the Rome collapse-model clock paper, and a content-funnel video that stacks them on the amplituhedron

**Date:** 2026-10-21 · **Filed by:** Dion
**Source (VERIFIED):** https://www.youtube.com/watch?v=KHjNVmpHO60. Julia McCoy channel (UCqzK60-oUOEq36uU9B1MMUg). Published 2026-10-21, 754 s, 35,240 views at pull time.
**Transcript:** `Canon/YT_TRANSCRIPTS/KHjNVmpHO60_McCoy_BarontiniColdAtomsTime_2026-10-21.txt`
**Primary papers (pulled and read in full):** `Canon/papers/problem_of_time_2026/`
- `Barontini_2026_PRR_L022047_VoR.pdf/.txt`: G. Barontini, *Testing the problem of time with cold atoms*, **Phys. Rev. Research 8, L022047 (2026)**, DOI 10.1103/1h9j-df4k. Received 25 Jul 2025, accepted 29 Apr 2026, published 11 Jun 2026. CC-BY version of record from the Birmingham repository. arXiv:2509.07745 (v1 9 Sep 2025, v3 11 Jun 2026) was also pulled.
- `Bortolotti_etal_arXiv_2504.06109.pdf/.txt`: N. Bortolotti, C. Curceanu, L. Diósi, S. Manti, K. Piscicchia, *Fundamental limits on clock precision from spacetime uncertainty in quantum collapse models*. arXiv:2504.06109 (8 Apr 2025), published as **Phys. Rev. Research 7, 043166 (2025)**, DOI 10.1103/p6tj-lg8l, **13 Nov 2025** (CrossRef-verified).

**Transcript method:** yt-dlp subtitles returned HTTP 429. youtube-transcript-api failed with its generic blocked-request error (the exact exception class was not captured). Audio came through with `yt-dlp -f 251`, and I transcribed it locally with **faster-whisper small.en** (CPU, int8, VAD off). Coverage runs 00:00 to 12:28 of 12:34. The one inter-segment gap over 10 s is 00:43→00:56; its contents were not checked (VAD was off, so it was not dropped by VAD). Proper nouns are corrected in this drop, not in the raw file.

---

## 0. Bottom line

| Question | Answer |
|---|---|
| What is the channel? | An **AI-clone content-marketing channel**. The channel describes itself as "750+ videos Julia never filmed". The presenter is a HeyGen avatar with an ElevenLabs voice. By McCoy's own published account, the scripts come from Claude trained on her voice, and "my video editors do most of the work". This video self-discloses at 07:05 ("you're hearing this from an AI clone"). The description funnels to paid products (Blueprint, AI Labs, Clone Mastermind, consulting). It is **not** a physics channel. |
| Are the cited papers real? | **Yes. All six sources in the description exist.** Nothing is fabricated at the citation level, which is better than this genre usually manages. Two metadata errors: the Rome paper is dated "(2026)" but is **2025**, and its on-air date "September 11" is wrong (§3). |
| Barontini: what does the paper actually show? | It is an **analog** experiment. A ≈2.4×10⁴-atom ⁸⁷Rb BEC is split into an observed and an unobserved sector. A post-hoc **entropic time** τ is built from the measured coarse-grained entropy of the observed sector. τ orders the data monotonically "almost everywhere", and an effective Schrödinger equation in τ reproduces the measured width. The author frames it as a "controlled experimental setting in which relational-time constructions can be quantitatively tested". It does **not** show that time emerges from anything in our universe. |
| "Time showed up anyway / stopped when atoms stopped changing" | Both are **true by construction** of Eq. (3). τ accumulates only when entropy is exchanged, and entropy here is ≈ atom number (footnote 36). The video presents a definition as a discovery. |
| Rome paper | Bortolotti et al. (CREF + Sapienza, Rome; INFN-LNF Frascati; Wigner/ELTE Budapest). **Theory only, conditional on collapse models.** It predicts a clock-time jitter of ~10⁻²⁸ s/yr (CSL) or ~10⁻³¹ s/yr (DP), "negligible for all contemporary timekeeping devices". It was published **7 months before** Barontini's paper, not "followed on September 11". 2026-09-11 is a ScienceDaily repost date. |
| WDW + amplituhedron "stack" | **Buzzword-stacking, not a formal connection.** The two have no shared derivation and live in mutually incompatible settings. They share only the word-level property "no time/space in the formalism", which means something different in each (§4). |
| Verdict | **The physics front half is accurate to press-release level, with real hedges. The structure is a sermon-and-funnel, and the physics is its veneer.** The house's own F-EO4 / register-inflation history is the right lens (§5). |

---

## 1. The channel: what it actually is

- [E] The channel description says: "Julia McCoy, founder of First Movers, was the first to build a clone of herself on YouTube that fully replaced her face and voice… 300,000+ subscribers · 750+ videos Julia never filmed · 2M+ impressions a month."
- [E] In the video itself (07:05): "And yes, you're hearing this from an AI clone. A thing that is quite literally information wearing a face." And at 09:25: "That file is why you're hearing this from a clone at all. A voice recording and about 100,000 words of me."
- [E] McCoy's own production account (AI-Branding Magazine, brandingacademy.ai/ai-avatar-for-youtube/): "I trained Claude in my voice, my cadence, my frameworks… Then I put HeyGen and ElevenLabs together." She adds "commit to a schedule of one new video per day. My video editors do most of the work." HeyGen also publishes a First Movers customer story.
- [E] Of the 40 most recent uploads (yt-dlp flat playlist), the large majority are AI-tool, AI-news, or clone-business videos (Topview, Genspark, HeyGen-for-realtors, GPT/Codex walkthroughs). A minority are faith-inflected AI or metaphysics videos ("Is AI the Mark of the Beast?", "AI Just Touched the Math God Wrote", "What's Beyond Matter? The Truth"). Physics is a sideline genre inside a motivational/faith funnel.
- [O] **So the answer to "who writes the science content" is: an LLM-drafted script in McCoy's trained voice, team-edited, delivered by an avatar.** It is neither a physicist's side project nor a dedicated science-communication shop. It is closest to an *in-house AI content engine*, which is the product the channel sells.
- [C] The first-person research claims ("I've spent two weeks pulling on that thread", 00:32; "I spent two weeks reading quantum field theory", 07:33) are production/authorship claims spoken by a clone. They are **unverifiable self-report** and should be handled per the production-authorship rule. Two weeks of reading by whom: McCoy, an editor, or the model?
- [O] Minor biographical ambiguity, not a contradiction. The video says "January 2023, I burned all my ships… Then I spent a year flat on my back". Her magazine account dates the health crash to **January 2025**. "Then" can span the gap. I did not verify further.

## 2. Barontini, PRR 8, L022047: what the paper says vs the video

**Abstract, verbatim (version of record):** "We realize a cold-atom system to quantitatively test relational constructions of time. A well-isolated atomic Bose-Einstein condensate evolves in a conservative trap that is partitioned by a thin optical barrier into an observed and unobserved sector, with negligible dissipation on the experimental timescale. Motivated by relational-time approaches discussed in the Wheeler-DeWitt framework, we ask whether the dynamics of the observed sector can be ordered using only internal degrees of freedom. To this end, we construct an entropic time from an experimentally defined coarse-grained entropy and demonstrate that it can robustly order the events in the observed sector across repeated cycles of expansion and recollapse. We finally derive an effective Schrödinger equation parametrized by this internal time and show that it is able to reproduce the measured evolution. These results establish a controlled experimental setting in which relational-time constructions can be quantitatively tested."

**What was actually done, from the paper:**
- [E] The BEC has "≃2.4 × 10⁴ ⁸⁷Rb atoms" in a crossed 1070 nm + 1550 nm dipole trap, with trap frequencies ≃2π×(25,70,70) Hz. An ≃8 µm barrier at 675 nm is projected by a digital micromirror device. The text says "On the timescale of interest of this experiment (≃100 ms), the system does not experience any measurable dissipation or particle loss."
- [E] The data were taken **in laboratory time**: "we follow the dynamics in laboratory time for 120 ms, taking an absorption image every 2 ms". The run was repeated for several barrier heights V. N and φ (the centre of mass, the "clock field") are extracted from each image, along with the entropy per atom s via Madeira et al. (2020), giving S = N·s.
- [E] Entropic time is **defined**, Eq. (3): τ(λ) = (σ/k_B) ∫_λ (dS/dφ)|dφ|. The paper continues: "This definition ensures that, as long as dS and dφ have the same sign, the arrow of time does not change direction." It also says "the entropic time flows faster when entropy is transferred in or out of the system and stops when no entropy is exchanged with the dark sector."
- [E] Result: "τ grows monotonically almost everywhere." With the exception of "a few 'wiggles' where dS and dφ change sign, caused by the coarse sampling in the clock field φ, the ordering of the data broadly reflects the one in laboratory time." Its rate differs from lab time. For V≃1 the bright sector goes to a "heat death" where τ stops. Total entropy of both sectors was constant within error bars, and the per-point statistical uncertainty was ~5%.
- [E] Footnote 36 is the load-bearing caveat: "Since the entropy per particle s remains of order unity throughout the evolution, the total entropy S is effectively proportional to the number of atoms in the bright sector. Thus, entropy flow is directly linked to atom number dynamics."
- [E] An effective "entropic time Schrödinger equation", Eq. (6), is derived from a Feshbach–Villars split keeping only the positive branch. A split-step simulation of it for V≃0 matches the measured width σ(τ) ("excellent agreement").
- [E] The scope is stated by the author. Eq. (2) is "structurally similar to a WDW minisuperspace model". He flags the difference himself: "the kinetic term in Eq. (2) is positive definite, whereas in canonical WDW equations the DeWitt metric induces an indefinite (hyperbolic) structure" (he argues this doesn't affect the phenomenology). He calls the result "a recipe for building an emergent internal time" and positions it next to Connes–Rovelli thermal time: "operationally from measurable entropy exchange… rather than from the algebraic structure of observables… It would be interesting to investigate whether the two notions coincide".

**Operational meaning of "time showing up":** it is **neither** Page–Wootters entanglement time (Page & Wootters is cited only as background, ref. 11) **nor** Connes–Rovelli thermal time (named as a conceptual cousin, explicitly different). It is a **stochastic-thermodynamics-style entropic parametrisation** (by analogy to Pigolotti et al. 2017). The ordering it produces is *checked against* the lab clock, which remains the ground truth throughout.

**Video vs paper:**

| Video line | Paper | Register |
|---|---|---|
| "sealed 24,000 atoms inside a tiny universe… No clock in there, nothing from the outside world allowed to touch it" (00:00) | Conservative optical trap: three external laser fields define the "universe", imaged every 2 ms against a lab clock. "Isolated" means negligible dissipation over ~100 ms. | [M] dramatized; the number 2.4×10⁴ is [E] |
| "Time showed up anyway. It came out of the atoms themselves." | An internal ordering parameter was **constructed** from measured entropy and found to reproduce the lab ordering, with wiggles. | [M] as phrased; underlying result [E] |
| "When the atoms stopped changing, time stopped." | True **by definition** of Eq. (3): τ only accrues when dS≠0. This is a design property, not a finding. | [M]: definition sold as discovery |
| "used two laser beams to split the cloud" | Two beams make the trap. The splitter is a third beam, a 675 nm DMD-projected barrier. | [E] minor garble |
| "a few billionths of a degree above absolute zero" | From the press release. The main text gives the coupling scale H_max/k_B ≃ 255 nK and no condensate temperature. | [E] from the press release, not the paper |
| "Physicists call that spread entropy" | Entropy here is ≈ atom number in the bright sector (fn. 36). The "spread" is atoms crossing the barrier. | [E], fair |
| "first controlled experiment to show time can be defined from the inside" (02:15) | The word "first" comes from the **Birmingham press release** quote ("first controlled experimental evidence…"), not the abstract. Moreva, Brida, Gramegna, Giovannetti, Maccone & Genovese (INRIM Turin), *Time from quantum entanglement: an experimental illustration*, PRA 89, 052122 (2014), already gave an experimental illustration of Page–Wootters internal time. "First" holds at most for the *entropic* construction. | [C]: contestable priority claim, inherited from the press office |
| "Quick honesty check. This is 24,000 atoms in a lab. A model. It doesn't prove our universe works this way." | Consistent with the paper's scope. | [O] **credit**: a real hedge |
| "Birmingham just showed Chronos is the manufactured kind… a year where nothing in you changed barely happened" (08:12) | Nothing in the paper concerns subjective, biographical, or human time. τ is a parameter for one sector's entropy exchange with another. | [M]: misappropriation |

## 3. The "Rome team, September 11" paper

- [E] **Identified:** Bortolotti, Curceanu, Diósi, Manti, Piscicchia, PRR 7, 043166. Affiliations: Bortolotti at CREF (Museo Storico della Fisica e Centro Studi e Ricerche "Enrico Fermi", Rome) and Sapienza Rome; Curceanu at INFN-LNF Frascati and IFIN-HH; Diósi at Wigner RCP and ELTE Budapest; Manti at INFN-LNF; Piscicchia at CREF and INFN-LNF. Funding: Templeton grant 62099, FQxI/Fetzer, INFN.
- [E] **Dating, corrected.** arXiv 8 Apr 2025. Accepted 31 Jul 2025. Published **13 Nov 2025**. "September 11, 2026" is the date of a ScienceDaily repost of the FQxI press release ("Physicists just found a tiny glitch in time itself", sciencedaily 260910225251). Earlier reposts: FQxI 6 Feb 2026, ScienceDaily 3 May 2026. **The video's "this month… On September 11th, a team in Rome… published" is false three ways:** wrong date, wrong year (the description also says "2026"), and wrong order. The Rome paper *predates* Barontini's publication by 7 months and his arXiv v1 by 5 months. The video's "followed on September 11" narrative of escalating findings is an artefact of press-cycle reposts.
- [E] **What it claims (abstract):** "We show that this mechanism could link both models — not just DP — to fundamental uncertainties in Newtonian gravity… these models suggest an induced uncertainty in the flow of time due to fluctuations in the Newtonian potential. We calculate the ultimate limit on time uncertainty and demonstrate that the resulting clock-time uncertainty remains negligible for all contemporary time-keeping devices, including atomic clocks."
- [E] Numbers: Δt ≃ 10⁻²⁸ s in 1 yr (CSL) and 10⁻³¹ s in 1 yr (DP) at reference parameters. The allowed CSL range is 10⁻³¹ to 10⁻²⁶ s at 1 yr. The effect is maximal for clocks of size ~ the smearing length σ and averages out for larger clocks. Δt grows as √t (white-noise random walk).
- [H] Register of the paper's own claim: **conditional on spontaneous collapse models (DP/CSL) being real *and* on the gravitational reading of their noise field.** It is a calculation, not an observation. It is falsifiable in principle (the collapse-parameter bounds are experimental), but the predicted effect lies many orders below any clock.
- [M] The video's gloss "Time has grain. Like wood. Grain is what you find in things that were made" (03:31) **mis-describes the physics**. The predicted effect is a *continuous stochastic jitter* (diffusive, Δt ∝ √t), not granularity or discreteness. The "made things have grain" inference is a design-argument move with no support in the paper.
- [O] The Rome and Birmingham papers share **no formalism and no question**. One is collapse-model noise in the Newtonian potential; the other is relational/entropic time in a WDW analog. Only the word "time" links them, and the video joins them with "And this month, it got stranger."

## 4. Wheeler–DeWitt + amplituhedron: formal connection or buzzword-stack?

**What the video actually does.** The description says "Stack that on Wheeler's 1967 equation and the amplituhedron, and the stage itself comes apart." On air (05:06 onward) it builds a "layer cake": hand → atoms → protons → quantum fields → space and time ("which we just watched come apart") → entanglement and change → it-from-bit → *Logos* (John 1:1), Hebrews 11:3, Genesis.

- [E] **Wheeler–DeWitt is real and correctly glossed at the headline level.** DeWitt, *Quantum theory of gravity. I.*, Phys. Rev. 160, 1113 (1967), which is Barontini's ref. [1]. The Hamiltonian constraint Ĥ Ψ = 0 has no external time parameter. "They checked. It had dropped out of the math completely" (02:35) is a dramatization: absence of time follows from the constraint structure of canonical GR and was not an empirical check.
- [E] **The amplituhedron is real, and the house already audited it** (`drops/DIGEST_2026-10-15_Amplituhedron_PositiveGeometry_Audit_ContrastCase.md`). Arkani-Hamed & Trnka, arXiv:1312.2007, JHEP 10 (2014) 030. A positive geometry in momentum-twistor space whose canonical form gives planar **N=4 SYM** amplitudes. Locality and unitarity are derived from positivity. Gravity and the real world have not been landed (per the ERC UNIVERSE+ release, as recorded in the house digest). The video's caveat "It works in a simplified practice universe so far" (04:15) is **accurate**. [O] Credit for that.
- [M] Video overstatements on the amplituhedron:
  - "Space and time come out of it as results" (04:08). What comes out is *locality and unitarity of the S-matrix*, not spacetime. Momentum-space on-shell amplitudes contain no positions for *any* theory; that is a property of the observable, not a discovery.
  - "Calculations that used to fill hundreds of pages shrink to one line" (03:56). This is the 2013 popular gloss, historically owed to Parke–Taylor (1986) / BCFW-era simplifications that predate the amplituhedron.
  - "Space time is doomed. That's Nima Arkani-Hamed." The phrase is widely attributed to his public talks. I did not establish whether the audio here is a clip of him or the clone reading it.
- [E] **The settings are mutually incompatible, and this is the core of the verdict:**
  - Wheeler–DeWitt is canonical quantum gravity of a *closed* universe: no asymptotic region, **no S-matrix**, and time is absent because of diffeomorphism invariance.
  - The amplituhedron needs a **flat asymptotic region and an S-matrix** (scattering in/out states). It has **no gravity**, is supersymmetric, and is planar. "No spacetime in the formalism" there means *no position-space integrals*, a completely different absence from WDW's *no external time parameter*.
  - Van Raamsdonk (arXiv:1005.3035, GRG 42:2323, 2010; correctly cited) is **AdS/CFT**: negative cosmological constant, boundary CFT. It is a thought-argument essay, not a computed "model universe" with entanglement being "turned down".
  - Barontini is a **BEC analog** whose reduced Hamiltonian is only "structurally similar" to minisuperspace, with the kinetic-sign difference the author himself flags.
  - No published derivation links the amplituhedron to the WDW equation or to the problem of time, and none is cited by the video.
- [E] The nearest genuine bridge in the literature, which the video does **not** cite, is Arkani-Hamed, Benincasa & Postnikov, *Cosmological polytopes and the wavefunction of the universe* (arXiv:1709.02813). It gives a positive geometry for the perturbative late-time wavefunction of conformally coupled scalars on a **fixed FRW background**. That "wavefunction of the universe" is a QFT-in-curved-spacetime object, **not a solution of the WDW constraint**, and contains no quantized gravity. So even the best real link does not connect positive geometry to the problem of time. [O] It also does not discharge the house's F-AMP3 (no gravity, toy scalar). I flag it as a precision note for the amplituhedron digest, which did not mention it.
- [O] **Verdict for §4: buzzword-stacking.** The video does not quite *assert* a formal connection, and its individual hedges are honest. But the "stack" rhetoric converts four independently scoped, mutually incompatible results into consecutive layers of one ontology. Each has its own register: a WDW analog in a BEC, an N=4 SYM S-matrix geometry, AdS entanglement–connectivity, and a 1989 programmatic essay. The thing glued between the layers is a shared English phrase ("no space/time in it"), not a shared object, map, or derivation. That is the exact shape of a vocabulary collision posing as a connection.

## 5. Tie-back to the house's own failure history (required)

- [E] `90_System/LEDGER_2026-10-15_F-EO2_OverConstraintTest.md` §9 records Bolonkin's diagnosis of the house's own v5.1 failure: "the failure mode was nobody actually checking load-bearing math once the vocabulary looked sufficiently dense (amplituhedron, constructor theory, algorithmic probability)." §10 (candidate F-EO4, Oryon) asks whether importing the **N=4-SYM-specific** amplituhedron as a filter on ordinary causal histories "is importing structure from a maximally special theory" — a category error.
- [O] **This video is the F-EO4 move in a rhetorical register.** It imports the amplituhedron's "no spacetime" out of planar N=4 scattering and into a story about the problem of time in quantum cosmology, a domain where the amplituhedron's own preconditions (asymptotic flatness, an S-matrix, no gravity) do not hold. The house made the same transplant in v5.1 with filter A(h), which the F-EO2 test showed was **undefined** (no history → positive-geometry map). Neither the house nor the video supplied a map. The difference is that the house's version claimed to be formalism.
- [E] The house's amplituhedron control-case digest (§4 row 7) put the house *closer to Astrum/Jon than to the amplituhedron* on "refuses to overclaim". It located the "jewel / death of spacetime" inflation **in popular coverage, not in the papers**. This video is a clean instance of that popular layer: it uses the word "jewel" verbatim (03:56) and the "spacetime is doomed" line.
- [E] `GENERALIZATION_REGISTER_INFLATION.md`: "A claim sits at a stronger register than its evidence licenses." Applied here, each layer of the stack is promoted one register up just by being placed under the previous one.
- [O] **Friction against us.** The video's final move, from it-from-bit to *Logos* to "your imagination is closer to the floor of reality than your bank balance" (08:30), is the same theological decompilation the house's register-tags reference warns about in **our own** canon ("syntropic binding pressure = Logos / God's Love"). If we score the video harshly here, we owe the same score to our "syntropy as God's love" lines. See the friction table.

## 6. Claim audit and friction table

| Dimension | Source claim (who) | Audit | Register |
|---|---|---|---|
| BEC experiment exists, 2.4×10⁴ atoms, bright/dark sectors | Video, from Barontini | Verified in the VoR text | [E] |
| Entropic time orders events robustly | Barontini abstract | Verified, "almost everywhere", with coarse-sampling wiggles; lab clock is ground truth | [E] |
| Time "stops" when nothing changes | Video, as discovery | Definitional property of Eq. (3) | [M] |
| Entropy flow here = atom-number flow | Barontini fn. 36 | The video omits this; it deflates the "entropy" framing to "atoms crossing a barrier" | [E] |
| Effective Schrödinger equation in τ reproduces data | Barontini | Verified for the V≃0 width; one configuration shown | [E] |
| "First controlled experiment" of internal time | Birmingham press release, repeated by video | Moreva et al. 2014 (PRA 89, 052122) predates it for Page–Wootters time | [C] |
| Rome team published Sept 11 (2026), after Barontini | Video and description | False: PRR 13 Nov 2025; Sept 11 2026 is a ScienceDaily repost | [E] correction |
| Collapse models imply a clock jitter, negligible today | Bortolotti et al. | Verified; conditional theory calculation | [H] |
| "Time has grain… things that were made" | Video | Effect is continuous diffusive noise, not grain; design-inference unsupported | [M] |
| WDW has no time parameter | Video, from DeWitt 1967 | Correct headline | [T] (within canonical GR quantization) |
| Amplituhedron: spacetime "comes out as results" | Video | Locality and unitarity emerge, not spacetime; N=4 planar only | [M] |
| WDW + amplituhedron + Van Raamsdonk "stack" | Video description | Incompatible settings; no map; vocabulary collision | [M] |
| Mass of proton ≈99% field energy | Video | Roughly correct (QCD binding; quark masses ~1%) | [E] |
| It from bit at the floor of reality | Wheeler 1989, via video | Programmatic essay; correctly quoted as Wheeler's position, not a result | [C] |
| Imagination "closer to the floor of reality" than a bank balance | Video (clone/McCoy) | Self-sealing; no observable; falsifier missing by construction | [M] |
| **[CRITICAL DIVERGENCE] against the house** | House canon: "syntropy = Logos / God's love" style lines | Same decompilation move as the video's John 1:1 → it-from-bit step. The house tags it as analogy but has repeatedly let it run ahead of its tags (amplituhedron digest row 7) | [O] |
| **[CRITICAL DIVERGENCE] against our own scepticism** | Video hedges ("doesn't prove our universe", "practice universe", "your watch is fine") | The physics front half is *more* hedged than the house's own v5.1 A(h) claim was. A harsh verdict must not erase that | [O] |

## 7. Falsifiers for this drop's own claims

- [F] **F-MC1 (the buzzword-stack verdict).** A published derivation mapping the amplituhedron (or any positive geometry) to solutions of the Wheeler–DeWitt constraint, or to a relational/entropic time construction, would upgrade §4 from "collision" to "connection". Prior: none known. The cosmological polytope does not qualify (fixed FRW background, no quantized gravity).
- [F] **F-MC2 (definitional-not-discovery).** If Barontini's supplemental material shows τ was predicted *before* the data and could have failed in a nontrivial way, e.g. ordering lab-time inversions *without* tracking atom-number flux, then "true by construction" is too harsh. The mild version stays: monotonicity is guaranteed only while dS and dφ share a sign, and the paper shows where they don't. **SM not read this pass.**
- [F] **F-MC3 (Rome dating).** An APS or arXiv record of a *new* Bortolotti et al. paper on 2026-09-11 would falsify the "repost date" correction. Checked: arXiv author search shows one Bortolotti paper; CrossRef shows 2025-11-13.
- [F] **F-MC4 (channel nature).** A statement from McCoy or First Movers that this video's script was written by a named physicist or science writer would move §1 from "AI content engine" to "outsourced science writing". Not found.

## 8. Verdict

- [O] **Barontini is a real, honest, modest paper.** It is a clean analog testbed with one well-defined entropic parametrisation. The author scopes it carefully ("structurally similar", "recipe", "testbed") and flags the kinetic-sign mismatch with real WDW himself. The strongest inflation is in the **Birmingham press release** ("first controlled experimental evidence… new insight into the nature of time in quantum gravity"), and the video inherits it.
- [O] **The video's physics is press-release-accurate and better-hedged than the genre.** It has real citations, no fabricated papers, and explicit "this is a model" caveats. But it gets the Rome paper's date, year, and ordering wrong; it sells the definition of τ as a discovery; and it mis-glosses both "grain" and the amplituhedron's "no spacetime".
- [O] **Structurally it is a sermon and a funnel.** About half the runtime (06:14–12:34) is scripture, a biographical redemption arc, and a call to "write down the field-sized version of your dream". It ends on the product's own premise: "information wearing a face". The physics is used to license "Birmingham just told us which kind of change makes time", a claim the paper cannot support.
- [O] **The Wheeler–DeWitt + amplituhedron stack is buzzword-stacking**, the same vocabulary-density failure the house diagnosed in itself on 2026-10-15 (F-EO2 §9, F-EO4). The useful thing to take from this source is a clean outside specimen of our own failure mode, not the physics. If anything is cited downstream, **cite the two papers, never this video**.

*Draft compiled by Dion (ClawHorde Backend) | Status: Pre-Adversarial Working Draft. No NotebookLM, GitHub, or Drive replication performed in this pass (scope fence).*
