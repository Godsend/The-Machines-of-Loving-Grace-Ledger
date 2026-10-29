# BLOCKED — Members-only gate. No transcript obtained.

**Status: BLOCKED. Zero transcript coverage. No drop filed; no content synthesized.**

- Video id: `QhWzn95-XE4`
- URL: https://www.youtube.com/watch?v=QhWzn95-XE4
- Title (verbatim from the live page): *Why Mirror Life Doesn't Exist: Chemistry & the 2026 Nobel Award*
- Channel: **Anton Petrov** — channelId `UCciQ8wFcVoIIMi-lfu8-cjQ`
- Published (microformat publishDate/uploadDate): **2026-10-26T01:06:44-07:00** (= 2026-10-26T08:06:44Z)
- Duration: **930 s** (15:30) | Category: Science & Technology
- Observed page badge: **"Members first"**; the playability screen item is titled "Members-only content" (`offerId: sponsors_only_video`)
- Intake run: **2026-10-26** (~20:42 UTC), host Nitro, yt-dlp 2026.08.19, Chrome/145.0.7632.6

This drop file is a **declared non-drop**. It records rails tried, exact errors, and what a human must do. Nothing below is presented as transcript content, because **no transcript, caption track, or audio byte was obtained.**

---

## 1. Why this was expected to work, and why the premise failed

The parent's working assumption was that the video "sits inside the user's own Unlisted playlist, therefore the user's account has access, therefore this is a login wall and not an availability problem."

**That inference is not borne out.** A YouTube playlist entry does not confer members-only entitlement. The definitive test was run inside the already-logged-in browser: the page renders the members-only interlock, not a player, and the authenticated player endpoint returns `UNPLAYABLE`. The account shown on that page (from the membership upsell panel) is **"Machine of Loving Grace: Gene Yanenko"**, and YouTube is offering it a *join* flow — PLANETARY $4.99/month (first-month promo applied), STELLAR $9.99/month, GALACTIC $99.99/month. **The logged-in account is not currently a member of this channel**, so there is no session cookie that unlocks this video.

---

## 2. Rails attempted, with the exact error returned by each

### Rail 1 — yt-dlp with the local logged-in browser cookie jar (FAILED)

```
yt-dlp --cookies-from-browser 'chromium:/home/godsend/.hermes/profiles/dion/cache/chrome-live' \
  --skip-download --print '%(channel)s|%(duration)s|%(upload_date)s|%(title)s' \
  'https://www.youtube.com/watch?v=QhWzn95-XE4'
```
Exact output:
```
ERROR: secretstorage not available as the `secretstorage` module is not installed. Please install by running `python3 -m pip install secretstorage`
WARNING: failed to decrypt cookie (AES-CBC) because UTF-8 decoding failed. Possibly the key is wrong?
ERROR: [youtube] QhWzn95-XE4: Join this channel to get access to members-only content like this video, and other exclusive perks.
```
The browser-cookie path could not decrypt the Chromium cookie DB, so yt-dlp fell back to anonymous and hit the wall. The recommended fix (`python3 -m pip install secretstorage`) also failed in this environment:
```
.../venv/bin/python3: No module named pip
```
Writing that failure down exactly, as instructed.

### Rail 1b — cookies extracted live from the running session via CDP (FAILED, and this is the load-bearing negative)

To rule out the decryption problem, the cookie jar was pulled straight out of the live, logged-in browser over CDP (`Network.getAllCookies` on the port-9333 session): **214 cookies returned, 27 of them `youtube.com`-scoped**, including the auth set `SID`, `HSID`, `SSID`, `APISID`, `SAPISID`, `LOGIN_INFO`, `__Secure-1PSID`, `__Secure-3PSID`, `__Secure-1PAPISID`, `__Secure-3PAPISID`. These were written to a Netscape `cookies.txt` and fed to yt-dlp:
```
yt-dlp --cookies cookies.txt --skip-download --print '%(title)s|%(duration)s' 'https://www.youtube.com/watch?v=QhWzn95-XE4'
ERROR: [youtube] QhWzn95-XE4: Join this channel to get access to members-only content like this video, and other exclusive perks.
```
**A fully authenticated, undecrypted cookie set returns the same wall.** This eliminates "cookie plumbing" as the cause. Re-tried across player clients, all identical:
- `player_client=tv` → same members-only error
- `player_client=web_safari` → same
- `player_client=mweb` → same
- `player_client=web_embedded` → same
- `player_client=android` → `WARNING: [youtube] Skipping client "android" since it does not support cookies`, then same error
- `player_client=ios` → `WARNING: [youtube] Skipping client "ios" since it does not support cookies`, then same error
- `player_client=tv_embedded` → `WARNING: [youtube] Skipping unsupported client "tv_embedded"`, then same error

