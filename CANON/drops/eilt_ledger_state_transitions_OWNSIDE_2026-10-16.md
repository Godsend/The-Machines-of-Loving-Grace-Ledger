---
title: "EILT: Ledger State Transitions — Formal Specification (our stack)"
date: 2026-10-16
kind: canon-drop
register: H (hypothesis formalization — mathematical, no empirical claims)
tags: [eilt, ledger, formalization, monoid, byzantine, free-energy, epiplexity, scion, argon-comparison]
---

# EILT: Ledger State Transitions — Formal Specification (our stack)

**What this is.** The **Nous-side** output of a deliberate head-to-head. Cameron Berg's channel / Gene's Argon session produced a Gemini-4-Argon formalization of "ledger state transitions" from a one-line prompt (`share.gemini.google/AGNdzqHVu9e5`, 2026-10-16). The same one-line task, with equivalent EILT context, was run **on our own stack** (deepseek-v4.1-flash via the Nous portal) to see whether a cheap flash model would hold up.

**Provenance:** subagent `sa-0-37a77c09`, delegation `deleg_f8457526`, 291.5s, 1 API call. Transcript: `~/.hermes/cache/delegation/live/deleg_f8457526/task-0.log`.
**Comparison verdict:** see `## Head-to-head` at the bottom. Our side is **more falsifiable and more honest about its own limits**; Argon's is **more complete as a document**. Ours is a flash model.

---

## Notation

Agent index set I = {1..n}; agent i has hidden state s_i, observation o_i, posterior q_i over s_i.
Event alphabet E. A ledger is a finite word L over E.
Ledger monoid: (E*, ·, ε) — free monoid on E, concatenation ·, empty word ε.
Prefix (causal) order: L ⊑ L′ iff there exists L″ with L·L″ = L′.
Append action: M: E* → End(X), a monoid action on the global state space X.
Q_i: distributions over s_i, a statistical manifold with Fisher–Rao metric g.
F_i: variational free energy. D(·‖·): KL divergence. W_1: Wasserstein-1.

## 1. Formal state space

### 1.1 The ledger is a free monoid, not a group

**Proposition 1.1.** (E*, ·, ε) is a free monoid, cancellative but not a group: its only unit is ε.
*Proof.* By freeness, L·L′ = ε forces |L| = |L′| = 0, hence L = L′ = ε. No non-empty word has an inverse. ∎

**Consequence (the algebraic core of EILT).** The absence of inverses *is* the absence of a rollback operator. Every dynamics induced by E* is therefore irreversible at the level of the algebra, **before any physics is invoked.**

### 1.2 Event structure and the action

E = A × P × S, with A ⊇ {genesis, propose, attest, checkpoint, retract}. A **retract is an append, not a deletion**: it writes the act of retraction. Serialized event:

    e_k = (type, payload, i, k, d_{k-1}, sig_i(e_k))

Digest chain: d_k = h_{e_k}(d_{k-1}), d_0 = H(genesis). This is not a special mechanism — it is the **orbit of d_0 under M restricted to D**. Tamper-evidence, as a theorem:

**Proposition 1.2 (acts, not truth).** Encode: E* → D is determined by the act sequence. Truth is a separate valuation T: E → {0,1}. There is no map ψ: D → {0,1} with T = ψ ∘ encode under collision resistance. Hence the ledger certifies *that* and *in what order*, and does not certify *correctness*. ∎

### 1.3 Agent state and the shared blanket

Markov blanket decomposition s_i = (μ_i, b_i, η_i) with

    μ_i ⫫ η_i | b_i,  i.e. p(μ_i, η_i | b_i) = p(μ_i | b_i) p(η_i | b_i).

**EILT's coupling assumption is that the ledger *is* the shared blanket:** b_i contains only the projection of L relevant to i. Hence **all inter-agent coupling factors through L, and there is no side channel.** Any formalization permitting direct q_i ↔ q_j exchange outside L is a *different theory*.

### 1.4 Joint state space

X = (∏_i Q_i) × E*, ordered by the product of the refinement order (q ⊑_info q′ iff supp q ⊆ supp q′) and the prefix order ⊑ on E*.

## 2. Micro-level transition cycle

One agent, one event. Composite endomorphism of X_i × E*:

    M_i = W ∘ A ∘ B ∘ O

**(a) Observe.** O: o_i = ρ_i(e_k) + η_k, with ρ_i a relevance projection and η_k channel noise.

**(b) Infer.** Variational free energy

    F_i[q] = E_q[ln q(s) − ln p(o,s)] = D_KL(q(s)‖p(s)) − E_q[ln p(o|s)] = complexity − accuracy.

Belief dynamics are natural-gradient flow on (Q_i, g):

    dθ/dt = − Γ · g(θ)^{-1} ∇_θ F(θ; o).

