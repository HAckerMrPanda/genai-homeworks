# Tasks 001

- [x] T-0 Save baseline: `--expect baseline` → B 11/11 pass, T01/T02/T03/T05 fail (`evidence/01_baseline_before.txt`)
- [x] T-1 Human review of spec/plan/tasks (behaviour, edge cases, AC, scope) → approval before code (approved 2026-11-15)
- [x] T-2 Create branch `feature/001-repeat-skip-out-of-stock`
- [x] T-3 Add `state.repeatNotice`; partition lines in the repeat handler (plan §1–2)
- [x] T-4 Render the escaped `#repeatNotice` in `renderDraft()` (plan §3)
- [x] T-5 Clear the notice in Clear / interpret / submit (plan §4)
- [x] T-6 Run `--expect implemented`; save output (`evidence/03_implemented_after.txt`; first attempt with a check defect kept in `02_…`)
- [x] T-7 Manual UI run and screenshots for AC1/AC2 and AC5; save `git diff main -- app/`
- [x] T-8 Write EVIDENCE.md with the decision ACCEPT / RETRY / REJECT
