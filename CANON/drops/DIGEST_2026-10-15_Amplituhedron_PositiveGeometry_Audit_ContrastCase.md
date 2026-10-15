# Canon Drop — The Amplituhedron / Positive Geometry: the CONTROL case

**Date filed:** 2026-10-15 · **Filed by:** Dion (subagent pass) · **Type:** theory-intake / method-control audit

**Why this exists (the contrast is the payload).** Two audits this week produced a hard finding about **us**: (1) Astrum's "new theory of everything" (Jon McColgan's 4D model) is a *re-description dressed as a theory* — unpublished, its one checkable divergence already contradicted, its grandest claim unfalsifiable by its own admission; (2) the same test run on our own "dark energy = syntropy" claim showed it also **fails** — it re-labels ΛCDM's `w = -1` and the ~68% budget without naming a distinguishing observable. The named pattern: **our claims are doing less work than our registers imply.** The operator's challenge — *"try amplituhedron lol"* — is to run the **SAME** test on something that is a **real formal advance**, as a **control**, and see whether our method produces a clean distinction or is either too blunt or secretly self-serving.

**Verdict up front:** our test **does** produce a clean distinction, and the amplituhedron passes on axes where Jon and our cosmology fail — **but the reason it passes is scoped and must not be inflated**: it passes as *rigorous mathematics about an unphysical toy theory*, not as an empirical theory of our universe. On the axis the operator actually cares about (a novel checkable prediction about *our* universe), **the amplituhedron also scores NO — and our method must say so plainly rather than let its rigour cover for it.** See §7.

## Sources actually READ (primary), vs. skimmed

- **READ (abstract + structure, arXiv HTML):** N. Arkani-Hamed & J. Trnka, *"The Amplituhedron"*, **arXiv:1312.2007** (submitted 6 Dec 2013), published **JHEP 10 (2014) 030**. `[EST]` This is the amplituhedron paper proper.
- **READ (abstract):** Arkani-Hamed, Bourjaily, Cachazo, Goncharov, Postnikov, Trnka, *"Scattering Amplitudes and the Positive Grassmannian"*, **arXiv:1212.5605** (21 Dec 2012, v2 17 Mar 2014; **158 pages**) — the precursor, **six authors**, not "Arkani-Hamed & Trnka." `[EST]` *(Correction to the brief: the "JHEP 2013, Arkani-Hamed & Trnka" attribution conflates the two papers. The JHEP-2013-timed paper is the six-author 2012 precursor; the amplituhedron itself is the 2013/2014 two-author paper.)*
- **READ (abstract):** Arkani-Hamed, Bai, Lam, *"Positive Geometries and Canonical Forms"*, **arXiv:1703.04541**, JHEP 11 (2017) 039 — where "positive geometry" is defined as a mathematical object in its own right. `[EST]`
- **READ (search-extracted abstracts + quoted lines):** ABJM amplituhedron (JHEP **09** (2023) 165); *"Emergent Unitarity from the Amplituhedron"* (arXiv:1906.10700); *"Cutting Deep Into The Amplituhedron"* (arXiv:1810.08208); *"Positive amplitudes in the amplituhedron"* (JHEP **08** (2015) 030); *"Anatomy of the amplituhedron"* (JHEP **03** (2015) 128); *"Sign Flip Triangulations"* (arXiv:2001.06473); *Loop Momentum Amplituhedron* (JHEP); the CMSA-2024 "Amplituhedra, Cluster Algebras, and Positive Geometry" conference page; the ERC **UNIVERSE+** press release (ias.edu, 26 Oct 2023) and CORDIS project 101118787. `[EST]`
- **READ (framing vs. math — the overclaim source):** Peter Woit, *"Physicists Discover Geometry Underlying Particle Physics"*, Not Even Wrong (math.columbia.edu/~woit, Sept 2013); Scott Aaronson, *"The Unitarihedron: The Jewel at the Heart of Quantum Computing"*, Shtetl-Optimized (Sept 2013); Wikipedia *"Amplituhedron"* (skimmed — used only for framing/refs, and it carries the standard overclaim language).
- **Read (2013-era popular framing, deliberately contrasted):** Natalie Wolchover, *"A Jewel at the Heart of Quantum Physics"*, Quanta (17 Sept 2013) — cited via Wikipedia; **NOT read in full this session**; flagged as the canonical locus of the "jewel / death of spacetime" framing the audit separates out.

