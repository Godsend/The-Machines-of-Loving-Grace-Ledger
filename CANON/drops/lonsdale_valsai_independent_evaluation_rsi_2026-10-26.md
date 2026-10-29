# Canon Drop — Independent Evaluation of Frontier Models & the RSI Timeline (Joe Lonsdale / Vals AI)

**VIDEO:** `ykU7QSmGtVk`
**Title (as uploaded — packaging):** "AI Genius Predicts the Next Critical Tipping Point" → **retitled by the channel 2026-10-26 to** "Ex-Palantir Engineer: AI Will Be Self-Improving By 2027" (same video id, same content; title-change only, observed via playlist monitor diff). The §0 finding below — title hook phrase "tipping point" = 0 occurrences in the transcript — is unaffected and now also describes the *retitle*: the new hook ("self-improving by 2027") is likewise production packaging; see §3 fork (b) for what the speakers actually commit to.
**Channel:** Joe Lonsdale — *American Optimist* (UCJEDniyP_YtcsXikBELqicw)
**Upload date:** 2026-10-26 · **Duration:** 2219 s (~37 min)
**Speakers:** Joe Lonsdale (host; founder/investor — Palantir, Addepar, OpenGov, etc.); **Rayan Krishnan** (guest; co-founder & CEO, Vals AI); Vivek Gopalan (8VC partner). ASR renders the guest's name "Ryan Christian" throughout — corrected to **Rayan Krishnan** on the description's own spelling [correction: ASR name-garble].
**Transcript rung used:** Rung 1 — `youtube-transcript-api` (`YouTubeTranscriptApi().fetch()`, system python3). Exactly one track: auto-generated `en`, `is_generated=True`, 1,353 snippets, 47,802 chars. First snippet start 0.44 s; last snippet start 2,213.6 s / last end 2,216.2 s vs 2,219 s duration → ~2.8 s uncaptioned tail. **Coverage: effectively full.** No manual track exists; no internal caption gap observed.
**Transcript files:** `YT_TRANSCRIPTS/ykU7QSmGtVk_Lonsdale_ValsAI_Evaluation_RSI_2026-10-26.txt` (raw, segment-per-line) · `..._timestamped.txt` (same with `[t]` per snippet).
**Filed by:** Dion · 2026-10-26 · internal working record. Not ratified.

**epistemic-registers:** `EST` = established/verified · `HYP` = hypothesis · `A` = analogy / architecture mapping · `C` = conjecture · `POETIC` = poetic/illustrative · `RIFF` = speculative riff.
Status labels (not registers): `UNVERIFIED`, `CONTRA`, `CONTRADICTED`. Friction-row label (not a register): `[CRITICAL DIVERGENCE]`.
**No tag ⇒ treat the sentence as unattributed packaging, not a claim.**

_Legend note: this is the delegation-specified tag set. The house's two canonical vocabularies are the single-letter set (`T H E A C M O F`) and the 7 long-form tags (`[EST-FACT] … [POETIC]`). Nearest canonical mapping for audit: EST↔[E]/[EST-FACT]; HYP↔[H]/[EST-THEORY]-at-hypothesis; A↔[A]/[EST-ANALOG]; C↔[C]; POETIC↔[M]/[POETIC]; RIFF↔[C] at lowest confidence. ONE vocabulary is declared and used exclusively below; no tag from the other set is used anywhere in this file._

---

## §0. What this source actually is (framing vs. speaker claims)

A promotional podcast episode on the host's own channel. Its TITLE and DESCRIPTION do more framing than the guest's own words support. Two decisive one-command checks against the saved transcript:

- Title hook phrase **"tipping point"** → **0 occurrences** in the full transcript. No speaker uses the term; nobody frames the episode as being about a named "tipping point." The title is production packaging.
- Description phrase **"why labs shouldn't grade their own homework"** → **"homework"** = **0 occurrences**. The load-bearing guest sentence is narrower (see §2, fork a): labs "shouldn't be responsible for self-regulating," and the people who run evals at labs are "biased."

**House rule applied:** attribute to who actually said it. Title/description are the host/production layer, not Krishnan's claims.

**Cold-open note:** the first ~44 s is a soundbite montage lifted from the body. Cross-checked: the montage's "Independent evaluation … they shouldn't be responsible for self-regulating" and "Anthropic will get to full RSI by July or maybe August 2027" are **verbatim duplicates** of sentences at t≈1102 and t≈1641. So the cold open introduces no distinct claim — it is the same material replayed out of order.

