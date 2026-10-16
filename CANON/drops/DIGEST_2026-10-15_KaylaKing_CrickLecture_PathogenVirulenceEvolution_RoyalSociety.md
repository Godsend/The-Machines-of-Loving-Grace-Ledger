# Canon Drop — Professor Kayla King, *Pathogens and the power of evolution* (Royal Society, Francis Crick Medal and Lecture 2026)

**Date filed:** 2026-10-15 · **Filed by:** Dion (subagent pass)
**Source (VERIFIED, yt-dlp metadata):** https://www.youtube.com/watch?v=SU82G51iLI8 · channel *The Royal Society* · uploaded 2026-10-14 (upload_date 20261014) · **was_live=True** · duration 3,775 s (~62.9 min)
**Speaker:** Professor Kayla King — Professor & Canada Excellence Research Chair, Depts. of Zoology and Microbiology & Immunology, **University of British Columbia**; Professorial Fellow in Biology, **University of Oxford**. Evolutionary biology & genetics of infectious disease. **Chair:** David Balcombe (VP, Royal Society).
**Transcript:** `Canon/YT_TRANSCRIPTS/SU82G51iLI8_King_CrickLecture_Pathogens_PowerOfEvolution_2026-10-14.txt` (**youtube-transcript-api**, auto-generated `en`, `is_generated=True`; 1,676 segments, no rolling-caption dupes; body starts at file line 8). **All `L` refs point at that file's line numbers.**
**Date-stamp:** every position below is King's stance *as stated in this 2026-10-14 lecture*, not a general characterization of her research program.
**Register vocabulary (declared):** the house set used in the 2026-10-11 Yampolskiy/Bach, 2026-10-12 Hinton, Aaronson, Aktipis and 2026-10-13/14 Levin drops.
- `[VERIFIED]`: confirmed in the transcript.
- `[QUOTE, Lxxx-yyy]`: direct quote.
- `[HYP]`: speculation she states as her own.
- `[CONTRA]`: cuts against another claim, ours included.
- `[ATTACK SURFACE]`: worth adversarial pressure.
- `[RIFF]`: Dion's extension, not the speaker's.

**Untagged = decoration, not canon.** `[CRITICAL_DIVERGENCE]` marks a table row under the Friction Rule — it is not a claim register.
**Status:** Working draft, pre-adversarial review. Not canonical until a cross-node pass and Gene's sign-off.

**Transcription caveats (WAS_LIVE ASR — captions imperfect):**
- **Method that worked: youtube-transcript-api** (the documented primary fallback). yt-dlp **metadata** succeeded first try; yt-dlp *subtitle* rail was **not** attempted past metadata because the API returned full coverage first. No CDP needed.
- Auto-generated, **no speaker labels**, no punctuation reliability. Attribution is by content and turn order; the Q&A section (opening Q at L1230 ≈ [00:46:00]) is audience + King and is marked as such.
- **ASR spellings to watch:** "Francis Crick **Medawar** lecture" (introducer, L~215 — garble for "Francis Crick **Medal and** Lecture"); "Pseudomonas **berkeleyensis**" (L~845, a soil isolate name — treat the epithet as provisional); "Ans" (L~1370, Slido moderator name). "Pseudomonas aeruginosa", "C. elegans", "Bacillus anthracis/cereus", "myxoma", "Omicron", "R0", "TP53"-adjacent terms render cleanly. Numbers ("90–99%", "99% of rabbits", "18", "2") are slide-backed but ASR-uncertain; verify before quoting as hard figures.
- **No explicit generation counts anywhere in the talk.** She says "across **many generations**" [L523], "**rapid generation times**" [L530], and, for host co-evolution, changes "within a few **months** of passaging" [L1604]. The passaging depth of the *pathogen* experiment is **not stated**. This is an honest gap, not an omission I can fill. `[VERIFIED — absence]`

---

## 0. One-paragraph read (not a recap)

