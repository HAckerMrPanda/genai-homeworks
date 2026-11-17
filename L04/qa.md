# L04 QA

**Student:** Kodirjon Khayitov  `kodirjon_khayitov@student.itpu.uz` 
**Date:** 2026-11-14  
**Reviewer:** `ihar_rubanovich@epam.com`  
**Services:** Gemini app (Nano Banana, "Fast" mode) • ChatGPT (free tier)

## Track: B — courier character

## Traits that must be preserved
1. Short black hair faded on the sides + neatly trimmed short beard
2. Round black-framed glasses
3. Bright orange windbreaker with reflective white stripes on the sleeves
4. Square navy-blue thermal backpack with a reflective silver stripe across the top
5. Dark-green cargo trousers + grey sneakers
6. Black smartwatch on the left wrist

## Per-shot check
| Image | Traits preserved (✓/✗ each) | What drifted | Iterations needed |
|---|---|---|---|
| 01_free.png | — (free-form prompt, no traits specified) | The model invented everything: a different courier, London, crowd, real brand logos (see below) | 1 |
| 02_structured.png / 03_gemini.png | 1 ✓ 2 ✓ 3 ✓ 4 ✓ 5 ✓ 6 ✓ | Rides diagonally instead of straight toward the camera; no motion blur on the wheels; a VW badge and a number plate on a background car despite "no brand names, no text" | 1 |
| 03_chatgpt.png | 1 ✓ 2 ✓ 3 ✓ 4 ✓ 5 ✓ 6 ✓ | Courier left of center rather than in the left third; no motion blur on the wheels; small emblem on the bike frame; blurred number plate | 1 |
| 04_sheet.png | 1 ✓ 2 ✓ 3 ✗ 4 ✓ 5 ✓ 6 ✓ | Sleeve stripes became 1 horizontal + 2 vertical lines instead of 2 horizontal bands; all 4 views otherwise consistent (watch on the left wrist in every view, including the back view) | 1 |
| 05_road.png | 1 ✓ 2 ✓ 3 ✓ 4 ✓ 5 ✓ 6 ✓ | Stripe pattern follows the sheet; background almost sharp (weak motion blur); the model chose a New York-like street on its own (yellow cabs, NY plates); Honda and Toyota badges on cars despite the "no brand names" constraint | 1 |
| 06_door.png | 1 ✓ 2 ✓ 3 ✓ 4 ✓ 5 ✓/— 6 ✓ | Nothing drifted; sneakers are out of frame (cropping), trousers visible | 1 |
| 07_break.png | 1 ✓ 2 ✓ 3 ✓ 4 ✓ 5 ✓ 6 ✓ | Nothing significant; framed as a medium shot rather than a medium close-up | 1 |
| 08_edit.png (edit of 06) | 1 ✓ 2 ✓ 3 ✓ 4 ✓ 5 ✓/— 6 ✓ | Only the bag was replaced with a plain white pizza box, as asked. Face, pose, jacket, backpack, door, hallway, camera and light are unchanged. Small drifts: the box is held upright like a bag (physically implausible for pizza) and a remnant of the bag handle stays between the two hands | 1 |

**Consistency summary:** the courier is recognizable in all 6 character shots (02–08). In scenes 05–08 the sleeve stripes repeat the *sheet* (04), not the first structured shot (02). This shows the attached reference sheet, not the text, drove the identity. The watch stayed on the left wrist in every shot.

## Free-form vs structured
What the model decided on its own in the free-form version (`01_free.png`):
1. **Location:** London, Oxford Street ("OXFORD ST" sign, red double-decker buses, black cabs, Underground sign).
2. **The courier:** a young man in a blue helmet, orange-and-navy jacket, teal backpack, green e-bike, seen from the side.
3. **Time and weather:** overcast daytime after rain, wet road.
4. **Background:** a busy street with a crowd of pedestrians and heavy traffic.
5. **Real brands and text:** Deliveroo logos on the backpack, jacket and bike frame, plus Pret A Manger and Sainsbury's shop signs and "BIKE LANE" road text. These were never requested; the model filled the gap with the most "typical" courier, which is a real trademark (red zone).

The structured prompt (`02`) removed all of this. It produced an empty early-morning street, the exact courier described, no brands on him, and every slot (subject, setting, camera, light, style, must-have details, constraints) visibly applied.

## Two services, one prompt
| Criterion | Service 1: Gemini (03_gemini.png) | Service 2: ChatGPT free (03_chatgpt.png) |
|---|---|---|
| Prompt following | All 6 traits; courier in the left third ✓; rides diagonally instead of toward the camera; no wheel motion blur | All 6 traits; rides straight toward the camera ✓; left of center rather than in the left third; no wheel motion blur |
| Text in image | No text was requested ("no text anywhere"): only a VW badge and a number plate on a background car | No text was requested: only a small emblem on the bike frame and a blurred number plate |
| Product/character preserved | 6/6 traits | 6/6 traits; glasses closer to "round" |
| Aesthetics | Calm, natural colors, true to "documentary street photography" | More cinematic: saturated golden glow, sun in frame, closer to stock/ad photography than documentary |
| Verdict: which one I'd pick for this task and why | **Gemini.** For a character series it followed the documentary style, kept identity from an attached sheet across 3 scenes, and made a pixel-stable "change only X" edit (08) on the first try | Good alternative for a single hero shot where exact composition (toward the camera) matters; free-tier image limits make it less practical for a whole series |

## Edit check (Track B)
`08_edit.png` vs `06_door.png`: **one thing changed** (brown paper bag → plain white pizza box, no print). Everything listed under "keep" stayed: face, glasses, beard, orange jacket, backpack, pose, door, hallway, camera angle and light. The only side effects are the upright box orientation and a small leftover of the bag handle.

## Takeaways
1. **Free-form prompts defer every decision to the "average" image.** For a courier, the average image includes real brand trademarks, so constraints (`no brand names, no logos`) are a requirement, not decoration.
2. **Constraints apply to what the model treats as the subject.** Brands vanished from the courier, but car badges in the background (VW, Honda, Toyota) still appeared. Background objects need explicit wording, such as "unbranded cars".
3. **A reference sheet beats words for identity.** Scenes inherited details from the sheet (stripe pattern), even where the sheet itself drifted from the text.
4. **"Change only X, keep the rest" works when you pass the image back.** The edit was localized on the first attempt; only physical plausibility (how a pizza box is held) slipped.
