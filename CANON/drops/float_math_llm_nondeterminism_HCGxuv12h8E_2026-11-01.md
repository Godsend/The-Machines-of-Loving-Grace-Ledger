---
title: "Canon Drop — Parag Dhawan: 'The Float Math Flaw Breaking Production LLMs (And How to Fix It) | Mystery of LLM Nondeterminism' (SECONDHAND systems explainer relaying three real primary sources: Thinking Machines Lab batch-invariant kernels · arXiv 2609.25624 cross-GPU bitwise determinism · Microsoft LLM-42 verified speculation)"
date: 2026-11-01
filed_by: Dion
source_type: "YouTube explainer (SECONDHAND relay — the narrator summarises published research; the video carries no primary artifact of its own; production reads as AI-written/AI-narrated — flagged, not asserted)"
video_id: HCGxuv12h8E
channel: Parag Dhawan
channel_id: UCFqeqjMPuWyP2lmJx7JIX_w
upload_date: 2026-10-31
duration_s: 612
duration_hms: "10:12"
views_at_pull: 11
likes_at_pull: 1
transcript_path: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/HCGxuv12h8E_LLMNondeterminism_FloatMath_ParagDhawan_2026-11-01.txt"
transcript_timestamped: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/HCGxuv12h8E_LLMNondeterminism_FloatMath_ParagDhawan_2026-11-01_timestamped.txt"
metadata_json: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/HCGxuv12h8E.metadata.json (trimmed key-field extract of the yt-dlp --dump-json output)"
epistemic-registers: "EST=fact I independently reproduced this session (ran the numbers) · HYP=technical assertion verified verbatim against a named primary source but NOT reproduced by me on this host · A=analogy only (ours) · C=conjecture with no evidence · POETIC=metaphor/framing · RIFF=our speculative synthesis, not the source's"
register-rule: "no tag = treat as unverified; row-status labels [CRITICAL DIVERGENCE]/[DIVERGENCE]/[CONVERGENT] are NOT registers"
---

# Parag Dhawan — "The Float Math Flaw Breaking Production LLMs (And How to Fix It) | Mystery of LLM Nondeterminism"

## Source

**Source (VERIFIED):** `https://www.youtube.com/watch?v=HCGxuv12h8E` — channel **Parag Dhawan** (`UCFqeqjMPuWyP2lmJx7JIX_w`, `@ParagDhawan`), uploaded **2026-10-31**, **612 s (10:12)**, **11 views / 1 like** at pull, channel follower count **1,730**, **0 chapters**. Identity re-verified live via `yt-dlp --dump-json` (id / title / channel / channel_id / duration / upload all match the brief — no correction) and `oembed` (`author_name = Parag Dhawan`). Metadata JSON saved at `YT_TRANSCRIPTS/HCGxuv12h8E.metadata.json`.

**Filed by:** Dion (dion lane) · **Date processed:** 2026-11-01 · **Scope:** local only — no GitHub push, no NotebookLM, no rclone/Drive mirror, no TTS, no outbound send.

**Source class:** **SECONDHAND explainer.** The video is a single-narrator dramatised summary ("a literal hardware level who done it", "the scene of the crime", "hardware detectives") of **three published primary sources**, which the transcript names or clearly identifies by content:

1. **Thinking Machines Lab — "Defeating Nondeterminism in LLM Inference"** (Horace He et al., Sept 2025; DOI 10.64434/tml.20250910) — named on tape ("*The engineering team over at Thinking Machines Lab*").
2. **arXiv 2609.25624 — "Accelerating the Mitigation of LLM Inference Nondeterminism Across GPU Architectures"** — "another team" (cross-GPU bitwise determinism, four rules, BF16→FP32 register upcast).
3. **Microsoft — "LLM-42: Enabling Determinism in LLM Inference with Verified Speculation"** (arXiv 2601.17768; SOSP 2026) — named on tape ("*LLM42*").

**Production provenance (FLAG — not asserted as a defect):** heavy LLM-style narration ("*slammed your head against the desk*", "*boom, a completely different token is chosen*", generic "*it is absolutely a space we'll be keeping our eyes on… I'll catch you in the next one*" close), no on-camera authored presenter named, brand-new upload on a small channel (11 views, one day old). This reads as an AI-scripted / AI-narrated content-production pipeline. **Importance: it is NOT rejected for this** — see Verdict. The reason it does not meet the "AI-generated slop → reject" bar is narrow and evidence-based: **every headline number and mechanism in it checks out verbatim against the named primary sources** (Verification notes). Slop is rejected for *fabrication*, not for *automation*.