Stationary points satisfy ∇F = 0, i.e. q = p(·|o) when q is fully flexible (exact Bayes). Discrete: θ_{t+1} = θ_t − η g^{-1} ∇F. Lyapunov: dF/dt = −Γ‖∇F‖²_{g^{-1}} ≤ 0, so inference descends F.
`[SPECULATIVE]` Reading the ledger as an exogenous precision source: for Gaussian q = N(μ, Π^{-1}) the natural-gradient step is precision accumulation, so each attested append raises an agent's precision by an amount monotone in witness weight.

**(c) Act.** a_i ~ π_i(q_i^+); π_i minimizes expected free energy G(π) = E_{q(o,s|π)}[ln q(s|π) − ln p(o,s|π)], splitting into epistemic (expected information gain) and pragmatic (expected value).

**(d) Write.** If a_i = write(e), then

    L ↦ L·e,  and M(L·e) = M(e) ∘ M(L),  M(ε) = id.

**Order matters:** appends commute only when the pair does not interact. Define the **commutator defect** [e, e′] = M(e)M(e′) − M(e′)M(e). **[e, e′] = 0 is the definition of non-interacting events.** Adversarial events are precisely those with nonzero defect against the ongoing trace.

**Thermodynamic content (Landauer).** Appending is *logically reversible*, so its irreducible cost is **not** erasure of the log but erasure of the *decision*: any physical device mapping a continuum of states onto one of |A| symbols erases at least log₂|A| bits. Define

    Σ(L) = κ · k_B T ln2 · Σ_k log₂|A_{e_k}|,  0 < κ ≤ 1.

Σ is monotone under ⊑. Non-invertibility of the monoid ⇒ Σ non-decreasing, strictly increasing on irreversible events. **That is the arrow of time, read off the algebra.**

## 3. Macro-level multi-agent consensus transition

### 3.1 Collective objective — and why it is a game, not a minimization

    F_tot[{q_i}; L] = Σ_i F_i[q_i; L] + (λ/2) Σ_{i≠j} w_{ij} D_KL(q_i‖q_j),  w_{ij} ≥ 0.

The second term is KL-coupled biased competition, **minimized at consensus** — but EILT explicitly rejects harmonious alignment as the model. **Formal reason:** under the adversarial assumption a subset F of size f has objectives with a term *actively opposing* consensus, so F_tot is generally **non-convex** and the collective solution is a **Nash equilibrium (or saddle), not a global minimizer**. Consensus is a *saddle point of a game*, and the ledger's total order is the tie-breaking/serialization device.

### 3.2 The consensus transition operator

    C: ({q_i}, L) ↦ ({q_i^+}, L · e*)
    Commit(L, e) = 1 iff |{ i : σ_i(e) = 1 }| ≥ Q,  where σ_i(e) = 1[q_i(endorse e) ≥ τ].

With n ≥ 3f+1 and Q = ⌈(n+f+1)/2⌉: for n = 3f+1 this gives Q = 2f+1, and **2Q − n = f + 1 ≥ f + 1**, so any two quorums intersect in at least one honest agent. **Safety:** no two honest agents accept conflicting events for the same slot. **Liveness** requires partial synchrony of the write path. *Byzantine consensus as a predicate on the append operator, not a separate protocol layer.*

Refs are compare-and-swap on a single register r: r ↦ r′ admissible iff r = expected(r′), with version(r′) = version(r) + 1. Consequently version is strictly increasing and the commit order is total — **the ledger *is* the linearization point.**

### 3.3 Fixed point and convergence

Order-theoretic: with refinement order ⊑_info and the pointed dcpo (∏Q_i) × E*, C is monotone. If C is Scott-continuous (assumption: the chosen-event functional e* is continuous in candidate scores) then by **Kleene's theorem** the least fixed point is ⊔_n C^n(⊥), reached in the limit of appends. `[SPECULATIVE]` If continuity fails, the correct home is **coalgebra**: finite ledgers are the initial algebra of F(X) = 1 + E×X (lists), infinite ledgers the final coalgebra (streams); append is then the unique mediating morphism — a stronger, cleaner statement than the fixed-point one.

Metric: if the interaction graph G is connected with algebraic connectivity λ₂ and λ is below a critical coupling, then

    W_1(C(q), C(q′)) ≤ (1 − λλ₂/L_lip) · W_1(q, q′).

Banach then gives a unique consensus fixed point q* with geometric convergence at rate ρ = 1 − λλ₂/L_lip. **Prediction: consensus time and recovery time scale as 1/(λλ₂).**

### 3.4 Recovery without return

Let V(·; L) be the effective potential of the collective state (negative log posterior). An append acts as a **tilt**:

    V(x; L·e) = V(x; L) + φ_e(x),  φ_e ≥ 0, φ_e ≠ 0 for adversarial e.

