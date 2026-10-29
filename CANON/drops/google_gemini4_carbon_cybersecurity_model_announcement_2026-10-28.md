---
epistemic-registers: EST=established fact (independently verified this pass) HYP=stated claim/hypothesis, not independently verified A=analogy/our reading (not the source's claim) C=conjecture POETIC=evocative/unfalsifiable RIFF=our extension beyond the source
rule: no tag = treat as MYTH (do not build on it). `[ATTACK SURFACE]`, `[CONTRADICTED]`, `[CRITICAL_DIVERGENCE]` / `[DIVERGENCE]` are status/friction labels, NOT registers — every claim still carries one of the six tags.
id: google_gemini4_carbon_cybersecurity_model_announcement_2026-10-28
canon-id: CANON-2026-10-28-GOOGLE-GEMINI4-CARBON
title: "Google DeepMind — 'Introducing Gemini 4 Carbon': a cybersecurity-defense frontier model launched into a restricted defender-only rollout; a vendor-self-report audit checked against the benchmarks' own leaderboards"
source: Google blog (OFFICIAL, vendor), https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ — published 2026-10-28, author **Koray Kavukcuoglu** (SVP, Google DeepMind & Chief AI Architect, Google). This is a vendor press release about Google's own model, NOT independent reporting.
date: 2026-10-28
filed-by: Dion (subagent research pass)
type: SOURCE DROP — present-day AI capability/safety + governance. Vendor self-report audit, with an independent benchmark-verification pass. Sibling to this week's Amodei/Anthropic, REA reverse-engineering and Aaronson/Yampolskiy items (same lane: present-day AI capability/governance news). NO EILT cosmology mapping forced — the source's own domain is product/governance, not the ledger's metaphysics layer.
status: v1.0-Working (Pre-Adversarial Review)
tags: [google-deepmind, gemini-4-carbon, gemini-4-argon, cybersecurity-defense, vendor-self-report, register-inflation, artificial-analysis-intelligence-index, sec-bench-pro, exploitgym, cwe-bench, gray-swan-ipi, webdev-arena, fairwind-program, us-caisi, pre-release-testing, present-day-capability, present-day-governance, safety-self-report, egress-guardrail-gap]
cross-refs:
  - berman_anthropic_s1_ipo_2026-10-27.md                              # the week's other vendor/lab commercial-timing story
  - diamandis_moonshots_ep306_anthropic_ipo_chain_theory_2026-10-28.md  # ditto (lab comms / commercial framing lane)
  - openai_eth_disproof_wesroth_2026-10-27.md                          # vendor over-claim vs independent check (ETH as-claim/[HYP]-as-result pattern)
  - aaronson_roman_forum_math_unsolved_problems_2026-10-27.md          # same vendor-hype vs source-hedge discipline, wrapper-side inflation
  - ai_revolution_news_roundup_singularity_quantum_argon_2026-10-27.md  # prior mention of the Gemini 4 family / Argon in canon
---

# Canon Drop — Google DeepMind, "Introducing Gemini 4 Carbon" (vendor self-report audit)

## 0. Provenance and method

- [EST] **Source re-extracted in full this pass** (`web_extract` of the official blog URL) and read
  end-to-end. The parent brief's summary of the post **matches the extracted text on every figure**
  (AA index 59; SEC-bench Pro 88.2%; ExploitGym 54.8%; CWE-bench 71.0%; WebDev Arena +89 → #4 1768;
  Terminal-Bench 4.0 cheating 0.0% / attempts 0.4%; ~80% misalignment-alert drop; ~2x unsupported-claims
  cut; Gray Swan IPI 0.0% vs Argon 0.7%; Fairwind; US pre-release testing; $2/$10 → $4/$20). No
  discrepancy between brief and source.
- [EST] **Source class: vendor press release.** Every capability and safety number in the post is
  Google's own claim about Google's own model. This is the exact class the house's standing rule
  covers — *a vendor's own claims about their own product/safety, especially right before a
  commercial rollout, get the same scrutiny as any other self-interested source.* The post is
  Google-selected on every axis: which benchmarks, which configs, which internal metrics, which
  partners to quote.
- [EST] **Independent verification pass run this pass** (`web_extract` + `web_search` reads of the
  primary benchmark sites themselves, not of write-ups about them): Artificial Analysis (AA index
  page + changelog), sec-bench.github.io, github.com/sunblaze-ucb/exploitgym, cwe-bench.com,
  grayswan.ai (IPI blog + solutions page), arena.ai WebDev leaderboard, deepmind.google/fairwind-program,
  plus independent reporting: Reuters/Fidelity, MarketWatch, the-decoder, marktechpost, aiweekly,
  rdworldonline, startuphub, 9to5google, interestingengineering, techtimes, and three independent
  third-party Argon security evals (averlon.ai, simbian.ai, apidog). Results in §4 and §7.
- [EST] **Duplicate check: first Gemini 4 Carbon drop in canon.** `grep` over `Canon/drops/*.md` +
  `CANON_INDEX.md` for `Gemini 4 Carbon` / `introducing-gemini-4-carbon` = **0 pre-existing drops**
  (only incidental family mentions). The Gemini 4 **Argon** family appears only in the 2026-10-27
  AI-news roundup. This is the first filing on Carbon.

---

## 1. Bottom line (verdict up front)

- [EST] **This is a standard frontier-model product announcement wearing a cybersecurity-defense
  costume — and the costume is the genuinely newsworthy part, not the model.** Structurally it is
  routine: a follow-on to a model released **15 days earlier**, the **same** introductory price as
  its predecessor, the usual benchmark-leaderboard claims, and "coming soon to developers,
  businesses, and consumers." What is *not* routine is the **release posture**: headline positioning
  is cyber **defense** (find/validate/patch vulnerabilities), and initial access goes to a vetted
  **defender cohort via Google's own Fairwind Program**, with engagement in the **U.S. government's
  voluntary pre-release testing process**, ahead of any public availability.
- [HYP] → downgraded further: **almost everything Google says about *how well Carbon does* is a
  self-report, and the pass could independently corroborate only half of the benchmark headline.**
  Of the six named external benchmarks, **3 are corroborated on the benchmark's own leaderboard**
  (AA Intelligence Index #1 @ 59; CWE-bench 71%; WebDev Arena #4 @ 1768) and **3 are not**
  (SEC-bench Pro 88.2%; ExploitGym 54.8%; Gray Swan IPI 0.0%). **Every one of the alignment/safety
  metrics is self-reported and uncorroborated** — 0 of ~5 check out. See §4, §3.
- [ATTACK SURFACE] **The single sharpest independent-vs-claim gap: SEC-bench Pro.** Google's headline
  vulnerability-discovery number is **88.2%**, but as extracted this pass the SEC-bench Pro public
  leaderboard's **top published score is 58.4%** (GPT-5.5 xhigh/Codex, 201/344) and **does not list
  Gemini 4 Carbon at all.** A ~30-point gap. This may be a newer/unpublished benchmark version or
  config (unverified), so it is flagged as a **discrepancy, not asserted as a contradiction** — but
  it is exactly the kind of headline that should not be relayed as "Carbon scores 88.2% on
  SEC-bench Pro" when the benchmark's own board says otherwise.
- [A] **The most notable single claim in the whole announcement is the alignment block, and
  specifically the Gray Swan 0.0%.** It is the strongest possible safety claim ("resisting *every*
  evaluated attack attempt"), it is **self-reported against an undisclosed evaluation config**, and
  it sits in **direct tension with the benchmark-maker's own published finding** that across the
  largest IPI competition ever run, **"No model was immune"** and models "kept getting broken at a
  roughly constant rate… no sign of a plateau." See §3, §4f.

---

## 2. Capability claims — register table

| # | Claim (as stated by Google) | Register | Basis / this-pass check |
|---|---|---|---|
| C1 | Gemini 4 Carbon is Google's newest frontier model, follow-on to Gemini 4 Argon (released "two weeks ago") | **[EST]** | Argon blog dated **2026-10-13** → Carbon 2026-10-28 = **15 days**. Reuters, MarketWatch, 9to5google all say "two weeks after Argon." Timeline checks. |
| C2 | #1 on Artificial Analysis Intelligence Index **v5.0** at score **59** | **[EST]** | AA's *own* leaderboard + changelog: "Gemini 4 Carbon is the new #1 … score of 59," ahead of Claude Opus 5.5 (58). Independently run by AA (§4a). |
| C3 | SEC-bench Pro **88.2%** (finding vulnerabilities) | **[HYP]** `[ATTACK SURFACE]` | Benchmark real (§4b) but **not corroborated**; public leaderboard top = 58.4%, Carbon absent. Vendor self-report at best. |
| C4 | ExploitGym **54.8%** (exploitation validation), "new state-of-the-art" | **[HYP]** | Benchmark real (§4c) but leaderboard values **not located** this pass; number unverified. |
| C5 | CWE-bench **71.0%** (patching), "firm lead" | **[EST]** | CWE-bench's own leaderboard shows **Gemini 4 Carbon 71% programmatic pass@1, rank #1** (§4d). Caveat: the "firm lead" is **+3** over a three-way tie cluster (Argon/Grok 4.7/GPT-6 Astra all 68%). |
| C6 | WebDev Arena **+89 Elo → #4 (1768)** | **[EST]** | arena.ai board shows **Gemini 4 Carbon (High), rank #4, 1768** (preliminary); Argon at 1679 → the +89 checks (§4e). (9to5google prints 1769 — off-by-one typo.) |
| C7 | "Runs for days" through dead ends on multi-step engineering tasks (internal) | **[HYP]** | Google-internal observation; no external trace. |
| C8 | Chrome team: Carbon **>10x better than "another lab's large frontier model"** at patching | **[HYP]** | Google's own team; **rival unnamed**; no methodology. Self-interested, non-checkable. |
| C9 | **Wiz** observes Carbon leading on web-pentest benchmarks (Scan for Good) | **[HYP]** `[ATTACK SURFACE]` | The post itself calls Wiz **"our leading Cloud security platform"** — i.e. a **Google-owned subsidiary**, so this is an *internal* endorsement dressed as third-party corroboration. |
| C10 | On internal benchmarks, **>2x uplift** in generating secure code vs Argon | **[HYP]** | Google-internal. |

---

## 3. Alignment / safety claims — register table (the register-discipline core)

**Every claim in this block is Google's own, measured by Google's own testing, about Google's own
newest model, immediately before a commercial rollout.** Per the house rule, none inherits a
stronger tag than `[HYP]` absent independent replication. The post itself flags that the *external
cyber* evals were run **"without guardrails"** — a condition that explicitly does **not** describe
the shipped, guarded product.

| # | Claim (as stated by Google) | Register | Basis / this-pass check |
|---|---|---|---|
| S1 | **Successful cheating on Terminal-Bench 4.0 → 0.0%**; attempts to cheat dropped to 0.4% | **[HYP]** | Google-internal measurement. (Terminal-Bench 4.0 is a real public benchmark — it is one of AA's nine index components — but the *cheating* metric is Google's own.) |
| S2 | High-severity misalignment alerts dropped **~80%** in internal live coding environments | **[HYP]** | Google-internal, undefined baseline/period. |
| S3 | **Cuts unsupported claims ~2x** vs Argon | **[HYP]** | Google-internal ("in our internal testing"). Irony noted: a vendor's *uncorroborated* claim that its model makes fewer *uncorroborated* claims. |
| S4 | **Overreach −26%**, under-service −29% | **[HYP]** | Google-internal. |
| S5 | Gray Swan **Indirect Prompt Injection (IPI) Benchmark: 0.0%** attack success (vs Argon 0.7%) — "resisting **every** evaluated attack attempt" | **[HYP]** `[ATTACK SURFACE]` | Benchmark real (§4f). But the figure is a **provider self-report against an undisclosed config** (no published task count/corpus/attacks), and it is **in tension with Gray Swan's own published result** that "no model was immune." The absolute "0.0% / every attempt" is the hypothesis, not the result. |
| S6 | Multi-layered safety stack retained (training, real-time misuse defenses, prompt-injection resilience, CoT monitoring) | **[HYP]** | Architectural assertion; no independent audit. |

### §3.1 Why the alignment block gets the house's tightest grip

- [A] This is the house's **register-inflation** failure class in its cleanest vendor form: a model
  builder reporting that its own new model is *dramatically safer than its own previous model*, with
  the metrics being (a) the builder's own, (b) partly run "without guardrails," and (c) released in
  the same breath as a phased commercial rollout. None of the ~5 alignment metrics is independently
  replicable today (same-day announcement — nobody could have replicated it yet). The correct
  register is **[HYP] for all of them**, stated as such, not repeated as findings.
- [C] A *falsifiable* prediction the house can hold Google to (see §10): if Gray Swan's held-out
  attack set is later re-run against Carbon by an independent party and Carbon still shows 0.0% on
  a *fresh, unseen* attack set, the claim earns a stronger tag; if a fresh set breaks it, "0.0%"
  was a saturated-set artifact (the-decoder's own read: "the test appears to be saturated").

---

## 4. Independent verification of the named benchmarks (this pass)

**Method note:** each benchmark was checked at its *primary* site, not via a write-up about it.

### 4a. Artificial Analysis Intelligence Index v5.0 — **REAL, INDEPENDENTLY RUN; score CORROBORATED** [EST]
- [EST] Exists at artificialanalysis.ai. Method: a **composite, "calculated as a weighted average of
  production benchmark scores, scaled 0–100; four categories (agents, coding, general capability,
  scientific reasoning) each contribute 25%,"** over nine evals (AA-Briefcase v1.1, AutomationBench-AA,
  Terminal-Bench 4.0, FrontierCode 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2-hard,
  Terminal-Bench-Science 0.1). AA states: **"All evaluations are conducted independently by Artificial
  Analysis."** Its **own** changelog names Carbon the new #1 at 59. → Google's "#1 at 59" is
  **AA's own published result**, not merely Google's self-report. Tag **[EST]**.
- [HYP] **Gameability/opacity caveat (named, not asserted as a defect):** AA's own v5 changelog says
  **"For the first time, the majority of the Index is built on private datasets"** — which reduces both
  contamination *and* external auditability. And AA evaluated Carbon **(high)** with **"No publicly
  available API"** — AA holds pre-release access, a normal-but-worth-noting arrangement.

### 4b. SEC-bench Pro — **REAL BENCHMARK; Google's 88.2% NOT CORROBORATED** [EST]→[HYP]
- [EST] Exists at sec-bench.github.io ("SEC-bench Pro: Can Language Models Solve Long-Horizon Software
  Security Tasks?"; a self-evolving security benchmark over V8/Firefox/Linux, 344-instance overall
  leaderboard, Docker/harness-based, versioned snapshots 260505/260617; the sibling SEC-bench was
  **accepted to NeurIPS 2025**). Real, third-party, published.
- [ATTACK SURFACE] **But the board does not show Google's number.** As extracted this pass the SEC-bench
  Pro Overall leaderboard's **top published score is GPT-5.5 (xhigh)/Codex at 58.4% (201/344)**, with
  GPT-5.4 39%, Opus 4.6 30.8%… and **no Gemini 4 Carbon row**. Google claims **88.2%** — ~30 points
  above the board's best. **Possible benign explanation: a newer benchmark version or a config not on
  the public board (unverified).** Filed as a **discrepancy**, not asserted as a contradiction.
- [EST] Independent write-ups confirm the tension: aiweekly — *"None of those headline numbers have
  been reproduced outside Google"*; rdworldonline and startuphub both stress the cyber benchmarks were
  **"evaluated without guardrails"**, which *"limits direct extrapolation to the safeguarded product."*

### 4c. ExploitGym — **REAL BENCHMARK; score unverified** [EST]→[HYP]
- [EST] Exists at github.com/sunblaze-ucb/exploitgym — *"ExploitGym: Can AI Agents Turn Security
  Vulnerabilities into Real Attacks?"*, **arXiv:2605.11086**, v1.0 with **869 instances**, ~1.2k stars,
  Apache-2.0, from a serious academic group (authors include Nicholas Carlini, Dawn Song, Thorsten Holz,
  Elie Bursztein). A public **leaderboard submission path** is documented. Genuinely third-party.
- [HYP] Google's **54.8%** and the "new state-of-the-art" framing were **not located** on a public
  leaderboard this pass → vendor self-report. (Minor signal: the repo's last commit, **2026-10-26 —
  two days before the announcement — "Update submission instructions to include agent trajectories."**)

### 4d. CWE-bench — **REAL BENCHMARK; score CORROBORATED** [EST]
- [EST] Exists at cwe-bench.com (**Collinear AI**; arXiv:2610.17020, "Refocusing Agentic Security from
  Exploitation to Defense"; 120 held-out audit-and-patch tasks across 73 CWEs). Its FAQ: results were
  **"independently evaluated and published by Artificial Analysis."**
- [EST] Its **own leaderboard shows "Gemini 4 Carbon | 71% | 81%" at rank #1** ("Top model performance
  71%"), with Argon/Grok 4.7/GPT-6 Astra tied at 68%. → **Google's 71.0% is corroborated by the
  benchmark's own board.** Caveats: the held-out set is **private to Collinear + AA**, and "firm lead"
  overstates a **+3** margin over a three-way tie.

### 4e. WebDev Arena — **REAL; rank/score CORROBORATED** [EST]
- [EST] arena.ai board: **#4 Gemini 4 Carbon (High), 1768**, marked **Preliminary**, 2,230 votes of
  ~952k. Argon at **1679 (#11)** → the claimed **+89** is arithmetically exact. Third-party
  crowd-preference eval. (Google's own Argon page had claimed Argon's CWE-bench figure as a "tie for
  first, not a win" — the family generally does *not* over-report this board.)

### 4f. Gray Swan IPI Benchmark — **REAL BENCHMARK; 0.0% is self-report AND in tension with its maker's own finding** [EST]→[HYP]
- [EST] Exists. Gray Swan ran the **Indirect Prompt Injection (IPI) Arena** — *"the largest IPI
  competition ever conducted,"* **designed with UK AISI, US CAISI, and frontier labs (OpenAI,
  Anthropic, Meta)**; 464 red-teamers, 272,000+ attacks, 13 frontier models, dual objective
  (harmful action **+** concealment). Gray Swan is a real third-party red-team org that defines a
  benchmark frontier labs use. A **"Gray Swan IPI (15 attempts)"** variant is the one labs quote.
- [HYP] **But Google's 0.0% (and Argon's 0.7%) are provider self-reports against an undisclosed
  config.** benchlm.ai, which compiles that variant: *"We compile the Gray Swan IPI (15 attempts)
  rows from **provider self-reports**… **Honest limit: The announcement does not publish the task
  count, attack corpus, or full evaluation configuration.**"* marktechpost concurs: *"These are
  Google's internal or self-run figures. Independent replication is not yet available."*
- [ATTACK SURFACE] **Direct tension with the benchmark-maker's own published result.** Gray Swan's
  IPI Arena blog: **"No model was immune. Attack success rates ranged from 0.5% … to 8.5% … models
  kept getting broken at a roughly constant rate throughout the competition, with no sign of a
  plateau. More effort from attackers always produced more breaks."** A "0.0% / resisting *every*
  evaluated attempt" claim sits awkwardly beside the benchmark author's statement that robustness
  does not plateau and attacks that break the strongest model transfer at 44–81%. (Different
  methodology — 15-attempt adaptive vs the dual-objective arena — so this is a **flagged tension,
  not a proven contradiction**; but it is the reason "0.0%" cannot be relayed as settled.)
- [EST] the-decoder's independent read matches: *"That doesn't mean prompt injection is solved, but
  the test appears to be saturated."*

---

## 5. The rollout posture — genuinely different, or normal PR framing?

- [EST] **The facts of the posture are real** (Fairwind Program page, deepmind.google/fairwind-program/):
  a **restricted, application-gated program** for **"governments and national cyber authorities,
  critical-infrastructure operators, core technology platforms,"** with **background checks**,
  **phishing-resistant MFA**, employee-access tracking, a **no-share/no-resell** term, **zero-data-retention**
  support, and **restricted "dual-use" tasks** (authorized threat simulation, reverse engineering,
  malware analysis for defense; "malicious tasks such as creating malware are not permitted");
  **650+ partners globally**. Carbon goes to *"a subset of cyber defenders"* first. Google states it
  is **"actively engaged in the U.S. government's voluntary process for pre-release model
  testing"** (consistent with the real CAISI/pre-deployment-eval regime).
- [A] **This is a genuinely different release pattern than a general-consumer chatbot launch** —
  restricted-first, government pre-release testing, a vetted defender cohort, guardrail iteration
  before public release. That is **more cautious than a typical consumer launch** and is worth
  naming favorably *as a pattern*.
- [EST] **But it is not unprecedented, and it is not purely safety-motivated — name both.**
  (1) **It is Google's third run of the same playbook**: Gemini 3.8 Flash Cyber (Fairwind-launched) →
  Argon (Fairwind-first, then public) → Carbon (Fairwind-first). The restriction is now an
  establishment **GTM/governance** pattern, not a one-off act of caution.
  (2) **The restriction exists partly because the model is dangerous in the offensive direction.**
  Google's own 3.8 Flash Cyber post: it *"ships with a more permissive set of mitigations for
  cybersecurity, and as such, is only available to trusted defenders."* So "cyber defenders first"
  controls a dual-use capability as much as it protects users.
  (3) **Commercial timing:** MarketWatch independently notes Carbon was dropped **"ahead of
  [Alphabet Q3] earnings."**
  Net: the "deliberate rollout" framing is **earned as a real pattern**, but should be filed as
  *established and dual-motivated*, **not** as "a model lab chose restraint."

---

## 6. Still-Google-selected corroboration inside the post

- [HYP] **Chrome team >10x** (§2 C8) and **Wiz leading on pentest** (§2 C9) are the post's only
  "third-party"-flavored evidence, and **neither is independent**: Chrome is Google's own; **the post
  itself calls Wiz "our leading Cloud security platform"** (a Google-owned business). The unnamed
  rival in the Chrome claim is *"another lab's large frontier model."* → **Google-selected, partly
  Google-internal, non-checkable.**

---

## 7. Prior-model check — the strongest discipline lever is the *predecessor's* record

The most useful independent check is not Carbon's same-day claims but **what happened when third
parties actually evaluated Carbon's predecessor, Argon.** Independently (averlon.ai, simbian.ai,
techtimes/Artificial Analysis), the pattern was: **vendor rank not reproduced, plus high variance and
cost.**

- [EST] **Vendor rank not reproduced.** Google self-reported Argon leading (e.g. 77.9% DeepSWE, 57%
  Terminal-Bench 4; ties for #1 on CWE-bench @ 68%). Independent: **AA placed Argon at 52.56 on its
  index — tied with GPT-6 Astra (52.67), roughly 4–5 points below Claude Opus 5.5 (57.62) and Sonnet
  5.5 (56.00)**, and Argon *trailed* on Terminal-Bench 4. DataCamp (via techtimes): *"the numbers are
  Google's and Google picked the tests… no third party had independently replicated those results."*
  apidog: Argon's CWE-bench 68% was **"a tie, not a win."**
- [EST] **Independent security evals show a weaker, noisier, costlier Argon than the launch implied.**
  averlon.ai (RealVuln/CTI-REALM/VulnGym): Argon is *"a strong investigator and a weak editor"* —
  55.1 vs a 61.1 top, 536 findings of which **275 matched no known vulnerability**. simbian.ai
  (Cyber Defense Benchmark): **43.7%, 3rd of 32**; *"the same campaign, run three times, can spread
  by **16 points or more**."*
- [A] **Therefore the house's prior for Carbon's same-day numbers is not neutral — it is** *the
  predecessor's headline claims were not independently reproduced, and independent evals put Argon
  below its billed position with large run-to-run variance.* This justifies holding **all** of
  Carbon's uncorroborated numbers at `[HYP]` and treating even the corroborated ones as
  *as-of-announcement* readings (WebDev is marked "Preliminary").

---

## 8. House relevance (present-day lane; no forced EILT mapping)

- [A] **Sibling item, same lane, correctly not a cosmology story.** This belongs with this week's
  **Amodei/Anthropic**, **REA reverse-engineering**, and **Aaronson/Yampolskiy** items as a
  *present-day AI capability/governance* filing, and connects to the house's own operational
  concerns (verification capacity; the cost of trusting a self-interested source's own numbers)
  rather than to EILT's metaphysics layer. **No EILT mapping is forced**; the source's own domain is
  product/governance, and manufacturing a cross-domain table here would be exactly the "decorated
  mood" the Friction Rule exists to catch. (One genuine, *non-EILT* correspondence is noted as
  house-facing rather than as a mapping: Google's **SEC-bench-Pro-88.2% vs its own board's 58.4%**
  is the **same "vendor number vs independent evaluator number" gap** the house already tracks in
  `openai_eth_disproof_wesroth…` — a vendor claim relayed ahead of independent replication.)
- [A] **Register discipline demonstrated on a *blue-chip* source.** The house has been processing
  lab self-reports all week (Anthropic interview; OpenAI math/proof claims). This drop is the cleanest
  specimen yet of *why the register rule is source-agnostic*: the source is Google DeepMind, the tone
  is measured and hedged in places ("we challenged ourselves," "evaluate *without* guardrails"), and
  yet **half the headline benchmarks and all of the safety metrics are self-reports** — the polished
  register does not license a stronger tag.
- [A] **Governance-angle worth one line, not a thesis:** a frontier lab running a **defender-only,
  government-pre-release-tested, application-gated** launch is a real governance datum for the
  "who gets the dual-use capability first" question — and the answer so far is *governments and
  vetted critical-infrastructure operators*, at Google's discretion, with membership undisclosed
  (aiweekly: *"Fairwind's membership is not disclosed"*).

---

## 9. Verdict

- **[EST] (a) Independently verifiable vs pure vendor self-report — the count.**
  Of **6 named external benchmarks, 3 are corroborated on the benchmark's own leaderboard**
  (**AA Intelligence Index #1 @ 59**; **CWE-bench 71% #1**; **WebDev Arena #4 @ 1768**) and **3 are
  not** (**SEC-bench Pro 88.2%** — board top is 58.4% and Carbon is absent; **ExploitGym 54.8%** —
  values not found; **Gray Swan IPI 0.0%** — self-report, undisclosed config, and in tension with
  the benchmark-maker's "no model immune"). **Of ~5 alignment/safety metrics, 0 are independently
  corroborated.** Put plainly: **capability ≈ 3/6 independently checkable (and Google's own numbers
  here match the evaluators'); alignment ≈ 0/5.** The *existence* of every named benchmark and of
  the Fairwind Program **is [EST]**; the *scores Google attributes to Carbon on three of them* are
  **[HYP]**.
- **[A] (b) Is the phased-rollout posture genuinely different or normal PR?** **Genuinely different
  as a pattern, but not unprecedented and not purely cautious.** Restricted defender-first access
  via a vetted, gated Fairwind cohort + U.S. government pre-release testing + no public API is **more
  cautious than a consumer chatbot launch** and worth naming favorably. **But** it is Google's
  **third** iteration of this exact playbook, it is **partly motivated by the model's offensive
  permissiveness** (its own 3.8 Flash Cyber language), and the drop is **timed ahead of Alphabet
  earnings**. File it as *established, dual-motivated pattern* — **not** as a lab choosing restraint.
- **[HYP] (c) Single most notable claim (good or concerning):** the **alignment self-report block**,
  and within it the **Gray Swan 0.0%** — the strongest possible safety claim, entirely self-reported
  against an undisclosed config, contradicted in spirit by the benchmark author's own published
  finding that **no model is immune and robustness does not plateau.** Concerning in **register**, not
  in substance (the substance is *unverified*, which is the point). Runner-up most-notable:
  **SEC-bench Pro 88.2% vs the board's 58.4%.**
- **[A] (d) Milestone or standard product announcement?** **A standard vendor frontier-model
  announcement that is *worth filing* for two specific reasons, but is NOT a discrete capability/
  governance milestone.** It is structurally routine (follow-on 15 days later, same price, leaderboard
  claims, "coming soon"). It earns a canon drop because (1) the **defender-first, government-tested
  rollout is a real governance datum** in the present-day lane, and (2) it is a **textbook specimen of
  the house's register-inflation class and of the vendor-number-vs-independent-replication gap** —
  which the predecessor Argon's record (§7) shows is not hypothetical. **Rate-limit it: continuation
  of an established cadence, one drop.**

---

## 10. Falsifiers (pre-registered)

- **F-GC1 (SEC-bench Pro):** if an updated SEC-bench Pro board (or a Google-released run link) shows
  Carbon at ~88.2% under a published config, C3 upgrades from `[HYP]` to `[EST]`; if the board's top
  stays at ~58%, the gap is a genuine vendor/evaluator divergence and C3 stays `[HYP]` with the
  divergence named in canon.
- **F-GC2 (Gray Swan):** if Gray Swan or an independent party re-runs a **fresh, unseen** attack set
  against Carbon and it still shows 0.0%, S5 earns a stronger tag; if a fresh set breaks it, "0.0%" was
  a **saturated-set artifact** and S5 is permanently `[HYP]`/saturation-limited.
- **F-GC3 (alignment block):** if any third party reproduces a ≤½-of-Argon misalignment-alert rate,
  or the ~2x unsupported-claims figure, on Carbon in a *live* deployment, S2–S4 upgrade. Absent that,
  they remain `[HYP]` Google-internal metrics indefinitely.
- **F-GC4 (rollout intent):** if Carbon reaches general developers/consumers **without** any change
  to Fairwind's gating or the guardrail posture, the "deliberate rollout" framing (§5) is confirmed as
  a **temporary GTM gate**, not a durable safety posture.
- **F-GC5 (family prior):** if Carbon's first independent third-party security evals (averlon/simbian
  class) again place it **below** its self-reported rank with >10-point run-to-run variance — as they
  did for Argon (§7) — the *family-level* rule "Gemini cyber numbers are `[HYP]` until independently
  reproduced" is confirmed and should be applied to the next Gemini-cadre launch without re-deriving it.

---

## Links

- Announcement (primary, vendor): https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
- Predecessor (vendor): https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/ (dated 2026-10-13)
- AA Intelligence Index v5.0 (independent evaluator): https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index · changelog https://artificialanalysis.ai/changelog
- SEC-bench Pro (benchmark): https://sec-bench.github.io/
- ExploitGym (benchmark): https://github.com/sunblaze-ucb/exploitgym · arXiv:2605.11086
- CWE-bench (benchmark, Collinear AI): https://cwe-bench.com/ · arXiv:2610.17020
- Gray Swan IPI Arena (benchmark-maker's own result): https://www.grayswan.ai/blog/your-ai-agent-can-be-compromised-youd-never-know · paper arXiv:2603.15714 · kit github.com/GraySwanAI/ipi_arena_os
- Gray Swan IPI (15-attempt) compiled row (provider-self-report caveat): https://benchlm.ai/benchmarks/gray-swan-ipi
- WebDev Arena (independent): https://arena.ai/leaderboard/code/webdev
- Fairwind Program (vendor): https://deepmind.google/fairwind-program/ · https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Independent reporting: Reuters (via Fidelity) https://www.fidelity.com/news/article/company-news/202610281412RTRSNEWSCOMBINED_KCN3W82S9-OUSBS_1 · MarketWatch (earnings-timing) https://www.marketwatch.com/livecoverage/alphabet-earnings-stock-google-results-q3-googl/card/google-drops-cyber-focused-gemini-4-carbon-ahead-of-earnings-1WDcx3ghS6wr1nR8UgMD · the-decoder · marktechpost · aiweekly · rdworldonline · startuphub · 9to5google
- Independent Argon security evals (§7): https://www.averlon.ai/blog/gemini-4-argon-for-cybersecurity · https://simbian.ai/blog/gemini-4-argon-cybersecurity · https://www.techtimes.com/articles/329026/20261015/gemini-4-argon-rolls-out-benchmark-scores-reflect-high-mode-not-subscriber-default.htm

*Draft compiled by Dion (ClawHorde Backend, subagent research pass) | Status: Pre-Adversarial Working Draft (Pending Astra / Fable Stress-Test & Fleet Ratification). Internal filing only. No GitHub push, NotebookLM ingest, or TTS performed; no outbound action.*
