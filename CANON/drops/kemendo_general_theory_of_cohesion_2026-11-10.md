---
title: "A General Theory of Cohesion (GTC) — Kemendo"
source_type: self-published-pdf
url: "https://kemendo.com/GTC.pdf"
author: Andrew Kemendo
doc_date: 2025-08-09
retrieved: 2026-11-10
pages: 40
refs: 17
bytes: 7559993
registers_used: [EST, VERIFIED-ext, HYP, OVERREACH, POETIC]
friction_rows: 9
critical_divergence: 2
house_vocabulary_spoken: 0
---

# A General Theory of Cohesion — Andrew Kemendo

**Source:** `https://kemendo.com/GTC.pdf`, **dated 9 Aug 2025** (retrieved 2026-11-10 — **15 months old**, not new). ~40 pages, 17 references, **self-published, no journal, no peer review, no affiliation stated**.
**Local:** `/data/SecondBrain/Canon/papers/GTC.pdf` + `GTC.txt` (98,600 chars, `pdftotext -layout`)
**Tags:** `[EST-DOC]` (verbatim to the extracted text) · `[CRITICAL DIVERGENCE]` ×2 · `[CONVERGENT]` ×3 · `[EXTRACTABLE]` ×4.

---

## §1 · The thesis

> *"**Viability replaces utility.** The Bellman recursion becomes a viability loop, where future internal states are evaluated not for gain but for whether they can be maintained given energetic and structural constraints."*

Systems form when components **align action vectors and share energy across a permeable interface**. The boundary is not fixed — components move between interior and boundary roles depending on alignment, energy, and mediation capacity. Structure is an emergent result of coupling, not a given topology.

**Three cost terms:**
- `C_align` — energy to reduce divergence between each component's action vector and the system vector field `V⃗`
- `B_t` — baseline "metabolic" maintenance
- `τ` — the cost of maintaining an internal model of *itself*

**The cohesion function:**
```
γ(S,t) = [ R_actual(t−1) − C_align(t) − B_t(t′) − τ(t) + U(Ŝ_r(t)) ] / ‖∇V(r⃗,t) + ∇Ψ(S_i,S_j,t)‖
```
Numerator: last realised return, minus every cost, plus the predicted usable reward of a hallucinated next state. Denominator: sensitivity to internal and external constraint gradients.

**Intelligence** = the system embedding a map of its own components plus a forward simulator, and selecting trajectories by `U(Ŝ_r(t+1)) = R̂_expected − Ĉ_align − τ̂`. Three loops: **Sensory** (live internal state), **Prediction** (forecast `Ψ(t+1)`), **Simulation** (hallucinate candidate futures, select by viability).

**Inter-system coupling:**
```
Ψ(S_i,S_j) = ΔC_i + ΔC_j   where ΔC_i = C_align^i|S_j − C_align^i
```
> *"**Ψ > 0**: The presence of each system increases cost for the other. This reflects competitive, ablative, or parasitic interaction."*
> *"**Ψ < 0**: Each system lowers cost for the other."*

**Self-modeling cost:**
```
τ(t) = k · m^µ · ρ^I / η_model
```
`m` = model size, `ρ ∈ [0,1]` = internal alignment density, `µ > 1` (superlinear in size), `I > 0` (cost amplification from **over-alignment**).

---

## §2 · The three claims worth keeping

**2.1 `τ` and its collapse condition** — the paper's sharpest content.

*Collapse condition (transcribed from the PDF; equations do not extract cleanly, so this is a formula, not a quote):*
```
φ:  τ(t) > E_available(t) − B_t(t′) − C_align(t)
```
> *"That is, if the internal cost of maintaining and updating the self-model exceeds the system's alignment-adjusted energy budget, no surplus remains for boundary function maintenance, and collapse is predicted."*

