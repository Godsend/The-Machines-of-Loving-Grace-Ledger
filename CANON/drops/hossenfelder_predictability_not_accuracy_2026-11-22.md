---
title: "Canon Drop — Hossenfelder: predictability and accuracy decouple, and the best models have the most unpredictable errors"
date: 2026-11-22
source_type: "YouTube — Sabine Hossenfelder, solo explainer (6:50)"
video_id: -MiM5xfAe2c
channel: "Sabine Hossenfelder"
upload_date: 2026-11-21
views_at_pull: 321736
source_of_record: "Gemini structured extraction (8,986 chars; 37,317 video tokens). CAPTIONS UNAVAILABLE (youtube-transcript-api IpBlocked). Quotes are [reconstruction] and must be caption-gated before public use. CITATIONS VERIFIED separately against the literature."
canon-id: CANON-2026-11-22-MiM5xfAe2c-HOSSENFELDER-NONDETERMINISM
---

# Predictability is not accuracy

## §1 · The claim `[EST]`

> *"The more reliably the current AI models respond, the less accurate they are."* `[reconstruction]`

**The argument in order:**

1. LLMs sample next-token probabilities; temperature=0 does **not** give determinism
2. Hardware floating-point rounding differs with batch size and chip count, so identical prompts produce different results
3. **Accuracy → predictability holds. Predictability → accuracy does NOT.** *"It might just mean it's more consistently wrong."*
4. Deep networks show **"prediction churn"**: changing one bit of initialisation yields a different network in **~48%** of cases
5. **Longer reasoning → more random errors**
6. **Automated error-spotting costs as much as building a better model** — *"there's no cheap way to spot the problem"*

## §2 · Citations verified independently `[EST]`

**All three principal papers exist and are correctly named** — checked against the literature, not taken from the extraction:

| Paper | Venue |
|---|---|
| **Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference** | **NeurIPS 2025**, arXiv `2506.09501` |
| **Fractal basin geometry and the limits to predictability and reproducibility in deep learning** | **Nature Machine Intelligence** (`s42256-026-01336-3`), arXiv `2510.05606` |
| **The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?** | arXiv `2601.23045` + Anthropic alignment page |

**`[C]` One of these is peer-reviewed in a Nature journal. That matters: this is not a YouTuber's hot take, it is a popular report of published results**, and the strongest result sits behind review.

## §3 · ★ The result that bears on everything this house does `[EST]`

**From the fractal-basin paper, as reported:**

> *"Even more interestingly, the most accurate models were the ones that disagreed most about the responses they got wrong."*
> *"The better the model is, the fewer errors it makes, but the more unpredictable it becomes just what it gets wrong."*

**`[C]` This is a formal statement of why spot-checking cannot work on capable systems.** An error rate is a scalar; *which* errors occur is the variable that becomes unpredictable precisely as capability rises. **You cannot sample your way to confidence about a system whose failure locations are the least predictable part of it.**

**And it is the argument for a ledger, stated by someone who is not arguing for a ledger:** if you cannot cheaply spot the mistakes, **the only remaining instrument is a record of what was actually done** — not to verify it, but to have something to check *when* the unpredictable failure occurs.

**Note the honesty in her own position:** she does not claim to have solved it. *"How do you want to make an AI safe if making it more powerful makes its errors more random and incomprehensible?"* `[reconstruction]`

## §4 · The measured noise floor — what this does to our own benchmarks `[CRITICAL]`

**Numerical nondeterminism alone shifts a model's score on a math benchmark by up to 9%** `[EST]` (NeurIPS paper, as reported).

**`[C]` Applied to our own work from the last 48 hours:**

- The **iWSP** drop recorded rebuilt NLP models *"lose about 1.4 points of hidden accuracy."* **1.4 points is deep inside a 9% noise band.** That finding may be real, but **it is not established by that comparison** — and I filed it yesterday without checking the noise floor.
- Any canon or eval claim built on a delta **below ~9%** is currently unfalsifiable against nondeterminism unless the measurement controls for it (fixed seeds, identical hardware, replicated runs, bitwise-reproducible serving).

**This is the most actionable thing in the video and it cuts at us, not at the labs.** Our entire culture of "we measured X versus Y" needs a noise floor attached, or the numbers are decoration.

**Pre-registered (F-NOISE-1):** re-run any of our benchmark-style claims with N≥5 replicates; if the between-replicate spread exceeds the claimed effect, the claim demotes to `[HYP]`.

## §5 · "Being predictable is not intelligent" — and the RLHF thread `[C]`

> *"In the end, though, the fundamental problem might be that being predictable is not intelligent."* `[reconstruction]`
> *"It seems that intelligence needs a little bit of chaos."* `[reconstruction]`

**`[C]` This is the sharpest available statement of why preference optimisation is structurally the wrong instrument.** RLHF optimises for a predictable, agreeable response. **If predictability and accuracy are decoupled — and the papers say they are, in one direction — then optimising the former does not optimise the latter.** It can raise consistency while lowering correctness, and the symptom is exactly *"more consistently wrong."*

**That connects directly to the house's standing position** (`restraint beats constraints`; `a reason is not an excuse`): a system trained to be reliably agreeable **has been optimised on the axis that does not track truth**.

## §6 · Friction rows

**R1 · Her causal attribution is a hedge, and it is doing work she does not support** `[DIVERGENCE]`: *"I suspect it's specific to these models"* `[reconstruction]` — she offers a mechanism (states close in weights, far in meaning) but **does not test it against alternative architectures**. She marks it as suspicion, correctly; we should not cite it as a finding.

**R2 · The Nvidia counter-result is stated but not integrated** `[DIVERGENCE]`: bit-for-bit reproducible training across 2,000+ chips for 800 steps shows **determinism is achievable with engineering**. That weakens the "inherent chaos" reading and supports a different conclusion — **nondeterminism is a default, not a law**, which makes our missing noise floors a fixable defect rather than a fact of nature.

**R3 · "Intelligence needs chaos" is poetry wearing a finding's clothes** `[POETIC]`: no measurement is offered for what quantity of chaos intelligence requires. The measured claims are the decoupling and the fractal basins; **the aphorism is not one of them**, however appealing.

## §7 · What was not established

- No replication of the 9% figure in this pass; it is reported, not reproduced `[EST→reported]`
- The 48% one-bit-churn figure is reported, not reproduced
- No statement of which model classes were tested, or at what scale
- **The video does not connect nondeterminism to any safety mechanism** — it raises the problem and stops, which is honest but leaves the practical question open

## §8 · Why this is filed

**Because it supplies a measured noise floor for our own numeracy, and because the fractal-basin result is the strongest external argument yet for a record over a sample.** It also lands a blow on our own recent work — the 1.4-point rebuild loss is inside the noise — and the house's rule is that a correction lands on the source, not beside it.
