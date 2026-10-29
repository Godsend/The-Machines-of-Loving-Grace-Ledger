# Canon Drop — "Perturbing Complex Networks: How Hidden Structure Shapes System Response" (Debanik Bhattacharjee)

**Date:** 2026-10-26 · **Filed by:** canon-intake subagent (delegated by Dion)
**Source (VERIFIED):** https://www.youtube.com/watch?v=9IWGvY04bCA
**Transcript / Text:** `/data/SecondBrain/Canon/YT_TRANSCRIPTS/9IWGvY04bCA_Bhattacharjee_PerturbingComplexNetworks_2026-10-26.txt` (clean) · `…_timestamped.txt` (per-segment timestamps)
**epistemic-registers:** T=theorem H=hypothesis E=empirical A=analogy C=conjecture M=myth/poetic O=opinion F=falsifier — **no tag = treat as MYTH**

---

## Identity & attribution (verified this pass)

- **video id:** `9IWGvY04bCA` · **title (YouTube):** *"Perturbing Complex Networks" by Debanik Bhattacharjee* · **channel:** Michael Levin's Academic Content (`@drmichaellevin`) · **duration:** 38:16 · **upload:** 2026-10-26.
- **Full stated title (from the video `description`, rung 0):** *"Perturbing Complex Networks: How Hidden Structure Shapes System Response"* by **Debanik Bhattacharjee**, "given at our Center" (Allen Discovery Center, Tufts) "on the topic of porous media and neural computation." The video title is a **truncation** of the description's fuller title. **The phrase "hidden structure" never occurs in the transcript (0 hits)** — it is production/framing copy, not a speaker claim.
- **This is a research seminar / job-talk BY Bhattacharjee, not a paper-reading and not Levin talking.** Two voices only:
  - **Presenter = Debanik Bhattacharjee** — talk body, 0:00–38:16 uninterrupt. Postdoc (NeuroAI) at ELSC, Hebrew University of Jerusalem, with **Idan Segev**; PhD (Environmental Engineering) Technion; MSc (Mechanical Eng.) University of Alberta. His own ELSC page independently confirms the porous-media→cortical-microcircuit arc ("from pore networks in disordered media to synaptic networks in cortical microcircuits") and the Segev postdoc.
  - **Host/interlocutor = Michael Levin** — from ~30:25 (1825 s) to end. Every turn from ~30:25 on is Levin: the questions, the Toufts-lab descriptions, the planaria graft anecdote, the "diverse intelligence" framing.
- **Attribution discipline:** the planaria 2-head memory, the **17 %** graft figure, the "cognitive viruses" preprint, and the "semantic content is the hard problem" framing are **LEVIN's, not Bhattacharjee's** — do not attribute them to the speaker. Bhattacharjee's talk body does **not** mention bioelectricity at all.

## Extraction & coverage (honest)

- **Rung used:** rung 1 — `youtube-transcript-api` via `~/.hermes/bin/uv run --with youtube-transcript-api`, **first try**. A manual track was **not** offered; the only English rail is **auto-generated `en`** (`is_generated=True`). 22 auto tracks total (en + 21 translations); no manual caption.
- **Coverage: FULL.** 1,085 segments, first snippet `0.0 s`, last snippet `2295.56 s` = **38:15.6** vs stated **38:16** → ~99.98 % of runtime, start-to-end, no gaps observed in segment continuity. Rung 0 (description / linked written transcript) yielded **no** written transcript and **no** paper link — only the scholar profile and the Allen Center URL, which is why rungs 2–4 were never needed.
- **ASR caveat:** auto-caption grade. Proper nouns are occasionally garbled or absent (e.g. he *points at a slide* for a "very popular network scientist … who started his journey with invasion percolation in porous media in the '90s" — **the name is not in the audio at all**, so it cannot be recovered from this transcript; "biological mix circuit" is likely "biological microcircuit"; "UV and IT U in Linz" = JKU/IT:U Linz). Where a number/name is load-bearing it is verified against a primary source below.

---

## Claim inventory (register-tagged; single-letter set)

