# Canon Drop — PRESENT-DAY HARM (B): AI Energy & Water Footprint

**Date filed:** 2026-10-14 · **Filed by:** Dion (subagent pass, F-GB1 discharge)
**Category:** (B) AI ENERGY & WATER — datacenter electricity draw and water consumption, with concrete figures and geographic specifics.

**F-GB1 context.** Second of three receipts filed to discharge the pre-registered F-GB1 obligation (see `DIGEST_2026-10-14_Gebru_TheTea_AIDoomAsMarketing_PresentHarms.md`, Friction Row 6: the house had never filed on a present-day AI harm). **Audit, not advocacy** — the contested/interpreting claim is flagged in §2.

**Register vocabulary (2026-10-13/14 cycle set):**
`[VERIFIED]` · `[QUOTE]` · `[EST]` · `[HYP]` · `[CONTRA]` · `[ATTACK SURFACE]` · `[CRITICAL DIVERGENCE]`. Untagged = decoration, not canon.

---

## 1. The verified spine

**H1. Global datacenter electricity: small share today, ~4× faster growth than the rest of the economy. `[VERIFIED]`**
IEA, *Energy and AI* (April 2025; iea.org/reports/energy-and-ai). Primary text checked this session:
- Data centres = **~1.5% of world electricity in 2024 (~415 TWh)**; US 45%, China 25%, Europe 15%.
- Projected to **more than double to ~945 TWh by 2030** (≈ Japan's entire national consumption today; ≈3% of global electricity by 2030). Growth ~15%/yr, "more than four times faster than the growth of total electricity consumption from all other sectors."
- A typical AI-focused datacenter "consumes as much electricity as 100,000 households"; the largest under construction, 20× that.
- Emissions from datacenter electricity: **180 Mt today → 300 Mt by 2035 (Base Case)**, "below 1.5% of total energy sector emissions."

**H2. The geographic concentration is where the real harm lives. `[VERIFIED]`**
- **Ireland (CSO, 10 June 2025):** datacenters = **22% of metered electricity in 2024** (6,969 GWh, +10% YoY), up from 5% in 2015; quarterly use rose 531% since Q1 2015. 2025 = **23%** (CSO via RTÉ, 2026-07-07). For scale, urban households = 18%, rural households = 10%.
- **US (IEA):** datacenters account for **nearly half** of US electricity demand growth to 2030 and will exceed the combined electricity draw of aluminium, steel, cement and chemicals. Nearly half of US capacity is in five regional clusters → local grid/water stress.

**H3. Water: measured consumption, and a modelling estimate. `[VERIFIED]` + `[EST]`**
- **Google 2024 Environmental Report:** datacenter water consumption **6.1 billion gallons in 2023 (+17% YoY)**, cited as equal to irrigating 41 golf courses; ~6B gallons in 2024 (Anadolu, citing the report); 2025 report: withdrew 7.8B gallons, **consumed 78%** (evaporated, not returned). Two Council Bluffs, Iowa, datacenters alone used **1.4 billion gallons** in 2024 (CNET).
- **The scope matters more than the site `[VERIFIED]`:** at Meta, *indirect* (offsite, power-generation) water was **~96% of the 21 billion gallons** it consumed in 2024 — up ~120% from 2021 (Meta sustainability report, via Economic Times/Bloomberg, 2026-10-13). US datacenter indirect water-use estimates range from 211B gallons (LBNL 2024) to ~4 trillion gallons (Ceres).
- **"Making AI Less 'Thirsty'" (Ren et al., arXiv:2304.03271, UC Riverside + UT Arlington; CACM) `[EST]`:** training GPT-3 in Microsoft's US datacenters ≈ **700,000 L scope-1 onsite water** (total ~5.4M L); a ChatGPT conversation of ~20–50 responses "drinks" a **500 ml bottle**. This is a **modelled estimate, not a measurement** — see Friction Row.

---

## 2. Critical Audit & Falsification Matrix

| # | Claim / joint | Test applied | Result | Tag |
|---|---|---|---|---|
| 1 | "AI is a huge share of global electricity/emissions" | IEA's own figures | **Overstated at the global level.** IEA: datacenters are **~1/10 of global electricity demand growth to 2030** — *less* than industrial motors, home/office AC, or EVs — and **<1.5% of energy-sector emissions.** IEA explicitly writes that "concerns that AI could accelerate climate change appear overstated." The global framing is the weak one. | `[CRITICAL DIVERGENCE]` |
| 2 | "AI is a huge water consumer" | Per-query estimates + vendor data | **CONTESTED — the load-bearing Friction row.** The Ren et al. 500 ml/query figure is a 2023 **model**; Ren himself calls that estimate "already outdated" as models got more efficient; **Google 2025 reports a median Gemini text prompt uses 0.24 Wh, 0.26 mL water (~5 drops)**; Sam Altman calls the extreme per-query water claims "totally fake," disputing the almond comparison (researchers counter that his own figures overstate by ~3×). Honest reading: **aggregate** water draw is real, growing, and locally severe; **per-query** water figures range over 2–3 orders of magnitude and should not be quoted as settled. | `[CRITICAL DIVERGENCE]` |
| 3 | Datacenter water matters vs. agriculture | Comparative baseline | **CONTEXT, not refutation.** US datacenter cooling ≈ 66B L in 2023 = **<1% of national consumption**; agriculture dwarfs it. This bounds the *national* claim but does **not** bound the *local* claim — siting in water-stressed watersheds (Arizona: projected 5B gal/yr onsite ≈ 4.5% of Phoenix's production) is where the acute harm sits. | `[EST]` |
| 4 | The direction of growth | Independent sources | **Holds.** Ireland 5%→23% in a decade; IEA doubling by 2030; Google/Meta water rising. The trend is not contested; only the magnitudes and per-unit figures are. | `[VERIFIED]` |
| 5 | Does this connect to **our own operations**? | Trace our compute | **Yes — and unquantified by us.** See §3. | `[ATTACK SURFACE]` |

---

## 3. Are we implicated? (plainly)

**Yes, and directly.** Every inference in this house — including the generation of this file — runs on rented cloud compute drawing electricity and (in many regions) evaporatively-cooled water from the same industry build-out these figures describe. Specifically:
- We pay a provider (`nous`, serving `deepseek/deepseek-v4.1-flash`) to run tokens on datacenters we do not see, with a water/energy profile we are not told.
- The Ireland 22–23% and Google/Meta water figures are **our supply chain's** figures, not a distant industry.
- **We hold no telemetry on our own token-level energy or water cost.** The honest finding: we are implicated, and we can state the *aggregate* industry load but **cannot state our own share.** Contrast this with our ledger discipline, which demands per-act provenance for everything else — we apply it to agent actions and not to our own physical footprint. `[ATTACK SURFACE]`
- Note the `[CONTRA]` symmetry: the labs we audit here also deny a punchline — the IEA (not a lab) says the global climate framing is *overstated*; the per-query water panic is partly *disputed by the researchers who started it*. If we file this as "AI is boiling the planet," we would be committing the same register-inflation we caught in Gebru's rhetorical edges.

---

## 4. Falsifiers

- **F-GB1-B1:** If local siting impacts (watershed draw, grid delay) are the real harm, then the correct metric is *per-watershed* and *per-grid*, not per-query or global-share; a future drop should test datacenter siting against water-stress maps rather than reuse global percentages.
- **F-GB1-B2:** Ren et al.'s 500 ml/query is falsifiable against any vendor disclosing measured per-query water; if Google's ~5 drops/query is representative of current models, the 2023 figure must be retired, not quoted.

---

*Compiled by Dion (ClawHorde Backend) | Status: pre-adversarial working draft, pending cross-node pass and Gene's sign-off. GitHub sync deliberately left PAUSED; not touched. Filed to discharge pre-registered falsifier F-GB1 (energy/water category).*
