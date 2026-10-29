---
epistemic-registers: T=theorem H/HYP=hypothesis E=empirical A=analogy C=conjecture M/POETIC=myth/poetic O=opinion F=falsifier · cycle set: [VERIFIED] [QUOTE, Lxx] [EST] [HYP] [CONTRA] [ATTACK SURFACE] [RIFF] [CRITICAL_DIVERGENCE]
rule: no tag = treat as MYTH (do not build on it)
source: Avshalom Elitzur interviewed at IAI "How The Light Gets In" — YT l8oJ878kJ64, The Institute of Art and Ideas
date: 2026-10-18 (source published 2026-10-17)
---

# Canon Drop — Avshalom Elitzur, "Reconceptualising Causality" (IAI) — checked AGAINST the standing §8 backward-cone downgrade, not as a fresh drop

**Filed:** 2026-10-18 · Dion (subagent) · **Status:** working draft, pre-adversarial. GitHub sync untouched.

**Source [VERIFIED, live page 2026-10-18]:** https://www.youtube.com/watch?v=l8oJ878kJ64. Published `2026-10-17T09:00:26-07:00`, `PT22M5S` (22:05), 8,399 views, 115 likes, channel The Institute of Art and Ideas (797K subs). **The page `<title>` read *"Can Effects Precede Causes? | Avshalom Elitzur"* on first load and *"Reconceptualising Causality | Avshalom Elitzur"* on the second.** That looks like title A/B testing. Both are IAI framing. Elitzur is at the Israeli Institute for Advanced Research (Iyar). He is a PhD student of Aharonov and co-originator of the Elitzur–Vaidman bomb tester. Credibility is high.

**Transcript:** `Canon/YT_TRANSCRIPTS/l8oJ878kJ64_Elitzur_ReconceptualisingCausality_IAI_2026-10-17.txt` (183 lines, 0:00→21:55, full coverage, YouTube ASR, no speaker labels). **Method:** `youtube-transcript-api` was blocked, then yt-dlp subtitles returned **HTTP 429**. The **CDP 127.0.0.1:9333 "Show transcript" panel** worked (24,335 chars), so faster-whisper was not needed. `L` refs point to that file. ASR fixes (Aharonov, Bohm, Vaidman, Wigner, von Neumann, Bohr, Schrödinger, TSVF) are listed in the file header.

**Content map:** about 7 of 22 minutes are physics (`L76–L132`, 8:00–15:40). The rest covers consciousness and the hard problem (inverted-qualia argument, `L53–L74`), Aharonov as mentor, education, and a closing political exhortation (`L150–L183`). Only the physics block bears on house canon.

---

## 0. Framing check (IAI copy vs his words)

| IAI description | What he says | Verdict |
|---|---|---|
| *"a measurement done in the present influences not only the future, but the past"* | His first words on the topic are a disclaimer: *"it doesn't mean that you can change your past"* `[QUOTE, L77]`. Then, in a stronger idiom: *"your measurement determines not only the state of the cat at that moment, but it's entire history"* `[QUOTE, L89]` and *"its effect goes… from this moment backwards until the previous measurement"* `[QUOTE, L115-116]`. | **PARTIAL.** The copy is faithful to his *idiom*. It drops the disclaimer he leads with, and it drops the fact that his "influence" is bounded by the *previous measurement*, not by "the past" in general. |
| "Can effects precede causes?" (alt title) | He never says an effect precedes its cause in a signalling sense. His cash-value claims are retrodiction ("you can know… position and momentum very precisely… in retrospect", `L116-117`) and an interpretive picture of EPR ("zigzags through space time", `L120-121`). | **OVERCLAIM (title).** This is the same promo-copy inflation class as the 10-14 New Scientist/Rovelli finding. |
| "radical implications… for… consciousness" | He **rejects** consciousness-causes-collapse (Wigner/von Neumann: *"a brilliant idea but it's wrong"*, `L44`). He adopts Bohr's *"irreversible act of amplification… this is thermodynamics"* `[QUOTE, L48-49]`. | **Register-swap.** His consciousness position is deflationary about QM. The copy implies the opposite. |

---

## 1. What his claim actually is (mechanism, in his words, then in his papers)

