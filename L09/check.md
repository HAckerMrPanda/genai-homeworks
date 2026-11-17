# L09 • Check: three questions for each thing

## Thing 1: event announcement document (Claude Docs)
Source: synthetic brief W301 (5 lines). Screenshots: `screenshots/1_document_before.png`, `1_document_after_fix.png`.

**1. Are the numbers and facts right?** Yes, every value was checked against the brief:
- Event "Verify AI output" ✓, 12 November 2026 ✓, 18:30 Europe/Warsaw ✓, 60 minutes ✓, beginners ✓.
- The three topics ✓, "Registration is required" ✓.
- Location, meeting link, price and recording are all shown as "Not specified" ✓.
- Claude deliberately did **not** calculate an end time (19:30) because the brief does not state it.

**2. What did Claude make up?**
- *Claude's own answer:* the subtitle "A teaching session for beginners", the heading "What you will learn" (the brief only says "Topics"), and two **new fields**: "How to register: not specified" and "Registration deadline: not specified".
- *What I found that Claude did not admit:* its first reply said **"Every detail comes from brief W301"**, yet the same document contained the two added fields. The self-report contradicted the document until I asked directly.
- *Formatting:* the details table has an **empty header row**.
- The two invented fields were removed with the fix.

**3. Personal data inside?** No. The brief is fictional and contains no names, e-mails or phone numbers. The document is private ("Only you").

## Thing 2: support ticket dashboard (Data artifact)
Source: `tickets.csv` (12 tickets), **anonymised before upload** to `tickets_anonymised.csv`. E-mails were replaced with Customer 01–12, and staff names (Marta, Oleg, Anya, Ravi) with Agent A–D. Screenshots: `screenshots/2_dashboard_before.png`, `2_dashboard_what_invented.png`.

**1. Are the numbers right?** Yes, every tile was recounted from the file:

| Dashboard | From the file | |
|---|---|:-:|
| Total 12 | 12 rows | ✓ |
| Open 9 | status exactly "Open": T-101, 102, 104, 105, 106, 108, 109, 110, 112 | ✓ |
| Open P1 4 | T-101, T-104, T-106, T-110 | ✓ |
| Open, no owner 2 | T-105, T-110 | ✓ |
| Oldest Open: T-108, 8 days | T-108 days = 8 (max among Open) | ✓ |
| By area: Courier app 2 (both Open), every other area 1; Packaging, Promo codes, Receipt not Open | matches | ✓ |

**2. What did Claude make up?**
- *Claude's own answer:*
  - Assumptions: `days` = days open; P1 = highest priority; empty owner = unassigned; "Open" = status exactly "Open".
  - **Own rules:** the "Needs attention today" rule (Open and P1 or no owner), its ranking order, the extra "Oldest Open ticket" line (not requested) and the "Why" labels.
  - Speculation in chat: that the file "looks like a helpdesk export".
- *The assumption that matters most* (Claude flagged it itself): if "Waiting customer" and "Waiting engineering" also count as unresolved, Open is **11, not 9**. The file does not define it.
- **Inaccuracy I found that Claude did not notice:** the subtitle under "Needs attention today" says *"Unassigned P1s first, then by days open"*, but T-105 (6 days) is listed **last**, after T-104 (1 day). The page states one rule and shows another. In chat Claude described a third version ("unassigned P1, then P1, then unassigned").
- The chart legend "Waiting or Closed" merges two different statuses into one colour.

**3. Personal data inside?** No. E-mails and staff names were removed before upload. Claude warned that anyone with a link to the dashboard can read the **whole attached CSV**, not only the page. That is acceptable only because the file is anonymised; it is the reason "a link is a publication".

## Safety and sharing
- The original `tickets.csv` (with e-mails) was **not** uploaded. Only the anonymised copy was.
- Both artifacts are private ("Only you"), and I hand in screenshots instead of links. If links are added later, they are safe to share: no personal data inside, though the dashboard link exposes the full anonymised CSV.