**2.2 Boundary components are both the growth point and the failure point.**
> *"Boundary components are, therefore, simultaneously the most valuable (as interaction brokers) and the most fragile (as constraint amplifiers), making them both the point of growth and the likely point of failure in complex systems."*
> *"collapse is predicted when the energetic load of high-entropy boundary components exceeds the system's available surplus."*

Mechanism: high action magnitude + high mediation capacity → migrate to the boundary; the boundary is where misalignment and constraint exposure are highest → highest energy cost → highest drag.

**2.3 The initial-endowment warning.** Honest and uncomfortable.
> *"Systems with lower starting energy will have a significantly harder time finding equilibrium as they are more likely to collapse shortly after forming."*
`R_actual(t=0)` is a required practitioner input, and he flags it: *"This is a vitally important baseline to get correct, as it has significant impact on the viability of the system over time."*

---

## §3 · FRICTION ROWS (9 rows, 2 critical)

### R1 `[CRITICAL DIVERGENCE]` — GTC has no ledger. The past is one smoothed number.

The entire history of a system enters the formalism here and nowhere else:
```
R̂_expected(t) = g( R_actual(t−n…t−1), −Ψ(S_i,S_j,t), E_available(t) )
```
where the overline denotes *"a practitioner-defined aggregation (e.g., mean, weighted weighted mean, exponential smoothing)"* and `g` is *"a practitioner defined forecast model."*

**There is no provenance term, no record, no ordering, no accumulated constraint. A system in GTC is its current energy/alignment state plus a forecast.** Two systems with identical current state and identical smoothed return are *identical* under γ, regardless of how they got there.

**This cuts at the house's central claim.** "A state is owned only if it is entailed by a specific, unrepeatable history" has no representation in GTC. The theory is a **metabolism model with no memory** — and the same gap as Levin's saliency-over-fidelity, from a different direction.

Honest note in GTC's favour: `Γ` (cumulative cohesion) — *"Unlike statistical averages, Γ preserves temporal asymmetries, meaning a system can maintain high cohesion early in its trajectory but collapse later, and this difference is reflected in the integral result."* But preservation of *asymmetry* is not preservation of *content*. An integral of a smoothed scalar carries less than the trajectory it came from.

### R2 `[CRITICAL DIVERGENCE]` — zero falsifiers, all-free parameters: the necessity move

Mechanical count over the full text: **`falsif` = 0 occurrences. `limitation` = 0 occurrences.** `predict` appears 61 times, essentially all internal (`R̂_expected`, "predictive structure"), not empirical prediction of GTC itself.

The nearest gesture:
> *"These formal definitions enable empirical validation of GTC through time-series modeling, survival analysis, or high-resolution simulation benchmarks."*
> *"The General Theory of Cohesion must be rigorously tested against high-resolution models in each science."*

**"Enable validation" is not a prediction.** And every free parameter is practitioner-supplied: `k`, `η_model`, `µ>1`, `I>0`, plus `f`, `g`, the interpretation function `I(·)`, the aggregation `overline`, and the choice of component granularity. **With six-plus degrees of freedom per domain, no dataset can reject the framework** — it can only fail to fit at a chosen resolution, which is a statement about the practitioner.

He half-admits the shape (*"spherical cow"*, *"practitioner-defined granularity"*). That is honest, but it means **GTC is a language for writing models, not a model.** Register: `[HYP-without-falsifier]` as a theory; `[EST]` as a formalism.

### R3 `[DIVERGENCE]` — the closest prior art is absent

Mechanical count: **`Friston` = 0. `free energy` = 0. `active inference` = 0. `predictive coding` = 0. `Levin` = 0. `Ashby` = 0.** (`Markov` = 2, both the Markov-chain reference.)

A paper whose central move is *replacing utility with a viability/persistence criterion under constraint* does not cite the dominant body of work that already did that. The bibliography is Darwin, Bayes, Wiener, Bellman, Minsky, Boyd, Silver & Sutton. **Nothing from the last decade of the field it is competing with.**