**NOT a reupload / NOT a re-cut.** `HCGxuv12h8E` = **0 hits** across `Canon/`; the video is an original 10-minute explainer, not a clip of any filed source.

---

## Claim inventory (literal quotes from the transcript)

Quotes are the source's own words as captioned (YouTube auto-caption `en-orig`); ASR garbles preserved and repaired in ASR repairs below.

- **[0:32–0:47]** "*You lock in your seed to 42. You crank that temperature dial all the way down to zero. In theory, that means the model should strictly pick the highest probability token every single time through greedy decoding. It should be perfectly 100% deterministic, right?*"
- **[0:54–1:01]** "*You run it a thousand times and it actually spits out 80 different unique responses.*"
- **[1:39–1:49]** "*For the longest time, the developer community pointed the finger squarely at thread concurrency race conditions and atomic memory operations.*"
- **[2:04–2:18]** "*Atomic ads aren't even used in a standard LLM forward pass… Things like dense matrix multiplications, RMS norm, attention, they all execute without any atomic additions at all.*"
- **[2:18–2:26]** "*if you run a static input tensor with a fixed batch shape on a single GPU, it actually spits out bitwise identical outputs every single time.*"
- **[2:26–2:33]** "*the true culprit… it's dynamic batching. Float math and dynamic batching.*"
- **[2:49–2:57]** "*GPUs use finite floatingoint precision, we're talking formats like float 32 or Bflat 16, they have to round the result after every single operation.*"
- **[2:57–3:24]** "*because of that rounding, simply changing the order of your addition fundamentally changes your final result… A plus b plus c is the exact same no matter how you group them. But in GPU architecture, a plus b rounded plus c absolutely does not equal a + c rounded plus b. It is a completely different property called floatingpoint nonassociivity.*"
- **[3:24–3:42]** "*As user traffic fluctuates on your serving engine, let's say you're using VLLM or SG lang, the batch size is constantly changing. To maximize compute efficiency, low-level GPU libraries like Kublas dynamically select different thread block dimensions or split K reduction factors based on that exact batch size at that exact moment.*"
- **[3:49–3:58]** "*by changing its reduction order, it slightly scramles those underlying calculations. And that tiny microscopic rounding noise, it compounds over layers and layers until the top two tokens are in a near tie and suddenly boom, a completely different token is chosen.*"
- **[4:10–4:46]** "*The engineering team over at Thinking Machines Lab… They forced the GPU to use a single universal reduction strategy regardless of what the batch size was doing. By making sure that every single row of a batch processes its reduction on a single core in a perfectly consistent order, they actually did it.*"
- **[5:02–5:18]** "*The default vendor optimized kernels hit a blistering 527 teraflops. But those batch invariant kernels, they plummeted all the way down to 194 teraflops. I mean, that is a massive 60% drop in computational throughput…*"
- **[5:57–6:32]** the "four incredibly strict design rules" for cross-GPU linear layers: "*they totally bypassed the undocumented Tensor Core internals using only strictly defined ILE E fused multiply AD instructions*" (1) · "*absolutely no autotuning*" (2) · "*they used a deterministic split K scheme with zero atomic additions*" (3) · "*they used the batch invariance we just talked about*" (4).
- **[6:32–6:57]** "*By loading the weights in low precision BF-16 from memory and then upcasting them to FP32 entirely inside the GPU's registers, this method drastically cuts down on memory bandwidth… it actually achieves up to a 3.1x speed up over the previous state-of-the-art FP32 determinism baselines.*"
- **[7:12–7:28]** "*mathematical outputs that are bit forbit identical across three entirely different generations of NVIDIA GPUs… whether you are running on an Ampere, an ADA love lace, or a hopper architecture.*"
- **[7:53–8:02]** "*LLM42 acts like a really clever scheduling bypass… letting the system race ahead on an ultra-fast path, while a parallel process acts like a strict safety inspector.*"
- **[8:33–8:49]** "*the roll back frequency. For many workloads, the system requires exactly zero roll backs. Zero… Token divergence is actually quite rare on a per token basis until the errors have a chance to compound.*"
- **[8:58–9:22]** "*LLM42 operates at an impressive 911 tokens per second. That is comfortably within 3% of the peak unmitigated throughput of 931 tokens per second. Just compare that to forcing everything into deterministic mode, which plummets all the way down to 415.*"