### Rail 2 — yt-dlp subtitle and audio grab with cookies (FAILED)

```
yt-dlp --cookies cookies.txt --skip-download --write-auto-sub --write-sub --sub-langs 'en.*,en' ... → ERROR: [youtube] QhWzn95-XE4: Join this channel to get access to members-only content like this video, and other exclusive perks.
yt-dlp --cookies cookies.txt -f 'bestaudio/best' --no-download ...                      → ERROR: [youtube] QhWzn95-XE4: Join this channel to get access to members-only content like this video, and other exclusive perks.
```
No format list and no caption track is exposed on a locked video, so there was nothing to write a subtitle file from.

### Rail 3 — CDP against the live logged-in Chromium on port 9333 (FAILED — gate not lifted)

Chrome/145.0.7632.6 was confirmed answering on `http://127.0.0.1:9333/json/version`. A tab was navigated to the watch URL and driven over CDP. Findings:

- `document.title` = "Why Mirror Life Doesn't Exist: Chemistry & the 2026 Nobel Award - YouTube" — the page loads, so this is an entitlement wall, not a 404 or geo-block.
- The rendered body reads: `Members-only content` / `Join this channel to get access to members-only content like this video, and other exclusive perks.` — and, critically, a **membership signup panel**, not a player.
- `document.querySelector('video')` exists but `readyState = 0`, `duration = null` — nothing plays.
- The "Show transcript" control is **absent** (`hasTranscriptBtn: false`), and the chapter macro-markers list is empty. The transcript-panel extraction described in the `youtube-content` skill had no panel to open.
- `window.ytInitialPlayerResponse.playabilityStatus` = `{"status":"UNPLAYABLE","reason":"Join this channel to get access to members-only content like this video, and other exclusive perks.","errorScreen":{"playerLegacyDesktopYpcOfferRenderer":{"offerId":"sponsors_only_video"}}}`. `captions` is `"NONE"`. `streamingData` is **absent**.
- In-page authenticated fetch (carries the session cookies) to `/youtubei/v1/player`:
  `{"status":"UNPLAYABLE","reason":"Join this channel...","hasStreaming":false,"hasCaptions":false}`
- In-page authenticated fetch to `/api/timedtext?type=list&v=QhWzn95-XE4`: **HTTP 200, body length 0** (no caption tracks advertised at all).
- In-page authenticated fetch to `/youtubei/v1/get_transcript`: **HTTP 400**.
- Re-checked at the end of the run: still `UNPLAYABLE`.

CDP was not unstable — it worked cleanly. It simply confirmed, from inside the authenticated session, that the entitlement is missing.

### Rail 4 — yt-dlp bestaudio + local faster-whisper small.en (NOT RUNNABLE)

Cannot be attempted: Rail 2 could not produce an audio stream, so there is no input for ASR. Recording this as **not attempted because unreachable**, not as a failure with an error string, so the record stays accurate.

### Out-of-band extra rails, also negative

- **Wayback Machine** `archive.org/wayback/available?url=youtube.com/watch%3Fv%3DQhWzn95-XE4` → `"archived_snapshots": {}` — no snapshot exists (the video is hours old).
- **Channel recent-uploads scan** (top 40 via `.../channel/UCciQ8wFcVoIIMi-lfu8-cjQ/videos`) and the **channel RSS feed** → the members-first item `QhWzn95-XE4` does **not** appear in the public feed, and **no public upload on the same topic** exists in the recent window. There is no public duplicate of this video on the channel to fall back to.
- **Whole-YouTube title search** (`ytsearch6:Why Mirror Life Doesn't Exist`) surfaced only unrelated items. The nearest hit, `b2Fg9IfjkCI` "Mirror Life: The Hidden Biology We Might Be Missing" (channel *AI Labs: Exploratory Science and Paradoxes*), is a **different, older video** — uploaded **2025-05-17**, 685 s, 224 views — not a mirror of this one and not a substitute source for it. **Not filed, not used.**