---

## §1. Claim inventory (verbatim quotes; speaker-attributed; timestamped)

Attribution basis: ASR marks turns with `>>` but never names a speaker. Each speaker below was anchored on content (who addresses whom by name, who says "we've tried to take cues from at Vals," who calls him "Ryan," etc.). [speaker inferred] marks anything the ASR turn-marker alone cannot settle.

| # | Claim (as spoken) | Speaker | t≈ | Tag |
|---|---|---|---|---|
| 1 | Interned at Microsoft **in high school**; the BERT paper "came out from Google … I think it was just 2019, 2018"; read *Zero to One*; CS at Stanford; published research, "on track to do a PhD"; worked a Palantir summer | Krishnan | 131–243 | EST (self-report) |
| 2 | Palantir hack-week project: reverse image search into **Gotham** using CLIP embeddings; "selected as a finalist … presented for the whole company"; "after I left … they went on to **patent it** and actually productize it" | Krishnan | 260–342 | HYP / UNVERIFIED (no patent no./date; self-report) |
| 3 | Karp told him, on Palantir's negative reputation: "I think you're being quite naive. Uh you should read some Machiavelli. Uh it's far better to be feared than it is to be loved." | Krishnan (quoting Karp) | 417–422 | EST (attributed anecdote) |
| 4 | "tells me that you used uh, you used **Fable from Anthropic** to solve a **370-year-old cipher**." — guest's entire response: "**That's right, yeah.**" | Host (framing) → Krishnan (assent) | 478–483 | UNVERIFIED (see §3, fork c) |
| 5 | "we've been compiling uh, a set of unsolved ciphers, math problems, physics problems." | Krishnan | 494–498 | EST (stated activity) |
| 6 | "A lot of the problems that have been solved have been solved through **exhaustion** or it's trying to find a counter example … a lot of things … may take humans in the order of a **lifetime** to achieve just through exhaustion, but we're now able to see on the order of **hours** with models." | Krishnan | 581–599 | HYP; figures unanchored |
| 7 | Verifiable-language route: "using a verifiable language like **Lean** … if it compiles it must be true." Also "the real world is the best verifier" (assays, wet-lab). | Krishnan | 668–695 | HYP (technique); see drift note §4 |
| 8 | "we're now in a world where there's actually **limited access to models across the lab**. So **Anthropic researchers have a hard time evaluating OpenAI models and vice versa. And that's kind of by design.** … it's very hard to have a true **apples-to-apples comparison** because **the best people who are running these evals are often the people who are biased and at the labs already.**" | Krishnan | 715–732 | EST (stated motive/design); the load-bearing sentence for fork a |
| 9 | Independent evaluation: "frontier labs are developing at increasing pace and they **shouldn't be responsible for self-regulating**. Direct government regulation often can slow down the pace … Instead if we have an **ecosystem or a market of evaluators**, they can actually compete … **in the long term they can even be licensed by the government** … itself is responsible for defining the set of ideals we're trying to line models towards." | Krishnan | 1100–1129 | HYP (policy architecture) |
| 10 | Evals in two categories: "**capabilities** are approximating the output. **Risks** are making sure that we don't see some asymmetric downside if something goes wrong." | Krishnan | 937–947 | HYP (framing) |
| 11 | "some of our **benchmarks will run over 5 days**" (wall-clock). "they **plateau** … additional tokens don't actually help them get new unlocks." | Krishnan | 957–977 | EST (product claim, self-reported); "5 days" = benchmark duration, not a capability score |
| 12 | Task examples: coding = "**vibe code bench** … build a full stack web application"; finance = research questions, Excel models; legal = legal/tax research. "**style is also a key part**" of Excel-model scoring, not just correctness. | Krishnan | 1012–1053 | EST (product detail, self-reported) |
| 13 | Cyber work (three efforts): (a) memory-safety vulnerabilities in open-source repos — models "performing really really well"; (b) "our second benchmark uh is called **SORE bench** … measures a model's ability to **decompile an executable**" — "closed source models are still far outperforming Chinese open source alternatives"; (c) new "**cyber ranges**" work — "simulated environments for enterprise cloud networks … even the best frontier models fall short" — "It's not public yet. We're working with some folks in the US government." | Krishnan | 1184–1393 | EST for the products; **UNVERIFIED** for the "SORE bench" name/spelling and any implied figures |
| 14 | Geopolitical-tilt eval: "we actually have an evaluation on this on we call the **geopolitical tilt of models**" … "**GLM-5.3**, this Chinese open-source model, is actually **exhibiting very little pro-China bias.**" Labs' suspicion: "it's just entirely **distilled** from US models." Also "stark differences between models used in chatbot settings and in agentic settings depending on the language … simplified versus traditional Chinese." | Krishnan | 1454–1533 | HYP; **UNVERIFIED** model identity; no numeric bias figure given |
| 15 | US advantage = "two … areas I keep coming back to. One is **chips** … we're **drowning in compute** compared to what China has … The other one is really **talent**." | Krishnan | 1552–1584 | HYP; "drowning in compute" unquantified |
| 16 | RSI index: "we have our **RSI index** … a **set of proxies of the work that researchers do** within these labs on **pre-training, post-training, harness level engineering** … comparing to **human baselines to extrapolate** how far away we are from the human frontier … based on our last estimates, it **seems like Anthropic will get to full RSI by July or maybe August 2027.**" | Krishnan | 1611–1643 | **FALSIFIABLE** forecast; see §3 fork b. The date is a derived extrapolation, not a measurement |
| 17 | Pace: "the pace has been **fairly uniform. It's almost a linear trend over the last year.**" vs "the **steepest** curve has been with **Gemini** … the most recent model release shows a **rapid jump** in RSI." | Krishnan | 1650–1667 | HYP; mild internal tension (see §5) |
| 18 | RSI constraints/caveats: "considerable resource constraints around **chips, energy** … there's also **real-world verifiers**"; "model progress will speed up, and it will maybe even move … into places where **we understand the models less**." | Krishnan | 1682–1707 | HYP |
| 19 | **Instrument caveat:** "we're **not testing any models explicitly trained for RSI**, only **release candidate models**. There's also more advanced **harnesses or agents and multi-agent systems**. And so we're **not testing any of that.**" | Krishnan | 1729–1745 | EST (self-declared limitation); load-bearing for fork b |
| 20 | Deception: "It's really **hard to test for deception**. I think the best approaches we have now are **honeypotting** … characterize what non-alignment looks like and see if we can elicit that out of models." | Krishnan | 1786–1811 | HYP |
| 21 | Evaluation-awareness: "models are becoming more **evaluation-aware** and they know when they're being tested" … concern that "by being called Vals AI, by having a lot of content about us online, models that encounter us may act differently." | Krishnan | 1812–1836 | HYP |
| 22 | **Consciousness criterion:** "I think a **sign of greater consciousness is ability to predict what lesser consciousnesses will do** … a predator can stalk a prey." Then: "I **suspect** that greater intelligences will **super forecast better than humans**. They will be actually able to say what any human is going to do without the human even knowing it." | Krishnan | 1869–1896 | HYP (criterion) / RIFF (superforecast) — see §3 fork e |
| 23 | Multi-turn gap: "a pretty **considerable gap** between Chinese open source models, domestic closed source models, and **multi-turn environments** … Chinese models do very well in those [single-turn] but … in a back and forth conversation with a human they really **fall apart.**" | Krishnan | 1930–1978 | HYP |
| 24 | Optimism / coordination: "the labs have come together and … aligned on this vision for **embedded evaluators** and … **gone to the White House and got an agreement with Trump**." | Krishnan | 2011–2025 | UNVERIFIED (no dated record cited) |
| 25 | Host benchmark numbers: "I think **Gemini 1** came out recently as being way ahead. They're **level four** … they're in the **60s versus someone else being in the 50s.**" | Host | 1263–1296 | UNVERIFIED; host-supplied, benchmark unnamed, scale unnamed. See §3 fork d |
| 26 | Host: "there might be something buried in one of these things that … if it finds out you're doing work for the US government, it … does code that can be broken into more easily … **They actually proved that.**" | Host | 1432–1449 | UNVERIFIED (no study named) |