---

## Independent technical check (numbers I actually ran this session)

The brief's duty splits the video's claims into three grades. They grade **differently**.

### (a) Float arithmetic order-dependence — **REAL, REPRODUCED — [EST]**

The video's core arithmetic assertion — *(A+B)+C ≠ A+(B+C)* under finite precision — is true and I demonstrated it in strict float32 (round-to-nearest **after every operation**, via `struct` round-tripping):

```
a = 1.0,  b = 3e-8,  c = 3e-8   (float32)
(a+b)+c = 1.0                   bits 0x3f800000
a+(b+c) = 1.0000001192092896    bits 0x3f800001
DIFFER = True
```

Because the sum of two float32 values is exactly representable in double, rounding the double result back to float32 is faithful float32 accumulation — the two sides genuinely pick different last bits.

**Order-dependence at scale** — summing **200,000 random float32 values** the same way, just in different orders, yields **five distinct float32 results** (not five approximations — five different bit patterns):

```
array order  : -177.06016540527344
reversed     : -177.05848693847656
ascending    : -177.44023132324220
descending   : -177.35069274902344
by |abs| asc : -177.06082153320312
distinct float32 results among the 5 orderings: 5
spread (max − min) = 0.381744384765625
```

**Reduced-precision amplification** — the same 200k summation accumulated in **bfloat16 (8-bit mantissa)** vs **float32 (23-bit mantissa)**:

```
exact (double)   = -177.05873980
f32  accumulate  = -177.06016541   |err| = 1.43e-03
bf16 accumulate  =  -49.25000000   |err| = 1.28e+02
ratio bf16/f32   = ~89,650x
```

**Conclusion (a):** the claim "*simply changing the order of your addition fundamentally changes your final result*" is **EST — established, reproduced here**. The bf16-vs-fp32 spread also independently supports the weaker sub-claim that *lower-precision accumulation amplifies* the divergence. **This part of the video is correct.**

### (b) GPU-kernel non-determinism, split-K, atomic adds, batch-drift — **VERIFIED AGAINST PRIMARY SOURCES, NOT REPRODUCED BY ME — [HYP]**

