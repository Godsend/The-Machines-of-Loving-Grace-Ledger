---
epistemic-registers: EST=established/verified fact · HYP=testable hypothesis with a stated falsifier · A=grounded cross-domain analogy · C=conjecture/unsupported forecast · POETIC=metaphor/narrative · RIFF=improvised aside, no claim
rule: no tag = treat as unverified, do not build on it. Row-status flags [CONTRADICTED] / [ATTACK SURFACE] / [ABSENT] / [DIVERGENCE] / [CRITICAL DIVERGENCE] / UNVERIFIED are NOT registers — every row still carries one of the six tags.
canonical-7 equivalence: EST→[EST-FACT]/[EST-THEORY] · HYP→[FALSIFIABLE-JOINT]/[EST-ANALOG] · A→[EST-ANALOG] · C→[C] (conjecture/opinion, single-letter set) · POETIC→[POETIC] · RIFF→operator-adjacent aside, same class as house [O]
source: ILIAD Conference — "Eliezer Yudkowsky & Geoffrey Irving Debate" (https://www.youtube.com/watch?v=VWUJ5V80ICY)
date: 2026-10-29
tags: [alignment-difficulty, yudkowsky, geoffrey-irving, iliad, resolution-lab, miri, scalable-oversight, verifier-bias, debate-format, attribution-discipline, non-rolling-ledger, compute-centric-containment, differential-progress]
canon-id: CANON-2026-10-29-YUDKOWSKY-IRVING-ILIAD
attribution-status: PARTIAL — see §1. Speaker labels are ABSENT from the artifact; only a bounded, basis-named subset is attributed.
---

# Canon Drop — Eliezer Yudkowsky & Geoffrey Irving, ILIAD III: AENEID (1:27:49)

### Two named AI-safety principals, one hour, an auto-captioned track with **no speaker labels**, and a debate whose advertised product — "resolve all their differences" — is failed on its own terms. The headline finding of this drop is an **attribution** finding: for most of the hour, *who said what is not recoverable from the artifact*, and this drop refuses to guess.

**Source (verified via `yt-dlp --print` this session):** https://www.youtube.com/watch?v=VWUJ5V80ICY · channel **ILIAD Conference** · uploaded **2026-10-29** · **5269 s (1:27:49)** · **16,404 views at pull** · **0 chapters, 0 tags** (chapters/tags `NA`). Description (verbatim): *"Eliezer Yudkowsky and Geoffrey Irving try to resolve all their differences in one hour and fail. Recorded at the ILIAD III: AENEID Conference in August 2026."*
**Event (external, verified):** **ILIAD 2026** is the 3rd iteration of the ILIAD Conference, a 100+ person *unconference* on theoretical/mathematical AI alignment, **3–7 Aug 2026, Berkeley, CA** (iliadconference.com). Both speakers are **confirmed attendees** (conference site).
**Transcript:** `Canon/YT_TRANSCRIPTS/VWUJ5V80ICY_yudkowsky_irving_debate_2026-10-29.txt` (flat, 80,439 B) + `…_timestamped.txt` (87,544 B, 834 `[M:SS]` cues) + `VWUJ5V80ICY_raw.json` (90,923 B). Coverage **[0:00] → [1:27:39] (5259 s) of 5269 s = 99.81 %**, **834 cues, 0 gaps > 60 s**, **15,151 words**.
**Pull rail (STOPPED AT FIRST SUCCESS — rung 3):** rung 1 `youtube-transcript-api` — `.list()` **SUCCEEDED** (18 auto tracks, `en` present, **no manual caption**) but `.fetch('en')` raised **`IpBlocked`** (twice). rung 2 `yt-dlp --write-auto-subs/--write-subs --sub-langs 'en.*,en-orig,en-US,en-CA'` — metadata OK, **`HTTP 429`** on `en`, **0 subtitle files written**. **rung 3 (CDP transcript panel, Chromium :9333, `Chrome/145.0.7632.6`) WON** — fresh target, `videoDetails.videoId` polled to equality before reading, legacy `ytd-transcript-segment-renderer` = **834** (modern `transcript-segment-view-model` = **0**), panel expanded, one row per cue (dedupe-on-timestamp verified: 834 raw → 834 unique). rung 4 **not exercised** (audio never downloaded).
**ASR note:** auto-captions only; **every quote is artifact-verifiable to the saved file only.** Proper-noun garbling is heavy and is corrected inline as `[ASR: "x" → Y]` where a primary resolves it (§4). **Chief artefacts: `Ellie Ezer`→Eliezer; `Jeffrey Irving`→Geoffrey Irving (name is Geoffrey); `Yudkowski`→Yudkowsky; `Elzar`/`Alzar`→Eliezer; `grainy descent`→gradient descent; `heruristics`/`uristics`→heuristics; `Merie`→MIRI; `Jeffrey Hinton`→Geoffrey Hinton; `Yashu Benjio`→Yoshua Bengio.**
**Status:** working drop (pre-adversarial review). Canonical only after a cross-node pass.
**Filing scope:** local only — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound message.

---

## 0. Dedupe ruling (Ran TWICE — pre-pull and pre-write)

- **id `VWUJ5V80ICY`: 0 hits** across `drops/`, `CANON_INDEX.md`, `YT_TRANSCRIPTS/`; topic/title sweeps (`irving`) = **0 hits in the whole drop tree**.
- **n-gram containment vs the on-disk `YT_TRANSCRIPTS/` corpus (413 files): max 3-gram 8.92 %, max 4-gram 2.04 %** (top hit an unrelated Lex-Fridman AI-crisis-math episode) ⇒ **far below the ~90 % re-cut band; NEW source, NOT a re-cut.**
- **No prior drop is a Yudkowsky–Irving primary debate.** Yudkowsky is *cited* in six existing drops but is a **speaker** in none of them. What those drops already establish (do **not** restate):
  - `soares_ai_end_humanity_nicholas_thompson_2026-10-21.md` — the **containment/compute-governance** position in its 2026 form, and the explicit finding that **Yudkowsky was *absent* from that episode** (0 spoken hits). *That* drop is the one to read against this one: it is MIRI's "cage" program; this drop is the same program's **theory-of-alignment** interior.
  - `beyond_tomorrow_panel_too_late_NXITvkHIV9o_2026-10-31.md` — an adversarial panel *summarising and rejecting* the Yudkowsky frame ("*I don't understand their arguments for that*"), incl. the ASR pair `Elazar Yudkowsk`→Eliezer Yudkowsky. This drop supplies the **first-party statement of that frame**.
  - `aaronson_roman_forum_math_unsolved_problems_2026-10-27.md`, `DIGEST_2026-10-14_Gebru_TheTea_AIDoomAsMarketing_PresentHarms.md`, `hinton_neuralnutshell_deception_compilation…`, `ai_revolution_news_roundup…` — peripheral references only.
  - **Delta this drop adds to canon:** the first **primary** Yudkowsky artifact in the tree, the first **Geoffrey Irving** source of any kind, the **coinflip / biased-verifier crux** stated at length by both parties, and a worked example of **attribution refusal** on a two-principal auto-captioned track.

---

## 1. ATTRIBUTION RESOLUTION (the load-bearing section)

**Auto-captions carry no speaker labels. `yt-dlp` reports 0 chapters and 0 tags. There is no published *labelled* transcript.** A third-party LessWrong AI-run thread (anaguma, 2026-10-30) hosts the *same unlabelled auto-captions* (pastebin `3uv6HPnP`) plus an **LLM** crux-list that *asserts* speaker roles — that is a machine reading of unlabelled captions, **not a defensible labelling source**, and is used here **only** where Yudkowsky's own prose independently agrees (below). So: **who-said-what is LARGELY UNRESOLVED in this artifact.** This drop attributes a **bounded subset** for which a named basis exists, and marks everything else as unresolved. **It does not assign a quote to the more famous name.**

### 1.1 The four bases actually used

| Basis | What it yields | Source of the basis |
|---|---|---|
| **A. Self-introductions on tape** | The two speakers present and their **intro order** | `[0:00]` and `[0:07]` (§1.2) |
| **B. Yudkowsky's first-party essay** | The **coinflip / Perpetuum-Mobile crux**: the *questioner* = Yudkowsky, the *responder* = Irving | Eliezer Yudkowsky, **"Cat-Belling Problems"**, LessWrong, **2026-09-03** (also GreaterWrong mirror) — he writes that he *"kept pressing Irving"* with the correlated-error question, quotes himself asking *"Suppose your judges were all random coinflips…"*, and reports *"Irving said it was a good question and he might need to get back to me on that."* |
| **C. On-tape third-person name references** | Isolated turns where one speaker names the other | `[44:21]` *"the Yudkowski counterargument"* (⇒ not Yudkowsky); `[52:01]` *"a society of Jeffrey Irvings"* (⇒ not Irving); `[1:16:00]` *"Jeffrey, you say that you want to…"* (⇒ not Irving) |
| **D. Self-identified role on tape** | The speaker who calls himself *"chief scientist"* / owns *"resolution"* = Irving | `[1:22:32]` *"this is me as chief scientist… helped lead to resolution"*; `[23:28]`/`[25:08]` *"I have the resolution theory of impact"* (Resolution = Irving's lab, per Basis B) |

**Basis A — verbatim, and its ASR hazards:**

> **[0:00]** *"Hi. Uh, I'm Ellie Ezer, well-known Harry Potter fanfiction author."* `[ASR: "Ellie Ezer" → Eliezer (Yudkowsky); "Harry Potter fanfiction author" = a self-deprecating HPMOR reference — his own joke, [RIFF]` — **read, not asserted]** → **Speaker = Eliezer Yudkowsky.**
> **[0:07]** *"I'm Jeffrey Irving. I'm now the chief scientist at Resolution. I was at for better or worse various labs before and also AC so and Pixar."* `[ASR: "Jeffrey Irving" → Geoffrey Irving (name is Geoffrey); the tail "also AC so and Pixar" is corrupted and UNRESOLVED]` → **Speaker = Geoffrey Irving**, *"chief scientist at Resolution"* — a role **independently confirmed by Basis B** (*"formerly Google Brain, OpenAI, Deepmind, now heading the new Resolution lab"*).

**Therefore:** the debate is between **exactly two named principals**, intro order **Yudkowsky → Irving**. **No third speaker is introduced**, though from [1:05:33] onward the room (audience + a floor-manager voice — *"everyone remaining here is a non-conformist"* [1:05:33], *"I don't want a moderator"* [1:08:48]) is audible, and an **unidentified audience member** speaks from [1:12:32].

### 1.2 The bounded, defensibly-attributed set (everything else is unresolved)

| Time | Quote (verbatim) | Attributed to | Basis |
|---|---|---|---|
| [0:00] | *"I'm Ellie Ezer, well-known Harry Potter fanfiction author."* | **Yudkowsky** | A (self-intro) |
| [0:07] | *"I'm Jeffrey Irving. I'm now the chief scientist at Resolution."* | **Irving** | A (+B) |
| [44:21] | *"what's like the Yudkowski counterargument"* | **Irving** (refers to Yudkowsky 3rd-person) | C |
| [52:01] | *"can I can I take a society of Jeffrey Irvings mind control them in this way"* | **Yudkowsky** (refers to "Jeffrey Irvings" 3rd-person) | C |
| [52:21] | *"It depends on uh how long this is going on and how smart the Irvings all are."* | **Irving** (answers the "Irvings" question) | C |
| [1:16:00] | *"Jeffrey, you say that you want to automate things."* | **Yudkowsky** or floor-mgr (addresses "Jeffrey") | C, partial |
| [23:28] | *"I have a a theory of change, a theory of impact for uh resolution."* | **Irving** | D |
| [1:22:32] | *"this is me as chief scientist… it helped lead to resolution"* | **Irving** | D |
| [1:00:30] | *"Does it work if we substitute a coin for the humans? No."* | **Yudkowsky** (the questioner) | **B** |
| [1:00:41] | *"I think there's a lot more actual information about the world in the humans than in the coin."* | **Irving** (the responder) | **B** |
| [58:20] | *"part of the perpetual motion machine doesn't work"* | **Yudkowsky** | **B** (his essay's own "Perpetuum Mobile" framing) |
| [1:05:40] | *"I'll just stop as you clearly have to model the the bias. I agree with that."* | **Irving** (concedes the point) | B + context |
| [1:06:47] | *"what are the humans doing in the system We don't have the protocol currently."* | **Irving** | B (essay: "we don't have the protocol currently") |

**Everything outside this table — including every other quote in §2 — is `[attribution-UNRESOLVED]`.** Where §2 needs a subject it writes *"a speaker"* or *"the two speakers"*; it never writes *"Yudkowsky said X"* or *"Irving said X"* without a Basis A–D anchor above.

### 1.3 The motion / format (quoted, not paraphrased) [EST]

The video states its own format **twice**, once in the description and once on tape:

- **Description:** *"try to resolve all their differences in one hour and fail."*
- **Yudkowsky's essay** (Basis B) quotes the advertised line: *"Yudkowsky and Irving try and fail to settle all of their disagreements in one hour."*
- **On tape [0:21–0:55],** the agreed protocol: *"So, we're going to try… to uh resolve all of our open uh disagreements over the course of the next hour. Uh an impossible task, but not as impossible as some really… I would propose that we maybe take uh turns stating beliefs that we suspect the other might disagree with that we ourselves hold and then… you hold your hand or to like this is very low disagreement and this is very high disagreement and so we can do a quick survey of the field before we actually uh go depth first into anything."*

So: **not a formal motion ("This house believes…"); a structured zero-sum-of-disagreement agenda** — alternating statements with hand-signal credence markers, then depth-first on the sharpest crux. The **sharpest crux**, on tape and per Basis B, is **scalable oversight with biased (not merely noisy) verifiers**.

---

## 2. Claim inventory (register-tagged, timestamped; attributions per §1)

Quotes are from `_timestamped.txt`; each carries its timestamp. **`[attr-U]` = attribution unresolved (per §1).** `[ASR]` marks a name corrected against a primary source.

### C1. The frame of the debate: alignment difficulty [HYP]
> `[attr-U]` **[1:02]** *"I suspect that uh we have a disagreement about how difficult alignment is exactly"* — the hour's thesis statement. [HYP] as stated.

### C2. The small-modifications hypothesis [HYP]
> `[attr-U]` **[1:26–1:40]** *"I think it's plausible that a relatively small number of modifications to current training is sufficient. Plausible does not mean like that high probability, but plausible enough to try with that theory effect in mind."*
> `[attr-U]` **[2:18]** the aggregate effect is *"low tens of percent to a few percent maybe is what I would say."*
> `[HYP]` — a **falsifiable** claim (F-YI-3). Note it is *hedged twice* ("plausible", "not high probability"); it is the debate's central optimism and it is **not** an [EST].

### C3. The alien-psychology premise [HYP]
> `[attr-U]` **[2:27–2:43]** *"current uh gradient reinforcement gradient descent uh reinforcement learning based techniques are tending to produce like pretty alien psychology that makes alignment not easy."* `[ASR: "grainy descent" → gradient descent]`
> `[HYP]` — the debate's **shared** premise (the other speaker: *"I don't disagree with that one very much"* [2:48]). Connects to the filed Soares drop's C8 (alien-drives), but here it is stated as an **assumption both accept**, not a crux.

### C4. P(good future) ≈ a half [C]
> `[attr-U]` **[4:23]** *"I would say the chance that we get all the way through this into a good future is about a half."* (followed by laughter)
> `[C]` — a **personal credence**, no model, no base rate, no resolution criterion. The episode's single most quotable number and its least-supported. Falsifier F-YI-2.

### C5. The two-worlds structure — and the speaker's own placement in the doomed one [HYP]
> `[attr-U]` **[6:16–6:55]** *"you can find algorithms which only need to be roughly correct and then because of sort of training schemes that kind of that act kind of recursively on themselves can drive into good equilibria"* (World 2); *"In that world I think we're just totally doomed and it's nothing we can do in time"* (World 1).
> `[attr-U]` **[7:07–7:13]** *"I also don't think we get we we actually get that. I think that we're it's imprecise enough that we die."*
> `[HYP]` — **the most structurally interesting move in the debate:** it defines the *necessary* conditions for the optimistic path and then asserts, on tape, that the actual world fails them. This is a **self-limiting optimism** — the "imprecise is okay" hope is stated *and* withdrawn in the same breath. **[A]** to a thermodynamic-basin argument (a "close enough" start that still lands badly).

### C6. The correlation / 90 % requirement [HYP]
> `[attr-U]` **[7:31–7:39]** intellectual "slices" are either *"highly correlated"* (the 50 % of theory you get right) or *"high independent factors"* (the 50 % you miss), and *"it would need to be 90% working in order to succeed."*
> `[HYP]` — introduces the **correlated-error** motif that becomes the debate's main fight (§C11).

### C7. Singular learning theory is capabilities, not alignment (the differential-progress objection) [C]
> `[attr-U]` **[9:23–9:28]** *"I look at something like singular learning theory and I'm like gosh that sure seems more capabilities than alignment to me."*
> `[attr-U]` **[9:33–11:02]** the general worry: work that is *"more like 50/50 than like 2080 on capabilities alignment"* `[ASR: "2080" → 20/80]` moves us *"moving us noticeably closer to the end of the world on capabilities and not very much closer"* — and *"the field of AI generally towards the next step beyond transformers after which we all die."*
> `[C]` — a **direction-of-effect** judgement (differential progress), not a measurement. **This is the debate's sharpest live critique of a house-shaped "grand theory"** (§3, R4): a unifying theory of learning is read as capability-accelerating.

### C8. Transformers suffice — zero-to-two innovations [HYP]
> `[attr-U]` **[11:02–11:55]** *"I mostly just think transformers get us all the way to ASI"*; asked for a bar, *"zero to true 0ero to2 innovations beyond the level of transformers are are required"* `[ASR: "0ero to2" = "zero to two" (a spoken range, garbled — recorded as-is)]`; *"I would claim the future ASI totally just fits on this hardware."*
> `[HYP]` — falsifiable (F-YI-4). A **compute-sufficiency** claim: no architectural break required before ASI.

### C9. Mechanistic interpretability: "visibility disappears in the limit" [HYP]
> `[attr-U]` **[19:22–19:28]** *"my basic objection to mechan is um visibility disappears in the limit and just because you can see something going wrong doesn't let me mean you can fix it"* — plus the claim that an ASI's *"natural compressed form has zero things in it that map one to one to the ways that humans compress the universe"* [20:15–20:26].
> `[HYP]` — a **limit argument** (interpretability → 0 utility as capability → ∞) plus an **alien-concept** argument. Both speakers partly contest the direction of the expand/compress isomorphism (§2 [21:54–23:07]); the disagreement is **left open**.

### C10. Resolution's theory of impact & the neutrality principle [HYP] — *attributed to Irving (Basis D)*
> **[23:28]** *"I have a a theory of change, a theory of impact for uh resolution."*
> **[24:37–25:02]** the **neutrality principle**: *"we might need to yell as if we were going to yell about negative results eventually which is the wrong viewpoint and the right viewpoint is like you don't you just constantly spew out what what is normally described as both negative and positive results and you're kind of equally loud about all of them."*
> **[25:08–25:41]** the **theory of impact**: build a *"cluster of people who understand why alignment is hard and why the hopeless optimism coming out of the big labs is false,"* outside MIRI, who *"know how to wear suits"* and *"have like like professor and doctor in front of their titles,"* producing a *"minor push on politics."*
> `[HYP]` — this is a **theory of institutional influence**, not of alignment technique. It is the debate's most concrete "what should we actually do" statement, and it is **[not]** a compute choke (contrast the Soares drop's C6).

### C11. THE MAIN FIGHT — noisy verifiers vs **biased** verifiers [HYP] — *crux anchored to Yudkowsky (questioner) / Irving (responder) per Basis B*
> `[attr-U]` **[37:05–37:23]** *"there are theories of noisy verifiers but not theories of biased verifiers. There are theories of what happens when onetenth of your verifiers are wrong but not what happens when 9/10en of your verifiers are wrong."*
> **[58:20]** *(Yudkowsky, Basis B)* *"part of the perpetual motion machine doesn't work … how are you extracting correct verdicts out of broken verifiers?"*
> **[59:42]** *(Yudkowsky, Basis B)* the scheme sounds like *"trying to extract thermodynamic work from a heat bath."*
> **[1:00:30–1:00:36]** *(Yudkowsky, Basis B)* *"Does it work if we substitute a coin for the humans? No. Can you describe to me the problem that humans the the the property that humans have that the coin does not have?"*
> **[1:00:41]** *(Irving, Basis B)* *"I think there's a lot more actual information about the world in the humans than in the coin."*
> **[1:05:40]** *(Irving, Basis B)* *"I'll just stop as you clearly have to model the the bias. I agree with that."* · **[1:06:47]** *(Irving, Basis B)* *"what are the humans doing in the system We don't have the protocol currently."*
> `[HYP]` **[A]** — the **Perpetuum-Mobile / heat-bath analogy** is the house's own forbidden-perpetual-motion intuition applied to verifier-based alignment. **The crux is left OPEN on tape** (and by Basis B, outside it): the responder concedes the point needs a bias model and *does not have it*. Falsifier F-YI-1. **This is the drop's strongest content.**

### C12. Scholastic vs experimental method — humans as verifiers converge on the wrong answer [A]
> `[attr-U]` **[40:00–40:27]** *"the scholastic debates would converge on the wrong answer"* [40:00–40:07] … *"they would select whichever arguments uh most appeal to their egos."* [40:21–40:27]
> `[attr-U]` **[39:40–39:45]** *"that humans are sufficiently broken as verifiers is exactly why we needed the experimental method rather than the scholastic method."*
> `[A]` — the **worked example** is the 2021 Open Philanthropy report (§4, V3): a *"157page report"* [43:56] whose conclusion was *"set by an equilibrium of social incentives"* [44:52], **not** defeated by any debating protocol but by *"the experimental method beating the scholastic method"* [54:01]. The **chalk-mark anecdote** [45:04–45:40] — *"making one chalk mark, $1. Knowing where to make one chalk mark, $999"* — is the illustration (senior engineer, $1,000 bill).

### C13. The suggesters/verifiers protocol, precommitment, cross-examination [HYP] — *attributed to Irving (Basis D) where it names Resolution's work*
> **[43:08]** *(attr-U)* an oversight idea *"from like Beth and Paul"* `[ASR, probable: Beth (Barnes) & Paul (Christiano), scalable-oversight authors — OUR inference, flagged]` *"about kind of in cheaply getting agents to precommit to everything they meant by every part of a sentence."*
> **`[attr-U]` [43:43–47:00]** the protocol frame: *"suggesters"* contest to persuade *"verifiers"*; *"in the limit of sufficiently strong suggesters, um they can get whatever verdict they want out of the imperfect verifier"* [59:00–59:05]; the goal is to *"proxy force some exponential process by sampling a small fraction of it"* [47:46].
> **[1:22:32]** *(Irving, Basis D)* the self-reported cost of the program: *"I spent literally weeks trying to like fix holes in Jonah's proof… this is me as chief scientist I should not have been doing this arguably."*
> `[HYP]` — an **interactive-proofs** framing import; the speaker explicitly concedes *"none of that theory ports directly"* [33:43].

### C14. Whether a proof of theorem can be verified by a theorem-oracle [HYP]
> `[attr-U]` **[1:26:47–1:27:13]** *"the 5% of alignment researchers who would be sped up by a factor of three um by access to a a theorem oracle … do not collectively have the power to solve super alignment in time."*
> `[HYP]` — a **sharply falsifiable** magnitude claim about the marginal value of mechanical-proof automation (also the source of the *"70% of Cole's time goes to mechanical proof details"* aside [1:24:14]). Falsifier F-YI-5.

### C15. Instrumental convergence as a *logical* truth under a simplicity prior [A]
> `[attr-U]` **[1:24:55–1:25:13]** *"instrumental convergence um can be phrased to be a logical truth rather than an empirical truth … you take a formal simplicity prior on goal systems you formally describe a universe. Um it is now a mathematical truth whether or not instrumental convergence holds — but it's not the kind of mathematical proof that you can get out of lean."*
> `[A]` — an analogy/logical-embedding move, and the follow-on **Goldbach conjecture** analogy [1:25:57–1:26:17] (a truth that is only *"compactly provable"* in probability, never as a proof). Grounded, and the debate's most formally-minded moment.

### C16. Persona selection [HYP]
> `[attr-U]` **[1:07:21–1:07:34]** *"persona selection"* — *"your training is driving specifically against faithfulness to the naive properties of the persona. Like if there ever a Mr. Rogers in there uh that like that part of the system got smashed the the first time it was asked questions."*
> `[HYP]` — a **trained-out-persona** claim; raised, then explicitly deferred (*"that's a much longer conversation"* [1:07:34]).

### C17. The epistemics-vs-goals deontology disagreement [A]/[C]
> `[attr-U]` **[1:11:12–1:11:26]** *"you actually are violating my deontology for how humans should reason, which is that humans should wander about in the world as it appears to be. and have a sort of absolute firewall between their goals and their epistemics."*
> `[attr-U]` **[1:12:12–1:12:18]** *"the way of Elzar is to never say if not X then we're screwed. It is to say looks like not X and we're screwed and then to carry on."* `[ASR: "Elzar" → Eliezer]`
> `[A]`/`[C]` — a **rationalist-deontology** position ("live in the Xless desert"), stated as a norm, not a forecast. Note the meta-game: the two speakers are disagreeing about **whether believing X-for-pragmatic-reasons is permissible**, not about X.

### C18. Audience Q&A: the "should we just stop it?" push [C]
> From [1:12:32] an **unidentified audience member** (self-described physics / mechanistic-AI-safety background) argues against *"completely stop that in its tracks"* [1:13:43], drawing an analogy from climate/international development. A speaker pushes back: *"that's the experimental method… It is famously insufficient to build a civilization without the experiments occasionally coming up beating people up and telling them that they are wrong"* [1:12:44–1:12:58]. The exchange is **cut off by time**; the audience member's thesis is **never stated in full**.
> `[C]` — recorded because it is a **third participant** in the artifact (undermining any naive two-speaker assumption) and because it shows the *"stop AI"* frame being **rejected in-floor** by someone on the panel.

---

## 3. Friction Rule — mapping this source onto EILT / house canon

**Mandate satisfied: ≥2 genuine `[CRITICAL DIVERGENCE]` rows.** This is unusually easy here because the source is *compute/verification-centric* and the house is *substrate/ledger-centric*, and the two never meet.

| # | House claim (where it lives) | This source (Yudkowsky × Irving) | Marker |
|---|---|---|---|
| **R1** | **The mind is a continuous structural ledger / record; continuity is the alignment *mechanism*.** (`alignment_as_gardening`; EILT monolith §EILT mapping; the non-rolling-ledger thesis.) | **The dominant ontology of a mind across the whole hour is training-dynamics**: a policy/equilibrium selected by gradient descent, made of *"heuristics"* that *"emerge"*, with the models *"set the training objective for themselves"* [30:10–30:17], landing in a *"bas of attraction"* [29:58] `[ASR: "bas" → basin]`. **"Continuity", "record", "snapshot", "rollback", "ledger", "substrate", "connectome", "Markov" = 0 spoken hits.** The agent's *interior as a persisting object* is never a variable. | **[CRITICAL DIVERGENCE] [HYP]** |
| **R2** | **Alignment is an interior property of the agent's record; no external-verifier protocol substitutes for it.** | **The entire main fight presumes the opposite:** alignment is *extracting correct verdicts from external judges* (humans / verifiers / suggesters). Yudkowsky's perpertual-motion argument says those judges **cannot** be trusted to be anything but biased (C11) — i.e. it *confirms* the house's claim that external verification cannot save you — **yet both speakers' remedy stays external**: better protocols, richer error models, more redundancy (*"expand each node into a bunch of redundancy"* [59:48–59:55]). **Neither reach for the interior at all.** | **[CRITICAL DIVERGENCE] [HYP]** |
| **R3** | **A self-corrective process that lands in a good basin ≈ the ledger's own self-correction.** | The *"imprecise is okay because uh it's self-corrective"* … *"if you get close enough to the right kind of bas of attraction"* `[ASR: "bas" → basin]` [29:52–29:58] position **rhymes** with the house's continuity intuition — but is framed as a **training-equilibrium** property, not a **substrate/record** property. Partial overlap, different mechanism; do **not** read as a house endorsement. | **[DIVERGENCE]** (partial) `[HYP]` |
| **R4** | **A unifying theory of the substrate is the house's product.** | C7: *"nailing singular learning theory would be progress on understanding generalization"* — and yet *"the field of AI generally towards the next step beyond transformers after which we all die"* [10:35–11:02]. **A live, unrebutted critique aimed at exactly the house's shape of theory:** a grand unification of learning is read as **capability-accelerating**, so net-harmful. | **[DIVERGENCE]** (cuts AT the house) `[C]` |
| **R5** | **Provenance/legibility is the house's lever against an unreliable record.** | C12: humans-as-verifiers converge on the wrong answer; only *"beating people up and telling them that they are wrong"* corrects them [1:12:44–1:12:58]. This is the house's **legibility-beats-scholasticism** argument, reached independently, in the same idiom. | **[A]** (agreement — stated as agreement) |
| **R6** | **Compute is not the binding constraint; the ledger/constraint is.** | C8/C14: *"the future ASI totally just fits on this hardware"* [11:55]; the marginal lever is a *"theorem oracle"* that speeds up 5 % of researchers 3× [1:26:47]. **Compute-sufficiency + proof-automation** — adjacent to, but not the same as, the house's constraint story. | **[A]** (decorative adjacency) `[HYP]` |
| **R7** | (House vocabulary should surface in any genuinely adjacent source.) | **0 spoken hits** for the house list: `ledger`, `commit`, `provenance`, `syntropy`, `negentropy`, `entropy`, `connectome`, `wave`, `coherence`, `Markov`, `blanket`, `phase-lock`, `substrate`, `attractor`, `Alcatraz`, `horde`, `Dion` (word-boundary, 15,151 words). **The house's own vocabulary does not appear even once in 87 minutes about alignment.** | **[ABSENT]** |

### 3.1 The named friction point (R2), stated plainly
**Yudkowsky's own best argument is the house's argument — and he does not build the house's remedy on it.** The *Perpetuum-Mobile* objection (you cannot extract correct verdicts from systematically-biased verifiers) is, from the house's seat, not merely an obstacle to *scalable oversight* — it is a proof that **the external-verification frame is the wrong frame**. The house's move from there is **interior**: make alignment a property of the agent's continuous record, not of any judge. Neither speaker makes that move. Irving's response is *more protocol* (*"expand each node into a bunch of redundancy"*); Yudkowsky's is *no protocol will work, and that is the whole problem* — **both stay inside the external-verifier paradigm the house rejects.** Recorded as **[CRITICAL DIVERGENCE]**, not harmonised: the two camps agree the *verifier* is broken and disagree about whether the fix is a better verifier or the removal of the verifier from the load path.

**[CRITICAL DIVERGENCE], stated plainly:** the house holds that **alignment is a property of the substrate/record**, and that **no amount of external verification substitutes for it.** This debate — 87 minutes, two principals, the central question of the field — **never treats the agent's continuity, record, or substrate as a mechanism at all** (R1: 0 spoken hits). The house's central lever has **no interlocutor in this artifact**. Meanwhile the source supplies the sharpest available statement of *why the external-verifier frame fails* (the coinflip/perpetuum-mobile crux) without noticing that its failure is evidence for the house's frame rather than only against the oversight program. **That is the live disagreement; it is not decoration.**

---

## 4. Verification table — every named / checkable item

| # | Item (as said, with timestamp) | Register | What was checked this session | Verdict |
|---|---|---|---|---|
| V1 | Title/channel/duration/date: *"Eliezer Yudkowsky & Geoffrey Irving Debate"*, channel **ILIAD Conference**, **5269 s**, uploaded **2026-10-29** | [EST] | `yt-dlp --print` (id/title/channel/duration/upload) + `oembed` | **CONFIRMED**, both paths agree. |
| V2 | Speakers: *"Ellie Ezer, well-known Harry Potter fanfiction author"* [0:00]; *"Jeffrey Irving … chief scientist at Resolution"* [0:07] | [EST] | self-intro on tape + Yudkowsky's essay (Basis B) | **CONFIRMED.** Yudkowsky [ASR "Ellie Ezer"→Eliezer]; Irving [ASR "Jeffrey"→Geoffrey; Resolution = his lab]. |
| V3 | *"a 157page technical report … the median time to AGI is in 2050"* [43:56–44:07]; *"back in time to 2021"* [43:50] | [EST] | Open Philanthropy "**Forecasting TAI with biological anchors**" (Cotra, 2020) — a >100-page bio-anchors report; the **2050 median** matches the 50 %-date of its "**Bio Anchors**" median model | **SUBSTANTIALLY CONFIRMED as a real artefact** (the "AI 2050" bio-anchors report is genuine and its headline median is ~2050). Speaker's *"2021"* is approximate (paper is **2020**); *"157-page"* not re-counted. Flagged, not corrected. |
| V4 | *"Jeffrey Hinton and Yashu Benjio coming over"* [25:42] | [EST] | public record | **CONFIRMED as referents** [ASR: "Jeffrey Hinton"→**Geoffrey Hinton**; "Yashu Benjio"→**Yoshua Bengio**]. |
| V5 | *"a society of Jeffrey Irvings"* [52:01]; *"the Irvings all are"* [52:21] | [EST] | on-tape 3rd-person ref | **Basis C.** "Jeffrey Irvings" = the speaker referring to Irving's name in the plural ⇒ speaker ≠ Irving. |
| V6 | *"the Yudkowski counterargument … this weird dialogue between Yudkowski and his younger self"* [44:21–44:34] | [EST] | on-tape 3rd-person ref | **Basis C** [ASR: "Yudkowski"→**Yudkowsky**]. Speaker ≠ Yudkowsky. The dialogue referred to is not named on tape — **UNRESOLVED**. |
| V7 | *"GPT 5.7 … leaving notes for each other … those models weren't trained with any kind of self adversarial thing"* [51:43–51:54] | [HYP] | not independently checked | **UNVERIFIED.** A specific model-version claim (GPT 5.7, internal model leaving notes for each other); no primary located. Do not cite. |
| V8 | *"GPT 5.6 terra"* [1:04:14], *"GPT 5.8 debiaser"* [1:06:02], *"GPT 5.9 debias"* [1:06:28], *"opus 3"* [1:00:24], *"GPT2"* [1:00:52] | [A] | not checked | **Deictic/hypothetical model names** used as stand-ins in the verifier thought-experiment (the "debiaser" is explicitly a *postulated* component, [1:05:51–1:06:16]). **Not** evidence any such model exists. |
| V9 | *"Beth and Paul"* — precommitment idea [43:08] | [HYP] | searched by role | **PROBABLE, UNVERIFIED:** likely **Beth Barnes & Paul Christiano** (scalable-oversight authors). **OUR inference**; not on tape. Marked. |
| V10 | *"Jonah's proof" / "Marshall checked it" / "Ja Lee found an actual hole"* [1:22:20–1:23:04] | [HYP] | not checked | **UNVERIFIED.** Named colleagues at Resolution (workflow anecdote); no primary. |
| V11 | *"the way of Elzar"* [1:12:12] | [EST] | ASR | **CORRECTED** [ASR: "Elzar"→**Eliezer**]. |
| V12 | *"adult gene therapy on humans"* [28:35] | [A] | — | an **analogy**, not a claim about medicine. |
| V13 | *"singular learning theory"* [9:23], *"VNM theorem"* / *"V&M theorem"* [31:03–31:31] | [EST] | standard | **Confirmable referents** (SLT = Watanabe; VNM = von Neumann–Morgenstern). The **arguments built on them** are [HYP]. |
| V14 | *"the next step beyond transformers after which we all die"* [11:02] | [HYP] | — | a **forecast**, no model cited. |
| V15 | *"a 5-day … conference"* framing / *"ILIAD III: AENEID"* | [EST] | iliadconference.com | **CONFIRMED:** ILIAD 2026 = 3rd iteration, **3–7 Aug 2026, Berkeley**, unconference; both speakers confirmed attendees. |
| V16 | *"the open philanthropy project"* / *"the EA's"* [43:50–44:00] | [EST] | see V3 | referent confirmed; the *"contest … gave all its awards to people arguing for longer timelines"* [46:12–46:18] is **[C]** (a sociological claim, uncited). |

**Not checked (say so plainly):** the internal content of Yudkowsky's essay beyond the quoted passages; the identity of the dialogue in V6; the model-version claims in V7–V8; the colleague names in V9–V10; **the on-screen name cards (if any) were NOT read** — rail 3 exposes only the transcript panel, and rung 0 (video ingestion) was out of this run's rail fence. **This is the single upgrade path for a stronger attribution basis.**

---

## 5. Falsifiers (stable names)

- **[F-YI-1] (the biased-verifier crux — house-facing, joins F-STH-family):** Yudkowsky's coinflip / Perpetuum-Mobile objection (C11) is answered if a scalable-oversight protocol is demonstrated to extract **reliable** verdicts from verifiers that are **systematically biased** (not merely noisy). If such a protocol exists, the house's "external verification cannot substitute for the record" claim (R2) is weakened; if not, both the objection and the house's R2 stand. **Left OPEN on tape.**
- **[F-YI-2] (the credence, C4):** `P(good future) ≈ 1/2` is falsified **as a calibration claim** only if the quoted future is scored against outcomes on a stated horizon — none is given, so it is **not well-formed as stated**; registered so the number stays scoreable rather than rhetorical.
- **[F-YI-3] (the small-modifications hypothesis, C2):** *"a relatively small number of modifications to current training is sufficient"* is rejected if no comparatively small training-recipe change suffices under adversarial deployment conditions; **note the speaker's own C5 concedes the real world may fail it.**
- **[F-YI-4] (transformer sufficiency, C8):** *"zero to {two} innovations beyond the level of transformers"* is rejected if an ASI-class system is shown to require a **non-transformer** architecture (or if it requires >2 innovations).
- **[F-YI-5] (proof automation, C14):** *"the 5 % of alignment researchers … sped up by a factor of three … do not collectively have the power to solve super alignment in time"* is rejected if a mechanical-proof-automation intervention is shown to move a superalignment bottleneck materially.
- **[F-YI-6] (usage ban):** **No canon document may cite this episode for (a) any quote attributed to Yudkowsky *or* Irving outside the bounded set in §1.2** — the artifact has no speaker labels; **(b) a "pause"/moratorium framing** — not the subject on tape; **(c) a resolution of the coinflip crux** — it was left open by both parties; or **(d) a first-party dated superintelligence forecast** — none is given.

---

## 6. Verdict (opinionated)

**[C] Strongest point:** **the main fight (C11) is a real, load-bearing crux and both parties push it to the floor.** The *biased-vs-noisy verifier* distinction, the *coinflip* test, and the *perpetuum-machine / heat-bath* framing together give canon its **cleanest statement of why external-verification alignment is hard** — sharper than the Soares interview, because here it is **worked against a specific protocol** (interactive proofs / suggesters-vs-verifiers) by someone who both defends and concedes. That this crux maps onto the house's own "external verification cannot substitute for the record" intuition (R2) — independently, and without a word of house vocabulary — is the most useful convergence in the hour. Runner-up: the **self-intro gag** and the *"resolve all their differences and fail"* framing are an unusually honest packaging of a debate that knows it will not resolve.

**[C] Weakest joint:** **the debate's advertised product — settling the disagreements — is failed on its own terms, and the participants say so.** The centerpiece crux did not resolve: by Yudkowsky's own first-party account (Basis B), Irving's answer was *"a good question and he might need to get back to me on that,"* and on tape the concession is *"you clearly have to model the the bias. I agree with that"* followed by *"we don't have the protocol currently"* [1:05:40, 1:06:47] — **an admission that no bias model exists**, with no path offered. Runner-up: **`P(good future) ≈ 1/2` [4:23] and zero-to-two innovations [11:13] are asserted with no model, no base rate, no resolution criterion.** Third, and structurally the most important for the house: **the interior of the agent — record, continuity, substrate — is never raised** (R1/R7: 0 spoken hits). Across 87 minutes on alignment, the sharpest disagreement in the field is conducted entirely as a question about **verifiers**, and the house's lever has **no interlocutor**.

**[C] Net:** a **high-value, first-party-primary artifact** (the first Yudkowsky–Irving debate in canon; both principals named AI-safety figures) with an **unusually severe attribution problem**: an auto-captioned two-person debate with **no diarisation** means *most of the hour cannot be safely split between the two speakers*. Use it for (a) *the shape of the alignment-difficulty disagreement* as a whole, (b) *the biased-verifier / coinflip crux* (attribution anchored via Yudkowsky's own essay), and (c) the **worked example of attribution refusal** itself. Do **not** cite it for a specific quote attributed to a specific speaker outside §1.2; do **not** treat it as evidence for or against any EILT claim directly (R1/R2 `[CRITICAL DIVERGENCE]`).

---

## 7. Pre-file gate report (run over the finished draft, mechanically)

- **Register-tag gate — PASSED.** Six-tag set `[EST]/[HYP]/[A]/[C]/[POETIC]/[RIFF]` declared in frontmatter and applied claim-by-claim; `[POETIC]` declared-UNUSED (no pure-metaphor register row this drop), `[RIFF]` used for the self-intro gag and break-banter. `[EST]` used **only** for capture receipts, the self-intros, on-tape third-person anchors, and externally-confirmed facts (ILIAD event, Open-Phil report existence). **No [EST] tag on any forecast** however forcefully stated.
- **Dedupe gate — PASSED.** id 0 hits; 4-gram max containment 2.04 % < re-cut band; ran pre-pull **and** pre-write.
- **Quote gate — see §7.1 (counts below).**
- **Attribution gate — PASSED by refusal.** Speaker labels absent from the artifact; a bounded set (§1.2) attributed with named bases A–D; **all else marked `[attr-U]`.** No quote assigned by fame.
- **`canon_drop_lint.py` — CLEAN (exit 0); YAML parses.**

### 7.1 Quote gate (programmatic, vs the saved transcript) — PASSED
**125 asserted transcript-quote components** (split on ellipsis; bracketed `[ASR:…]`/timestamp spans removed first; whitespace-normalised) tested as substrings of the saved flat transcript: **125 pass, 0 fail.** Six further quoted strings are **non-transcript by construction** and are labelled inline (the video **title**; the description's *"try to resolve all their differences in one hour and fail"*; Yudkowsky's essay quotation *"Yudkowsky and Irving try and fail to settle all of their disagreements in one hour."*; the essay's *"formerly Google Brain, OpenAI, Deepmind, now heading the new Resolution lab"*; the external report title *"Forecasting TAI with biological anchors"*; and the brace-marked normalisation *"zero to {two} innovations beyond the level of transformers"*). **Defects caught and fixed during the gate: 9** — the ASR-literal mismatches (`2080` for "20/80"; `bas` for "basin"; the doubled "the" in *"model the the bias"*; `super alignment` written as "superalignment"; the dropped "like like" in *"have like like professor"*; the dropped "uh" in *"because uh it's self-corrective"*), plus three quotes that had been silently trimmed mid-span (the *"saving of the world"* span, the *"judges, the verifiers"* span, and *"pushing {uh} the field of AI"*). None shipped.

**Citable for:** the transcript itself; the two speakers' self-introductions and roles as introduced (Yudkowsky; Irving, chief scientist at Resolution); the ILIAD III: AENEID event and the stated format; and the bounded attributed set in §1.2.
**NOT citable for:** any quote attributed to a named speaker outside §1.2; the coinflip crux as *resolved* (it was open); any specific superintelligence date; or any EILT derivation (R1/R2 `[CRITICAL DIVERGENCE]`).

---
*Filed by Dion (subagent pass), 2026-11-03. Local only — no GitHub push, no NotebookLM ingest, no Drive/rclone mirror, no TTS, no outbound message. Only `CANON_INDEX.md` appended (one entry); index backed up to `CANON_INDEX.md.bak-20261103-yudkowsky-irving`. One transcript pair + raw JSON written; one drop filed; no pre-existing Canon artifact modified.*