| # | Claim (paraphrased, attributed) | t | Reg |
|:--|:--|:--|:--|
| 1 | Speaker's own CV: MSc U. Alberta (2018, transport/porous media/droplet spreading); PhD Technion (porous-media multiphase flow in heterogeneous networks, "finished earlier this year"); zebrafish-embryo calcium-signalling experiments in C.-P. Heisenberg's group, Austria; current postdoc Hebrew University "till the end of 2027"; recent visit to JKU/IT:U Linz. | 0:18–1:35 | `[E]` |
| 2 | General perturbation method: perturb a system → measure the response → infer a mechanism; "widespread" across networks, financial networks, pore networks, neural networks. | 2:05–2:30 | `[E]` |
| 3 | His "complex-systems lens": architecture (heterogeneity, connectivity) + local interaction rules → collective dynamics → macroscopic response. | 2:29–3:00 | `[O]` |
| 4 | Pore-network representation: pores = graph nodes, throats = edges; coordination number chosen per physics (uses 3 or 6). | 4:31–5:05 | `[E]` |
| 5 | Throat-size statistics modelled with **gamma and Gaussian** distributions; Gaussian becomes symmetric at high shape parameter *K*, right-skewed as *K* falls (captures pore-size tailing). | 5:04–5:45 | `[E]` |
| 6 | Capillary pressure given by the **Young–Laplace** equation; contact angle <90° = hydrophilic, >90° = hydrophobic (noting literature disagrees on cutoff). | 6:20–7:35 | `[E]` |
| 7 | **Surfactants** = chemical perturbation agents that lower oil–water interfacial tension; applications: soil remediation, oil-spill remediation, enhanced oil recovery. | 7:35–8:01 | `[E]` |
| 8 | Model stack: invasion-percolation ("around for more than 40 years") for primary invasion + mass conservation "analogous to Kirchhoff's law" + Poiseuille flow; a **lumped mass-transfer coefficient** collapses convection+diffusion; Langmuir adsorption isotherm; literature-borrowed surfactant parameters. | 9:30–10:38 | `[E]` |
| 9 | Ensemble design: **500 random networks**, fixed mean throat size, sweep the **variance** (= heterogeneity); adjacency matrix, coordination 3/6, prescribed boundary conditions. | 11:16–11:40 | `[E]` |
| 10 | Primary/secondary invasion is a **sigmoidal S-curve**, quantified by a **Gaussian CDF** of the normal distribution (invaded fraction vs time). | 13:45–14:30 | `[E]` |
| 11 | **Phase 1 (PR E):** the S-curve **functional form is preserved regardless of boundary conditions**; kinetics mainly **rescales time**; higher variance → earlier invasion via "fast pathways"; dynamics set by **one control ratio** = the mass-transfer timescale. | 14:31–17:20 | `[E]` |
| 12 | Mass-transfer coefficient **increases linearly with heterogeneity**, explained via newly-available interface/throat sizes and surface-area-to-volume ratio. | 15:35–16:10 | `[E]` |
| 13 | Phase-1 take-home: secondary invasion = "a time-rescaled sigmoidal trend … controlled by the mass-transfer time scale and **amplified by** the heterogeneity of the pore spaces." | 17:06–17:28 | `[O]` |
| 14 | **Phase 2 (PR E, gamma/non-Gaussian networks):** a **time/mass-transfer scaling** and a **Laplace-pressure scaling** are "two coordinates of the same activation" — both invasion trajectories fit the **same** Gaussian CDF. | 17:30–20:12 | `[E]` |
| 15 | Regime selection: **heavy-tailed throats → Laplace pressure controls; symmetric distribution → mass transfer controls.** Heterogeneity decides the pressure-vs-kinetics bottleneck. | 20:05–20:30 | `[E]` |
| 16 | A **third PhD phase** exists (preprint out) but is **not presented** (time). | 17:51–18:06 | `[E]` |
| 17 | **Neural work (postdoc, preliminary, "first pass"):** digital twins — a biophysical neuron model is stimulated under defined perturbations; outputs (voltage traces, spike trains) train a **3-layer temporal convolutional network (TCN)**; spike/voltage prediction difficulty defines a **"functional complexity index" (FCI)**. | 23:58–25:05 | `[H]` |
| 18 | The FCI is **borrowed from a labmate's recent PNAS paper**; that work "did not do perturbation," which is his new angle. | 25:08–25:22 | `[E]` |
| 19 | Target variables: **inhibition, dendritic geometry, synaptic placement, circuit structure** (shunt placed at different dendritic locations) shape computation. | 25:24–25:46 | `[H]` |
| 20 | Honest limitation, stated on air: results are **one realization only**, "not a full statistical interpretation yet"; the TCN predicts spikes well in some conditions, poorly in others. | 26:37–26:50 | `[E]` |
| 21 | Broader directions: population-level activity (mouse recordings + drug intervention, RNN, low-rank systems for cheap computation); organismic/group scale (bees + pesticide exposure altering behavioural dynamics). | 27:52–29:05 | `[H]` |
| 22 | Closing aphorism (his own adaptation of two quotes seen in Singapore ~7 yrs ago): "I moved across systems to collect ignorance. I kept my idea: structure shapes function, whether the network has pores, neurons, firms, or financial institutions. Perturbations reveal what matters most." | 29:35–30:01 | `[M]` |
| **— Levin (host) from ~30:25 —** | | | |
| 23 | Levin: the physics here is inspiration "but more importantly … what the **information** is doing"; wants to erase the materials/energy/information boundaries. | 30:44–31:10 | `[O]` |
| 24 | Levin: interesting to apply this to "the movement of **literally thoughts** within a cognitive system" — cognitive content (in brain *and* non-brain tissue), not just neural activation; "stress patterns and priors … move around in tissue that isn't brain tissue." | 30:50–31:48 | `[C]` |
| 25 | Levin: has someone building novel visualizers of how cognitive content moves inside **language models**; how **beliefs/truths spread** through logic/inference — "prove a theorem over here and the consequences … percolate up." | 31:55–32:34 | `[C]` |
| 26 | Levin: mentions "one of your preprints … **using large language models as cognitive viruses**" — describes it as "a perspective piece … **I wasn't the main driver on it**." (self-disclosed attribution: not his primary work) | 32:57–33:34 | `[E]` |
| 27 | Levin: "our biggest issue now is that we have a hard time **visualizing**" non-physical things; metabolic/bioelectric states are hard, **semantic content** is hardest; making visualizers is tough but would be useful. | 33:30–34:12 | `[O]` |
| 28 | Levin (planaria): can make **two-headed** flatworms by changing bioelectric pattern memory; a tiny piece of a two-headed worm **surgically implanted into a one-headed host** makes the host two-headed in **"something like 17 %"** of cases; the **cells are not coming out** (tracked), "**something's coming out, some kind of influence.**" | 36:19–37:02 | `[H]` |
| 29 | Levin: lab focus = "**diverse intelligence**" across embodiments solving problems; interest is in the **semantic content** of what is measured. | 37:46–38:10 | `[O]` |

