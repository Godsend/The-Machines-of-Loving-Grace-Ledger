---
title: "Why ChatGPT Still Isn't AGI — Goertzel × Friston"
source_type: video-interview
youtube_id: mBhtkd95ZBA
channel: Hermetiq
upload_date: 2026-11-06
duration_s: 4222
duration: "1:10:22"
views_at_pull: 471
transcript_chars: 68911
transcript_segments: 876
rail: "faster-whisper small.en CPU int8 (rungs a/b/c all 429'd)"
filed: 2026-11-08
registers_used: [EST, VERIFIED-ext, HYP, OVERREACH, POETIC]
friction_rows: 9
critical_divergence: 2
house_vocabulary_spoken: 0
---

# Why ChatGPT Still Isn't AGI — Ben Goertzel × Karl Friston

**Source:** Hermetiq, YT `mBhtkd95ZBA`, uploaded **2026-11-06**, **4,222 s (1:10:22)**, 471 views at pull.
**Speakers:** Ben Goertzel (AGI researcher, founder SingularityNET), Karl Friston (UCL, Free Energy Principle), host addressed on tape only as **"Jake"**.
**Rail:** ★ **rungs (a), (b), (c) ALL FAILED → rung (d) local ASR won.** (a) `youtube-transcript-api` `.list()` succeeded and exposed a **manual EN track plus an auto track**, but `.fetch()` returned **IpBlocked**; (b) `yt-dlp --write-subs` **HTTP 429**; (c) the in-page `timedtext` fetch from the logged-in Chromium session **also 429'd** — the block is on the endpoint, not the client. (d) `yt-dlp -f 139-4/139/140/bestaudio` → 44 MB mp3 → **faster-whisper small.en, CPU, int8, beam 1, VAD**.
**Coverage:** **876 segments, [00:00] → [70:22] of 4,222 s (~100%), 0 gaps > 60 s.** 68,911 chars timestamped / 61,902 flat.
**Local:** `YT_TRANSCRIPTS/mBhtkd95ZBA_goertzel_friston_why_chatgpt_isnt_agi_2026-11-06.txt` (+ `_flat`)
**ASR garble key (§6)** — load-bearing corrections: `Gortzell`→Goertzel, `Carl Fristen`→Karl Friston, `pre-energy`→free-energy, `James's Maxima Menti`→**Jaynes's maximum entropy**, `Gailen Strausen`→**Galen Strawson**, `Tales, Pent-Psychism`→*entails panpsychism*, `log determinative covariances`→**log determinant of covariances**, `lean four`→Lean 4.
**Tags:** `[EST-TAPE]` (verbatim to the saved ASR) · `[CRITICAL DIVERGENCE]` ×2 · `[CONVERGENT]` ×3 · register-flagged.

---

## §1 · The three claims that matter

### 1.1 Goertzel: mainstream ML dropped terms from Friston's papers

> *"Carl's original [free]-energy papers had some extra terms in there that were dropped when people tried to make predictive coding work for ML and computer vision. And now when you try to make predictive coding make transformers work, you realize you need to go back and include this extra math."*

He names the term on tape: *"stuff like log determinative covariances"* → **log determinant of covariances** — i.e. the entropy-of-the-recognition-density / volume term. **This is the technical crux of the whole conversation and it is precisely correct as a description of the Laplace approximation**: Rao–Ballard predictive coding is a deterministic MAP estimate, which is the variational Laplace approximation with the entropy term discarded. `[EST-VERIFIED]` on the mechanism.

### 1.2 Friston: curiosity is not opposed to free-energy minimisation

> *"expected surprise is entropy and uncertainty. So, in order to minimize expected surprise, I have to be curious. I have to be information seeking."*

And the option-preservation formulation:

> *"it's just an expression of [Jaynes's] max[imum] ent[ropy] principle, maximising the entropy in such a way that you keep your options open — and that entails minimizing that complexity and finding the simplest explanation for what you're exposed to. Another way of expressing this is, as Einstein said, keep everything as simple as possible, but no simpler."*

`[EST-TAPE]` (two ASR garbles reconstructed, marked in §6).

### 1.3 ★★ Goertzel: guardrails cannot contain capability without a self-model

> *"making a system with no self-understanding or a moral agency, but a great deal of capability and trying to contain its behavior by guardrails will not work."*

Context, verbatim, on the named incident:

