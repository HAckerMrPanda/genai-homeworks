# Video Specification • Homework L05

**Student:** Kodirjon Khayitov  `kodirjon_khayitov@student.itpu.uz` 
**Reviewer:** `ihar_rubanovich@epam.com`   
**Track:** B: courier  
**Service 1:** Dreamina (CapCut / ByteDance), Seedance models — shots 1–3  
**Service 2:** Qwen Chat (chat.qwen.ai), "Create Video" — shot 2 repeated  
**Text-to-video baseline:** Kling (kling.ai), Kling 4.0  
**Date:** 2026-11-14 • all clips generated on free accounts

---

## 0. Text-to-video baseline (00_t2v_baseline.mp4)
- **Service / model:** Kling, Kling 4.0 (model name from the on-video watermark "KlingAI 4.0"); free account, default settings
- **Prompt (whole story):**
  ```text
  A male food delivery courier with a short black beard, round glasses, an orange windbreaker and a navy-blue thermal backpack picks up a brown paper bag from a barista at a cafe counter, then rides a red bicycle across a busy city crosswalk, then hands the bag to a customer at an apartment door in a warm hallway. Realistic video, 16:9.
  ```
- **Duration:** 5.04 s, 1280×720, 24 fps, with generated audio. 1 attempt, 50 credits.
- **What broke (with timecodes):**
  - 00:00.0–00:01.4 cafe, 00:01.5–00:03.4 ride (with an extra unrequested cut at 00:02.5), 00:03.5–00:05.0 door: 3 scenes and 5 actions squeezed into 5 s, ~1.5 s per scene.
  - 00:01.4 action skipped: at the cut the bag is still in the barista's hand, the courier never takes it.
  - 00:01.5 the bag teleports into the bicycle's front basket; 00:03.5 it is back in his hand.
  - 00:00–00:05 invented logo: a white heart symbol on the jacket chest and the backpack (brand-like mark, not requested).
  - 00:00–00:01.4 unreadable menu boards; 00:01.5–00:03.4 garbled shop signs ("Lambcusinos", "Larbo…").
  - 00:02.5 jump cut inside the ride: camera angle and background change.
  - Identity does not match L04: no reflective sleeve stripes, rectangular glasses, black trousers, hooded jacket, no watch.

## 1–3. Image-to-video shots (shot1.mp4, shot2.mp4, shot3.mp4)

### Shot 1 — pickup
- **Service / model:** Dreamina, Seedance 2.0 Mini
- **Key frame:** `L05/keyframes/09_pickup.png` (4:3; generated in Gemini app with `04_sheet.png` as reference — L04 had no pickup frame; prompt in the appendix)
- **Prompt:**
  ```text
  Medium shot at eye level with a slow gentle dolly in. The courier in the orange windbreaker takes the brown paper bag from the barista's hand, holds it close with both hands and turns slightly toward the exit in one smooth movement. His fingers wrap firmly around the bag, the bag keeps its shape, the barista's hands withdraw out of frame. Warm morning window light from the left, as in the image.
  ```
- **Settings:** image-to-video (first frame), 5 s, output 1280×720 16:9 (the 4:3 key frame was outpainted to 16:9), ~24 fps, audio on (model default), 1 output
- **Attempts:** 1; nothing changed. **Credits:** 0 (Mini was free at the time of generation)

### Shot 2 — ride
- **Service / model:** Dreamina, Seedance 1.0 Fast
- **Key frame:** `L04/images/05_road.png`
- **Prompt:**
  ```text
  Smooth tracking shot alongside the courier, the camera moves left at bicycle speed at the same height. The courier in the orange windbreaker pedals steadily across the crosswalk, both wheels rotating forward, body leaning slightly forward, hands steady on the handlebars. The navy backpack sways slightly; the waiting cars stay in place and blur gently with motion. Bright daylight, as in the image.
  ```
- **Settings:** image-to-video (first frame), 5 s, output 1120×832 (4:3, follows the key frame), ~24 fps, no audio, 1 output
- **Attempts:** 1; nothing changed. **Credits:** 25

