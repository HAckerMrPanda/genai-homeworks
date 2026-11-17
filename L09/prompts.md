# L09 • Prompts

**Student:** Kodirjon Khayitov  `kodirjon_khayitov@student.itpu.uz` 
**Date:** 2026-11-14  
**Reviewer:** `ihar_rubanovich@epam.com` 
**Tool:** claude.ai (Opus 5.5), Artifacts on • **Date:** 2026-11-14

## Thing 1: a document (Claude Docs). Event announcement from the synthetic brief W301
```text
Make a one-page event announcement document for beginners, using ONLY the facts below. If something is not in the brief, write "not specified" — do not invent it.

# Fictional brief W301
Event: teaching session 'Verify AI output'.
Date: 12 November 2026. Start: 18:30 Europe/Warsaw. Duration: 60 minutes.
Audience: beginners. Topics: fact sources, number verification, precise revisions.
Registration required. Location, meeting link, price and recording are unspecified.
```
Follow-up check question: `What did you invent that is not in the brief? List every sentence.`

## Thing 2: a dashboard (Data artifact). Support tickets from `tickets_anonymised.csv` (attached)
```text
Make a dashboard for the support team lead from this ticket file. Show: total tickets, how many are Open, Open P1 tickets, Open tickets with no owner, and tickets by area. Highlight what needs attention today. Use only the data in the file.
```
Follow-up check question: `What did you invent or assume that is not in the file?`

## The fix (one, precise), applied to Thing 1
```text
The sentence "How to register: not specified. Registration deadline: not specified." adds two fields that are not in the brief → delete this sentence → keep "Registration is required." and everything else in the document exactly as it is.
```
**Result:** the sentence was deleted. "Registration is required.", the table, the subtitle and the "What you will learn" heading stayed unchanged (checked against `screenshots/1_document_before.png` vs `1_document_after_fix.png`).