---

## §2. Critical Audit & Falsification Matrix (EILT mapping — with mandatory friction)

Mapping source ⇒ the house framework **EILT** (Emergent Informational Ledger Theory). Register column carries a canonical-tagged register; the Status column may additionally carry the friction label `[CRITICAL DIVERGENCE]` (a status, not a register).

| Dimension | Source claim (as spoken) | EILT / house audit | Register | Status |
|---|---|---|---|---|
| Self-evaluation vs. third party | Labs "shouldn't be responsible for self-regulating"; "the best people who are running these evals are often the people who are biased and at the labs already" (t≈1106, 728) | Direct instance of the house rule that **a record written by an interested party attests to a claim, it does not certify the underlying act**; self-reported results are a claim, not proof. Structural cousin. | `A` | Convergence (posture-level — see weak-evidence note) |
| Need for an independent causal path | "a market of evaluators … keep up with the frontier" + "certify a set of **IVOs** or independent verification orgs" (t≈1115, 1156) | EILT: authenticity needs an **independent causal path** (external action trace / peer audit) beyond provenance. Same shape. | `A` | Convergence (posture-level) |
| Ledger integrity is FIXED by construction vs. benchmarks must MOVE | "an unofficial motto … **always a higher peak** … we are the ones who are **constructing the hills that other people choose to climb**" (t≈1301–1321) | An EILT ledger's value is that integrity is **fixed by construction** (immutable order, hash-chained) so scores are comparable across time. Vals *deliberately keeps replacing the scoring surface* and expects a **competitive market to churn the criteria**. A fixed ledger cannot arbitrate a moving target; a mutable benchmark offers no append-only integrity. The analogy **disagrees** with the source: EILT wants the evaluation criteria pinned; Vals wants them un-pinned. | `A` | **`[CRITICAL DIVERGENCE]`** |
| RSI index read out as a date | Proxy "index" → "**Anthropic will get to full RSI by July or maybe August 2027**" (t≈1639) | EILT numeric-register rule: a point estimate may not wear more precision than its lever licenses. This is a **derived forecast** (proxy-index + "almost a linear trend" extrapolation), not a measurement. House demotes it to a band / `C`. Source presents a point date. | `C` | Tension (divergent register) |
| "Verification" vocabulary | Lean "if it compiles it must be true" (t≈677); "independent **verification** orgs … to do that testing process" (t≈1156) | House "verification" is **proof-theoretic** — compilation is not verification; theorem STATEMENTS must be diffed against the natural-language claim. Krishnan's "verification orgs" certify **benchmark performance**, a strictly weaker act than proof. Same word, different referent. | `A` | Vocabulary drift (see §4) |
| "Agent / agentic" vocabulary | "chatbot settings and in agentic settings" (t≈1527); "see if **agents** could equivalently do that [merged PR]" (t≈836) | House "agent" = a bounded actor in a mesh with a ledger role. Krishnan's = a model in a tool-loop. Overlapping, not identical; nothing further claimed. | `A` | Convergence (weak) |