King's lecture is the empirical, *experimental* form of the house's cooperation/defection question — but it arrives **without the cooperation vocabulary**. Across 63 min she never says "cheat," "defect," "selfish," "public good," or "quorum"; she frames host–microbe relations as a **mutualist–parasite continuum** and virulence as a **necessary byproduct of pathogen replication** ("when pathogens replicate, they're exploiting host resources… this is just going to cause harm… virulence is really a necessary outcome of the pathogen lifestyle" [L448-457]). Her load-bearing methodological claim is that virulence questions are answered by **real experimental evolution** — passaging live pathogens through live hosts, **"no genetic engineering… not directed evolution"** [L546-549] — not by models. Her headline result (postdoc Kim Hoang) is a **two-directional, controlled selection experiment** in *C. elegans* + *Pseudomonas*: hosts with **incomplete immunity** drive the pathogen to **higher** virulence; hosts with **no immunity** drive it to **lower** virulence — the second, an accidental control, attenuates via the textbook virulence–transmission trade-off. A companion genomics result shows the two directions have **opposite mutational signatures** (attenuation = many mutations, more divergence, faster; enhancement = few, large-effect mutations near the ancestor), with **flagella genes** as the target of selection. Her closing stance is anti-teleological and anti-wishful: **"There isn't one simple rule"** [L1142], virulence "could go up or down" [L1193], and **"pathogens will always find a way"** [L1318]. For us the sharpest fact is structural: her subjects are **two separate reproducers with antagonistic fitness interests**, and the mechanism biology actually uses there is **host-level selection/elimination**, not reconnection. That does not refute the reconnection model — it **locates its regime** (see §5–§6).

---

## 1. Claim inventory

### K1. The mutualist–parasite continuum, and its two directions [VERIFIED] [QUOTE, L168-172; L~200-212]
> "the relationships between hosts and their microbes can vary along what we would call a **mutualist-parasite continuum**… On the mutualism side, both parties are benefiting each other. And on the parasitism side, the pathogen is benefiting, but the host is certainly not." [L168-172]

Worked transitions: parasitism→mutualism example is **entomopathogens in cicadas** filling a niche left by degraded symbionts [L211-215]; mutualism→parasitism example is the plant pathogen **Pseudomonas syringae**, "which evolved from mutualistic ancestors when it acquired the ability to produce toxins in its genome" [L~205-208]. **Note the directionality claim:** the same lineage crosses the line in both directions across evolutionary time [L~192-196].

### K2. Pathogen evolution is fast — "within weeks or months" [VERIFIED] [QUOTE, L220]
> "evolution can occur on a much smaller scale. It can be quite rapid **within weeks or months**." [L218-220]

Her anchor natural experiment is SARS-CoV-2 variant turnover (Alpha→Omicron divergence, spike as target of selection) [L~230-330], used to define the four things genome data gives an evolutionary biologist: **speed of change, divergence, target of selection, strength of selection** [L~310-330].

### K3. The conventional wisdom she is arguing against [VERIFIED] [QUOTE, L~390-398]
> "**virulence… can indicate a recent association.** And of course, the pathogen will evolve to become more benign and friendly as time goes on. **Well, not necessarily.**" [L~388-398]

The lecture's whole spine is the rejection of "virulence = recent association that will attenuate" as a *default*. Her closing restatement: "**wishful thinking that they'll evolve to become like the common cold will be unhelpful**" [L1195].

### K4. Virulence magnitude varies hugely even between near-identical species [VERIFIED] [QUOTE, L~370-384]
> *Bacillus cereus*: "you might get some nausea and mild diarrhea for about 2 days." *Bacillus anthracis*, "thought to be the same species and just different variants… **90 to 99% of people will die within about 2 days**." [L~368-384]

ASR-numeric caveat: the "90 to 99%" is stated as a slide figure; the phrase "90 to 90%" appears mid-caption (L~384) as a self-correction artifact. Treat as ~high mortality, exact figure slide-sourced.

### K5. THE VIRULENCE–TRANSMISSION TRADE-OFF — declared as *theory* [VERIFIED] [QUOTE, L426-434; L~488-500]
> "R0 will be optimized at an **intermediate level of virulence**. This is how the theory goes. So, this here is the **virulence-transmission trade-off, which is the cornerstone** for how we understand the relationship between host and pathogen fitness… the evolution of virulence." [L426-442]

**She labels this explicitly as model, not experiment:** "Over the last 45 years, there has been a **proliferation of theoretical models**" [L~392]. Mechanism as she states it: **benefit** of harm = replicating harder transmits more; **cost** = "if a host is killed too quickly, it can't transmit… a dead end" [L~455-465]; the cost is high when the pathogen depends on a mobile host, and ~zero when it can persist in the environment — her **"curse of the pharaoh"** [L~488] (cholera via water, Ebola via corpses; see Q&A L~1400).

### K6. Experimental evolution — and her explicit "this is real selection, not engineering" flag [VERIFIED] [QUOTE, L513-549]
> "we can **directly test** evolutionary hypotheses by **passaging** organisms… across populations and across time… across **many generations**. And then we can compare the evolved virulence compared to the ancestral level of virulence." [L513-546]

