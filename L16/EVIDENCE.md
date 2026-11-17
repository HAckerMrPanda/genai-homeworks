# EVIDENCE · Feature 001 "Repeat order skips out-of-stock products"

**Author / reviewer:** Kodirjon Khayitov · **Date:** 2026-11-15
**Project:** my own small project, the WholesaleDesk prototype from L14 (one HTML file, sample data). This is the "small project you can run locally" option. The guided Course Recall `sdd_demo` package was not in my lesson materials (the full pack contains only the L16 homework text).

## Client, model, mode
- **Agent:** Claude (Anthropic), model **Claude Opus 5.5**, working as a coding agent in its own Linux workspace with file and shell tools (git, Python, headless Chrome via Playwright).
- **Mode:** spec-driven, with a human gate.
  - The agent wrote the requirement-based spec/plan/tasks.
  - I reviewed and **approved them before any code change**. This is recorded in the commit "Record spec approval" and in `tasks.md` T-1.
  - Implementation happened on the isolated branch `feature/001-repeat-skip-out-of-stock`; `main` keeps the starter.
- **Rules for the agent:** `AGENTS.md` (no code before an approved spec, baseline checks must not be edited, small diff, report real output only).

## Checks and real outputs
**Command:** `python3 tests/run_checks.py --expect baseline|implemented`
- 11 baseline checks (B01–B11) cover existing behaviour: totals, case rounding, unrecognised items, injected discount ignored, manager flow, repeat keeps the address.
- 6 target checks (T01–T06) were written from the spec's acceptance criteria **before** implementation.

| Step | File | Result |
|---|---|---|
| Before code, starter on `main` | `evidence/01_baseline_before.txt` | B **11/11** · T 2/6 (T01, T02, T03, T05 fail as expected; T04/T06 are regression guards) · *EXPECTATION baseline: MET* |
| After code, attempt 1 | `evidence/02_implemented_attempt1_T01_check_defect.txt` | B 11/11 · T **5/6**, T01 FAIL · *NOT MET* |
| Diagnosis | — | The code was right (T03 showed 4 lines and 2,323,200). **T01 itself was imprecise:** it searched for "Chickpeas" in the whole draft area, which also contains the notice that AC2 *requires* to name the product. AC1 is about draft **lines**, so I narrowed T01 to the table rows. |
| After the check fix | `evidence/03_implemented_after.txt` | B **11/11** · T **6/6** · documents present · *EXPECTATION implemented: MET* |
| Is the fixed check still meaningful? | `evidence/04_new_checks_on_old_code.txt` | The new checks on the **old** code: T01 still FAILS ("5" lines), so the fix did not weaken it |

The baseline checks B01–B11 were **not edited**. The only test change is the T01 narrowing above, visible in the git history.

## Files changed (`git diff main -- app/` → `evidence/feature_001.diff`)
- `app/index.html`, +22 / −6:
  - new `state.repeatNotice`;
  - a new `repeatOrder(o)` function that splits lines into kept and skipped by **current** `CATALOG` availability;
  - an escaped `#repeatNotice` in `renderDraft()`;
  - the notice is cleared on Clear, on a new interpreted draft and on submit;
  - the old one-line repeat handler now calls `repeatOrder`.
- `tests/run_checks.py`: T01 assertion narrowed (+3 / −1).
- No change to prices, rounding, the catalog, the manager view or storage.

## UI observation (screenshots in `evidence/`)
- `05_original_order_5_lines.png`: the order is oil, rice, tea, tomato paste (Limited) and chickpeas (Out of stock). Total **2,497,200 UZS**, address Yunusabad.
- `06_repeat_skips_out_of_stock.png`: after **Repeat order**:
  - the notice says *"Not added from order #1001 — out of stock: Chickpeas, 1 kg pack."*;
  - the draft has **4 lines**, and tomato paste keeps its "Limited" badge;
  - total **2,323,200 UZS** (= 2,497,200 − 174,000);
  - the address is still Yunusabad;
  - history still shows **#1001 · 5 line(s) · 2,497,200 UZS**.
- `07_repeat_all_out_of_stock.png`: a chickpeas-only order, repeated:
  - the notice says *"Nothing could be repeated from order #1001 — all products are out of stock: Chickpeas, 1 kg pack."*;
  - the draft is empty and **Submit is disabled**.

## Remaining limitations
- In this prototype availability is a **static** catalog value. So "availability at repeat time" cannot yet show a product that became out of stock *after* ordering. The test uses a product that is already out of stock.
- The notice stays visible if the buyer then adds a product from the catalog or changes cases. The spec only requires clearing on Clear, a new text draft and submit. Small, but a UX question for users.
- The feature does not prevent submitting an out-of-stock product through a new text order: the chickpeas-only order was accepted. Substitutes and a submit-time stock check are out of scope (spec non-goals).
- Checks run against the local file, so the AI-model interpreter path (`sample` capability) is not covered. Repeat does not use the model.
- Tests prove the behaviour described in the spec, not that the spec is what buyers want. That still needs user feedback.

## Decision: **ACCEPT**
- All acceptance criteria are met, with independent evidence: the check output, the old-code counter-check and the screenshots.
- The baseline is unchanged and green.
- The diff is small, readable and inside the approved scope.
- The one problem found was in my own target check, not in the code. It was fixed narrowly and shown to still catch the old behaviour.