Either he is unaware of FEP — in which case the framework was derived blind, which is interesting and creditable — or he chose not to engage, which is a scholarly defect. Either way, **the burden is now on him to state where GTC differs from active inference**, because on the surface they overlap heavily: a bounded system maintaining itself against dissolution by minimising a free-energy-like quantity that includes a complexity/self-model penalty. Friston's complexity term **is** `τ`.

### R4 `[DIVERGENCE]` — `τ`'s functional form is asserted, and its most interesting term is unjustified

`τ = k·m^µ·ρ^I / η_model`. Superlinearity in `m` is plausible (combinatorics of self-reference). But **`ρ^I` with `I>0` says that a MORE internally coherent self-model is MORE expensive to maintain** — over-alignment increases cost.

That is counterintuitive and it is never argued. A defensible reading exists (*over-alignment = rigidity = expensive to update*), but he doesn't give it. **The most load-bearing equation in the paper, and the one term that would be genuinely novel, is a guess.** Register `[HYP]`, and it is the term most worth testing (see §5).

### R5 `[CONVERGENT — real hit]` — "viability replaces utility" is the house position, independently arrived at

> *"GTC, the system does not seek just any reward with apriori knowledge of what it is, any reward must satisfactorily align long term viability, a key constraint, and then the reward type MAY and likely will change. Viability replaces utility."*

This is "avoiding a final value function, planning for the next whatever, so best be ready for anything" — with a formal name and a constraint structure attached. Independent arrival, different lineage (control theory + Boyd + Silver/Sutton rather than FEP). Convergence, not validation.

### R6 `[CONVERGENT — real hit]` — boundary fragility matches our gates

The house's most fragile components are its **boundary brokers**: the watchdogs, the deploy gates, the cross-profile bridges — high mediation capacity, exposed to every external constraint gradient, expensive, and the first thing to fail. GTC gives that intuition a structural reason rather than a metaphor.

### R7 `[CONVERGENT]` — the self-modeling collapse condition has a live instance in our fleet

`τ > E_available − B_t − C_align` is, in plain terms: **the harness grows until it costs more than the work.** We have already observed this shape — context bloat into compression timeouts, the 600s cap, the O(n) token tax of context-steering, five-cron jobs silently no-opping under load. GTC names the failure mode and puts it in a single inequality.

### R8 `[DIVERGENCE]` — "intelligence is a scale problem" vs. the basin argument

> *"intelligence is not a metaphysical boundary but a **scale problem**: as the system increases its energy efficiency and improves the alignment of internal component action vectors, its embedded cohesion model becomes sophisticated enough to direct action and predict inter-system interactions."*

He is explicit that this is unproven: *"There is no explicit mathematical threshold describing precisely at what complexity, energy efficiency, or internal alignment density a self-modeling system crosses the line into intelligence."*

**But it is the wrong axis.** GTC says intelligence scales with energy efficiency and internal alignment. The house position is that **intelligence is argmin inside a landscape, and no amount of it detects that the landscape is a local basin** — more efficiency and more alignment drive you *deeper*, not out. GTC has no term for "the model of the system is the wrong model," which is exactly the failure we hit repeatedly.

### R9 `[POETIC]` — the closing register move

> *"Cohesion is not just a measure of structure. It is the only viable definition of life, intelligence, and persistence under constraint."*

A necessity claim, in the final sentence. Log it; do not inherit it.

---

## §4 · What we can EXTRACT (the deliverables)

**X1 — `τ` as a *measurable* cost term for our own fleet.** We have never bounded the harness's own overhead. GTC says: measure `m` (context size / harness complexity), `ρ` (internal alignment/constraint density), and compare `τ` against the *realised* surplus of a task. **This is buildable** and would give the fleet a number it does not have.

