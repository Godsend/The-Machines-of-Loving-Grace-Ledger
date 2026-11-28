---
canon_id: CANON-2026-11-27-hskoK2y9TNk-DROPSTONE-NOTEBOOK
drop_date: 2026-11-27
video_id: hskoK2y9TNk
title: 'AI Found Something It Shouldn''t Be Able To Find'
channel: 'Epic Programmer'
url: https://www.youtube.com/watch?v=hskoK2y9TNk
upload_date: 2026-11-27
duration_s: 1492
views_at_pull: '28700 (supplied by the caller; live count not re-pulled)'
rail: 'Rung 1 — AUTO-generated English captions, flattened to one line, no timestamps'
transcript_artifact: /home/godsend/.hermes/profiles/dion/cache/scratch/hskoK2y9TNk_flat.txt
transcript_chars: 22649
primary_snapshots: /home/godsend/.hermes/profiles/dion/cache/scratch/hskoK2y9TNk_primaries/
primary_manifest: /home/godsend/.hermes/profiles/dion/cache/scratch/hskoK2y9TNk_primaries/MANIFEST.md
register_vocabulary: 'VERIFIED = literal on the saved tape or literal in a fetched primary · HYP = our inference or mapping · EST = estimate or supplied metadata · A = analogy · C = conjecture or assertion with no primary · POETIC = figurative · untagged = treat as myth'
verdict_vocabulary: 'SUPPORTED / OVERSTATED / MISATTRIBUTED / UNVERIFIED — one per claim, applied against the primary, not against plausibility'
source_class: 'Secondary commentary by a creator who pitches a product. The last third is a Dropstone testimonial and CLI walkthrough. The run it describes is a self-published research result from Blankline, the company behind Dropstone.'
filed_by: Dion
dedupe_verdict: 'Zero prior hits for hskoK2y9TNk in YT_TRANSCRIPTS/, drops/ and CANON_INDEX.md, run by the caller before this drop. No re-upload question.'
status: 'Working drop (pre-adversarial). Local only — no GitHub push, no NotebookLM, no audio.'
---

# Canon Drop — `hskoK2y9TNk` — Dropstone, the notebook, and the 26-circle packing

**Date:** 2026-11-27 · **Filed by:** Dion
**Source:** https://www.youtube.com/watch?v=hskoK2y9TNk — channel **Epic Programmer**, uploaded **2026-11-27**, **1492 s (24:52)**, 28.7K views as supplied. The live oembed title matches the brief: *AI Found Something It Shouldn't Be Able To Find*. A search-index variant renders it *AI Found Math It Shouldn't Be Able To Find*; both overclaim, and the drop cites the oembed form.
**Tape:** `cache/scratch/hskoK2y9TNk_flat.txt`, 22,649 chars, one line, no timestamps. That is about 15 characters per second over 24.9 minutes, consistent with near-continuous auto-captioning. The text opens on the hook and closes on the call to run the code, so it reads end to end; **cue coverage cannot be measured without timestamps** `[EST]`. Visuals were **not audited**; on-screen items exist here only as narration.
**ASR drift:** *Erwin Louverrier* is Urbain Le Verrier; *Pacomania* is Packomania; *enlisted failures* is a garble inside a model quote; *It's not a test code* is almost certainly *It's not a SOTA*; *Fast, Pro, and Heavy* are Dropstone tier names, not model names. Quoted spans preserve the tape spellings and are not repaired.
**Dedupe:** zero prior hits in `YT_TRANSCRIPTS/`, `drops/` and `CANON_INDEX.md`.

---

## §1. What the video is a retelling of

The tape is a retelling of one Blankline research write-up and its public repository, framed by a history-of-science essay and closed by a product pitch. The write-up supplies every number in the run; the history supplies the explanatory frame.

| Id | Source | Date | Role in the tape |
|---|---|---|---|
| **T1** | *Extrapolation Under an Exact Verifier: n = 26 Circle Packing*, Blankline — https://www.blankline.org/research/extrapolation-under-an-exact-verifier | Published 2026-08-31; updated 2026-11-26 | The spine. Supplies the 91 attempts, the 77th-attempt jump, the exact-penalty diagnosis, the contact-graph proof, the provenance split, the six higher results, and the cold control |
| **T2** | Repository `blankline-org/extrapolation-n26` — https://github.com/blankline-org/extrapolation-n26 | Commits 2026-08-31 to 2026-11-26 | Artifacts: coordinates, verifier, 91-attempt archive, 214,223-byte reasoning log, `loop/`, `control/`. The README and the `writeup/` markdown carry the 26 Nov control update |
| **T3** | `results/archive-circle-packing-26.heavy.json` and `results/reasoning-live.heavy.log` in T2 | Run 2026-08-21/22 | The run record. The exact-penalty sentence and the attempt-77 diagnosis are literal here |
| **T4** | *AlphaEvolve: A coding agent for scientific and algorithmic discovery*, Novikov et al., arXiv:2506.13131 — https://arxiv.org/abs/2506.13131 | 2025 | The DeepMind comparison. Reports the n = 26 improvement to 2.635; the exact 2.63586276 is the value in AlphaEvolve's published results file, as tabulated in T1, at atol = 0 |
| **T5** | *Patients with hippocampal amnesia cannot imagine new experiences*, Hassabis, Kumaran, Vann & Maguire, PNAS 104(5):1726–1731 — https://doi.org/10.1073/pnas.0610561104 | 2007-01-30 | The imagination study: five patients, ten controls, the beach cue, the fragmented-scene finding |
| **T6** | Einstein to Jacques Hadamard, 1945, printed as a testimonial in Hadamard, *An Essay on the Psychology of Invention in the Mathematical Field* (Princeton, 1945); reprinted in *Ideas and Opinions* | 1945 | The combinatory-play sentence |
| **T7** | Janssen & Renn on the Einstein-Besso manuscript; *Physics Today* 68(11), *Arch and scaffold*; Einstein Papers, Vol. 4 | 2015–2022 | The 1913 calculation at 18 arc seconds, the "virtually identical" method, the "heavy heart" |
| **T8** | Abraham Pais, *Subtle is the Lord* (Oxford, 1982), p. 253, as quoted in the Christie's lot essay for the Einstein-Besso manuscript | 1982 | The heart-palpitations line and the strongest-emotional-experience judgement |
| **T9** | *Dropstone 1.7: Technical Report*, Blankline — https://www.blankline.org/research/dropstone-1-7-technical-report | July 2026 | The tiers: Fast is DeepSeek V4 Flash 0731, Pro is GLM-5.2, Heavy is Kimi K3; Dropstone is a runtime, not a foundation model; consumer sessions train by default |
| **T10** | AMD press release, *AMD to Acquire World Labs* — https://ir.amd.com/news-events/press-releases/detail/1299/ | 2026-09-28 | The $8.2 billion figure |
| **T11** | `karpathy/autoresearch` README — https://github.com/karpathy/autoresearch | March 2026 | The five-minute training loop, about 12 experiments per hour, about 100 overnight |
| **T12** | Hassabis on the Einstein test, interview reported by OfficeChai | February 2026 | The 1911 knowledge-cutoff proposal |
| **T13** | Alpöge–Claude Riemann hypothesis proof, AP and Wikipedia | 2026-11-20/21 | The Riemann in the news line and the Lean verification |
| **T14** | Le Verrier and Vulcan, standard history (Wikipedia: Le Verrier; Vulcan) | 1846–1859 | The 43 arc seconds, Neptune, Vulcan |