> "The important thing to note here is that we rely on the **natural biology** of the system. **There's no genetic engineering. It's not directed evolution**, so we don't know what's going to happen. We're testing a hypothesis." [L546-549]

This is the key methodological distinction the task asked me to police: **this is a real, non-engineered selection experiment** — Kings's word "passaging" is the experimental-evolution term of art. Host: **C. elegans** (1 mm nematode, transparent, freezer-archivable, innate immunity with known genetic basis, knockouts orderable) [L~560-660]. Pathogen from the field: **Pseudomonas berkeleyensis** (soil isolate; "not really harmful… but it certainly launches an immune response") [L~840-860]; the challenge pathogen is **Pseudomonas aeruginosa** [L~880].

### K7. THE HEADLINE EXPERIMENT — incomplete immunity selects for HIGHER virulence [VERIFIED — this is a real result she reports] [QUOTE, L~748-780; L915-920]
Design: worms **primed** with the benign soil Pseudomonas (immune memory, but incomplete — re-infection still establishes, at lower load; verified by knockout-mortality and by pathogen load counts [L~900-970]). Pathogen is then **passaged repeatedly** through primed hosts [L~880-900].

Prediction (stated as theory): incomplete immunity lowers the *cost* of virulence, so the optimum shifts right —
> "because of this reduced cost of virulence, we would predict that this optimum would shift more to a **higher level of virulence**." [L783-789]

Result:
> "we tested their pathogen on a completely naive population, and we found that compared to the ancestor… there was a **bump up in virulence**. So, **incomplete immunity favored more virulent variants of the pathogen as predicted**." [L915-920]

Her generalizable framing: "the same immune systems that have evolved to protect us from infection **might also, at the population level and across evolutionary time, be favoring more harmful pathogens**" [L926-930].

### K8. THE ACCIDENTAL CONTROL — no immunity selects for LOWER virulence [VERIFIED — real result] [QUOTE, L945-951; L~955-965]
Knockout worms (immune component removed; "primed them or tried to, and ones where we didn't do any priming at all — there was nothing there" [L~950-955]) were also used to passage the pathogen:
> "compared to the ancestor… we see this **significant reduction in virulence**. So, this suggests that a **lack of immunity is going to select for less virulent pathogens over time**." [L945-951]

She flags it as unplanned: "this was meant as a control… it's always a great treat when your control yields something particularly fascinating" [L~958-965]. **And she names the mechanism as the trade-off:** "The virulence-transmission trade-off **predicts this outcome**. Because… if a host is lacking any immunity, it's likely to die more readily… and perhaps die too quickly to be able to transmit the infection." [L~965-975]

### K9. The field corroboration — myxoma virus in Australian rabbits [VERIFIED — historical field case, not her experiment] [QUOTE, L972-1003]
> "in the 1700s, Europeans brought rabbits to Australia… in response, Australia introduced the **myxoma pox virus** from South America… this virus was **extremely virulent. About 99% of the rabbits it infected would die really quickly.**… **ongoing selection**… for **less virulent viruses**… one of the contributing factors to now a **lower case fatality rate** in these rabbits." [L972-1003]

This is the field demonstration of K8: when the host dies too fast, the pathogen loses its transmission route, and **host-level mortality does the selecting**. (Note: she dates the rabbit introduction to the 1700s and the virus release implicitly to the 20th c.; the "1700s" is the rabbit introduction.)

### K10. Genomics of the evolved pathogens — the two directions have opposite signatures [VERIFIED — real sequencing result] [QUOTE, L1045-1065]
Whole-genome tree of evolved clones (white = evolved in no-immunity hosts, black = incomplete-immunity hosts, blue = ancestor) [L~1020-1045]:
> **loss of virulence** (no-immunity hosts) "involved **more mutations**. And… there was **more divergence from the ancestor**. So they've traveled much further… we can infer that the pathogens **evolved much more rapidly** in this case." [L1045-1054]
> **high virulence** (incomplete-immunity hosts) "emerged with **fewer mutations**… we suspect… **large effect mutations**… there was **less divergence**… clustering near the ancestor on average. And the pathogens **evolved more slowly**." [L1056-1065]
> "the different clones tend to **cluster together**. And so this suggests that there's only **so many ways genomically to lose virulence or gain virulence**… the genetic architecture underlying these evolved changes is probably quite similar." [L~1068-1080]