**Claim count: 29 rows** (22 Bhattacharjee talk-body, 7 Levin Q&A). Register spread: `[E]` ×14, `[H]` ×4, `[O]` ×6, `[C]` ×3, `[M]` ×1. No `[T]` and no `[F]` minted in the inventory (falsifiers are listed separately, below).

---

## Verification against primary sources (what checks, what doesn't)

**CONFIRMED:**
- **PR E Phase 1 = REAL and matches ("published … few months ago").** Bhattacharjee, Ramon & Edery, *Spatiotemporal dynamics of surfactant-driven secondary invasion in Gaussian pore networks*, **Phys. Rev. E 114(2):025101, published 1 Aug 2026**, DOI `10.1103/ptlk-gj5f` (Technion CRIS). Gaussian throat-size variance controls disorder; sigmoidal trajectories; mass-transfer kinetics + network variance "rescale invasion timescales while preserving the overall functional form" — **the transcript's Phase-1 claims 11–13 are accurate.**
- **PR E Phase 2 = REAL.** Bhattacharjee, Ramon & Edery, *Evolution of invasion patterns due to surfactant adsorption in non-Gaussian pore distribution: Role of mass transfer and Laplace pressure*, **Phys. Rev. E 112(6):065108 (Dec 2025)**, DOI `10.1103/b2wy-b918`. Heavy-tailed vs symmetric regime split is in the abstract. **Note a naming slip in the talk:** he says "gamma network," the paper says **"non-Gaussian"** — same object, his shorthand.
- **"Invasion percolation … more than 40 years"** = accurate: Wilkinson & Willemsen introduced IP in **1983** (*J. Phys. A* 16:3365), motivated by Chandler et al. 1982 → 43 years at time of talk.
- **The borrowed PNAS paper = REAL and correctly described.** Aizenbud, Yoeli, Beniaguev, de Kock, London & **Segev**, *Dendritic morphology and synaptic nonlinearities enhance functional complexity in human cortical neurons*, **PNAS 123(28):e2533168123, 2026-07-07**, DOI `10.1073/pnas.2533168123`. It introduces the **Functional Complexity Index (FCI)**, uses a **three-layer TCN** trained to mimic a biophysical neuron, and is **not about perturbation** — exactly as he says. His "someone in the lab" is the Segev-lab authorship. Claims 17–20 accurately describe it.

