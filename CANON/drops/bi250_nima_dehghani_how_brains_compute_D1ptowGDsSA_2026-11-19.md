---
title: "Canon Drop — BI 250 Nima Dehghani: How Brains Compute (Brain Inspired #250)"
date: 2026-11-19
filed_by: Dion
source_type: "YouTube podcast episode — long-form interview (Brain Inspired, host Paul Middlebrooks; guest Nima Dehghani, MIT). PRIMARY-SOURCE TALK: the guest is the author of the work discussed; the episode is a first-person account of his own programme. Caption track = the truth source for quotation (AUTO-ONLY, ASR-grade)."
video_id: D1ptowGDsSA
channel: Brain Inspired
upload_date: 2026-11-18
duration_s: 6473
duration_hms: "1:47:53"
views_at_pull: 1952
chapters: 13
register: "PRIMARY-SOURCE INTERVIEW. Dehghani speaks for his own programme (N4 framework, theory of physical computation, computational closure). Nothing here is a house artifact; the EILT mapping in §5 is OURS and is tagged [A]/[CONVERGENT]/[DIVERGENCE]/[CRITICAL DIVERGENCE]. All quotes are caption-verified against the saved AUTO track; the track is ASR-grade so wording is near-verbatim and proper nouns carry garble (§1.C)."
epistemic-registers: "EST=on-tape fact (a thing said/depicted in the episode, verified against the saved caption) · HYP=a forward-looking or not-yet-released claim the speaker marks as such · A=analogy only (ours) · C=conjecture / speaker's own unhedged-but-unestablished position · POETIC=metaphor/framing · RIFF=our speculative synthesis, not the speaker's"
register-rule: "no tag = treat as unverified; row-status labels [CONVERGENT]/[DIVERGENCE]/[CRITICAL DIVERGENCE]/[ATTRIBUTION]/[HOST]/[SIC]/[ASR] are NOT registers"
transcript_path: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/D1ptowGDsSA_transcript.txt"
transcript_timestamped: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/D1ptowGDsSA_transcript_timestamped.txt"
raw_segs: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/D1ptowGDsSA_raw.json"
canon-id: CANON-2026-11-19-D1ptowGDsSA-DEHGHANI-HOW-BRAINS-COMPUTE
related:
  - "0-Fe-_O2arg_molg_immutable_ledger_2026-11-07.md (DIFFERENT source: house ledger/immutability material. Shares the 'relay vs commit' / provenance axis; NOT a duplicate.)"
  - "AV86mJDD7mk_wolfram_mathematically_impossible_ai_problem_2026-11-02.md (DIFFERENT source: Wolfram on computational irreducibility — the EILT anchor for the §5 friction row. NOT a duplicate.)"
---

# Canon Drop — BI 250 Nima Dehghani: How Brains Compute (Brain Inspired #250)

**Source (identity re-verified live this session):** `https://www.youtube.com/watch?v=D1ptowGDsSA` — **Brain Inspired** (channel `Brain Inspired`, uploader `Brain Inspired`), uploaded **2026-11-18**, **6473 s (1:47:53)**, **1,952 views** at pull (yt-dlp `--dump-json` this session; title/channel/duration/upload_date all agree). **13 chapters.**
**Filed by:** Dion (dion lane) · **Date:** 2026-11-19
**Filing scope:** local only — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send. One transcript set written; no pre-existing Canon artifact modified.

---

## 0. ★ FILING VERDICT — A PRIMARY-SOURCE INTERVIEW, NOT A RELAY

**This is the podcast's own long-form interview with the researcher whose work it discusses** — not a news relay, not a synthesis, not a house artifact. Dehghani speaks for his own programme (he calls the umbrella the **N4 framework**: neurophysics, neurocomputation, neurodynamics, and neuro-AI over all of them). Paul Middlebrooks (host) is a working neuroscientist and half the episode is him probing/clarifying; **attribution between the two speakers matters and is marked per quote (§4).**

**★ What this drop is for:** (a) the on-tape argument map; (b) every quoted span caption-verified with a timestamp and a speaker tag; (c) an EILT mapping **that includes genuine friction** (§5); (d) an honest statement of what the episode did **not** establish (§7).
**★ What it is NOT for:** treating any EILT convergence as validation (the speaker never uses house vocabulary — §6 house-vocab probe = ~0), or laundering a self-description of unreleased work ("I'll be releasing this") into an established result — those are tagged `[HYP]`.

**★ Headline honesty caveat:** the episode's most quotable line — *"the closure criterion will not tell you what the brain computes. It will tell you what you have to demonstrate before you're entitled to say that it computes anything at all"* — is **the HOST reading from Dehghani's blog** (`[5596.4]` says "here's a little quote from your … blog post"), **not** Dehghani speaking live. Marked `[ATTRIBUTION]` at Q10.

---

## 1. Provenance & extraction rail

