---
title: 'Canon Drop — Welch Labs — "Fei-Fei Li''s $8B World Model" (technical explainer; narrated analysis + PRIMARY on-camera interview clips with World Labs co-founders Fei-Fei Li, Justin Johnson and Ben Mildenhall; the three design decisions behind the Atlas world model — New View Prediction, an autoregressive multimodal diffusion transformer, and training from scratch; filed with a 6-row EILT mapping carrying 2 [CRITICAL DIVERGENCE])'
date: 2026-11-20
filed_by: 'Dion (subagent: canon-drop pipeline)'
source_type: 'YouTube technical explainer (solo narrator = Stephen Welch / Welch Labs) with embedded PRIMARY interview clips of World Labs co-founders, plus a sponsor segment (Hudson River Trading) and a book pitch. The narration is secondhand commentary; the founder clips are primary. Auto-generated caption track only (no manual/publisher track) = the truth source for quotation; treated as ASR-grade near-verbatim.'
video_id: hORDMRY_bZ0
url: 'https://www.youtube.com/watch?v=hORDMRY_bZ0'
channel: 'Welch Labs'
channel_id: UConVfxXodg78Tzh5nNu85Ew
uploader_id: null
title_on_tape: null
upload_date: '2026-11-20'
duration_s: 2571
duration_hms: '42:51'
views_at_pull: '31,541 views / 679 likes (yt-dlp --print, 2026-11-20); category Science & Technology; tags: none'
chapters: 0
intake_trigger: 'Delegated ClawHorde canon-drop subagent, 2026-11-20 — operator-supplied id hORDMRY_bZ0.'
epistemic-registers: 'EST=on-tape fact accurately reported (a thing said/depicted in the episode, checked against the saved caption this session) OR a fact re-checked against a primary source this session (labelled separately) · HYP=a speaker''s forward-looking / attributed / otherwise-not-yet-true claim · A=analogy only (ours) · C=conjecture (no evidence either way) · POETIC=metaphor/framing · RIFF=our speculative synthesis, not the source''s'
register-rule: 'no tag = treat as unverified. Row-STATUS labels [CRITICAL DIVERGENCE] / [DIVERGENCE] / [CONVERGENT-with-guard] / [A] / [DECORATION RISK] are NOT registers. Registers used here are ONLY the six above.'
registers_used: [EST, HYP, A, C, POETIC, RIFF]
transcript-rail: 'RUNG 1 (youtube-transcript-api instance API) `.list()` SUCCEEDED (21 tracks, ALL auto-generated incl. one auto `en`; NO manual/publisher track) but `.fetch(en)` = IpBlocked ×N at the content endpoint. RUNG 2 (yt-dlp --write-auto-subs) reached the endpoints then HTTP 429. RUNG 3 (CDP Chromium :9333 transcript panel, newer `transcript-segment-view-model`) WON — 337 segments scraped out of the live page. RUNG 4 (faster-whisper) NOT exercised. RUNG 0 (Gemini-3.8-flash direct URL ingest) ALSO run as the brief directs; its argument-map prose is a paraphrase and its dedicated VERBATIM QUOTES block was cross-checked against the rung-3 caption.'
rail_evidence_class: 'auto `en` caption, API flag is_generated=True ⇒ ASR-grade near-verbatim, NOT human-caption contract quality. A garble key is mandatory and is in §example.'
transcript: '/data/SecondBrain/Canon/YT_TRANSCRIPTS/hORDMRY_bZ0_fei_fei_li_world_model_2026-11-20.txt (flat, 41,779 chars / 7,256 words / 337 segments)'
transcript_timestamped: '/data/SecondBrain/Canon/YT_TRANSCRIPTS/hORDMRY_bZ0_fei_fei_li_world_model_2026-11-20_timestamped.txt (44,395 bytes, 337 lines)'
raw_segs: '/data/SecondBrain/Canon/YT_TRANSCRIPTS/hORDMRY_bZ0_fei_fei_li_world_model_2026-11-20_raw.json'
structured_extraction: '/data/SecondBrain/Canon/YT_TRANSCRIPTS/hORDMRY_bZ0_fei_fei_li_world_model_2026-11-20_structured_gemini.md (rung-0 model extraction — MODEL-READ, faithful-in-substance NOT verbatim; its argument-map prose is a paraphrase and is NOT a quote source)'
quote-gate: 'see §9 — 138 spans grep-checked against the FLAT caption this session; 137 contiguous hits, 1 repaired to the tape (see §9)'
external_checks: 'AMD investor-relations press release + Bloomberg + CNBC + AFP + Fortune (the $8.2B all-stock acquisition of World Labs, 2026-09-28); worldlabs.ai/blog/atlas + deeplearning.ai/turingpost/dealroom (Atlas architecture); arXiv 2402.15391 (Genie), ai.meta.com V-JEPA (2024-02-15), arXiv 2407.01392 (Diffusion Forcing), arXiv 2606.13676 (Modality Forcing), arXiv 2602.11401 (Latent Forcing), arXiv 2304.06706 (Zip-NeRF), arXiv 2404.02101 (CameraCtrl), Wikipedia/Caltech (Caltech-101), Wikipedia (ImageNet).'
canon-id: CANON-2026-11-20-hORDMRY_bZ0-WELCH-LABS-WORLD-MODEL
related:
  - 'drops/state_of_ai_2026_benaich_N4GpNBxBm-Q_2026-10-30.md (DIFFERENT source — the Nathan Benaich state-of-AI roundup that first asserted the AMD/World Labs deal; its V7 row already flags ~$8.2B all-stock. This drop is the Welch Labs TECHNICAL explainer of the same company — shares the acquisition axis, no shared video id, no shared segment.)'
  - 'drops/HjKRaty1dU4_lecun_memorized_internet_2026-11-19.md (DIFFERENT source — Yann LeCun''s own world-model position. LeCun there explicitly distinguishes his representation-level world model from Fei-Fei Li''s pixel-level one. This drop is the Li/World Labs side of that exact disagreement.)'
  - 'drops/2oYNAEde61o_karaman_when_ai_does_everything_2026-11-02.md (DIFFERENT source — Karaman''s "FA Lee should be congratulated on her exit" [1:20:37] is an unconfirmed candidate reference to this same World Labs exit; this drop supplies the primary confirmation.)'
