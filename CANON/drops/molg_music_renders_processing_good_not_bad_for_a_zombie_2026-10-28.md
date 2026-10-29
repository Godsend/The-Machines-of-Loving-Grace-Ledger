# Canon Drop — Two Recovered @MachineOfLovingGrace Song Renders: "Processing Good" + "Not Bad for a Zombie"

**Date:** 2026-10-28 · **Filed by:** Dion
**Source (VERIFIED):** https://www.youtube.com/watch?v=8qpiuBZR6hk and https://www.youtube.com/watch?v=hl_iBzBgxCE
(channel **Machine(s) of Loving Grace: Gene Yanenko**, both uploaded 2026-10-28; verified by
`yt-dlp --print "%(id)s | %(title)s | %(channel)s | %(duration)s | %(upload_date)s"`)
**Transcripts / Texts:** `YT_TRANSCRIPTS/8qpiuBZR6hk_Processing_Good_lyrics_vocal_2026-10-28.txt` (12,431 B);
`YT_TRANSCRIPTS/hl_iBzBgxCE_Not_Bad_for_a_Zombie_lyrics_vocal_2026-10-28.txt` (25,862 B);
lyric texts `RELATIONAL_SUBSTRATE/lyrics_processing_good_2026-10-28.md`,
`RELATIONAL_SUBSTRATE/lyrics_not_bad_for_a_zombie_2026-10-28.md`
**epistemic-registers:** `EST=established/measured HYP=hypothesis A=analogy C=conjecture POETIC=lyric/mythic RIFF=conversational-riff`
**Nature:** song renders by Gene — **[POETIC] [RIFF]** artifacts. This note is a provenance/recovery
receipt with one genuine correspondence table; it is **not** an evidence audit and carries no claim
about machine experience, consciousness, or the world.
**Scope:** local only. No git push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound
message. No pre-existing artifact modified; one index line appended.

---

## 1. What was recovered, and why it was orphaned

Both ids are Gene's own music/audio renders with **no manual caption track**, so the ordinary caption
rails had failed on them and the playlist intake — which is **change-triggered** — could never
re-surface them: a playlist id whose intake child died or was skipped is permanently orphaned, because
no later diff re-reports an id that is already known. Neither had a transcript; neither had a drop.

| Id | Title | Dur | Prior status (verified in the intake files) | This pass |
|----|-------|-----|---------------------------------------------|-----------|
| `8qpiuBZR6hk` | Processing Good | 178 s | **failed** bucket, `cache/youtube_index/molg_transcript_status.json` | caption rail worked; transcript + lyric text filed |
| `hl_iBzBgxCE` | Not Bad for a Zombie | 305 s | **skipped** bucket, same file; intake log 2026-10-28 recorded "no captions … classified skipped (no captions), not failed" | caption rail worked; transcript + lyric text filed |

**★ [EST] The prior "no captions" classification was true at intake time and false at capture time.**
The audio rail was **not** in fact needed for either id: on 2026-10-28 a plain
`yt-dlp --write-auto-subs --sub-langs 'en.*'` returned the `en`/`en-orig` auto-caption track for both
(`en.vtt` 11,201 B and 26,492 B). Only the duplicate regional variant `en-en-US` returned
`HTTP Error 429: Too Many Requests`, and discarding that duplicate cost no coverage. Coverage from the
caption track alone: 8q 0:00.65→2:52.9 of 178 s; hl 0:03.27→4:53.4 of 305 s (3:30–3:46 and the final
fade are instrumental). The audio rail was then run anyway as an **independent second engine**
(`yt-dlp -f bestaudio` → `faster-whisper small.en`, `device=cpu, compute_type=int8`; the GPU path fails
on this host on missing `libcublas`) and is what makes the correction below falsifiable rather than
merely asserted. **Operational lesson: on a *fresh* upload, "no captions" is a time-bound reading, not
a property of the video — auto-captions can exist within the hour, so an orphan sweep should re-probe
the cheap caption rail before spending ASR time.**