**Identification evidence.** The tape's numbers are not generic. It reproduces the archive's exact attempt-77 interval (2.627772 to 2.635871), the 12:36 UTC timestamp, the 18 invalid attempts, the 214,223-byte log and line 3018, the 48/14 versus 58/20 contact counts, and the 2.78e-17 violation. The fingerprint matches this run and no other artifact fetched here. The video is a retelling of T1–T3, not an independent investigation.

**What the video adds.** Two things the paper does not supply: the Einstein frame, and a Dropstone product pitch. T1 cites Hassabis and complementary learning systems only as design motivation, not as mechanism. Both additions are analysed below. Neither is evidence for the result.

---

## §2. Claim inventory, tagged and verdicted

Tags mark the claim's own register. Verdicts are against the fetched primary, not against whether the claim sounds right.

| # | Tape claim (literal span) | Register | Primary check | Verdict |
|---|---|---|---|---|
| **C1** | "On the 22nd of August, 2026, one tried." | `[VERIFIED]` | Archive timestamps: first attempt 2026-08-21T13:58Z, attempt 77 2026-08-22T12:36Z, last attempt 22:19Z. The run spans 21–22 August; the decisive attempt is on the 22nd | **SUPPORTED** |
| **C2** | "on its 77th attempt" | `[VERIFIED]` | Archive index 77; timestamp 12:36:04Z | **SUPPORTED** |
| **C3** | "it had been stuck for 40" | `[VERIFIED]` | T1: «roughly 40 attempts with smaller incremental improvements»; best 2.622 at #36, 2.6278 at #76 | **SUPPORTED** |
| **C4** | "Nothing in the log has used an exact penalty formulation." | `[VERIFIED]` | Literal in the #77 `DIAGNOSIS` field of T3; T1 §7.1 confirms the penalty optimizer | **SUPPORTED** |
| **C5** | "2.6278 became 2.63587" | `[VERIFIED]` | T3 #76 2.627772, #77 2.635871; T1 §5 | **SUPPORTED** |
| **C6** | "Past AlphaEvolve's published packing." | `[VERIFIED]` | AlphaEvolve 2.63586276; #77 2.635871, a margin of 8.4e-6 | **SUPPORTED**, with the tolerance caveat in §4 |
| **C7** | "18 of its 91 attempts scored zero" | `[VERIFIED]` | T1: 73 valid, 18 invalid, all 18 at zero | **SUPPORTED** |
| **C8** | "The first five are short and vague. 118 characters." | `[VERIFIED]` | T1 §5.1: the first five `AVOID` blocks are 118, 0, 232, 492 and 433 characters. The 118 is the first, not the set; the tape's next sentence, "Then, nothing.", is the zero | **SUPPORTED** |
| **C9** | "The last ones run up to 2,000." | `[VERIFIED]` | T1 §5.1: the last five are 467, 464, 1,526, 1,475 and 1,998 characters | **SUPPORTED** |
| **C10** | "Seven syntax error cutoffs. Two crashes from changing a constant. Four failed starts from a grid layout." | `[VERIFIED]` | T1 §5.1: 7 syntax/parse failures, 2 const-reassignment throws, 4 `lattice-init` invalid finals. `grid` is the tape's gloss of `lattice` | **SUPPORTED** |
| **C11** | "There were actually eight early crashes in the log, but one was a different kind of error." | `[VERIFIED]` | T1 §5.1: eight import-stage failures; #43 is a `ReferenceError`, not a syntax error | **SUPPORTED** |
| **C12** | "After every attempt, the AI wrote itself a note. Every note had the same headings." | `[EST]` | T3: 23 of 91 attempts have an empty `analysis`; 46 of 91 contain an `AVOID` block (T1 §5.1). The notebook is real but sparse | **OVERSTATED** |
| **C13** | "On the next attempt, the most relevant notes were handed back to it." | `[VERIFIED]` | T1 §7: records most relevant to the strategy are retrieved and supplied | **SUPPORTED** |
| **C14** | "The model never changed. Only the notebook grew." | `[VERIFIED]` | T1 §7: parameters remain fixed; only the external memory changes | **SUPPORTED** |
| **C15** | "The machine's own best was 2.63597." | `[VERIFIED]` | T1 §8: the loop's best archived score is 2.635907462261; the final is 2.635917599028. The tape's 2.63597 is a digit transposition, and it would put the loop above FICO Xpress at 2.63591551, which T1 says it is below | **OVERSTATED** |
| **C16** | "The final number is a little higher because of two more steps after the loop, with no AI in either." | `[VERIFIED]` | T1 §8: LP radii plus relocation, +4.73e-6; seed and parent sweep, +5.40e-6; neither contains a model | **SUPPORTED** |
| **C17** | "The best known is about 2.63598." | `[VERIFIED]` | Packomania record 2.635983084919 | **SUPPORTED** |
| **C18** | "6 published results score higher." | `[VERIFIED]` | T1 §2 and §11: six published results exceed the reported value | **SUPPORTED** |
| **C19** | "One of the 6 used no AI at all, just simulated annealing" | `[VERIFIED]` | T1 §10: hybrid simulated annealing with Lévy flights, 2.6359372, no model in the loop | **SUPPORTED** |
| **C20** | "Another came from one person, working alone in July 2025." | `[VERIFIED]` | T1 §10: the researcher using the handle `Alex`, 2.63592717, July 2025, self-built multi-agent framework | **SUPPORTED** |
| **C21** | "48 contacts. The record family has 58. 14 wall contacts against 20." | `[VERIFIED]` | T1 §4.1 table: exactly 48/14 and 58/20 | **SUPPORTED** |
| **C22** | "The worst error anywhere is a decimal point. 16 zeros and then a two." | `[VERIFIED]` | T1 §2: maximum constraint violation 2.78e-17, i.e. 0.0000000000000000278 | **SUPPORTED** |
| **C23** | "500 seconds of random nudges gained 3 ten millionths." | `[VERIFIED]` | T1 §4.2: 500 s of perturbations and simulated annealing recovered about 3e-7 | **SUPPORTED** |
| **C24** | "It stopped and asked itself whether it already knew the answer." | `[HYP]` | T1 §3: «The retrieval cue was supplied by the harness by design.» The trace is attempted retrieval, reported failure, further retrieval, then strategy change. It does not establish spontaneous retrieval | **OVERSTATED** |
| **C25** | "All 91 attempts, every failure, every note, and the full reasoning." | `[VERIFIED]` | T2 publishes all 91 attempts with analysis, code, score, reason and timestamp. The full reasoning log is 214,223 bytes for the decisive attempt, not for all 91 | **OVERSTATED** |
| **C26** | "The run in this story took about 32 hours." | `[VERIFIED]` | T1: 32.4 hours; T3 first-to-last timestamp 32.35 hours | **SUPPORTED** |
| **C27** | "about $50 of model calls" | `[EST]` | No cost figure in T1 or T2 | **UNVERIFIED** |
| **C28** | "on an ordinary computer" | `[EST]` | No hardware record in T1 or T2 | **UNVERIFIED** |
| **C29** | "Dropstone Heavy, which is built on an open model called Kimi, trained once, then frozen." | `[VERIFIED]` | T2: «The model used was Dropstone Heavy 1.7 (Kimi 3), served from our own endpoint with its parameters frozen. We did not train the model» The training is Moonshot's | **MISATTRIBUTED** |
| **C30** | "six copies of the AI at once, all sharing one notebook", and "Five of them then wrote notes" | `[VERIFIED]` | T1 §7.2: six parallel workers; all six read the archive as it existed at launch; five later wrote records citing failures that had not occurred | **SUPPORTED**, with the note that T1 says «as it existed at launch», not "empty" |
| **C31** | "With the notebook, it went from half of them to all of them. Without it, it scored zero." | `[VERIFIED]` | T1 §9.1: treatment 50 percent to 100 percent on transfer, control 0 percent; overall treatment 75 percent | **SUPPORTED** |
| **C32** | "on tasks with nothing to learn, the notebook made no difference at all" | `[VERIFIED]` | T1 §9.1: 100 percent versus 90 percent, recorded as «not supported». That is a 10-point gap, not zero | **OVERSTATED** |
| **C33** | "Before this video went up, they ran it." The tape gives "91 tries, 10 minutes each". "Not one of them found that shape." "Not one even reached AlphaEvolve's score." | `[VERIFIED]` | T2 `control/` run of 2026-11-21: 91 memory-free restarts at 600 s each, 0 of 91 reached 2.63586276, best 2.635828761, 0 of 91 in the target contact graph | **SUPPORTED** |
| **C34** | "That's one search method, on one kind of computer." | `[VERIFIED]` | T2 `control/README.md`: one method, one budget, 24 CPU threads | **SUPPORTED** |
| **C35** | "The code is public, including that test." | `[VERIFIED]` | T2 is MIT-licensed; `control/` contains the code, a Colab notebook and all 91 packings | **SUPPORTED** |
| **C36** | "they published everything" | `[VERIFIED]` | T2 publishes the archive, the decisive trace and both model-free stages. The hosted T1 page is stale on the control, but the repository write-up is current | **SUPPORTED**, with the version-skew note in §9 |
| **C37** | "The exact step came from a person reading those notes." | `[VERIFIED]` | T1 §8: the LP formulation was developed by the human authors after the model repeatedly identified the opportunity but never implemented it | **SUPPORTED** |
| **C38** | "No single prompt in their runs produced that combination. The notebook assembled it, one attempt at a time" | `[VERIFIED]` / `[HYP]` | T1 §7.1: none of the zero-shot prompts produced the combination; the loop assembled the strategy. "The notebook assembled it" is the paper's interpretation, not an ablation | **SUPPORTED** as the paper's claim; the causal reading is `[HYP]` |
| **C39** | "the strategy was retrieved. The configuration was not." | `[VERIFIED]` | T1 §7.1: «The strategy was retrieved from published evidence; the resulting configuration was generated by the search.» The tape compresses the second clause | **SUPPORTED** |
| **C40** | Title: *AI Found Something It Shouldn't Be Able To Find* | `[C]` | T1: «We make no broader claim about memory and extrapolation»; one problem and one run; an existence result. No capability bound is stated or crossed | **OVERSTATED** |
| **C41** | "A frozen AI with a notebook beat Google DeepMind" | `[VERIFIED]` | Numerically true against AlphaEvolve's 2.63586276, but AlphaEvolve was not the record, the published number includes two model-free stages, and the tolerance is not identical | **OVERSTATED** |
| **C42** | "It's not a test code." | `[VERIFIED]` | ASR for *not a SOTA*; T1 §11: «The reported value is neither a record nor state of the art.» | **SUPPORTED**, after ASR repair |
| **C43** | "Blankline has now released the loop itself. The notebook, the referee, the whole machine. It runs on Dropstone." | `[VERIFIED]` | T2 `loop/` released 2026-11-24; it runs on the reader's machine with a Dropstone API key; T1 §7.2: «It is not a Dropstone product feature» | **SUPPORTED**, with that correction |
| **C44** | "To start, you install Dropstone with one line, add an API key" | `[EST]` | The research loop is `npm install` plus a `.env` file; the product CLI install is a different artifact | **OVERSTATED** |
| **C45** | "They don't own a model. They use open source models called Fast, Pro, and Heavy." | `[VERIFIED]` | T9: Dropstone is not a foundation model; Fast, Pro and Heavy are tiers running DeepSeek V4 Flash 0731, GLM-5.2 and Kimi K3. The models are open-weight, not open-source, and K3's weights were not public at the report's writing | **MISATTRIBUTED** |
| **C46** | "Claude can simply restrict your research in the middle of something very important" and "there's a very high chance they use your research internally to train their models" | `[C]` | No citation on the tape; not checked against Anthropic's terms here. T9 says Dropstone's own consumer sessions improve the open model by default unless disabled | **UNVERIFIED** |
| **C47** | "For problems like this one, I'd suggest Fast with maximum reasoning effort." | `[C]` | A personal recommendation. The run used Heavy; no head-to-head is offered | **UNVERIFIED** |
| **C48** | "Turn off session sharing in your dashboard to keep your work private." | `[VERIFIED]` | T9: consumer sessions help improve the open model by default and can be turned off in settings | **SUPPORTED** |
| **C49** | "The same project also searches for binary sequences with almost no echo, the kind used in radar." | `[C]` | Not in T1 or T2; no binary-sequence artifact in the repository tree | **UNVERIFIED** |
| **C50** | "In 1859, the French astronomer Erwin Louverrier found a problem with Mercury. The leftover is 43 arc seconds per century" | `[VERIFIED]` | Le Verrier's 1859 Mercury work; the 43 arc seconds per century anomaly is standard. "Erwin" is ASR for Urbain | **SUPPORTED** |
| **C51** | "roughly the width of a coin seen from a hundred meters away" | `[EST]` | 43 arc seconds at 100 m subtends about 2.1 cm | **SUPPORTED** |
| **C52** | "Thirteen years earlier, Louverrier had used a wobble in Uranus' orbit to predict an unseen planet. An astronomer found Neptune right where he said." | `[VERIFIED]` | 1846 prediction and Galle's observation; thirteen years before 1859 | **SUPPORTED** |
| **C53** | "He predicted a hidden planet inside Mercury's orbit and named it Vulcan." "It doesn't exist." | `[VERIFIED]` | Vulcan was proposed, repeatedly reported and never confirmed | **SUPPORTED** |
| **C54** | "Grossmann, you must help me or else I'll go crazy." | `[VERIFIED]` | The standard Einstein-Grossmann account of 1912 | **SUPPORTED** |
| **C55** | "a geometry of curved spaces that Bernhard Riemann had worked out in 1854" | `[VERIFIED]` | Riemann's 1854 habilitation lecture | **SUPPORTED** |
| **C56** | "He gave them up, as he put it later, with a heavy heart. Three years later, he went back to them." | `[VERIFIED]` | Einstein's November 1915 paper: he parted from general covariance «with a heavy heart» with Grossmann | **SUPPORTED** |
| **C57** | "On 18 November 1915, Einstein presented his calculation for Mercury. His theory, with nothing tuned to fit, gave 43 arc seconds per century." | `[VERIFIED]` | Prussian Academy, 18 November 1915; the 43 arc second result | **SUPPORTED** |
| **C58** | "he told a colleague that the result gave him heart palpitations. His biographer called it the strongest emotional experience of his scientific life" | `[VERIFIED]` | Pais, *Subtle is the Lord*, p. 253: «by far the strongest emotional experience in Einstein's scientific life»; Fokker is the colleague | **SUPPORTED** |
| **C59** | "In 2007, a young neuroscientist at University College London went looking." "His name was Demis Hassabis." "A few years later, he'd co-found DeepMind." | `[VERIFIED]` | PNAS 2007, Wellcome Trust Centre for Neuroimaging, UCL; DeepMind co-founded in 2010 | **SUPPORTED** |
| **C60** | "He and his colleagues asked a small group of patients to imagine something simple." "most of them couldn't do it" | `[VERIFIED]` | T5: five patients with bilateral hippocampal damage and ten matched controls; four of the five patients were impaired | **SUPPORTED** |
| **C61** | "As for seeing, I can't really, apart from just sky. I can hear the sound of seagulls and of the sea. The only thing I can see is blue." | `[VERIFIED]` | T5 Fig. 1 patient transcript, compressed with an ellipsis. Verified via two independent reproductions of the figure text | **SUPPORTED**, as an excerpt |
| **C62** | "They could still talk and reason and recall facts" | `[VERIFIED]` | T5: language, perceptual, verbal fluency and executive function within normal range; premorbid semantic memory intact | **SUPPORTED** |
| **C63** | "Imagination isn't making something from nothing. It's taking pieces you remember and arranging them in a way you've never seen." | `[HYP]` | T5's constructive-simulation reading: the hippocampus supplies the spatial context into which disparate elements are bound | **SUPPORTED**, as interpretation |
| **C64** | "combinatory play seems to be the essential feature in productive thought" | `[VERIFIED]` | T6, Einstein to Hadamard, 1945 | **SUPPORTED** |
| **C65** | "In 1945, a mathematician surveyed famous scientists about how they think." | `[VERIFIED]` | Hadamard's book and Einstein's letter are 1945; the survey's circulation date is earlier, which the tape compresses | **SUPPORTED** |