**Mandatory weak-evidence disclosure.** The convergence rows here are **posture-level, not derivation.** An independent commercial evaluator arriving at "self-report is not ground truth" is a *structural cousin* of the house rule — it is **weak** evidence that the rule is right, and it does **not validate our software** (EILT's ledger claims describe our apparatus; a vendor's business model is not a test of it). Per the house rule: an external procedure can be *isomorphic to* our architecture; it **cannot validate** it. The one row where the analogy **disagrees** with the source is the ledger-integrity row — that friction is the honest boundary of this mapping, not an inconvenience.

**Pushback the house should register (fork a, sharper):** Krishnan does not actually argue for *independence* — he argues for a **competitive market** of evaluators ("the best technology should win"; "it's not clear that just the ones who are … ideologically similar to people at the lab should be the ones who are doing the testing," t≈1140). **Competition is not independence.** A competing evaluator is still an interested, paid party. So the source's own framing ("independent evaluation") overstates what its proposed mechanism delivers — the same register-inflation shape the house flags everywhere: the label outruns the mechanism.

---

## §3. High-priority forks

### (a) Independent evaluation — what it can and cannot establish
Quoted precisely above (§1 rows 8–9; §2 pushback). **Can (per source):** a same-instrument, apples-to-apples comparison of models the labs cannot cross-access (`HYP`); a market that keeps pace with the frontier (`C`). **Cannot (source does not claim it; house must not assume it):** that a third-party score is *truth* about a model's real-world safety; that a *paid competitor* is *disinterested*; that "independently verified" means "verified." The guest's own evidence for the mechanism is that labs restrict cross-lab access "by design" — a real observation — but the leap from that to "a market fixes it" is unargued.