**COULD NOT VERIFY:**
- **The planaria graft "~17 %" figure (claim 28, Levin).** The documented Levin-lab result is a **~30 % penetrance for *re-cutting* cryptic worms into two-headed animals** (Durant et al. 2017/2019; Pezzulo et al. 2021, *Phil. Trans. R. Soc. B* 376:20190765) — **not 17 %**, and via **amputation**, not **grafting**. A transplant experiment exists as a *model* (Cervera, Manzanares, Levin & Mafe, *J. Theor. Biol.* 558:111356, 2023) but no located paper states a 17 % graft-transfer figure. Treat the 17 % as **Levin's on-air, uncited, possibly-newer lab claim — unverified**.
- **The unnamed "very popular network scientist"** whose slide he points at (t ≈ 21:11–21:30). The name is absent from the audio; not recoverable from this transcript.
- **"biological mix circuit"** (likely "biological microcircuit") and the **mouse/drug-intervention** dataset — future work, no paper named.
- Levin's promise to email cognition references — no artifact.

---

## Critical Audit & Falsification Matrix

*(Single-letter registers. `[CRITICAL DIVERGENCE]` is a friction-row **status label**, not a register — each row still carries one canonical tag.)*

| Dimension | Source claim | House (EILT/ClawHorde) audit | Reg |
|:--|:--|:--|:--|
| **Structure→function (the stated thesis)** | "structure shapes function … whether the network has pores, neurons, firms, or financial institutions" (claim 22). | Directly congenial to the house's core plank that substrate geometry/topology specifies computation. But this talk *earns* it only on pore networks; the neural clause is asserted, not shown (claim 17–20 are one-realization). | `[M]` (aphorism) / `[H]` (neural) |
| **Perturbation as probe** | Perturb → measure response → infer mechanism; "perturbations reveal what matters most" (claims 2, 22). | **Genuine, specific correspondence** to the house's own "audit" logic: the falsifier/probe is how you locate the load-bearing variable. His PR E work is the house's own method ("find the invariant; see what the disorder merely rescales") executed competently on a tractable system — a *working example*, not a validation of our architecture. | `[A]` |
| **[CRITICAL DIVERGENCE] — invariant vs. specifier** | Across 500 random networks and a wide variance sweep, **heterogeneity only rescales the timescale while preserving the S-curve functional form** (claims 11, 14). | **The analogy and the source genuinely disagree.** The strong form of the house's "structure specifies function" predicts that re-drawing the micro-architecture should change the *functional form* of the macroscopic response. Bhattacharjee's own published result says the opposite: structural disorder is a **single-knob rescaling** — the macro functional form is **invariant** to the disorder. If the house wants structure to carry the *content* of the computation, this source says the microstructure mostly carries only a *rate constant*. Load-bearing friction; do not wave it away. | `[E]` |
| **Two scalings = one activation** | Mass-transfer/timed scaling and Laplace-pressure scaling are "two coordinates of the same activation," both fitting the same Gaussian CDF (claim 14). | Parallels the canon's recurring finding that rival vocabularies are often *the same claim in two coordinates* (cf. GNW vs. the GPU/GUI split). But [CRITICAL DIVERGENCE]: the house's ledger insists **provenance** (which mechanism did it) is the load-bearing record; here the two mechanisms are explicitly **non-fungible in regime** yet **algebraically interchangeable in form** — provenance is real (heavy-tail→Laplace) but the *prediction* doesn't need it. | `[E]` |
| **Non-genetic pattern memory (Levin)** | Cells "are not coming out … something's coming out, some kind of influence" transfers 2-headedness by graft (claim 28). | Structurally the house's "commit / pattern memory" — a stable, re-writable state carried outside the genome. **But** [CRITICAL DIVERGENCE]: Levin's influence has **no named carrier, no addressability, and a diffusible/field character**, whereas the house's commit is **bearer-independent and addressable**. And the transfer's *content* is anatomical (a body-plan), not propositional — so this is **not** evidence for a propositional ledger. | `[H]` |
| **Information movement (Levin)** | Erase materials/energy/information boundaries; apply the tools to "literally thoughts … within a cognitive system," to beliefs/truths spreading through formal systems (claims 23–25). | This is the **canon's home domain** and its live target (how semantic content propagates; the ledger certifies *provenance*, not *truth*). It is a **sibling to the house's own open problem**, offered as a direction, not a result. His "prove a theorem, consequences percolate up" is a clean falsifier-shaped research program the house could actually run. | `[C]` |

