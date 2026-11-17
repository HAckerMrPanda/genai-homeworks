# Audio Acceptance • Homework L06
**Student:** Kodirjon Khayitov  `kodirjon_khayitov@student.itpu.uz` 
**Date:** 2026-11-14  
**Reviewer:** `ihar_rubanovich@epam.com` • **Track:** B • **File checked:** `final_voiced.mp4` / `audio/mix.wav` (15.6 s)  
Timecodes are in the final video. Durations and levels were measured with ffmpeg (`silencedetect`, `volumedetect`, `ebur128`).

| # | Checklist item | Result | Evidence | Timecode | Cause |
|:-|:---|:-:|:---|:-:|:---|
| 1 | **Words** match the script: speech-to-text + critical terms | ✓ | `transcript.txt`: two raw runs, and all 6 critical terms recognised in both (table below). Word error rate = 0 / 19 after writing numbers the same way. Punctuation differences: no comma after "Timur" in either run, and no colon after "Route" in run 1. | 00:10.1–00:12.3 (no comma) | The missing comma is the **voice**: B's line 3 has no pause after "Timur," (no silence > 50 ms). The missing colon and the digits-vs-words difference are **speech-to-text format** (the same file gave different formats in two runs). |
| 2 | **Pronunciation** of names, numbers, terms (by ear) | ✓ | By ear (student): all lines clear. "Four-seventeen" is read as "four seventeen", not "four hundred seventeen" (run 1 writes it in words). "Six forty-two" is read as a time. "Timur", "Park Street", "Elm Avenue" and "one minute" are recognised in both runs. | 00:00.6–00:03.2 (417, 6:42), 00:05.6–00:07.4 (streets), 00:10.1–00:12.3 (Timur) | — |
| 3 | **Timing**: each line fits its shot, not cut by a transition | ✓ | Speech spans 00:00.60–00:03.15, 00:05.60–00:07.38 and 00:10.10–00:12.29, all inside the windows in `script.md` (0.6–3.7, 5.6–8.6, 10.1–13.1 s). Every line starts after the crossfades (4.59–5.09, 9.11–9.61) and ends before the next one. Words / max: 7/7.75, 6/7.5, 6/7.5. | — | Voice A would have failed here: line 1 is 3.62 s against a 3.1 s window (**voice**: 0.56 s pause after "Order 417,"). |
| 4 | **Mix**: voice clear, background ducked, no stray speech (first and last 3 s) | partly | Mean level during speech: −18.4 dB (line 1), −17.7 dB (line 2), −14.0 dB (line 3). Bed level: cafe −40 dB, street −23 dB under the voice / −24 dB between lines, hallway −46 dB. First 3 s: line 1 over a quiet cafe bed, no other speech. Last 3 s (12.6–15.6): hallway tone and fade only. The bed is synthesized and contains no voices, so there is no stray speech. | 00:10.1–00:12.3 | **Voice**: line 3 is ~4 dB louder than lines 1–2. Each Gemini generation came out at a different level, and no per-line level matching was applied before the mix. The street section 00:08.6–00:09.6 (−24 dB between lines) is the busiest part of the bed but stays below speech. |
| 5 | **Loudness** −14 ± 1 LUFS, true peak ≤ −1 dBTP | ✓ | `qa/loudness.png`: Integrated −14.0 LUFS, True Peak −1.7 dBTP, LRA 7.5 LU. Measured on the AAC track of `final_voiced.mp4`; `mix.wav` measures −14.0 / −2.0. | whole file | — (AAC encoding added 0.3 dB of peak, within the −2 dBTP limiter headroom) |
| 6 | **Rights**: voice and music licence, consent, "AI-generated" label | ✓ | Licence table in `audio_spec.md`. Library / prebuilt voices only, no cloning. Background is own work. AI caption burned in at 13.6–15.6 s. | 00:13.6–00:15.6 | Note: ElevenLabs Free has no commercial licence, so voice A is fine for homework but not for publication. Voice B was the one kept. |

### Critical terms
| Term | Heard as (transcript.txt) | Correct? | After listening: voice error or speech-to-text format? |
|---|---|:-:|---|
| 417 | run 1 "four seventeen"; run 2 "417" | ✓ | Speech-to-text format only. The voice said "four seventeen" as written in the spoken text; one run wrote words, the other digits. |
| 6:42 | run 1 "six forty-two"; run 2 "6:42" | ✓ | Speech-to-text format only; read as a clock time in both. |
| Park Street | "Park Street" (both) | ✓ | — |
| Elm Avenue | "Elm Avenue" (both) | ✓ | — ("Elm" was a risk for "Helm"/"Alm"; not confused) |
| Timur | "Timur" (both), but "Courier Timur arriving" without a comma | ✓ | The name is correct. The missing comma comes from the **voice** (no pause after "Timur,"), not the transcriber. |
| 1 minute | run 1 "one minute"; run 2 "1 minute" | ✓ | Speech-to-text format only. |

### Service A vs service B
On **words (item 1)** both voices produced clear speech. The difference is in how they handle text. ElevenLabs (A) was given digits and silently chose the number readings itself. Gemini TTS (B) read **everything in the text field**: its first attempts spoke the style instruction aloud (10.6 s and 9.5 s files), a "voice" error caused by where the instruction was placed. On **pronunciation and pacing (item 2, with item 3)**, A is slower and pauses longer at punctuation: 0.56 s after "Order 417," and 0.48 s after "Route:". That made line 1 too long for its window. B is faster, fits every window, and even drops the pause after "Timur,". B was kept, which also cost ~58× less at list price.

### Conclusion
No critical term was lost. Every mismatch in the transcripts is either a speech-to-text **format** choice (digits vs words, which changes between two runs of the same file) or **prosody** (a missing comma pause). That is why critical terms must be checked by ear, not by string comparison. I would fix the following:
- **Per-line level:** normalise each TTS line (or apply a gentle compressor) before mixing, so line 3 is not ~4 dB louder than lines 1–2.
- **Prosody:** write "Courier Timur… arriving in one minute" (or add a full stop) in B's spoken text to force the pause.
- **Instructions:** always put the style instruction in the model's style or system field, never in the text that will be spoken.
- **Voice A:** paste the spoken text, not the digits, and shorten line 1 ("Order four-seventeen, picked up six forty-two") to fit 3.1 s.
- **Background:** with a working sound-effects quota, replace the synthetic bed with a real ambience. A cafe without murmur and a street of filtered noise sound thin compared with recorded or generated effects.
