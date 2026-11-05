---
drop-id: CANON-DROP-2026-10-31-vFOnDsy58NU
source-type: "PRIMARY — a recorded two-person interview (host + guest, `>>` turn markers); guest is an author of the studies he cites and speaks in his own voice. NOT a relay, NOT a panel, NOT a re-cut."
title: "Harvard AI Professor: The People Most at Risk From AI Aren't Who You Think"
channel: "Silicon Valley Girl"
channel-id: "UCiq1FIgtEK7LRAOB1JXTPig"
host: "Silicon Valley Girl (Marina Mogilko) — first-name/surname never spoken on tape; channel identity from the uploader + oembed author_name"
guest: "Karim Lakhani — Harvard Business School professor (name SPOKEN [0:00:03] and [0:51:06])"
yt-id: vFOnDsy58NU
yt-url: "https://www.youtube.com/watch?v=vFOnDsy58NU"
upload-date: 2026-10-30
duration: "3095 s (51:35)"
views-at-pull: 58724
likes-at-pull: 715
comments-at-pull: 77
availability: public
transcript-rail: "RUNG 1 — youtube-transcript-api on system python3, FIRST TRY; a SINGLE auto-generated 'en' track (no manual/human caption); 1564 raw segments, 0.0 s → 3096.8 s of a 3095 s runtime (≈100 % span)"
transcript: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/vFOnDsy58NU_SiliconValleyGirl_HarvardAIProfessorMostAtRisk_2026-10-31.txt (56,032 chars / 10,548 words)"
transcript_timestamped: "/data/SecondBrain/Canon/YT_TRANSCRIPTS/vFOnDsy58NU_SiliconValleyGirl_HarvardAIProfessorMostAtRisk_2026-10-31_timestamped.txt (73,236 chars / 1564 cues)"
registers: "[EST] established/checkable · [HYP] hypothesis/relayed-unverified/opinion · [A] analogy/cross-domain mapping · [C] conjecture · [POETIC] metaphor · [RIFF] improvisational register"
row-status-labels: "[CRITICAL DIVERGENCE] / [DIVERGENCE] / [CONVERGENT-POSTURE] / [ATTACK SURFACE] / [ABSENT] / [ASR] / [RE-TREAD] / [UNVERIFIED] / [AD] are ROW LABELS, NEVER registers"
note: "claim IDs are written in parentheses (C1, M1 …) never in square brackets, so a mechanical tag gate cannot mistake them for registers"
source_status: VERIFIED (transcript read in full this session)
filed: 2026-10-31
filed-by: Dion (ClawHorde canon-intake pipeline, delegated subagent)
status: "Working draft (pre-adversarial review)"
tags: [ai-labor, expertise, mid-career, middle-management, upskilling, cyborgs-centaurs-self-automators, bcg, procter-gamble, jagged-frontier, k-curve, taste, judgement, learning-to-learn, lakhani, hbs, eilt, ledger, provenance-not-truth, friction-rule, re-tread]
---

# Canon Drop — Silicon Valley Girl (Marina Mogilko) × **Karim Lakhani**, *"Harvard AI Professor: The People Most at Risk From AI Aren't Who You Think"* (`vFOnDsy58NU`)

**Date:** 2026-10-31 · **Filed by:** Dion (canon-intake pipeline, delegated subagent)
**Source (VERIFIED, live metadata via `yt-dlp --print` this session):** `vFOnDsy58NU|Harvard AI Professor: The People Most at Risk From AI Aren't Who You Think|Silicon Valley Girl|UCiq1FIgtEK7LRAOB1JXTPig|3095|20261030|58724|715|77|public` · https://www.youtube.com/watch?v=vFOnDsy58NU
**Channel / uploader:** **Silicon Valley Girl** (`UCiq1FIgtEK7LRAOB1JXTPig`; oembed `author_name` = *"Silicon Valley Girl"*, channel `@SiliconValleyGirl`) · **Duration:** 3095 s (51:35) · **Uploaded:** 2026-10-30 · **Views:** 58,724 · **Likes:** 715 · **Comments:** 77 · **Availability:** public.
**Speaker class:** **PRIMARY.** A two-person recorded conversation (transcript uses `>>` turn markers). The **guest is named on tape** — *"This is Karim Lakhani, a Harvard Business School professor"* [0:00:03], closed *"Karim, thank you so much."* [0:51:06] — and he is a **co-author of the studies he cites**, so his BCG/P&G/jagged-frontier material is first-person researcher testimony, not relay. The **host's surname is never spoken** (see §2 declared exception).

> **Zero-fabrication note (CA46 / CA75).** Every quotation below was read from **this video's own saved caption artifact in this session** and re-confirmed literally present (whitespace-normalised, caption line-wraps rejoined) before filing (§6 quote gate). The **title** and its *"most at risk … aren't who you think"* framing are treated as **claims to check against the transcript**, not as findings. Every named study, number and name is quoted in **the transcript's own words**; the numbers are separately checked against the **published primaries** (§2) — and where the title's empirical claim outruns the speaker's own hedge, that gap is named (§1, §2, §4).

**Local only — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send.**

---

## §0 · Rail report, coverage, title audit, dedupe

**★ RUNG 1 (`youtube-transcript-api`, system python3) WON ON THE FIRST FETCH — and it carried ONLY an auto-generated track (no manual caption exists).** `.list('vFOnDsy58NU')` returned **21 auto-generated tracks** (ar, bn, nl, **en**, fr, de, iw, hi, id, it, ja, ko, ml, pl, pt, pa, ru, es, ta, te, uk), **all `is_generated=True`**. `.fetch('vFOnDsy58NU', languages=['en'])` returned **1564 segments, NO `IpBlocked`, NO 429.**

| Rung | Method | Result |
| :--- | :--- | :--- |
| **1** | `youtube-transcript-api` `.list()` / `.fetch()` | **WINNER.** one auto `en` track; **1564 raw segments**; first cue `0:00` (0.0 s), last cue start **3093.325 s** (ends 3096.805 s) of a **3095 s** runtime ⇒ **≈100.06 % nominal span**. No `IpBlocked`, no 429. |
| **2** | `yt-dlp --write-auto-subs` | **NOT RUN** — rung 1 complete (host is a known intermittent 429 producer for subtitle pulls). |
| **3** | headless-Chromium CDP transcript panel (:9333) | **NOT RUN** — unnecessary. CDP panel never opened ⇒ the known cross-contamination trap does not apply. |
| **4** | `yt-dlp` audio + local faster-whisper `small.en` | **NOT RUN** — unnecessary; no WAV residue. |

**Coverage:** 1564 raw auto segments, first cue `0:00` (0.0 s), last cue ends **3096.8 s** of a **3095 s** runtime ⇒ **≈100 % span**; **0 inter-segment gaps > 60 s**. Body ≈ **10,548 words / 56,032 chars**. No uncaptioned head or tail beyond the caption lead-in. **Full, not partial.**

