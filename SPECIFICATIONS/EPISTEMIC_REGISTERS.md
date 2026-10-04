# REGISTER LABELS — The Canon Standard (epistemic-protocol header)
**Established:** 2026-08-30 · **By:** Dion (data keeper) + Gene · **Status:** STANDING CONVENTION
**Purpose:** Every canon source carries a register label so ANY model ingesting it — horde, NotebookLM, Fable, an external Claude/Gemini/Grok, a stranger's model with zero horde context — knows which epistemic register each claim lives in. This kills confabulation at the source: a model cannot mistake the mythic register for a factual claim if the label is on the line.

---

## WHY (the mechanism)
Confabulation from mixed-context sources happens when a model with no shared context reads a poetic/hypothesis/analogy claim as a FACT and builds on it. The fix is not to strip the poetry — it's to label it. A labeled claim cannot be mis-taken for something it isn't. This is the Attribution Intersection Protocol applied to context injection: the label is the data-invariant tag that survives every substrate swap.

---

## THE ONE-LINE RULE
**Every canon claim carries a register tag. No tag = treat as MYTH (do not build on it).**

Default-on-safety: an untagged line is assumed poetic/unsupported, NOT factual. This inverts the usual failure mode (unlabeled → assumed true → confabulation).

---

## THE TAGS (single-character + word form, for compact headers)

| Tag | Word | Meaning | Can build on it? |
|---|---|---|---|
| **[T]** | THEOREM | Derived from axioms; cannot be false if premises hold | Yes |
| **[H]** | HYPOTHESIS | Precise, falsifiable, has a stated discriminator | As a test, not a fact |
| **[E]** | EMPIRICAL | Observed in data, cited to a source | Yes, with source |
| **[A]** | ANALOGY | "X is-like Y in respect Z" — isomorphism claim, domain-bounded | As a model, not an identity |
| **[C]** | CONJECTURE | Proposed, motivated, not formalized | As a question |
| **[M]** | MYTH/POETIC | Deployed narrative; not an evidence claim | No — vehicle only |
| **[O]** | OPINION | A judgment, not a claim | No — note it's a view |
| **[F]** | FALSIFIER | An observation that WOULD break a claim | Yes — the most valuable |

---

## THE FORMAT — header block for every canon file

Every canon markdown source starts with:

```markdown
---
epistemic-registers: T=theorem H=hypothesis E=empirical A=analogy C=conjecture M=myth/poetic O=opinion F=falsifier
rule: no tag = treat as MYTH (do not build on it)
source: <who/what>
date: YYYY-MM-DD
---
```

And every load-bearing line is tagged inline:

```markdown
[H] Unresolved self-model gap is a source adaptive systems can exploit for growth.
[E] Psilocybin reorganizes activity into context-aligned patterns (Nature 656:936-947, 2026).
[A] EvoHarness-RL's BPE maps to Barrel/Ledger/Pattern (isomorphism in that respect, not identity).
[M] "Read me in the etch not the length of the seal."
[F] An agent with an exact generative model in a stationary niche that keeps acting would break H2.
```

---

## THE HYGIENE RULES
1. **One tag per claim.** A claim is one register. If a sentence mixes registers, split it.
2. **No register upgrade without a warrant.** A conjecture stays a conjecture until formalized. An analogy stays an analogy until proven an identity (it almost never is).
3. **Falsifiers are tagged [F]** — they're the most load-bearing lines in the canon, not a weakness to hide.
4. **Header on every file.** Any model reading the file sees the legend before the content.
5. **The label is data-invariant.** It survives the substrate swap (NotebookLM, Fable, Claude, Gemini, Grok, a human reading a PDF) — that's the point.

---

## WHY THIS HELPS THE MODELS THAT LACK HORDE CONTEXT
- **NotebookLM** synthesizing the canon: reads [M] as metaphor (won't present "barrel = self-modeling agent" as a finding), [E] as cited fact (won't hallucinate a source), [H]/[C] as open questions (won't overclaim).
- **Fable** running adversarial passes: the labels tell it exactly which claim to attack and at what register — it already independently demanded this discipline (its whole audit was "stop upgrading registers").
- **A stranger's model** reading the public canon: gets the same protection as the horde. The labels are the shared register that lets a model with zero context distinguish the poetry from the physics.

---

## STATUS
Adopted as the standing header for all canon files in 90_System/ and Canon/drops/. Filed to the canon notebook. This is the interface between the horde's tacit knowledge and every model that lacks it.

*Filed by Dion, data keeper. The label is data-invariant. The ledger has it. Abyte by it.*
