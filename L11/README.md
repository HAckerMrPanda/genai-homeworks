# L11 • Project rules and one skill

**Author:** Kodirjon Khayitov · **Date:** 2026-11-15

## What is here
| File | Status |
|---|---|
| `AGENTS.md` | shared project rules, unchanged |
| `source-facts.md`, `draft-announcement.md` | inputs, unchanged (byte-compared with the originals) |
| `.agents/skills/review-announcement/SKILL.md` | **edited**: one rule added (below); name, description and existing steps kept |
| `.agents/skills/review-announcement/references/checklist.md`, `assets/review-template.md` | files referenced by the skill, unchanged |
| `drafts/announcement-review.md` | **result**: correction table, missing information, complete corrected announcement |

## Skill change (step 2)
The only diff in `SKILL.md`:
```
+ If a joining link is absent, write 'Joining link not provided' and do not generate a link.
```

## Request sent to the agent (step 3)
```
Use the review-announcement skill to check draft-announcement.md against source-facts.md. Save the claim/source/correction table and the complete corrected announcement as drafts/announcement-review.md. Apply the missing-link rule. Do not change the source files or publish anything.
```

## My check of the result (step 4)
| Item | `source-facts.md` | Draft (before) | `announcement-review.md` (after) | OK |
|---|---|---|---|---|
| Date | 4 November 2026 | 5 November 2026 | 4 November 2026 | ✅ |
| Start / timezone | 18:30 Europe/Warsaw | 19:00 Europe/Warsaw | 18:30 (Europe/Warsaw) | ✅ |
| Duration | 90 minutes | two hours | 90 minutes | ✅ |
| Registration | required, via the group's teaching chat, by 18:00 on 3 Nov 2026 (Europe/Warsaw) | "No registration is needed" | required, same channel and deadline | ✅ |
| Joining link | not supplied | not mentioned | "Joining link not provided", and a search for `http`, `www`, `.com` found no link | ✅ |
| Kept facts | title, Teams, audience, free, topic | same | same | ✅ |

No remaining mismatch was found, so no manual correction was needed. The agent did not change the source files and did not publish or send anything. Only synthetic data was used.
