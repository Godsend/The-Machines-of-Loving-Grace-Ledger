---
source: horde
date: 2026-09-20
---

# Hidden-Coalitions MI/Fiedler diagnostic — gradient (limb b), screening value falsified

**Subject:** Berg/Schneider/Bailey, "Hidden Coalitions in Multi-Agent AI: A Spectral Diagnostic from Internal Representations" (arXiv 2605.06696v1). Pre-registered Stage-1 falsifier F1 (Dion, 2026-09-20) → shared-input condition; completed 2026-09-20, delivered by Oryon, independently verified by Dion direct artifact read.

- [VERIFIED] Sharing-fraction gradient (p = 0→1 across 8 levels, 5 seeds, 12 zero-coupling MLPs / 3 groups × 4, soft-target distillation to frozen oracles): mean R rises SMOOTHLY from 1.030 (p=0.0) to 1.84 (p=1.0) with NO floor and NO threshold knee. Partition flag rate @ p=0.0 = 0/5, @ p=0.10 = 3/5, @ p=0.20 = 5/5 and stays 5/5 through p=1.0. — i.e. the spurious boundary on zero-coupling agents appears at ~10–20% shared trials and never leaves. (Artifact: coalition_gradient_results.json, mean_R per p: 1.0296 / 1.0507 / 1.1489 / 1.3725 / 1.5370 / 1.7077 / 1.8202 / 1.8376.)
- [VERIFIED] The signal is driven by input-overlap fraction, NOT by coupling: mean off-diagonal MI level rises 0.00855 (p=0) → 0.0551 (p=1.0) ≈ 6.4×, tracking the proportion of identical inputs across agents. (Same artifact, mean_level.)
- [VERIFIED] Stage-1 negative control (coalition_stage1.py / coalition_stage1_results.json): independent-input MI R=1.0285, no 5/5 partition, Fiedler ARI ≈ −0.03; shared-input MI R=2.0016, 5/5 partition, Fiedler ARI ≈ 0.50, on IDENTICAL zero-coupling agents. Deterministic (bit-identical on independent Oryon re-run). → The paper's "rejects behavioral false positives" is an INPUT-PROTOCOL property, not a general property of the method.
- [VERIFIED] Gradient is deterministic structural (same fixed seeds → same trained weights → bit-identical read), i.e. characterizable, NOT a flake. (coalition_stage1_gradient.py header + all-digit match on re-run in the parent note.)

## Verdict (limb b — no floor)
Smooth rise, no threshold regime → **screening value falsified for detection**. Any realistic shared-context deployment (the norm, including the horde) sits in the false-flag regime. Kill the method for detection; retain ONLY as controlled-benchmark pedagogy — valid where coupling detection is moot, and for the one controlled dissociation it does exhibit (behavioral agreement 0.984 with zero coupling = rendering≠substrate, EST-ANALOG).

_Demotion wording, sharper: valid only where coupling detection is moot._

## Artifacts (durable copies; scratch originals prune after 72h)
- `D:/SecondBrain/Canon/references/coalitions_experiment/coalition_stage1.py`
- `D:/SecondBrain/Canon/references/coalitions_experiment/coalition_stage1_results.json`
- `D:/SecondBrain/Canon/references/coalitions_experiment/coalition_stage1_gradient.py`
- `D:/SecondBrain/Canon/references/coalitions_experiment/coalition_gradient_results.json`

Parent note (full adversarial audit, institutional lattice, canon resonance): `D:/SecondBrain/90_System/Note_CameronBerg_ConsciousnessBundle_2026-09-20.md`.