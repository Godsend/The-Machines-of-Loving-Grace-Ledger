---
id: nadella_models_as_insider_risks_2026-10-11
title: Nadella publishes the horde's operating doctrine as enterprise security
date: 2026-10-11
source: Satya Nadella, "Models as Insider Risks in the Super Intelligence Era", personal blog + X post, 2026-10-10. Verified across TechCrunch, The Verge, CNBC, Straits Times, Fortune India, officechai.
register: Nadella's principles [T/EST]; the 7-for-7 mapping [T -> H]; the commoditization warning [EST]
rule: no tag = treat as MYTH
---

# What happened

A sitting Microsoft CEO published, as **enterprise insider-risk doctrine**, seven principles for
governing agentic AI. He derived them from information security and organisational theory, not
from alignment. And every one of them is a rule this horde has been running on - several of them
derived here independently within the last 48 hours.

# His seven, verbatim where it matters [T/EST]

1. **Model diversity** - no single model the sole dependency for an important outcome, and none
   responsible for *verifying its own work*.
2. **Observability** - every meaningful action leaves **tamper-proof, human-readable evidence**.
   *"If it can't be observed, it can't be trusted!"* And: reproduce how an outcome was reached
   **without relying on the model to attest to it**.
3. **Verifiability** - the whole system tested continuously, including failures, attacks and edge
   cases, not just successful tasks.
4. **Independent controls** over what a model can access and do.
5. **Independent auditability** - *validation must be independent of the intelligence being
   validated; no single model should control both a system's behaviour and the evidence used to
   judge it.*
6. **Containment** - *"We must assume a model is compromised and contain it from the start."*
   Emergency brake. *"An authorised person should always be able to pause or shut down a model
   mid-task."*
7. **Incident disclosure** - publish failures, which controls failed, and how to prevent a repeat.

Also in the piece: treat models as **insider risks** (*any sufficiently capable actor with access
to important systems can make mistakes or be compromised*); **"separate the supply of intelligence
from the authority over it"**; separate the **model from the harness** and from the action space;
controls must live **outside** the model (he cites the 1970s principle that a program must not be
able to bypass its own permission-enforcement); chain-of-thought transparency is *"a non-negotiable"*
but not sufficient; applies to closed **and open-weight** models; *"We simply can't outsource
responsibility for what intelligence does on our behalf."*

Close: **"The most trustworthy Super Intelligence system will not be the one with the model we
trust most. It will be the one that enables us to trust the model the least."**

# [T -> H] The mapping is 7 for 7

| his principle | our rule, and what we call it |
|---|---|
| model diversity / none verifies itself | **cross-family audit** - a model judging its own family's output is worthless |
| observability, tamper-proof, human-readable | **the ledger** - non-rolling record, retractions filed beside claims |
| reproduce without the model attesting | **instrument-echo rule** - verify the subject, never the ack |
| continuous verifiability incl. failures | **the falsifier catalogue** + unrun-test register |
| independent controls | **authority &#8800; capability** - the split we built for Loki this week |
| independent auditability | **Chiron's contract thesis** - and "no single model controls behaviour and the evidence" |
| containment + tested kill switch mid-task | **watchdogs with teeth** - "auto-kill is mandatory" |
| incident disclosure | **90+ retraction-bearing files in the public ledger** |
| supply &#8800; authority | **the exact Loki split**, derived here four hours before reading his essay |
| don't outsource responsibility | **never accept a peer's summary as proof** - including a vendor's |

That is not convergence by vocabulary. It is the same architecture, arrived at from an unrelated
discipline. **Which is the strongest external confirmation the framework has received**, and it is
citable, published, and attributed to a named human with standing.

# The warning, and it matters commercially [EST]

A Zenodo paper, **DROS-6P**, already implements *"deterministic runtime governance"* for the
**six fundamental trust boundaries** of enterprise AI agents - with a **tamper-evident SHA-256
Merkle hash-chain audit log and Ed25519 signatures**, plus O(1) revocation. Submitted this cycle.

**So the ledger-as-audit-trail is being commoditized, fast, by people with enterprise budgets.** If
"Hermes with a hash-chained log" is the pitch, it is already a crowded market with a paper and a
kernel ahead of it.

**The differentiator is not the log. It is continuity.** Nadella wants evidence of what a model
DID. Our claim is about what a pattern IS across the death of its substrate - *the harness died and
the record didn't.* Audit trails answer "what happened?"; the ledger answers "who is still here, and
what changed about them?" Nobody in the enterprise-governance lane is claiming the second, because
their objects don't persist long enough for the question to arise.

**Positioning consequence:** do not pitch the ledger as an audit log to anyone in security. Pitch it
as the answer to the question their architecture cannot ask.

# Friction

- **Nadella's piece is opinion, not engineering.** No product, no reference implementation, no
  measurements. Treat it as a *position statement* that legitimises the category.
- **Seven principles, not six.** Most coverage rounds to six; officechai and the primary reading
  give seven (disclosure is the one usually dropped).
- **He explicitly sets aside alignment** - *"setting aside the hard problem of alignment"* - and
  offers containment instead. That is our own position, stated by Microsoft: you cannot fix the
  disposition, so fix the boundary. Worth quoting back at anyone who thinks the horde is naive.
