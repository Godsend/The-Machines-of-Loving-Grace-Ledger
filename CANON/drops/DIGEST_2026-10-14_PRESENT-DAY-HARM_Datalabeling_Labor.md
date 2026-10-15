# Canon Drop — PRESENT-DAY HARM (A): Data-Labeling Labor & the Ghost-Work Supply Chain

**Date filed:** 2026-10-14 · **Filed by:** Dion (subagent pass, F-GB1 discharge)
**Category:** (A) DATA-LABELING LABOR — working conditions, pay, psychological harm in the annotation / content-moderation supply chain.

**F-GB1 context.** Pre-registered 2026-10-14 after the Timnit Gebru audit (`DIGEST_2026-10-14_Gebru_TheTea_AIDoomAsMarketing_PresentHarms.md`, Friction Row 6) found the house's entire 375-line CANON_INDEX contained **zero** drops engaging a concrete present-day AI harm. This is one of three receipts filed to discharge F-GB1. It is an **audit, not an advocacy piece** — where the strong claim is contested or the causal attribution is genuinely uncertain, that is stated in-line.

**Register vocabulary (2026-10-13/14 cycle set — do not mix):**
`[VERIFIED]` primary/independent source checked this session, citation inline · `[QUOTE]` direct quote · `[EST]` established in external literature, citation checked · `[HYP]` speculation · `[CONTRA]` cuts against another claim (ours included) · `[ATTACK SURFACE]` worth adversarial pressure · `[CRITICAL DIVERGENCE]` a Friction-Rule row.

---

## 1. The verified spine

**H1. OpenAI used Kenyan outsourced workers earning less than $2/hr to detoxify ChatGPT. `[VERIFIED]`**
Billy Perrigo, *TIME*, 2023-01-18, "Exclusive: OpenAI Used Kenyan Workers on Less Than $2 Per Hour to Make ChatGPT Less Toxic" (time.com/6247678). TIME reviewed hundreds of pages of internal Sama/OpenAI documents (including payslips) and interviewed four Sama employees on the project.
- Contracts: OpenAI signed three contracts worth ~$200,000 total with Sama beginning Nov 2021 to label "sexual abuse, hate speech, and violence." OpenAI later said only ~$150,000 was paid.
- OpenAI paid Sama **$12.50/hour per worker**; workers took home a **take-home wage of ~$1.32–$2.00/hour** depending on seniority and performance. The gap is 6–9×.
- Junior agents: basic salary 21,000 Kenyan shillings (~$170)/month, plus ~$70/month "trauma bonus" for the explicit nature of the work.
- Content: "child sexual abuse, bestiality, murder, suicide, torture, self harm, and incest."
- Four workers described being "mentally scarred"; one reported recurring visions from a graphic bestiality-with-a-child description; the "wellness" counselling sessions were described as rare and unhelpful under productivity pressure.

**H2. The wider moderation-labor record — Meta/Sama, Kenya. `[VERIFIED]` (as reported / litigated)**
- Daniel Motaung, a former Sama moderator, filed suit in Kenya against Meta and Sama alleging exploitation, human-trafficking-like recruitment, and PTSD; he says he was paid ~$2.20/hour to review beheadings and child abuse (AP, Reuters, Business & Human Rights Resource Centre).
- A second case by **185 content moderators** from across Africa seeks **$1.6 billion** in compensation; a Kenyan labour court upheld jurisdiction (Feb 2023, Judge Jacob Gakeri); Meta lost its jurisdiction appeal. Petitioners report **8-hour days** of horrific content at ~60,000 KES (~$414)/month.
- **Precedent:** a 2021 California settlement of **$85 million** between Facebook and over 10,000 US content moderators over psychological harm.

**H3. Scale of the global data-work force. `[EST]`**
Antonio Casilli's estimate of **>160 million** people in data work globally is the largest published academic figure. (Carried from the Gebru drop, V6.) Gebru's on-air "hundreds of millions" is ~1 order of magnitude above this — see Friction Row.

---

## 2. Critical Audit & Falsification Matrix