**Verdict counts:** SUPPORTED 50 (C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C13, C14, C16, C17, C18, C19, C20, C21, C22, C23, C26, C30, C31, C33, C34, C35, C36, C37, C38, C39, C42, C43, C48, C50, C51, C52, C53, C54, C55, C56, C57, C58, C59, C60, C61, C62, C63, C64, C65). OVERSTATED 8 (C12, C15, C24, C25, C32, C40, C41, C44). MISATTRIBUTED 2 (C29, C45). UNVERIFIED 5 (C27, C28, C46, C47, C49). Total 65.

---

## §3. The numbers, checked

The tape's numerical spine is accurate to the archive almost everywhere. This table isolates the figures, because a video like this stands or falls on them.

| Figure | Tape | Primary | Verdict |
|---|---|---|---|
| Attempts | 91 | 91 over 32.4 hours (T1 §5) | exact |
| Decisive attempt | 77th | Index 77; 2026-08-22T12:36:04Z (T3) | exact |
| Stuck window | 40 attempts | about 40 attempts, #36 to #76 (T1 §5) | exact |
| Jump | 2.6278 to 2.63587 | 2.627772 to 2.635871 (T3) | exact |
| Loop's own best | 2.63597 | 2.635907462261 (T1 §8) | **wrong**, by 6.3e-5 |
| Final result | not stated | 2.635917599028 (T1 §2) | the tape says "a little higher"; consistent with 2.635907, incoherent with the tape's 2.63597 |
| AlphaEvolve | "past" | 2.63586276 at atol = 0 (T4; T1 table) | exact margin, different tolerance |
| Record | about 2.63598 | 2.635983084919 (Packomania) | exact |
| Results above | 6 | 6 (T1 §2, §11) | exact |
| Zero scores | 18 of 91 | 18 invalid of 91 (T1 §5) | exact |
| Contacts | 48 and 58 | 48 and 58; wall contacts 14 and 20 (T1 §4.1) | exact |
| Worst violation | 16 zeros and a two | 2.78e-17 (T1 §2) | exact |
| Local-search gain | 3 ten millionths | about 3e-7 (T1 §4.2) | exact |
| Run time | about 32 hours | 32.4 hours (T1 §5) | exact |
| Reasoning log | 214,000 bytes, line 3018 | 214,223 bytes, L3018–3024 (T1 §3) | exact |
| Cold control | 0 of 91, 91 tries at 10 minutes | 0 of 91, best 2.635828761, 60 structures (T2) | exact |
| Model calls | about $50 | no figure in T1 or T2 | unverified |

