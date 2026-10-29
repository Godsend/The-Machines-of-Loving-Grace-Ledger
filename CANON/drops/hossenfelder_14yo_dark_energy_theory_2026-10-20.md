---
epistemic-registers: T=theorem H=hypothesis E=empirical A=analogy C=conjecture M=myth/poetic O=opinion F=falsifier
rule: no tag = treat as MYTH (do not build on it)
source: "Sabine Hossenfelder, 'A 14-Year-Old's New Theory of the Universe', YT y4fN8APrV8I, uploaded 2026-10-20, 6:26 (386 s). Primary source audited: Liam Desre, 'ΛCDM+S – Thermodynamic Cosmology: Simulating The Universe's Expansion Without Dark Energy', Youth Science Canada ProjectBoard entry (posted 2026-02-24; all section tabs read in full 2026-10-21)"
date: 2026-10-20
canon-id: CANON-2026-10-20-HOSSENFELDER-DESRE-LCDM-S
tags: [cosmology, dark-energy, entropic-cosmology, horizon-thermodynamics, hubble-tension, science-fair, title-inflation, press-inflation, dark-energy-syntropy, hossenfelder]
continuity: hossenfelder_universe_born_magnetic_hubble_tension_2026-10-17.md (same source, prior calibration — her body content held up there too)
---

# Canon Drop: Hossenfelder on Liam Desre's "ΛCDM+S", checked against the submission