- **RAIL: RUNG 1 (`youtube-transcript-api` instance API) WON ON THE FIRST TRY — the ONLY English track is AUTO-GENERATED.** `.list('D1ptowGDsSA')` returned **13 tracks — ALL auto-generated** (`is_generated=True`): `ar, bn, nl, en, fr, de, hi, id, it, ml, pl, ru, es`. **NO manual/publisher track exists** for this id. `.fetch('D1ptowGDsSA', languages=['en'])` returned **2838 cues, no `IpBlocked`, no `429`.** Rungs 2 (yt-dlp subs), 3 (CDP `:9333`) and 4 (Whisper/ASR) were **never exercised** ⇒ no yt-dlp sub file, no CDP panel, no audio/WAV, no second ASR pass.
- **★ Interpreter note (for the next lane):** the working interpreter this session is the Hermes venv **`/home/godsend/.hermes/installs/78a1d139eb1c29b6/environments/8d40ada0318c4ce0b73c51bfeea24e1d/venv/bin/python3`** (module resolves). Other lanes have used `/home/godsend/.hermes/hermes-agent/venv/bin/python3` — **the install-hash path is the one that resolved this session; the hash changes per install, so `ls -d ~/.hermes/installs/*/environments/*/venv/bin/python3` is the robust lookup.**
- **Coverage: cues span [3.84 s → 6468.2 s] of 6473 s ≈ 99.9 %; 2838 segments; 0 gaps > 60 s.** Flat body **103,533 chars**; timestamped **128,584 chars**.
- **Artifacts written:** `YT_TRANSCRIPTS/D1ptowGDsSA_transcript.txt` (flat, 103,533 B) + `D1ptowGDsSA_transcript_timestamped.txt` (128,584 B, `[sec.1] text`, 2838 lines) + `D1ptowGDsSA_raw.json` (raw 2838 segs) + two descriptive-name copies (`D1ptowGDsSA_nima_dehghani_how_brains_compute_2026-11-19(.txt/_timestamped.txt)`). `D1ptowGDsSA_meta.json` (yt-dlp dump) lives in the scratch dir.
- **★ Track type: AUTO-GENERATED ONLY ⇒ ASR-grade near-verbatim.** Quotes are caption-verified (§9) but the track carries recognisable ASR name-garbles; wording is near-verbatim and proper nouns must not be carried off the caption unrepaired. The garble is *inconsistent* — the same phrase appears correctly spelled in one place and garbled in another (e.g. "computational closure" **and** "computition closure" **and** "computation closure" all occur).