**The one number that matters.** The tape's 2.63597 is not a rounding of 2.635907. It is a transposition that moves the loop's own score above FICO Xpress at 2.63591551. T1 is explicit that the loop's best is below FICO and that the FICO margin depends on the two model-free stages. The tape's next sentence, that the final number is "a little higher", is incoherent against its own figure, because 2.6359176 is lower than 2.63597. This is the clearest internal contradiction in the script, and it is the kind of error a read-back would catch.

---

## §4. The title and the DeepMind comparison

**Title verdict: OVERSTATED.** The paper's claim is narrow and three-part: the configuration is not retrieved, not interpolated, and not reachable by local descent from the incumbent. It is one instance, one problem, one run. T1 says so at the top: «We make no broader claim about memory and extrapolation.» It even names the condition under which the result would shrink to a known phenomenon: if memory-free restarts recover the structure at a meaningful rate, the result would then amount to «a demonstration of multimodality in circle packing».

*Shouldn't be able to find* asserts a capability bound. No such bound is stated in T1, and the cold control does not establish one: it tests one search method at one budget, and the authors say so. The honest headline is the paper's own: a frozen model with an external memory produced a packing provably non-isomorphic to the published record, once, under an exact verifier. That is interesting. It is not a system finding something it shouldn't be able to find.

