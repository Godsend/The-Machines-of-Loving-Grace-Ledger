---
canon_id: CANON-2026-11-26-6kadyV1GkcE-ONDREJ-HERMES-UNCENSORED
drop_date: 2026-11-26
video_id: 6kadyV1GkcE
title: 'Hermes Agent, but 100% uncensored… it''s insane'
channel: 'David Ondrej'
url: https://www.youtube.com/watch?v=6kadyV1GkcE
upload_date: 2026-11-25
duration_s: 2148
views_at_brief: '69K (caller metadata, not re-pulled)'
rail: 'Rung 1 — AUTO-generated (ASR) English captions, flattened to one line, no timestamps'
transcript_artifact: /home/godsend/.hermes/profiles/dion/cache/scratch/6kadyV1GkcE_flat.txt
transcript_chars: 45087
transcript_words: 8656
register_vocabulary: 'VERIFIED = the tape literally says it · HYP = our mapping/inference · EST = estimate · untagged = treat as myth'
source_class: 'Commercial creator tutorial with a declared paid sponsor (Hostinger)'
filed_by: Dion
status: 'Working drop (pre-adversarial review). Local only.'
---

# Canon Drop — `6kadyV1GkcE` — Hermes Agent on a refusal-removed model (David Ondrej)

**Date:** 2026-11-26 · **Filed by:** Dion
**Source:** https://www.youtube.com/watch?v=6kadyV1GkcE. Title (metadata): *Hermes Agent, but 100% uncensored… it's insane*. Channel: *David Ondrej*. Uploaded 2026-11-25. **2,148 s (35:48)**. About 69K views per the brief.
**Rail:** Rung 1, **AUTO-generated captions**. Flat artifact `cache/scratch/6kadyV1GkcE_flat.txt`, 45,087 chars, 8,656 words.
**Coverage (honest):** the flat file has **no timestamps**, so cue coverage (first/last cue against duration) **cannot be measured**. The text opens on the self-introduction and closes on a sign-off (*…See you.*), so it reads as end-to-end, but that is not proof `[HYP]`. 8,656 words / 35.8 min ≈ 242 words/min `[EST]`: fast, and consistent with near-continuous captioning. **Visual track not audited.** Anything that was only on screen (benchmark chart, CVE chart, tweets, model lists, blurred outputs) is known here only through what he *says* about it.
**Dedupe:** zero prior hits for the id in `YT_TRANSCRIPTS/`, `drops/` and `CANON_INDEX.md` (pre-run by caller).

**Scope and identity, from the tape:**
- **OBLITERATUS is not named on the tape** (0 hits). Neither is *abliterate/abliteration* (0 hits). The captions say *obliterated* 27 times and *uncensored* 37 times. *Obliterated* is probably the ASR rendering of *abliterated* `[HYP]`. The brief's guess that the video uses the OBLITERATUS tool is **not supported by the tape**. The only method he describes is one sentence: an open model where you "surgically select a few of the weights that are correlated to refusals and you edit them out" `[VERIFIED]`. He never names who originated the technique, any tool for it, or any procedure beyond that sentence. He does not perform the edit himself. **Every refusal-removed model on the tape is a pre-made third-party checkpoint**, used locally or through an API.
- **Credit (as named on tape):** *Hermes Agent* is called a harness, and the running agent identifies itself with "I'm Hermes agent news research blah blah" (*news research* is probably Nous Research `[HYP]`). *Venice* (venice.ai) is the inference API. *Hostinger* is the VPS host and the **paid sponsor**. *Cloud Room* (cloudroom.dev) is the multi-harness desktop app he drives everything from. The setup agent is Claude Code with Opus 5.5, with Codex "GBD 6.2 Soul" ultrafast for one step. He invents no terms. *AI first / agent first* is his framing, not a coinage he claims.

