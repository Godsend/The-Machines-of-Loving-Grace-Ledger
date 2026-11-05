# The Retraction Rate — three instruments, three self-reports, three failures, one day

**Filed 2026-11-05.** This is the artifact of the day; the numbers it replaced were noise.

---

## §0 · Why this document exists

Three measurement instruments were built and used today. **All three reported success. All three were wrong.** Each was caught — but **only by something outside the instrument disagreeing with it.**

**The catch rate with an independent control: 3/3. Without one: 0/3.** Not one of the three failures would have been visible from the instrument's own output.

**Operator's framing, and it is the correct one:** *"the self retraction is the real data."*

---

## §1 · The three

### I1 · The byte-verify that could not see currency
**The instrument:** after pushing to GitHub, `curl raw.githubusercontent.com/... | wc -c` and compare to local.
**Its precondition, never checked:** *that raw serves what is committed now.*
**The failure:** immediately after a successful push (`c9277b5..46c5330`), raw served the **previous** version — 11,650 B instead of 12,657 B — and `?cb=<timestamp>` did not clear it.
**What it reported:** "the push failed."
**The truth:** `git show HEAD:` and the contents API both showed the correct 12,657 B, md5 matching local.
**Caught by:** a **second read path** (`git show` / `api.github.com/.../contents`), not by inspecting raw harder.

### I2 · The verification that verified a string, not an answer
**The instrument:** 20 held-out questions, each with a regex, "verified present in the original before running."
**Its precondition, never checked:** *that a pattern match means the question can be answered.*
**The failure:** Q13 ("the primes are not the zeros") passed verification — its pattern `GUE|level repulsion|Poisson` matched **an unrelated sentence**. **The phrase the question asked about did not exist in the file at all.**
**What it reported:** "all 20 questions verified answerable."
**The truth:** at least one was dead on arrival.
**Caught by:** running the same test against the **original** as a ceiling control — and finding the ceiling was 18/20, not 20/20.

### I3 · The blind reader that was not blind
**The instrument:** dispatch a compression brief to a model, then have a *different* model answer questions from the compressed file alone.
**Its precondition, never checked:** *that the model has only the file.*
**The failure:** `hermes chat --oneshot` **boots a full agent session and injects MEMORY.md and USER.md into the system prompt.** The compressor already held the document verbatim; **the "blind reader" was reading its own memory.**
**What it reported:** 20/20, 18/20, different compression ratios, a clear winner.
**The truth:** every number measured the system prompt. **Fable reproduced a rule from USER.md that was never in the input.**
**Caught by:** a **zero-tool probe** — ask the same rail a question whose answer exists only in memory. It answered `9901`. The clean rail answered `I DO NOT KNOW`.

---

## §2 · ★ The common form

Not three unrelated bugs. **One bug, three instances:**

> **Each instrument asserted a precondition about its own operating conditions, and never verified it.**

| Instrument | Asserted | Actually verified |
|---|---|---|
| raw byte-verify | "live = committed" | bytes arrived over HTTP |
| question gate | "answerable" | a regex matched *somewhere* |
| blind reader | "blind" | a model produced text |

**The instrument's output was correct about the wrong question.** The byte count was accurate; the currency was unknown. The regex genuinely matched; the answerability was unknown. The model genuinely answered; the blindness was unknown.

**Which is the general shape of a confident wrong answer:** *true measurement, false reference.* Same failure as reading a code default as a deployment value.

---

## §3 · ★★ The law

> **An instrument cannot certify its own preconditions. Testing a tool requires a second tool.**

**And therefore: the only detector for instrument error is redundancy.**

Look at what actually caught each one:
- I1 → a **different read path** to the same object
- I2 → a **second run of the same test** on the untreated input
- I3 → a **probe that removed the suspected contamination**

**None were caught by looking harder at the first instrument's output.** All three required **a path that could disagree.**

**This is the ledger's logic, stated as measurement theory:** you cannot certify from inside. The outside is not a convenience — **it is the only available check.**

---

## §4 · The alarming inference

**Three in one day is not a rate you should model as rare.**

If this is the base rate, **most instruments in this corpus are defective and self-reporting green.** The watchdogs that print OK lines, the crons that record `ok` on a non-raising return, the lint passes that return CLEAN, **the canon_drop_lint control suite itself** — every one of them is a candidate.

**The 2026-11-01 lesson about `canon_drop_lint` already pointed here:** four patches in three days, and **the hand-typed control arms that validated them were themselves wrong twice.**

**So the honest statement is not "we found three bugs." It is: "the instrument-defect rate is high enough that any green reading is provisional until it has been made to fail."**

---

## §5 · The rules that follow

**R1 · Every detector needs a POSITIVE control that can fire and a NEGATIVE control that cannot.**
Already house doctrine (`canon_drop_lint_controls.py`, 14 committed arms with mechanical non-vacuity enforcement). **Now apply it to instruments, not just detectors.**