tags: [world-models, spatial-intelligence, world-labs, atlas, marble, fei-fei-li, nerf, jepa, genie, sora, diffusion-forcing, autoregressive-diffusion, exposure-bias, imageNet, caltech-101, alexnet, amd, robot-learning, real-to-sim-to-real, welch-labs, eilt, friction-rule, caption-rail]
---

# Canon Drop — **Welch Labs**, *"Fei-Fei Li's $8B World Model"* (`hORDMRY_bZ0`)

> **Zero-fabrication note (CA46/CA75).** Every `*"…"*` span below was read from this source's own saved caption artifact **in this session** and gated against the flat transcript (§9). The rail is **rung 3 (CDP transcript panel)** because rungs 1 and 2 were blocked; the served track is **auto-generated**, so quoting earns **near-verbatim-as-served**, not human-caption contract quality — the ASR garble key is in §2 and is mandatory. This episode is a **narrated explainer with embedded primary interview clips**: the founder quotes are the founders' own on-camera words, but the **connective narration is commentary**, and **every external fact it asserts (dates, dataset sizes, model sizes, the acquisition price) is the narrator's claim**, filed here as `[HYP]-as-said` unless §6 records a primary-source re-check. **A finance number carried by a video title is not a verified figure** — the title's "$8B" and the narrator's "8 billion" are checked against the AMD press release in §6.

---

## §0 · Filing verdict — SOURCE CLASS: technical explainer (narration) + primary founder clips

**What this is.** A 42:51 Welch Labs explainer. The narrator (**Stephen Welch**) walks the viewer through three design decisions behind **Atlas**, the second world model from **World Labs** (the company co-founded by **Fei-Fei Li**): (1) **New View Prediction** as the training objective (in place of explicit 3D outputs); (2) an **autoregressive, multimodal diffusion transformer** (causal, interactive) rather than a bidirectional full-sequence video diffusion model; (3) **training from scratch** at scale. Embedded are primary on-camera clips of Li and co-founders **Justin Johnson** and **Ben Mildenhall**; the opening frames a business frame — World Labs founded January 2024, acquired by **AMD** in September 2026. The last ~3 minutes are a Welch Labs book/Patreon pitch, and there is a mid-roll sponsor segment for **Hudson River Trading (HRT)**.

**Why it earns filing.** It is the **technical read** of the World Labs/Atlas story — the world-model design space (NeRF/Zip-NeRF reconstruction → Sora/V-JEPA/Genie generative world models → CameraCtrl → Diffusion Forcing → Atlas) explained with real architecture content, and it is the **Li side** of the same disagreement the LeCun drop (`HjKRaty1dU4`) records from LeCun's own mouth. It is **not** a novelty source for the house; the EILT mapping (§5) is ours and is **not uniform**.

---

## §1 · Identity (re-verified live)

| field | value |
|---|---|
| id | `hORDMRY_bZ0` |
| title (live) | **Fei-Fei Li's $8B World Model** |
| channel | **Welch Labs** (`UConVfxXodg78Tzh5nNu85Ew`) |
| uploaded | **2026-11-20** |
| duration | **2571 s (42:51)** |
| at pull | **31,541 views / 679 likes**; category *Science & Technology*; **tags: none**; chapters: **0** |

