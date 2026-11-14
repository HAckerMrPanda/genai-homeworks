# Audio Specification • Homework L06

**Student:** Kodirjon Khayitov  `kodirjon_khayitov@student.itpu.uz` 
**Reviewer:** `ihar_rubanovich@epam.com`  **Track:** B (courier, Glovo case)  
**Video:** L05 `final.mp4` (15.6 s, no original sound) → `final_voiced.mp4`  
**Date:** 2026-11-14

## 1. Voice
| | Service | Model | Voice name | Settings / style instruction | Attempts per line |
|---|---|---|---|---|---|
| A | ElevenLabs (web, Free plan) | ElevenLabs v4 (`elevenlabs-v4`, from the file names) | "Mask" (library voice; per the student, not modelled on a real person) | default settings, no style tags. **Input text was the viewer script with digits** ("Order 417, picked up at 6:42."), not the spoken text, so the voice decided how to read the numbers | 1 / 1 / 1 |
| B | Google AI Studio, Generate speech (Free) | Gemini 3.8 Flash TTS (`gemini-3.8-flash-tts`) | template "The Everyday Assistant" ("helpful and professional"); prebuilt voice name [fill in from Run settings] | spoken text only. Attempt 1 had the style instruction ("Read in a calm, friendly dispatcher voice…") at the start of the text field, and the model **read it aloud**. Attempt 2 used the spoken text alone | 2 / 2 / 1 |

Rejected attempts are kept in `audio/rejected/` as evidence: line 1 attempt 1 is 10.6 s and line 2 attempt 1 is 9.5 s, both with the instruction spoken aloud.

**Kept: B.** By checklist item 1, speech-to-text matched every critical term. By the timing rule, all three B lines fit their speech windows (2.55 / 1.78 / 2.19 s against 3.1 / 3.0 / 3.0 s). Voice A line 1 runs 3.62 s, 0.5 s over its 3.1 s window, because of a 0.56 s pause after "Order 417,".

## 2. Background and licences
| Track | Source (service / video model / library) | Licence | Commercial use? | Attribution needed? |
|---|---|---|---|---|
| Voice A (compared, not in the final mix) | ElevenLabs Free plan, ElevenLabs v4, library voice | ElevenLabs Terms, Free plan: **no commercial licence** | No (Free plan) | Check the ElevenLabs Free-plan terms before publishing |
| Voice B (in the final mix) | Google AI Studio, Gemini 3.8 Flash TTS, prebuilt voice | Gemini API / Google AI Studio terms | Per Google's Gemini API terms; verify before commercial release | Not required by the tool; the AI label is added anyway |
| Background `bed.mp3` | Synthesized in ffmpeg (filtered pink and brown noise, sine "clinks" and a two-tone bicycle bell). No AI, no samples | Own work | Yes | No |
| Video (picture) | L05: Dreamina (Seedance 2.0 Mini / 1.0 Fast), free plan, visible watermark | Dreamina terms, free plan | Not verified for commercial use | — |

The plan was ElevenLabs Sound Effects for the background (prompt: *"Continuous city ambience… No voices, no speech, no music."*). Three attempts returned "Free generations are busy right now… nothing was charged", so the bed was synthesized instead.

**Consent:** no voice cloning. Only library or prebuilt voices were used, and no real person's or brand's voice or jingle was imitated.

## 3. Mix
- **Tool and steps:** ffmpeg (no Audacity).
  1. Voice B lines placed so speech starts at 0.60 s, 5.60 s and 10.10 s (`adelay` 330 / 5345 / 9774 ms, after trimming each file's leading silence). Each start is after the preceding crossfade has ended (crossfades at 4.59–5.09 s and 9.11–9.61 s).
  2. Bed at −2 dB, ducked under the voice with `sidechaincompress` (threshold 0.015, ratio 10, attack 15 ms, release 350 ms).
  3. Voice + ducked bed summed (`amix`, no auto-normalisation), then two-pass `loudnorm` I = −14 LUFS, TP = −2 dBTP, linear mode → `audio/mix.wav` (48 kHz, 24-bit, stereo).
  4. `mix.wav` muxed onto L05 `final.mp4` as AAC 192 kbps, picture re-encoded with the AI caption → `final_voiced.mp4`.
- **Result** (ffmpeg `ebur128`, measured on the AAC soundtrack of `final_voiced.mp4`): **Integrated −14.0 LUFS, True Peak −1.7 dBTP, LRA 7.5 LU** (screenshot `qa/loudness.png`). `mix.wav` before encoding: −14.0 LUFS, −2.0 dBTP. AAC encoding raised the peak by 0.3 dB, inside the 1 dB of headroom.
- **AI label:** burned-in caption, 13.6–15.6 s (over the final freeze and fade), two lines:
  - "Voice: AI-generated (Google AI Studio, Gemini 3.8 Flash TTS)"
  - "Background: synthesized with ffmpeg (no AI)"

  The assignment's wording is "Voice and music: AI-generated (…)". "Music" was replaced because the background is neither music nor AI-generated.

## 4. Cost
List prices:
- ElevenLabs Starter is $6/month for 30,000 credits, so $0.0002 per credit.
- Gemini 3.8 Flash TTS is $9.00 per 1M audio output tokens, at 25 tokens per second of audio (Gemini API price through 31 Dec 2026). Text input ($0.50 / 1M) is negligible here.

| Item | Unit | Quantity × attempts | List price | Cost at list price | Actually paid |
|---|---|---|---|---|---|
| Voice A (ElevenLabs v4) | credits | 1,844 credits for 3 lines (~100 characters), 1 attempt each | $0.0002 / credit (Starter) | $0.37 | $0 (Free plan) |
| Voice B (Gemini 3.8 Flash TTS) | seconds of audio → audio tokens | 28.4 s generated over 5 attempts (10.6 + 9.5 + 3.1 + 2.4 + 2.9 s) ≈ 711 tokens | $9.00 / 1M audio tokens | $0.0064 | $0 (AI Studio) |
| Background | track | ffmpeg synthesis (3 failed ElevenLabs Sound Effects attempts, 0 charged) | — | $0 | $0 |
| Speech-to-text | input tokens | 437 tokens × 2 runs (Gemini 4 Hydrogen, AI Studio) | not looked up | < $0.01 | $0 (AI Studio) |
| **Total** | | | | **≈ $0.38** | **$0** |

**Observation:** ElevenLabs charged **1,844 credits for ~100 characters**, about 18 credits per character. The rate for its standard models is ~1 credit per character. The newest model (v4) is far more expensive per character, so the same three lines cost ~58× more than with Gemini TTS. A 3-line test used ~18% of the 10,000-credit monthly free allowance.
