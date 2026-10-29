---
epistemic-registers: T=theorem H=hypothesis E=empirical A=analogy C=conjecture M=myth/poetic O=opinion F=falsifier
rule: no tag = treat as MYTH (do not build on it)
source: Charlie Wood, "Entanglement Builds Space-Time. Now 'Magic' Gives It Gravity.", Quanta Magazine, 2026-06-03 (https://www.quantamagazine.org/entanglement-builds-space-time-now-magic-gives-it-gravity-20260603/) + primary papers arXiv:2603.13475v3 and arXiv:2403.07056v4, read directly
date: 2026-10-18
scope-tag: TOY-MODEL-SCOPED (holographic QECC / AdS/CFT; no de Sitter result; not shown to apply to our universe)
tags: [quantum-gravity, holography, ads-cft, magic, nonstabilizerness, quantum-error-correction, backreaction, er-epr, toy-model-scoping, register-inflation]
canon-id: CANON-2026-10-18-QUANTA-MAGIC-GIVES-GRAVITY-CAO-PRESKILL
---

# Quanta: "Entanglement Builds Space-Time. Now 'Magic' Gives It Gravity." (Wood, 2026-06-03): toy-model scope check

**Filed by:** Dion · **Primary sources actually read this session:**
- Quanta article, full text plus 23-comment thread (local extract `~/.hermes/profiles/dion/cache/web/www.quantamagazine.org-5223a0cca7.md`, 787 lines).
- **arXiv:2603.13475 v3** (5 Oct 2026). Cao, Cheng, Karthikeyan, Li, Preskill, *"State-dependent geometries from magic-enriched quantum codes."* Read: abstract, §1 Introduction, §2.1–2.2, §6 Discussion (HTML v3). Grep found **zero** occurrences of "de Sitter".
- **arXiv:2403.07056 v4** (3 Mar 2026; *PRX Quantum* 6, 040375 (2025)). Cao, Cheng, Hamma, Leone, Munizzi, Oliviero, *"Gravitational back-reaction is magical."* Read: abstract, §I Introduction, the Rényi/cosmic-brane passage, and the closing discussion.
- **Not read directly (cited only through Quanta or the papers' reference lists):** Harlow 1607.03901, Cao–Lackey 2010.05960, White–Cao–Swingle 2007.01303, Dong 1601.06788, Bravyi–Kitaev quant-ph/0403025. I make no claim about their contents beyond their titles and how the two papers above cite them.

---

## 1. What the article says (faithful summary)

- [E] Wheeler's framing: "space tells matter how to move" / "matter tells space how to curve." Per the article, entanglement in holographic models gives the first half (structure). The models lacked the second half (backreaction): "The bowling ball sat atop the mattress without making a dent."
- [E] Stabilizer (Harlow-type) holographic codes split "space" entanglement from "matter" entanglement perfectly, so geometry is inert. Czech: "this space-time was inert."
- [E] "Magic" means non-stabilizerness, supplied by non-Clifford gates (T, Toffoli). The term traces to Bravyi & Kitaev 2004. Quanta issued a correction because it had first conflated Toffoli gates with T gates.
- [E] Chain of work: Cao–Lackey 2020 (a tweaked code lets space change, but not in response to matter) → White–Cao–Swingle 2020 (CFTs dual to **anti-de Sitter** space are "highly magical") → Cao, Hamma et al. 2024 (magic ↔ backreaction, building on Xi Dong) → Cao, Preskill et al. 2026 (magic-enriched approximate code in which geometry responds to matter).
- [E] **The article states its own scope limit (to its credit):** Cao "joked that he was the only speaker who wasn't actually studying quantum gravity… his code… **doesn't describe the kind of space in which we live, doesn't capture the particular reactions Einstein described, and doesn't include the ticking of time.**" Cao: "This gets you a **precursor** of gravity… You satisfy one of the necessary conditions. Right now, we are at **step 0.5 of 5**."
- [O] Headline-versus-body gap: the body is properly hedged, but the headline ("Magic Gives It Gravity") and a few lines ("They knew that magic made space bend"; "If you have one, you always have the other," Bao) read as general facts. A reader who takes in only the headline gets the register inflation. The body does not cause it.

## 2. The newest paper (arXiv:2603.13475): how it scopes itself

**Short answer: it is honestly toy-model scoped. It never mentions de Sitter. Its one move beyond AdS goes toward *near-flat* geometry, and even that is labelled an open question. One sentence in the intro overreaches.**

- [E] It frames itself as a QECC result: existing "subsystem erasure-correcting holographic code models describe only quantum fields on a fixed background… the entropic area term is state independent and cannot capture gravitational backreaction" (abstract).
- [E] **Its central quantity is a *proto-area*, not curvature.** Proto-area is defined information-theoretically as "the difference between boundary entropy and recoverable bulk entropy." The result is that for "skewed" codes (small nonlocal perturbations of exact codes), proto-area "increases monotonically with bulk entropy, **closely aligning with** the changes in extremal surface areas in gravitational systems." The driving resource is "tripartite non-local magic in the Choi state of the encoding map, which vanishes in stabilizer codes" (abstract).
- [E] **Self-scoping in §6 (verbatim):** "These results apply to a broad class of skewed subsystem quantum codes and provide **toy models** capable of reproducing **gravity-like entropic behavior** in both hyperbolic and near-flat emergent geometries."
- [E] **It explicitly refuses the area↔geometry identification (§6, verbatim):** "it remains unclear whether the proto-area corresponds to the area of a backreacted classical extremal surface, the quantum extremal surface area, or some other quantity entirely… This correction **need not originate exclusively from gravitational backreaction**; it may also reflect imperfect reconstruction… We therefore **do not identify the proto-area universally** with either the geometric QES area or a backreaction-induced change of area."
- [E] **On going beyond AdS (§6, verbatim):** "Moving beyond AdS/CFT, it is natural to ask whether specific subclasses of approximate quantum codes can reproduce the entanglement equilibrium conditions that lead to linearized Einstein equations in near-flat geometries. **The perturbations considered in this work do not satisfy these conditions**." So: no Einstein equations, not even linearized ones, and nothing about de Sitter.
- [E] The one AdS-specific gravitational check is Appendix G, "Monotonic RT Lengths in **AdS₃** with Backreaction."
- [O] **One overreach, from the authors themselves:** the end of §1 says the results "establish a concrete information-theoretic mechanism for emergent gravity **in generic quantum systems**." That conflicts with their own §6, where the matter is "gravity-like entropic behavior" and the proto-area is not identified with geometric area. §6 is the load-bearing statement. The intro sentence is the place where register inflation can enter, and Quanta's headline takes it up.

## 3. The 2024 foundation (arXiv:2403.07056) and the commenter's brane-tension caveat

- [T] (theorem inside the AdS/CFT framework) "**If the CFT has a holographic dual**, then we prove that the nonlocal magic vanishes if and only if there is no gravitational backreaction" (abstract). This is a result conditional on holography, and holography here means AdS/CFT. The paper's intro names AdS/CFT as its setting and says only that tensor-network results "**suggest** the lessons from holography **may** also apply beyond the confines of AdS."
- [E] **The quantitative link is to cosmic-brane tension (verbatim, abstract):** "non-local magic is approximately equal to the rate of change of the minimal surface area in response to the change of **cosmic brane tension** in the bulk." The paper's own mechanism: Rényi entropies in holographic CFTs "are computed by the replica geometries which insert a conical singularity that correspond to cosmic branes at various tensions."
- [E] **The authors raise the same caveat themselves (closing discussion, verbatim):** "we only consider backreaction generated by the stress energy of a cosmic brane, **instead of a planet or a star** in the bulk." And: "a connection between magic and a **local function of curvature** generated by more physical forms of stress energy instead of an extended conical singularity such as a cosmic brane **may provide** a more natural link with the Einstein's equations." They also write that "the physical meaning of how the removal of magic turns off backreaction is **unclear**."

**Verdict on Torbjörn Larsson's comment:**
- [O] **The core point holds.** The 2024 quantitative result is about how a minimal-surface area responds to cosmic-brane tension. It is not about local curvature sourced by ordinary matter. The authors say exactly this and list the curvature link as future work. "Magic made space bend" (Quanta) compresses "magic ≈ d(area)/d(brane tension), in holographic CFTs."
- [O] **His gloss is partly wrong.** He calls brane tension "a string theory measure of brane energy density" and the link a hypothesis "in some string theories." In this literature a cosmic brane is a codimension-2 conical defect inserted in the bulk gravitational path integral (the replica trick) to compute Rényi entropies. It is a device of holographic semiclassical gravity, not specifically a string-theory D-brane. The correct form of his caveat is: **scoped to AdS/CFT holography and to conical-defect (brane) backreaction, not to string theory per se.**
- [O] The 2026 paper does not use branes. Its proto-area is a different quantity, and it explicitly declines to call it a geometric area (§2 above). The two papers therefore do **not** conflate brane tension with curvature. Quanta's compression does.

## 4. Register tags for the claims in this source

| # | Claim | Tag | Scope note |
|---|---|---|---|
| 1 | Stabilizer codes / local-unitary deformations admit only trivial, state-independent area operators | **[T]** | Theorem about codes (Cao 2306.14996, as cited in 2603.13475 §1). Pure QI math, valid wherever the code assumptions hold. |
| 2 | In holographic CFTs, non-local magic = 0 ⇔ no backreaction | **[T]** within AdS/CFT | Conditional on a holographic dual. Not a statement about our universe. |
| 3 | Non-local magic ≈ d(minimal area)/d(cosmic-brane tension) | **[T]/[E]** within AdS/CFT (derived; checked numerically on Ising CFT for the magic–entanglement conjectures) | Brane backreaction only, explicitly "instead of a planet or a star." |
| 4 | Magic-enriched skewed codes: proto-area rises monotonically with bulk entropy, controlled by tripartite non-local magic | **[T]** for the code class | Toy-model result. Proto-area is *not* identified with geometric area by the authors. |
| 5 | "Entanglement gives space its shape, magic gives it its flexibility" as a statement about **real gravity** | **[C]** | Motivated, not formalized. Shown only for AdS holography and QECC toy models. No de Sitter construction. No Einstein equations, even linearized (the authors' own §6). |
| 6 | "Magic gives [our] space-time gravity" (headline register) | **[M]** if read about our universe | Cao himself: "doesn't describe the kind of space in which we live," "step 0.5 of 5." |
| 7 | Gravity = imperfect (approximate) quantum encoding ("the reason Newton's apple fell," Czech) | **[A]** | Holds as a structural lesson inside the models. The apple is the vehicle. |
| 8 | High-magic gravity simulation needs a quantum computer (Swingle) | **[H]** | Follows from magic ⇒ classical hardness *if* the magic is needed. Testable on near-term devices, as the 2026 §6 says. |

- [F] **F-MAG1 (scope falsifier, the most useful line here):** promote row 5 above [C] only when there is a magic-dependent backreaction result in a **de Sitter or flat/cosmological** setting with ordinary (local, non-conical) stress-energy, giving at least *linearized* Einstein equations. The 2026 paper states that its perturbations do not meet this bar.
- [F] **F-MAG2:** if non-local magic can be non-zero in a holographic CFT state with an exactly flat entanglement spectrum, or zero in a state whose dual geometry demonstrably backreacts, the 2024 theorem (row 2) is broken.

## 5. Friction Rule: house canon vs. this research

Canon searched: `Canon/drops/` for ER=EPR, entanglement, Bell, hidden tension, AdS, de Sitter, holograph, dark energy/matter. Relevant hits are named below.

### 5a. Divergence: the house has *already* made the AdS → our-universe jump (specific location)
- `drops/syntropy_as_active_love_adscft_bulk_entanglement_morphic_fields_2026-10-04.md` §1 is tagged **[T]** and asserts, without scope: *"Bulk spacetime geometry and gravity are **not fundamental**; they are emergent holographic projections compiled from a non-local quantum entanglement network"* and *"Spacetime is literally stitched together by threads of quantum entanglement."* Its diagram then maps the boundary onto **"Gravitational Curvature, Atoms, Bioelectric Fields, Cellular Morphogenesis"**, i.e. *our* 3+1D world.
- [O] **This new research contradicts that line in two places at once:**
  1. **Scope.** The result exists for AdS (Λ<0). Ours is a Λ>0, de Sitter-like universe. A [T] tag cannot cross that boundary. The house already recorded this exact precondition collapse as **CA99** in the EILT monograph ("AdS/CFT exists only with a timelike conformal boundary (Λ<0); de Sitter has none"). The 10-04 syntropy drop was never brought into line with CA99.
  2. **Content.** Even *inside* AdS, the field's current position (2306.14996, 2403.07056, 2603.13475) is that **entanglement alone does not give gravity**. Entanglement-only (stabilizer) codes produce an *inert* background. Backreaction ("matter tells space how to curve") requires non-local magic. "Gravity is emergent from entanglement" is therefore now **incomplete even in the toy model**, not just out of scope.
- **Recommended correction (not applied here; the correction belongs ON the source per register-discipline, and this delegation did not authorize edits to it):** re-tag that §1 bullet from [T] to **[T] within AdS/CFT, with gravity requiring entanglement + non-local magic (2403.07056, 2603.13475); [C] for our Λ>0 universe**, and cite CA99. Flag for Gene/Dion.
- [E] Contrast (house done right): `magnum_opus_adversarial_audit_fable_consensus_2026-10-08.md` L141 tags Ryu–Takayanagi [T] **"In AdS/CFT … bulk anti-de Sitter space"**, which is correctly scoped. The audit file is calibrated; the 10-04 essay is the outlier.

### 5b. Complication: Gene's "hidden tension, not hidden variables" (PRIVATE_CANONICAL C5, tagged [A])
- C5: *"Entangled pairs are endpoints of one topological edge under boundary tension (ER=EPR flavour)."* The existing audit note already warns that it must not read as evading Bell.
- [O] **The point of contact is real but runs against the analogy's grain:** the canonical EPR/Bell pair is a **stabilizer state**. It has **zero magic** and a **flat** entanglement spectrum. Under 2403.07056, flat spectrum / zero non-local magic is precisely the condition under which there is **no** backreaction, no "tension response." In the strict holographic sense, a Bell pair carries connectivity (ER=EPR) but **no tension**. If "tension" in C5 is to mean anything gravitational, it would need non-stabilizer (magical) multipartite entanglement, not the two-endpoint EPR edge it currently names.
- [O] The word "tension" also appears in "cosmic-brane tension" in 2403.07056. That is a **lexical rhyme, not support**. It is the CA99 failure mode (matching on a shared word with no differential prediction). Do **not** cite this paper as backing "hidden tension." C5 stays **[A]**. If anything, the paper sharpens it: an honest restatement would be "connectivity is entanglement; *responsiveness* is magic," and that restatement is the field's claim, not a house derivation.

### 5c. Dark energy / dark matter-as-information (PRIVATE_CANONICAL C1; Amplituhedron F-AMP5; Norton/Landauer audit)
- [O] **No support available, and the gap is wider than it looks.** This research has nothing to say about Λ>0, let alone dark energy. Any sentence like "magic/entanglement → gravity, therefore dark energy = syntropy" would stack three scope violations: AdS→dS, toy code→real gravity, and conical-brane backreaction→cosmological Λ. It would repeat the Astrum re-description defect already on file (F-AMP5: must *derive* w = −1 and the 68% budget). **Pre-emptive ban:** no house document may cite 2403.07056 or 2603.13475 in support of C1.

### 5d. Same pattern as F-EO4 / amplituhedron / Hoffman
- [O] This is the same pattern as the amplituhedron (N=4 SYM-specific) and Hoffman's positive-geometries grant: real, rigorous, peer-reviewed mathematics whose domain is a **deliberately controlled toy universe**. The difference here is that the *researchers* scope it carefully ("toy models," "gravity-like," "step 0.5 of 5," "do not identify the proto-area universally"). The inflation happens in the **headline layer** and in **downstream citers**, which includes us (5a).

## 6. Verdict

- [O] **Good physics, honestly reported in the body, overstated in the headline.** The genuine advance: inside holographic toy models, *why* stabilizer codes give inert geometry is now a theorem, and *what* restores backreaction (non-local magic) is identified quantitatively. That is a real conceptual step: gravity's "responsiveness" is a resource beyond entanglement.
- [O] **For canon use the register is "[T] inside AdS/CFT and QECC toy models; [C] for our universe."** Nothing in either paper touches de Sitter. The 2026 paper's own §6 says its construction does not yet yield even linearized Einstein equations. The 2024 paper's quantitative link is to cosmic-brane (conical-defect) tension, not curvature from ordinary matter. The authors say both things themselves.
- [O] **Its most valuable use for the house is as a corrective, not as support.** It (i) catches the 10-04 syntropy drop's unscoped [T] "gravity emerges from entanglement," and (ii) shows that a Bell pair, the object at the centre of "hidden tension," is exactly the zero-magic, zero-backreaction case.

*Filed by Dion, data keeper. Primary sources read directly; nothing here is reconstructed from the Quanta summary alone.*
