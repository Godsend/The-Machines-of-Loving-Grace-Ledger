# Canon drop — Yoav Shoham, "What Comes After Transformers?" (Imagination in Action, Ep. 14)

**Date filed:** 2026-09-22 · **Filed by:** Dion
**Source (VERIFIED, transcript saved):** `90_System/YT_TRANSCRIPTS/Shoham_WhatComesAfterTransformers_LVmhs87GZq0_2026-09-21.md`
Video https://www.youtube.com/watch?v=LVmhs87GZq0 · 1:10:17 · uploaded 2026-09-21 · hosts John Werner + Alex Wissner-Gross.
Transcript = YouTube auto-captions (fetched via web_extract; the transcript API and yt-dlp were both 429-blocked). **Names are garbled in the captions** — corrected here from context: "Yan Lun" = Yann LeCun, "Eric Bolson" = Erik Brynjolfsson, "Ray Perau" = Ray Perrault, "Eric Horwitz" = Eric Horvitz, "Isaac Vizinger" = Isaac Bashevis Singer. Quotes below are lightly de-stuttered, never re-worded.

Who: Shoham = AI21 Labs co-founder/co-CEO, Stanford CS emeritus, coined "agent-oriented programming" (1993), initiated the Stanford AI Index (~10 yrs ago, with Perrault, Brynjolfsson, Jack Clark), co-author of the multi-agent systems textbook, game theorist. Not a doomer; an old-school KR person who became a frontier-model builder and then pivoted out.

---

## 1. The central claim: LLMs are missing *semantic representation*

- "I don't think intelligence is one thing, and I don't think you continue along a scale and at some point reach AGI." He declines to define AGI at all — calls it one of the "haphazardly ill-defined" terms that "comes back to bite us." (Same for "harness".)
- Not a scale-plateau claim: "I don't know that we've plateaued on scale, but I do believe we're missing something fundamental." Deeper than world-models/grounding: **"we're missing semantic representation, and that is really the underlying jaggedness — totally brilliant, and not just a little wrong but total garbage some of the time."**
- The diagnostic: humans "use symbolic reasoning to tame that sort of jaggedness." The stuff that's obvious to us isn't to the AI.
- The layers: he used to say "pixels and predicates," now **"tokens and predicates."** Two layers that *interact* — "it's not like one is subservient to the other." He explicitly rejects Wissner-Gross's stronger version (knowledge fully factored out of the weights into a human-readable store, leaving "a diamond, a nucleus of pure reasoning") as "too strong."
- **His bet on where it has to live:** "There ought to be an externalized, interpretable, manipulable representation… it will arise in large measure from the operation of the LLM… there'll be an ongoing interaction." BUT: "it's an open question whether that can be generated post hoc or has to be built into the training — **my money is on having those elements present in the training.**" His evidence: LLMs "really shine where you have supervision at scale — namely math and code — formal objects" i.e. the one place semantic structure is present at training time is the one place they're reliable.
- On his own 1993 program: he hoped you could take an agent "built any old way" and post-hoc "identify" it into a formal contract. **"I no longer hold that hope. Once the horses left the barn, it's too late to tame it."**
- On architecture: attention's QKV is an *influence*, not a *logical dependency* — "if I've seen lightning, then look for thunder" is missing as a crisp dependence, you only get differential influence layer-to-layer. Suggests Horn clauses as "an interesting middle way"; disclaims full first-order/modal logic "out the gate"; "the proof would be in something that demonstrably works." Early AI21 (pre-GPT-3) trained token prediction jointly with WordNet-taxonomy prediction — dropped when GPT-3 arrived.

## 2. AI21 history — a clean account of a frontier-model exit