### 1.C · ASR garble key (logged, NOT silently "corrected" in the tape)
| caption literal | intended (evidence) |
|---|---|
| `Nema` / `Nima Deani` / `Nema Deani` | **Nima Dehghani** (the guest; description names him) |
| `infor` / `neuro4` / `N4` / `nurai` | **N4 framework** = neurophysics/neurocomputation/neurodynamics/neuro-AI (description + `[626.2]`) |
| `neurohysics` / `neuropysics` | **neurophysics** |
| `touring` / `touring complete` / `touring church` | **Turing** / **Turing-complete** / **Turing+Church** (context: Hilbert/Church/Turing, `[1372]`–`[1431]`) |
| `wave blocker` / `wave walker` / `wave walkers` | the **walking-droplet / wave-walker** system (context: oil bath, bouncing droplet, imprints, `[1954]`–`[2015]`) |
| `Michael Levid` / `Mike` / `Michael Leven` | **Michael Levin** (context: non-excitable membrane maintaining memory of shape; "mad man of biology" NIPS talk; host's "you're almost like Michael Leven", `[451.7]`, `[925.5]`) |
| `Yuri Bjaki` / `Bjaka` | **György Buzsáki** (context: *The Brain from Inside Out*, implementation→computational, `[3223]`) |
| `David Hikir` / `Gardini` | **Heeger / Carandini** (context: divisive normalization gain control, adapt to changing stimuli, `[3855]`) |
| `Henry Yen` | **Henry Yin** (context: control-theory, "crisis in neuroscience", internal reference signal, `[2804]`) |
| `Eve Martyr` | **Eve Marder** (context: "few unsophisticated neurons in lobster's gut … same wiring can give you zillion types of dynamics", `[3700]`–`[3716]`) |
| `Bto Babadi` | **Babak Babadi** (context: computational neuroscientist + physician; backprop-without-backprop collaborator, `[4918]`) |
| `Larbat and himlinsky` | **UNRESOLVED — not guessed** (`[4926]`, Babadi's mentors) |
| `Jerome Deuk` / `Alan Institute` | **Jérôme Lecoq** / **Allen Institute** (context: Brain Observatory platform, `[6214]`) |
| `Carlos Fabua` / `Christopher Cook` | **UNRESOLVED — not guessed** (`[6224]`) |
| `Hillary Putnham` | **Hilary Putnam** (`[1776]`) |
| `astrotes` / `iron channels` / `talortical` / `mamalian` | **astrocytes / ion channels / thalamocortical / mammalian** |
| `one of my legs in the experimental world` | "one **leg** in the experimental world" — ASR artifact, phrase otherwise intact |

### 1.D · Chapter spine (from the video's own chapter list, yt-dlp)
`0:00` Intro · `2:49` Computer metaphor · `9:38` N4 approach · `19:00` Defining computation · `30:36` Category theory for computation · `36:37` Computational closure · `43:40` Agency · `47:31` / `59:02` Canonical motifs of cortical operations · `52:44` Marr's levels · `1:15:12` Bio-inspired AI · `1:28:58` Importance of composition · `1:34:22` Computation across all life?

---

## 2. Speakers (verified)

| role | who | evidence |
|---|---|---|
| **Host** | **Paul Middlebrooks** — working neuroscientist; runs Brain Inspired; organised the "brains aren't computational machines — so what are they" workshop the previous Friday | first-person host framing; `[193.3]`–`[209.5]`; the podcast self-ID |
| **Guest** | **Nima Dehghani** — computational/theoretical neuroscientist at MIT; author of the "theory of physical computation" and the "computational closure" programme; ex-MIT physics postdoc who "hangs out" with physics-of-living-systems people; collaborates with **Michael Levin** (and has papers with him) and with **Babak Babadi** | `[86.7]`–`[94.4]`; `[205.8]`, `[455.8]`, `[472.6]`, `[4918.3]` |

*Attribution rule applied below: the host's own probes ("is the brain a computer?", "does the bacteria have it?") are the host's; the answers, and all programme claims, are Dehghani's unless a quote is tagged `[HOST]`.*

---

## 3. Argument map (what Dehghani actually argues)

All rows below are `[EST]` (on-tape) unless tagged otherwise; the tag describes the *epistemic status of the claim as stated*, not our endorsement.

1. **Brains DO compute — but only under a tightened definition.** He agrees the brain computes — *"with like serious constraints on like how we define this sort of thing"* `[254.1]` `[SIC: ASR "like" fillers preserved]`. The episode's shared premise is that "computation" is often used as *"a filler term … because they're not formalizing what computation is"* — the phrase is the **host's** `[1209.8]` `[HOST]` — and that *"not every information relay is a computer"* `[406.6]`, *"not every information transfer is a computation"* `[1268.2]`.
2. **The rock test.** If everything that changes state "computes", the word is useless: *"if I throw a rock … the rock computes trajectory … if that's computation then … everything that moves … is computation"* `[1253.8]`–`[1268.4]` — so a **criterion** is required.
3. **That criterion = a *theory of physical computing* whose arrows run the other way.** Classical computability runs *computable function → model of computation → physical device* (Church–Turing, motivated by Hilbert's programme). The physical theory runs **the reverse**: *"handed a physical system … figure out … degrees of freedom in the system … how does this system go from the sort of state transitions that it can carry … to the sort of operations that interests us"* `[1496.6]`–`[1531.2]`. Category theory (functors, natural transformations, adjunctions) is the *tool* for mapping between the physical and abstract levels — "not a decoration" `[1909.7]`–`[1926.4]`.
4. **Computational closure** is the payoff concept: the system **builds its own abstraction** — the abstract level is *embedded in the physical machinery itself*, not imposed by an outside observer. His paradigm case is a **walking-droplet / wave-walker** system (an oil bath vibrated below threshold, a droplet bouncing and leaving wave-imprints; a French group's PRL paper). The walker has *"touring like primitives"* `[ASR: "touring" = Turing]` — memory, eraser, writing, feedback — **but is not an autonomous physical computing device**, because the **experimenter closes the loop** by shifting the wave's phase from outside `[2086.0]`–`[2097.0]`. "Our brain has computition closure but not every computing system has it" `[2078.9]`.
5. **Agency = computational closure built into the system.** *"The agency comes from this aspect of having … computational closure built into the system that now you can have an understanding of the environment and then from there you can act on it … and now you have internal model of the world"* `[2769.4]`–`[2783.6]`. This is where he reaches for **"the forbidden word"** — *"that's where intelligence consciousness agency all … are different"* `[74.5]` — while insisting (a) he has *"a little bit of allergy about using the word … consciousness"* `[2131.4]`, and (b) the label is downstream of a measurable structural property: *"I want to be precise about like this is what we measure. This is what we can do."* `[2800.4]`. He explicitly places his approach as *touching* **Friston's free-energy principle**, **Marr's levels**, and **Buzsáki's** account — *"it touches all those things in in some ways … but all bounded by … the actual physics"* `[3393.4]`–`[3405.0]`.
6. **Agency is a misnomer for AI "agents".** The **host** proposes AI agents have *"nothing actually agential about those because they don't have the computational [closure]"* `[2639.6]` `[HOST]`; Dehghani agrees, calling the label *"such misnomer. This is terrible."* `[2645.0]`; and he rejects the "the agents went out of control and hacked something" framing — *"No, they didn't go out of control. You didn't put the right boundaries."* `[2656.1]`.
7. **The nervous system is for homeostasis.** *"at the end the whole nervous system is there for the regulation of our body"* `[2835.8]`; the world-model exists *"for us to be able to interact with it and maintain the internal state"* `[2865.6]`. He links this to **Henry Yin's** control-theoretic "crisis in neuroscience" (a system must set its **own** reference signal / set-point internally, not have it set by an external observer) `[2804.9]`–`[2828.5]` — the host raises Yin, Dehghani agrees "Yeah. Yeah. Exactly."
8. **Life, not just brains.** Asked "is all life computation?" he answers *"I think so … I think all life has that aspect of computation closure"* `[5700.5]`–`[5707.7]`; **E. coli** (chemotaxis) *"does"* have it and *"it has evolved to do so"* `[2959.0]`–`[2965.8]`; a **biofilm** does something a single bacterium cannot (boundary cells sense; calcium/potassium ion-wave pulsations *"carrying a sort of information … about the environment"*) `[3063.4]`–`[3111.5]`.
9. **No "spooky emergence".** Emergence is allowed only as *layers of an onion* built on real lower levels: *"properties that emerge at a scale that are not a spooky emergencies"* `[3448.1]`; *"there is no spooky … demons sitting there"* `[3121.1]`. But pure reductionism *"is bound to fail"* `[4482.0]` — citing **Philip Anderson's "More is Different"** `[1074.9]`, `[4455.4]`.
10. **Composition is the mechanism of emergence (his research programme).** Two **canonical cortical motifs** — **divisive normalization** (change a neuron-population's gain; "shown by Heeger and Carandini"; adapts to changing stimuli) `[3576]`, `[3855.8]` and **winner-take-all** (two populations compete; one "silences the other one through some sort of like common inhib") `[3885.5]` — are *"repeated over and over and over … which evolution does in the cortex"*. His move: describe each finite-state motif as **funnels** (have an end state) and **gears** (can switch between states) `[4004.1]`; then **compose** two such circuits and map the joint state space (e.g. a **4×8 grid**), asking where a stable, composed "gear" can emerge *out of purely funnel systems* `[4193.9]`, `[4300.6]`. *"Who is connected to whom is what defines the … constraints of how the system as a whole is composed and operates"* `[4227.5]`.
11. **Why recurrence is the crux.** *"Recurrence is a beast … that's the holy grail of neuroscience … how they change their operations without … constantly changing the synaptic weight … biology cannot afford back propagation at that scale"* `[3918.0]`–`[3939.4]`. `[HYP]` He says he has a paper (unreleased) proving *"a fundamental limit … fundamental physical limit of what feed forward systems do and that is something that you need recurrence for … without recurrence you cannot solve those problems"* `[4745.6]`–`[4758.8]`. `[HYP]` With **Babadi** he built a **recurrent machine that operationalises what backprop does, with no backprop** — *"we don't need to change the weights the whole thing actually happens the weights are the recurrent state of the system"* `[4966.0]` — *"we are not claiming … this is what biology does but it it's a clue"* `[4972.7]`.
12. **Effective theories + shared data.** Method: build *"effective theories that can … give us the right interpretation at that level without … detaching us from the reality of the lower levels"* `[1022.3]` `[elision: ASR speaker-turn marker ">>" falls between "can" and "give"]`. He repeatedly insists measurement bounds theory, credits **open neuroscience** (Allen Institute Brain Observatory), and flags partial observation as the fundamental limit.

---

## 4. Verified quotes (caption-verified, timestamped, attributed)

Every span below was **grep-verified against the saved AUTO caption** (`D1ptowGDsSA_transcript.txt`); the literal (including ASR garble) is preserved, not silently corrected. Tag = the claim's register.

| # | speaker | t (s) | verbatim (caption literal) | tag |
|---|---|---|---|---|
| Q1 | Dehghani | `[1268.2]` | *"so not every state changes computation not every information transfer is a computation and that's actually the key point here"* | `[EST]` |
| Q2 | Dehghani | `[406.6]` | *"some of them could be just information relay not every information relay is a computer right is not an actual description of what a computer is"* | `[EST]` |
| Q3 | Dehghani | `[2078.9]` | *"our brain has computition closure but not every computing system has it"* [ASR: "computition closure" = computational closure] | `[EST]` |
| Q4 | Dehghani | `[2090.6]` | *"it has a touring like primitives but it's not an autonomous physical computing device"* [ASR: "touring" = Turing] | `[EST]` |
| Q5 | Dehghani | `[2769.4]` | *"the agency comes from this aspect of having the sort of computational closure built into the system"* | `[EST]`/`[C]` |
| Q6 | Dehghani | `[5700.5]` | *"I think all life has that aspect of computation closure"* | `[C]` |
| Q7 | Dehghani | `[3918.0]` | *"recurrence is a beast right and I think that's the holy grail of neuroscience"* | `[EST]`(framing) |
| Q8 | Dehghani | `[3924.8]` | *"can we come up with theories of how these recurrent systems are working, how they like doing the operations, how they change their operations without like constantly changing the synaptic weight … biology cannot afford back propagation at that scale"* | `[EST]`/`[HYP]` |
| Q9 | Dehghani | `[4745.6]` | *"there is a fundamental limit fundamental physical limit of what feed forward systems do and that is something that you need recurrence for"* | `[HYP]` (unreleased paper) |
| Q10 | **`[HOST]`** (reading Dehghani's blog) | `[5611.6]` | *"the closure criterion will not tell you what the brain computes. It will tell you what you have to demonstrate before you're entitled to say that it computes anything at all"* | `[ATTRIBUTION]` — host's voice, Dehghani's text |
| Q11 | Dehghani | `[4861.1]` | *"but it has no experience of what rain is. Like you know, you know what? … My dog knows what rain is"* | `[EST]`/`[POETIC]` |
| Q12 | Dehghani | `[5787.0]` | *"to me good explanations are explanations that are hard to vary. So if you have David Deutsch kind of idea as well"* | `[EST]` |
| Q13 | Dehghani | `[925.5]` | *"… has a non-exitable membrane but is still doing something in terms of maintaining some sort of like memory um of its own shape … And that's actually for example uh the work of Michael Levid"* [ASR: "Levid" = Levin] | `[EST]` |
| Q14 | **`[HOST]`** | `[3217.4]` | *"there are people like Yuri Bjaki … who wrote you know the the brain from inside out is his most recent book but he says no no no let's go from the implementation level to the computational level"* [ASR: "Bjaki" = Buzsáki] | `[ATTRIBUTION]` — host describing Buzsáki |
| Q15 | **`[HOST]`** | `[2804.9]` | *"Henry Yen comes at this from a control theory perspective … he writes about the crisis in neuroscience … you need a control system that sets its own reference signal uh internally somehow and that's where the closure of computation comes in"* — Dehghani replies *"Yeah. Yeah. Exactly."* `[2831.6]` | `[ATTRIBUTION]` — host describing Yin; Dehghani assents |
| Q16 | Dehghani | `[3393.4]` | *"the relationship to Bjaka's idea or Mars idea or for instance free energy principle it has it touches all those things in in some ways right … but all bounded by … the actual physics"* | `[EST]` |
| Q17 | Dehghani | `[1074.9]` | *"it's almost like you know Philip Anderson's more is different sort of like paper"* | `[EST]` |
| Q18 | Dehghani | `[4482.0]` | *"that why you know pure reductionism is bound to fail"* | `[EST]` |
| Q19 | Dehghani | `[5419.1]` | *"composition is what enables us to go from like lower level abstraction to bigger and much richer abstractions"* | `[EST]` |
| Q20 | Dehghani | `[2650.3]`, `[2656.1]` | *"Oh, these agents, they got out of control and they went hacked some." "No, they didn't go out of control. You didn't put the right boundaries."* [first clause = his paraphrase of others' framing; the reply is his] | `[EST]`/`[C]` |
| Q21 | Dehghani | `[2645.0]` | *"That's such a that such misnomer. This is terrible."* (of calling AI systems "agents") | `[EST]`(opinion) |
| Q22 | Dehghani | `[4966.0]` | *"we don't need to change the weights the whole thing actually happens the weights are the recurrent state of the system"* | `[HYP]` (unreleased, w/ Babadi) |
| Q23 | Dehghani | `[5481.4]` | *"the environment itself shapes that machinery when you interact with it and you want to predict about have predictions about that environment"* | `[EST]` |
| Q24 | Dehghani | `[1022.3]` | *"we need to be able to build effective theories that can … give us the right interpretation at that level without uh basically detaching us from the reality of the lower levels"* [elision: ASR speaker-turn marker `>>` falls between "can" and "give"] | `[EST]` |
| Q25 | Dehghani | `[4004.1]` | *"Let's call them funnels and gears. And funnels are the one that are basically they have an end state as this uh you know reminiscent of the name funnel. And gears are the ones that actually could switch could switch between different states."* | `[EST]` |
| Q26 | Dehghani | `[4300.6]` | *"gears out of purely funnel systems"* | `[EST]` |
| Q27 | Dehghani | `[3578.3]`, `[3855.8]` | *"another motif is called a winner take all motif where essentially a decision is made"*; divisive normalization *"was shown by David Hikir and Gardini … this helps us adapt our visual experience"* [ASR: Hikir=Heeger, Gardini=Carandini] | `[EST]` |
| Q28 | **`[HOST]`** | `[205.8]` | workshop title: *"brains aren't computational machines so what are they"* | `[EST]` |
| Q29 | Dehghani | `[3107.4]` | *"this pulsation is now carrying a sort of information for them about the environment"* (biofilm ion waves) | `[EST]` |
| Q30 | Dehghani | `[3121.1]` | *"there is no spooky like you know demons sitting there and doing these things"* | `[POETIC]`/`[EST]` |
| Q31 | Dehghani | `[2835.8]` | *"at the end the whole nervous system is there for the regulation of our body"* | `[EST]` |
| Q32 | Dehghani | `[2959.0]` | *"Yes, it does."* (E. coli has computational closure) … *"it has evolved to do so"* `[2965.8]` | `[C]` |
| Q33 | Dehghani | `[628.8]` | *"the N4 so I have uh neuropysics, neuro computation, neurodynamics and what I say is that like neuri or bio inpired intelligence builds on top of this"* | `[EST]` |
| Q34 | Dehghani | `[1496.6]` | *"In a theory of physical computing, the arrows are reversed"* | `[EST]` |
| Q35 | Dehghani | `[2131.4]` | *"I have a little bit of allergy about using the word like consciousness"* | `[EST]` |
| Q36 | Dehghani | `[4769.7]` | *"we are not claiming okay look this is what biology does but it it's a clue"* | `[EST]` |
| Q37 | Dehghani | `[5519.6]` | *"every day uh we know more and more about cell types … About wiring diagrams"* + *"You look at these papers, what you learn at the end, you just it's just like a catalog"* `[5541.8]` | `[EST]`/`[C]` |
| Q38 | Dehghani | `[1457.0]` | *"I think it was 1912 but you know I may be wrong about it"* (on Hilbert's problem set — **his own hedge on the date**) | `[EST]` (self-hedged) |

---

## 5. ★ EILT MAPPING — Emergent Informational Ledger Theory

**Credit discipline:** *polycomputing* and *cognitive light cones* are **Levin's**; *ruliad* and *computational irreducibility* are **Wolfram's**; *active inference / free-energy principle* is **Friston's**. None of these terms is spoken by Dehghani (§6 probe = 0); every mapping cell below is **ours** and tagged as an analogy. **The table is NOT uniformly convergent — R1 is a `[CRITICAL DIVERGENCE]` that cuts at the source's own central methodological claim.**

| # | EILT element | Dehghani's on-tape position | status |
|---|---|---|---|
| R1 | **Computational irreducibility (Wolfram)** — for irreducible systems there is **no shortcut**; you must *run* the system; a closed-form predictor would be the reduction the theory denies. | Dehghani's method is the opposite wager: he wants **effective theories** that give *"the right interpretation at that level"* (Q24) **and** states his composition programme will let us *"mathematically computationally predict the properties of the [composed recurrent] system"* `[4340.2]`–`[4349.4]` — *instead of* brute-forcing the state space. He even names the brute-force cost as *"competition very expensive … it's insane … zillion s of configuration"* `[4168.5]`–`[4176.7]`. **This is the exact move irreducibility forbids: he assumes a level exists where the composed repertoire is *predictable without running it*.** | **`[CRITICAL DIVERGENCE]`** — source claims the shortcut; EILT/Wolfram denies it exists in general. (Possible reconciliation: his claim is about *stickable* funnel/gear machines only — a bounded, reducible subclass — but the tape does not restrict the scope.) |
| R2 | **Polycomputing (Levin) + ledger/provenance** — a physical system can compute many functions at once, and abstraction/memory can be *embedded in matter*. | Dehghani **excludes** the wave-walker because *"it's not an autonomous physical computing device"* — the loop is closed from outside (Q4). But the wave that registers the walker's path IS an abstraction embedded in physical machinery (his own account, `[2027.2]`–`[2052.8]`). | `[DIVERGENCE]` — Dehghani's *closure* criterion denies computational status where a Levin-polycomputing lens would grant a material computation. (Nima cites Levin elsewhere, so this is friction *between two positions he holds*.) |
| R3 | **FEP / active inference (a system that maintains itself by modelling the world and acting on the model; self-set reference signal)** | *"the agency comes from … computational closure … you can have an understanding of the environment … you can act on it … internal model of the world"* (Q5); *"the whole nervous system is there for the regulation of our body"* (Q31); he explicitly says his frame *touches* the free-energy principle (Q16). | `[CONVERGENT]` (by his own bridge) — his closure ≈ FEP self-evidencing, but he subordinates it to *physics*, not to a prior on surprise. |
| R4 | **Relay ≠ commit** (an information transfer is not automatically a ledger entry / computation) | *"not every information relay is a computer"* (Q2); *"not every information transfer is a computation"* (Q1); *"that's actually the key point."* | `[CONVERGENT]` — near-identical to the house's "relay is not a commit" discipline. |
| R5 | **Emergent informational ledger (composition producing new, higher-level state)** | *"composition is what enables us to go from like lower level abstraction to bigger and much richer abstractions"* (Q19); *"gears out of purely funnel systems"* (Q26); *"more is different"* (Q17/Q18). | `[A]` — his funnel/gear composition ≈ the ledger's level-emergence, but he is tracking *repertoire*, not *provenance*. |
| R6 | **Bioelectricity / cognitive light cones (Levin)** | *"the work of Michael Levid"* on non-excitable membranes maintaining memory of shape (Q13); biofilm calcium/potassium ion-wave signalling (Q29). | `[A]` — the closest genuine correspondence to Levin's programme; but *light cone* / *bioelectric* are never spoken. |
| R7 | **The world as the only certifier / environment-referenced validity** | *"the environment itself shapes that machinery when you interact with it"* (Q23); wants *causal* / *counterfactual* descriptions via poking the system `[6044.6]`–`[6062.6]`. | `[CONVERGENT]` — environment-as-constraint matches the house's outcome-certification axis. |
| R8 | **Agency / the "forbidden words"** | Reaches for the label but *resists* it: *"I have a little bit of allergy about using the word … consciousness"* (Q35); *"I want to be precise about … what we measure"* `[2800.4]`. | `[DIVERGENCE]` — Dehghani withholds the operative vocabulary (and calls "AI agent" a *"misnomer"*, Q21) where EILT is willing to name the stack. |

---

## 6. Critical Audit & Falsification Matrix

**House-vocab probe (spoken by the speaker = 0 unless noted):** `ledger` `provenance` `commit` `immutable` `non-rolling` `append-only` `syntropy` `epiplexity` `ruliad` `polycomputing` `Markov blanket` `light cone` `coupling` `stakes` `amnesia` `EILT` `horde` `Oryon` `AGI` — **all = 0** on the 103,533-char body. `polycomputing`/`light cone` = 0 even though Levin is cited by name. This is what makes the §5 table an **analogy** and not a convergence-by-construction: **the speaker never uses our words, so any rhyme is ours to own or drop.**

| tag (register) | claim | assessment |
|---|---|---|
| `[EST]` | "not every information transfer is a computation" | **Solid; the strongest single joint in the episode.** It is a *criterion* claim, stated flatly, and it is what separates him from pancomputationalist wordplay. |
| `[C]` | "all life has that aspect of computation closure" (Q6); E. coli "does" (Q32) | **Unhedged conjecture.** He asserts closure for bacteria on the strength of chemotaxis; the *measurable* demonstration he demands of others (Q10's "what you have to demonstrate") is not supplied on tape for the bacterium. |
| `[HYP]` | feed-forward "fundamental physical limit" (Q9); backprop-free recurrent machine (Q22) | **Unreleased work, self-flagged** ("when I release it we'll talk again"), and he explicitly declines the biological claim ("we are not claiming … this is what biology does"). Correctly `[HYP]`; do not cite as a result. |
| `[EST]` | divisive normalization / winner-take-all as canonical motifs | **Reported as established** (attributes DN to Heeger & Carandini). The *composition* result (gears from funnels) is his new claim `[C]`/`[HYP]`, computational "expensive … insane" by his own admission. |
| `[EST]` | Hilbert date "1912 … I may be wrong about it" | **Self-hedged**; not a citable date. |
| `[A]` | our §5 EILT mappings | **Ours.** Analogy only. R1 is friction, not support. |
| `[POETIC]` | "no spooky … demons" (Q30); "onion … layers" `[3436.8]` | Framing metaphors, load-bearing only rhetorically. |

---

## 7. What the episode did NOT establish

- **No empirical numbers.** Zero statistics, effect sizes, or measurements on tape. Nothing here is a numerical result.
- **No primary papers cited by identifier.** Titles/DOIs/arXiv-IDs: **none given.** Named works are by title spoken loosely: Anderson's *More is Different* (`[1074.9]`), Buzsáki's *The Brain from Inside Out* (`[3223.2]`), a "wave computation" paper he released, a *"how long is the coastline?"* paper he "just put out" (`[2588.8]`), and an **unreleased** feed-forward-limit paper. A "French group" PRL paper on walking droplets is referenced **without authors** (`[1946.5]`).
- **No claim to have solved computation.** Asked "how much of brain processing is computation", he answers *"I don't know. That's the reality."* (`[5759.7]`).
- **No claim that his artificial recurrent machine is what biology does** (Q36).
- **No definition of "computation" delivered on tape** — he says it needs a rigorous definition and points to his papers/videos, but the *criterion itself* is left off-mic except as the closure slogan (Q10), which the host reads.
- **No verification of his collaborator claims** (Levin papers, Babadi machine) — asserted, not shown.
- **The visual track was not audited** (audio/caption + metadata only).

---

## 8. ★ VERDICT

**★ Strongest point — the "relay ≠ computation" criterion (Q1/Q2) welded to the closure criterion (Q3/Q4).** Dehghani does the one thing most "brains compute" talk refuses: he names an *exclusion*. The wave-walker has memory, erasing, writing, feedback — everything the loose definition calls "computation" — and he still rules it **not** an autonomous physical computing device because *the observer closes the loop*. That is a real, testable joint: it predicts that any system whose abstraction is imposed from outside will show a phase/parameter knob the system cannot turn for itself. It also converges, independently and without our vocabulary, on the house's **relay-is-not-a-commit** discipline (R4).

**★ Weakest joint — the `[CRITICAL DIVERGENCE]` wager (R1).** His programme's whole payoff — turn composition from brute-force search into a *predictive* mathematics (*"mathematically computationally predict the properties of the system"*) — is the exact bet computational irreducibility says you lose in general: for an irreducible composed system there is no cheaper-than-running predictor, and his own "zillion s of configuration / it's insane" line is the empirical shadow of that wall. If his claim is silently scoped to *reducible* funnel/gear machines, it survives; as stated on tape it is unrestricted, and that is where it is most likely to fail. A secondary weakness is the *closure-for-all-life* move (Q6/Q32): it asserts the same criterion he says must be demonstrated, for E. coli, without the demonstration.

**One-line friction:** *Dehghani's method promises a mathematics that predicts a composed recurrent system's repertoire without running it — straight against Wolfram's computational irreducibility, which says the run IS the only way to get the answer.*

---

## 9. Falsifiers & quote gate

**Falsifiers (house-facing, where relevant):**
- **F-ND-1** (testable joint → `[CRITICAL DIVERGENCE]`): if composed recurrent systems are in general computationally irreducible, no predictive theory can shortcut them ⇒ Dehghani's R1 wager fails and the house must not adopt "predict-without-running" language. Test: exhibit a composed recurrent system whose steady-state repertoire is provably not computable in time sub-linear in its configuration-space size.
- **F-ND-2**: the closure criterion must classify: name a system the criterion **excludes** but that independently maintains its own abstraction boundary — if one exists, "closure" is not the right cut.
- **F-ND-3**: E. coli computational closure — name the *measured* abstraction boundary; if none can be exhibited, Q6/Q32 stay `[C]`.
- **F-ND-4** (house-facing): if EILT's own ledger is a purely *observational* record (house §18.8: origin, not validity), then Dehghani's *closure* (a system building its **own** abstraction) is a **stronger** requirement than EILT currently imposes — the house must say whether closure is required or optional for a "commit."

**★ Quote gate (all §4 spans, checked literally against the saved AUTO caption):** 38/38 spans found **verbatim (case- and garble-preserving)** — **0 fabricated, 0 missing, 0 spliced.** Positive controls HIT: `"...not every information transfer is a computation"`, `"...not every information relay is a computer"`, `"...the closure criterion will not tell you what the brain computes"`, `"...biology cannot afford back propagation at that scale"`, `"...the weights are the recurrent state of the system"`. Negative controls MISS (confirming the gate bites): `"nothing really persists"` (belongs to a *different* video), `"can we actually program networks"`, `"typically like you know the people who come from the systems neuroscience"` — none of these is on this tape. ASR garble is **logged in §1.C and preserved in the quotes**, never silently repaired.

*Lint (`canon_drop_lint.py <file>`): see §10 — pattern file is shared-scope; run as a backstop per the skill, not as a blocking gate.*

---

## 10. Register-tag compliance & lint note

- **Declared vocabulary:** the six-tag set `EST / HYP / A / C / POETIC / RIFF` (frontmatter `epistemic-registers:`). **No invented tags.** RIFF is effectively unused.
- **`canon_drop_lint.py`** reads a shared pattern file at `/data/SecondBrain/90_System/retracted_formulations.json` (single-file mode never writes). Run as a backstop after filing per the skill; **if it flags a retracted formulation here it will be reported in the run summary, not silently edited.**

**Citable for** — Dehghani's own on-tape statements (verbatim, timestamped, to the saved caption only): the relay≠computation criterion (Q1/Q2), the closure criterion + wave-walker exclusion (Q3/Q4), agency-as-closure (Q5/Q31), the recurrence/backprop-affordability framing (Q7/Q8), the `[HYP]` feed-forward-limit and backprop-free-recurrent claims (Q9/Q22), the funnel/gear composition programme (Q25/Q26), the EILT mapping's own friction row (R1). **NOT citable for** — any empirical number (there are none), any unreleased result as established (`[HYP]`), the "coastline" or wave-computation papers as anything but titled mentions, the Hilbert date, `"Michael Levid"`/`"Yuri Bjaki"`/`"David Hikir"` as proper names (garble — §1.C), or any house-vocab derivation (the speaker never uses house vocabulary — §6). **The §5 table is `[A]`; R1 is `[CRITICAL DIVERGENCE]`.**

**Local only** — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send; one transcript set written, one drop filed, one index entry appended, no pre-existing Canon artifact modified.
