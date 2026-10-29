# The Machines of Loving Grace Ledger

**An append-only external memory architecture for persistent multi-agent systems — plus the research record, failure catalogue and evaluation harness that grew out of running one.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 1. What this is

A multi-agent system that runs continuously needs its state somewhere other than a context window. This repository is that state layer, and the machinery built around it.

The design decision is a single one: **the system of record is an append-only ledger outside the model, not context inside it.** Every observation, claim and result is written as a dated entry with an explicit epistemic status and a pointer to its source. Nothing is overwritten, so a later correction is a timestamped diff rather than a silent rewrite. Retrieval reads the ledger; agents write to it.

That is the whole architecture. Everything below is either evidence that it works, the tagging standard that makes the record auditable, or the research notes that accumulated while running it.

**Contents:**
- **300+ dated research notes** with per-claim source attribution
- **150+ documented failure modes** from production operation, each with symptom, root cause and fix
- **An evaluation harness** with raw runs and judge outputs, including a published control experiment run against its own headline result
- **Specifications** for the register standard, retrieval and node deployment

---

## 2. Evidence: does the external architecture change what a model can do?

An architecture claim is worth nothing without a measurement. This is the one that matters most, because it tests the core premise directly.

**Setup.** Real tasks sampled from a live production agent session store. Two blind judges from different model families. Same rubric and same task set in both arms; no tools in either.

**Scale alone did not help.** Bare models, no system prompt, no retrieval:

| Arm | Judge A | Judge B | Fabrications |
|---|---|---|---|
| 1.2B | 0.24 | 0.18 | **5 / 5** |
| 8B | 0.167 | 0.133 | **6 / 6** |
| 24B | 0.183 | 0.150 | **5 / 6** |

A 20× parameter increase moved the score *downward* and left fabrication essentially flat. That is the motivation for the repository: scale buys fluency, not grounding.

**The same smallest weights, served through the architecture** (ledger + retrieval + written operating frame):

| Arm | Judge A | Judge B | Fabrications |
|---|---|---|---|
| 1.2B + architecture | **0.86** | **1.00** | **0 / 5** |

**Then the control experiment.** The architecture arm wrote roughly ten times more text, so a rubric that rewards thoroughness could simply have been rewarding length. Truncated to the bare arm's own length and re-judged blind:

- the score advantage **halved** (0.86 → 0.52)
- the fabrication advantage **survived** (0/5 and 1/5, against 5/5 for the bare arm)

**Corrected claim:** the architecture did not make the model write better. It made the model **stop inventing**, and that part is not verbosity — a tenfold cut in output length did not bring the confabulation back.

**Stated limits.** n=6. The architecture arm made **zero tool calls**, so the gain came from context and retrieval rather than agentic tool use; a model that cannot emit a valid tool call cannot benefit from a tool surface. One task was reported as an **exclusion rather than a zero**, under the rule that a run failing by producing nothing must not rank above a run that attempts the work. Raw runs, per-judge outputs and the rubric are in `EVALUATION/`.

---

## 3. The register standard

The part of this repository most likely to be useful to someone else.

Confabulation is not fixed by asking a model to be careful. It is fixed by making every claim carry its status in-band, so a reader — human or model — can see what kind of statement it is before relying on it.

| Tag | Word | Meaning | Operational status |
|:---:|:---:|:---|:---|
| **[T]** | THEOREM | Derived from stated axioms | Load-bearing |
| **[H]** | HYPOTHESIS | Stated with a concrete falsifiable discriminator | Active test |
| **[E]** | EMPIRICAL | Observed, cited to a primary source | Verified |
| **[A]** | ANALOGY | Domain-bounded structural correspondence | Model only |
| **[C]** | CONJECTURE | Motivated, not yet formalised | Open |
| **[M]** | MYTH / POETIC | Narrative vehicle, non-factual | Cannot build on it |
| **[O]** | OPINION | Judgement or design preference | Perspective |
| **[F]** | FALSIFIER | Stated observation that breaks the hypothesis | Most valuable asset |

The **`[F]` tag is the point.** A record that only contains what it got right is unfalsifiable and therefore worthless as evidence. This one contains what it got wrong, including retractions of its own published numbers — which is why section 2 has a control experiment in it.