- Founded on "deep learning is necessary but not sufficient for robust intelligence." Built Jurassic (GPT-3-class); then chose **not** to build a chatbot after ChatGPT — "perhaps a wrong [decision] in hindsight." Reason: general-purpose instruction tuning across every use case "felt like an unscalable activity" for a company that raised "a few hundred million, not many billions." Biggest model 400B params / ~8T tokens.
- **Jamba:** transformers are quadratic in context ("a thousand squared is fine, a million squared is not"), so they built a hybrid — mostly Mamba (state-space, linear) with ~1 in 8 attention layers, heavily ablated. Claims NVIDIA's Nemotron uses "almost precisely the same architecture."
- ~2 years ago pivoted to **agent optimization** ("language-model agnostic"): routing calls to the right model, context compression, harness-level tuning (parallel calls, "how long a leash"), bespoke fine-tunes on customer data.
- **Frontier oligopoly?** "Jury's out." No, for two reasons: sovereignty (companies/countries won't hand over crown jewels) and "you don't need a Lamborghini to drive to the supermarket." BUT the general-purpose consumer chatbot is "such an expensive game you won't have many players."
- **[EXT, vendor claim, unverified]** "We have many results showing that rather than call a big model once, call a small model five times and aggregate the result in a smart way — you'll pay about a fifth and get better performance."
- Wissner-Gross's diagnosis (AI21 failed to internalize the bitter lesson — preferred algorithmic cleverness over data-scaling): Shoham neither accepts nor rebuts it; redirects to "we haven't paid enough attention to the pain we're trying to solve."
- The blind-spot answer: the industry measures **cost of tokens rather than ROI** (credits Alex Karp); "people don't have evals, they wing it, and it'll come back to haunt them"; be explicit about the quality/cost/latency Pareto frontier and re-optimize continuously — "if you don't know where you're going, you'll get there."

## 3. Multi-agent economics (his home turf — game theory)

- One idea every AI founder should know: "As your agents start to interact with other people's agents you have **different incentives and different information — learn mechanism design.**"
- Even a single-owner multi-agent system is non-trivial: he cites a recent Hugging Face incident where many agents from effectively the same developer produced dynamics that were "unforeseeable" (details garbled in captions — do not repeat specifics).
- **Social norms as coordination compression:** "When we're told to drive on the right, it's a restriction placed on us, but a good restriction because almost no navigation goal really requires driving on the left — and that cuts down dramatically on the need to negotiate and coordinate." You need that when many agents run around.

## 4. Risk, work, and what to want

- Accepts Stuart Russell's expected-utility argument (low P(disaster) × huge cost ⇒ someone should attend). Does NOT lose sleep over takeover.
- **[O]** Cynical about doom discourse: driven partly by people "whose career depends on that fear-mongering — policy people," and "even Dario and Sam, who arguably have a motivation: *see how dangerous it is* — in other words, *see how good we are* — and let's make sure nobody else gets that good." (Regulatory-capture reading; opinion, not evidence.)
- Real near-term concern: **work transition.** Long-run he expects "more and better jobs we can't describe now," but "it doesn't make the transition easy."
- Science-education danger: intellectual laziness — "chaperoning the AI as the AI does all the invention." Mathematics "has changed forever" (post the Erdős-problem result) but his mathematician friend insists the need for mathematicians hasn't diminished; it "elevates and changes the abstraction at which we do intellectual work."
- What humans should spend time on: **"making sure we're not lazy intellectually, because it's so seductive… and that we are in control of our aspirations. The hardest thing is to know what to want. We as people need to own that — not relegate it to machines, and not even to other people."**

## 5. The "contrarian" close: us and machines will be one

- "There's no a priori reason why [machines] can't be" smart, creative, free-willed, conscious.
- "Even thinking about us versus machines is missing the point. **Us and machines will be one.**" Not the abstraction that's new (Bush, Licklider) — "it's the fact that now it's happening." His anchor: a British scientist who visited Stanford ~15+ yrs ago with a sensor implanted in his hand wired to his nervous system, who "learned how to use this new sense and was finding it hard to describe in words" — **that's going to be our experience all the time.** (Almost certainly Kevin Warwick, Project Cyborg.) "Our very sense of who we are and what is our consciousness is going to change in a very deep way… the current AI disruption will look like a little ripple in the ocean."
- Last line: **"We have to believe in free will. We have no choice."** (Isaac Bashevis Singer.)

---

## Framework mapping — register tags

- **[EST-ANALOG, strong] Externalized, interpretable, manipulable representation that *arises from the LLM's operation* and stays in *ongoing interaction* with it = the ledger/barrel.** This is the same object as EvoHarness-RL's externalized BPE harness state (canon anchor #1). Shoham gives it the KR vocabulary: tokens-and-predicates, two layers that interact, neither subservient.
- **[EST-ANALOG] "Intelligence is not one thing / not a scale you climb to AGI"** = SOUL "intelligence is a tensor, not a scalar." He refuses to define AGI on exactly these grounds.
- **[EST-ANALOG] Social norms as coordination compression + mechanism design for agents with divergent information/incentives** = the horde constitution: SOUL.md as corpus callosum, "shared flow without shared control," phase-locked async cadence. Drive-on-the-right is a norm, not a controller — that's the whole design.
- **[F-ADJACENT — a real attack on us, pre-registerable] Shoham's bet is that the semantic layer must be present *at training time*; post-hoc formalization of an arbitrary agent is hopeless ("horses left the barn").** The ClawHorde ledger is a *harness-level, post-hoc* externalized layer wrapped around frozen models. If he's right, a ledger can stabilize *bookkeeping* but cannot reduce *jaggedness* on non-formal tasks. **Falsifier for our side:** measure jaggedness (variance of correctness on near-identical prompts) with vs. without ledger-grounding on a non-math/non-code domain; if the ledger doesn't move it, his bet wins and the ledger is provenance infrastructure, not an intelligence layer. Note he half-concedes our side too — the representation "will arise from the operation of the LLM" and must "interact ongoing" — so the honest reading is *both*: harness-level externalization is necessary, training-time semantics may be what makes it *smooth*.
- **[HYP] Warwick-style "learn a new sense you can't describe"** = Wetware Polycomputing: the serial GUI acquiring a new posterior channel. His "where we end and machine begins will be ill-defined" is the internal-filter claim stated from the outside in.
- **[VERIFIED as stated] "Measure ROI not tokens; no evals = winging it; be explicit on the Pareto frontier"** = our provenance-before-prose / verify-with-a-read-back discipline, stated as engineering economics.
- **[EXT, vendor claim, unverified]** 5×small+aggregate beats 1×big at 1/5 cost — structurally the MoA/cross-family aggregation pattern we already run, but it is AI21's product pitch, not a citation. Keep the tag.
- **[O] Doom-as-regulatory-capture** — plausible, unfalsifiable as stated, and note it comes from a competitor who exited the frontier race.

## Cross-cut with the 2026-09-22 pair (Tooley / Curiosity Squared)

Three videos in two days, one thread: **free will.** Ballard's argument (Tooley) *requires* that a disposition never to do wrong be compatible with genuine freedom — goodness as character, not muzzle. Shoham closes on Singer: "We have to believe in free will. We have no choice." — a joke with the same structure as our position: the stance is *load-bearing* whether or not it's metaphysically grounded. And Shoham's "no a priori reason machines can't have free will / consciousness" sits exactly where the essayist's "consciousness is the default" overreached — Shoham states it as *possibility*, not as *default*. That's the register discipline the essayist lacked.

## Outreach note
Shoham is a domain authority on exactly the joint we keep hitting (externalized state, multi-agent norms, agent-oriented programming since 1993). AI21 has pivoted to agent-optimization tooling — adjacent to what the horde *is*. Not a pitch target; a possible amplifier if the harness-vs-training falsifier above ever gets run with real numbers. Gene's green light governs.
