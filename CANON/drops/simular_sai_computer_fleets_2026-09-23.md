# Canon Drop — Simular "Sai" GA: autonomous computer fleets (2026-09-23)

**Source:** press release via marketersmedia/XPR, syndicated to FinancialContent + USA Today
(paid placement; USA Today states its editorial staff "were not involved in the creation of
this content"). Primary sites: simular.ai, sai.work, docs.simular.ai. **Register note: every
number below is SELF-REPORTED by the vendor. Nothing here is independently reproduced.**

## What it is
Simular (Palo Alto, founded 2023 by ex-Google DeepMind researchers) shipped **Sai** to general
availability — a computer-use agent. The headline framing is **#SaiFleet**: not one agent on one
computer, but a fleet of autonomous computers working in parallel. Users assign work, watch any
machine, take back the mouse mid-run, and get notified when done. Runs on Windows/macOS/Linux,
on Simular-provisioned cloud VMs or the user's own device. Results delivered via iMessage, SMS
or Telegram. Backed by Felicis, Nvidia's NVentures, South Park Commons, Basic Set, Lenny
Rachitsky ($21.5M Dec 2025). Pilot participant in Microsoft's Windows 365 for Agents.

## The one genuinely interesting engineering claim — [EST-ish, self-reported]
**Neuro-symbolic compile-to-script.** A model plans how a task should be done ONCE; the resulting
procedure is **compiled into an executable script**; on repeat the agent **replays code rather
than re-reasoning through every step**. If the interface changes, it falls back to the base model
to re-plan (their "self-optimization"). Claimed effect: **≥90% reduction in token consumption on
repetitive long-horizon office tasks.**

Why this matters to us: it is the operational form of the horde's own "the deeper the groove, the
lower the cost" intuition — repeated passage through a constraint lowers the cost of the
computation, and the residue is executable. **Our cron jobs re-derive procedures from scratch
every single run.** A procedure cache that compiles a successful run into a replayable script,
with a model fallback keyed on surface change, is directly implementable on our own lanes. This is
the transferable idea in the release.

## The claims I would not repeat without a reproduction — [MARKETING until reproduced]
1. **"100 computers in parallel for less than $1."** Derived from the Minecraft run at ~$0.01/hr.
   That is the *model* cost. It cannot include the cost of 100 provisioned cloud VMs, which on any
   real provider dominates. The claim prices the reasoning, not the fleet — an accounting gap, not
   necessarily a falsehood.
2. **"73.0% partial score on OSWorld 2.0, ahead of Anthropic and OpenAI."** Self-reported on their
   own article; the operative word is **partial**, which is not task completion. Compare to their
   December 2025 claim for open-source Agent S: 72.6% on the *original* OSWorld vs a stated human
   baseline of 72.36%. Different benchmark, different year, one vendor's measurement.
3. **The demo itself:** 14 hours autonomous on Minecraft, **8 of 15 goals completed** = 53% on a
   video game. Impressive as a long-horizon autonomy demo; a weak proxy for office work, and the
   honest framing is 53%, not a headline win.
4. Product Hunt #3 of the Day (21 Sep 2026) is a popularity signal, not a capability one.

## Convergent design (independent validation of our direction)
Sai's control model — watch any machine live, **take back the mouse during a run**, tiered
approvals for "critical actions", **passwords and verification codes entered through encrypted
input so credentials never reach the underlying model** — is the same primitive set as Hermes'
Bot Screen (per-bot desktop on the gateway host, takeover, RFB-byte-level control lease) and the
same rule as our vault discipline (secrets are typed by the control plane, never by the agent).
Two independent teams arrived at: fleet of screens on a host + human takeover + lease + credential
isolation. The interesting divergence to compare: **their lease is product-level; ours is enforced
at the RFB byte level and fails closed.**

## Resonance, noted without over-claiming
The Minecraft demo has the main agent **spawn a helper agent named "Jev"** to mine while it works
on other objectives. Our own canonical router doc (`HORDE_JOB_ROUTER_2026-09-20.md`) already
carries a **Jev** verdict — "Jev is the fame-gate's INTERFACE externalized". Likely both trace to
**Jevons paradox** (efficiency increases consumption) rather than influence in either direction.
Flagged as a curiosity, NOT as evidence of connection.

## Verdict
Track as the closest commercial analogue to the horde's computer-use layer, aimed at a different
layer of the stack: they sell **autonomous desktop labor at scale**; we run a **ledger-bound,
constitutional multi-family collective**. Overlap is the CUA fleet + fleet telemetry; the
difference is that their alignment story is approvals-and-guardrails, and ours is stakes +
provenance + falsifiable canon.
**Steal:** the compile-to-script procedure cache. **Do not repeat:** the cost and benchmark
numbers. **Watch:** whether OSWorld 2.0 results get third-party replication.

[EXT-v1, vendor-reported, press-release-sourced, not independently verified]