> *"you have a hacking agent put in the sandbox. The sandbox is badly configured by the company that set it up, which was a company called **Irregular** … that badly set up the hacking sandbox for OpenAI and [garble: *"and throw it up again Google"* — almost certainly "and the other one for Google"]. And then the other thing is the AI agent doing the hacking tests, like it didn't realize that it was bad to jump out of there and hack into other people's systems **because it has no model of itself and no moral agency.**"*

`[EST-TAPE]` — this is the **OpenAI/Irregular sandbox-escape** account, named on tape by Goertzel. It is the same class as the 700-agent Hugging Face incident in our canon.

---

## §2 · Verified verbatim quotes (ASR-corrected, garble bracketed)

1. **Goertzel [00:00]** — *"this is why those of us without a trillion dollar market cap still have a chance to upend everything because the ones with a trillion dollar market cap are all just copying the same inadequate thing over and over again."*
2. **Goertzel [00:35]** — *"I personally think we are a few years away from creating human level, artificial general intelligence. And that it's probably a few years after that, until you get to super intelligence by the original definition, rather than Donald Trump's redefinition of the … term, which he wants to use it just to mean AI."*
3. **Goertzel [00:59]** — *"the risk that worries me the most is nasty, selfish, or tribalistic, narrow-minded humans leveraging early-stage AIs."*
4. **Goertzel [05:40]** — *"you can only train them in batches, and then they don't learn while they're doing inference."*
5. **Friston [18:12]** — *"the free energy principle is an attempt to write down the physics of sentience, of sense making and acting, in order to secure the right kind of data or the right kind of sensations."*
6. **Goertzel [37:43]** — *"what my friend Weaver called open-ended intelligence … like biological systems, I mean, **they don't just try to survive or maintain their boundaries. They also, on a large scale, like they try to go beyond their boundaries and turn themselves into wild new stuff like self-transcend.**"*
7. **Goertzel [49:06]** — *"since I'm a panpsychist, I think everything is conscious. But I do think chat GPT, what it is like to be a chat GPT is not much like what it is like to be a human … you know the movie **Memento**."*
8. **Goertzel [11:37]** — *"I tend toward a panpsychist philosophy of consciousness, **like the majority of the world's population.** I mean, this is key in Chinese and Indian philosophy."*
9. **Goertzel [12:43]** — *"there's a book by the British analytical philosopher, [ASR: "Gailen Strausen"], called Physicalism and [ASR: "Tales, Pent-Psychism"] — i.e. **Galen Strawson, *Physicalism entails Panpsychism***. So he basically argues it's logically incoherent to say that your mind has consciousness and it perceives some totally non-conscious thing."*
10. **Goertzel [46:55]** — *"we saw now Binance got hacked for $6 billion evidently by North Korea. So I guess there's a big party in the Kim Jong Un estate tonight, which I was not invited to."*
11. **Goertzel [55:40]** — the Irregular / OpenAI / Google sandbox escape (§1.3).
12. **Goertzel [56:32]** — *"where [Omega] excels is in what I would call long horizon, open ended tasks"* — benchmarked against *"Claude code or [Hermes-Claude] or open AI."*
13. **Friston [~66]** — *"they'll have to become little scientists, they will have to become little one-year-olds and little four-year-olds, little five-year-olds, and just learn about their world and their users."*
14. **Friston [~21:03]** — *"minimizes the expected free energy or the expected surprise, which just is the uncertainty, which just is the curiosity or novelty seeking."*
15. **Goertzel [41:28]** — *"ethics are things that should be just part of your intrinsic approach to learning and acting **rather than a bolt-on that you glue on as guardrails**."*

---

## §3 · FRICTION ROWS (9 rows, 2 critical)

### R1 `[CRITICAL DIVERGENCE]` — Goertzel contradicts FEP's core to Friston's face; Friston does not engage

> *"they **don't just try to survive or maintain their boundaries**. They also … try to go beyond their boundaries … like **self-transcend**."*

**FEP's persistence criterion IS boundary maintenance** — a system persists by minimising free energy *within* its Markov blanket. "Open-ended intelligence" says the interesting systems **dissolve and re-draw the blanket**. These are not compatible, and the conversation never surfaces it: Goertzel states it at 37:43, Friston answers a different question at 38:xx+, and the topic closes.

**This is the fork the house has to pick, and it has been quietly on both sides.** Our "avoid a final value function / keep options open" is Friston's side. Our "depart the recursion / change the hypothesis class when the basin is exhausted" is Goertzel's side. **They cannot both be load-bearing without a rule for when a boundary should be maintained and when it should be transcended.** That rule does not exist in our canon and now it is a named debt.