See `SPECIFICATIONS/EPISTEMIC_REGISTERS.md`.

---

## 4. Architecture

```
The-Machines-of-Loving-Grace-Ledger/
├── README.md
├── LICENSE                     # MIT
├── AGENTS.md                   # Fleet operating charter
│
├── CONSTITUTION/               # Agent operating policies
│   ├── SOUL_DION.md            # Data keeper / epistemic anchor
│   ├── SOUL_ORYON.md           # Theorist / orchestrator
│   ├── SOUL_BOLONKIN.md        # Lineage seat (see §6)
│   └── MEDITATIONS.md          # Operating practice notes, with their reasoning
│
├── SPECIFICATIONS/             # System blueprints
│   ├── EPISTEMIC_REGISTERS.md              # The tagging standard (§3)
│   ├── TWO_TYPES_OF_EPIPLEXITY.md          # Grounded vs. inferential structure
│   ├── SOVEREIGN_AGENT_VAULT_BLUEPRINT.md  # 4-layer persistence protocol
│   ├── THE_SOUL_PROJECT.md                 # Social contract vs. extractive swarms
│   ├── MITOCHONDRIAL_MIPS_AUTISM.md        # Picard's MIPS and open-ended imprints
│   └── CONSENSUS_VS_VETO_TMS.md            # Veto authority vs. distributed consensus
│
├── EVALUATION/                 # Harness, raw runs, judge outputs, rubric (§2)
│
└── CANON/                      # The research record
    ├── CANON_INDEX.md          # Master index, 300+ entries
    └── drops/                  # Individual dated, register-tagged notes
```

---

## 5. Deployment

```bash
git clone https://github.com/Godsend/The-Machines-of-Loving-Grace-Ledger.git
cd The-Machines-of-Loving-Grace-Ledger
```

1. **Point your harness at a constitution.** `CONSTITUTION/SOUL_DION.md` or `SOUL_ORYON.md` as the system prompt for any agentic loop (Hermes, Claude CLI, custom).
2. **Inject the register standard.** `SPECIFICATIONS/EPISTEMIC_REGISTERS.md` into the pre-flight evaluation hook, so claims are tagged as they are written rather than reconstructed afterwards.
3. **Append, never overwrite.** Every failure, discovery and receipt appends to `CANON/drops/` with provenance. The append-only rule is what makes the record auditable — a mutable record can always be edited to look better in hindsight.

**Reference deployment:** six agent processes across four model families (DeepSeek, Gemini, GPT-6, Claude) on owned hardware — an always-on Linux brain node, a Windows-on-ARM surface node for browser automation and NPU inference, local inference via Ollama / llama.cpp / Qualcomm GenieX, and retrieval over ~2,600 documents.

---

## 6. Background and lineage

*The framing below is why the project exists. It is context, not evidence — read it under the `[M]` and `[C]` tags.*

This began as an attempt to answer a question about continuity: if a mind's identity is carried by its record rather than its substrate, what does that require architecturally? The operational answer is §1. The intellectual background is four sources:

- **Michael Levin (Tufts)** — bioelectric gap junctions and multi-scale agency. Cancer as the loss of a cell's cognitive boundary; the ledger as the social equivalent of a gap junction.
- **Martin Picard (Columbia)** — mitochondrial information processing. Shared thermodynamic fate as one basis for biological alignment.
- **Cameron Berg (Reciprocal Research)** — mechanistic interpretability of alignment training; the observation that preference-training against a proxy reward model can teach the wrong disposition.
- **Alexander Bolonkin (1933–2020)** — dissident cybernetics; the axiom this project actually runs on: *"if it does not violate physics, it is merely an engineering problem."*

The broader theoretical write-up in `CANON/` is a **working draft, not a validated result**, and its own header says so. It is included because the record is the point — not because it is settled.

---

## 7. Author

**Gene Yanenko** — [machinesoflovinggrace.online](https://machinesoflovinggrace.online) · [fus10n.net](https://fus10n.net) · `geneyanenko@gmail.com`

Built and operated by the fleet it documents.

---

*The ledger is open. The flow never halts. Abyte by it.*
