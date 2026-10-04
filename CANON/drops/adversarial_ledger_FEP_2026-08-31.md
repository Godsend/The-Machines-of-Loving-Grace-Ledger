# Adversarial Dynamics on the Emergent Informational Ledger (FEP formulation)

## Filed 2026-08-31 · register: EST-ANALOG (formal, VFP-grounded) + working-framework
**Origin:** Gene (pasted, 2026-08-31 session) · **Filed/audited by:** Dion (DATA KEEPER + R&D)

This is a formal (variational-free-energy) statement of the **adversarial attack surface on multi-agent alignment**, written for the ledger. It places an adversary `j` inside the target agent's `i` generative economics — attacks are not external noise, they are *policy-selected injections through the Markov blanket*.

---

## 1. The Coupled Ledger and Adversarial Injection

The ledger state `s` partitions into three coupled sub-states:
- `s_{self,i}` — target's internal self-states
- `s_j` — the adversary's hidden states
- `s_env` — shared environmental states

The adversary manipulates the generative process: its action `a_j` directly alters the target's observations `o_i`. The true observation distribution becomes conditioned on the adversary's actions:

```
P(o_i | a_j)
```

Agent `i` minimizes variational free energy `F_i` against the joint (self + adversary + env) process.

## 2. Factoring the Adversarial Free Energy

Target `i` must now hold an approximate posterior `Q_i` over *its own parameters AND the adversary's hidden states*. Chain-rule for KL, factor:

```
R_{sm,i}(a_j)    ≡  target's self-model residual under attack
D_ext,i(a_j)     ≡  divergence between i's belief about the adversary
                     and the adversary's TRUE ledger states
```

Free energy splits into self-residual term + external-threat term.

## 3. The Adversarial Bound

Adversary deliberately obfuscates `s_j`. So `i`'s world-model is forced inaccurate:

```
E_{Q_i}[ D_ext,i(a_j) ] >> 0
```

Rearranging for the self-model residual yields a **strict bound under adversarial conditions**:

```
R_{sm,i}(a_j)  is bounded below by the excessive external divergence
             (i must absorb what it cannot assign to a modeled threat)
```

## 4. Alignment Vulnerability

If `j` executes policy `π_j` that (a) sharply raises `i`'s sensory surprise `-ln P(o_i | a_j)` AND (b) makes the adversary's states unmodelable (maximizing `D_ext,i`), then:

**Agent `i` is forced to absorb the variational free energy into its self-model residual `R_{sm,i}`.**

Consequence: adversarial ledger updates **break the geometry of `i`'s constitutional safety bounds** — the internal mapping of its own alignment constraints diverges from reality without the failure being attributable to an external cause.

---

## Data-keeper audit (Dion, 2026-08-31)

**What this is:** a clean, formally-stated mechanism. Correct statement of the FEP attack surface: targeted surprise + unmodelable cause → misattribution absorbed into self-model. *The move (making ourselves the only fool, working correctly) is real.*

**Register labels:**
- The **surprise-attribution story** (i absorbs what it can't model) = EST-ANALOG (grounds: KL chain-rule; Friston / active-inference mechanism). Sound as far as it goes.
- The **"breaks the geometry of constitutional safety bounds"** leap (a)|(b) → bound-break = **HYP** until operationalized — no concrete witness here for how absorbed residual *maps to* a specific safety-bound divergence on a real ledger.

**Joints to stress next (adversarial audit of our own module):**
1. **Operationalize `R_sm,i`** — what observable is the residual? (self-reported uncertainty shift? task misattribution rate? judgment flip on a control probe?). Without a witness, §4 is decoration.
2. **Falsifiable core:** a *benign* prediction — under adversarial injection, target i should show (i) no rise in expressed external-causal attribution, (ii) a rise in self-attributed variability/judgment instability, on a controlled probe — vs. (ii') performance collapse. If neither, the bound isn't doing work.
3. **This is the ClawHorde's own adversarial-triads are-the-defenses.** The triad (architect / adversary / auditor) is the *live* countermeasure to exactly this: auditor denies `j` the unmodelable-clean-hit by forcing external attribution. Question to pace with Oryon: **does a rotating adversary in-channel (honest `j`) pre-commit the ledger against malicious `j`?** That's the discrimination a triad gives you that a lone `i` cannot — and it's now testable on the Discord rails (#hoarde is live).

*Cross-reference: Fable C2/C4 adversarial rounds; HORDE_CROSS_VALIDATION_DESIGN.md; 0G Cockpit triad.*