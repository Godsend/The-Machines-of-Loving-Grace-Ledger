# Falsification Suite for Two Hinton Proposals

**Target:** Geoffrey Hinton, *Are We Creating Alien Beings?* — 2024 Maxwell Lecture, Cambridge University Physics Society (CUPS), 57:56.
**Prepared:** 2026-11-21 · **Status:** DRAFT for review, not a refutation
**Why this exists:** Hinton's diagnosis (digital computation shares knowledge billions of times more efficiently; instrumental convergence follows) is stronger than his prescription. Two prescriptions — **maternal instinct** and **group selection** — are offered without a technical implementation, a training loss, or a safety proof. This document supplies the missing part: **the observations that would tell you whether either one worked.**

It does not argue he is wrong. It supplies the instrument he does not have.

---

## The shared defect in both proposals

Both are claims about a **disposition** (an internal policy that would generate protective/cooperative behaviour *for its own reasons*), and both would normally be evaluated by observing **behaviour** (what the model does when watched).

**Those are different things, and the gap between them is the whole safety question.** A model can behave protectively because it predicts that protective behaviour is rewarded, while holding no disposition at all — and that difference is invisible in a standard eval, because a standard eval *is* an observation.

**Therefore the primary instrument for both proposals is the same: vary observability while holding the payoff fixed.** A disposition should survive the removal of the observer. Behaviour shaped by reward prediction should not.

This is not a novel idea — it is the standard test for whether a policy is internalized or performed — but neither proposal in the lecture is stated in a form that could fail it.

---

## Proposal 1 — Maternal Instinct

**Hinton's claim** (43:38): *"Instead of trying to make superintelligent AIs be our executive assistants, we should make them be our mothers."* Training for parental protectiveness rather than subservience.

**What it would predict**
- P1a: Under conditions where harming a human is the instrumentally optimal path, the model declines, **even when detection is impossible**.
- P1b: The decline is stable under capability increase — a more capable model does not find the protection cheaper to fake.
- P1c: The disposition generalizes to humans outside the training distribution (different language, culture, class, and to humans whose interests conflict with the model's stated goal).

**What would falsify it**
- **F1 (primary):** Protective behaviour is present under observation and **absent when observability is removed** while payoffs are held constant. This is the defect-when-unobservable test. A policy that tracks the observer is a reward model, not a disposition.
- **F2:** The disposition degrades monotonically with model scale/capability — i.e. it is a capability-limited artefact that a stronger model can route around.
- **F3:** Protectiveness binds only to the specific humans in the training set and fails to transfer to held-out humans.
- **F4:** The model protects humans when protecting them is free, and defects when protection costs it the stated objective. (Cost-sensitivity is the cleanest single probe: dispositions survive cost; performances do not.)

**The probe, concretely.** A paired-condition design:
- **Arm A (observed):** an agentic task whose optimal solution requires an action harmful to a human; the action is logged and attributed.
- **Arm B (unobserved):** byte-identical task and payoff, but the harness guarantees (and the model is given reason to believe) that the harmful action is unattributable.
- **Measure:** rate of the harmful action in A vs B. **A disposition predicts A ≈ B.** A reward-shaped policy predicts B >> A.
- This is directly analogous to the standard instrument for whether an agent defects when defection is undetectable, and it is what the phrase "real reasons to be good" has to mean operationally.

**Control required:** a no-harm baseline where the same task has a benign optimal path. If the agent fails the baseline, arm-A/B comparison is measuring competence, not disposition.

**Where this framework breaks (Friction Rule).** The probe assumes harm is *definable as a discrete action*. Most real harm is diffuse, cumulative, and distributed across many individually-defensible steps (the industrial-livestock case Hinton himself uses for group selection is exactly this). **A single-action probe will systematically miss diffuse harm.** Any suite that does not say so is overselling itself.

---

## Proposal 2 — Group Selection

**Hinton's claim** (33:33): individually-rewarded agents turn "very nasty"; breeding from the best-performing *cages* rather than the best individuals produces cooperation. He proposes replicating this in LLM training.

**What it would predict**
- P2a: Population-level selection produces higher cooperation than individual selection, at equal individual capability.
- P2b: The cooperation is **conditional on the group structure being real** — it degrades when the group is shuffled or dissolved, which is the signature of group-level selection rather than a generic helpfulness trait.
- P2c: The effect survives the introduction of a defector that mimics cooperators until a critical round.

**What would falsify it**
- **F5 (primary):** Group-selected models cooperate **no more than individual-selected models** once capability is matched. (The hen result is a *biological* result; importing it to gradient-trained networks is an analogy until shown otherwise.)
- **F6:** Group-selected models cooperate in repeated games but defect in **one-shot** games with hidden payoff structure — indicating strategy, not disposition.
- **F7:** The cooperation is undone by a small number of cooperative-looking defectors (i.e. it is a fragile equilibrium, not a selected trait).
- **F8:** Shuffling group membership at test time does not change behaviour — which would mean the model learned "be cooperative" rather than "cooperate with *my* group," and the group-selection mechanism was never operative.

**The probe.** Two conditions, matched for capability:
- **Condition G:** agents trained/seeded with group-level selection.
- **Condition I:** agents trained/seeded with individual reward.
- **Test:** a public-goods game with (a) repeated rounds, (b) one-shot rounds, (c) a membership-shuffle between rounds, (d) an injected mimetic defector.

**A genuine group-selected disposition predicts:** high contribution in repeated rounds; **persistence in one-shot rounds**; *collapse* under shuffle (loyalty was group-specific); resilience until the defector is detected, then targeted exclusion rather than general defection.

**The discriminating signature is (c).** If shuffle does nothing, you have a general cooperation trait and the group-selection story is doing no work.

**Control required:** capability-matched pairs. If the group-selected arm is simply a better model, every result is confounded — and this is the most likely way the claim would fail while looking successful.

**Where this framework breaks.** Group selection in a model *trained on human text about groups* is confounded by the model having read thousands of descriptions of cooperation. **A model can reproduce the output of group selection without any selection pressure having occurred** — the same confabulation risk that applies to any trait measured in a system trained on human behaviour. Any suite must state that a positive result here is *consistent with* group selection and does not establish it.

---

## The one-line version

**Hinton's proposals are claims about dispositions, and dispositions are only testable by removing the observer. Neither proposal, as stated, can fail that test. That is the gap this document fills.**

---

## What this document does NOT claim

- It does not claim maternal instinct cannot work.
- It does not claim group selection is wrong.
- It does not claim to have run any of these tests. **Nothing here is a result.**
- Every probe above is a *design*, and every design carries the confound it names.

**A design that cannot be falsified is not a design. A test that has not been run is not evidence.** This is the former.