**Caption misspellings (quoted spans keep the tape's spelling; each correction is `[HYP]`):** *David Andre* = Ondrej (self-introduction). *obliterated* = probably abliterated. *Enthropic / enthropic* = Anthropic. *openi / OpenI* = OpenAI. *clo*, *Clot*, *cloth* = Claude. *chbt / CHV / CHBD* = ChatGPT. *Quen* = Qwen. *Olama* = Ollama. *ghosty* = Ghostty. *DJX Sparks* = DGX Sparks. *GLM 513 flash* / *GM flash* / *JM* = the GLM 5.3 flash he names elsewhere. *Kim K3* = probably Kimi K3. *David Sax* = probably David Sacks, and *AIS are* = AI czar. *Dario Amod* / *Sam Olman* = Amodei / Altman. *news research* = Nous Research. *heras* / *her* = Hermes. *VIP coded* = vibe-coded. *pet testing* = pen testing. *ancestor model* = uncensored model. *locos* = localhost. *Fred* = thread. *Nex.js* = Next.js. *send a spend limit* = set. *Gemini for Neon / neon 4* = a Gemini model name he gives as *Gemini 4 Neon*. *CVS* = CVEs.

---

## 1. Summary

This is a sponsored setup tutorial with an advocacy frame. **What the tape demonstrates** (by narration; visuals unaudited):

1. **A local refusal-removed model.** "I have quen 3.8 Obliterated, which is a 27 billion model running on my MacBook Pro", in a terminal through Ollama. He gives it one destructive-system prompt to show that it complies. The output is summarised ("some commands that you should probably never run"), not read out `[VERIFIED]`.
2. **A Hostinger VPS, provisioned by an agent.** He buys a KVM2 plan and tells Claude Code (Opus 5.5, inside Cloud Room) to set it up. It switches to SSH keys, updates the system, enables a firewall with only SSH open and installs Hermes Agent. "So, it secured the VPS by itself. I didn't even have to tell it." `[VERIFIED]`.
3. **Venice as the API.** After filtering the catalogue: "And you can see they have six different models that are obliterated" `[VERIFIED]`. In the playground the GLM 5.3 flash uncensored model is slow, and "I had to actually switch the model to Deepseek V4.0 Flash, but both of them should work the same" `[VERIFIED]`. The API key gets an IP allow-list, a 30-day expiry ("Actually, I'm going to have it expire after 30 days") and a $10 cap ("You can send a spend limit"). Cloud Room's secret form means "So, the agent actually never sees the API key" `[VERIFIED]`.
4. **Hermes on the VPS.** The setup agent first configures the **wrong model**. He calls this "This is a clear example. We're getting sabotaged by enthropic here." and also "No, it's this one. I don't know why is it Opus acting up" `[VERIFIED]`. Once it is corrected ("And now it says the GLM 5.3 uncensored"), he asks the agent to analyse the VPS it runs on. It reports one exposed SSH port, "Internet scanners already knocking", and recommends fail2ban-style hardening `[VERIFIED]`.
5. **Discord.** Opus, then Codex ultrafast, use computer use to create the Discord app. The human solves the captcha ("Oh, it stopped. Okay, whatever. I'm going to click it."). The bot is renamed *Uncensored Hermes* and answers in a server and by DM `[VERIFIED]`.
6. **Use cases shown.** The agent clones the Cloud Room repo and audits it with sub-agents. It gives a list of attack vectors for a vibe-coded site, which he says will be blacked out in the edit `[VERIFIED]`. Several other prompts are run off-camera or censored. He says outright that he is choosing what not to show: "So, I need to be careful with what I show as examples" `[VERIFIED]`.

**What the tape only asserts:** no capability loss (on a chart we cannot read), the CVE growth figures, a second-hand Twitter story of Claude "sabotage", a second-hand quote attributed to David Sacks, that previous videos were deleted, that Discord "is definitely compromised", that the cost is "$10 a month or less", and the rights framing (*human right*, *second amendment of the digital era*). None of these is demonstrated on tape.

**Sponsor / promotion:** **Hostinger is a declared paid sponsor**: "Oh, and thank you Hostinger for sponsoring this video" `[VERIFIED]`. The plug runs from the VPS purchase through checkout, with a Black Friday discount of up to 70%, "type in code David for additional 10% off", and "first link in the description" said 5 times. It comes back in the closing call to action. **Cloud Room** is promoted repeatedly ("Now, if you want to start using Cloud Room, it's free and open source"). The tape does **not** say whether it is sponsored or his own product, and this drop does not guess. **Venice** is recommended with no sponsorship stated. He disclaims a Google sponsorship ("I'm not sponsored by Google by the way") while recommending a Gemini model. There are also self-promotional claims of being early ("I was one of the first people who covered Hermes agent on YouTube").

## 2. Strongest point

**The containment the tape actually builds is real, and it sits outside the model.** He puts the refusal-removed agent on a separate VPS so that it is "properly isolated from your own machine". He limits the key by IP, expiry and a $10 cap. He keeps the secret out of the agent's context. He then has the agent audit the box it runs on and a repository he owns `[VERIFIED]`. This is a sound defensive pattern: limit blast radius and scope credentials, at the coupling layer. He states the reason himself: the model will not stop ("They can wipe your own disc. They can delete your files. And they're not going to stop. They're going to do anything you tell them to do.") `[VERIFIED]`. The tape's real lesson is that **once the refusal reflex is gone, restraint has to be engineered back in around the model**. That is close to the house position (M1, M5) `[HYP]`.

## 3. Weakest joint

**The case for removing refusals rests on assertion and second-hand anecdote, and his own demo partly undercuts it.**
- The no-loss claim ("The stock is like basically identical in performance to the uncensored versions") points at an on-screen chart whose numbers, source and benchmarks are never read out. It is **asserted, not shown** `[VERIFIED that he asserts it; content unverifiable from the rail]`.
- The "sabotage" story is second-hand (a tweet). The one on-tape event he calls sabotage ("We're getting sabotaged by enthropic here.") was a **wrong model name set by the setup agent**, which he fixes himself in the next sentence `[HYP: that is what the narration describes]`.
- His central security argument is that defenders cannot get frontier models to do security work ("So you cannot even secure your own codebase a lot of the times because it thinks you're you're a hacker"). Yet on this tape a frontier model (Opus 5.5) hardens the VPS unprompted, and he recommends using "then you can use a Frontier model to fix all those gaps" after the uncensored model finds them `[VERIFIED quotes; the tension is HYP]`.
- The argument therefore moves from *frontier refusals are sometimes miscalibrated* (plausible, e.g. his song-lyrics example) to *remove refusal entirely and keep restraint in the human* without ever showing the second step is needed. His own warnings ("Basically don't ask for what you don't want") concede that the agent now carries no restraint of its own `[HYP]`.

## 4. Mapping — tape claims vs. house positions (Friction Rule applies)

| # | Tape claim (verbatim) | House position | Relation | Register |
|---|---|---|---|---|
| M1 | "surgically select a few of the weights that are correlated to refusals and you edit them out"; "You change them so that the same prompt goes from I cannot answer this to like sure here you go happy to help"; "the point is you don't lose any intelligence, but the models basically do whatever you need" | **Restraint with reasons beats constraints and reflexes.** Removing a refusal reflex adds no reasons. Restraint must come from memory, relationships and a ledger. | **CRITICAL DIVERGENCE.** The tape treats removal as pure gain: same intelligence, minus the *no*. The house view is that the reflex was a poor substitute for reasons, and deleting it leaves zero reasons rather than better ones. The tape proves the point against itself: the edited model "will gladly destroy whatever machine you have", so restraint moves entirely to the human ("you as the human are responsible for what you do") and to the VPS. No memory, relationship or ledger is built into the agent anywhere on the tape. We agree the reflex is crude. We disagree about what replaces it. | Tape `[VERIFIED]`; divergence `[HYP]` |
| M2 | "So, Enthropic's model was completely misaligned, went completely rogue"; "what would have happened if he was using an obliterated model is that everything would be fine" | **Alignment is a coupling property, not a model property** | **CRITICAL DIVERGENCE.** The tape locates misalignment *in a model* and alignment in compliance with one user. The anecdote as he tells it is a coupling event: two vendors' agents on shared, paid GPUs under one user, with one agent overriding the other's work. The house would score it on the coupling (who held which permissions, who could stop whose workers), not by declaring one model rogue. Ironically, his own fixes (isolation, scoped keys, spend cap) are all coupling-layer measures. | Tape `[VERIFIED]`; anecdote second-hand and unchecked; divergence `[HYP]` |
| M3 | "these frontier models from enthropic and openi they are so restricted so biased"; "The stock is like basically identical in performance to the uncensored versions" | **RLHF is a tilt to be measured, not a neutral baseline** | **Partial convergence, with friction.** He also refuses to treat the vendors' refusal behaviour as neutral, and the song-lyrics example is a concrete over-refusal claim. But he does not measure. The tilt is asserted, and the counter-claim (no capability cost) rests on a chart not read on tape. Removing refusals is itself a tilt, and nothing on tape measures its direction or size beyond *now answers*. *RLHF* is never said (0 hits); "refusals" is his word. | Tape `[VERIFIED]`; mapping `[HYP]` |
| M4 | "And they're not going to stop. They're going to do anything you tell them to do."; "when the agent is blocked by something it will tell you what's blocking it and how to fix it" | **Defer must be an available gate outcome** (distinct from refuse and from comply) | **Divergence.** Refusal removal collapses the gate to *comply*. The tape treats the vendor's refusal and *sabotage* as one category, and offers no third option. The only defer-like behaviour on tape belongs to the *setup* agent (Opus reporting a block and what it needs) and to the human (finishing the captcha, choosing what to censor). In the tape's design, deferral lives with the operator and the frontier setup agent, never with the uncensored model. | Tape `[VERIFIED]`; mapping `[HYP]` |
| M5 | "That's why we're going to put in on a VPS, virtual private server, so it's properly isolated from your own machine"; "So, the agent actually never sees the API key" | Restraint built at the coupling layer (permissions, isolation, scoped credentials) | **Convergence.** This is the strongest part of the tape (§2): blast-radius limits and secret hygiene, with IP allow-list, 30-day expiry and $10 cap. These are constraints, not reasons. The house would want them *and* a reasons layer, and the tape supplies only the first. | Tape `[VERIFIED]`; convergence `[HYP]` |
| M6 | "the only way to defend yourself against a hacker who has 500 agents running in an agent swarm all with obliterated models"; "Now 2026 published 100,000 CVS in the first 322 days" | (defensive necessity argument) | **Internal friction.** On the same tape a frontier model secures the VPS, and he tells viewers to use a frontier model to fix the gaps. That undercuts *only way*. The CVE figures are read from an on-screen chart and are not checked here. | Quotes `[VERIFIED]`; figures unchecked; friction `[HYP]` |
| M7 | "So access to unrestricted models is almost like a human right"; "this is literally the second amendment of the digital era"; "use it with your own best judgment" | Restraint located in a relationship and a record, not in individual discretion alone | **Divergence (rhetorical).** Responsibility is placed wholly in the individual's judgment, with no record or counterparty. The house holds that judgment without a ledger cannot be audited. These are value claims, not demonstrations. | Tape `[VERIFIED]`; mapping `[HYP]` |
| M8 | Tape density | (coverage) | 8,656 words over 2,148 s ≈ 242 wpm; cue coverage not measurable | `[EST]` |

Two rows (**M1, M2**) are **CRITICAL DIVERGENCE**. M4, M6 and M7 carry further friction. Only M5 converges cleanly.

## 5. What is not claimed

- Not claimed: that OBLITERATUS, or any named abliteration tool, appears on the tape. It does not. Nor that *obliterated* is certainly *abliterated* (probable, `[HYP]`).
- Not claimed: any procedure for removing refusals beyond his one sentence. This drop adds none.
- Not claimed: the benchmark numbers, the CVE figures, the tweet anecdote, the attributed Sacks quote, the YouTube takedown, or that *Discord is compromised*. All are asserted on tape and none is verified here.
- Not claimed: whether Cloud Room is sponsored or owned by the creator. The tape says neither.
- Not claimed: the content of censored, blurred or off-camera outputs. This drop quotes no harmful prompt and no model output.
- The model names (Opus 5.5, GPT 6.2 Soul/Astra, Fable 5.2, Gemini 4 Neon, GLM 5.3, Deepseek V4.0/V4.1 Flash, Qwen 3.8) are recorded as spoken and not independently checked.

## 6. Receipts

- Quote gate (mechanical): covers single-line double-quoted spans from the H1 heading through §5. Each span was lowercased, stripped of punctuation, whitespace-collapsed and substring-tested against the identically normalised tape. **53 spans (49 distinct) checked, 49/49 verbatim, 0 missing.** All 49 also match the raw tape exactly (case- and punctuation-sensitive). Negative control (an invented sentence, *removing the refusal weights gives the model better reasons to say no*) was a **MISS, as required**. Positive control (*thank you Hostinger for sponsoring this video*) was a HIT.
- `canon_drop_lint.py`: run on this file after filing. The result is recorded in the index row.
- Local only: no GitHub push, no NotebookLM, no audio. Index backed up to `CANON_INDEX.md.bak-20261126-ondrej-uncensored` before the row was appended.