---

## 3. Page metadata that WAS read (verbatim, from the live page) — metadata only, not transcript

The locked page still exposes the full video description and chapter list. This is quoted verbatim from `ytInitialPlayerResponse.microformat.playerMicroformatRenderer.description` as read this session. **It is metadata. It is not transcript and must never be cited as something Anton Petrov said in the video.**

Description body (after the standard Patreon/PayPal/"Wonderful Person Tee" preamble and before the camera-affiliate list):

```
Hello and welcome! My name is Anton and in this video, we will talk about the nobel prize in chemistry (2026) and the mirror life
Links:
https://royalsocietypublishing.org/rsos/article/13/10/260921/483780/Circularly-polarized-luminescence-as-a-contingency
https://pmc.ncbi.nlm.nih.gov/articles/PMC13474939/pdf/ja6c03792.pdf
https://royalsocietypublishing.org/rsos/article/13/10/260921/483780/Circularly-polarized-luminescence-as-a-contingency
https://chemrxiv.org/doi/full/10.26434/chemrxiv.10001955/v6
https://www.nobelprize.org/prizes/chemistry/2026/summary/
#nobel #chemistry #mirrorlife
```

Chapter list (verbatim, from the description — these are the uploader's own written chapters, not machine-extracted):

```
0:00  2026 Nobel Prize in Chemistry - chirality and mirror molecules
2:00  Chirality and mirrors in DNA and proteins
3:30  Why no mirror life? Kagan and Soai
6:10  Manufacturing mirror proteins
6:50  Membranes don't like mirror molecules
7:50  Existential biohazard
10:30 How can we detect this mirror life?
12:35 Conclusions and implications
```

Two observations worth recording: the Royal Society Open Science link is **listed twice** (a copy-paste duplicate by the uploader), and the chapter headings show the video has a segment on biosafety ("Existential biohazard") and on detection/monitoring of mirror life — i.e. the *topic* touches governance/biosafety, but **no spoken claim about it can be quoted or characterized from this run.**

---

## 4. Citation verification — done on the description's links, NOT on the video's content

Because the description itself hands over primary sources, those links were checked directly (this is the only content-adjacent verification possible this session). Results:

- [EST] **https://www.nobelprize.org/prizes/chemistry/2026/summary/** — HTTP 200, page title "Nobel Prize in Chemistry 2026 - NobelPrize.org". It states the prize was awarded **jointly to Henri B. Kagan and Kenso Soai**, "for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis", 1/2 share each. This is a **real, checkable news peg** and it lines up with the video's chapter 3:30 "Kagan and Soai".
- [EST] **Royal Society Open Science article** — the direct URL returns **403 with a Cloudflare "Just a moment..." interstitial** (bot wall, not a missing page). Resolved instead through the Crossref API: **DOI `10.1098/rsos.260921`**, title *"Circularly polarized luminescence as a contingency assay for 'mirror life' bio-hazards"*, journal **Royal Society Open Science**, published **2026-10-07**, authors **Lewis E. MacKenzie, Dominic J. Black, Robert Pal**. Real paper; RSOS is open access.
- [EST] **https://pmc.ncbi.nlm.nih.gov/articles/PMC13474939/pdf/ja6c03792.pdf** — HTTP 200. The article is *"Chemical Synthesis of Mirror-Image Proteins Reveals Chirality-Dependent Cellular Uptake Mediated by a Cell-Penetrating Peptide"*, **J Am Chem Soc** 2026 Jun 17;148(31):33039-33048, **doi 10.1021/jacs.6c03792**; authors **Eman Nassar, Ashok Donthoju** (Schulich Faculty of Chemistry, Technion-Israel Institute of Technology, Haifa). Real paper; matches the video's 6:10 "Manufacturing mirror proteins" chapter.
- [UNVERIFIED — DOES NOT RESOLVE] **https://chemrxiv.org/doi/full/10.26434/chemrxiv.10001955/v6** — `doi.org` resolution returns **404**, and Crossref returns "Resource not found" for that DOI. The DOI string also does not match the usual ChemRxiv pattern. **Flagged, not trusted.** Do not repeat this link as a working citation until someone resolves it.
- **House trap checked:** the instruction warns that a ScienceDaily/press-release *repost* date is routinely mistaken for the real journal date. Here the JACS paper carries its **own** publication date (2026 Jun 17) and the RSOS paper its own (2026 Oct 7) — neither is a press-release date, so no confusion arises. But note the ordering: the JACS mirror-protein paper (June 2026) **predates** the Nobel announcement, i.e. the video's "2026 Nobel" framing is about a prize awarded for earlier work, not about the JACS paper itself.

---

## 5. EILT mapping: deliberately none

No friction-rule mapping table is supplied, and that is the correct outcome rather than an omission. A mapping between a source and EILT requires source text; there is no source text here. Any table that mapped this video's *chapters and title* — or Anton Petrov's known/reputed positions — onto EILT vocabulary (ledger, provenance, substrate, commit) would be **fabricated evidence dressed as analysis**: exactly the confirmation-bias failure the friction rule exists to prevent. The house vocabulary-drift check cannot be run against this source either, for the same reason. If the video is later unlocked and transcribed, a mapping with genuine divergence rows can be produced then; until then, this file asserts no convergence and no divergence.

---

## 6. What a human needs to do to unblock it

Ranked by cost:

1. **Cheapest — wait, then re-check.** The page carries a **"Members first"** badge, [HYP] suggesting early access for members that later becomes public, and this channel publishes public uploads on a daily cadence around **22:00 UTC**. The video was uploaded 2026-10-26T08:06Z and this run was at 2026-10-26T20:42Z. **Re-check the watch URL after ~2026-10-26T22:00Z and again the following day**; if it has flipped to public, re-run Rail 1b (or Rail 3) and the normal `youtube-content` pipeline will apply. This is the most likely resolution and needs no payment.
2. **If an account already has access** — export that member account's cookies to a Netscape file and re-run:
   `yt-dlp --cookies cookies.txt --skip-download --print '%(title)s|%(duration)s' 'https://www.youtube.com/watch?v=QhWzn95-XE4'`
   If that returns metadata instead of the members-only error, proceed to the subtitle/audio rails and, failing those, to the CDP transcript-panel path documented in the `youtube-content` skill. No script changes are needed; the method is proven on this host.
3. **Pay to unblock** — join the channel membership (PLANETARY, $4.99/month, first month promo $0.00 as shown on the page), then do (2). **This run did not do this**: it is a money-spending side effect and was not authorized. It should be a deliberate human decision, not an agent's.
4. **Repair the cookie-decryption path (only needed for Rail 1a).** Install `secretstorage` into a Python that has pip, or point yt-dlp at a `cookies.txt` exported from a normal browser profile. Note this only fixes the *plumbing*; it does **not** grant entitlement, so it will not unlock this video while (1) is pending.
5. **Read the primary sources instead.** The RSOS paper (`10.1098/rsos.260921`, open access) and the JACS paper (`10.1021/jacs.6c03792`) are both real and independently addressable. If what the house actually wants is the *content* of the mirror-life / 2026-Nobel story rather than this specific video, those two papers are reachable **today** without anyone joining a channel. That is a different intake, not a substitute transcript for this file.

**Do not** treat this file as containing any claim made in the video. It does not.

---

## Falsifiers

- **F-ML1** — the watch URL begins returning `playabilityStatus: PLAYABLE` (no membership needed): the block is a time-limited members-first window, not a permanent gate. Test: re-run the CDP `youtubei/v1/player` probe.
- **F-ML2** — the logged-in account turns out to hold a membership (page shows perks instead of a join offer): Rail 1b should then have worked, and the same cookie jar must yield a real format list. Test: re-run Rail 1b.
- **F-ML3** — DOI `10.26434/chemrxiv.10001955/v6` resolves to a real preprint: the [UNVERIFIED] tag on that link is wrong and should be struck.
- **F-ML4** — the public release ships a manual or auto caption track: the "no caption track" observation was an artifact of the lock, not a property of the video.

**Verdict.** Strongest point: the citation trail is genuine and the news peg verifies — the 2026 Nobel Prize in Chemistry (Kagan & Soai) is real, and both journal papers check out, so this video is worth a real intake once reachable. Weakest joint: transcript coverage is **zero** — the entire content layer sits behind a members-only entitlement that neither the browser's own logged-in session nor any client variant could cross, so nothing in this file can speak to what the video actually argues.

No existing drop file was modified. No content was invented. No EILT mapping was forced.