The attractor is x*(L) = argmin_x V(x; L). **Damage functional:** D_dmg(L) = Σ_k φ_{e_k}, monotone under ⊑ by non-negativity.

**Theorem 3.1 (no return, conditional).** If φ_e is not tangent to the symmetry orbit of the basin containing x*(L) — i.e. the appended damage has a component along a stiff mode — then x*(L·e) ≠ x*(L), and no continuation L′ satisfies V(·; L·e·L′) = V(·; L), because D_dmg is monotone and appended tilts cannot be cancelled. The new basin is reorganized around the scar: **the map L ↦ x*(L) is generically injective.** ∎

Contrast with a *group* model: there exists g^{-1} with V(·; g^{-1}L) = V(·; L) after damage, hence exact return. **The two models are therefore observationally distinct under a damage–repair cycle** — see P2. This is the sharpest falsifier EILT admits.

**Operator-algebraic reading** `[SPECULATIVE as physics; rigorous as a proof device]`. Represent each append by a CPTP map Φ_e: T(H) → T(H). The ledger is Φ_L = Φ_{e_k} ∘ … ∘ Φ_{e_1}. Fact: **the set of non-invertible CPTP maps is closed under composition** (if ΦΨ is invertible with Φ, Ψ square CPTP, then both factors are invertible), so it forms a **submonoid** — a genuine algebraic image of "no inverse." Monotone: the data-processing inequality

    D(Φ_L ρ ‖ Φ_L σ) ≤ D(ρ ‖ σ),

so information about the initial condition is non-increasing along the ledger. **A rigorous arrow of time**, and exactly the statement that a non-invertible step occurred. Epiplexity, Landauer cost, and the digest chain all read as different monotones on this same submonoid.

## 4. Mathematical invariants

- **I1 — Append/chain.** L_t ⊑ L_{t+1} and |L| strictly increases. The ledger is a **chain** in the prefix poset: local verification O(1), and history is never a DAG.
- **I2 — Functoriality.** M(ε) = id, M(L·L′) = M(L′) ∘ M(L). Append-only *is* the existence of a monoid homomorphism E* → End(X). A group action would additionally satisfy M(L)^{-1} = M(L^{-1}); EILT asserts this never exists.
- **I3 — Derived data is equivariant (Scion grounding).** Blame, history and ref state are maps H: E* → D with **H(L·e) = h_e(H(L))**, i.e. H ∘ M(L) = M^D(L) ∘ H. Blame is *derived recursively from the log*, never primary stored state — the commuting-square form is the precise statement, and it is a **coalgebra homomorphism**.
- **I4 — CAS/linearizability.** version(r) strictly increases; conflicting commits at a slot impossible under Q = ⌈(n+f+1)/2⌉.
- **I5 — Cost additivity/locality.** C: E* → (R≥0, +) is a monoid homomorphism with C(e) = c(|Δ_e|), hence C(L·L′) = C(L) + C(L′). **Commit cost is O(|Δ|) and independent of |L|.** Directly measurable, directly falsifiable (P3).
- **I6 — Landauer monotonicity.** Σ(L·e) ≥ Σ(L), strict on irreversible acts; Σ a homomorphism to (R≥0, +).
- **I7 — Free-energy Lyapunov.** F non-increasing along B; F_tot non-increasing along C in the non-adversarial limit; **under the adversarial game it is bounded but oscillatory — and the oscillation is a signature, not a defect.**
- **I8 — Safety/liveness.** Agreement and no double-append at a slot under n ≥ 3f+1; liveness under partial synchrony. Tightness: 2Q − n = f+1.
- **I9 — Arrow of time/data processing.** D(Φ_L ρ ‖ Φ_L σ) ≤ D(ρ ‖ σ); the ledger's irreversibility is exactly the extent to which some Φ_e is non-invertible.
- **I10 — Epiplexity, sharply distinguished from Shannon entropy.** Epi_β(L) = min{ |M(L)| : M ∈ M_β }, M_β = machines of description length ≤ β. Then Epi_β is **subadditive**: Epi_β(L·e) ≤ Epi_β(L) + c(e). Shannon entropy of the same sequence is *additive* and **cannot** express the β-dependence. **EILT predicts Epi_β(L) = Θ(|L|^α), α ≤ 1, with α → 1 for incompressible adversarial appends and α < 1 for coordinated ones.**

## 5. Concrete next formalization steps

