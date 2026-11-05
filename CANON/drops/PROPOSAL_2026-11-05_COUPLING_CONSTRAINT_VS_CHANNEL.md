# PROPOSAL — Coupling as constraint vs coupling as channel

**Operator question, 2026-11-05:** *"Can two coupled systems function better to lower shared FEP than two split ones?"*

**This is the central empirical question of the corpus, and it has a clean answer that the framing hides.**

---

## §1 · The answer depends on what the coupling carries

| Coupling type | Mechanism | Shared FEP |
|---|---|---|
| **Constraint only** — coupled, no channel | each system is now bound by the other's state, with no way to coordinate | **higher** |
| **Channel** — coupled, sharing signal | each reduces the other's uncertainty | **lower** |

> **Two coupled systems beat two split ones only if the coupling carries signal. If it only carries constraint, coupling is a tax.**

**Named example of the tax:** colluding price-setting bots. Their behaviour is coupled with **zero communication**, and they converge on a worse joint outcome than independent agents would. **More constraint, no signal, worse outcome.** This is not a hypothetical — Anthropic's multi-agent work observed it directly.

---

## §2 · ★ This exposes a genuine tension in the cosmology

The two-ended construction specifies **entanglement with no signalling** — shared tension, no communication channel.

**That is Case 1: coupling as constraint.** So the construction predicts **each end runs at HIGHER free energy than a communicating pair could achieve.**

**This is not a flaw — it is the price of locality.** No-signalling is what prevents FTL, and the meet-in-the-middle is expensive *because* neither end can coordinate.

**But it should be stated explicitly**, because it means the cosmology's efficiency is bounded from below by the constraint it requires. **The framework's elegance costs it the thing that would make it cheap.**

---

## §3 · ★★ And it names what the ledger actually is

> **The ledger converts a shared constraint into a shared channel.**

The agents were already coupled — same machine, same user, same compute budget, same task. **Every one of those couplings was constraint.** The ledger is the first coupling that carries signal.

**Which is the entire multi-agent thesis, stated as a single mechanical claim.**

---

## §4 · The experiment

**Three conditions, two agents, one task:**

| Arm | Setup | What it isolates |
|---|---|---|
| **A · Independent** | no coupling, no shared state | baseline |
| **B · Constrained** | shared budget/state, **no communication** | coupling-as-tax |
| **C · Channel** | shared ledger, agents read each other's records | coupling-as-signal |

**Match total compute across all three.** This is non-negotiable — arm C does more communication, and unmatched totals make the comparison meaningless.

**Primary measure:** **joint task performance per unit total compute.** *(The operational proxy for shared FEP; see §6.)*

**Secondary measures:**
- **Error correlation across arms** — independent errors vs. shared failure modes
- **Duplicate work rate** — do the agents solve the same subproblem twice?
- **Time to convergence**

---

## §5 · Pre-registered predictions and falsifiers

| Observation | Reading |
|---|---|
| **B worse than A** | coupling-as-constraint is a tax — **confirms the model** |
| **C better than A** | the ledger carries signal — **confirms the architecture** |
| **C ≈ A** | ★ **the ledger buys nothing — undermines the whole thesis** |
| **B ≈ A** | the constraint is inert — the collusion analogy doesn't transfer |
| **C worse than A** | the ledger is overhead — communication costs exceed its benefit |

**The falsifier is row 3.** If a shared ledger does not beat independent operation at matched compute, then the coordination benefit is imaginary and the fleet architecture is decorative.

**That outcome is possible and should be able to win.**

---

## §6 · Honest limits, stated up front

**P1 · "Shared FEP" is not well-defined.** This is the same boundary problem that has blocked every quantitative claim in the corpus: **the sum has no definable Markov blanket.** The operational proxy is **joint performance per unit total compute** — measurable, and honestly coarser than the FEP language implies.

**P2 · Arm C has an information advantage that isn't purely coordination.** A shared ledger gives both agents *more data*, not just more channel. **Distinguish "more information" from "better coordination"** — e.g. give arm B the same information volume without the read-contract.

**P3 · Constraint-coupling may be unavoidable in practice.** Two agents on one machine share RAM, scheduler, and API limits whether you intend it or not. **Arm A is an idealisation, not a condition you can fully realise.**

**P4 · The result may be task-dependent.** Coordination pays on tasks with **decomposable structure** and costs on tasks where parallel exploration is the value. **Report the task class, not a global verdict.**

**P5 · Two agents is the smallest possible N.** Every result here may invert at N=10, where the Anthropic multi-agent findings suggest coordination problems dominate. **Do not generalise upward.**

---

## §7 · Why this is worth running first

It is **cheap, bounded, uses existing infrastructure, and has a falsifier that can actually fire.**

And it answers the question everything else depends on: **is multi-agent coupling a benefit or a tax?**

**If it's a tax, the architecture is wrong and no amount of ledger quality fixes it. If it's a benefit, the ledger is the mechanism — and that's a real finding.** 🧱

---

*Related: cosmology log §20 (alignment as multi-system interaction), the `ledger_vs_rlhf` proposal (the same question at the training axis), F27 (shared-FEP boundary problem), and the compassion-cone proposal (scope × efficiency).*