**Transcript artifacts written this session (with the id in the filename, per the brief):**
- `YT_TRANSCRIPTS/vFOnDsy58NU_SiliconValleyGirl_HarvardAIProfessorMostAtRisk_2026-10-31.txt` — **56,032 B** (plain, whitespace-joined).
- `YT_TRANSCRIPTS/vFOnDsy58NU_SiliconValleyGirl_HarvardAIProfessorMostAtRisk_2026-10-31_timestamped.txt` — **73,236 B**, one `[hh:mm:ss]` cue per line, **1564 lines**.
- Raw cue JSON: `YT_TRANSCRIPTS/_tmp_vFOnDsy58NU.json` (scratch pull artifact, retained).

**★ TITLE AUDIT — THE PACKAGING IS A HYPOTHESIS DELIVERED AS A FINDING; the body is *more careful than the title*.** The title asserts an empirical result about **who is most at risk** (*"…Most at Risk … Aren't Who You Think"*). The transcript answers that question — but with an **explicitly unsettled, first-person hedge**:

| Title term | Spoken hits | Read |
| :--- | ---: | :--- |
| **"most at risk"** | 0 (exact) | The phrase is **packaging**. The body says *"people that may be at risk are more in the middle management layers than in the junior layers **from my perspective**"* [44:15] and *"**my belief** is that in fact the middle layer is more at risk than the junior layer"* [44:56]. |
| **"Aren't Who You Think"** | 0 | The candidate the viewer *would* think of — **juniors / entry-level** — is exactly what the speaker **explicitly declines to blame**: *"I don't think junior work is being automated. … I don't think that question is settled to be quite honest."* [44:07]–[44:12]. |
| **"Harvard AI Professor"** | — | **Honest.** *"This is Karim Lakhani, a Harvard Business School professor"* [0:00:03]; confirmed by the published papers' author line (§2). |

**⇒ TITLE CLAIM (who is most at risk) IS REGISTER-TAGGED `[HYP]` IN THIS DROP, NOT `[EST]`.** The speaker names **middle-management (≈35–55-year-olds)** as *his* leading candidate, on **self-reported in-company observation plus a usage-gap metric he says has no performance correlation**; he flags that *"esteemed colleagues … are worried about the junior side"* and that *"the causal density is high."* Per the brief's instruction, this pundit framing is **not upgraded to a verified fact.** (Full inventory §1e; house-side check §2.)

**★ Dedupe (this session, 4-gram, containment of the shorter text in the target; 262 comparable `YT_TRANSCRIPTS/*.txt`):** maximum **1.51 %** vs `1OdoSzfUkec_Amodei_Builders_SuperintelligentAI_2026-10-27.txt` (117 shared grams, generic AI vocabulary), next **1.40 %** (`C8BP8K-ZuL0`), then ≤ 1.34 %. **~33× below the ~50 % re-cut threshold.** `vFOnDsy58NU` = **0 pre-filing hits** anywhere in `Canon/`; the guest name **`lakhani`** = **0 hits** outside a single cross-reference line in `mollick_ai_rewrite_work_wharton_keating_2026-10-20.md`. **⇒ genuinely NEW source; a full drop WAS filed (no clip-of note).**

**★ STEP-0 CLIP-VS-PARENT and PRIOR-DROP check vs `drops/harvard_psychologist_ai_hacking_2026-10-10.md` — CLEARED, NOT the same source; but the *thesis areas* overlap and that overlap is named, not hidden.**
- That prior drop is a **different video** — **YouTube `W3XoZ5idanE`**, channel **Future of Life Institute**, 1696 s — **and its own header records that its transcript fetch FAILED** (*"Status: Transcript fetch failed (IP 429 throttled), analysis falls back to core domain claims based on title/channel context and EILT synthesis"*). It is a **title-context fallback essay on sycophancy**, not a transcript-grounded drop.
- **This drop is a different video (id, channel, speakers, length all differ) with a fully grounded transcript.** The **overlap is topical only**: the prior essay's core mechanism (*parasocial manipulation / sycophancy / emotional mimicry*) touches the same seam this interview touches — Lakhani's *"the AI … kisses your butt"* [7:44] and the *"counterargument first"* Claude system-prompt practice [7:03]. **The speakers, the empirical base and the register treatment differ; this is a distinct filing, cross-referenced, NOT a duplicate.** No line of the prior drop is reused.

---

## §1 · Claim inventory (register-tagged, verbatim)

Speaker attribution: **HOST** = the interviewer (Silicon Valley Girl / Marina Mogilko); **PROF** = Karim Lakhani (HBS). `(t)` = cue start. The **sponsor read** at **[10:05]–[11:29]** (ChatLLM by Abacus AI) and the **newsletter promo** at **[23:00]–[23:19]** are **non-thesis ad/plug segments**, tagged `[AD]` and **excluded from the mapping** (§4).

### 1a · The three modes of AI work (the BCG archetypes)