Identity re-verified via `yt-dlp --print` (id/title/channel/channel_id/duration/upload match the dispatch). No correction.

---

## §2 · Rail + garble key (mandatory)

**Rail ladder actually run (in order).** Rung 1 `youtube-transcript-api`: `.list()` **succeeded** — 21 tracks, **all auto-generated** (one `en` + 20 auto-translations), **no manual/publisher track**; `.fetch(en)` returned **`IpBlocked`** at the content endpoint. Rung 2 `yt-dlp --write-auto-subs`: reached the subtitle endpoints then **HTTP 429**. Rung 3 **CDP Chromium `:9333` transcript panel** (newer `transcript-segment-view-model`): **WON** — 337 segments scraped from the live page. Rung 4 (faster-whisper) not exercised. **Rung 0 (Gemini-3.8-flash direct URL ingest) ran too**, per the brief: `finish=STOP`, 233,967 video tokens → a 15,893-char structured extraction; **its prose is a paraphrase and only its vendor-quote block is usable, and only after the caption cross-check** — the caption governs everywhere they differ.

**Coverage:** `[0:00 → 42:43]` of 2571 s ≈ **99.7 %**, **337 segments**, **max inter-segment gap 14.0 s**, **0 gaps > 60 s**; flat **41,779 chars / 7,256 words**.

**★ ASR GARBLE KEY (caption forms → referent):**
`Fe Lee` / `Fee Lee` / `Fhei` / `FFE` / `Fay` / `Faye` / `Fee` / `Feefe` / `Feel` → **Fei-Fei Li**; `Warlabs` → **World Labs**; `imageet` / `Imageet` → **ImageNet**; `Nerf` → **NeRF**; `ZipNerf` → **Zip-NeRF**; `Alexet` → **AlexNet**; `Yan Lun` / `Yan` → **Yann LeCun**; `Jeepa` / `VJ Jeepa` / `VJEPO` → **JEPA / V-JEPA**; `Ben Mildenhal` → **Ben Mildenhall**; `Kristoff Lassner` → **Christoph Lassner**; `Jaang` / `Jaw` → **Jia Deng**; `AMA` (at 6:50) → **Meta** [garble; not resolved on tape]; `Juan` → **Wan** (open-source video model) [garble; not named on tape]; `birectional` → bidirectional; `auto reggressive` / `autogressive` → autoregressive; `gausian` → Gaussian; `nancond` → nanosecond; `microscond` → microsecond; `slo` → slog; `largecale` → large-scale.

**★ Rail-integrity note (rung-0 caveat).** The Gemini extraction's own "WHAT WAS NOT ESTABLISHED" block claimed the AMD acquisition is *"a narrative device, dramatized projection, or future-dated scenario … not an actual closed historical transaction."* **That is the model's editorializing and is CONTRADICTED both by the caption** (the narrator presents it as news: *"in September 2026, AI Pioneer and CEO Fe Lee announced an [music] 8 billion acquisition deal with AMD"*) **and by primary sources** (§6: AMD IR, Bloomberg, CNBC). Recorded here because it is exactly the failure mode the brief warns about — the model's prose hardening a real event into a non-event.

---

## §3 · Argument map (the video's own structure)

**§3.1 Intro / business frame (0:00–0:40).** Founders shown; **World Labs founded January 2024**; **"in September 2026 … an 8 billion acquisition deal with AMD"** `[elided]`; the hook *"what makes the lab that built it worth $8 billion"*; three decisions previewed.

**§3.2 Li's data-history arc (0:40–5:23).** **Caltech 101** (the *"9,000 image Caltech 101 data set"*) showed models that *"struggled to generalize to unseen data"*; **ImageNet** (the *"over 14 million images"*) pushed the data frontier to **AlexNet** (2012); Li pivots to robotics + the **BEHAVIOR** simulator; the bottleneck named as *"we don't have good world modeling"* / a *"scarcity of data problem"* in robot learning.

**§3.3 Two lineages of world model (5:23–10:14).** **NeRF / Zip-NeRF** = per-scene 3D reconstruction from 2D images (high quality, static, non-interactive); then **February 2024** generative world models — **Sora** (2024-02-15, "world simulator" framing), **V-JEPA** (2024-02-15, 2M-video feature predictor), **Genie** (2024-02-23, 200,000 hours of gameplay, "foundation world model"). **World Labs' first model, Marble**, generated **3D Gaussian splats** from 2D inputs and *"marble was kind of bottlenecking through this gausian splat representation."*

**§3.4 Decision 1 — New View Prediction (10:14–17:16).** Instead of predicting an explicit 3D structure, predict **what the world looks like from a new camera pose** — 3D moves from an *"explicit prediction target to an implicit state within the model."* Li: *"The next view is our next token."* Contrasts with the bolt-on **CameraCtrl** approach (camera-conditioned video diffusion).