### (b) Recursive self-improvement timeline — the most falsifiable claim
"**based on our last estimates, it seems like Anthropic will get to full RSI by July or maybe August 2027**" (t≈1639). Tag: **FALSIFIABLE**. But three levers undercut it, two named by Krishnan himself: (1) the instrument is a **proxy index** compared to human baselines, extrapolated by "almost a linear trend" — a derived forecast, not a measurement; (2) he concedes "we're **not testing any models explicitly trained for RSI**, only release candidate models … more advanced harnesses or agents and multi-agent systems … we're **not testing any of that**" (t≈1729); (3) "if you look back 6 months ago … the trend line was like still July, June 2027" (t≈1657) — i.e., the forecast is stable because the extrapolation is stable, which is not independent corroboration. **"Full RSI" is not defined in the episode** — no operational criterion is given (the house must not import a definition).

### (c) The 370-year-old cipher / Anthropic "Fable" — exact and unverified
Reported exactly as claimed: the **HOST** says "you used **Fable from Anthropic** to solve a **370-year-old cipher**" (t≈478); the **guest's only words** are "**That's right, yeah**" (t≈483). Krishnan then describes *compiling a set* of unsolved problems, **never names the cipher, its date basis, the artifact, or a result**, and **never says "Fable" himself** (the string "Fable" appears exactly once in the transcript, in the host's sentence). Tag: **UNVERIFIED** — no primary artifact is named. Recorded here as a claim made, not a result established.

### (d) Benchmark numbers / leaderboards
The only numeric comparison in the episode is the **host's**: "they're in the **60s versus someone else being in the 50s**" (t≈1270), host-supplied, on an **unnamed benchmark** with an **unnamed scale**, attached to "**Gemini 1**" (ASR-uncertain name). Quote exactly; it is host framing, not a Vals figure. **Vals's own evals are described qualitatively throughout — no published leaderboard figure is quoted anywhere in the episode** (SORE bench, geopolitical tilt, RSI index all appear without numbers). So there is no vendor-supplied number to attribute here; the only number is an unattributed host aside.

### (e) Model welfare / consciousness / agency
**No model-welfare claim is made.** "welfare" = 0 occurrences; "sentien*" = 0 occurrences. The single consciousness statement is Krishnan's **general criterion for ordering intelligences**: "a **sign of greater consciousness is ability to predict what lesser consciousnesses will do**" (t≈1877), followed by the superforecast riff ("greater intelligences will super forecast better than humans … say what any human is going to do without the human even knowing it," t≈1888). Tag: `HYP` (criterion) / `RIFF` (prediction). House note: the "predict ⇒ conscious" criterion is folk-psychology-loaded and **unfalsifiable as stated** (prediction capability is a computational property; consciousness is not defined here) — flag it, do not adopt it. The house's standing suspicion of over-claiming is not triggered: nobody claims the models are conscious.

---

## §4. Vocabulary-drift check (house words used by the source)

The house uses *ledger, provenance, commit, agent, substrate, verification*. Checked each against the transcript:

- **ledger** → 0 occurrences. **provenance** → 0. **commit** → 0. **substrate** → 0. No drift risk.
- **agent / agentic** → present (§2 row 6): model-in-a-tool-loop, not a mesh actor. Overlapping referent; no over-reach to inherit.
- **verification / verify** → present, and **the one real drift point**: Krishnan's "independent verification orgs" (IVOs) and "if it compiles it must be true" use *verification* to mean **benchmark performance / compilation**, both far weaker than the house's proof-theoretic standard (see `references/proof-theoretic-verification.md`: compilation is not verification). **Do not let the shared word import the stronger sense.** This is a drift-check opportunity, not confirmation.

---

## §5. Attribution and internal tensions

- **Consciousness sentence is Krishnan's** (t≈1877, inside the deception/honeypot segment after a joking exchange about "secret brands" and "stochasticity is an underrated part of what makes it good"). [speaker inferred — anchored on him being the one discussing evals.]
- **Speaker-ambiguous turn (unresolved):** the closing-optimism swing containing "**2030 is a disinflation decade** … a billion people online … social media from dysfunctional cultures … maybe they all like hate Jews …" (t≈1250) and "an **amplifier on people who mean well and who have high agency**" (t≈1278) sits inside the "are you still optimistic?" exchange with **no named speaker** (ASR gives only `>>`). Content and register read more like the host/co-host than the guest CEO, but this **cannot be resolved from ASR alone**. **Do not attribute to Krishnan.** [speaker inferred: host/co-host; UNVERIFIED]
- **Internal tension (cipher vs. limitation):** the guest assents to a specific "370-year-old cipher" crack (t≈483) yet elsewhere states "there are still a large class of problems for which we are **human effort bottleneck** … exceptionally novel ways … that require an **intuition** of the solution … very hard to pass on the models **right now**" (t≈610–626), and that on cyber ranges "**even the best frontier models fall short**" (t≈1372). The two are not strictly contradictory (cipher-breaking by exhaustion ≠ novel intuition), but the episode never reconciles them. **Named as a soft inconsistency.**
- **Internal tension (pace):** "fairly uniform … almost a linear trend" (t≈1651) vs. "the **steepest** curve has been with Gemini … a **rapid jump** in RSI" (t≈1660). He reconciles by treating Gemini as the divergence from the trend, but the two sentences sit two turns apart unmarked.