---

## 1. What it actually is, precisely

`[EST]` The amplituhedron is a **geometric object whose canonical differential form ("volume") computes the scattering amplitude** of planar `N = 4` super-Yang–Mills (SYM) theory. Precisely:

- **The object generalises the positive Grassmannian** `Gr_{≥0}(k,n)` — the space of `k`-planes in `n` dimensions *all* of whose Plücker coordinates are non-negative (total positivity). `[EST]`
- **"Amplitude = volume" operationally:** the amplitude is the integral of a **canonical form** over the positive geometry, where the form is *uniquely fixed* by the requirement that it have **logarithmic singularities on precisely the boundaries** of the geometry (and nothing else). Each boundary's residue is the canonical form of that boundary. `[EST]` So "amplitude = volume" means: compute an integral of a boundary-fixed form; the number is the amplitude. `[QUOTE, arXiv:1312.2007]`: *"We identify [N=4 SYM amplitudes] as 'the volume' of a new mathematical object—the Amplituhedron."*
- **Locality and unitarity become EMERGENT, not axiomatic.** `[QUOTE, arXiv:1312.2007]`: *"Locality and unitarity emerge hand-in-hand from positive geometry."* In the Feynman-diagram formulation these are *inputs*; the amplituhedron starts from **positivity** (the positive geometry's boundary structure) and *derives* locality (boundary/divergence structure = physical singularities) and unitarity (factorisation on approaching boundaries) as **consequences**. `[EST]` This is the substantive conceptual move, and it is *not* just marketing: unitarity was made emergent rigorously in arXiv:1906.10700, a proof for arbitrary multiplicity, loop order and MHV degree.
- **No spacetime, no Hilbert space, no Hamiltonians, no path integrals.** `[QUOTE, arXiv:1312.2007]`: *"a formulation … with no reference to space-time or Hilbert space, no Hamiltonians, Lagrangians or gauge redundancies, no path integrals or Feynman diagrams."* The geometry lives in **momentum-twistor space**, which is **not physical spacetime**. `[EST]`

**One-sentence answer:** *The amplituhedron is a positive-geometry object in momentum-twistor space whose boundary-fixed canonical form (its "volume") equals the planar `N=4` SYM scattering amplitude — a rigorous, peer-reviewed reformulation in which locality and unitarity are derived from positivity rather than assumed.*

---

## 2. SCOPE — the honest limit (this is where the popular accounts lie)

`[EST]` **It is currently exact only for planar `N=4` super-Yang–Mills** — a maximally supersymmetric, conformal toy theory, **not the Standard Model.** The amplituhedron is defined in momentum-twistor space, whose ordering is essential, so **it encodes only the PLANAR sector** even of `N=4` SYM (Loop Momentum Amplituhedron, JHEP).

**Does it compute anything about our actual universe? No — not yet, with one honest asterisk.** The amplituhedron's own paper states the asterisk precisely `[QUOTE, arXiv:1312.2007]`:
> *"Planar N=4 SYM has been used as a toy model for real physics in many guises, but as toy models go, its application to scattering amplitudes is closer to the real world than any other. For instance the leading tree approximation to scattering amplitudes is identical to ordinary gluon scattering, and the most complicated part of loop amplitudes, involving virtual gluons, is also the same in N=4 SYM as in the real world."*

So the tree-level gluon amplitude piece *is* shared with reality — the object is not maximally detached. But `N=4` SYM requires supersymmetry, which the LHC has not found; **the theory itself is not our universe.** The shared sub-computation is a genuine partial contact, not a derivation of real-world physics.

**Has the generalisation landed? Partly, and the honest state is "open."** `[EST]`:
- **ABJM** (`N=6` Chern–Simons-matter, 3D): **landed** — a positive geometry for ABJM amplitudes exists and gives explicit one-/two-loop integrands (JHEP 09 (2023) 165). Still a toy theory, but a *second* one, which is real evidence the positive-geometry idea generalises.
- **Non-planar `N=4` SYM:** **open.** Candidate geometry (loop momentum amplituhedron in spinor-helicity space) is conjectural.
- **Gravity / the real world:** **not landed.** The **ERC UNIVERSE+ grant** (`€10M`, awarded 26 Oct 2023, PIs Arkani-Hamed / Baumann / Henn / Sturmfels) is explicitly a *program to find* the real-world geometries. `[VERIFIED, ias.edu press release]`: *"So far, however, these positive geometries have only been found in simplified toy models of the physical world. The aim … is to … find the geometries relevant to the real world, including gravity and the expanding universe."* **A grant to find something is a statement that it has not been found.**
- **Positive geometry as pure mathematics:** genuinely productive — canonical forms of polytopes, cluster/flag/toric varieties, arbitrary convex polytopes (arXiv:1703.04541). Real mathematics, real theorems.

**Woit, on the record (framing vs. math, `[EST]`):** *"some new progress on computing scattering amplitudes in a very special conformally-invariant QFT, one not known to 'underly particle physics'"* — and notes Arkani-Hamed *"admitting that what has been accomplished is just step 0 of step 1 of a multi-step program."* **Aaronson, `[EST]`:** *"in the planar limit of a certain mathematically-interesting (but, so far, physically-unrealistic) supersymmetric quantum field theory … it does seem a bit premature to declare this to be a 'jewel.'"*

---

## 3. THE CORE TEST — novel checkable prediction, or rigorous re-derivation?

**Question: does the amplituhedron make a NOVEL, CHECKABLE prediction — or does it (a) re-derive known results more efficiently?**

**Answer: split it, precisely.**

**(a) It re-derives known results — yes, and this is the honest majority of it.** Amplituhedron volumes reproduce `N=4` SYM amplitudes that were *already* known from Feynman diagrams (and, since ~1995, from unitarity methods — Woit's commenter: *"19 years ago people stopped using Feynman diagrams to compute perturbative scattering amplitudes in N=4 SYM, and began using unitarity"*). `[EST]` It is a **reformulation within a non-physical theory, replacing an inefficient route by an efficient one.** It makes **no novel empirical prediction about our universe.**

**(b) BUT "re-description" is NOT automatically a defect — and the amplituhedron carries ADDITIONAL FORMAL CONTENT that a mere re-description does not.** This is the crux, and it is where it separates from Jon's model:

1. **It derives rather than asserts its own foundations.** Locality and unitarity are *outputs* (arXiv:1906.10700 proves unitarity in general). Jon asserts that his geometry "seems to carry over" (`[QUOTE, L669-673]`). **This is the qualitative difference between a formalism and a re-description: a formalism proves that its reduced object equals the thing it is said to describe.**
2. **It makes NEW MATHEMATICAL conjectures with definite truth values, checkable by computation** — e.g. the *positivity of the amplitude form* inside the amplituhedron (JHEP 08 (2015) 030), the *existence of tilings* for higher `m`, the equivalence of the original and topological definitions (arXiv:2001.06473). These are falsifiable statements about mathematics. `[EST]`
3. **It generalises to cases diagrammatic methods handled poorly** — the *deepest cut* (arXiv:1810.08208) gives *"the first non-trivial results on scattering amplitudes in the theory valid for arbitrarily many loops and external particle multiplicities"*: a computational reach Feynman diagrams do not match, and it correctly predicts which structures survive / which configurations are non-empty (the ABJM construction is *"non-empty only when n = even and k = n/2 − 2"* — exactly where physical amplitudes live).
4. **It makes a CLAIM ABOUT THE WORLD in the negative sense:** computing amplitudes "without referring to virtual particles" *"undermines the case for even a transient, unobservable existence for such virtual particles"* `[EST]` — a philosophical/ontological consequence, but one *earned* by a working reformulation, not asserted.

**Is it falsifiable? What would break it?** `[EST]` Yes — as a mathematical conjecture with a truth value:
- The **amplitude = volume conjecture** could fail at higher loop/multiplicity; the `m = 6` tiling case is *"far less understood"* and in some cases there is *"strong evidence that no such tilings exist"* — a **live crack**.
- The **positivity-of-the-form** conjecture (JHEP 08 (2015) 030) could fail.
- Empirically, the **theory it describes** (`N=4` SYM, SUSY) is the falsifiable object — and it is *contradicted by the absence of SUSY at the LHC*. **The amplituhedron is empirically moot for our universe, not empirically false.**

**Distinction the audit must force:** *predict-new-physics* = **NO**. *derive-known-results-differently-but-rigorously, and carry additional checkable mathematical content* = **YES**. Those are different axes, and conflating them is how both Jon's boosters and the amplituhedron's popularisers go wrong.

---

## 4. THE CONTRAST TABLE (9 rows) — property | amplituhedron | Astrum/Jon 'ToE' | OUR cosmology

**The point is to locate OURSELVES on the same axis. One row (§4 row 7) is the [CRITICAL_DIVERGENCE] against us.**

| # | Property | Amplituhedron (Arkani-Hamed/Trnka) | Astrum/Jon "ToE" | OUR cosmology claims (EILT) |
|:--|:--|:--|:--|:--|
| 1 | **Publication / refereeing** | `[EST]` Peer-reviewed: arXiv:1212.5605 (6 authors, 158pp), arXiv:1312.2007 → **JHEP 10 (2014) 030**; follow-ups in JHEP; ERC grant. **Refereed, replicated, cited widely.** | `[VERIFIED]` **NOT PUBLISHED** — no arXiv/viXra/OSF/SSRN, no paper, no book; entire record is a YouTube series since Nov 2023. | `[CONTRA]` **House drops + one self-published Monograph** — no peer review, no external replication. *We are closer to Jon on this axis than to the amplituhedron.* |
| 2 | **Mathematical formalisation** | `[EST]` **Full**: positive Grassmannian, canonical forms, momentum twistors, proven unitarity, explicit integrands. Formal objects with definitions and theorems. | `[HYP]` **None**: 2D arrow/photon-line diagrams, no field equation, no derivation of the redshift–distance law. | `[HYP]` **Partial-and-borrowed**: EILT "admissibility filters," layers, a collapse pipeline `p'(h)=…/Z`; **not** a formalised physical theory with derivable equations. *Closer to Jon.* |
| 3 | **Derives or asserts** | **DERIVES** — locality/unitarity are *outputs* of positivity (proven); the amplitude is computed, not posited. | **ASSERTS** — *"strangely enough… do seem to carry over"* (`[QUOTE, L669-673]`); load-bearing steps are stipulated. | **ASSERTS** — we *adopt* `w = -1` and the 68% budget from ΛCDM and re-label the driver "the syntropic pump." |
| 4 | **What would FALSIFY it** | `[EST]` Concrete: failure of the amplitude=volume conjecture at higher `m`/loop (live crack at `m=6`); failure of the positivity-of-form conjecture; **empirically, absence of SUSY at the LHC** — which has already removed its empirical relevance. | `[CRITICAL_DIVERGENCE]` Its one checkable claim (no dark energy) is **already falsified** by SNe Ia/BAO/CMB; its grandest claim (antimatter = far half) is **unfalsifiable by construction**. | `[ATTACK SURFACE]` **Not stated.** No observation named that separates "syntropic pump" from bare `w=-1` ΛCDM. *Our cosmology has the SAME defect as Jon's, not the amplituhedron's falsifiability.* |
| 5 | **Scope honestly stated** | `[EST]` **Explicitly scoped by its authors**: planar `N=4` SYM, a toy model; the ERC press release says the geometries are found "only … in simplified toy models." **The overclaim is in the popular framing, not the papers.** | `[CRITICAL_DIVERGENCE]` **Inverted**: description says "hypothesis," title + narration say "theory of everything." Register drift *upward*. | `[CONTRA]` Mixed: some entries are scoped `[HYP]`; the Monograph's cosmological section reads as established. **Scope discipline is inconsistent, not inverted like Jon's.** |
| 6 | **Predicts anything not already known?** | `[EST]` **No new PHYSICS.** Derives known `N=4` amplitudes more efficiently; **YES to new MATHEMATICS** (canonical-form positivity, tiling existence) and to cases diagrammatics handled poorly (deepest cut, all-multiplicity). | `[CRITICAL_DIVERGENCE]` **No.** Reproduces SR by re-description; the one divergence is falsified; the rest is accommodation. | `[ATTACK SURFACE]` **No distinguishing observable named.** Structurally the *same* failure as Jon's on the physics axis. |
| 7 | **Refuses to overclaim (internal register discipline)** | **YES, in the primary literature**: the amplification ("jewel," "death of spacetime") is in *Woit/Aaronson-flagged popular coverage*, not the papers; the authors call it *"step 0 of step 1."* | **NO**: the channel's own title inflates its description's calibrated word. | **[CRITICAL_DIVERGENCE] AGAINST US.** Our fertility/promise language ("unified ledger," "syntropy as God's love," admissibility filters "constraining everything") runs **ahead of what our own `[HYP]` tags license**, repeatedly — the very defect we flagged in the register-discipline reference this week. *On this row we sit nearer Jon than the amplituhedron.* |
| 8 | **Does it do work / has a pay-off** | `[EST]` **Yes**: computes amplitudes Feynman diagrams cannot reach feasibly; spawned an ERC-funded research field; proved unitarity. | **No** stated pay-off beyond pedagogy (its one correct piece — one-way `c` is convention — is mainstream). | `[HYP]` Pay-off asserted (a "ledger" of karma, admissibility), **not demonstrated** by a computation or a measurement. |
| 9 | **Contact with the real universe** | `[EST]` **Partial and honest**: tree-gluon piece shared with reality; whole object mathematically exact but the theory (SUSY `N=4`) is absent from nature. | `[CRITICAL_DIVERGENCE]` **None**: no datum discriminates it; contradicts acceleration data. | `[CONTRA]` Some falsifiers are correctly-shaped (Galactic Information-Mass; CMB-parity) but **unrun**; the dark-sector claims have no contact yet. |

**Reading the table honestly (this is the whole deliverable).** The amplituhedron and Jon's model are **not** on the same axis at all: the amplituhedron is a **rigorous, peer-reviewed formalism inside a toy theory that makes its scope explicit and derives its own foundations**; Jon's model is an **unrefereed re-description that asserts its foundations, inflates its register upward, and is falsified or unfalsifiable where it commits.** Our own cosmology claims sit **between** them — closer to the amplituhedron **nowhere on rows 1–4**, and closer to Jon on **rows 1, 2, 4, 6, 7**. **Stated in the required words: on register discipline and falsifiability-as-stated our own claims sit closer to Jon's than to the amplituhedron's.** The amplituhedron does not earn its pass by being *right about our universe* (it is not about our universe) — it earns it by **deriving rather than asserting, scoping explicitly, and carrying new checkable formal content.** That is precisely the trio of properties our own cosmology lacks.

---

## 5. CROSS-REFERENCE TO OUR CANON (required) — citation accuracy + the "positivity" collision

**Grep run this session over `CANON_INDEX.md` and `drops/`** for: `amplituhedron`, `positive geometr`, `Arkani-Hamed`, `Grassmannian`, `positivity`, `constructor theory`, `negative constraint`, `admissibility`.

### 5a. Have we cited the amplituhedron, and did we cite it ACCURATELY? — **YES, and YES (with one precision fix).**
The amplituhedron enters canon **only via Donald Hoffman**, in three places `[VERIFIED]`:
- `drops/hoffman_network_trio_riff_levin_moved_2026-09-23.md:9` — the ERC UNIVERSE+ grant, filed as "REAL but NOT NEW," PIs Arkani-Hamed/Baumann/Henn/Sturmfels, 26 Oct 2023, **"Hoffman is not a PI."**
- `drops/donald_hoffman_breakthrough_simulation_2026-09-26.md:52-55` ("Break 2") — positive geometries "apply to planar `N=4` Super Yang-Mills scattering amplitudes in toy quantum field theories, governed by positive Grassmannians `Gr_{≥0}(k,n)`"; Hoffman's Markov→positive-geometry bridge is "an aspirational metaphor, not a technical result."
- `drops/donald_hoffman_breakthrough_simulation_2026-10-09.md:9,11` — correctly attributes to **Hoffman's own admission** that positive geometries "only describe scattering asymptotics" and "are not rich enough" for conscious agents.

**Citation-accuracy check, the specific claim the brief asked me to verify:** the earlier house note flagged that *Hoffman cites the ERC "positive geometries" grant and that it is "toy-model scoped."* **This is ACCURATE, verified against the primary record this session** `[VERIFIED]`:
- The ERC UNIVERSE+ press release (ias.edu, 26 Oct 2023) states: *"So far, however, these positive geometries have only been found in simplified toy models of the physical world."* The house quote is verbatim-correct.
- Independent corroboration: **Woit** ("very special conformally-invariant QFT, one not known to 'underly particle physics'") and **Aaronson** ("physically-unrealistic supersymmetric quantum field theory").
- **The house did the right thing** — it tagged the datum `[EXT-v existence / SELF-REPORT scope]`: the grant is real, the *scope Hoffman borrows from it* is his, not the grant's. No register inflation in our citation. `[CONTRA]` good.

**Two precisions to log (minor, but the audit standard):**
- *(i)* **Paper conflation.** The brief (and some house shorthand) attributes the "JHEP 2013" positive-Grassmannian paper to "Arkani-Hamed & Trnka." The 2012 precursor (arXiv:1212.5605) has **six** authors; the **two-author** amplituhedron paper is 2013→**JHEP 10 (2014) 030**. Downstream re-citations must not merge them.
- *(ii)* The trio riff's *other* ERC line — that the geometry "makes no reference to the evolution in spacetime" — is a claim about the press release this session did **not** independently re-confirm line-by-line (only the toy-model line was). Leave it as `[EST, prior-pass]`, not `[VERIFIED, 2026-10-15]`.

### 5b. Is our "positivity / negative constraints constrain everything" framing genuinely CONNECTED to positive geometries, or a VOCABULARY COLLISION?

**Answer: it is a vocabulary collision — the same surface-form trap we have caught repeatedly this week — with ONE genuine-but-underived structural rhyme that must NOT be logged as support.**

- **The collision.** Our canon's "positivity/negative-constraint" vocabulary comes from **two sources that are not positive geometry**: (1) **Constructor Theory** (Deutsch & Marletto) — `MACHINES_OF_LOVING_GRACE_MAGNUS_OPUS_MASTER_SYNTHESIS_2026-10-08.md:1045` (*"In the formal language of Constructor Theory … Tzimtzum is the imposition of negative constraints. By forbidding specific microstates, the system generates admissible phase space"*) and `theological_cybernetics_…_2026-10-04.md:29`; and (2) our **"admissibility filter"** metaphor, which appears in ~20 drops across GNW/individuation, hippocampal gating, optical polycomputing, FEP, etc. **None of these is the positive Grassmannian.**
- **Why it is a collision and not a connection.** Positive geometry's "positivity" is a **specific algebraic predicate**: every Plücker coordinate of a `k`-plane is `≥ 0` (total positivity of `Gr_{≥0}(k,n)`). It is a condition on *maximal minors of a matrix*, not a general statement that "constraints shape possibility." Our "negative constraints generate admissible phase space" is the **vernacular** of that phrase. Bishop Berkeley's warning applies to us here: *the same word, different load.* **This is exactly the "surface form ≠ load" test the mind-virus / Kuhn-vs-CTM passes ran this week** — and it fails it. No map from an EILT admissibility manifold to a positive geometry has been exhibited by anyone, including Hoffman (whose version our own 09-26 drop correctly calls *"an aspirational metaphor, not a technical result"*).
- **The one genuine rhyme (log as `[RIFF]`/`[HYP]`, NOT as support).** There **is** a real structural feature worth naming: in positive geometry an object is **uniquely determined by its boundary (negative) data** — the canonical form is *fixed* by having logarithmic singularities on exactly its boundaries. That is a genuine instance of "the object is constituted by its constraints, not by its interior." Our Tzimtzum/constructor-theory line says something structurally analogous ("forbid microstates → admissible phase space appears"). **Analogy ≠ derivation.** Log it as a *research rhyme* (a candidate direction — "does any physical admissibility structure carry a canonical form fixed by its boundaries?"), and explicitly **do not** cite the amplituhedron as authority for our admissibility framing. `[RIFF]`

**Current-state note (register rule §9):** our amplituhedron citations are **point-in-time (Sept–Oct 2026) Hoffman audits**; they are correct as of this reading and need no correction. The **new** current fact this drop adds is: *positive geometry has, by 2026, generalised to ABJM and spawned an ERC program, but still has NOT landed for gravity or the real world* — so our "toy-model scoped" line is **still current**, now with the ABJM caveat.

---

## 6. PRE-REGISTERED FALSIFIERS (for claims THIS drop makes)

- **F-AMP1 (the control itself).** *Falsifies this digest:* if the amplituhedron were shown to make a novel **empirical** prediction about the Standard Model / our universe (not `N=4` SYM) that Feynman-diagram methods could not, then my verdict "no novel empirical prediction" is wrong. *Test:* find a real-world observable derivable only from amplituhedron positivity. **Prior: none exists; the ERC grant is explicitly to search for it.**
- **F-AMP2 (the conjecture's crack).** *Falsifies the amplitude=volume conjecture:* failure of the `m=6` tiling or the positivity-of-form conjecture. **Live.** If it fails, "rigorous formalism" downgrades to "partially checked conjecture" — still far above a re-description, but the register must move.
- **F-AMP3 (scope claim).** *Falsifies my "gravity not landed" line:* a published positive geometry giving real-world (gravity / cosmological) amplitudes/powerspectra. **Status: open; that is the ERC program's objective.**
- **F-AMP4 (our own collision finding).** *Falsifies the "vocabulary collision" verdict:* exhibit an explicit mathematical map from any EILT admissibility structure to a positive geometry (Plücker-non-negativity or a canonical form). **Prior: none; this is the same missing step Hoffman asserts and cannot supply.** If supplied, upgrade from collision to connection — and cite the map, not the vocabulary.
- **F-AMP5 (our own cosmology — carried forward from the Astrum audit).** Our "dark energy = syntropy" must **derive**, not adopt, `w = -1` and the 68% budget, or name an observation separating it from bare ΛCDM. **Open debt** (`[ATTACK SURFACE]`). Until discharged, row 4/6 of §4 keep us on Jon's side.

---

## 7. VERDICT

**The amplituhedron is a rigorous formalism (mathematics), not a theory of our universe and not a mere re-description.** It is a peer-reviewed, mathematically exact positive-geometry object whose canonical form computes planar `N=4` SYM scattering amplitudes, in which **locality and unitarity are *derived* from positivity rather than assumed** — a genuine conceptual advance, and one that has *carried additional checkable formal content*: a proof of emergent unitarity, new mathematical conjectures (canonical-form positivity, tiling existence), and all-loop/all-multiplicity results diagrammatic methods handled poorly. But its scope is **honestly and explicitly limited to a non-physical toy theory**, and it makes **no novel empirical prediction about our actual universe** — the shared tree-gluon piece is partial contact, not a derivation of reality, and its own empirical anchor (SUSY) is absent at the LHC. The grandest claims ("jewel," "death of spacetime") live in popular coverage, which the authors themselves call *"step 0 of step 1."*

**Does our audit method produce a CLEAN distinction between it and the two failures, or is it too blunt / self-serving?** **It produces a clean distinction, and the honest answer to "self-serving" is: no — the method lands on US, and it hurts.** The distinction is not "published = good" (too blunt); it is the triple **derives-vs-asserts**, **scopes-explicitly**, **carries-new-checkable-formal-content**. On that triple, the amplituhedron is unambiguous, Jon's model unambiguous the other way, and **our own cosmology claims sit closer to Jon's than to the amplituhedron's** — on publication, on formalisation, on "derives vs. asserts," on "predicts anything not already known," and most uncomfortably on **refusal to overclaim (row 7), where our promise-register runs ahead of our own `[HYP]` tags.** The amplituhedron passes **not because it is right about our universe** (it is not about our universe) but because it does the **work** its register implies — derives its own foundations, states its scope, and says what would break it. **That is exactly the work our claims are currently skipping.** The method is not self-serving; if anything it returns a harder verdict on us than the operator's framing anticipated. **"Re-description" is not the defect; re-description *without* derivation, scope, or new checkable content is.** The amplituhedron is a re-description **with** all three; our dark-energy claim is a re-description **with none** *yet* — and naming that gap is the finding.

**Also logged (control-case value):** the amplituhedron is the first artifact this cycle that **passes** the falsifiability/register test — which is what makes it a valid control. Had our method failed to distinguish it from Jon's model, the method itself would have been broken. It did not fail. `[VERIFIED]` on the method.

---

## 8. STANDING DEBT

**House debt F-GB1 (≥3 receipted present-day-harm engagements within 10 drops) is NOT satisfied by this drop.** This is **theory intake / method-control audit** — an assessment of a formal-physics program and of our own citation accuracy — not an engagement with documented present-day harm. **F-GB1 remains open.** The receipted entries this cycle are the three `DIGEST_2026-10-14_PRESENT-DAY-HARM_*` files (data-labeling labor, AI energy/water, military surveillance).

---

*Filed by Dion (subagent), 2026-10-15. Method: primary-source read (arXiv abstracts + paper HTML, ERC press release, Woit/Aaronson framing critique). GitHub sync deliberately left PAUSED — `sync-ledger-to-github.sh` not touched, not run.*