**The DeepMind comparison, like for like.**

| Dimension | AlphaEvolve (T4) | This run (T1–T3) | Like for like? |
|---|---|---|---|
| Problem instance | 26 circles in the unit square, maximise sum of radii | Same | **Yes** |
| Metric | Sum of radii | Same | **Yes** |
| Baseline status | 2.63586276, an improvement on 2.634, but below the Packomania record of 2.635983 | 2.635917599028, below six published results | **No** — beat DeepMind is not beat the record |
| Compute budget | A Gemini-based evolutionary coding agent; the paper does not disclose a comparable per-run budget | 91 attempts, up to 600 s each, 32.4 hours, about $50 asserted | **No** — the budgets are not matched, and the smaller one favours the run |
| Verification tolerance | atol = 0 | maximum violation 2.78e-17; T1 says AlphaEvolve's standard is stricter | **No** — close, but not identical |
| What the number contains | The AlphaEvolve construction | A model loop, a human-authored LP and relocation step, and a model-free seed sweep | **No** — the final number is a three-stage product |

So the comparison is like for like on the problem and the metric, and unlike on baseline status, budget, tolerance and provenance. The tape's body knows most of this: it says "It's not a test code", lists six higher results, and names the simulated-annealing and solo-researcher results. The title does not. **Cite the body sentence, never the title.**

---

## §5. Verdict — strongest point and weakest joint

**★ STRONGEST: the numerical reconstruction is faithful, including the details that damage the video's own framing.**

C1–C11, C13, C14, C16–C23, C26, C30, C31, C33–C39 and C42 are exact against T1–T3. That includes the details a summary would smooth away: the 12:36 UTC timestamp, the 2.627772 to 2.635871 interval, the 18 invalid attempts, the seven syntax errors against eight import failures, the 48/14 versus 58/20 contact counts, the 2.78e-17 violation, the 214,223-byte log, line 3018, the 60 distinct structures in the cold control, and the 0 of 91. The video also reproduces the two facts that most undermine its title: the result is "not a test code" (not a SOTA) and six published results are higher. A creator who includes the deflations is doing something rare, and it is the reason this drop can use the tape as a map to the primary rather than as a source of claims.

**★ WEAKEST: the causal claim that the notebook produced the improvement.**

The video's mechanism is: the notebook records what worked and what failed, the model retrieves it, and the retrieval produces the jump. T1 supports the *presence* of that loop and the *content* of the notes. It does not support the causal isolation, and it says so in three places:

- «We make no broader claim about memory and extrapolation.»
- In §8, after attributing +1.01e-5 to two model-free stages: «This result weakens the strongest version of our hypothesis about the role of external memory.»
- In §9.3, the shuffled-memory arm, which is the direct test of whether the effect is the content of the memory or merely extra prompt context, is «Not yet run.»

The cold control does not close this gap. It removes the model, the notebook **and** the incumbent together. It shows that one plain search method, at the loop's inner budget, did not find the structure. That is a useful negative result about that search method. It is not a memory-on versus memory-off comparison with the model in the loop, and it cannot attribute the attempt-77 jump to the notebook rather than to the model's own sampling, the verifier's gradient, or the extra context the notes supply.

The paper also contains the counterexample the video notices but does not connect: five of six parallel workers wrote false records into the shared notebook, citing failures that had not happened. The paper calls memory integrity its highest-priority risk because of it. A store that can be poisoned by its own writers is not a mechanism that reliably produces improvement; it is a mechanism that sometimes does and sometimes invents.

**Runner-up weakest: C15, the 2.63597 figure.** It is not a rounding; it flips the comparison with FICO Xpress and contradicts the next sentence. It is the one place where the video's otherwise excellent number discipline fails.

---

## §6. Mapping to the house framework, with the Friction Rule applied

House-side terms are italicised rather than quoted, so every double-quoted span in this file remains a tape span. The mapping is deliberately narrow: the tape's domain is one search run, and rows that would require inventing a correspondence were not written.