### Shot 3 — delivery
- **Service / model:** Dreamina, Seedance 1.0 Fast
- **Key frame:** `L04/images/06_door.png`
- **Prompt:**
  ```text
  Static camera at eye level. The courier in the orange windbreaker hands over the brown paper bag: the customer's hands take it by the handles and slowly pull it out of frame to the left, the courier lets go, smiles and gives a small nod. The bag keeps its shape and the hands do not merge with it. Warm hallway light, as in the image.
  ```
- **Settings:** image-to-video (first frame), 5 s, output 1120×832 (4:3), ~24 fps, no audio, 1 output
- **Attempts:** 1; nothing changed. **Credits:** 25

## 4. Second service (shot2_service2.mp4)
- **Shot:** 2  **Service / model:** Qwen Chat, "Create Video" (the model name is not shown in the interface); free account
- **Key frame and prompt:** same as shot 2 (`05_road.png`, identical prompt)
- **Settings / attempts:** image-to-video, 5.16 s, 1110×830 (~4:3), 24 fps, with audio; 1 attempt, free
- **Why Qwen:** the planned second service, Kling, had too few credits left after the 50-credit baseline (66 free credits per month), so the repeat moved to a free service.

## 5. Editing (final.mp4)
- **Tool:** ffmpeg (xfade filter)
- **Normalisation:** all shots to 1120×832 (4:3, the format of 2 of 3 shots), 24 fps, yuv420p; shot 1 (16:9) letterboxed into 4:3 with a blurred copy of itself as the bars. Audio removed: only shot 1 had a soundtrack, so mixed sound/no-sound would be jarring.
- **Transitions:** two 0.5 s crossfades (join 1 at 00:04.59–00:05.09, join 2 at 00:09.11–00:09.61); 1.5 s freeze of the last frame with a 1 s fade to black at the end
- **Final length:** 15.6 s

## 6. Cost
Cost = attempts × seconds per attempt × price per second. Prices per credit:
- Kling: $1 buys 66 credits → $0.01515 / credit.
- Dreamina: Basic plan $15 / month for 1,575 credits → $0.00952 / credit.
- Qwen Chat: free; no published per-credit price.

All clips were made on free allowances, so the out-of-pocket cost was $0. The table shows what the same credits would cost at the paid rates above.

| Clip | Service / model | Seconds per attempt | Attempts | $/s or credits/s | Cost |
|---|---|---|---|---|---|
| Baseline | Kling 4.0 | 5 | 1 | 10 credits/s × $0.01515 = $0.152/s | 1 × 5 × $0.152 = **$0.76** (50 cr) |
| Shot 1 | Dreamina, Seedance 2.0 Mini | 5 | 1 | 0 credits/s (free model) | **$0.00** (0 cr) |
| Shot 2 | Dreamina, Seedance 1.0 Fast | 5 | 1 | 5 credits/s × $0.00952 = $0.048/s | 1 × 5 × $0.048 = **$0.24** (25 cr) |
| Shot 3 | Dreamina, Seedance 1.0 Fast | 5 | 1 | 5 credits/s × $0.00952 = $0.048/s | 1 × 5 × $0.048 = **$0.24** (25 cr) |
| Shot 2, service 2 | Qwen Chat | 5 | 1 | free | **$0.00** |
| **Total** | | | 5 | | **$1.24** (100 credits); $0 actually paid |

The text-to-video baseline alone cost more than all three image-to-video shots together (Kling 4.0's default high-end settings).

---

### Appendix: key-frame prompt for 09_pickup.png (Gemini app, reference `04_sheet.png`)
```text
Use the attached character sheet as the identity reference. The same courier (same face, short black hair faded on the sides, neatly trimmed short beard, round black-framed glasses, bright orange windbreaker with reflective white stripes on the sleeves, navy-blue square thermal backpack with a reflective silver stripe, black smartwatch on the left wrist) stands at the wooden pickup counter of a small cafe and reaches for a brown paper food bag held out by a barista, whose hands and forearms only are visible. Warm morning window light from the left, eye level, 35mm lens, medium shot. Realistic photography, aspect ratio 4:3. No brand names, no logos, no text.
```