**Falsifiers (proposed, `[F]` — pre-registered, to be tested by the house, not by the source):**
- **F-B1.** If a single neuron's FCI is *not* invariant to the specific perturbation protocol used to generate its training data (only to the underlying cell morphology), then "functional complexity" is measuring the *perturbation*, not the neuron — the metric collapses.
- **F-B2.** If the pore-network S-curve's functional form *does* change under a re-drawn topology at matched variance (i.e. the invariance in claim 11 is specific to his Gaussian ensemble), the "heterogeneity is only a rescaling knob" claim fails.
- **F-B3.** If the graft-transfer effect (claim 28) is shown to require living cells migrating (contrary to "the cells are not coming out"), the "influence without a carrier" reading dies.

---

## Opinionated verdict (not a recap)

- **Strongest point.** The measured invariance and the two-coordinate unification. That a capillary-dominated invasion front, across 500 random networks and a swept disorder, keeps its **sigmoid functional form** while a **single mass-transfer timescale** rescales it — and that a time-scaling and a Laplace-pressure-scaling are shown to be **the same curve in two coordinates** — is a real, twice-published, cross-validated invariant. It is exactly the house's own epistemic move ("find what the disorder cannot touch") done cleanly, with self-imposed caveats he volunteers on air instead of hiding.
- **Weakest joint.** Everything neural. The postdoc half is **one realization**, **no statistics**, built on a metric (**FCI**) he explicitly borrowed from a labmate's PNAS paper that **never tested perturbation** — so there is no validation that FCI means anything *under* perturbation. The pore→neuron bridge is asserted at the level of shared vocabulary ("nodes, edges, flows, thresholds"), and he concedes "a lot of differences" but **never names one**. The analogy is a hypothesis wearing a framework's clothes.
- **Contradiction with existing canon.** One real one, and it points at us: the **published** invariance result pushes against a strong "specific microstructure specifies function" reading (see the `[CRITICAL DIVERGENCE]` row). Otherwise the talk is **orthogonal** to the cosmology cluster and **consistent** with the existing Levin bioelectricity drops (`michael_levin_cognitive_glues_bioelectricity_2026-10-09.md`, `DIGEST_2026-10-15_MichaelLevin_BioelectricityAging_Khemani.md`) — Levin's planaria pattern-memory claim is the same, already-filed phenomenon. **First Debanik Bhattacharjee source in canon; first pore-network/invasion-percolation source in canon** (dedupe: `bhattacharjee` 0 hits across `Canon/`, `9IWGvY04bCA` 0 hits; the porous-media/invasion-percolation vocabulary is new to the index).

*Scope note: CANON DROP ONLY. No GitHub push, no NotebookLM ingest, no TTS, no Drive mirror — replication is Dion's separate pass. Rung 4 (ASR) was not required; coverage is full and verified against the stated duration.*