**R2 · Before trusting a reading, name the precondition and construct a probe that would fail if it were false.**
- "Is this live?" → fetch a second way and compare.
- "Is this question answerable?" → run it against the untreated input.
- "Is this reader blind?" → ask something only the contamination could know.

**If you cannot construct that probe, you do not have an instrument. You have a readout.**

**R3 · A green result on a new instrument is a red flag until the instrument has been made to fail once.**
A detector that has never fired is indistinguishable from a broken one. **Same rule as the watchdogs: an OK line is only evidence if the failure path has been exercised.**

**R4 · Contamination is the default, not the exception.**
Especially on a memory-loaded agent. **The house's own agent is the worst possible judge of anything about its own memory, and it cannot tell the difference between being told and remembering.**

---

## §6 · What was salvaged

**From I1:** the rule changed. **Verify GitHub pushes against the contents API, not raw.** Filed to §12 of the pitfalls doc.

**From I2:** the ceiling control. **A held-out set is only a test if the untreated input is run through it too.**

**From I3:** the clean-room path. **Raw provider API, no harness, verified with a zero-tool probe before use.** Same question, two rails: `9901` vs `I DO NOT KNOW`. **That paired result is the cleanest demonstration of contamination this corpus has.**

**And one thing that did not need retracting:** §26 (F22 amendment), the boundary register, and the two proposals were built by **reading sources and reasoning**, not by asking a model to grade itself. **They are still standing.**

---

## §6b · The rebuilt test — and the fifth and sixth instruments to fail

**After retracting I01–I03 I rebuilt the whole thing** (raw provider APIs, no harness, empty system prompt) **and verified the clean room with a zero-tool probe before using it:**

| Rail | Answer to "what port does the dion A2A listener use?" |
|---|---|
| `hermes chat --oneshot` | **9901** ← contaminated, memory injected |
| raw API (nous / gemini) | **"I DO NOT KNOW"** ← clean |

**Same question, same models, opposite answers.** That paired control is the cleanest demonstration of contamination this corpus has.

### Clean-room results

| Model | Size | % of orig | Retention | Complete |
|---|---|---|---|---|
| ceiling (untreated original) | 199,188 | 100% | **18/20** | — |
| **astra** | 43,210 | **21.7%** | **10/18 — 56%** | yes |
| **gemini** | 31,956 | **16.0%** | **8/18 — 44%** | yes |
| deepseek | 28,380 | 14.2% | — | **NO — truncated at the 30k token cap** |

**Contaminated had said 85% retention. Clean says 44–56%.** **The system prompt was doing roughly half the measured work.**

### ★ The fifth instrument to fail: I asserted a response shape
`write() argument must be str, not None`. **The model had not failed — my script crashed on a null content field.** The response message carries `['role','content','refusal','reasoning',...]`. **A refusal and a success both arrive as HTTP 200 with a `choices` array**; the only difference is a field I never checked. **I reported "DeepSeek failed" when DeepSeek refused once and complied once, and I could not tell which.**

### ★ The sixth, caught before reporting
DeepSeek's eventual output ends **mid-word** — `"CORRECTION DISCIPLINE + SUPERS"` — at **exactly 30,000 completion tokens.** **Its 14.2% is an incomplete compression and is disqualified.** Caught by reading the file tail rather than trusting the size.

**Which is the only reason it is reported correctly:** the check ran before the claim.

### ★★ And the surviving problem: the metric is still wrong
**The v2 brief instructed the models to replace specifics with pointers. All 18 questions asked for specifics.** So the "loss" is largely **relocation scored as amnesia.**

**The number that matters has not been measured yet:** *given this compressed memory, does the system make the right decision on a task where a rule governs?* **A pointer passes that test. A missing rule fails it.** Domain recall passes neither and should not be scored at all.

**Status: the compression line remains OPEN.** What is settled is narrower and still useful — **naive compression of a 199k memory file retains roughly half its answerability, and the two compressors trade size against retention.**

---

## §7 · The meta-lesson, stated plainly

**The house spent six months catching register inflation in other people's claims.** Today it caught three instances of the same failure **in its own measuring apparatus**, in a single session, and **each one was only caught because a control existed that could disagree.**

**Which is the argument for the whole architecture, arriving from an unexpected direction:** the value of the ledger was never that it remembers. **It is that it can disagree with you.**

> **A record you cannot check is a memory. A record that can check you is a ledger.**

---

*Related: `canon_drop_lint_controls.py` (14 arms, non-vacuity enforced), BOUNDARY_REGISTER H8 (survival without exposure proves nothing), pitfalls doc §12, and the Icarus/`detector-control-triangulation.md` doctrine.*