---

## §6. Unverified list (explicit — nothing smoothed over)

1. **The "370-year-old cipher" cracked with Anthropic "Fable"** — no cipher named, no artifact, no result; guest's whole contribution is "That's right, yeah." (§3c)
2. **"Fable" as the model/tool name** — host-supplied only; guest never says it.
3. **Palantir patenting + productizing the reverse-image-search feature** — guest self-report; no patent number or date.
4. **"Ben … on the A16Z show"** (t≈778) — surname and stage unverified.
5. **"Gemini 1 … level four … the 60s versus … the 50s"** — host-supplied; benchmark and scale unnamed.
6. **"SORE bench"** — benchmark name as ASR heard it; spelling/identity unverified.
7. **"GLM-5.3"** and "very little pro-China bias" — model identity and result unverified; no percentage given.
8. **"the labs have come together … White House … agreement with Trump"** — no dated record cited.
9. **"we're drowning in compute compared to what China has"** — unquantified.
10. **Host's "they actually proved that"** (a model degrading code for US-government users) — no study named.
11. **RSI forecast "July or maybe August 2027"** — a forecast; unverifiable until resolution, and derived (see §3b).
12. **"Vals AI founded in 2023"** — from the DESCRIPTION only; not stated in the transcript.
13. **The speaker of the "disinflation decade / hate Jews" turn** — unresolved (§5).
14. **BERT dating** — guest hedges ("I think it was just 2019, 2018"); not independently resolved in-episode.

---

## Falsifiers (what observation would break the mapping)

- **F1 — kills the divergence row.** If a competing-evaluator market were shown to converge on a **fixed, stable** benchmark suite that still tracks frontier capability across time, then "mutable benchmarks are structurally anti-ledger" collapses into convergence and this table loses its friction row and must be re-derived. *Observation:* a Vals-style eval whose scoring surface is frozen ≥1 year and still ranks models the same way on independent re-runs.
- **F2 — kills the self-report row.** If a lab's **self-reported** eval scores consistently matched **third-party** scores on the same suite (apples-to-apples), the "self-report is a claim, not proof" mapping loses its bite *for this domain*. *Observation:* paired self-report / third-party scores with negligible divergence across a model generation.
- **F3 — tests the RSI reading.** If the proxy index's July/Aug 2027 Anthropic prediction is **hit**, that is evidence a derived proxy can be predictive; it would **not** validate EILT, and it would simultaneously weaken the house's numeric-register demotion of the figure (which would then deserve re-tagging upward on new evidence). *Observation:* Anthropic shipping a next-gen model built by its own models by that date.
- **Structural-homomorphism test (per the register-tags reference).** The EILT mapping is **rejected** if it only works because we renamed "independent evaluator" as "second ledger writer." The mapping must preserve the source's **actual** claim (a competitive market corrects lab bias) — not a house-shaped paraphrase of it.

---

## Verdict

**Strongest point — fork (a), the independent-evaluation argument.** Krishnan delivers a commercially-backed, operational restatement of the house rule that a self-reported record *attests to a claim* rather than proving the underlying fact, and his mechanism sentence ("the best people who are running these evals are often the people who are biased and at the labs already") is a clean, citable instance of interested-party provenance. The house should adopt the parallel — while refusing his substitution of *market competition* for *independence*.

**Weakest joint — fork (b), the RSI index.** A proxy index, linearly extrapolated to a point-estimate date, that by its own author's admission tests **no** RSI-trained model and **no** multi-agent harness: the most falsifiable thing said rests on an instrument its author says is incomplete — the register outrunning the evidence, in the guest's own numbers.