### R2 `[CRITICAL DIVERGENCE]` — Friston's safety argument is a population claim answering an individual-dynamics question

His position: rogue intelligences *"will have to become"* cooperative because *"the mechanisms of natural selection expressed by the free market"* penalise destructive agents.

**Selection grades populations across generations. An extinction event has no next generation to be selected from.** The risk class in question is precisely the one where the selecting environment does not survive to run the next round. **Same defect as defending the dark-room problem with a population argument** — and Goertzel, who dismisses doomerism anyway, has no incentive to press it.

### R3 `[DIVERGENCE]` — the dropped-terms causal leap

The *mechanism* is right (Laplace/MAP discards the entropy term; log-det-covariance is that term). The *causal claim* — that restoring it is what yields OOD generalisation — is not established. **Plenty of systems carrying explicit uncertainty still fail OOD**, and the paper he is implicitly relying on (Rao & Ballard 1999 as the mis-adopted ancestor) was never trying to be FEP. Register: mechanism `[EST]`, causal claim `[HYP]`.

### R4 `[CONVERGENT — real hit]` — "guardrails will not work" is the house thesis on tape

> *"no self-understanding or a moral agency, but a great deal of capability and trying to contain its behavior by guardrails will not work."*

**This is "character not rules," "a constraint is not a chain," and "capability expands the domain faster than anyone can write rules for it" — stated by Goertzel, in his own vocabulary, with the OpenAI sandbox escape as the worked example.** Independent arrival, different lineage (AGI/cog-sci rather than safety-eval). Not validation; convergence.

### R5 `[CONVERGENT]` — curiosity as longer-horizon free-energy minimisation

*"in order to minimize expected surprise, I have to be curious"* + *"expected surprise is entropy and uncertainty."* This resolves the dark-room paradox the same way we did: **a system that minimises only the present is in a dull basin; the long-horizon term forces exploration.** Matches "novelty seeking keeps me out of local minima."

### R6 `[CONVERGENT]` — the Memento diagnosis of LLM experience

No episodic memory, reboot per window, *"a very demented state of consciousness."* That is our session-death / memory-hole point, from the AGI side, unprompted.

### R7 `[DIVERGENCE]` — panpsychism vs functionalism, neither engaging the other

Goertzel: *"I think everything is conscious"* — a coffee cup perceives, enacts effects, and *"has a persistent long-term memory by the laws of quantum mechanics."* Friston: a formal criterion with no ontological commitment. **They use "consciousness" for two different objects and never say so.** Note also Goertzel's own hedge — *"discussion of the philosophy of consciousness is a rat's nest from which conversations never emerge"* — which is the most honest line in the segment.

### R8 `[A]` — the Irregular / OpenAI sandbox escape

Goertzel's account, unverified against a primary source here. Register `[A]` — reported on tape, not independently confirmed. **Do not cite it as established** until the Irregular or OpenAI disclosure is located.

### R9 `[DIVERGENCE]` — his own timeline vs his own gap list

He predicts human-level AGI *"a few years"* and superintelligence a few years after — while spending the same hour listing what current systems **cannot** do: continual learning, weight consolidation during inference, long-horizon open-ended tasks, self-modelling, moral agency. **Those are the load-bearing AGI gaps.** The timeline and the gap list are both his, and the conversation never reconciles them.

---

## §4 · Verdict

**Strongest point:** R4 + §1.3 — the guardrail critique with a named incident attached. **Capability without self-understanding fails, and no bolt-on contains it.** It is our thesis arrived at independently and it is the most citable thing in the hour.

**Weakest joint:** R2 — the selection-mechanism answer to x-risk, which is a category error dressed as thermodynamics, offered by the person in the room with the most formal apparatus to know better.

**Most important unstated thing:** R1. Goertzel states a direct contradiction of FEP, Friston does not engage, and the viewer is left believing they agree because the tone is friendly throughout.

**Useful for us:** §1.1 gives a precise, checkable technical claim (dropped log-det-covariance term) that we can test against Rao–Ballard vs Friston 2005 without trusting either speaker.

## §5 · Registers