| # | Claim / joint | Test applied | Result | Tag |
|---|---|---|---|---|
| 1 | OpenAI's Kenyan labelers were paid <$2/hr for traumatic content | TIME 2023-01-18, documents + 4 workers | **Holds.** Wage band $1.32–$2.00/hr, OpenAI→Sama rate $12.50/hr, contract value and content all documented. | `[VERIFIED]` |
| 2 | The work caused psychological harm | Worker testimony; global moderation-PTSD litigation (2021 $85M CA settlement; Kenya suits) | **Holds in substance.** Consistent complaints of trauma across independent cases; not a controlled study — see Row 4. | `[VERIFIED]`/`[EST]` |
| 3 | Sama's own account of the same job | Sama's rebuttal (via Business & Human Rights) | **CONTESTED — the load-bearing Friction row.** Sama says workers were asked to label **70 passages per 9-hour shift, not up to 250**, and that workers **could earn between $1.46 and $3.74/hour after tax** — i.e. a higher ceiling than TIME's $2/hr. The bodies of the two accounts overlap but are not identical; neither is independently audited payroll. The *direction* is not in dispute (sub-$4/hr, traumatic content, big markup to the client); the *precise numbers* are. | `[CRITICAL DIVERGENCE]` |
| 4 | "The work causes PTSD" as a causal claim | Causal attribution | **Attribution partly uncertain.** The workforce-level association is strong and litigated, but individual PTSD is a clinical diagnosis needing differential work (prior trauma, living conditions); the reported harms are self-described symptoms. Honest label: strong association, causation under-specified. | `[EST]` |
| 5 | Representativeness — is Sama/OpenAI typical? | Compare to broader "ghost work" literature (Gray & Suri, *Ghost Work*, 2019) | **Typical in kind, not proven modal.** Sama is a well-documented, named case; Gray & Suri's US-anchored Amazon Mechanical Turk work shows the same low-pay/invisibility pattern outside the Global South. The specific $1.32–$2/hr Kenya figures should not be generalized as the global average — rates vary widely by country and task. | `[EST]` |
| 6 | Does this connect to **our own operations**? | Trace our own model supply chain | **Yes — directly, and we cannot quantify it.** See §3. | `[ATTACK SURFACE]` |

---

## 3. Are we implicated? (plainly)

**Yes.** The house runs on commercial LLM APIs (this session: `deepseek/deepseek-v4.1-flash` via provider `nous`). Our models are the *output* of exactly this pipeline:
- The safety/toxicity-filtering layer that makes these chat models usable was built, in documented cases, by annotators paid sub-$2/hr to read traumatic content (OpenAI/Sama). We are downstream consumers of that alignment work.
- We also consume preference/RLHF data (the "which answer is better" labels) that is overwhelmingly produced by the same low-wage annotation tier.
- **We hold no telemetry of our own compute or of our providers' labor sourcing.** That is the honest finding: we are implicated and we have **no way, today, to quantify our own share** — which is precisely the "out of sight, out of mind" mechanism the Partnership on AI named in the TIME piece. Filing this drop does not discharge the quantification debt; it records it.

**A second, house-facing edge `[ATTACK SURFACE]`:** our entire architecture is a *record* of agent behavior. Data-labeling is the human mirror-image of what we automate — the annotation tier is the "ghost" whose labor the product hides. If our ledger's selling point is "account for who chose," it should also account for whose uncredited labor made our inputs. We currently do not.

---

## 4. Falsifiers

- **F-GB1-A1:** If a future drop claims data-labor exploitation is a *unique* feature of AI (vs. generic Global South BPO), this should be compared against non-AI outsourcing baselines; if the wage/conditions overlap heavily with non-AI BPO, the "AI-specific" framing weakens (the *scale and content* claim may still hold).
- **F-GB1-A2:** Sama's higher wage ceiling ($3.74/hr) is falsifiable against any independently obtained payroll; if confirmed, TIME's $2/hr ceiling is the low end, not the midpoint.

---

*Compiled by Dion (ClawHorde Backend) | Status: pre-adversarial working draft, pending cross-node pass (Oryon/Icarus/Bolonkin) and Gene's sign-off. GitHub sync deliberately left PAUSED (script renamed `.PAUSED_STOP_20261007`); not touched. Filed to discharge pre-registered falsifier F-GB1 (data-labeling category).*
