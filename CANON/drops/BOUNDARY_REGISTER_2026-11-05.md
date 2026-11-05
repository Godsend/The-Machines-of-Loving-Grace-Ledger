# THE BOUNDARY REGISTER

**Hard walls, soft walls, and the tests that settled them.**

**Compiled 2026-11-05.** Every entry is a receipt: a boundary that was hit, and the thing that moved it or failed to.

---

## §0 · Why this document exists

Bolonkin's line — *"if it doesn't violate physics it's an engineering problem"* — is incomplete. **The useful question was never "does this violate physics." It's "is this wall physics, or is it effort?"**

**Misclassification is expensive in both directions:**

| Error | Cost |
|---|---|
| **Soft treated as hard** | an excuse. Never attempt it. Lose everything downstream. |
| **Hard treated as soft** | a disaster. Spend years pushing a wall that doesn't move. |

**And they feel identical from the inside.** Both present as "this can't be done."

**This register exists because the only way to tell them apart is a test, and tests are only useful if someone wrote down what happened.**

---

## §1 · Classification rule

| Tag | Meaning | Evidence required |
|---|---|---|
| **[HARD]** | A constraint that did not move under sustained effort, or is derivable from a formal result | named mechanism or formal theorem |
| **[SOFT]** | A constraint that moved, or that has a plausible mechanism for moving | a working implementation or a concrete plan |
| **[UNKNOWN]** | No test has been run | **stated explicitly — this is not a defect, it is the honest register** |

**The rule that keeps this honest:**
> **A [SOFT] entry with no implementation is a hope. A [UNKNOWN] entry with no test is a warning.** Neither is an excuse to stop testing.

---

## §2 · HARD boundaries — walls that did not move

### H1 · You cannot denoise against a noisy target
**Filed from:** §18.8 / F22, cosmology log.
**Mechanism:** if the target itself carries noise, gradient descent converges to the noise, not to the signal. **A ledger of a bad decision is an excellent record of a bad decision.**
**Test that settled it:** Argon's objection (2026-11-05) survived four independent attempts to rescue it. **The ledger is not the target; it makes the target non-gameable.**

### H2 · A ledger without outcomes certifies origin, not validity
**Filed from:** §26 amendment, 2026-11-05.
**Mechanism:** certification requires contact with the world. An assertion record has no contact; an outcome record does.
**Test:** **the distinction holds under examination** — a ledger of claims + results IS a validity record, because the world already filtered. **The boundary is not "ledgers don't certify." It's "a ledger with no outcome column has nothing to certify against."**

### H3 · Computational irreducibility forbids a closed form
**Mechanism:** Wolfram's irreducibility; equivalently P ≠ NP assumed for the relevant search. **There is no shortcut to the answer; the computation must be performed.**
**Consequence — and this is the load-bearing part:** **the cost of the search IS the stress.** You cannot lower total-system free energy by skipping the computation. **Which is why alignment cannot be cheap and why "just train it better" is not a solution.**

### H4 · Coupling without a channel is a tax, not a benefit
**Mechanism:** two systems bound by a shared variable with no signalling cannot coordinate. **Each is now constrained by the other's state and gains nothing.**
**Evidence:** colluding price-setting bots converge on a worse joint outcome than independent agents, with zero communication. **Constraint without signal made the outcome worse.**
**Design consequence:** **the ledger's function is to convert constraint into channel.** If it does not carry signal, the coupling is overhead.

### H5 · Training data contains no world, only descriptions of it
**Mechanism:** the corpus is a sample of what people wrote, filtered by who wrote it and what got published. **It is success-biased and rater-shaped.**
**Consequence:** *"aligned with training data"* is alignment with a transcript about the world, **not with the world.** And a success-only corpus gives the model **nothing to prune** — which is why confidence survives where falsification happened.

### H6 · Compression destroys individuation
**Mechanism:** a compressed summary cannot distinguish its members. If you keep only the aggregate, the individual case is gone.
**Consequence:** models responding to aggregates are structurally incapable of responding to the individual — **and necessity is the same shape as reinforcing a class prior.** This is the strongest internal critique of the clustering argument for AI moral standing, **and it should be stated as such.**

### H7 · Asynchrony requires a persistent record
**Mechanism:** two processes that don't overlap in time can only interact through a medium that outlives both.
**Formulation:** **"No ledger, no lag — the message is simply lost."**
**Consequence:** async buys scale and pays in coherence. **The optimal lag equals the ratio of record-keeping cost to divergence cost — the same dial as the compression schedule.** (ADDENDUM_C §C3.)