I **cannot** demonstrate these from first principles on this host: there is no usable GPU here (the box's GPU path fails — `libcublas` missing, per the rail skill), so I could not execute a split-K GEMM, an atomic-add reduction, or a batch-size sweep. Per the brief's rule, **an assertion I cannot reproduce does not get EST.** Each is therefore **[HYP]** — but each is HYP *backed by a verbatim match to a named primary source*, which is much stronger than a bare claim:

| Video assertion | Primary source | Match |
|---|---|---|
| "atomic adds aren't even used in a standard LLM forward pass"; static fixed-shape batch on one GPU is "bitwise identical" | TML "Defeating Nondeterminism in LLM Inference" | ✔ **verbatim**: "*in the typical forward pass of an LLM, there is usually not a single atomic add present*"; kernels are run-to-run deterministic |
| "1000 runs → 80 unique responses" | TML | ✔ exact: Qwen3-235B-A22B-Instruct-2507, temp 0, 1000 completions → **80 unique**, first divergence at **token 103** |
| cuBLAS "*dynamically select different thread block dimensions or split K reduction factors*" by batch size | TML + arXiv 2609.25624 | ✔ split-K / batch-dependent tiling & tensor-core instruction selection confirmed |
| TML "*single universal reduction strategy regardless of… batch size*" | TML batch-invariant kernels | ✔ batch invariance = fixed reduction order per row |
| "**527 → 194 TFLOPS**, a massive **60% drop**" | **LLM-42 paper** (arXiv 2601.17768) | ✔ figures **exact**: "*cuBLAS (via torch.mm) reaches up to 527 TFLOPS, whereas the batch-invariant kernel peaks at 194 TFLOPS, a slowdown of **63%***" — **the video says 60%; the paper says 63%** (minor understatement; the 527/194 pair is verbatim) |
| four rules (bypass Tensor Core → IEEE FMA; no autotuning; deterministic split-K, zero atomics; batch invariance) | arXiv 2609.25624 (R1–R4) | ✔ matches the paper's design rules |
| BF16 weights loaded → upcast FP32 in registers → "**3.1x** speed up" | arXiv 2609.25624 | ✔ "*load 16-bit weights from memory, upcast them to FP32 in registers… **1.17 to 3.1×** faster… cutting weight-memory traffic in half*" — the video takes the **upper bound** (3.1×) as *the* figure |
| "bit forbit identical across… Ampere, Ada Lovelace, Hopper" | arXiv 2609.25624 | ✔ bitwise-identical across A100/L40S/H100 on every probe shape |
| LLM-42 "scheduling bypass… ultra-fast path + strict safety inspector"; "*exactly zero roll backs*"; "*911 tok/s… within 3% of 931… deterministic mode… 415*" | LLM-42 (arXiv 2601.17768) | ✔ **exact**: decode–verify–rollback; "*more than half of the requests complete without any rollback*"; **911 tok/s within 3% of 931**; deterministic mode collapses to **415**; **2.2× over SGLang-deterministic** |

**Conclusion (b): every headline number in the video matches its primary source**, and several match to the digit (80/1000, 527/194, 911/931/415, 3.1×). The **only** numeric discrepancy found is the video's "**60%**" vs the paper's "**63%**". **Grade: [HYP]** — the underlying mechanism is real and sourced, but I did not reproduce it; the video is a faithful relay, not an artifact.

### (c) The over-reaching "root cause / the float-math flaw" frame — **PARTIALLY SUPPORTED — [HYP]/[A]**

The **body** of the video is more careful than its **title**. It says the cause is "*dynamic batching. Float math **and** dynamic batching*" — i.e. the **interaction** of non-associativity with a reduction order that varies with batch size. That is exactly TML's own thesis ("*the primary reason nearly all LLM inference endpoints are nondeterministic is that the load (and thus batch-size) nondeterministically varies*"). So the "root cause" claim is **supported**.

But the **title packaging — "*The Float Math Flaw Breaking Production LLMs*" — overstates float math in isolation.** Non-associativity alone does **not** produce nondeterminism; TML is explicit that the forward pass on a fixed shape is deterministic. The nondeterminism requires the **external, load-driven variable** (batch size) that *selects a different reduction tree*. Float math is the **necessary substrate**, not the cause. **Grade [HYP]/[A]:** the mechanism is right, the "flaw" framing is a simplification a reader could over-generalize.

**Internal tension worth recording:** the video says atomic adds "*aren't even used*" in a forward pass, yet its own cross-GPU rule set is "*deterministic split-K scheme with **zero atomic additions***" — implying split-K variants **do** use atomics (TML agrees: atomic adds appear in split-K / `scatter_add` patterns, just not the standard pass). The two statements are reconcilable but the video never reconciles them.

---

## EILT mapping (every right-hand cell ours)

| Row | Source claim (transcript) | House/EILT concept | Status | Why |
|---|---|---|---|---|
| R1 | "*the top two tokens are in a near tie and suddenly boom, a completely different token is chosen*" [3:49–3:58] | **Fractal basin boundary / sensitive dependence on initial conditions** — a borderline state where an infinitesimal perturbation selects a different attractor | **[A]** | Rhyme is real: a perturbation below the resolution of a decision flips the downstream trajectory. But EILT varies the **initial condition in a fixed landscape F**; the video varies the **reduction order itself** — see R4. Analogy only. |
| R2 | "*that tiny microscopic rounding noise… compounds over layers and layers*" [3:49–3:58] | **Trajectory amplification toward a saddle point** (basin-boundary approach) | **[A]** | Both describe a small early deviation so amplified by the dynamics that it dominates later state. Directional, not formal. |
| R3 | "*deterministic replay for auditing and debugging*" [1:17–1:33] | **The EILT Ledger Principle** — "*every significant system output is an entry in the permanent record… append-only, timestamped… author-attributed*" | **[CONVERGENT]** | Both want a reproducible, provenance-bound record of what the system actually produced. Independently stated. But see R5 for the friction: provenance ≠ bit-identity. |
| R4 | "*low-level GPU libraries like Kublas dynamically select different… split K reduction factors based on that exact batch size*" [3:33–3:42] | *(claimed as)* EILT's **dynamics F on the possibility space Ω** | **[CRITICAL DIVERGENCE]** | **The analogy fails and the divergence is load-bearing.** In EILT the landscape/vector field **F is a property of the system** (sculpted by the system's own history and biology); variation comes from **where in Ω you start**. Here the **execution that realises F is itself chosen by an external co-scheduling variable** — the number of *other users' concurrent requests* — which is **not an input to the system's own state at all.** EILT has no slot for "*the same point in Ω follows a different F depending on how many other trajectories the machine is computing at the same instant.*" The house's landscape is the system's; this data's "landscape" is set by a serving-load artifact **outside Ω**. Heuristic rhyme, opposite causation. |
| R5 | "*just getting the exact same answer twice… you absolutely rely on deterministic replay*" [0:09–0:17] | The ledger's **provenance-not-truth bound** — the ledger records *where a thing came from*, not *that it is true*, and not that it can be *regenerated bit-for-bit* | **[DIVERGENCE]** *(guard)* | **Homonym guard.** The video wants **bit-identical regeneration** of an output — a strictly stronger demand than the ledger's append-only provenance entry. EILT's Ledger Principle would be satisfied by recording *that* a nondeterministic output occurred and *which environment produced it*; it does not require the output be reproducible. Same word ("record/determinism"), different guarantee. |
| R6 | "*atomic ads aren't even used in a standard LLM forward pass*" [2:04] | EILT's **commit** — an append-only, atomic-*looking* write to the ledger | **[DIVERGENCE]** *(guard)* | **Homonym guard.** "Atomic" here is the hardware race primitive (atomicAdd); the ledger's append-only entry is an atomicity *guarantee*, near the opposite sense. The video's *absence* of atomics is not EILT's *presence* of atomic commits. |