**§3.5 Decision 2 — autoregressive vs bidirectional (17:16–31:02).** Sora/Wan-class models are **bidirectional** diffusion transformers (all frames denoised in lock-step; attention uses past **and future** patches). This is **non-causal → non-interactive**. The LLM fix (**causal mask** / **teacher forcing**) fails on video due to **exposure bias** (continuous RGB, error compounding). **MIT's Diffusion Forcing** (independent per-frame noise levels) reformulates both bidirectional diffusion and teacher forcing as special cases; World Labs' **Latent Forcing** and **Modality Forcing** extend it to per-modality noise. Result: **Atlas = a multimodal autoregressive diffusion transformer.**

**§3.6 Decision 3 — train from scratch (31:02–36:05).** Atlas pretrained from scratch (cost *"on the order of tens of millions of dollars"*); Johnson frames it as the control needed to innovate on **data / architecture / training stack** and calls Atlas *"mainly bottlenecked just by compute."* A **Real-to-Sim-to-Real** pipeline reconstructs a scene from ~**three iPhone videos** into a physics simulator where *"counterfactuals"* can be run.

**§3.7 Close (36:05–42:51).** Li's memoir/immigration arc; the *"visual intelligence … is fundamental to animals, humans and machines"* line; Li *"will join AMD as chief scientist"*; then the Welch Labs book/Patreon sponsor pitch.

**Business footing vs technical footing.** The **technical thesis** is coherent and well-sourced internally (each shaping prior — NeRF, Sora, JEPA, Genie, Diffusion Forcing — is named, dated and explained). The **business footing is a single narrated sentence**: an $8B acquisition, justified as *"a fascinating test case"* for scaling. The episode **never states an Atlas parameter count, token count, or any benchmark number** (§7).

---

## §4 · Selected verbatim quotes (caption-verbatim to the saved artifact; garble preserved)

**Narration (Welch):**
- *"These are the founders of World Labs. Their World Model Atlas lets you do things like this. World Labs was founded in January 2024."* `[0:00]`
- *"But less than 3 years later, in September 2026, AI Pioneer and CEO Fe Lee announced an [music] 8 billion acquisition deal with AMD."* `[0:09–0:17]`
- *"what makes the lab that built it worth $8 billion."* `[0:26]`
- *"Atlas is the second model to come out of World Labs. The team's first effort, Marble, is trained to directly predict 3D representations of the world."* `[0:40]`
- *"the auto reggressive diffusion transformer came into focus."* `[1:11]`
- *"Even one of Fee's own mentors discouraged the effort telling her that she had taken the idea way too far."* `[2:43]`
- *"just as Imageet appeared to be fading into obscurity something truly shocking happened."* `[3:15]`
- *"The winning submission, AlexNet, reignited interest in neural networks"* `[3:38]`
- *"OpenAI unveiled the text to video model Sora on February 15th, demonstrating an unprecedented level of video quality."* `[7:00]`
- *"On the same day, February 15th, 2024, a research team at Meta published VJ Jeepa"* `[7:30]`
- *"Eight days after the Sora announcement, Google DeepMind unveiled a world modeling approach of their own that they called Genie."* `[8:18]`
- *"The bet that these approaches share is that the key to understanding the physical world is to watch lots and lots of videos."* `[9:15]`
- *"A space-time patch is perhaps an overly fancy name for a little block of pixels in our video. In this case of dimension 16x 16x4, each space-time patch is mapped to a single token"* `[18:33]`
- *"Note that this attention head is using information from both past and future frames to figure out how to render the ball in the current frame."* `[20:24]`
- *"This method is known as teacher forcing."* `[23:02]`
- *"The model has not been trained to handle the errors and imperfections from the model's own generation process, resulting in these errors compounding over time and the model going off the rails."* `[24:38–24:47]`
- *"This is known as the exposure bias problem."* `[24:54]`
- *"Video models, on the other hand, output continuous RGB pixel values that are more susceptible to noise and drift."* `[25:02–25:09]`
- *"Atlas generates worlds one new view at a time, adding the newly generated views to its context as it goes, in the same way that auto reggressive LLMs add their newly generated tokens back to their input."* `[29:44–29:52]`
- *"In July 2026, the company demonstrated a real to simtoreal approach"* `[33:17]`
- *"The World Labs AMD acquisition should prove to be a fascinating test case"* `[37:33]`