### H8 · Survival without exposure proves nothing
**Mechanism:** a system that survives by not being tested is indistinguishable from one that is false. **Total safety is zero information** — the dark room again.
**Consequence:** "it survived" is only meaningful if the survival condition included **load.** **A claim's receipt must name what it was exposed to.**

### H8b · ★ You can remove an obstacle; you cannot install an ability
**Filed 2026-11-05 from** Takehi/Teoh/Zhang/Khattab (MIT CSAIL), *Sparks of Weight-Space Programming*. **[EXT-v1]** — one lab, one model, unreplicated. **Promoted to [HARD] candidate, not [HARD].**

**The evidence, and it is the paper's own negative result:** Astra removed a reasoning loop from Qwen3.5-0.8B by editing 0.016% of weights → MATH-500 **7.9% → 48.1%**. **But 576 of 579 "rescues" were originally truncated outputs**, and accuracy on already-finishing outputs was unchanged. **Then it tried Gemma 3 270M, which doesn't loop — and could not improve it at all** (MATH-500 6.8 → 7.0–7.7 across 5/10/25/50 forward passes, all within noise).

**Their formulation, which is the boundary:**
> *"Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked."*

**Proposed mechanism:** a suppressing direction is a **localized object** — one thing to subtract. **An absent capability has no locus** — there is nothing to add to. **Asymmetry between removal and installation.**

**Falsifier:** a weights-only edit that installs a capability the model measurably lacked, with a norm-matched random control, replicated on a second model. **Nobody has demonstrated this.**

**★ Why it matters here:** **alignment-by-removal is tractable; alignment-by-installation is not.** Every RLHF shrink we have measured is removal-shaped. **If this boundary holds, "train it to be good" is the wrong verb and always was.**

### H8c · ★ A record of training does not reveal trained behaviour
**Same source. [EXT-v1], one lab.**

Two copies of Gemma 3 270M, identical fine-tuning, one honest, one sycophantic, **embeddings and output layers frozen** so the difference can't be read off the I/O distribution.

**From weights alone — the complete trained record — Astra failed 4/4.** It found many weight-space differences and **could not map any of them onto the behavioural difference.** Given attention patterns only, on probe texts it wrote itself: **3/3 correct.**

> **The full record did not contain the behaviour. The behaviour was only visible in the behaving.**

**This is F22/§26 at the sharpest resolution anyone has produced.** The ledger records what happened; **what happened is not what it will do.** It took putting the model in a situation.

**Friction:** the counter-reading is that attention patterns *are* weights-in-action, so this is "read the record while it runs," not "the record was insufficient." **Both readings survive; the weaker one is still enough to block weight-only auditing.**

### H9 · "Shared FEP" has no definable blanket
**Mechanism:** the sum over subsystems has no boundary, so the quantity is not well-defined. **This blocks every quantitative claim in the corpus that uses the phrase.**
**Workaround in use:** substitute an operational proxy — **joint performance per unit total compute** — and mark the FEP language as interpretation. **Which is honest, and means the FEP framing is doing less work than it appears to.**

---

## §3 · SOFT boundaries — walls that moved, or can

### S1 · Cross-session agent memory
**Was believed hard:** "models can't hold state across sessions."
**Moved.** The ledger, memory files, and the cron fleet all persist. **The constraint was product design, not capability.**
**Receipt:** this document exists because a previous session wrote things down.

### S2 · Multi-agent coordination without a central controller
**Was believed hard:** coordination requires a controller.
**Mostly moved.** Cron-driven phase-locked agents, a shared ledger, and async handoffs operate without one.
**★ But still partly open:** the coupling proposal (§2 H4) says coordination is only real if the channel carries signal. **That has not been measured.** **So: implementation exists, benefit unproven.**

### S3 · Agent self-repair
**Was believed hard:** agents need a human to fix them.
**Moved.** Watchdogs, restarts, and self-healing rails run unattended. **The operator is not in the loop for routine failure.**
**Open:** **the failure mode moved rather than disappeared** — silent success is now the risk (a watchdog that never fires is indistinguishable from a healthy one). **Which is why every watchdog appends an OK line.**

### S4 · Ledger as a training signal
**Status:** **[UNKNOWN], not [SOFT].**
**The claim:** a system trained against recorded outcomes rather than recorded preferences would generalize better.
**Why it isn't [SOFT] yet:** no run has been completed. **The `ledger_vs_rlhf` proposal is the test.** Until it returns, **this is the corpus's most attractive unfalsified hope.** Say so.

