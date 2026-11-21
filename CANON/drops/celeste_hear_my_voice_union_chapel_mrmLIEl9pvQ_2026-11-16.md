# Canon Drop — Celeste, "Hear My Voice" (Live From The Union Chapel) [song performance / [POETIC]]

**Date:** 2026-11-16 · **Filed by:** Dion
**Source (VERIFIED):** https://www.youtube.com/watch?v=mrmLIEl9pvQ
**YT ID:** mrmLIEl9pvQ · **Title (as it appears):** "Celeste - Hear My Voice (Live From The Union Chapel) | From The Trial of the Chicago 7 on Netflix"
**Channel:** Celeste (@celestemusic) · **Duration:** 206 s (3:26) · **Uploaded:** 2021-03-23 · **Views/Likes at pull:** 4,968,980 / 92,771
**Transcript / Text:** `YT_TRANSCRIPTS/mrmLIEl9pvQ_hear_my_voice_union_chapel_2026-11-16.txt` (rail-labeled copy) + `YT_TRANSCRIPTS/mrmLIEl9pvQ_hear_my_voice_union_chapel_2026-11-16_structured.md` (raw rung-0 output)

epistemic-registers: EST=established HYP=hypothesis A=analogy C=conjecture POETIC=poetic/expressive RIFF=improvisational aside

---

## §0 Does this source warrant a substantive drop? — No, and that is the finding

mrmLIEl9pvQ is a **solo live song performance**, not a talk, interview, or argument. It contains **no spoken word, no interlocutor, no claims, no numbers, no citations** — nothing to audit, verify, or map. This drop is therefore deliberately thin: it records (a) that the source was read by a real rail, (b) what the video actually is, (c) the song's lyrics at their true evidence class, and (d) the song's provenance. **No EILT mapping table is filed, because none is warranted** — forcing one would be the "decorated mood" the Friction Rule exists to catch, in its purest form. Any resonance between the song's protest/"be heard" theme and the house's concerns is filed at `[POETIC]`/`[A]` and carries **no evidential weight** (§5).

## §1 Rail report

| rung | rail | result |
|---|---|---|
| 1 | `youtube-transcript-api` (instance `.list()`) | **DEAD — `TranscriptsDisabled`** ("Subtitles are disabled for this video"). Not a throttle: the video genuinely has no caption track. |
| 2 | `yt-dlp --list-subs` / `--write-auto-subs` | **DEAD — "has no automatic captions" / "has no subtitles"** ("There are no subtitles for the requested languages"). Both confirmed in the same pull. |
| 3 | CDP panel (port 9333) | **NOT exercised** — nothing to expand; rung 0 won. |
| 4 | local ASR (whisper) | **NOT exercised** — rung 0 won (no reason to spend ~35 s of ASR for a rail that would only recover the same sung audio). |
| **0** | **Gemini-direct URL ingest (`yt_gemini_ingest.py`, `gemini-3.8-flash`)** | **WON.** ONE call, `finish=STOP`, 18,757 video tokens → 2,006 chars. **MODEL-READ: faithful-in-substance, NOT verbatim.** |

**Evidence class declared:** every quotation in §3 is a **rung-0 model-read** — the model's reading of the media, not the audio's own cue text. Per the house ladder, a rung-0 quote may **not** be presented as verbatim and must be marked *reconstruction*. This is stated at the point of use below.

## §2 Source identity (verified)

Title, channel, duration (206 s), upload date (2021-03-23) and view/like counts were read from `yt-dlp --print` and `youtube.com/oembed` at pull time — i.e. the identity is a measurement, not a guess. `[EST]`

## §3 What the video actually contains

Per the rung-0 read (`[HYP]` — model-read; the negative findings are what the model reported as absent, consistent with the title and the music-channel format):

- A **single sung song**, start to finish, performed live. `[EST]` (title + read agree)
- **No interview, no host, no dialogue, no spoken intro/dedication/outro, no narrator, no live audience or applause.** `[HYP]`
- **No clips or montage from *The Trial of the Chicago 7***; **no on-screen lyrics, title cards, lower-thirds, or end credits.** `[HYP]`
- Staging (rung-0 read): Union Chapel interior; grand piano; Celeste walks the aisle to a stand mic; a small string ensemble (violins, double bass) appears in the chapel alcoves; venue empty of audience. `[HYP]`

**No interview content was invented or inferred.** If an interview existed it would be recorded here; it does not.

## §4 The lyrics — rung-0 MODEL-READ (reconstruction, NOT verbatim)

`[POETIC]` · **Evidence class: reconstruction.** These lines are the model's reading of the sung audio; they are **not citable as verbatim** and are not a substitute for the published lyric sheet. The built-in "VERBATIM QUOTES" block of the extraction is reproduced as the model-read's own section; treat its word "verbatim" as *the model's claim*, not a verified match to the tape.

Cross-check against published lyrics (independent secondary sources — Genius, Shazam, the official-video description `pnY9_DXMBis`, Dork/LRCLIB): the model-read agrees **in substance and near-completely in wording**, with these deltas on tape-worth noting:

- read has **"Hear my cry"** where the published sheet reads **"Hear my cries"** `[EST-delta]`
- read has **"Still I'll raise this hand"** where the published sheet reads **"Still I raise this hand"** `[EST-delta]`
- the published chorus folds the repeated *"world, world"* that the read drops `[EST-delta]`

So the block is **substance-accurate and wording-approximate**; do not quote it as the lyric sheet.

```
Hear my voice / Hear my dreams / Let us make a world / In which I believe
Hear my words / Hear my cry / Let me see a change / Through these eyes
You may think I won't be heard / Still I'll raise this hand / Spread this word
These words of fire / Of hope and desire / And I'll let them free
Hear my voice
[Vocalizing]
Hear my dreams / Let us make a world / In which we believe / In which we believe
Hear my words / Hear my choice / Hear my voice
```

## §5 Provenance of the song and this performance (external, grounded)

`[EST]` (multiple independent secondary sources; not from the rung-0 read):

- **Songwrights:** "Hear My Voice" was **co-written by Celeste (Celeste Epiphany Waite) and composer Daniel Pemberton**. (Apple Music credits, Shazam, Universal Music Canada press release.) `[EST]`
- **Film:** it is the **focus/end-title song of *The Trial of the Chicago 7*** (Netflix, written/directed by Aaron Sorkin, 2020) — a dramatisation of the 1969 trial of anti-Vietnam-War protesters charged after the 1968 Democratic National Convention. (Universal Music Canada; Netflix Tudum.) `[EST]`
- **Release:** single released **2020-10-08** on Polydor/Universal Music Canada. (Universal Music Canada.) `[EST]`
- **This performance:** the **Union Chapel, London** arrangement — voice, piano, strings — was **showcased by Netflix Playlist** ~December 2020 (Billboard: "the performance, showcased by Netflix Playlist, features [Celeste] powerfully singing in London's Union Chapel, accompanied by a piano and string arrangement"); Billboard dates the segment to a Monday, 7 December). This YouTube upload is Celeste's own channel posting the same performance, 2021-03-23. `[EST]`
- **Award status:** the song was **nominated for the 2021 Academy Award for Best Original Song** (Netflix Tudum). `[EST]`

Nothing in this section is sourced from the tape; the tape supplies only the performance itself.

## §6 Assessment

**What this source can support:** `[EST]` the *contents of the video* — a live solo performance of a specific song at Union Chapel, the song's identity, its authorship and its film provenance. **What it cannot support:** any proposition about AI, consciousness, alignment, or the ledger — the video makes **no such claims**, and every house-facing register below is `[POETIC]`/`[A]` at most.

- The song is a **first-person plea to be heard** ("Hear my voice / Hear my dreams … Let me see a change through these eyes"). `[POETIC]` Its co-writer frames the film's theme as *"Why do people protest? Because they're not being heard"* (Variety). `[EST]` (Pemberton's stated intent) — but this is the **songwriters' framing of a film**, not evidence about anything the house measures.
- A resonance with the house's interest in **voices that are structurally unheard** is available — **but only as an analogy** `[A]`, and a weak one: a ballad is not an instrument, and a listen-request is not a measurement of whether anyone listened. Filed so the register is visible, **not** as a joint.
- **No EILT mapping table is filed.** There is no claim here whose falsifier could be written; a table would manufacture friction and convergence alike. The honest artifact is this note.

**Falsifiers (all source-facing; none house-facing — a house-facing falsifier would require a house claim, and none is made):**
- **F-CEL-1:** if the rung-0 lyrics diverge from the published lyric sheet in a **load-bearing** way beyond the three deltas named in §4, the §4 block is mislabeled — re-pull the lyric sheet and correct §4.
- **F-CEL-2:** if a caption track later exists on `mrmLIEl9pvQ` (manual or auto), rung 0's "no spoken word" finding is testable directly and should be re-run against rung 1; this drop then upgrades with **no** change to its substance expected.

## §7 Receipt

Written to disk this pass: this drop; the saved artifact `YT_TRANSCRIPTS/mrmLIEl9pvQ_hear_my_voice_union_chapel_2026-11-16.txt`; the raw rung-0 output `YT_TRANSCRIPTS/mrmLIEl9pvQ_hear_my_voice_union_chapel_2026-11-16_structured.md`; and one appended `CANON_INDEX.md` row. **Local only** — no GitHub push, no NotebookLM ingest, no rclone/Drive mirror, no TTS, no outbound send. Dedupe: id = 0 hits pre-pull, pre-write, post-write. No pre-existing Canon artifact modified.

**Citable for:** the video's own contents (a solo live performance of "Hear My Voice" at Union Chapel), the song's identity/authorship/film provenance, and the fact that the source contains no interview and no spoken word. **NOT citable for:** any verbatim lyric wording (rung-0 reconstruction — use the published sheet), or any claim about AI/consciousness/alignment/the house (the source makes none).