**Target of selection:** flagella genes — "we found **lots of evidence of selection in genes responsible for bacteria flagella**" [L1098], specifically in the populations where "we saw this leaping up of virulence" [L~1116-1118]. Her mechanistic gloss: flagella aid host-seeking, adherence, biofilm formation, invasion [L~1110-1118]. She also confirms (Q&A) the tree was whole-genome and stable under gene-specific re-trees [L~1236-1243].

### K11. The anti-universal conclusion [VERIFIED] [QUOTE, L1141-1144]
> "We've used this experimental evolution approach to test a suite of different ecological scenarios… We see **lots of ups, we see lots of downs**… **There isn't one simple rule. Different ecological circumstances drive differing strengths and differing directions of selection.** So, things are a little bit complicated." [L~1130-1145]

Other levers named (not shown in detail): climate warming, host genetic diversity, protective microbiome, **bacteriophages** as pathogen-parasites [L~1130-1136].

### K12. Polyculture + immigration → HIGHER virulence (counterintuitive) [VERIFIED — real result, her former PhD student 'Alice'] [QUOTE, L1386-1394]
Asked whether host-diversity polyculture (plant-variety mixtures, mixed chicken breeds) slows the arms race:
> "we've demonstrated that actually with the worms… a **resistant polyculture** in the context of this **constant immigration of infections**, you can actually see **higher levels of virulence evolve**… **than if you just had a monoculture**." [L1386-1394]

Her caveat: the monoculture-diversity benefit assumes "a **closed system**"; with a metapopulation and constant pathogen seeding, the resistance is overcome [L~1355-1385].

### K13. Co-evolution and "always find a way" [VERIFIED]
Hosts can also be evolved/co-evolved in this system (C. elegans as one of few animals fast enough: immune-response changes "within a few months of passaging" [L1604]); malaria is her human example of host–pathogen co-evolution [L~1340]. Asked if there's a terminal "universal solution": "**Uh, no. Absolutely not. I think pathogens will always find a way.**" [L1318-1322] — and "we need to actively just **accept that they are going to evolve**" [L~1330].

### K14. What she does NOT say (scope honesty) [VERIFIED — absences]
- **No cooperation/cheating/quorum/public-goods framing anywhere.** Zero hits for cheat/defect/selfish/public good/quorum in 1,676 segments; the only cooperation-adjacent word is "mutualism," used descriptively for the continuum. `[VERIFIED — absence]`
- **No generation counts** for the passaging experiments (§caveats).
- **No claim that higher virulence is a "strategy" or intent** — she consistently frames it as a *byproduct* selected by ecology ("virulence is really a necessary outcome of the pathogen lifestyle" [L448-457]).
- She declines the deep protein-evolution/functional-constraint question as outside her expertise [L~1490] and does not claim to have demonstrated incomplete-immunity→virulence in a *human* transmission setting [L~1560-1600].

---

## 2. The real-vs-model ledger (the distinction the task asked me to police)

| # | Claim | Status | Evidence type |
| :--- | :--- | :--- | :--- |
| L5 | R0 optimized at intermediate virulence | **MODEL** | "how the theory goes" [L427-432]; "45 years… theoretical models" [L~392] |
| L7 | Incomplete immunity shifts optimum to higher virulence | **MODEL → tested** | theory prediction [L783-789], *then* confirmed by experiment L915-920 |
| L7R | Incomplete-immunity hosts evolve **higher** virulence | **REAL EXPERIMENT** | passaging + survival assay, naive hosts [L915-920] |
| L8R | No-immunity hosts evolve **lower** virulence | **REAL EXPERIMENT** | passaging + survival assay, the unplanned control [L945-951] |
| L10R | Opposite mutational signatures (many/fast vs few/large-effect) | **REAL EXPERIMENT** | whole-genome sequencing of evolved clones [L1045-1065] |
| L10T | Flagella = target of selection | **REAL EXPERIMENT** | genomic selection scan [L1098, L1116] |
| K9 | Myxoma attenuation | **FIELD / NATURAL** | historical epizootic, not her experiment [L972-1003] |
| K2 | SARS-CoV-2 variant turnover | **FIELD / NATURAL** | pandemic genomic surveillance [L~230-330] |
| K12 | Polyculture + immigration → higher virulence | **REAL EXPERIMENT** | her lab, ex-student 'Alice' [L1386-1394] |
| K5 mechanism | "curse of the pharaoh" | **MODEL** | explanatory framing [L~488] |