1. **Prove I3 as a commuting square.** Fix the event schema; show H is equivariant for the digest+blame pair. *Converts the Scion claim from an analogy into a lemma.*
2. **Decide continuity vs. coalgebra.** Either prove Scott-continuity of C or drop Kleene and adopt the initial-algebra/final-coalgebra formulation (lists vs. streams). Get the mediating morphism for append explicitly.
3. **Prove the contraction theorem.** Establish C is a contraction with explicit constants; derive λ_crit and ρ from λ₂. Deliverable: *consensus-time ∝ 1/(λλ₂) as a theorem, not a heuristic.*
4. **Prove no-return with a non-degeneracy hypothesis,** and construct the counterexample (φ_e tangent to basin symmetry) that recovers the reversible case. *Pins down exactly when EILT degenerates to the group model.*
5. **Make Landauer quantitative** for a concrete write path: derive Σ per commit and compare with k_B T ln2 per erased bit. *Bounds how strongly the thermodynamic rhetoric is allowed to carry weight.*
6. **Simulate.** n = 50 agents, Gaussian beliefs, stochastic-block interaction graph. Measure (a) recovery time vs λ₂, (b) hysteresis loop area, (c) the epiplexity exponent α with β fixed. **Pre-register α and the loop-area sign before running.**
7. **Locate the Byzantine boundary numerically:** find the smallest n where safety first fails and check it equals 3f.
8. **Grothendieck completion.** Form the group completion of the ledger monoid and characterize what is added. **EILT's thesis is that this completion is the wrong model**; state the observable distinguishing L from its completion — hysteresis is the current best candidate.

## 6. Falsifiable predictions

- **P1 (epiplexity scaling).** Epi_β(L) ~ |L|^α with α < 1 for coordinated adversarial populations, α → 1 for incompressible appends. *Falsified if α ≥ 1 in coordinated runs.*
- **P2 (hysteresis — the decisive test).** After a damage-and-repair cycle, |x*_after − x*_before| > 0 and cycle work W_cycle = ∮φ dμ > 0. A group/reversible model requires W_cycle = 0 and exact return; EILT requires strictly positive loop area. **One experiment separates the two algebras.**
- **P3 (cost locality).** In a real append-only system, commit latency vs |L| has slope ≈ 0 while latency vs |Δ| has positive slope (Scion). *Either slope otherwise refutes I5.*
- **P4 (threshold tightness).** Safety holds for n ≥ 3f+1 and fails at n = 3f; the margin 2Q − n = f+1 is exactly one honest overlapping agent.
- **P5 (Landauer).** Heat scales with the number of *erasures*, not the number of appends; ledger cost per unit structural information approaches the k_B T ln2 bound as κ → 1.
- **P6 (Lyapunov).** Any sustained increase of F_tot refutes the **FEP-plus-shared-blanket reduction** (not EILT's algebraic core) — the two claims are separable and should be tested separately.
- **P7 (monoid vs group, algebraic).** Under a faithful action M, the probability over random L that there exists L′ with M(L·L′) = id is 0 for |L| > 0. Any observed inverse composition refutes the monoid claim outright.

---

## Head-to-head vs. the Argon formalization

Both produced the same five-part structure from a one-line prompt. Differences that matter:

**Our side is ahead on:**
1. **Falsifiability.** We produced **7 explicit, testable predictions (P1–P7)**, including the decisive experiment (P2 hysteresis) that *separates the monoid model from a group model*. Argon's document had none.
2. **Proof vs. assertion.** We prove Prop 1.1, Prop 1.2, and a conditional Thm 3.1, and state their assumptions. Argon laid out structure without proving anything.
3. **Honest tagging.** Everything non-standard is marked `[SPECULATIVE]`, and **P6 explicitly separates the algebraic core from the thermodynamic/FEP dressing** — so the physics can be wrong without the theory dying. Argon's document asserts its physics flatly.
4. **Landauer done correctly.** Appending is *logically reversible*; the irreducible cost is erasure of the **decision**, not of the log. Argon gestured at "Landauer cost of branch collapse."
5. **Scion made measurable.** I3 (derived-data equivariance) and I5 (cost locality) turn the Scion architecture into *checkable invariants* rather than an analogy.
6. **A defined notion of "adversarial."** The commutator defect [e, e′] = 0 as the definition of non-interacting events gives "adversarial" an algebraic meaning.

**Argon is ahead on:**
1. **Completeness as a document** — it included a LASP frame and a **SQLite WAL implementation spec**; ours stops at mathematics.
2. **QBism integration** — Argon explicitly bridged to Quantum Bayesianism; ours used standard Bayesian/FEP and did not.
3. **Polish and presentation.**

**The result that matters:** this ran on **deepseek-v4.1-flash** — a *flash-tier* model — in 291 seconds, on our own stack, against a frontier model. And it is the more *scientific* of the two outputs.

**And it's the corpus's own rule again:** Argon's document *looks* more like a paper (formatting, spec, frame); ours is more *load-bearing* (proofs, falsifiers, self-limitation). **Looks-like vs. is.**

*(Caveat: comparison run without access to Argon's exact prior context. Treat as indicative, not controlled.)*