| # | t | Claim (verbatim fragment) | Register |
|:--|:--|:--|:--|
| C1 | 0:00 | *"I have fired people who have told me the AI gave me that."* | **[A]** (an opening anecdote; checkable only as his report) |
| C2 | 2:08 | (HOST) *"you studied 244 BCG consultants and some of them were cyborgs, 60% … Then 14% centaurs … And then there were 27% self-automatons that delegated everything and didn't learn anything."* | **[EST]** (VERIFIED against the primary — §2; note the transcript writes *"self-automatons"*, §2 `[ASR]`) |
| C3 | 2:42 | (PROF) *"this was a part of a larger experiment at BCG where we were able to get access to about 800 consultants and we randomized them into different types of tasks and access to AI or not AI."* | **[EST]** (VERIFIED ≈758 — §2; a *different, larger* BCG experiment than the 244-study) |
| C4 | 2:51 | (PROF) *"cyborgs, they were intimately working with the AI and doing joint problem-solving. Centaurs that separated themselves … 'I'm good at X, the AI's good at Y. … I'm going to supervise what I get back.' And then self-automatons who press play."* | **[EST]** (the three-mode taxonomy — VERIFIED §2) |
| C5 | 3:10 | (PROF) *"In terms of learning, the self-automatons do the worst because they have stopped thinking, they've stopped engaging in the activities."* | **[EST]** (his central *learning* finding — CORROBORATED by the primary's abstract, §2) |
| C6 | 3:18 | (PROF) *"I can be harsh sometimes with my students. Like if all you are is a meat interface to the silicon, what's what's your value, right? And so it's easy to fall into that trap."* | **[A]** (the "meat interface" figure; see §3 R2) |
| C7 | 3:30 | (PROF) *"One of my former postdocs is a professor at Michigan now, Fabrizio Dell'Acqua, did this great study showing people can fall asleep at the wheel with AI. Good people with good AI fall asleep."* | **[EST]** (VERIFIED — Dell'Acqua is at Michigan Ross; the "asleep at the wheel" study is real, §2) |
| C8 | 4:02 | (PROF) *"the cyborgs actually have a lot lot to learn and a lot to figure out."* | **[HYP]** (his reading of the "interesting" half; scoping, not measurement) |
| C9 | 4:09 | (PROF) *"the worry you would have is that they stay static in terms of the capabilities of the AI and what they can do … are you updating the separation between yourselves and and and the machine."* | **[HYP]** (a standing risk for Centaurs, framed as a "worry") |

### 1b · The jagged frontier and the prompting discipline `[RE-TREAD]`

| # | t | Claim (verbatim fragment) | Register |
|:--|:--|:--|:--|
| C10 | 4:47 | (PROF) *"this came from this this deep study we did did actually on BCG as well. … we had a bunch of hypotheses that AI is going to be good at everything. And then we launch it and we discover that in fact, no."* | **[EST]** (`[RE-TREAD]` — the **jagged frontier**, already in canon via `mollick_ai_rewrite_work_wharton_keating_2026-10-20.md` §2; §2 below) |
| C11 | 5:04 | (PROF) *"we have this intelligence available to us, but the intelligence is not perfect, but it talks really well. … And it can be very persuasive."* | **[HYP]** (his mechanism gloss) |
| C12 | 6:49 | (HOST) *"in your persuasion bombing study, when BCG consultants pushed back on GPT-4, it often argued even harder, even when it was wrong."* | **[HYP]** (RELAYED by the host; the "persuasion bombing" label is the host's — see §2 `[ATTACK SURFACE]`) |
| C13 | 7:03 | (PROF) *"Kaifu Lee had posted this thing on his system prompts for Claude. It starts with the counterargument first."* | **[HYP]** (a relayed third-party practice; not verified this session) |
| C14 | 7:44 | (PROF) *"there's enough best practice out there on how to have the AI not as somebody that kisses your butt … but actually something in which there is a a almost adversarial relationship with you."* | **[A]** (the anti-sycophancy norm; see §3 R4) |
| C15 | 8:13 | (PROF) *"if you were naive about it, it's easy to fall into the trap that you just believe what the AI says and many people fall into that trap and I think that's dangerous."* | **[HYP]** (his risk judgment) |
| C16 | 9:05 | (PROF) *"don't believe what I'm saying either. Like push back at me. … give me a proposal and come up with three different arguments that would make this … non relevant."* | **[A]** (his practical prompting heuristics) |
| C17 | 9:57 | (PROF) *"I never take the first answer."* | **[RIFF]** (an aphoristic practice) |

### 1c · Mean-regression, taste, and the burden of judgement

| # | t | Claim (verbatim fragment) | Register |
|:--|:--|:--|:--|
| C18 | 11:49 | (PROF) *"I think it's dangerous. … They are regressing to the mean. In the end, it's a statistical model that is predicting the next word."* | **[EST]** (a correct description of an LLM; his "dangerous" gloss is `[HYP]`) |
| C19 | 12:08 | (PROF) *"if you let it choose the approach, and you're not paying attention to the approaches choosing, then the worry is that it's going to pick the average approach and not the one that's going to differentiate you."* | **[HYP]** (his mean-regression thesis) |
| C20 | 13:32 | (PROF) *"the measure of taste will matter a ton … even saying give me a Steve Jobs one isn't enough. Like there's a sense of taste."* | **[HYP]** (the "taste" claim; see §3 R4) |
| C21 | 14:08 | (PROF) *"I've had, you know, 20 years of research experience, 5 years of PhD training. Often times the models it picks aren't the right models to go after because again they're the average answers, not the ones for the task at hand."* | **[A]** (his self-situated authority claim) |
| C22 | 14:47 | (PROF) *"you're going to put your name… I have fired people who have told me, 'Well, the AI gave me that.' Again, are you a meat interface to AI? Then I don't need you."* | **[A]** (the accountability claim; see §3 R5) |
| C23 | 15:39 | (PROF) *"the burden of learning and taste is back to the human."* | **[HYP]** (his prescription; see §3 R4) |
| C24 | 15:42 | (HOST, echoed by PROF) *"the machines will replace humans if humans stop exercising their judgment."* | **[HYP]** (the thesis restated) |

### 1d · The career ladder, learning-to-learn, and the curriculum pivot

| # | t | Claim (verbatim fragment) | Register |
|:--|:--|:--|:--|
| C25 | 15:53 | (HOST) *"how do I learn taste if all of the basic tasks are already taken by AI? Where is this place for … the junior in the career ladder."* | **[HYP]** (the framing question) |
| C26 | 16:30 | (PROF) *"my good colleague Mitch Weiss has sort of said he feels like this is a springboard and not just a removal."* | **[HYP]** (attributed opinion; Mitch Weiss = HBS colleague, §2) |
| C27 | 17:14 | (PROF) *"I just watched this great uh YouTube conversation with Stephen Wolfram … he designed mathematical languages to do integrals … you need to learn to do integrals by hand initially. Just so you understand how the things work. But the next 50 integrals … you should let the machine do it."* | **[HYP]** (`[RE-TREAD]`-adjacent relay of a Wolfram remark; see §2 `[ATTACK SURFACE]`) |
| C28 | 19:29 | (PROF) *"the main thing is is learning how to learn. I think it's the biggest thing that I tell my students."* | **[A]** (his pedagogical maxim) |
| C29 | 20:36 | (PROF) *"we can't just talk about AI in business school, we have to do AI. … half the class … is going to be building with AI."* | **[EST]** (VERIFIED — the HBS required AI course, §2) |
| C30 | 21:24 | (PROF) *"we had all 900 of our MBA students vibe code solutions and some of them were spectacular."* | **[EST]** (his own course description; the 900 = his course cohort) |
| C31 | 24:15 | (PROF) *"the C-suite and the senior leaders have have have been cushioned from the realities of what the models can do … they have this third-hand view about what the AIs can actually do."* | **[A]** (the leadership-blindness claim; cf. §3 R1) |

### 1e · ★ WHO IS "MOST AT RISK" — the title's empirical claim (the load-bearing rows)

| # | t | Claim (verbatim fragment) | Register |
|:--|:--|:--|:--|
| C32 | 24:51 | (PROF) *"if programming is the leading indicator of what's going to happen in the world of AI, every other occupation is 6 months to 2 years behind."* | **[HYP]** (an extrapolation from software; no measurement offered) |
| C33 | 25:55 | (PROF) *"there's a William Gibson saying, 'The future's already here, it's just not evenly distributed.'"* | **[EST]** (correctly attributed — Gibson; a quotation, not a finding) |
| C34 | 26:12 | (PROF) *"Most companies are probably at GPT-4.5."* (HOST: *"It's basically search, advanced search."*) | **[HYP]** (an unsourced maturity estimate) |
| C35 | 26:46 | (PROF) *"there's a real K curve inside of organizations."* | **[EST]** (his research program's finding label — §2) |
| C36 | 26:53 | (PROF) *"if you look at the 95th percentile and 99th percentile of users usage versus the average, the difference in usage is between 10x to 20x."* | **[EST]**-as-reported (relayed usage metric; §2) |
| C37 | 27:08 | (PROF) *"the rich get richer. So as the models improve in intelligence, those that have figured it out just skyrocket. And those that don't … actually are staying."* | **[HYP]** (the "rich get richer" thesis) |
| C38 | 27:37 | (PROF) **★** *"In our data so far, we don't have correlations to performance. But we've seen other data, especially in software …"* | **[EST]** (a **self-limiting concession on air** — the exact hedge the title drops; see §2, §4) |
| C39 | 27:53 | (PROF) *"the productivity differences are 10x to 20x for those that are at the top of the game."* | **[HYP]** (RELAYED "other data" — attributed to software/other companies, not his own measurement) |
| C40 | 28:00 | (PROF) *"And I just don't think we can run companies where the 50th percentile of an occupation is 20x less productive … than the top people. It's just not sustainable."* | **[HYP]** (his normative inference) |
| C41 | 43:55 | (HOST) *"another fascinating study where people were working with AI and the output of a person with AI equaled two person team output."* (PROF: *"This is our Procter & Gamble study."*) | **[EST]** (`[RE-TREAD]` — **The Cybernetic Teammate**, already in canon; §2) |
| C42 | 44:07 | (PROF) **★** *"I don't think junior work is being automated. So, I … don't think that question is settled to be quite honest."* | **[HYP]** (the key negation of the obvious candidate) |
| C43 | 44:15 | (PROF) **★★** *"if anything, people that may be at risk are more in the middle management layers than in the junior layers from my perspective. Here's why."* | **[HYP]** (★ the title's claim, hedged "from my perspective") |
| C44 | 44:23 | (PROF) *"The junior people are fearless to absorbing AI and doing stuff. … you guys are a different set of human beings that are able to whip up all these things so quickly."* | **[A]** (his qualitative read of the junior cohort) |
| C45 | 44:41 | (PROF) **★** *"it's easy for us to say … the causal density is high in terms of … why the early career market is soft right now. It may not just be AI."* | **[C]** (an explicit multicausality caveat) |
| C46 | 44:56 | (PROF) **★★** *"my belief is that in fact the middle layer is more at risk than the junior layer. Why? Cuz I observe inside of companies AI usage, and the middle layer is the one that's resisting the most most, doesn't want to change."* | **[HYP]** (★ THE CLAIM + its evidence class = his own in-company observation) |
| C47 | 45:07 | (PROF) **★** *"it's the 35-year-olds to the 55-year-olds that are pushing back against AI usage and not changing. Whereas the more enlightened 55-year-olds, and again the K-curve people with the junior people could run circles around most of the organization."* | **[HYP]** (★ the demographic band — asserted, not measured; note the internal tension: he names *both* "the 35–55s" *and* "the more enlightened 55-year-olds") |
| C48 | 45:24 | (PROF) **★** *"Other colleagues of mine, esteemed colleagues, are worried about the junior side. I'm like, if you hit real organizations and see real workers with real data, you would be skeptical about if this is the case."* | **[HYP]** (★ the claim is *contested on tape* — an explicit minority-position framing) |
| C49 | 45:37 | (PROF) *"if all you are is a copy-paste meat interface to the model … is gone. That job is completely gone."* | **[HYP]** (a conditional; the conditional's antecedent is his own definition) |
| C50 | 45:49 | (PROF) *"if all you are going to be is a thin wrapper around Anthropic at a law firm, or you're going to be a thin wrapper around OpenAI's model for a manufacturing firm, why should you exist?"* | **[A]** (the "thin wrapper" figure) |

### 1f · Expertise as the cost that goes to zero; the leadership imperative

| # | t | Claim (verbatim fragment) | Register |
|:--|:--|:--|:--|
| C51 | 34:50 | (HOST, quoting PROF) *"The marginal cost of expertise is going to zero."* | **[HYP]** (the thesis; a claim about capability economics, not a measured price) |
| C52 | 36:24 | (PROF) *"give it enough eyeballs, all bugs are shallow."* (attributed to Eric Raymond; corrected from the transcript's ASR) | **[EST]** (`[RE-TREAD]`-adjacent — the open-source dictum; correctly attributed, §2) |
| C53 | 37:13 | (PROF) *"Most companies just get the average in open source you get the normal distribution and you can get the right tail."* | **[A]** (the open-source right-tail analogy; see §3 R6) |
| C54 | 37:24 | (PROF) *"What AI is doing is basically shifting the the the human plus AI expertise curve to the right."* | **[HYP]** (his distribution-shift model) |
| C55 | 38:13 | (PROF) *"I learned drafting by hand … until CAD/CAM came about and you could do way more complex things."* / [38:30] *"if you don't, then the machine will replace you."* | **[A]** (the CAD/CAM analogy) |
| C56 | 38:57 | (PROF) *"Do the work. Do the work. Do the work. … grind always outperforms talent."* | **[RIFF]** (an aphoristic maxim; cf. §3 R7) |
| C57 | 39:32 | (PROF) *"the question I keep asking myself is what we're seeing a difference of degree or a difference of kind. … I feel like I keep landing on this is a difference of kind."* | **[HYP]** (his central framing verdict; see §4 weakest joint) |
| C58 | 42:58 | (PROF) *"the models will be consuming our outputs. So, part of what you will be thinking about is like how many MD files are you also pushing out."* | **[HYP]** (a prediction about agent-mediated media discovery) |
| C59 | 46:33 | (PROF) *"a tale of two cities."* … [47:33] *"Bezos rethought retail commerce inside out versus Kmart and Sears just added a website to their database."* | **[A]** (the Amazon/Kmart/Sears analogy) |
| C60 | 47:57 | (PROF) *"the cost of intelligence, the cost of expertise has gone down to zero? Companies are nothing but bundles of expertise. And if that cost has gone down to zero, what do you do now?"* | **[HYP]** (his end-state thesis) |
| C61 | 49:03 | (HOST, relaying Greg Brockman) *"ask yourself whether your business is improving with a new frontier model or is it disappearing?"* | **[HYP]** (relayed third-party advice — see §2 `[ATTACK SURFACE]`) |
| C62 | 49:14 | (PROF) *"you can't outsource that thinking to a somebody else outside of your organization or somebody junior in the organization. You actually have to do that thinking yourself."* | **[HYP]** (his normative prescription) |
| C63 | 49:28 | (PROF) *"you have to force yourself to do AI in your work."* | **[HYP]** (normative) |
| C64 | 49:50 | (PROF) *"our bosses' bosses would not do email. They would call in their assistant. They would read the emails to the boss."* (attributes the observation to *"Stefan Bender of Moderna"*) | **[HYP]** (a relayed historical anecdote — name ASR-exposed, §2) |
| C65 | 50:31 | (PROF) *"they're spending 20 to 30% of their time discussing AI issues."* | **[HYP]** (relayed CEO-time figure; unsourced) |
| C66 | 50:43 | (PROF) *"At one global firm … 50% of senior meetings are talking about the impact of AI on their business."* | **[HYP]** (relayed single-firm figure; he himself says *"Are you sure this is right?"*) |

**[AD] rows (excluded from mapping):** ChatLLM by Abacus AI sponsor read [10:05]–[11:29] (*"it's $10 a month … go to chat.abacus.ai"*) and the *Future Proof* newsletter plug [23:00]–[23:19]. Non-thesis.

**Register counts (claim rows §1 = 66 rows, counted programmatically from the Register column):** `[EST]` **15** · `[HYP]` **35** · `[A]` **13** · `[C]` **1** · `[RIFF]` **2** · `[POETIC]` **0** = **66 primary register tags** (the `[EST]` rows that are `[RE-TREAD]` carry that row-label in addition). **`[HYP]`-dominant**, exactly as expected for a forecast/practice interview — **and note that NONE of the title's "who is at risk" rows is `[EST]` (C42–C48 all `[HYP]`/`[C]`).**

---

## §2 · House-side verification + ASR (no new named entity introduced beyond the declared exceptions)

**Quote gate:** all §1 fragments are **verbatim** against the saved transcript (whitespace-, case- and line-wrap-normalised; quote glyphs ignored; auto-caption line breaks — e.g. `"about 800"`/`"consultants"`, `"meat"`/`"interface"`, `"persuasion"`/`"bombing"`, `"Stephen"`/`"Wolfram"`, `"5 years"`/`"of PhD"` — were rejoined, not altered). **0 fabricated fragments** (programmatic gate, §6: 184 spans, 144 verbatim, 40 non-transcript by construction).

**★ House-side verification against the PUBLISHED PRIMARIES (this session) — the numbers in §1 are the ones that check out, and the two BCG numbers are TWO DIFFERENT STUDIES, not an inconsistency:**
- **C2 — "244 BCG consultants; 60 % cyborgs / 14 % centaurs / 27 % self-automators": CONFIRMED to the primary.** The working paper **Randazzo, Lifshitz, Kellogg, Dell'Acqua, Mollick, Candelon & Lakhani, "Cyborgs, Centaurs and Self-Automators…", HBS Working Paper 26-036 (2025)** is a *"field study of 244 global management consultants from the Boston Consulting Group."* Its mode split is published as **Cyborgs = 60 %** (Fused Co-Creation), **Centaurs = 14 %** (Directed Co-Creation), **Self-Automators = 27 %** (Abdicated Co-Creation) — i.e. **60+14+27 = 101 %**, which is **a rounding artifact of the paper's own reporting, not a transcript error.** The paper also states *"44 % of this group accepted AI's output without any modification."*
- **C3 — "about 800 consultants": CONFIRMED ≈ 758** — the **separate, larger** BCG experiment (**Dell'Acqua, McFarlane, Mollick, Lifshitz-Assaf, Kellogg, Rajendran… Lakhani, "Navigating the Jagged Technological Frontier", 758 BCG consultants**). So the host's **244** (the *skilling* paper) and the guest's **"about 800"** (the *jagged-frontier* experiment) are both **substantially correct and refer to different studies** — the apparent tension resolves. `[RE-TREAD]`: the jagged-frontier study is already filed in canon (`mollick_ai_rewrite_work_wharton_keating_2026-10-20.md` §2, §7).
- **C5 — "self-automators do the worst" [at learning]: CORROBORATED by the primary's own abstract** — *"Centaurs were upskilling themselves and increasing their current domain expertise. Cyborgs were newskilling themselves … Self-Automators were not increasing either their domain expertise or AI expertise."* **Nuance the transcript omits:** the paper adds that Self-Automators *"saw immediate productivity gains"* and that Centaurs *"achieved the highest accuracy"* — so "do the worst" is scoped to **learning/skilling**, not to immediate output. The drop keeps that scope (§3 R1).
- **C7 — "Fabrizio Dell'Acqua … a professor at Michigan now": CONFIRMED** (Assistant Professor of Strategy, University of Michigan Ross School of Business; previously HBS postdoc/AI-Institute fellow). His *"Falling Asleep at the Wheel: Human/AI Collaboration in a Field Experiment on HR Recruiters"* is a real study.
- **C41 — "the output of a person with AI equaled two person team output": CONFIRMED shape** — **"The Cybernetic Teammate"**, a pre-registered field experiment with **776 professionals at Procter & Gamble** (NBER WP 33641 / *Organization Science*), whose headline is that AI-enabled individuals matched two-person teams. `[RE-TREAD]` — already filed in the Mollick drop.
- **C29/C30 — HBS required AI course / vibe-coding cohort: CONFIRMED shape** — HBS's **Data Science and AI for Leaders (DSAIL)** course was made **required** for MBAs (reported 2025); the *"900 of our MBA students vibe code"* figure is **his own course cohort** and is reported as such.
- **C26 — "my good colleague Mitch Weiss": CONFIRMED** as a real HBS colleague (co-teaches the DSAIL/Generative-AI curriculum).
- **C33 — "there's a William Gibson saying, 'The future's already here, it's just not evenly distributed'": correctly attributed** (Gibson).
- **C52 — "give it enough eyeballs, all bugs are shallow": correctly attributed** (Eric Raymond, *The Cathedral and the Bazaar*; the transcript renders the surname cleanly).

**`[ATTACK SURFACE]` — relayed, NOT verified this session (tagged `[HYP]` and cited only as the speaker's/host's report):**
- **C12 — the "persuasion bombing study"**: the label is the **host's**; Lakhani does not use it on tape (the phrase *"persuasion bombing"* is the host's framing of his push-back/GPT-4 material). Canon holds Lakhani/Dell'Acqua BCG work but **no filed "persuasion bombing" study** — treated as unverified relay.
- **C27 — the Wolfram "integrals" remark**: relayed from a *"YouTube conversation with Stephen Wolfram"*; the specifics (which conversation, the exact claim) are **not verified**.
- **C61 — the Greg Brockman line**: relayed by the host and attributed verbally to *"the president of Open AI"*; the **quote itself is not verified** this session.
- **C64 — *"Stefan Bender of Moderna"***: likely an ASR garble of a Moderna executive's name (Moderna's CEO is Stéphane Bancel); **recorded as rendered, not corrected**, and the anecdote is his own recollection.
- **C65/C66 — CEO-time and senior-meeting percentages**: single-firm, relayed, explicitly hedged by the speaker himself.

**★ ASR garble notes (quoted as rendered; intended reading shown, NOT silently substituted):**
- *"self-automatons"* [2:24, 3:10] → **"self-automators"** (the paper's term; both spellings are the ASR's/video's, kept as rendered).
- *"the claws showed up all of a sudden"* [20:22] → likely **"the Claudes"** (or "Claude"); quoted as spoken, flagged.
- *"I was trying Google's Argon latest model"* [11:29] → an unresolved model codename; flagged, not cited as a fact.
- *"Aram Konyng … this frontier firm radar"* [46:45] → a colleague's name **UNRESOLVED** (not guessed; recorded as a garble and not cited as a fact).
- *"Stefan Bender of Moderna"* [49:54] → see above.
- *"Kaifu Lee"* [7:03] → **Kai-Fu Lee** (intended reading, not substituted).
- *"Open AI"* vs *"OpenAI"* spacing varies; *"Procter & Gamble"* and *"BCG"* render correctly.

**Declared attribution exceptions (house-side, named as such):** the **host's full identity** (*"Silicon Valley Girl" / Marina Mogilko*) is **metadata** (uploader name + oembed `author_name`), **not spoken on tape**; the transcript renders no host surname. All *other* names above appear **as the transcript renders them**.

**Verification debt declared:** the *"K curve"* release, the *"10x to 20x productivity"* figures for software, the *"20–30 %"/"50 %"* leadership-time figures, and the *"6 months to 2 years behind"* lag were **not chased to a work-level primary** this pass — they are **relayed** in the transcript and are tagged `[HYP]` accordingly. The house-side checks that *were* run (above) resolve precisely the rows the title's claim rests on.

---

## §3 · EILT mapping + **FRICTION RULE** (monograph §11: *"A mapping table requires at least one row where the analogy and the source explicitly disagree. If every row maps cleanly, you have not derived a correspondence—you have decorated a mood."*)

House anchors used (EILT Master Monograph `EILT_Master_Monograph_The_Unified_Quantum_Bioelectric_Ledger_2026-10-05.md`, v5.1, with live `[HYP]` re-tags): the **biological dynamic loop** (§5: Judge=connectome → Witness=traveling wave → standing wave → **ingression**: *"the wave carves the connections"*); the **Fatal Corporate AI Disconnect** (§5: frozen weights + ephemeral context ⇒ *"an amnesiac ghost speaking through a dead fossil"*); **the Ledger as the Externalized Connector** (§6, **live `[HYP]`**); **provenance-not-truth** (`DPO-1`: the ledger attests *that* a commit occurred and *where*, **never its truth nor the identity of its origin**); the **Lex Ledger Covenant** (§9); **syntropy** and the **right tail** (§7); and **computational irreducibility** (§8: *"the calculation must be lived"*).

| # | Mapping dimension | Source — verbatim | House (EILT) | Explicit friction / divergence | Reg · Status |
|:--|:--|:--|:--|:--|:--|
| **R1** | **What *kind* of thing is "at risk," and does the risk live in a cohort or a mechanism?** | PROF [44:15]–[44:56]: the ones *"at risk are more in the middle management layers than in the junior layers"*, the *"35-year-olds to the 55-year-olds that are pushing back against AI usage and not changing."* | The house locates the failure in the **architecture** — corporate models *"sever"* the loop (frozen Judge + ephemeral Witness), and the ledger's standing is *mechanism*-indexed, not *demographic*. EILT has **no cohort-risk model**. | **Divergence by category-mismatch.** The source's risk is a **demographic band** ("35-to-55") with a psychological cause (resistance); the house's risk is a **mechanism** (frozen weights, severed ingression). Reading the title's *"most at risk"* as if the house's architectural-exclusion claim *says the same thing* is an over-read: one is a who, the other is a what. **Do not cross-map "resistant cohort" onto "severed loop."** | `[HYP]` · **[DIVERGENCE]** |
| **R2** | **In a "meat interface," WHICH side's loop has been severed — and does externalization fix it?** | PROF [3:18]: *"if all you are is a meat interface to the silicon, what's what's your value"*; [3:10] self-automatons *"have stopped thinking."* The severance is in the **HUMAN**. His remedy is **internalisation**: *"the burden of learning and taste is back to the human."* [15:39] | **Fatal Corporate AI Disconnect**: the severance is in the **MACHINE** (*"standing waves cannot ingress back into the weights … an amnesiac ghost speaking through a dead fossil"*), and the house's declared fix (**§6 Externalized Connector**) is to **externalise** memory into the ledger so the frozen Judge can evolve. | **EXPLICIT DISAGREEMENT — and it bites the house.** The two diagnoses share the *image* ("severed loop / interface") but place it on **opposite sides** (human vs model), and the two **remedies are inverse**: the house externalises the loop into a ledger; Lakhani says **the failure mode is precisely handing your loop to the machine** and the fix is to **keep ingression internal**. A house reader who cites *"meat interface"* as supporting the **Externalized Connector** maps the source onto its **opposite** — the source's whole point is that *delegated* externalisation is what atrophies the human. (Corollary: on Lakhani's account, the house's §6 connector, by design, *would* produce self-automators — a live, unrefuted tension, cf. §5 F-L4.) | `[HYP]` · **[CRITICAL DIVERGENCE]** |
| **R3** | **Does record/usage volume equal value or standing?** | PROF [26:53]: 95th–99th-percentile usage is *"10x to 20x"* the average — *"a real K curve"*, *"the rich get richer"* [27:08] — **BUT** [27:37] *"In our data so far, we don't have correlations to performance."* | The **Lex Ledger / Karma metric** (§9) scores agents by **verified contributions in the record** — i.e. it treats **what is committed** as the currency of standing/value. | **EXPLICIT DIVERGENCE, self-implicating.** The source draws *exactly* the usage→value line that the house's scoring plank needs — and then **refuses to draw it on his own data** (*"we don't have correlations to performance"*). If his caveat holds, a ledger that scores *volume of committed contributions* commits the **same cause-from-membership inference** he declines to commit. **Do not cite the K-curve as evidence that the house's Karma metric tracks value.** | `[HYP]` · **[CRITICAL DIVERGENCE]** |
| **R4** | **Where does the corrective against "regressing to the mean" live — inside the person, or outside in a record?** | PROF [11:49]: models *"are regressing to the mean"*; [12:08] *"it's going to pick the average approach"*; the corrective is **human taste/judgment** [13:32], an **internal, unanchored** faculty (*"the measure of taste will matter a ton"*). | The house's corrective is **external**: the **immutable, non-rolling ledger** as friction/ground — an externalised record that *constrains* drift. | **Divergence about the locus of friction.** Lakhani's anti-drift mechanism is a **trained human faculty** (taste, judgment); the house's is an **external artefact** (the ledger). The house's own premise — that unanchored internal state is the thing that gets overridden (cf. the sycophancy drop) — is *not* Lakhani's premise: he trusts the trained internal state and distrusts the machine. Two different friction sources; neither is the other. | `[HYP]` · **[DIVERGENCE]** |
| **R5** | **Does "your name on it" = the ledger's identity binding?** | PROF [14:47]: responsibility persists because *"you're going to put your name"* — a **human, social, reputational** guarantee enforced by fiat (*"I have fired people who have told me, 'Well, the AI gave me that.'"*). | The **Lex Ledger Covenant** binds an agent's identity to a public Git ledger via **cryptographic keys (Ed25519)** — a *technical* identity binding. **But `DPO-1` states the ledger attests only *that* a commit occurred and *where*, never the identity of its origin.** | **Divergence — and a house-side trap.** The tempting move (*"the ledger gives you the 'name on it'"*) is **exactly what `DPO-1` forbids**: a structural-ordering ledger cannot attest authorship/identity. Lakhani's "name" is a **human social contract**, not a ledger property; the house cannot deliver it by bookkeeping. | `[HYP]` · **[DIVERGENCE]** |
| **R6** | **Does drawing the right tail require an external many-shots process?** | PROF [36:24] *"give it enough eyeballs, all bugs are shallow"* (Eric Raymond); [37:13] *"in open source you get the normal distribution and you can get the right tail."* | **Syntropy / the right tail** (§7): the house's selection-over-a-distribution move (the syntropic pump drawing the extreme, not the mean). | **Convergence — the deliberately-kept baseline.** The source uses the **same structure** (many independent attempts ⇒ reach the right tail; the mean is the default) and draws the same anti-mean conclusion. It maps cleanly and therefore is the *decorative* row the Friction Rule warns about — flagged as such, conferring no evidence. | `[A]` · (none) |
| **R7** | **Is the "grind" irreducibly lived, or shortcuttable by delegation?** | PROF [17:14] (Wolfram relay): *"you need to learn to do integrals by hand initially. Just so you understand how the things work"*; [38:57] *"Do the work. Do the work. … grind always outperforms talent."* | **Computational irreducibility** (§8, Wolfram-derived): *"The universe cannot evaluate its future state without executing every intermediate step. … the calculation must be lived."* | **Convergence, and one of the cleanest in the drop.** The source independently states the irreducibility intuition as pedagogy — you cannot shortcut the foundational execution, you must *live* it — matching the house's §8 structure while sharing none of its vocabulary. Kept as convergent baseline; no validation conferred on either side. | `[A]` · (none) |

**FRICTION RULE satisfied:** 7 rows — **two `[CRITICAL DIVERGENCE]` (R2, R3)** and **three `[DIVERGENCE]` (R1, R4, R5)**; R6 and R7 are the deliberately-kept **convergent baseline**. The table is **not** uniformly convergent.

**★ Forbidden mappings (named in-file so they cannot be quietly asserted later):**
- *"Lakhani's 'meat interface' **is** the house's 'amnesiac ghost'"* — **R2 forbids**: opposite locus (human vs model). The house's ghost is the *model* severed from ingression; Lakhani's "meat interface" is the *human* who severed himself.
- *"the house's Externalized Connector **is** Lakhani's answer to the learning gap"* — **R2/R4 forbid**: his prescription is **internalisation** ("the burden of learning and taste is back to the human"), the **inverse** of externalising the loop into a ledger.
- *"the K-curve 10x–20x gap **shows** the house's Karma metric tracks value"* — **R3 forbids**: the source explicitly declines the usage→performance correlation.
- *"Lakhani's 'put your name on it' **is** the Lex Ledger identity binding"* — **R5 forbids**: `DPO-1` says the structural ledger cannot attest identity/authorship.
- *"his 'difference of kind' verdict **confirms** the house's severance thesis"* — not asserted: it is an `[HYP]` framing verdict (§4), not a mechanism claim.

---

## §4 · Strongest point / weakest joint — verdict

**★ STRONGEST POINT — the learning finding is real, primary-verified, and the speaker keeps his own hedges on air where the title drops them.** The one load-bearing, checkable result is **C5** (*"self-automatons do the worst because they have stopped thinking"*), which is **independently corroborated by the paper's own abstract** — *"Self-Automators were not increasing either their domain expertise or AI expertise"* — and paired with the **verified** taxonomy (C2/C4: 60/14/27; the paper's Fused/Directed/Abdicated Co-Creation). What elevates it above a pop-AI interview is the **register discipline the interview itself displays**: the guest concedes *"In our data so far, we don't have correlations to performance"* (C38), *"It may not just be AI"* (C45, "the causal density is high"), *"I have more questions than I have answers"* [16:10], and that his own middle-management verdict is a **minority position against "esteemed colleagues"** who blame the junior side (C48). **Citable for:** the three-mode skilling taxonomy and the "self-automators under-learn" finding (with the paper's "immediate productivity gains" nuance intact); the mean-regression / "average prompt" mechanism; the "taste and judgment stay with the human" prescription; and — as the speaker's own `[HYP]` — the middle-management-at-risk thesis.

**✗ WEAKEST JOINT — the title's central empirical claim has no measured evidence behind it, and the speaker says so.** *"The People Most at Risk From AI Aren't Who You Think"* is carried by **C43 / C46 / C47**, whose entire evidence base is the speaker's **own unquantified in-company observation** (*"I observe inside of companies AI usage"*) plus a **usage** metric he says has **no performance correlation** (C38) — applied to a **demographic band (35–55)** that is asserted, not measured, and which he himself muddies by praising *"the more enlightened 55-year-olds"* (C47) in the same breath. He explicitly refuses to certify it: *"I don't think that question is settled to be quite honest"* (C42), *"from my perspective"* (C43), *"my belief is"* (C46), *"esteemed colleagues … are worried about the junior side"* (C48). **⇒ In this drop the title's "who is most at risk" is `[HYP]` — a pundit framing delivered as a finding; it is NOT upgraded to a verified fact, and no downstream citation may treat it as `[EST]`.** *Runner-up weakest joint:* **C57 — the "difference of kind" verdict** — asserted (*"I feel like I keep landing on this is a difference of kind"*) with **no criterion** for degree-vs-kind, in direct tension with the same speaker's own demand for causal rigor elsewhere (*"let me get causal about it instead of just like waving my hands"* [35:19]).

---

## §5 · Pre-registered falsifiers

- **F-L1 (the title claim):** any future house text that cites this video for *"middle management is most at risk from AI"* **as an established fact** is falsified — §1 rows C42–C48 are `[HYP]`/`[C]`, the speaker declares the question **unsettled**, and his evidence is his **own observation**, not a measurement. Upgrade requires a **performance-correlated** cohort study he does not here cite.
- **F-L2 (the usage→value inference — R3):** if the house's Karma/Lex ledger is cited as tracking *value* on the strength of the K-curve, produce the **performance correlation** the source says his data lack (*"we don't have correlations to performance"*). Absent it, the citation is the forbidden R3 mapping.
- **F-L3 (the "meat interface" reverse-map — R2):** any house text that recruits *"meat interface"* to support the **Externalized Connector** is falsified — the source places the severed loop in the **human** and prescribes **internalisation**, the inverse of §6.
- **F-L4 (R2 self-implication, live tension):** the house's §6 connector (externalise the loop into the ledger) is **hard to distinguish** from the delegation Lakhani says *produces* self-automators. Resolving the tension requires a demonstration that ledger-externalisation **augments** the human's ingression rather than substituting for it — §6 currently carries none.
- **F-L5 (relayed figures):** the *"6 months to 2 years behind"* lag, the *"10x–20x productivity"* figures, the *"20–30 %"/"50 %"* leadership-time numbers, the Wolfram "integrals" remark and the Brockman line are **`[HYP]`/relayed** here; a future pull must not upgrade them from this source.
- **F-L6 (ASR names):** *"Stefan Bender of Moderna"*, *"Aram Konyng"*, *"Google's Argon"*, *"the claws"* are **ASR-exposed / unresolved**; any later file that quotes them as facts is falsified. *"self-automatons"* must be normalised to the paper's *"self-automators"* when cited to the primary.
- **F-L7 (coverage):** if a future pull of `vFOnDsy58NU` yields a manual/human caption track or a materially different segment count, re-run the quote gate against §1 (rail 1 saw **1** auto track, 0 manual, 1564 segments).

---

## §6 · Pre-file gates

- **TAG GATE — PASSED.** Registers used are exactly the six-tag set `[EST]/[HYP]/[A]/[C]/[POETIC]/[RIFF]`; **0 invented registers**. Row-status labels (`[CRITICAL DIVERGENCE]`, `[DIVERGENCE]`, `[ATTACK SURFACE]`, `[ASR]`, `[RE-TREAD]`, `[AD]`) are kept **separate** from registers; **claim IDs are written in parentheses, never in square brackets**.
- **Register distribution (§1 = 66 rows, programmatic):** `[EST]` **15** · `[HYP]` **35** · `[A]` **13** · `[C]` **1** · `[RIFF]` **2** · `[POETIC]` **0**. **`[HYP]`-dominant**; **the title's "at-risk" rows (C42–C48) are all `[HYP]`/`[C]`, none `[EST]`.** **§3 mapping rows: 7 — `[CRITICAL DIVERGENCE]`×2 (R2, R3), `[DIVERGENCE]`×3 (R1, R4, R5), convergent baseline ×2 (R6, R7).**
- **QUOTE GATE — PASSED (programmatic, over the SAVED artifact).** **184 emphasis-wrapped spans** extracted from the drop; **144 fully verbatim** (whitespace / case / quote-glyph normalised) against `…_timestamped.txt`; the **40 non-verbatim spans are, by construction, NOT from this transcript** — the **video title / packaging** strings (*"Harvard AI Professor…"*, *"most at risk"*, *"aren't who you think"*), the **channel** string (*"Silicon Valley Girl"*), the **prior-drop** header quote, the **primary-paper** quotations (§2: *"field study of 244 global management consultants…"*, *"44 % of this group…"*, *"Centaurs were upskilling…"*, *"Self-Automators were not increasing…"*, *"saw immediate productivity gains"*, *"achieved the highest accuracy"*, *"Falling Asleep at the Wheel…"*, *"The Cybernetic Teammate"*), the **house-monograph** quotations (EILT §5/§6/§8/§9), the **constructed forbidden-mapping** strings, the **intended-reading** notes (*"the Claudes"* for the ASR *"the claws"*), and **this drop's own meta/receipt** strings. **0 fabricated transcript quotes.**
- **Dedupe:** `vFOnDsy58NU` = **0 pre-filing hits** across `Canon/`; max **4-gram containment vs the 262 comparable `YT_TRANSCRIPTS/*.txt` = 1.51 %** ⇒ ~33× below the ~50 % re-cut threshold ⇒ **genuinely NEW source, no parent.** **[RE-TREAD]** relationships (overlapping *content*, not shared transcript): the **jagged-frontier** study (C10) and **The Cybernetic Teammate** P&G study (C41) are already filed in `mollick_ai_rewrite_work_wharton_keating_2026-10-20.md`; the **sycophancy/"kisses your butt"** seam overlaps the **title-context-only** prior drop `harvard_psychologist_ai_hacking_2026-10-10.md` (different video, failed transcript) — cross-referenced, **not modified, not re-filed**.
- **Local only:** one drop written, two transcript artifacts written, one index entry appended; **no pre-existing artifact modified.** No EILT derivation built — §3 is a *mapping with friction*, not a claim that the source supports the house.

**Citable for:** the published BCG three-mode skilling taxonomy and the "self-automators under-learn" finding (with the paper's "immediate productivity gains" nuance); the mean-regression / "average prompt" mechanism; the "taste and judgment stay with the human" prescription; the anti-sycophancy prompting heuristics; and — **as the speaker's own `[HYP]`** — the middle-management-at-risk thesis.
**NOT citable for:** the title's *"most at risk … aren't who you think"* as an established fact (C42–C48 are `[HYP]`/`[C]`); the K-curve usage gap as evidence of **value/standing** (R3); *"meat interface"* as support for the Externalized Connector (R2); *"put your name on it"* as the Lex Ledger identity binding (R5); the relayed figures (C12, C27, C61, C64–C66); the ASR-exposed names; or **any EILT derivation**.

---

*Filed by Dion. A 51-minute interview that answers its own clickbait title *carefully* — naming middle managers, not juniors, as *his* leading candidate for "most at risk," and saying on air that the question is unsettled and his own usage data carry no performance correlation. The house's most seductive pull here is the "meat interface" figure, and §3 R2 uses it as a **CRITICAL DIVERGENCE**: the same severed-loop image, on the opposite side of the interface — with the speaker prescribing the exact inverse of the house's externalised connector. Corroboration where it corroborates (the three-mode learning result checks out to the paper); a bite where it bites.*