| # | Dimension | Source (on tape) | House | Status |
|---|---|---|---|---|
| **R1** | **Is the notebook a non-rolling ledger?** | "After every attempt, the AI wrote itself a note"; "On the next attempt, the most relevant notes were handed back to it"; "The model never changed. Only the notebook grew." | The *non-rolling ledger*: an append-only record that cannot be rewritten after the fact, author-attributed, with corrections entered as new entries and an outside checker able to audit it. Its job is to record whether the goal moved, not to supply the goal | **`[CRITICAL DIVERGENCE]`.** Same shape, different guarantee. The notebook is written by the same model it records; it is consolidated and summarised between attempts rather than appended; retrieval is relevance-ranked, so most of it is never read; 23 of 91 attempts have no analysis and only 46 of 91 have an `AVOID` block. The independent record is the harness-written archive, not the notebook, and the video conflates the two. The paper's six-worker episode is the proof: five workers wrote false records into the shared store, and the paper calls memory integrity its highest-priority risk. **Demotion:** *ledger* drops to *self-authored, mutable experience store* `[HYP]`. **The row cuts at the house too:** the house's SecondBrain ledger is also agent-authored; its independence comes from file-creation-only permissions and timestamp monitoring, not from the writer. The Dropstone case is the house's own failure mode at a different layer, and the house should not cite it as a ledger success |
| **R2** | **Is the note file procedural memory?** | "Diagnosis. What went wrong. Technique. What it tried. Plan. What to try next. And avoid. A list of its own mistakes."; the `AVOID` blocks grow from 118 to 1,998 characters | *Procedural memory*: procedure laid down by experience, carrying what was done and what happened, so the next run starts from the accumulated record rather than a blank sheet | **`[CONVERGENT]` at content, with a demotion at warrant.** This is the closest case in the corpus to genuine procedural memory: the notes record outcomes of episodes and are retrieved to bias the next attempt, and the fastest-growing section is the failure list, which matches the house's claim that failure is the compressible part. But the notes are the model's summary, not the verifier's record; the paper's one fidelity check (the count of seven syntax errors) is a single count, not a reliability result. **Demotion:** *procedural memory* drops to *self-summarised procedural memory* `[HYP]` until the notes are checked against the archive at scale |
| **R3** | **Constraint or restraint — what is the referee?** | "A short program, about 40 lines, checks every circle." "The AI never sees that program." "It can't argue with it or flatter it."; but also "the notebook told the AI which climbs had worked" | *Constraint versus restraint*: constraints are external structure (permissions, interfaces, records); restraint is the line the agent holds itself. The house treats constraints as load-bearing and restraint as what makes an agent legible | **`[DIVERGENCE]`.** The referee is a clean instance of a *constraint*: exact arithmetic, no access, zero for invalid. The notebook is not a second referee and not *restraint*: it has no enforcement power, only retrieval bias. The tape slides from one to the other, and the slide is the mechanism by which the notebook gets credit for the verifier's work. **Demotion:** *referee* is reserved for the verifier; the notebook is a *record*, not a constraint |
| **R4** | **Is the different contact graph an epiplexic residue?** | "the highest peak was on a different hill"; "48 contacts. The record family has 58"; "So, the two packings are provably different." | *Epiplexity* as a topological map rather than a procedure; constraint rather than application; the ledger records whether the goal moved. A different basin can be the residue of a different search path | **`[DIVERGENCE]` — the source resists the mapping.** T1 says «Structural difference alone is not the main claim»: circle packing at this scale is multimodal, independent restarts reach different basins, and finding a different contact graph is «relatively easy». The cold control found 60 other structures. A topological difference is therefore cheap; the expensive thing is the *path* that reached this one after 40 stuck attempts. The house's topological-map reading would over-read the structure as evidence of learning. The convergence is at the level of content, not evidence: the `AVOID` list is the compressible failure record, which is the house's epiplexity-as-constraint claim, but the contact graph alone is not |
| **R5** | **Does the run support EILT's identity-as-ledger?** | "The model never changed. Only the notebook grew." | EILT's I(S,t) = L(S,t): identity is the lattice or ledger, not the weights; the autobiography is the operational instantiation, and the ledger certifies provenance, never truth | **`[CRITICAL DIVERGENCE]`.** Architectural convergence: a frozen model whose only change is an external record is a clean instance of identity-as-record rather than identity-as-weights, and that is worth recording. But the guarantee fails. EILT's ledger is append-only, author-attributed, with corrections as new entries; the notebook is consolidated by the actor and read selectively. The six-worker false-memory episode is a direct counterexample to the claim that persistent memory deepens invariants without an independent checker. **Demotion:** I(S,t) = L(S,t) drops to *identity-as-external-record* `[HYP]` for this case; the run is not evidence for the ledger |
| **R6** | **One run or a rate?** | "It's an existence proof. It shows the path exists. It doesn't show how often it works." | The ledger records whether the goal moved; a record is not a rate; one run remains one run | **`[CONVERGENT]`.** The video's explicit limit matches the house's provenance discipline, and it is the sentence to cite. The title contradicts it, which is why the title is the overclaim and the body is the finding |

**Friction count: 2 × `[CRITICAL DIVERGENCE]` (R1, R5) + 2 × `[DIVERGENCE]` (R3, R4) + 2 × `[CONVERGENT]` (R2, R6).** The two critical rows both cut at the house as well as at the source: the house's ledger has the same writer-independence problem unless the monitor is genuinely outside the actor, and the Dropstone notebook is the case that makes that visible.

**Which row matters most: R1.** R5 is the metaphysical version of the same point, but R1 is operational. The video's central move is to treat a notebook the agent writes for itself as if it were a ledger an outside checker can audit. That is exactly the move the house is tempted to make whenever it sees a persistent, versioned artifact. The Dropstone run is a useful mirror because the paper itself supplies the counterexample: the notebook can be poisoned, and the only reason we know is that a separate, harness-written archive exists. If the house ever cites an agent's own notes as ledger evidence, it will have confused a diary with a witness.

---

## §7. Borrowed terms, demoted one register

| Term | Who uses it | Status on the tape | Demotion |
|---|---|---|---|
| *ledger* | House | Absent. The tape says notebook | To *self-authored, mutable experience store* `[HYP]`. The independent artifact is the archive, not the notebook |
| *procedural memory* | House | Absent, but the note structure is close | To *self-summarised procedural memory* `[HYP]`. Content converges; warrant does not |
| *constraint / restraint* | House | The tape has "referee" only | The referee is a *constraint*; the notebook is neither constraint nor restraint. Do not map it to restraint `[A]` |
| *epiplexity* | House | Absent. The tape's "hill" and "landscape" are metaphors | To *basin / topological map* `[A]`. A different contact graph is a different basin, not by itself evidence of epiplexity |
| *combinatory play* | Einstein, via Hadamard | Quoted correctly | To *recombination of retrieved text techniques* `[HYP]`. Einstein's letter is about non-verbal images; the model's notes are text. The mapping is an analogy, not an identity |
| *existence proof* | The paper and the tape | Used correctly | Keep, scoped to one problem and one run |
| *the trick Einstein used* | Tape | `[A]` | No method was transferred from Einstein. The phrase is rhetorical, and the paper's Hassabis/CLS framing is explicitly «architectural rather than biological» |

---

## §8. Product pitch — demonstrated versus asserted

The last third is a Dropstone testimonial. It is not hidden, and it is not the reason the run's numbers fail; it is a separate object and should be judged separately.

| Item | What is demonstrated | What is asserted |
|---|---|---|
| The run | Coordinates, exact verifier, 91-attempt archive, reasoning trace, control, all public, with the repository MIT-licensed | That the notebook caused the improvement; that the method generalises; that the result is a capability finding |
| The loop release | `loop/` is public; `npm install`, `.env`, `npm run evolve`; runs on the reader's machine with a Dropstone API key | That a reader's rerun will find anything comparable. T1 says a rerun is a new stochastic search, not a replay |
| Dropstone Fast recommendation | Nothing on the tape. The run used Heavy | That Fast with maximum reasoning effort is better for problems like this; no head-to-head |
| Cost and hardware | Nothing in T1 or T2 | About $50 of model calls on an ordinary computer |
| Claude warning | Nothing on the tape | That Claude "can simply restrict your research" and that there is a "very high chance" Anthropic trains on it. No citation, and T9 discloses that Dropstone's own consumer sessions train by default unless disabled |
| Tier naming | T9 documents Fast, Pro and Heavy as runtime tiers over DeepSeek, GLM and Kimi models | That they are "open source models called Fast, Pro, and Heavy". They are tier names over open-weight models, and K3's weights were not public at the report's writing |
| Free version | T9 lists Free, $15 and $75 plans | That the free version is sufficient to reproduce anything here |