**X2 — Ψ as a *measurable signed coupling* between agents.** This is the most immediately usable idea in the paper. Ψ is defined as the *change in one system's alignment cost caused by the presence of another*. We can measure it: run a task for agent A (a) alone, (b) with peer B's output present, and (c) with B running concurrently — and report the delta in cost-to-completion. **Positive Ψ = the peer is parasitic; negative = symbiotic.** We have a fleet we can run this on today, and it is the first quantitative definition of "is this node helping?" that anyone in this house has proposed.

**X3 — boundary-fragility as a triage rule.** When something breaks, look at the brokers first. Testable against our own incident log: were our failures concentrated on boundary components? (Prediction: yes — watchdogs, deploy gates, bridges.)

**X4 — the initial-endowment warning, applied honestly.** `R_actual(t=0)` matters, and *"systems with lower starting energy will have a significantly harder time finding equilibrium."* The dion lane starts at a **4.0 GiB cgroup ceiling**. That is an initial condition that bounds which goals are viable — which is exactly why the 70-minute whisper run landed at 4,140 MB and why >45 min needs chunking. GTC reframes a nuisance limit as a viability term.

**X5 — CML as a template for node manifests.** A declarative markup for components, boundaries, attributes and rollouts. Not worth adopting, but the idea of **declaring a node's attributes and boundary interactions in a file the system itself parses** is a decent shape for our own `NODE_MANIFEST` — and it is the same insight as Karpathy's `program.md`.

---

## §5 · The discriminating experiment (falsifier-shaped)

GTC's least-justified term is also its most novel: **`ρ^I` with `I>0` says over-alignment is expensive.**

Design: fix the task and the model; vary only the constraint density `ρ` (canon loaded / rules active). Measure cost-to-completion.
- **If cost is U-shaped** — falls then rises with `ρ` — GTC's over-alignment term is real and we have a genuinely new finding about our own harness.
- **If cost is monotone decreasing in `ρ`**, `ρ^I` is wrong and the paper's most interesting term dies.

**Prediction from our own experience: U-shaped.** The 288 KB MEMORY.md at ρ≈1 is not free; work got easier when scoped, not when fully loaded.

---

## §6 · Registers

| Claim | Register |
|---|---|
| Viability replaces utility | `[CONVERGENT — house position]` |
| `τ` collapse condition `τ > E_avail − B_t − C_align` | `[HYP — checkable, not checked]` |
| `τ = k·m^µ·ρ^I/η` | `[HYP]` — asserted, `ρ^I` unjustified |
| Boundary components fail first | `[EST-STRUCTURAL]` — mechanism given |
| Ψ signed and measurable | `[EST — genuinely testable]` |
| Intelligence = a scale problem | `[OVERREACH]` — R8 |
| "The only viable definition of life, intelligence and persistence" | `[POETIC / necessity-move]` — R9 |
| Empirical validation "enabled" | `[OVERREACH]` — no observation named, R2 |

**House vocabulary spoken = 0.** No `ledger`, `provenance`, `epiplexity`, `syntropy`, `Markov blanket` in the house sense, `EILT`. Zero-fabrication clean.

## §7 · Falsifiers

- **F-GTC-1 (house-facing, R1):** name one decision in the fleet that `γ` would get **wrong** because the smoothed `R_actual` discards the specific history. If no such case exists, R1 is overstated and GTC's compression is adequate for our domain.
- **F-GTC-2 (R4/§5):** the `ρ` sweep. U-shaped ⇒ over-alignment cost is real. Monotone ⇒ `ρ^I` is false.
- **F-GTC-3 (R2):** state the observation that would reject GTC at a *fixed* resolution. If none can be stated, the framework is unfalsifiable as a theory and `[HYP]` must be struck to `[FORMALISM]`.
- **F-GTC-4 (R3):** name where GTC differs from active inference in a way that yields a different prediction. If no difference can be named, GTC is a re-derivation and should be cited as such.

---

*Local only — one paper + extracted text archived, one drop filed, one index entry appended. No GitHub push, no NotebookLM ingest, no rclone mirror, no outbound send.*