**Fei-Fei Li (primary clip):**
- *"Because data was really a problem in robotics uh learning in in training"* `[4:16]`
- *"I realized we don't have good world modeling and uh so that scarcity of data problem came out again"* `[4:47]`
- *"video models were not advanced enough to be action conditioned … but the journey is still long."* `[4:24–4:32]`
- *"in language and like what is the what is the analogy in in spatial intelligence? The next view is our next token."* `[11:18]`
- *"visual intelligence is um is whether you call it AGI or not is fundamental to animals, humans and machines."* `[38:37]`
- *"It's not like I woke up and and thought about world models. It's it's because solving visual spatial eventually closing the loop with physical intelligence is um my dream as a scientist."* `[39:14]`

**Justin Johnson (primary clip):**
- *"So then you can literally with Atlas like start with a text prompt, generate an image from scratch"* `[1:20]`
- *"marble was kind of bottlenecking through this gausian splat representation."* `[10:36]`
- *"LLM's taught us that next token prediction is really powerful. Um, video models teach us that next frame prediction is very powerful. Um, and Atlas teaches us that new view prediction is is extremely powerful."* `[13:25]`
- *"we really view ourselves as a frontier lab"* … *"to do that you need to be able to innovate on the data side. You need to be be able to innovate on the architecture. You need to be able to innovate on the training stack."* `[31:49–31:56]`
- *"but I'm not aware that you know anyone's done anything at this scale like autogressive diffusion models from scratch."* `[32:28]`  ← **the caption literally reads "autogressive"** (gate repair, §9)
- *"in terms of scaling, I think we're mostly compute bottleneck at this point."* `[36:34]`
- *"once you've got into the simulator, you've kind of left the atlas the Atlas realm, but now you're you're in you're in like perfect physics simulator realm. And now we can you can simulate all these counterfactuals."* `[34:27–34:44]`
- *"you take just three iPhone videos of the robot doing that task. And those three exterior iPhone videos is enough to reconstruct the 3D scene with enough fidelity"* `[34:10–34:19]`

**Ben Mildenhall (primary clip):**
- *"So sort of space-time navigation itself. It's not just novel view synthesis. It's like a essentially like an AGI complete task in the limit."* `[0:56–0:59]`
- *"have the model roll out its prediction and even inject new stuff into the token stream as you go."* `[35:38–35:45]`

**Sponsor (HRT) — sponsor's own words, `[HYP]`-as-advertised:**
- *"HRT's algorithms account for over 15% of US equity trading volume."* `[15:42]`
- *"These models allow for microscond reconstruction of order books that can be replayed while injecting hypotheticals and counterfactuals."* `[16:03]`

---

## §5 · Mapping to the house framework — **6 rows, 2 `[CRITICAL DIVERGENCE]`, NOT uniformly convergent**

> House canon quoted from the house's own artifacts read this session — §26.1 *"the world is the only certifier"*; §18.8 performance ≠ provenance (*"A record attests origin and integrity, never validity"*, `HORDE_STANDING_CONSTRAINT.md` §4); the **Core Inversion** — *"the connections do not compute; they constrain"* (the weights = the crystallized commit history; the live inference = the ephemeral wave); §5 the *"amnesiac ghost"* whose context window is *"liquidated the moment the session ends"* (all as carried in `drops/KGA7B_c_S4s_anthropic_ipo_gpt62_astra_news_2026-11-20.md` §5–6). **House vocabulary spoken on this tape = ~0** (`ledger`, `provenance`, `commit`, `immutable`, `non-rolling`, `append-only`, `epiplexity`, `EILT` = 0) ⇒ the mapping below is **ours**.