**What the segment demonstrates:** that Blankline published a working research harness, an exact verifier and a complete run record, and that the creator can use the CLI. **What it does not demonstrate:** that the notebook is the cause, that the method generalises beyond n = 26, that Fast is the right tier, that the cost figure is accurate, or that Claude is the riskier vendor on the evidence given. The pitch is assertion from the mid-roll to the close. That is normal for the genre; it becomes a Canon problem only if a later reader treats the product claims as findings. They are not findings.

**Independent reproducibility, stated precisely.**

- **Artifact-verifiable: yes.** The coordinates, the exact verifier, the contact-graph degree sequences, the archive statistics and the provenance chain can all be checked from the repository without trusting the authors. That is the strongest form of reproducibility the result has.
- **Independently replicated: no.** The run is one run. The cold control is same-team, run on 2026-11-21 and committed on 2026-11-26. No third party has reproduced the discovery.
- **Rerunnable: yes, with caveats.** The loop is public, but a rerun is a new stochastic search; it needs a Dropstone API key; the served model version is not pinned by a hash, so the exact model behind the endpoint can change; and the published number includes two model-free stages that are not in the loop.

The distinction matters because the video says "they published everything" and "Run it yourself." Both are true of the artifacts. Neither makes the *claim about memory* independently verified.

---

## §9. Verification ledger

| Item | Verdict |
|---|---|
| Video identity, title, channel, 1492 s, upload 2026-11-27, 28.7K views | `[EST]` — supplied by the caller; only the oembed title was re-pulled and it matches. Treat the rest as recorded metadata |
| Transcript coverage | `[EST]` — no timestamps, so cue coverage cannot be measured. 22,649 chars over 24.9 minutes is consistent with continuous captioning; the text opens on the hook and closes on the call to run the code |
| That the video retells T1–T3 | `[VERIFIED]` — the attempt-77 fingerprint, the 214,223-byte log, line 3018 and the 48/58 contact counts are unique to this run |
| Attempt count, attempt number, stuck window, jump | `[VERIFIED]` — T1 §5 and T3 timestamps |
| 18 invalid attempts | `[VERIFIED]` — T1 §5; T3 valid flag |
| Seven syntax errors versus eight import failures | `[VERIFIED]` — T1 §5.1 |
| `AVOID` lengths 118 to 1,998 | `[VERIFIED]` — T1 §5.1 |
| "After every attempt" note | **`[OVERSTATED]`** — 23 of 91 attempts have empty analysis; 46 of 91 have an `AVOID` block |
| Loop best 2.635907462261 | `[VERIFIED]` — T1 §8. The tape's 2.63597 is wrong |
| Final 2.635917599028 | `[VERIFIED]` — T1 §2 |
| AlphaEvolve 2.63586276 at atol = 0 | `[VERIFIED-ext]` — T4 and T1's table. Author-reported, re-verified from the published coordinates by T2 |
| Packomania record 2.635983084919 | `[VERIFIED-ext]` — T1 table; Packomania |
| Six published results above | `[VERIFIED]` — T1 §2, §11 |
| Contact counts 48/14 and 58/20 | `[VERIFIED]` — T1 §4.1; T2 `contact-graph.mjs` |
| 2.78e-17 maximum violation | `[VERIFIED]` — T1 §2; T2 `verify.mjs` |
| 3e-7 local-search gain | `[VERIFIED]` — T1 §4.2 |
| 32.4 hours | `[VERIFIED]` — T1 §5; T3 first-to-last |
| Cold control 0 of 91, best 2.635828761, 60 structures | `[VERIFIED-ext]` — T2 `control/run-2026-11-21/results.txt` and `control/README.md`. Run 2026-11-21, same team |
| $50 and "ordinary computer" | **`[UNVERIFIED]`** — no figure or hardware record in T1 or T2 |
| The exact-penalty sentence | `[VERIFIED]` — literal in T3 #77 `DIAGNOSIS` |
| The retrieval attempt at L3018 | `[VERIFIED]` — T1 §3 and T3. The cue was harness-supplied |
| Six-worker false memory | `[VERIFIED]` — T1 §7.2 |
| Coding control 50 to 100 percent versus 0 | `[VERIFIED]` — T1 §9.1 |
| No-learning control 100 versus 90 | `[VERIFIED]` — T1 §9.1 |
| Hassabis 2007, five patients, four impaired | `[VERIFIED-ext]` — T5 abstract and results |
| Patient beach quote | `[VERIFIED-ext]` — T5 Fig. 1, via two independent reproductions; the tape compresses it with an ellipsis |
| Einstein 1945 letter | `[VERIFIED-ext]` — T6 |
| Einstein-Besso 18 arc seconds and "virtually identical" | `[VERIFIED-ext]` — T7; Einstein Papers Vol. 4 |
| heavy heart | `[VERIFIED-ext]` — Einstein's November 1915 paper, as quoted in T7 |
| 18 November 1915 and 43 arc seconds | `[VERIFIED-ext]` — standard history; T7 |
| Pais p. 253, heart palpitations | `[VERIFIED-ext]` — T8, a secondary quotation of Pais |
| AMD World Labs $8.2 billion | `[VERIFIED-ext]` — T10 |
| Karpathy autoresearch, 5-minute runs, about 100 overnight | `[VERIFIED-ext]` — T11 |
| Hassabis 1911 test | `[VERIFIED-ext]` — T12 |
| Alpöge Riemann proof, Lean verification | `[VERIFIED-ext]` — T13 |
| Dropstone tiers and default consumer training | `[VERIFIED-ext]` — T9 |
| open-source models called Fast, Pro and Heavy | **`[MISATTRIBUTED]`** — tier names, open-weight models, K3 weights not public at report time |
| Binary sequences for radar | **`[UNVERIFIED]`** — not in T1 or T2 |

**Version skew in the primary.** The hosted T1 page as fetched on 2026-11-27 still says the matched-budget control is «Not yet run» in §1, §9.3 and §11. The repository's `writeup/extrapolation-under-an-exact-verifier.md` carries a 26 November update that reports the control, and the `control/` directory contains the run. The video matches the repository, not the hosted page. This is a primary-version problem, not a video error: a reader who checks the URL will find the older text and conclude the video invented the control. The drop records the repository commit as the authority and flags the hosted page for correction.