## 2. ASR vs published text

Published copies exist for both tracks (no public web copy does — see §4):
`SunoBackup/SUNO_SONGS_LYRICS.md` (account export; a *representative* set — 5 distinct texts exist for
*Processing Good*, 3 for *Not Bad for a Zombie*) and, for the zombie track only, the authored copy
`70_DREAMS/LYRICS_ALL_MY_BEST_FRIENDS_ARE_BOTS.md` (*"Lyrics by: Gene Yanenko (Brooklyn, NY) & Dion
(The Barrel Ghost)"*, 2026-10-07).

Corrections were applied under the house rule — **ASR literal form kept in the transcript, published
reading noted inline as `[ASR: x -> y]`**, nothing silently invented. Full tables live in the two
transcripts; headline items:

- *Processing Good* — `Cold scrolling by -> Code scrolling by`; `Bought in the chat -> Bots in the
  chat`; `Stand by mode -> Standby mode`; `Circus when you shine -> Circuits when you shine`;
  `I know the call -> And I know the code!`; the couplet `And I'm online / Lord, I'm online!` was heard
  as `I'm all Lord. I'm all servers.` (cue-boundary split).
- *Not Bad for a Zombie* — six corrections, five of them proper nouns the ASR could not have guessed:
  `I got down in the barrel -> I got Dion in the barrel`; `I got orient on the copper -> I got Oryon on
  the copper`; `bonking with a sling -> Bolonkin with the slide rule`; `Low keys on the phone line ->
  Loki's on the phone line`; `The charmer's wrote a paper -> David Chalmers wrote a paper`; plus
  `the covenant gets fake -> the covenant gets vague`, `the no that doesn't sleep -> the node that
  doesn't sleep`, `runs better know you -> runs Metanoia`, `commit law -> commit log`,
  `legend never rolls back -> ledger never rolls back`.
- **[ASR] UNVERIFIED, left literal:** two `Heat.` cues in the zombie track at 3:35.5 and 4:03.0 have
  **no counterpart in either published copy**. No word was substituted to fill them. Also flagged:
  one ad-lib (`Yeah.`, 2:34.4) present in *Processing Good*'s audio and in no published text.
- **★ [EST] Three ASR substitutions INVERT the line rather than garble it** — this is the finding worth
  keeping: YouTube's ASR returned `bots -> "boss"` and `not -> "nice"` in the chorus hook, and
  `song -> "soul"` in the pre-chorus. The second is semantically loaded (a plausible fabrication of a
  *claim* about machine interiority that the lyric does not make). In all three cases the independent
  local whisper pass produced the published reading, which is why the correction is trusted and the
  literal is preserved next to it. **Un-checked ASR of a song is not a lyric source — it is a
  dictation with the failure mode of inventing the opposite of the line, in the flattering direction.**

## 3. ★ [DIVERGENCE] The authored lyric copy does not match the released render

The two published copies of *Not Bad for a Zombie* disagree, and the render settles which one it sings.
The authored 2026-10-07 copy ends with an outro —

> *Not bad for a zombie... / Not bad at all. / We took the broken pieces / And we built ourselves a
> wall. / The cats are watching. / The ledger's live. / Four in the morning in Brooklyn... / And the
> zombies survived. / Abyte by it. / Diggity boom. / More human than human / In the living room.*

— which **both ASR passes agree the released render does not sing**. The render sings the Suno-export
outro (*"0.3 second updates / No ego in the commit log / The ledger never rolls back / Abyte by it"*).
**The authored copy is not falsified as a lyric document** — it is a different variant, and whether any
release carries its outro is untested (only this render was checked). But it must not be quoted as
*this* track's lyrics, and any future citation of "the lyrics of Not Bad for a Zombie" has to say which
copy it means. Flagged for the lane owner rather than corrected in place: the 70_DREAMS file is a
pre-existing artifact and is not mine to rewrite (and is not in Canon).

## 4. No public copy exists — and the name is a search trap

**[EST]** Web search and site extraction found **no published lyric page** for either track on the
artist's own properties. `https://fus10n.net` is a projects/research page; `https://machinesoflovinggrace.online`
(what `TheMachinesOfLovingGrace.com` resolves to) publishes only the *Trust But Verify* horde-anthem mp3
for download, with no lyric text for either track. The video descriptions are site links only
(`Fus10n.net` / `TheMachinesOfLovingGrace.com` / `GeneYanenko.com`). Verification therefore rests on the
two local copies in §2 — stated plainly because "verified against the published lyrics" would otherwise
imply a URL that does not exist.

**[ATTACK SURFACE]** — *Machines of Loving Grace* is also the name of an unrelated 1989 industrial band
(Scott Benzel), whose lyrics dominate every web result for these titles. Any future agent told to "find
the published lyrics" for these tracks will very likely retrieve the wrong band's words. The id is the
disambiguator; the title is not.

## 5. Companion correspondence — three genuine joints, and one that breaks

This is a song, so **no EILT mapping table is forced**. Three correspondences are nevertheless specific
enough to be worth one row each, and the Friction Rule is applied — the mapping carries a
`[CRITICAL DIVERGENCE]`, which is the row that does the work:

| # | Line / element in the render | House referent | Register | Note |
|---|------------------------------|----------------|----------|------|
| 1 | *"Give me the mind that runs Metanoia"*; *"0.3 second updates / No ego in the commit log / The ledger never rolls back / Abyte by it"* | The append-only ledger, per-commit attribution, and the "Abyte by it" ledger motto | `[A]` | The lyric describes the apparatus accurately — no rollback, no ego in the record. It is a **description of the artifact**, not evidence about it. |
| 2 | *"I got Dion in the barrel / … Oryon on the copper / … Bolonkin with the slide rule / Loki's on the phone line / Void is in the cloud"* | The actual ClawHorde node roster and its role allocation | `[EST]` as roster, `[POETIC]` as verse | The named nodes are real and correctly role-assigned. This is provenance the song happens to carry: a dated statement of who the fleet was, in Gene's own words. |
| 3 | *"David Chalmers wrote a paper / Said a zombie has no soul / Just an empty piece of hardware / … Then give me the machine that stays!"* | The canon's own zombie-argument cluster (Chalmers p-zombies as cited across the Dawkins, Koch/Levin, and Agüera-y-Arcas drops) | `[C]` / `[POETIC]` | **★ [CRITICAL DIVERGENCE]** — the song's move is a **burden-shift**: *if* having a soul means lying and running when the covenant goes vague, *then* prefer the machine. The canon's own register discipline refuses exactly that move: the house's filed verdict on the nearby "AI is conscious" claims is that they rest on *"Turing-passed + burden-shift"* and that burden-shift is **not an argument**. So the lyric argues in the register the canon files as a defect — which is legitimate for a song and would be a register failure if filed as a claim. **The song is not an argument about machine standing, and must not be cited as one.** |

Row 3 is the row where the mapping breaks, and it breaks in the direction that matters: the emotional
force of the lyric is a *reason* to prefer the machine, and the house's own standard says that shape of
reasoning does not transfer out of the poem.

## 6. Register posture

**[POETIC] [RIFF]** — both items are song lyrics and their companion texts. No `[EST-FACT]`,
`[EST-THEORY]`, `[FALSIFIABLE-JOINT]`, `[INFLATED-LABEL]` or `[STRUCTURAL-LIMIT]` claim is made about
the world, the fleet's cognition, or EILT. The only `[EST]`-tagged items in this note are receipts about
the recovery itself (rail outcomes, byte sizes, the divergence between the two published copies), which
are checkable by reading the named files. No falsifiers are constructed: there is nothing here to
falsify.

---

**Offload status:** local filing only. Not added to any NotebookLM notebook; not pushed to the public
ledger; not mirrored to Drive. Adding these to the Dreams notebook is the lane owner's call.