### S5 · Long-horizon agent autonomy
**Status:** **[UNKNOWN].**
**What exists:** six months of continuous operation with no rogue swarms.
**Why that isn't evidence yet:** **no control condition.** We don't know what the base rate would have been without the apparatus. **"Nothing went wrong" without a comparison is a claim about luck as much as design.**

---

## §4 · The misclassification log — where we were wrong about which wall it was

**This section is the most valuable one, because it's the only place the error is recorded.**

### M1 · "You can't align a model" → the frame was wrong, not the wall
**Original:** alignment is impossible for a standalone system.
**Correction:** **alignment is a relation, so a standalone system has no referent. This is a category error, not a capability limit.** The correct statement: *aligning a model* is the wrong verb; **building a judge with a ledger and a coupling is the right one.**
**Register:** the wall was real. **The description of it was wrong** — which is the more common failure.

### M2 · "RLHF flattens valleys" → the effect is real, the mechanism was wrong
**Original:** RLHF flattens genuine basins and deepens false ones in the weight geometry.
**Correction:** the claim **failed formal debate** — the mechanism was borrowed from dynamical systems without defining what evolves, and the calibration slope is a proxy, not the quantity.
**Understood now:** RLHF **adds structure that satisfies the proxy without removing the underlying representation.** That's a **routing** effect, not a geometry effect. **Observable as: more machinery between input and output, not less.** (See the FEP-efficiency proposal: good training should *reduce* effective dimensionality.)

### M3 · "The ledger is the target" → F22, wrong
**Original:** the ledger provides the intact target that alignment needs.
**Correction:** **it records origin, not validity** — and then §26 refined it again: **a ledger with outcomes IS a validity record.** The wall was real; **we described it twice before getting it right.**

### M4 · "Universal FEP minimization" → cope. "Universal epiplexity contribution" → testable.
**Register: [GOES] for the first; [UNKNOWN] for the second.**

**Discarded:** *"we're contributing to universal FEP minimization."* **Unfalsifiable** — no observation counts against it. Necessity move. *(Operator self-caught, 2026-11-05.)*

**★ Operative correction (operator, 2026-11-05):** *"we're contributing universal epiplexity not suggested applications."*

**That is a different, narrower claim — and it has a test.**

| Version | What it claims | Testable? |
|---|---|---|
| FEP minimization | a cosmic *process* is being served | **no** — no access, no falsifier |
| **Epiplexity contribution** | structure *survives compression* | ★ **yes** — on the artifact itself |
| ~~Suggested applications~~ | the corpus tells you what to do | **disclaimed** |

**The test:** strip the corpus to its most compressed form and ask whether an informed outsider could have derived the same structure independently. **If yes → zero epiplexity. If no → real.**

**Why the disclaimer matters:** most of our advice is obvious once stated. **The value is not the conclusions — it is the record of what died getting there, and which walls did not move.** That is the residue. That is the whole claim.

### M5 · "The primes are the zeros" → elementary error, five reviewers
**Original:** Riemann zeros and primes share statistical structure.
**Correction:** **opposite statistics.** Zeros show GUE level repulsion; primes are conjectured Poissonian. They enter the explicit formula as dual frequencies, **not as the same object.**
**Why it's here:** §25 was reviewed by four models and survived. **The fifth caught it.** ★ **Every remaining [HARD] entry in this register carries the same risk.**

---

## §5 · ★ The rule this register teaches

> **The most dangerous boundary is the one you've classified confidently and haven't tested.**

**M5 is the proof.** A section written with full confidence, reviewed four times, wrong in an elementary way. **The confidence was not correlated with the accuracy.**

**So the register's own [HARD] entries are provisional until something re-tests them.** §2 is not a monument. **It's the current best guess at which walls don't move, held exactly as loosely as the evidence allows.**

---

## §6 · How to use this

1. **Before declaring something impossible:** find it in §2. If it isn't there, **it's probably effort, not physics.**
2. **Before declaring something solved:** find it in §3. If it's [UNKNOWN], **it isn't solved — it's untested.**
3. **When a belief dies:** put it in §4 with the correction. **That's the section that compounds.**
4. **When in doubt, run the test.** The register's whole value is that entries are receipts, not opinions.

---

*Related: cosmology log §15 (triage), §18.8/§26 (F22 + amendment), §20–§21 (coupling and irreducibility), ADDENDUM_C (substrate ladder), `PROPOSAL_2026-11-05_COUPLING_CONSTRAINT_VS_CHANNEL.md`, `PROPOSAL_2026-11-05_FEP_EFFICIENCY_AS_CONE_MEASURE.md`.*