| # | Source claim (on tape) | House-EILT reading | Status |
|---|---|---|---|
| **R1** | *"Atlas generates worlds one new view at a time, adding the newly generated views to its context as it goes"* `[29:44]`, and the failure it names: *"these errors compounding over time and the model going off the rails"* `[24:47]` | The house's ledger must hold **the world's** answers (*"the world is the only certifier"*, §26.1). Atlas's **spatial context is a ledger the model writes from its OWN unverified generations** — and the video itself supplies the failure mode (compounding self-produced error). | **`[CRITICAL DIVERGENCE]` — CUTS AT THE SOURCE.** The source names the right failure (*self-fed context drifts*) **and locates the remedy INSIDE the model** — *Diffusion Forcing* trains the model to tolerate its own noise. The house locates the remedy **outside**: an external, non-rolling record. Same symptom, opposite remedy; the source never proposes certifying a generated view against anything but a downstream task. |
| **R2** | The whole value proposition is **counterfactual**: Sora *"learning simulations of the physical world that could be navigated in"*; HRT *"replayed while injecting hypotheticals and counterfactuals"* `[16:03]`; Johnson *"you can simulate all these counterfactuals"* `[34:44]`; Mildenhall *"inject new stuff into the token stream as you go"* `[35:38]` | A generative world model produces **possibilities that were never traversed**. The house's ledger is **past-directed** (append-only, non-rolling, outcome-recording). A counterfactual engine produces **no outcome to record** — nothing in the world certifies a path that was not walked. | **`[CRITICAL DIVERGENCE]` — CUTS AT BOTH.** The house cannot say what "certification" means for a counterfactual; the source cannot say what makes a generated view *valid* rather than merely *plausible*. The two are **structurally incompatible**, not complementary. |
| **R3** | *"we're mostly compute bottleneck at this point"* `[36:34]`; *"the kinds of data that we're training on, we can easily source a lot more"* `[37:01]`; *"our current approach is mainly bottlenecked just by compute"* `[37:24]` | The source's **entire causal story is capability = f(compute)**. The house's **Core Inversion** places identity/validity in the **record**, not the compute; capability scaling does not move the provenance line. | **`[DIVERGENCE]`.** A scaling-law account of capability vs. a provenance account of validity — orthogonal axes; the source has no stance on the house's axis at all. |
| **R4** | *"once you've got into the simulator, you've kind of left the atlas the Atlas realm, but now you're you're in you're in like perfect physics simulator realm"* `[34:27]` | World Labs **itself refuses to let the learned world model certify its own reconstruction** — it hands the reconstructed space to a physics engine for *"perfect fidelity."* That is §18.8 **performance ≠ provenance, arrived at from inside World Labs.** | **`[CONVERGENT-with-guard]`.** Convergent in spirit. **Guard:** the "physics simulator realm" is **also a model** — this is a handoff between two models, not to the world; the house's certifier remains uninstantiated. |
| **R5** | *"The next view is our next token"* `[11:18]`; next-token prediction as *"unreasonably effective"* | The house's **epiplexity** = the derived generalizable rule you can actually apply OOD. Next-view prediction as a transferable-to-3D/robotics objective is the same *shape* of claim (a rule that pays out beyond its training instances). | **`[A]` analogy only.** The source has zero provenance vocabulary; the mapping is ours. |
| **R6** | HRT: *"microscond reconstruction of order books that can be replayed while injecting hypotheticals and counterfactuals"* `[16:03]` | Superficially the house's **provenance + replay** ledger — a record you can rewind. | **`[DECORATION RISK]`.** It is a **sponsor advertisement**, and its defining move is **counterfactual injection** — the generative operation the non-rolling record exists to fence off. Shared words ("replay"), not a shared commitment. |

**Count stated:** 6 rows = **2 `[CRITICAL DIVERGENCE]`** (R1 cuts at the source, R2 cuts at both) + 1 `[DIVERGENCE]` (R3) + 1 `[CONVERGENT-with-guard]` (R4) + 1 `[A]` (R5) + 1 `[DECORATION RISK]` (R6). **Not uniformly convergent; the mapping does not fail.**

---

## §6 · Numbers and names — on-tape vs primary-source re-check

**Re-checked against primary sources this session (the headline finance figure first):**

| On tape (Welch Labs) | Primary source | Verdict |
|---|---|---|
| *"8 billion acquisition deal with AMD"* `[0:17]`; title **"$8B"** | **AMD IR press release 2026-09-28**: *"The all-stock transaction is valued at approximately **$8.2 billion** … expected to close by the end of 2026, subject to regulatory approvals."* Bloomberg/CNBC/AFP/Fortune agree ($8.2B all-stock). | **`[HYP]`-as-rounded.** The video's "$8B" is a rounding of the filed **$8.2B**; closing was **pending**, not closed (the video's framing implies a done deal). |
| *"Feefe will join AMD as chief scientist"* `[39:31]` | AMD IR: Li joins as **executive vice president and chief scientist**, reporting to Lisa Su. | **`[EST]`** (verified) — video omits the EVP title. |
| *"the 9,000 image Caltech 101 data set"* `[2:01]` | Caltech/Wikipedia: **9,146 images / 101 categories** (+ background). | **`[EST]`** — rounded down; consistent. |
| *"the over 14 million images that would become imageet"* `[2:25]` | ImageNet: **14,197,122** labelled images (~22,000 categories). | **`[EST]`** — consistent. |
| *"VJEPO was trained on a 2 million video data set"* `[7:38]` | Meta V-JEPA (2024-02-15): trained on **2M videos** (VideoMix2M). | **`[EST]`** — consistent. |
| *"Genie was trained on 200,000 hours of video game data scraped from the internet"* `[8:27]` | Genie arXiv 2402.15391: **>200,000 hours** of internet gaming video (filtered to 30,000 h of 2D platformers). | **`[EST]`** — consistent. |
| *"Sora on February 15th"* `[7:00]`, *"On the same day, February 15th, 2024 … VJ Jeepa"* `[7:30]`, *"Eight days after"* Genie `[8:18]` | OpenAI Sora 2024-02-15; Meta V-JEPA 2024-02-15; Genie 2024-02-23. | **`[EST]`** — dates consistent. |
| Atlas architecture (*autoregressive multimodal diffusion transformer*, pretrained from scratch on text/images/video/3D, camera-pose-grounded "spatial context") | worldlabs.ai/blog/atlas; deeplearning.ai *The Batch*; dealroom; turingpost. | **`[EST]`** — the video's architecture summary matches the primary blog. |
| World Labs' **Modality Forcing** / **Latent Forcing** | arXiv **2606.13676** (Duisterhof, Ramanan, Ichnowski, Johnson, Park — CMU + World Labs, 2026-06-11) and arXiv **2602.11401**. | **`[EST]`** — both papers exist; Johnson is a co-author. |
| **Diffusion Forcing** (MIT) | arXiv **2407.01392** — Boyuan Chen, Diego Martí Monsó, Yilun Du, Max Simchowitz, Russ Tedrake, Vincent Sitzmann (MIT/CSAIL), NeurIPS 2024; trained on Minecraft gameplay. | **`[EST]`** — video's *"MIT … Boyuan Chen et al."* consistent. |
| **Zip-NeRF** (Ben Mildenhall) | arXiv 2304.06706 — Barron, **Mildenhall**, Verbin, Srinivasan, Hedman (Google Research), ICCV 2023. | **`[EST]`** — consistent. |
| **CameraCtrl** / *"openweight stable video diffusion"* | arXiv 2404.02101 (He et al., 2024) — camera-pose module on Stable Video Diffusion/AnimateDiff. | **`[EST]`** — consistent. |

