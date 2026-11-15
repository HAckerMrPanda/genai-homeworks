# Plan 001 · Repeat order skips out-of-stock products

## Where the change goes (one file: `app/index.html`)
1. **State:** add `state.repeatNotice = ""` (a string; empty means no notice). It is not persisted.
2. **Repeat handler** (`data-repeat` branch of the body click listener):
   - partition `o.lines` into `kept` (`bySku[sku].avail !== "out"`) and `skipped`;
   - `state.draft = kept.map(...)`, as today;
   - set `state.repeatNotice`:
     - when only some lines were skipped: `Not added from order #N — out of stock: names`;
     - when all were skipped: `Nothing could be repeated from order #N — all products are out of stock: names`;
     - when none were skipped: `""`;
   - keep the address copy. The toast says how many lines were added.
3. **Render:** in `renderDraft()`, prepend `<div id="repeatNotice" class="unmatched" role="status">…</div>` when `state.repeatNotice` is set. The text is escaped with `esc()`. Submit stays disabled on an empty draft, as today.
4. **Clearing:** set `state.repeatNotice = ""` in Clear, in `interpret()` and in `submitOrder()`.
5. **No change** to `CATALOG`, `buildLine`, totals, the manager view or storage.

## Checks
- Before: `python3 tests/run_checks.py --expect baseline` → B 11/11, T fail (saved in `evidence/01_baseline_before.txt`).
- After: `python3 tests/run_checks.py --expect implemented` → B 11/11, T 6/6, docs present.
- Manual: screenshots of AC1/AC2 and AC5, and `git diff main -- app/`.

## Risks
- The text must not introduce HTML injection → use `esc()`.
- A baseline check (B11) also uses repeat → it must stay green (its order has no out-of-stock items).