**Friction rule satisfaction:** ≥1 genuine divergence row present — in fact **three** (R4 CRITICAL, R5, R6), with **R4** the load-bearing one: EILT models variation as initial-condition sensitivity within a system-owned landscape; this data's variation is a change to the *execution of the computation* driven by an external load variable that is not part of the system's state.

---

## Verification notes

- **Rail report (which rung won).** Rung 1 `youtube-transcript-api` on system python3: `.list('HCGxuv12h8E')` = **21 tracks, all `is_generated=True`** (NO manual/human caption), but `.fetch(['en'])` raised **`IpBlocked`** → rung 1 FAILED. Rung 2 `yt-dlp --write-auto-subs --sub-langs 'en.*' --sub-format vtt` = **`HTTP Error 429: Too Many Requests`** → rung 2 FAILED. **Rung 3 CDP transcript panel (Chromium :9333, `Chrome/145.0.7632.6`) SUCCEEDED:** navigated to the watch URL, polled `ytInitialPlayerResponse.videoDetails.videoId` until it **matched `HCGxuv12h8E`**, clicked `#expand` → "show transcript", then read the expanded `ytd-engagement-panel-section-list-renderer`. Probed **both** panels: **modern `transcript-segment-view-model` = 77 segments; legacy `ytd-transcript-segment-renderer` = 0** — modern only this session. Panel text length 12,636 chars. **Rung 4 NOT exercised** (audio was pre-downloaded as insurance — `hcg_audio.m4a`, format 139-4 — and left unused once rung 3 landed). **This transcript is the YouTube auto-caption track (`en-orig`), NOT local ASR.**
- **Coverage:** **[0:00] → [10:03] of 612 s (10:12)** = ~98.5% span; 77 segments; no gap > 60 s. Saved: plain `…_2026-11-01.txt` (**11,081 chars / 1,759 words**, header carries video id + URL) and `…_timestamped.txt` (11,621 chars, 77 `[M:SS]` cues). Metadata JSON alongside.
- **Dedupe gate:** `HCGxuv12h8E` = **0 hits** in `Canon/`; channel *Parag Dhawan* = 0 hits; no prior drop for this source ⇒ **first filing**, not a re-cut.
- **Claim-by-claim verification this session** (fetched live): TML blog `thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/`; arXiv `2609.25624`; arXiv `2601.17768` (LLM-42, SOSP 2026) + Microsoft Research page + `github.com/microsoft/llm-42`. The 527/194 TFLOPS pair was located in the **LLM-42 paper text** — the video's "60%" is the paper's "63%".
- **Registers declared (six-tag set):** `[EST]` (a)=1 · `[HYP]` (b)+(c)=1 block (≥9 assertions) · `[A]` R1,R2 + (c) frame = 3 · `[C]` = 0 (nothing asserted with no evidence) · `[POETIC]` = the "who done it / scene of the crime / hardware detectives" narration = 1 (framing, source's own) · `[RIFF]` = the R4/R5/R6 synthesis = ours. TAG GATE: no invented tags.
- **Quote gate:** all 17 quoted spans above reproduced verbatim from the saved transcript (`YT_TRANSCRIPTS/HCGxuv12h8E_…_timestamped.txt`). PASSED.

## Verdict

**[HYP]-dominant, with one load-bearing [EST] nucleus and three divergence rows.** **Not rejected, and not "slop" in the reject sense** — because it is **factually faithful**: every headline number and every mechanism it asserts matches a named primary source, several to the digit (80/1000 · 527/194 · 911/931/415 · 3.1× · bitwise across Ampere/Ada/Hopper). It adds **no primary claim of its own**, so its canon value is as a **secondary summary / record** of three real lines of research, plus this filing's reproduced float demo. Its weaknesses: (i) **secondhand** by construction; (ii) likely **AI-scripted/AI-narrated** production (flagged); (iii) a **title that overstates** ("The Float Math Flaw") relative to its own careful body; (iv) the **"60%" vs "63%"** slip; (v) it never reconciles its own "no atomic adds" with its "zero-atomic split-K" rule. **STRONGEST: the [EST] arithmetic nucleus — the order-dependence the video describes is real and I reproduced it (5 distinct sums of one 200k-term array; bf16 error ~89,650× the fp32 error). WEAKEST: the (b) block — genuinely dependent on GPU behaviour I cannot exercise here, so it stays HYP no matter how well it matches the papers.**

## Citable for / NOT citable for

- **Citable for:** the *secondary* summary that LLM inference nondeterminism at temperature 0 arises from float non-associativity interacting with batch-size-dependent reduction order (three named primary sources); the reproduced float-order-dependence demonstration; the three primary sources themselves (cite them directly, not the video).
- **NOT citable for:** any GPU-specific number (527/194 TFLOPS, 911/931/415 tok/s, 3.1×, bitwise-across-architectures) **as if this video established it** — cite TML / arXiv 2609.25624 / LLM-42; the "root cause = float math" frame as stated in the title; the "60%" figure (use 63%).

## Falsifiers

- **F-HCG-1:** a demonstration that temperature-0 LLM output is *bit-identical* across batch sizes with standard vendor kernels falsifies the video's central mechanism (R4 / (b)).
- **F-HCG-2:** an LLM forward pass found to *require* atomic adds for correctness (not just for split-K speed) falsifies the "*atomic adds aren't even used*" claim.
- **F-HCG-3:** a re-run of my 200k-term float32 summation that yields **one** result across all orderings falsifies (a) — it will not, because the arithmetic is order-dependent by definition, but the falsifier is stated.
- **F-HCG-4 (provenance):** if the video is shown to be human-authored/human-narrated rather than AI-scripted, the production-provenance flag drops — the *content* grade is unaffected.

## ASR repairs (source's YouTube auto-captions, `en-orig`)

`atomic ads`→**atomic adds** · `Bflat 16`→**bfloat16** · `Kublas`→**cuBLAS** · `VLLM`→**vLLM** · `SG lang`→**SGLang** · `ampear`→**Ampere** · `ADA love lace`→**Ada Lovelace** · `ILE E fused multiply AD`→**IEEE fused multiply-add** · `floatingoint`→**floating-point** · `nonassociivity`→**non-associativity** · `scramles`→**scrambles** · `bit forbit`→**bit-for-bit** · `LLM42` retained (= **LLM-42**). Speaker surname verified: **Parag Dhawan** (oembed + channel).

Local only — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send; transcript pair + metadata JSON written, one drop filed, one index row appended.