**1.1 In the video (all `[QUOTE]`, physics block):**
- **Schrödinger's cat, 3-day version** (`L85-91`): a cat found decomposed seems to show it was never in superposition. *"No, the moment you open the box, your measurement determines… its entire history."* No experiment is offered. This is an **interpretive assertion** `[O]`.
- **ABL / TSVF retrodiction** (`L107-117`): compute forward from the pre-selection and backward from the post-selection. *"If you do it with a cannonball, it's redundant… with a quantum mechanical object… they add to one another."* Measure position in the morning and momentum in the evening, and *"at noon… you can know the particle's position and momentum very precisely. You're not violating the uncertainty principle because this is in retrospect."* This is the **Aharonov–Bergmann–Lebowitz 1964** result `[EST]` (*Phys. Rev.* 134, B1410). It is a statement about assigning values to a pre- *and* post-selected sub-ensemble. **He concedes inline that it is retrospective.**
- **EPR "zigzag"** (`L118-122`): the influence *"goes backwards… to the common source… zigzags through space time. I don't say that it completely solves the mystery."* This is the Costa de Beauregard picture (1976) `[EST as interpretation]`. He hedges it himself.
- **Anomalous weak values** (`L123-132`): rare pre/post-selection pairs give *"too large spin… negative mass, negative energy… verified recently by some very delicate experiments… we are beginning to see the emergence of a completely new physics."* He names no experiment.

**1.2 The video is vague on mechanism, so I went to the paper:** Aharonov, Cohen & Elitzur, *"Can a future choice affect a past measurement's outcome?"*, **Annals of Physics 355 (2015) 258–268**, arXiv:1206.6224v6 `[VERIFIED, full text read]`. Setup: EPR pairs, each particle gets several **weak** measurements (Alice, "noon", recorded "on stone"), then one **strong** measurement along an orientation **chosen at the last moment** (Bob, "evening"). Findings, from the paper's own text:
- The weak record agrees with the later strong outcomes **only after "slicing"**, i.e. after sorting Alice's record into sub-ensembles *defined by Bob's later strong outcomes*. A single weak measurement is mostly noise. Agreement appears only in conditioned ensemble averages.
- §5: *"As TSVF and traditional quantum theory are equivalent, obliging one- and two-vector explanations to be equally valid, this contradiction can be resolved in two ways"*. Either the weak results *anticipated* the later choice (two-vector, "retrocausal in character"), or the weak measurements *slightly biased* the later strong ones (one-vector). They prefer the two-vector account on grounds of **"simplicity and elegance"** (§6), not on evidence.
- Strongest sentence (abstract): the experimenter's choice *"has been encrypted within the weak measurement's outcomes, even before the experimenters themselves know what their choice will be."*
- §6: *"Relativistic locality is not violated."* An optical test with Genovese (INRIM) was announced; I did **not** locate a published result → `[UNVERIFIED]`.

**1.3 TSVF's actual content** `[EST]`: Aharonov & Vaidman, *"The Two-State Vector Formalism: an Updated Review"*, quant-ph/0105101, abstract: *"a time-symmetrized approach to standard quantum theory particularly helpful for the analysis of experiments performed on **pre- and post-selected ensembles**."* ⟨φ| is the **post-selected state, i.e. an actual later measurement outcome**. It is a description-assignment rule for sub-ensembles and is empirically equivalent to standard QM. Weak values themselves are `[E]` (Ritchie, Story & Hulet, *PRL* 66, 1107, 1991; Lundeen & Steinberg, *PRL* 102, 020404, 2009; most recently Xie, Xu & Zhang, arXiv:2607.11284, July 2026, which is unreviewed). **Their "quantumness"/ontic reading is contested** (Ferrie & Combes, *PRL* 113, 120404, 2014; Kastner, quant-ph/9807037, on counterfactual use of ABL).

**Bottom line on the claim:** this is the **standard, no-signalling-compliant pre/post-selection effect**, i.e. the ABL/weak-value family, the same structural class as delayed-choice erasure. It is told in his preferred **two-vector causal idiom**. He makes **no stronger physical claim** than his papers do, and his papers say outright that the retrocausal reading is one of two empirically equivalent readings, chosen for elegance. "Completely new physics" `[O]` is his opinion. Observing anomalous weak values does not discriminate TSVF from standard QM, because they are predicted by standard QM.

---

## 2. Retroactive SIGNALLING? (the Landauer/Vopson-pattern check)

**No. He neither claims nor implies readable backward signalling. The no-signalling distinction survives intact, and the reason is structural:**