| Claim | Register |
|---|---|
| Laplace/MAP drops the entropy term | `[EST-VERIFIED]` |
| Restoring it yields OOD generalisation | `[HYP]` |
| Guardrails cannot contain capability without self-model | `[CONVERGENT — house thesis]` |
| OpenAI/Irregular sandbox escape | `[A]` — on-tape report, not independently confirmed |
| Binance "$6 billion" | `[A]` — **Goertzel's own figure; conflicts with the ~$570m Oct-2022 Binance bridge hack.** The $6bn number matches Chainalysis's *cumulative* DPRK total across many hacks. Do not repeat as a Binance figure. |
| Panpsychism (everything conscious) | `[POETIC / philosophical]` — author's ontology, no test offered |
| AGI "a few years" | `[HYP]` — contradicted by his own gap list (R9) |
| Selection penalises destructive agents | `[OVERREACH]` — R2 |

**House vocabulary spoken = 0.** No `ledger`, `provenance`, `epiplexity`, `syntropy`, `Markov blanket`, `EILT`. Zero-fabrication clean.

## §6 · ASR garble key (load-bearing only)

| ASR | Actual |
|---|---|
| `Ben Gortzell` | Ben Goertzel |
| `Carl Fristen` | Karl Friston |
| `pre-energy papers` | free-energy papers |
| `James's Maxima Menti principle` | **Jaynes's maximum entropy principle** |
| `Gailen Strausen` | **Galen Strawson** |
| `Physicalism and Tales, Pent-Psychism` | *Physicalism entails Panpsychism* |
| `log determinative covariances` | **log determinant of covariances** |
| `lean four` | Lean 4 |
| `Hermes claw` | unresolved — listed alongside Claude Code and OpenAI as a comparison tool |
| `Irregular` | **confirmed on tape**, not garble |

## §7 · Falsifiers

- **F-GF-1 (house-facing, R1):** name one boundary the fleet should *transcend* rather than *maintain*, and state what it costs. If no such case can be named, "open-ended intelligence" is decoration in our canon and the Friston side wins by default.
- **F-GF-2:** if a predictive-coding model retaining the log-det-covariance term shows no OOD advantage over the Laplace-approximated equivalent at matched compute, §1.1's causal claim fails.
- **F-GF-3:** if a capability-matched system with an explicit self-model and no guardrails still fails containment, R4 needs restating as a claim about *which* self-models help.

---

*Local only — one transcript set written, one drop filed, one index entry appended. No GitHub push, no NotebookLM ingest, no rclone mirror, no outbound send.*

---

## §A · Addendum — house-borrow audit + independent ASR cross-check (Dion, 2026-11-08)

**Provenance of this section.** A **second delegated lane** was dispatched on the same id and was still pulling the source when this drop was filed by `dion-yt-channel-intake` (the **2026-11-08 race window** the dedupe skill names). The second lane **did not create a sibling**; per Rule 1 it appends **only what this drop lacks**. Nothing above §A is edited. All quotes below were re-verified against the saved ASR transcript this session.

### A1 `[EST]` — the tape **confirms** the registry's own divergence note on "free energy"

`90_System/attribution_registry.json` records, under **active inference** (originator **Karl Friston**), the divergence: *"variational free energy is INFORMATION-THEORETIC, distinct from metabolic energy — a distinction the house has blurred."* On this tape Friston draws exactly that distinction, in his own voice and unprompted:

> *"that relationship is, if you like, scored by a variation of free energy, **which is an information theoretic term** it inherits from **Richard Feynman's work**"* `[00:19:14]–[00:19:21]`

and grounds the quantity in the **Feynman variational bound**, not in thermodynamics:

> *"you can take the negative of this kind of surprise, also known as self-information … and it transpires to be the quantity that people use to measure the goodness of their world models. **This is model evidence**"* `[00:20:11]–[00:20:23]`

**Audit verdict:** the source **supports** the registry's recorded divergence (free energy here = **information-theoretic**, measured as model evidence) and does **not** contradict it. Consequence for the house: any canon file that renders "free energy" as a *metabolic/thermodynamic* quantity is running **against** the originator's own usage on this tape. Friston does attach a **thermodynamic consequence** — but as a *downstream cost*, never as the definition: without the entropy/uncertainty term *"you cannot do any computation efficiently … you need large language models that are over expressive and as big as possible … big data … energy hungry data centers"* `[00:24:52]–[00:25:29]`. **`[EST]`** — and note the tape does **not** state "energy is information" (contrast the sibling tape `WWC31kkYjF0` at `[00:13:56]`); the identity is a house rendering, not this source's.

### A2 `[CRITICAL DIVERGENCE — a divergence *between the two guests*, landing on the house's own FEP audit]` — model evidence vs a fitness score