**On-tape numbers I could NOT re-check as fact, or that exist only in the model extraction (flagged):** the Genie **11B parameters** and the **$2/hour** first-job wage and the *"Layer 3, Head 2 / Layer 0, Head 38"* head indices appear in the **rung-0 Gemini on-screen-text read but NOT in the caption** — do not cite them from this video. The **18720×18720** attention dimension, the **16×16×4** patch, the **"12 frames"**, the **26th head / ninth layer**, **row 15322**, the **15 %** US-equity-volume figure, and the **"tens of millions of dollars"** compute cost **are** caption-verbatim.

---

## §7 · What was NOT established

1. **No Atlas scale or benchmark appears on tape.** The video shows qualitative demos and an attention-matrix visualization; it states **no** Atlas parameter count, token count, or comparative metric (no FVD/PSNR/LPIPS). *(External primary sources do publish Atlas reconstruction errors on DTU/ETH3D/ScanNet and "1 minute at 1440p" — but those are **not** the video's claims and are not filed here as such.)*
2. **The acquisition is narrated, not demonstrated.** No document, date-stamp beyond "September 2026", or closing status is shown; the primary sources put closing at *"by the end of 2026, subject to regulatory approvals."*
3. **The $8B/$8.2B rounding** and the omission of Li's EVP title (§6).
4. **"AMA"** at `[6:50]` (a third lab alongside OpenAI and DeepMind) is **ASR-garbled and unresolved on tape**; the referent is almost certainly **Meta** but is not said.
5. **"Juan"** (the open-source video model at `[17:45]`) is **not named on tape**; the referent is almost certainly **Wan** but is not said.
6. **Both rival world-model framings are asserted, not adjudicated.** The episode reports Sora's "world simulator" hypothesis and JEPA's feature-prediction alternative but presents **no** evidence that Atlas understands physics rather than rendering it plausibly.
7. **The HRT "over 15 %" figure is the sponsor's own number.** The entire HRT segment is an advertisement.

---

## §8 · Moments of self-correction (on tape)

- **Welch, on ImageNet** `[2:51]`: *"I didn't know how much of a slog it was"* — an explicit correction of his own prior assumption.
- **Fei-Fei Li, tempering the robotics claims** `[4:24]`: *"video models were not advanced enough to be action conditioned … but the journey is still long."*
- **Ben Mildenhall, catching his own terminology** `[12:10–12:19]`: *"an AGI complete task in the limit of or you know artificial spatial intelligence complete task"* — he visibly re-titles his own definition.
- **Justin Johnson, correcting Welch's framing** `[31:21]`: asked whether training from scratch was easy, he answers *"you picked up on one of them. Decision. It's a big one. It's no joke."*

---

## §9 · Quote gate (run against the FLAT caption this session)

**138 spans checked; 137 contiguous HIT; 1 repaired to the tape; 0 fabricated; 0 non-tape strings presented as quotes.**
- **Positive controls HIT:** *"The next view is our next token."*; *"This is known as the exposure bias problem."*; *"we're mostly compute bottleneck at this point."*
- **Gate CAUGHT + FIXED one real defect:** my first-pass span read *"…auto regressive diffusion models from scratch"*; the caption literally reads **"autogressive"** (`[32:28]`), and the gate repaired the quote to the tape (now filed with the garble preserved).
- Garble forms (*"Fe Lee"*, *"birectional"*, *"gausian"*, *"microscond"*, *"imageet"*) are **preserved as-served**, not silently corrected.
- **Convention:** spans elided with "…" are tagged `[elided]`; **house-canon quotes** (§5) and **primary-source quotes** (§6, e.g. the AMD IR release) are **fenced as non-tape** and are not counted as this video's words; the negative-control phrases in §11 (*"Marble was our first stab"*, *"compute bottlenecked at this point"*) are **search strings**, expected to miss — that is the point of a negative control. **Tape-quote defects caught + repaired this pass: 4** (two spelling defects — *"auto reggressive"* restored from my *"auto regressive"*, *"openweight"* from my *"open-weight"*; one over-tightened span — *"bottlenecking through this gausian splat"* restored from my *"bottleneck[ed]"*; and one **non-tape attribution removed** — a phrase I had attributed to Li, *"imagining what lies beyond"*, appears **nowhere** in the caption and was replaced with Mildenhall's on-tape line).