1. **In the video** he opens with the denial: *"it doesn't mean that you can change your past"* `[L77]`. His "influence" ends at the previous measurement `[L116]`.
2. **In the paper** the backward "information" is recoverable **only by conditioning on the future outcomes** ("slicing"). Before Bob measures, Alice's stone tablet is noise-dominated and her marginal statistics cannot depend on Bob's later choice. This follows from standard QM, which the paper itself says TSVF is equivalent to: the distribution of an earlier outcome is fixed by the state at that time. The "encrypted" metaphor is accurate in exactly this sense. **The key is the future result, so nothing can be read before the future happens.**
3. **The rhetorical risk is the "encrypted… before the experimenters themselves know" line** `[ATTACK SURFACE]`. Read without §2.2 it sounds like precognitive data. It isn't: no one can decrypt it in advance, and the paper never claims otherwise. **Any house retelling that drops the "only after slicing by future outcomes" clause would re-enact the Landauer/Vopson overclaim pattern** (a conditional/model-dependent result restated as unconditional). The Elitzur source itself does **not** commit it.
4. Postselection as a resource is real but quarantined. Aaronson's PostBQP = PP shows how powerful *conditioning* is, and it is exactly why post-selected "effects" cannot be read as causation without the discarded runs.

---

## 3. APPLYING THE EXISTING DOWNGRADE — objection by objection

**Current house status (corrected from the brief):** monograph §8 ⟨φ|/global causal invariance = **`[HYP]`** (re-tags 2026-10-14, `EILT_Master_Monograph…md` L137 Rovelli, L139 Bareinboim). **On 2026-10-15 CMR-6 went further:** the two-cone "bidirectional compilation" figure is **`[POETIC]` decorative motivation, NOT mechanism** (monograph L133; `daimon_cybernetics…2026-10-07.md` L169; strange-loop drop L41; `90_System/LEDGER_2026-10-15_PhysicsClaimRegisterPass.md` L15). So the claim is *already below* [HYP] at its figure sites. The question is whether Elitzur lifts it.

