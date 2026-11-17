# Spec 001 · Repeat order skips out-of-stock products

**Source:** `NEW_REQUIREMENT_REPEAT_SKIP_OUT_OF_STOCK.md` · **Status:** approved by the human reviewer before implementation · **Branch:** `feature/001-repeat-skip-out-of-stock`

## Problem
"↻ Repeat order" copies every line of a previous order into the draft, including products whose availability is now `out`. The buyer can resubmit them, and the manager rejects the same line again.

## Behaviour
When the buyer clicks **Repeat order** on order *N*:
1. For each line of *N*, look up the product's **current** availability in `CATALOG`.
2. Copy lines with availability `in` or `limited` into the draft with the **same number of cases**. Limited items keep their existing "Limited" badge.
3. Do **not** copy lines with availability `out`.
4. If at least one line was skipped, show a notice `#repeatNotice` above the draft:
   *"Not added from order #N — out of stock: Chickpeas, 1 kg pack."* It lists the product names, comma-separated.
5. If **every** line was skipped, the draft stays empty and **Submit** stays disabled. The notice reads:
   *"Nothing could be repeated from order #N — all products are out of stock: …"*
6. Copy the delivery address of *N* to the address selector (unchanged behaviour).
7. Order *N* itself is **not modified**: same lines, total and status.
8. The notice disappears when the draft is cleared, a new draft is prepared from text, or the order is submitted.

## Edge cases
- No line skipped → no notice (behaviour as before).
- A product that was `limited` when ordered is still copied. Availability is read at repeat time, not taken from the old order.
- The same product appearing once in an order → one entry in the notice. Lines are already merged by SKU.
- Repeating twice → the notice reflects the latest repeat only.

## Acceptance criteria (checked by `tests/run_checks.py`)
| ID | Given / when / then | Check |
|---|---|---|
| AC1 | Given an order with 5 lines incl. *Chickpeas (out)*, when repeated, then the draft has 4 lines and no chickpeas | T01 |
| AC2 | …and a visible `#repeatNotice` names "Chickpeas, 1 kg pack" and says "out of stock" | T02 |
| AC3 | …and the total is recalculated by code for the 4 lines: **2,323,200 UZS**, and the limited *Tomato paste* line is present | T03 |
| AC4 | …and the original order in history still shows 5 lines and **2,497,200 UZS** | T04 (regression guard) |
| AC5 | Given an order with only chickpeas, when repeated, then 0 draft lines, Submit disabled, and the notice says "Nothing could be repeated" and names the product | T05 |
| AC6 | Given the notice is shown, when the buyer clicks Clear, then the notice is gone | T06 (regression guard) |
| — | All 11 baseline checks B01–B11 still pass, unedited | B01–B11 |

Visible manual check (screenshots in `evidence/`): repeat a 5-line order with chickpeas → 4 lines + notice; repeat a chickpeas-only order → empty draft, disabled submit, notice.

## Scope
**In:** the repeat handler, the draft notice and its clearing, the feature checks T01–T06.
**Out (non-goals):**
- proposing substitutes;
- re-checking availability at submit time or for manually added lines;
- the manager view;
- changing catalog data, prices or rounding;
- the model/interpreter;
- persistence format.