**Filed by:** Dion (subagent pass), 2026-10-21
**Transcript:** `Canon/YT_TRANSCRIPTS/y4fN8APrV8I_Hossenfelder_14yoDarkEnergyTheory_2026-10-20.txt`. youtube-transcript-api was blocked and yt-dlp subtitles returned 429. The transcript came from the audio rail instead: yt-dlp `-f 251`, then ffmpeg at 16 kHz mono, then faster-whisper `small.en` on cpu/int8 with VAD. It has 104 segments covering 00:00 to 06:20 of a 6:26 video, with no gap longer than 15 s. ASR name errors are corrected in the file header: "Lion Desiree" and "Lime" are Liam Desre.
**Primary source status:** **READ.** I read the ProjectBoard entry (Why / How / What / So What / What's Next / References) through CDP. No paper, preprint or code exists yet. His own "What's Next" section says a peer-review draft and a GitHub release are still *planned*.
**Competition records checked:** Youth Science Canada CWSF 2026 release (2026-05-29), the cwsf-espc.ca 2026 history page, the Kiel University EUCYS 2026 winners page and news post, the YSC EUCYS release (2026-09-29), the EC R&I news item (2026-09-28), CBC Kids News (2026-06-19), and Times of India.

---

## 1. Who, what, which prize: verified

- [E] **Student:** Liam Desre (YSC also spells it "Desré"), from Kingston, Ontario. He was in Grade 9 at CWSF and Grade 10 at EUCYS. Kiel University's winners list gives his age as **14**.
- [E] **Prize 1, Canada-Wide Science Fair 2026, Edmonton:** Best Project Award – Discovery, presented 2026-05-28. He was one of 390 finalists with 344 projects. CBC reports about $700 in cash plus scholarship offers.
- [E] **Prize 2, the "5,000 euros" Sabine mentions:** **one of four Second Prizes (€5,000) at the 37th European Union Contest for Young Scientists (EUCYS), Kiel, 22–27 Sept 2026**, in the Physics category. At EUCYS the project ran under the title *"ΛCDM+S: Evaluating a Thermodynamic Extension to Standard Cosmology."* Kiel University's own page confirms this, so it does not rest on press copy. (This is not Regeneron ISEF or the Google Science Fair.)
- [E] Sabine's "won 5,000 euros" `[00:13]` **matches the EUCYS record.**

## 2. What the submission actually is

Everything below comes from the ProjectBoard entry.

- [E] **The idea:** treat the cosmic horizon the way black-hole thermodynamics treats an event horizon (Bekenstein, Hawking, Bousso, Padmanabhan are cited). Entropy growth on the horizon then drives the late-time acceleration in place of Λ.
- [E] **Construction:** he takes two Friedmann solutions, one matter-dominated and one "entropy-driven, dark-energy-like", and **stitches them together with a sigmoid transition function**. He says the sigmoid "introduced 4 new parameters" (How tab). The What tab says the model "deals with 5 parameters, 3 more than traditional ΛCDM". **The two parameter counts disagree inside the submission**, and the discrepancy is minor.
- [E] **Method:** Gaussian priors, 500 Monte Carlo runs ("3.5M data points"), a likelihood built against "48 million samples" from Planck, Pantheon+, SH0ES, H0LiCOW, DESI and SDSS, then Metropolis–Hastings MCMC with 64k samples.
- [E] **Headline result:** "93.4% agreement **relative to ΛCDM**". The benchmark is ΛCDM's own prediction, not the data. The number measures how well the model *mimics* the standard model. It also reports 98% agreement with the CMB acoustic scale and 99% with the BAO ruler. SNe Ia come out about 0.15 mag brighter at z = 0.1–0.5, which he lines up with the Pantheon+ residuals and the H₀ tension.
- [E] **Self-reported limitations, stated plainly:** the model is "systematically statistically disfavoured relative to ΛCDM in tests such as the BIC and AIC"; it "does not statistically outperform ΛCDM"; it has no Boltzmann code, so the CMB treatment is incomplete; and the Pantheon+ residuals may come from systematics (dust, Malmquist bias, calibration drift) rather than cosmology. He also writes: "agreement with observational data may not uniquely determine the underlying physics."

**Classification:** [E] this is **a phenomenological extension fitted to real public data**, built on an *existing* idea (horizon-entropy / entropic cosmology). It is not a new theoretical framework, and it is not just a simulation either. The engineering is real (derivation, MCMC, the data pipeline). The physics content is a parametrised interpolation. The "novel" part is his particular sigmoid variant, which Sabine describes as "a variant… in which the contribution from thermodynamics grows increasingly important" `[03:45]`.

## 3. Prior art: Sabine's "the idea itself is not new and it's not Liam's" is correct

- [E] **Easson, Frampton & Smoot, "Entropic Accelerating Universe", arXiv:1002.4278 (2010), read this pass.** The core move is the same: the apparent horizon carries Hawking-type temperature and Bekenstein entropy, the resulting entropic force replaces dark energy, and "Dark energy is thereby obviated." One author is a Nobel laureate.
- [E] **Basilakos & Solà, "Entropic-force dark energy reconsidered", PRD 90, 023008 (2014), abstract read.** They find that the entropic-force model "is not viable at the background and perturbation levels" because it adds no constant term. Phenomenological patches restore the deceleration-to-acceleration transition, but "recent structure formation data strongly disfavors" them. **Desre's sigmoid is exactly such a phenomenological patch.** Whether it escapes the growth-of-structure objection **cannot be judged**: his equations are not public and he has no perturbation or growth analysis. That is an open question, not a refutation.
- [E] Neither Easson–Frampton–Smoot nor Basilakos–Solà appears in the **15 references shown** on the board. He cites Padmanabhan 2010 and claims to have read "roughly 75 peer-reviewed papers", so the full bibliography could not be checked.
- [H, from recall, not fetched this pass] The "dark energy scales with horizon size" link Sabine points to `[02:03]` is also the premise of holographic dark energy (Cohen–Kaplan–Nelson 1999; Li 2004). Verify before citing.

## 4. Sabine's actual claims, checked

| Video (transcript) | Check | Register |
|---|---|---|
| "won 5,000 euros" `[00:13]` | EUCYS second prize, €5,000 | [E] accurate |
| His video abstract: "derived new solutions to the Friedmann equations… 3.5 million data points… Bayesian inference" `[00:31–00:49]` | Matches the board text word for word | [E] accurate |
| "check all the boxes for a typical journal submission" `[00:18]`, "the **scary** thing" | The format is there: lit review, Bayesian pipeline, limitations section | [O] fair. **Read the word "scary" carefully** (see §5) |
| "The idea itself is not new and it's not Liam's" `[03:41]` | Easson–Frampton–Smoot 2010 | [E] accurate |
| "introduces new parameters… makes it easier to fit the data" `[04:04]` | 3–4 extra parameters, and BIC/AIC disfavour it by his own report | [E] accurate |
| "He's very honest about what this method can and can't do" `[04:00]` | His Limitations section bears this out | [E] accurate |
| "fits the data reasonably well… could alleviate the Hubble tension" `[03:53]` | He claims "consistent with" the tension, not that it resolves it | [E] accurate, not overstated |
| "standard research paper… 10/10 on the bullshit meter… superfluous words… a model with more free parameters" `[04:13–04:29]` | Her own judgment on the genre | [O] defensible. The extra parameters are why the fit improves, and the thermodynamic story is not tested separately from them |
| "There are some discussion about whether dark energy really is constant" `[01:47]` | A nod to DESI-era evolving-w results; she does not name DESI | [E] true in general, not developed |

## 5. Title vs body: does the title oversell her framing?

[O] **Yes. But the inflation partly lives in her own opening line, and its real source is the competition and press chain.**
- Her first sentence repeats the title: "won a prize for a new theory of the universe which might explain dark energy" `[00:00]`. Two and a half minutes later she takes it apart herself: "not new and it's not Liam's", and in a standard paper "10 out of 10 on the bullshit meter". The pattern is a hook followed by a body verdict that cancels the hook. This differs from the 10-17 video, where the inflation came from the SLAC press release and she corrected it.
- [E] **The inflation started upstream:** YSC calls it "a credible alternative explanation for the expansion of the universe"; CBC Kids News says "an explanation of the universe that's never been thought of before"; Times of India says "proposed a thermodynamic alternative to dark energy". The CBC line is **contradicted by the 2010 literature.**
- [O] **The brief's reading needs one correction.** Sabine is not simply praising the submission's rigour. "Ticks all the boxes" is meant **ambivalently**. It is partly a compliment to the student and partly an indictment of the field: outsiders, and now AI, can reproduce the "community accent" `[01:01–01:25]`; "the standards in this area of research are currently incredibly low" `[04:47]`; "I want to see more of it but with more courage. Don't repeat the mistakes of the past." Her real point is that matching the journal format is now a weak signal of quality, not a strong one. She praises the kid and condemns the template he copied so well.
- [O] Her body framing is careful and, on every checkable point, correct. That is consistent with the 10-17 calibration. **Hossenfelder's body content: 2 for 2 against the primary source. Titles: 2 for 2 inflated.**

## 6. Canon connections and friction

- **[CRITICAL DIVERGENCE] with EILT Monograph §7 / PRIVATE_CANONICAL C1 ("dark energy = syntropy", [C]).** Desre's model rhymes with house C1 (horizon entropy linked to acceleration), but the **causal arrow runs the other way**. In his model, horizon-entropy growth *drives* the acceleration. In ours, w = −1 acceleration *expands* S_max and so maintains the gradient. The two are not the same claim and must not be cross-cited.
- [O] **Sabine's verdict hits house C1 harder than it hits Desre.** "All this talk about entropy and thermodynamics is really superfluous words; in the end it's a model with more free parameters." Desre at least has free parameters fitted to Pantheon+/BAO, a BIC penalty he admits, and a dated test (LSST/Euclid). C1 *adopts* w = −1 and relabels it, with no fit and no distinguishing observable. This is the same self-critical row as the Astrum drop (2026-10-15 §5 row 5): **a 14-year-old's science-fair entry is currently more falsifiable than our dark-energy claim.**
- [F] **Citation ban, in the same spirit as the Quanta/Cao–Preskill ban (10-18):** Desre's result may **not** be cited as support for C1. It is an unrefereed, BIC-disfavoured parametrisation with the opposite causal direction.
- Big Mystery Survey (10-15): the physicist plurality favours a *time-varying* field. ΛCDM+S is effectively one more evolving-dark-energy-like history, and it competes in exactly that crowded space. The connection is real but thin.
- Hossenfelder PMF/H₀ drop (10-17): both target the H₀ tension. PMF works through the early-universe sound horizon; Desre works through late-time expansion history. Orthogonal mechanisms. No forced link.

## 7. Falsifiers

- [F] **F-DES1:** his own stated test. If LSST/Euclid SNe Ia at z = 0.1–0.5 do **not** show the about 0.15 mag brightening relative to ΛCDM once Pantheon+ systematics are controlled, ΛCDM+S's distinguishing prediction fails.
- [F] **F-DES2:** a growth-of-structure (fσ₈ / S₈) analysis of the sigmoid model. If it reproduces the Basilakos–Solà failure, the model is dead at the perturbation level whatever its background fit.
- [F] **F-DES3 (house):** if the promised preprint appears and cites none of the 2010–2014 entropic-cosmology literature, the "new theory" framing is confirmed as a novelty error. If it engages that literature and shows where the sigmoid variant evades it, upgrade the novelty claim from [C] toward [H].

## 8. Verdict

- [E] The student, both prizes, and the submission are real, and every specific fact Sabine states checks out.
- [C] **The physics claim is conjecture-level:** a known idea (Easson–Frampton–Smoot 2010) given a phenomenological sigmoid. It mimics ΛCDM to 93% at the cost of 3–4 parameters, the information criteria disfavour it, and it has no CMB Boltzmann treatment, no perturbation analysis, no public code and no peer review.
- [O] **It is a genuinely impressive piece of self-taught work, and it is not a new theory of the universe.** The honest Limitations section is the most mature thing in it. Sabine's body content is accurate and her title is not. The actual inflation chain runs YSC → CBC ("never been thought of before") → title. Her sharpest point is aimed at the field, not the kid: matching the journal format has become cheap. The house should take that point personally, because by her criterion C1 does worse than his entry.