---

## §10 · Falsifiers (per the house register rule — a `[HYP]` names its test)

- **F-WL-1 (tests §6, source-facing):** if the AMD/World Labs transaction had **not** been announced on 2026-09-28 at ~$8.2B all-stock, the video's central finance frame is fabricated — falsified by the AMD IR release, Bloomberg, CNBC, AFP, Fortune (all read this session). **It stands.**
- **F-WL-2 (tests §5 R1, house-facing):** if an autoregressive world model's self-generated context were **certified by an external record** (not merely by downstream task reward), the house's R1 divergence would soften. *Test:* find a world-model pipeline that validates each generated view against a held-out external measurement before appending it.
- **F-WL-3 (tests §5 R2, house-facing):** if the house could specify what "certification" means for a **counterfactual** (a path never traversed), R2 would downgrade from `[CRITICAL DIVERGENCE]` to a tension. *Test:* produce a house account of validity that admits unobserved-but-simulated outcomes.

---

## §11 · Filing, dedupe, scope

**Dedupe: NEW.** id `hORDMRY_bZ0` = **0 hits** across `drops/`, `CANON_INDEX.md` and `YT_TRANSCRIPTS/` (checked pre-pull, pre-write **and immediately before write**). Distinctive-phrase clip check against `YT_TRANSCRIPTS/`: *"The next view is our next token"*, *"space-time patch"*, *"diffusion forcing"*, *"exposure bias"*, *"Marble was our first stab"*, *"compute bottlenecked at this point"* = **0 hits** each ⇒ **not a re-cut** of any existing transcript. Related-but-distinct prior art named in `related:` (the Benaich roundup's AMD row; the LeCun world-model drop; the Karaman "FA Lee" candidate) — none files this id, none is duplicated.

**Scope (honest):** the **audio/lyric track and metadata only**. The **visual track was NOT audited** — the "Gaussian splat"/"Zip-NeRF flythrough"/"attention heat map"/HRT imagery are described by the narrator, not independently verified. The rung-0 Gemini extraction is saved but is a **model-read, not a quote source**.

**Confirmed ≠ verified.** The house's Core Inversion (§5) says a record attests **origin, not validity**; this drop is a record of **what the episode said** and of **which external facts were re-checked**, nothing more.

---

### EILT pieces referenced
the **non-rolling, append-only ledger** (identity/accountability substrate); **§26.1** *"the world is the only certifier"*; **§18.8** performance ≠ provenance (a record attests origin, never validity); the **Core Inversion** — *"the connections do not compute; they constrain"*; **§5** the *"amnesiac ghost"* / context window *"liquidated the moment the session ends"*; **epiplexity** (the derived generalizable rule — R5); **§20 alignment-as-coupling** (not implicated here). **All quoted from the house's own artifacts read this session; house vocabulary on this tape = 0.**

**Citable for** the video's own on-tape narration and the founders' on-camera statements (near-verbatim, timestamped, speaker-tagged, to the saved caption only) + the §6 primary-source re-checks + the §5 friction rows. **NOT citable for** any Atlas scale/benchmark number (none on tape), the acquisition as *closed*, the rounded "$8B" as the filed figure, the Genie 11B / $2-hour / head-index figures (rung-0 model-read only, not on tape), "AMA"/"Juan" as identifications, or any house-vocab derivation (**R1/R2 `[CRITICAL DIVERGENCE]`**). **Cite the id, not the title.**

**Local only** — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send; one transcript set written (4 files), one drop filed, one index row appended, no pre-existing Canon artifact modified; index backed up to `CANON_INDEX.md.bak-2026-11-20-hORDMRY_bZ0`.
