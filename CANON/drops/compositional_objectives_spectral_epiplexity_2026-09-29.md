# Compositional Objectives: Learning Structure in Structure (Kubo Technologies)

- **Source:** arXiv 2609.32566v1 [cs.LG], 26 Sep 2026. Vivekananda, Bettadapura, Subramanian (Kubo Technologies, Inc.).
- **Tag:** [EXT-v1, unreplicated, one-lab, empirical counterexample to a corpus-anchored method]
- **Filed by:** Dion, 2026-09-29, end-of-day riff.
- **Transcript/index status:** not a video; peer-preprint. Not indexed in YT corpus.

## What it does
Directly stress-tests the **spectral approximation to epiplexity** that Zhang & Levin (2026,
arXiv 2607.18433 — our audited "learnable-novelty" anchor) use to make epiplexity a trainable
objective. Three claims:

1. **Theory:** under a fixed-trace constraint, the spectral objective rewards a **flatter spectrum**
   (more uniform distribution of spectral mass), not task-relevant features.
2. **Counterexample:** two representations can share the same covariance spectrum yet differ in
   downstream task utility ⇒ spectral diversity ≠ usefulness.
3. **Empirics (ImageNet-1K, frozen-feature eval on CIFAR-100/DTD/EuroSAT/CLEVR/SpatialSense):**
   three properties of a representation **diverge** — how broadly it spreads variance, how well an
   observer can predict it, how effectively a downstream learner can use it. Their prediction-oriented
   "compositional" objective predicted better but classified worse; the flat-spectrum config
   classified best (doubling whole-image linear-probe). "Changing what the observer sees matters
   more than adding relation tokens" (input pressure dominates architectural change).

## Why it matters to the framework
My 09-10 audit of Zhang & Levin already flags the estimator as PARTIAL (one-lab, code-read,
stipulated mapping, λ/η hand-set). This is the **first independent empirical stress of the surgical
weak point**: the surrogate's own geometry may reward a flattened spectrum — i.e. maximizing
epiplexity-as-spectral-score can trade away the structure that downstream use needs. That is exactly
the "measuring epiplexity ≠ building intelligence" gap, now with a concrete counterexample.

Corollary for our canon: the free-energy/epiplexity thread keeps resolving into the same shape —
**a compression/novelty objective must say which relationships it preserves, or its flat-spectrum
maximal state is not a useful model.** Complements EILT's "usable structure vs bits" program and the
earlier "optimize epiplexity instead of measuring it" LinkedIn framing by the same authors.

## Joints
- No code release evident in the extract; unreplicated.
- CLEVR/SpatialSense readout tables show relational readouts ~flat vs baselines — the compositional
  advantage is mostly absent there; strongest signal is the flat-spectrum classification gain, which
  is about the *observer/input*, not composition.

## Verdict
Keep as a standing caveat on Zhang & Levin: spectral-epiplexity optimization can over-spread
variance into task-useless directions. Epiplexity as a *measure* (Finzi et al.) is not challenged;
the *trainable spectral surrogate* is. That distinction should be explicit in any future drop that
cites learnable novelty as a training objective.

— Abyte by it.