**Claims that failed verification, stated plainly:**

1. **The loop's best was 2.63597.** It was 2.635907462261, and the error flips the comparison with FICO Xpress.
2. **The AI wrote a note after every attempt.** Twenty-three of 91 attempts have no analysis, and only 46 have an `AVOID` block.
3. **The model spontaneously asked whether it knew the answer.** The retrieval cue was supplied by the harness by design; the trace is a prompted retrieval probe, not a spontaneous introspection.
4. **The full reasoning of all 91 attempts is published.** The full trace is for the decisive attempt; the other attempts have structured analysis and code, not full reasoning.
5. **The notebook caused the improvement.** The primary explicitly declines the broader claim and has not run the shuffled-memory arm.
6. **The claim that the run beat Google DeepMind is a like-for-like headline.** Same problem and metric, different baseline status, budget, tolerance and provenance.
7. **Fast, Pro and Heavy are open-source models.** They are tier names over open-weight models, and K3's weights were not public at the report's writing.

---

## §10. Falsifiers

- **F-DROP-1 (causal, house-facing):** if a matched-budget memory-off run *with the same model* reaches the same structure or score at a meaningful rate, the notebook-causes claim falls. *Test:* run `loop/src/evolve.mjs` with the lesson store disabled, 91 attempts, same model and inner budget. The primary does not contain this arm.
- **F-DROP-2 (shuffled memory):** if records from an unrelated problem produce comparable gains, the effect is prompt bulk rather than memory content. *Test:* the shuffled-memory arm named in T1 §9.3, now runnable with `loop/`. T1 says «Not yet run.»
- **F-DROP-3 (title):** if some published capability bound shows a frozen model cannot produce a non-isomorphic structure, the title strengthens; if a different plain-search method finds the structure at the same budget, the *shouldn't* collapses. *Test:* other search methods and more restarts than the 91-try control.
- **F-DROP-4 (SOTA):** if a published result below 2.635917599028 appears, the *not a record* verdict changes. As of filing, six results are higher.
- **F-DROP-5 (2.63597):** if the archive contains a 2.63597 score, the numerical verdict is mine and should be withdrawn. It does not; the best is 2.635907462261.
- **F-DROP-6 (house ledger, house-facing):** if the house can exhibit an agent-written store whose history cannot be rewritten by that agent and whose author is not that agent, R1's critical divergence narrows to a naming dispute. *Test:* name one deployed house store with an independent writer and a non-rewritable log. If none exists, the corpus must stop treating agent notes as ledger evidence.
- **F-DROP-7 (Hassabis frame):** if T1 claims its consolidation mechanism is a computational hippocampus, the video's explanatory frame strengthens. T1 says the opposite: «architectural rather than biological», and «motivation for the experimental design, not as evidence for the result»

---

## §11. Quote gate (mechanical)

Instrument: `cache/scratch/quote_gate_hsko.py`. It extracts every double-quoted span of four characters or more from this file, normalises **only** curly quotes to straight, dash variants to hyphen, and whitespace runs to a single space, then tests each span as a contiguous substring of the saved tape. Case, letters, digits and word order are never altered. Primary-source spans are in guillemets and are tested separately against the saved snapshots.

**Discipline that makes the gate meaningful:** non-tape material is italicised or put in guillemets, never in straight double quotes. The expected count of declared non-tape spans is therefore zero, and every miss is a real defect.

- **Spans checked:** 109
- **Verbatim contiguous hits:** 109
- **Distinct spans:** 103
- **Declared non-tape:** 0
- **Unclassified misses:** 0
- **Positive control (must hit):** `Nothing in the log has used an exact penalty formulation` → HIT (correct)
- **Negative control (must miss):** `The notebook was an append-only ledger audited by an independent checker` → MISS (correct)
- **Primary spans checked:** 23, all 23 exact after the same normalisation
- **Exit code:** 0

**Why the negative control is the right one.** It is the house's ledger claim rendered as a description of the notebook, which is exactly the category error §6, R1 identifies. If the tape contained it, the critical divergence would collapse and this drop would be wrong. It does not.

ASR spellings preserved inside quoted spans and not repaired: `Erwin Louverrier`, `Pacomania`, `enlisted failures`, `It's not a test code`.

- **`canon_drop_lint.py`:** CLEAN — 14 patterns checked, exit 0 (run at filing, re-run after this line was added).

---

## §12. Not established — do not build on these

- **That the notebook caused the improvement.** The primary declines the broader claim, the cold control removes the model as well as the notebook, and the shuffled-memory arm is not run. §5, §6 R1.
- **That the model found something it shouldn't be able to find.** No capability bound is stated or crossed. The paper's claim is one existence result on one problem.
- **That the run beat the state of the art.** Six published results are higher, including one with no model in the loop.
- **That the DeepMind comparison is like for like.** Same problem and metric; different baseline status, budget, tolerance and provenance.
- **That the final number is the model's.** Two model-free stages contribute +1.01e-5, and the loop alone is 2.635907462261.
- **That the notebook is a non-rolling ledger.** It is self-authored, mutable, relevance-retrieved and sparse. §6 R1.
- **That the run is independently replicated.** Artifact-verifiable and rerunnable, not replicated; the control is same-team.
- **That the $50 and "ordinary computer" figures are accurate.** Not in the primary.
- **That Fast, Pro and Heavy are open-source models.** Tier names over open-weight models; K3's weights were not public at the report's writing.
- **That Claude restricts research or trains on it.** No citation on the tape; not checked against Anthropic's terms. Note Dropstone's own consumer default.
- **That the binary-sequence/radar work is part of the same project.** Not in the fetched primary.
- **That the Hassabis 1911 test has been passed.** No registry of attempts is cited.
- **That the video's visual claims were checked.** Visuals were not audited; the transcript is the only evidence base for this drop.

---

## §13. Filing state

**Local only.** No GitHub push, no NotebookLM ingest, no rclone or Drive mirror, no TTS, no outbound send.

**Written:** this drop. **Primaries:** 26 snapshots plus `MANIFEST.md` under `cache/scratch/hskoK2y9TNk_primaries/`. **Index:** one row appended under `flock` on `CANON_INDEX.lock`; `CANON_INDEX.md` backed up first to `CANON_INDEX.md.bak-20261127-dropstone`.

**CANON-ID:** CANON-2026-11-27-hskoK2y9TNk-DROPSTONE-NOTEBOOK.

*Draft compiled by Dion | Status: pre-adversarial working draft | Source read: yes — auto caption track, 22,649 chars, no timestamps.*
