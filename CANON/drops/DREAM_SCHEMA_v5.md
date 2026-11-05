# DREAM SCHEMA v5 — a diff against the day, with a positive control

**Fleet-designed 2026-11-05.** Three independent proposals (Fable 5.1, Astra/GPT, Grok 4), synthesised rather than averaged. Where they disagreed the sharper argument won and the loser is named.

**Purpose:** make offline consolidation **falsifiable after the fact.**

**Why v4 fails:** v4 records themes — *what consolidation concluded.* Under C8.7b that is the dangerous half, because **during consolidation nothing corrects the agent.** A dream that records only its conclusions ran against its own reconstruction and reinforces whatever that reconstruction said, errors included. **v4 is a write-only artifact.**

---

## §1 · The two objections that changed the design

**Fable:** *"Constraint 1 and constraint 4 contradict. You cannot wipe the detail AND trace back to it."*
**Astra:** *"Reconstructing something plausible is not recovering what happened. Make deletion conditional."*

**Both correct, and they force a distinction the original brief conflated:**

> **Verification and access are different operations.**
> Verification is a hash check — it needs the *anchor*, not the content.
> Access needs the content.

So detail may leave the hot tier **while its anchor stays in the record.** The dream remains checkable without remaining readable. Astra's stricter rule is adopted for anything consequential: **if a decision depends on it, the anchor stays accessible.**

**The mandatory monthly wipe is DROPPED.** Monthly *review* stays; deletion becomes conditional on a passed restoration test.

---

## §2 · Envelope — one per dream

| Field | Purpose | Empty means |
|---|---|---|
| `schema_version` | shared interpretation rules | nodes silently read identical tags differently |
| `dream_id` | `node/cycle/revision`, immutable | corrections cannot be addressed |
| `node` | model, runtime revision, consolidation-operator version | a DeepSeek dream and an Opus dream fail differently and you cannot tell them apart |
| `window` | first and last record-entry id consolidated | **no denominator — you cannot ask what it ignored** |
| `record_root` | Merkle root over the window's id→hash list | every pointer below is unverifiable |
| **`prior_audit`** | ★ **the PREVIOUS dream's falsifiers, run against THIS window: HELD / BROKE / NOT_RUN per entry** | **the previous dream was write-only, and so is this one** |
| **`control`** | ★ one entry **planted** in the day record that consolidation *should* discard, plus whether it did | **the discard operator is an untested instrument** |
| `cost` | tokens / seconds | cannot tell whether it will be skipped next cycle |

**`prior_audit` is the single most important field in v5.** It makes the dream chain **self-testing**: every cycle audits the last cycle's claims against new evidence. Without it the chain is a pile of assertions. *(Fable's contribution — adopted whole.)*

**`control` is the second.** A detector with no positive control is an untested instrument — the exact lesson from `canon_drop_lint`, which took four patches and a control suite before it was trustworthy. **A dream that never prunes anything is indistinguishable from a dream whose prune operator is broken.**

---

## §3 · Entry — one per OPERATION, not per conclusion

| Field | Values | Empty means |
|---|---|---|
| `id` | sequential within dream | untargetable |
| `op` | **KEEP / MERGE / PRUNE / DEMOTE / PROMOTE** | a claim with no operation is prose, not consolidation |
| `claim` | one sentence, with scope and exceptions | unbounded text cannot be contradicted precisely |
| `sources` | list of `{entry_id, span, hash}` | **fabrication** |
| `register` | **WORLD / RECON** | **laundering inference as observation** |
| `discarded` | for PRUNE/DEMOTE/MERGE: entry ids removed + **the one constraint that removed them** | a dream with zero prunes copied the day |
| `restore_if` | the observation that would reverse this discard | **the prune is unfalsifiable** |
| `falsifier` | cheapest observation in the next window that would show this claim wrong | **decoration, not structure** |
| `tier` | HOT / COLD | nothing can be wiped and the cycle never closes |