| Objection on file | Does Elitzur's video/paper answer it? | Verdict |
|---|---|---|
| **Bareinboim / CHT (evidential): L2/L3 causal claim asserted on L1 evidence** (`DIGEST_2026-10-14_Bareinboim…` §4 row 6) | **No. It is a textbook instance of the CHT, conceded by the authors.** His evidence is conditional ensemble statistics: P(weak record \| Bob's later strong outcome) = **L1**. The paper states that two causal models (future→past "anticipation" vs past→future "weak bias") fit the **same** statistics ("equally valid") and picks one by elegance. That is CHT part one verbatim: same L1, different L2. **Sharper still:** Bob's last-moment orientation choice *is* an intervention, a genuine do(·). At the interventional level the backward effect is exactly **null**: P(weak record \| do(future choice)) = P(weak record), by no-signalling. The dependence appears **only** when you also condition on the future *outcome*, i.e. through post-selection. That is the structure of selection/conditioning, not of a backward L2 effect. `[RIFF, Dion's analysis; follows from standard QM]` | ✦ **Objection stands, and gets stronger.** The one place a do-arm exists, the backward causal effect measures zero. |
| **Rovelli / RQM (definitional): no accessible global state for an absolute backward cone** (`DIGEST_2026-10-14_Rovelli…` §2 row 6, friction row 2) | **No. It isn't even engaged.** Elitzur's ⟨φ| is a **local, laboratory post-selection**: a definite later outcome recorded by a specific apparatus. That is *compatible* with RQM-style relative facts and needs no universal state. It also supplies **none** of the global/cosmic ⟨φ| the house used. The only Aharonov-line route to a cosmic final state is the separate Aharonov–Gruss "two-time interpretation" (quant-ph/0507269, 2005). It is not mentioned in the video, it has no discriminating prediction, and it posits a final *boundary condition*, not an optimising attractor. | ✦ **Objection untouched.** Real TSVF lives at the scale RQM permits; the house's usage lives at the scale RQM denies. |
| **DemystifySci (substrate): the backward wave is dispensable** (`DIGEST_2026-10-15_DemystifySci…` row 2) | Elitzur's own paper concedes the one-vector account is *available* (§5), at "conceptual cost" but with **no empirical cost**. That is a fourth statement that the backward vector is optional. | **Reinforced, by the authors' own admission.** |
| **CMR-6 [POETIC] (no falsifier, cosmic extension unestablished)** | No falsifier is offered for anything cosmic. The new item is a *mis-attribution* finding (below). | Stands. |

**[CRITICAL_DIVERGENCE] — attribution fidelity (new, from reading the primary source).** House canon (`daimon_cybernetics…2026-10-07.md` L160-166; monograph §8) cites TSVF for *"⟨φ(T)| backpropagates from the future syntropic boundary condition… the optimal variational free energy minimum (the teleological attractor / 'God's plan')"*. In Aharonov/Vaidman/Elitzur, ⟨φ| is **whatever outcome was actually post-selected**. It is not optimal, not a goal, not a minimum of anything, and in the rare-pair cases Elitzur highlights it is *improbable* by construction. **"Teleological attractor" is a house addition worn as a TSVF citation.** At best that is `[A]` by analogy. As attribution it is drift, the same shape as the 10-17 Deutsch/Constructor-Theory finding (house vocabulary attributed to a physicist who says otherwise).

### VERDICT

**LEAVE AS IS. No upgrade.** Monograph §8 stays at **`[HYP]`** and the two-cone figure stays at **`[POETIC]`**. **No further register drop is warranted**, because the figure is already at the floor (decorative). But Elitzur's primary paper **adds an attribution constraint**: the house may cite TSVF **only** for pre/post-selected ensemble statistics and weak values. Citing it for a future *teleological/syntropic/optimal* attractor is a mis-citation. Reasons, in one line each:
- **Not new evidence:** the claim is ABL-1964 / weak values, already on file as "TSVF's formal content… untouched" (CMR-6). Elitzur restates it in a stronger idiom.
- **Bareinboim objection not answered:** the authors concede the two causal readings are empirically equivalent (identical L1). Where an intervention exists, the backward effect is null.
- **Rovelli objection not reached:** his ⟨φ| is local and RQM-compatible, and it gives no global cone.
- **No signalling claimed:** so it cannot be the "strong" result that would be needed to move a backward-causation claim off [HYP].

**Proposed (NOT applied — no register is lowered, so rule 5's mandatory source re-tag is not triggered; needs Gene):** append one line under the CMR-6 marker at `daimon_cybernetics…2026-10-07.md` L169 and monograph L133:
`[ATTRIBUTION 2026-10-18: in TSVF ⟨φ| is the actually post-selected outcome, not an optimal/teleological attractor (Aharonov–Vaidman quant-ph/0105101; Aharonov–Cohen–Elitzur Ann. Phys. 355, 2015). "Syntropic attractor" is house [A], not TSVF. See elitzur_reconceptualising_causality_iai_2026-10-17.md §3.]`

---

## 4. Friction table

| # | Dimension | Elitzur | House | Divergence / prediction |
|---|---|---|---|---|
| 1 | What ⟨φ\| is | A post-selected measurement outcome; local; improbable in the interesting cases | Future syntropic **optimal** attractor; global | ✦ **[CRITICAL_DIVERGENCE]**: mis-attribution (§3) |
| 2 | Evidence type for "backward influence" | Conditional weak-value statistics, read two-vector "for simplicity and elegance" | L1 optical demo (Oldenburg), already struck | Both are L1. **His is better L1 (real QM data), but still L1.** |
| 3 | Measurement / commit | Bohr: *"irreversible act of amplification… thermodynamics"* `[L48-49]` | Ledger = irreversible record relative to the recorder (surviving Rovelli row 2) | **CONVERGENCE.** Supports the *surviving* plank, not the cone. Also note Elitzur says this "doesn't solve" the measurement problem `[L50]`. |
| 4 | A real "now" / becoming | *"another heresy of mine. I do believe that there is a now… becoming"* `[L79-80]` | §8 L129 cosmic "The Present" (cut by Rovelli friction row 3) | **[CONTRA] to Rovelli, by a credentialed physicist, but self-labelled heresy, with no argument given on air** → `[O]`. Does not rescue L129. Also: his becoming is an open future with empty "corridors" (`L80`), which is the opposite of a pre-fixed future attractor. |
| 5 | Consciousness and collapse | Rejects Wigner/von Neumann (`L42-47`) | House sometimes links commit and experience (bare-commit [HYP]) | No collision. His hard-problem position (`L53-74`) is standard Chalmers; no new content. |
| 6 | "New physics" | Anomalous weak values = *"emergence of a completely new physics"* `[L128-132]` | — | `[O]` / `[ATTACK SURFACE]`: they are predicted by standard QM, and his own 2015 paper concedes equivalence. |

---

## 5. Falsifiers

- **[F] F-EZ1 (would upgrade):** a published version of the INRIM/Genovese weak-then-strong EPR test, or any experiment, in which the **unconditioned** weak record's statistics depend on the later measurement *choice*, i.e. P(weak \| do(choice)) ≠ P(weak). That would be backward signalling. Standard QM predicts null. Only this kind of result would license moving any backward-causation claim above [HYP].
- **[F] F-EZ2 (would upgrade the reading, not the cosmology):** a TSVF prediction that **differs** from standard QM. None exists by the authors' own equivalence statement. Until one does, "two-vector = what really happens" stays `[O]`.
- **[F] F-EZ3 (inherited debt, Rovelli forward item):** the house must name an observable that distinguishes a *cosmic* final boundary condition (Aharonov–Gruss) from none. Without one, §8 is a mood, not a hypothesis.

**Not a present-day-harm engagement.** F-GB1 is not touched; this is theory intake. His closing political segment (`L163-183`) is `[O]` and out of scope.