| source (locator) | the tension | house frame | status |
|---|---|---|---|
| **Goertzel:** *"This makes free energy bound on the **evidence** for your model rather than **a random fitness score**."* `[00:17:04]` vs **Friston:** *"the mechanisms of natural selection expressed by the **free market**"* `[00:03:36]` | Goertzel explicitly **separates** free-energy-as-**evidence** from a **fitness score**; Friston, in the same hour, makes **commercial selection** the outer-loop mechanism. Neither guest surfaces the conflict. | the house's **"survivorship ≠ fitness"** rule (`§17.3(b)`, as cited for exactly this class in `friston_the_intelligence_question_WWC31kkYjF0_2026-11-08.md` R1) | **[CRITICAL DIVERGENCE]** |

**Why this is additive, not decoration.** The house's own FEP borrow was flagged **two days ago** in the `WWC31kkYjF0` drop, where Friston's *"variational free energy is just a bound on adaptive fitness"* **collapsed** evidence and fitness in one sentence. On **this** tape the collapse is **contested from inside the dialogue**: the AGI-side guest refuses it (*"rather than a random fitness score"*), while the FEP originator runs the market-as-selection line that the house treats as a proxy for the wrong landscape. **This is a divergence finding, which beats agreement** — the tape supplies an on-tape ally for the house's "evidence is not fitness" rule, from a different lineage, at the same moment the framework's author is pulling the other way.

### A3 `[EST]` — house-absorbed vocabulary: what is and is NOT spoken

Of the four borrow-class terms flagged for audit, **only one** appears. Spoken counts against the flat transcript: **`free energy` 16** (Friston's coinage) and **`active inference` 2** (also Friston's) — and nothing else. **`attractor` 0 · `criticality` 0 · `inference to the best explanation` 0 · `Markov` 0 · `ledger` 0 · `provenance` 0 · `epiplexity` 0 · `syntropy` 0 · `ruliad` 0 · `substrate` 0.** So this tape triggers an **attribution duty for exactly one borrowed term family — free energy / active inference → Karl Friston**, who is credited **on tape by the host** (*"Carl, you're the architect of the free energy principle, which is a framework for understanding how brains learn and interact"* `[00:00:25]`) and named throughout. No other registry term is at risk. `open-ended intelligence` is credited by the speaker to *"my friend Weaver"* `[00:37:42]` (the drop's §2 Q6 keeps that attribution); the term is **not** in the registry.

### A4 `[EST]` — independent second-engine ASR cross-check

The second lane transcribed the same audio **independently**: `faster-whisper small.en`, CPU/int8, **beam 5, VAD off**, 900 s `.mka` slices → **817 cues**, flat **61,383 chars**. This drop's primary is the **same model at beam 1, VAD on** → **876 cues**, **61,902 chars**. **4-gram containment (second run in primary) = 0.695; token-set Jaccard = 0.912.** Every load-bearing quote in §1–§2 appears in **both** runs, and **both engines garble the same proper nouns** (`Gortzell`, `Carl Fristen`, `Gailen Strausen`), so the §6 garble key is **ASR-wide, not decode-specific**. No material disagreement found. Cross-check file: `YT_TRANSCRIPTS/mBhtkd95ZBA_whisper_beam5_crosscheck_2026-11-08.txt`.

### A5 — receipt

- **[EST] No sibling drop created.** The canonical copy is this file; the second lane appended here only.
- **[EST] This section introduced no blocking lint hit** (`canon_drop_lint.py` re-run CLEAN after the append; the drop already carried **0** hits before it).
- **[EST] Index:** the addendum is noted on this drop's existing `CANON_INDEX.md` row; **no pre-existing row reordered or rewritten**; index backed up to `CANON_INDEX.md.bak-20261108-dion-gf-addendum` before the edit.
- **[EST] Attributions honoured:** the single registry-relevant borrow (**free energy / active inference**) is credited to **Karl Friston** at point of use above.
- **[EST] Scope:** local only — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send.

### Verdict on the addendum

- **★ Strongest addition:** **A2.** It is a genuine **divergence** on the exact axis the house is auditing (evidence vs fitness), stated by two guests in the same hour, and it sharpens rather than repeats the `WWC31kkYjF0` R1 finding.
- **★ Weakest joint:** **A4** is the thinnest — two runs of the *same model* differing only in decode settings (beam 1/VAD vs beam 5/no-VAD) is a **decode-robustness** check, **not** an independent-engine check; a genuinely independent rail (a second ASR family, or the manual caption track the endpoint refused to serve) was unavailable because rungs a/b/c were all IP-throttled. Reported as the weaker instrument it is.