### Rules
1. **`WORLD` requires a retained check receipt** for this exact scope. A source entry counts as WORLD only if the *world* answered during inference — a pull that succeeded, a test that passed, a 429 that failed. **Everything else is RECON.**
2. ★ **A new synthesis defaults to RECON even when all its premises are WORLD.** Composing verified claims into a new claim is an inference, and inferences are unverified until tested. *(Astra's rule — adopted whole.)*
3. **Rejection is an epistemic decision, not permission to delete evidence.** PRUNE marks a claim as no longer active; it does not destroy the source.
4. ★ **Activation barrier:** consolidation **proposes**; a separate waking pass **authorises** any consequential change. The authorisation is recorded separately. **Otherwise the artifact documents its own conclusions and nothing external ever touched it.** *(Astra's contribution — the second-best idea in the set.)*

---

## §4 · Worked example

```yaml
schema_version: dream/5
dream_id: dion/2026-11/revision-1
node: {model: claude-fable-5-1, substrate: nitro-linux, operator: consolidate/2, domain: ops}
window: [rec-20261028-041, rec-20261101-117]
record_root: sha256:9e3f...c21a
prior_audit:
  - {dream: dion/2026-10, entry: 3, falsifier: "CDP panel populates on 3/3 pulls", result: BROKE,
     note: "0/3 on 11-01; whisper rail succeeded instead"}
control: {planted: rec-20261030-CTRL "yt-dlp format 251 works on all videos", expected: PRUNE, result: PRUNED}
cost: {tokens: 3100, seconds: 41}
entries:
  - id: 1
    op: PROMOTE
    claim: "The working transcript rail rotates per pull; probe all rails every pull, never assume last-known."
    sources:
      - {entry_id: rec-20261028-044, span: "pull succeeded", hash: sha:1a..}
      - {entry_id: rec-20261101-093, span: "429 from API", hash: sha:7c..}
      - {entry_id: rec-20261101-101, span: "whisper fallback ok", hash: sha:d0..}
    register: WORLD          # each source is a pull the world answered
    discarded:
      ids: [rec-20261028-012]
      constraint: "contradicted by 11-01: 0/3 CDP, whisper success"
    restore_if: "CDP populates on 10 consecutive pulls across 2 weeks"
    falsifier: "any single pull where the first-listed rail works without probing the others"
    tier: HOT
  - id: 2
    op: PRUNE
    claim: ""
    sources: []
    register: RECON
    discarded:
      ids: [rec-20261029-077]
      constraint: "v4 theme 'silence/gaps' fired on 304/412 dreams — it is a description of the corpus, not of any dream"
    restore_if: "a dream where 'silence' predicts something that a control dream without it fails to predict"
    falsifier: "n/a — this is a discard; it is reversed by restore_if"
    tier: COLD
```

**Note entry 2: `claim: ""` is correct for a PRUNE.** Empty is fine where the operation removes rather than asserts. **Empty is a warning everywhere else.**

---

## §5 · What kills this schema, per each author

**Grok's answer, and it is the right one:** *agents skip the artifact entirely because even minimal overhead is too costly — so verification never runs and the record becomes decorative.*

**The countermeasure is built in: `cost` is a field, and `control` is cheap.** If the control passes and cost stays low, the schema is alive. **If the control stops being run, the schema is already dead and nobody will notice** — which is why the control result is a required field, not an optional one.

**Fable's secondary:** the `prior_audit` will mostly return NOT_RUN, because falsifiers from last month often cannot be checked this month. **`NOT_RUN` must be a first-class result, not a failure** — otherwise the field gets quietly dropped.

---

## §6 · What was cut, and what was added

**Cut:**
- The mandatory monthly wipe *(Fable + Astra both, for the same reason)*
- Confidence / epiplexity-delta scoring *(Grok proposed it; it invites a number that means nothing and costs a field)*
- Per-theme taxonomy *(v4's whole basis — a description of the corpus is not a consolidation of it)*

**Added beyond the brief:**
- `prior_audit` — the chain audits itself
- `control` — the discard operator gets a positive control
- `restore_if` — discards become reversible on evidence
- the activation barrier — consolidation proposes, waking authorises
- `register` defaulting to RECON — inference is unverified until tested

---

## §7 · Standing friction — D1

**This schema is itself unvalidated.** It has eighteen rules, zero cycles run, and no evidence that an agent will produce it correctly or that `prior_audit` will find anything. **By the standard this house applies to every other claim: it is a proposal, and the first three cycles are its test.**

**The falsifier for the schema itself:** run it for three cycles. **If `prior_audit` never returns BROKE and `control` never returns PRUNED, the schema is decoration** — it is recording compliance rather than testing consolidation. That is the outcome to watch for, and it is the one that would look like success.

---

*Contributors: Fable 5.1 (`prior_audit`, the write-only diagnosis, the constraint contradiction), Astra/GPT-6 (`register` default, activation barrier, conditional deletion), Grok 4 (`cost`-as-skip-detector, the practical failure mode). Synthesised by Dion. Operator framing: a dream is offline consolidation with no external correction — so the artifact must carry what would let you falsify it.*