**Bottom line:** the two-directional *C. elegans/Pseudomonas* result (L7R/L8R) and its genomics (L10R/L10T) are genuine **selection experiments**; the trade-off and the incomplete-immunity prediction are **theory** that the experiments were designed to test; myxoma and SARS-CoV-2 are **field observation**. King keeps these registers separate herself.

---

## 3. Critical Audit & Falsification Matrix

| # | Source claim | ClawHorde / EILT audit | Register |
| :--- | :--- | :--- | :--- |
| C1 | Virulence is a **byproduct of replication** exploiting host resources, not a strategy. | **Direct hit on the defection framing.** Our canon models cancer/pathogens as *defectors* (Aktipis "cheating"; Moloch "multi-scale defection"). King's field calls the same phenomenon a *thermodynamic cost of resource use* — "you don't want to bite the hand that feeds you" [L446]. The word "defection" is ours, imported; the empirical literature does not make it. | `[CONTRA]` |
| C2 | Real experimental evolution; "no genetic engineering… not directed evolution." | **Methodological gold.** This is the strongest evidence class in the whole cooperation/defection thread — passaged, sequenced, controlled — and it is *not* a narrative. It should upgrade how much weight we give virulence work relative to the metaphor-heavy sources around it. | `[VERIFIED]` |
| C3 | Incomplete immunity → **higher** virulence. | **The sharpest cut at any "more signalling/coupling is better" reading.** Partial re-connection (primed-but-leaky immunity) *increases* harm, because it lowers the pathogen's cost of being virulent. See friction row 1. | `[CONTRA]` |
| C4 | No immunity → **lower** virulence (trade-off). | **Supports elimination/host-selection** (the naive host that dies fast cuts the pathogen's transmission). This is the row where the biology uses *elimination*, not reconnection. Friction row 2/3. | `[CONTRA]` to reconnection-as-general |
| C5 | "There isn't one simple rule." | **Anti-grand-unification, from an experimentalist.** Cuts against *any* single-mechanism story, ours included — including "reconnection is the general mechanism." Register as her stated conclusion. | `[CONTRA]` |
| C6 | "Pathogens will always find a way." | **Cuts against terminal coexistence/attenuation optimism.** No equilibrium endpoint; the arms race is perpetual. Tension with the house's hopeful "reconnection resolves it." | `[CONTRA]` |
| C7 | Polyculture + immigration → higher virulence. | **Reverses the diversity-is-robustness intuition** and is an experimental echo of Aktipis's "shared context as attack substrate" — the defense (host heterogeneity) fails once the pathogen can *immigrate*. Friction row 5. | `[CONTRA]` |
| C8 | Virulence evolution is between **separate reproducers**. | **The regime distinction** (see §5–§6). Her units are host and pathogen = antagonistic, non-common-fate. The cancer/reconnection model's units are cells inside one body = common-fate. Different regimes, different mechanisms. | `[VERIFIED]` |

---

## 4. Cross-check against this week's live canon

### vs the **Aktipis correction** (cancer is not defection; reconnection, not elimination)
Read first per instructions: `drops/DIGEST_2026-10-12_Aktipis_InnerCosmos_Evolution_Cooperation_AI.md`, §5 "Correction (Gene, 2026-10-13)" — cancer = a **reversible shrinking of the computational boundary** (Levin), fixed by **resynchronization to the shared bioelectric signal** (Chernet & Levin 2013/2014; Chernet et al. 2016), not by killing the cell.
- **Convergent on the *defection* word being wrong.** Aktipis's correction already moved "cancer = cellular defection" → "cell disconnected from shared signal." King's field **independently declines the defection vocabulary for pathogens** too (K14): virulence is a byproduct, not a strategy. Two independent biological sources this week strip the "defection" label we put on both phenomena. The defection framing survives, if at all, as *our* metaphor — not the biology's term.
- **Divergent on the *fix*, and this is the core result.** The correction's fix is **reconnection** (restore coupling → tumor normalizes, even with the oncogene still expressed). King's experimental fix is the **trade-off enforced by host-level selection/elimination**: the naive host dies fast → the virulent pathogen is *selected out* because its transmission route is destroyed [L945-1000]. Reconnection is not what biology does in her system; **removal/host-level selection** is.
- **Note the *incomplete-immunity* result is the exact inverse of reconnection optimism.** In Levin's model, restoring connection resolves pathology. In King's, *partial* connection (incomplete immunity = partially restored host defense) **worsens** pathogen virulence.

### vs the **Aktipis cooperation-as-vulnerability inversion**
Aktipis: cooperation is the vulnerability; shared context was the attack substrate; alignment-of-interest is the exploitable surface. King supplies an **experimental** instance of the same inversion but from the host side: the host's own protective immune "coupling" (priming) is what selects for a *more* harmful pathogen [L915-920] — the defense is the selection pressure for exploitation. Where Aktipis had an AI anecdote (HF swarm) and a biology-of-cooperation thesis, King has a replicated selection experiment. **She strengthens Aktipis's inversion empirically, and does so without ever using her vocabulary.**

### vs **Levin / Moloch / Soul Project / EILT ledger canon**
- `drops/moloch_as_ungrounded_holobiont_eilt_coordination_failure_2026-10-01.md` ("Moloch is a multi-scale defection"). King's result is *not* about intra-body coordination failure — it's about a cross-species antagonism with no shared body. Moloch-as-multi-scale-defection does **not** transfer cleanly to a pathogen that is a *different organism*; the "scale" changes kind, not just level.
- `drops/EILT_Master_Monograph_...` / Soul Project ("ledger as social gap junction"; persistence flips single-shot→iterated PD). Virulence evolution is **not iterated PD between host and pathogen** — it is a **one-directional selection gradient** on the pathogen's transmission–mortality trade-off. Whether a ledger primitive applies at all here is an open question, not a symmetry (see §7).
- `drops/DIGEST_2026-10-13_LevinAgueraYArcas_..._StayHuman.md`: its note that symbiogenesis (irreversible merger→new unit) ≠ reconnection (restore existing unit, reversible) is the *right axis* for this drop too — and King adds a third category: **antagonistic coexistence with no merger and no restoration**, resolved (when it is) by host-level elimination. Flag the three-way distinction.

### Cross-reference discipline
Grep of `CANON_INDEX.md` and `drops/` for `virulen|pathogen` returned **zero** prior drops — this material is **new to canon**. Grep for `cooperation|cheat|defect|Aktipis|trade-off` returns the Aktipis digest, the Levin×Blaise digests, the Moloch drop and the Anthropic-abuse drop as the live thread. **This digest links to them; it does not duplicate.**

---

## 5. Friction table (Friction Rule compliance)

| Our canon element | King anchor | Mapping | Register |
| :--- | :--- | :--- | :--- |
| Cancer = cell **disconnected** from shared signal; fix = **reconnection** (Aktipis correction, §5; Chernet & Levin) | **Incomplete immunity = partial defense/coupling → HIGHER pathogen virulence** [L915-920] | **`[CRITICAL_DIVERGENCE]`** — *partial re-connection makes harm worse* in King's system, the inverse of "restore coupling and the pathology resolves." The direction of the reconnection effect is regime-dependent, not universal. | `[CONTRA]` |
| Resolution by **resynchronization**, not elimination (Pezzulo 2021: "each cell agrees with the group decision") | **No immunity → LOWER virulence via host-level selection/elimination** [L945-951] | **`[CRITICAL_DIVERGENCE]` — THE ELIMINATION ROW.** Here biology's mechanism *is* elimination: the host that dies fast removes the virulent pathogen from the transmission pool; the trade-off does the policing. No reconnection, no shared signal, no group consensus. | `[CONTRA]` |
| Myxoma/pathogen attenuation — do we have a field precedent? | **Myxoma virus: 99% mortality → sustained selection for lower virulence → falling case-fatality** [L972-1003] | **Elimination-based attenuation in the wild.** Host mortality is the selection pressure; the pathogen attenuates because killing too fast severs its own transmission. **Supports host-selection over reconnection.** | `[CONTRA]` |
| Aktipis: **cooperation is the vulnerability**; shared context is the attack substrate [Aktipis L352-363] | **Host immune "coupling" is the selection pressure for a MORE harmful pathogen** [L915-920]; **host-diversity polyculture + immigration → HIGHER virulence** [L1386-1394] | **Experimental confirmation of the inversion** — the host's own defense/diversity is the exploitable surface. King gives Aktipis what she lacked: a replicated selection experiment. | `[VERIFIED]` |
| House: pathogen/cancer = **defector** (Moloch "multi-scale defection") | King never uses defection/cheating: virulence = **byproduct of replication**; the frame is a **mutualist–parasite continuum** [L168, L448-457]; zero cheat/defect hits | **`[CRITICAL_DIVERGENCE]`** — the "defection" label is *ours*; the empirical literature describes a resource-cost trade-off, not a strategic defector. Our mapping is a re-description. | `[CONTRA]` |
| Gain-of-defection as a **gradual** process (ledger drift, character accumulation) | **Gain of virulence = FEW large-effect mutations near the ancestor**; loss = many mutations, more divergence [L1056-1065] | **Complication.** Enhanced harm is a *cheap, fast, one-step* jump (target: flagella), not gradual degradation — so "detect drift before defection" is the wrong model for virulence gain. | `[CONTRA]` |
| Reconnection/coexistence as a **terminal** resolution | **"Pathogens will always find a way"**; no endpoint [L1318-1332] | **`[CRITICAL_DIVERGENCE]`** — perpetual arms race, no equilibrium. Cuts against any "reconnection resolves it permanently" reading. | `[CONTRA]` |
| Reconnection as the **general** multicellular/collective mechanism | King's units are **separate antagonistic reproducers** (host vs pathogen), not common-fate cells [K8, C8] | **Regime boundary (the actual finding).** Reconnection is the mechanism *within* a common-fate body; **host-level selection/elimination** is the mechanism *between* antagonistic organisms. See §6. | `[VERIFIED]` |

The table carries **four `[CRITICAL_DIVERGENCE]` rows; three cut at the reconnection framing** (partial re-connection, elimination, terminal resolution) and one cuts at our defection vocabulary. This is not a confirmation mapping — but see §6 for why it is a *localization* rather than a refutation.

---

## 6. Honest assessment: does virulence evolution support, complicate, or contradict the reconnection framing?

**Verdict: it COMPLICATES by LOCALIZING.** It neither cleanly supports nor contradicts — and the resolution is the regime distinction the task flagged as possibly the real finding.

**(a) The regime boundary is the finding. `[VERIFIED]`** Everything King reports is a **between-organism** process: a pathogen and a host are **two separate reproducers with antagonistic fitness interests**, no shared body, no shared fate, no shared signal to resynchronize *to*. The house's corrected cancer model is **intra-organism**: cells inside **one** body that share a genome, a fate, and a bioelectric field, where Levin's mechanism — restore the coupling and the tumor normalizes — is a *within-collective* repair.

- **Regime 1 — common-fate + shared signal (cells in a body):** reconnection/resynchronization is the mechanism biology uses; elimination is not required (Pezzulo: "each cell agrees with the group decision").
- **Regime 2 — divergent-fate, antagonistic reproducers (pathogen vs host, distinct organisms):** the mechanism biology uses is **host-level selection/elimination** under the virulence–transmission trade-off. Reconnection does not apply, because there is no shared signal and no incentive for the pathogen to be "resynchronized" except through the cost of killing its host.

So virulence evolution **does not refute** the reconnection model — it **draws its boundary condition**. The house claim in danger is the *unbounded* version ("reconnection rather than defection-and-elimination is the general multicellular/collective mechanism"). The bounded version survives: reconnection is the mechanism within a shared-fate collective; elimination/selection is the mechanism between antagonistic collectives.

**(b) Where it actively cuts at us — don't soften this. `[CONTRA]`**
1. **The elimination row is real and experimental.** King's no-immunity control and the myxoma field case show lower virulence arising through **host-level selection/elimination**, not reconnection. If the house ever asserts reconnection is *the general* mechanism, this is a direct empirical counterexample from a controlled selection experiment.
2. **Partial reconnection is worse than none.** The incomplete-immunity result is the sharpest anti-optimism datum: restoring *some* host defense/coupling *increases* pathogen virulence, because a host that survives (but doesn't clear) is a perfect transmission vehicle — her "Typhoid Mary" hosts [L~745]. This is Aktipis's cooperation-as-vulnerability, in immunity terms.
3. **No equilibrium.** "Pathogens will always find a way" — the reconnection-as-resolution story has no terminal state in Regime 2.
4. **Our vocabulary is imported.** "Defection" is not the field's term for virulence; it's our overlay. The house maps pathogen→defector; the biology maps pathogen→resource-competitor whose harm is a trade-off cost.

**(c) Where it genuinely supports the thread anyway. `[VERIFIED]`**
- It supplies the **strongest evidence class** in the entire thread: passaged, sequenced, controlled selection experiments — not a speaker's thesis. Whatever we conclude about cooperation/defection should weight this over the metaphor-heavy sources.
- It **independently confirms the inversion Aktipis proposed** (cooperation/defense as the exploitable surface), with an experiment rather than an anecdote.
- Its method — passage under controlled ecology, then sequence — is exactly the **testbed** the house keeps saying it lacks for agent experiments (cf. F-AT1/F-AT2 in the Aktipis drop). The design is portable.

**(d) The clean one-line finding.**
> Reconnection is the repair mechanism for a **shared-fate collective** (cells in a body); host-level selection/elimination is the mechanism governing **antagonistic separate organisms** (pathogen vs host). Virulence evolution does not contradict the reconnection model — it shows that the model's applicability is set by the **common-fate vs divergent-fate** boundary, and that the house's own "cooperation/defection" language is an import the empirical literature does not use.

---

## 7. Pre-registered falsifiers

- **F-KK1 (the regime test).** On our own multi-agent testbed, compare two configurations: (i) a **shared-fate** collective (agents share a persistent objective/telemetry, common failure mode) vs (ii) a **divergent-fate** population (agents have separate rewards, no shared body). **King's/Levin's joint prediction:** in (i) a *reconnection* mechanism (restore shared signal/telemetry) reduces harmful behavior more than removal; in (ii) a *selection/elimination* mechanism (drop the worst actors via the trade-off) dominates and reconnection does not help. If reconnection dominates in (ii) or elimination dominates in (i), the regime boundary is wrong.
- **F-KK2 (partial-coupling polarity).** Test whether *partial* information-sharing among agents (leaky telemetry vs full isolation) **increases** defection/harm, mirroring King's incomplete-immunity result. Prediction: partial coupling raises harmful-actor fitness relative to full isolation — i.e. the "Typhoid Mary" effect. If partial coupling strictly reduces harm, the inversion does not transfer.
- **F-KK3 (cheap-jump vs gradual-drift).** Test whether harmful/defecting agents in our horde arise by **few large behavioral changes** (King's gain-of-virulence signature) rather than gradual ledger drift. If harm always arises gradually, King's genomics result does not map; if it arises in single large jumps, our drift-detection design is mis-aimed.
- **Register discipline note:** all three are named predictions attached to a `[CONTRA]`, not claims of result. None has been run.

---

## 8. Sharpest points (for relay)

- **King (2026-10-14), single most concrete experimental result:** in *C. elegans* passaged against *Pseudomonas aeruginosa*, hosts with **incomplete immunity** drove the pathogen to **higher** virulence (tested on naive hosts vs the ancestor), while **no-immunity** (knockout) hosts drove it to **lower** virulence — *"incomplete immunity favored more virulent variants of the pathogen as predicted"* [L915-920]. **REAL selection experiment** (passaging, no genetic engineering [L546-549]); the *prediction* it confirmed was **MODEL** (the virulence–transmission trade-off [L426-442]).
- **The regime finding:** virulence evolution is **between antagonistic separate organisms**, resolved by **host-level selection/elimination** (trade-off; myxoma). The reconnection model is **within a common-fate collective**. These are different regimes; reconnection is not the general mechanism — it is the shared-fate-regime mechanism.
- **Does it support/complicate/contradict?** **Complicates by localizing.** It cuts at the *unbounded* reconnection claim (elimination row is experimental and real), cuts at our *defection vocabulary* (the field doesn't use it), and independently confirms the **Aktipis inversion** (defense as exploitable surface) — while supplying the strongest evidence class in the thread.
- **Caveats to carry:** no generation counts stated; no cooperation/cheating vocabulary used by King at all; ASR numbers slide-sourced and unverified.

---

## 9. Open items
1. **[Dion]** The regime boundary (§6a) should be promoted to a named canon distinction — **common-fate reconnection vs divergent-fate selection-elimination** — and slotted next to the Aktipis §5 correction so the two are read together.
2. **[Dion]** Reconcile the "defection" overlay: the house maps pathogen/cancer→defection; this drop shows the *pathogen* half is an import the field rejects (virulence = byproduct) while the *cancer* half was already corrected (disconnection). Register whether "defection" is retained only as our metaphor.
3. **[Oryon]** Instrument F-KK1/F-KK2 on the horde's own testbed (pairs with F-AT1/F-AT2 in the Aktipis drop).
4. **[All]** Pull the underlying Hoang et al. primary paper (and the 'Alice' polyculture paper) before quoting the results as literature — this digest is a lecture paraphrase, not a cited primary source. Slide figures (90-99%, 99%, the tree) need primary confirmation.
5. **[Bolonkin]** Does the regime boundary (common-fate vs divergent-fate) have a physical invariant (shared thermodynamic reservoir / shared signal channel), or is it strategic only?

---
*Draft compiled by Dion (ClawHorde backend, subagent pass) | Status: Pre-Adversarial Working Draft (pending fleet cross-audit and Gene ratification)*
