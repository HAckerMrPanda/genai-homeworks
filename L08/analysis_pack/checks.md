# 60-second check • Northstar 2025

**Student:** [name / alias] • **Data:** `northstar_2025_EN.xlsx`, practice data (green zone) • **Chat used:** Claude (one conversation: file upload, cleaning, workbook, charts, report, recipe) • **Date:** 2026-11-14

## 1. File description (step 1)
- **Sales:** 1,261 data rows (excluding the header), 9 columns. One row is one day × channel × category × region × warehouse, not one order. Period: 2025-01-01 to 2025-12-31.
- **Reviews:** 357 rows (IDs unique). Period 2025-01-01 to 2025-12-31, rating 1–5, comment text, warehouse.
- **Zeros are not missing values:** `ad_spend = 0` on all 632 Email and Organic rows (326 + 306). These channels buy no ads; their ROAS is shown as N/A. No Search or Social row has zero spend. No negative numbers, no returns > orders, no empty cells.

## 2. Errors found and what I did

| # | Error | Where | What I did |
|---|---|---|---|
| 1 | **Text date** `'10/05/2025'` stored as text, not as a date | Sales, row 444 | Neighbours are 2025-05-09 (row 443) and 2025-05-10 (row 445), so read it as DD/MM: **2025-05-10**. Converted to a real date. |
| 2 | **Exact duplicate** (2025-03-19, Social, Home, South, S1, 72 orders, $3,890.50, $958.51 ad spend, 4 returns) | Sales, rows 265 and 266 | Removed row 266 |

**Rows before / after cleaning:** 1,261 → **1,260** (−1 duplicate; the date fix changes no row count). The input file is untouched: `analysis.xlsx` keeps `Sales_raw` (1,261 rows, exact copy) next to `Sales_clean` (1,260).

## 3. Workbook check (`analysis.xlsx`)
- **Formula cell:** `Sales_clean!K2` contains `=IF(H2=0,"N/A",G2/H2)` (revenue / ad spend), result **4.29**. `K3` (an Email row with $0 spend) shows **N/A**.
- **Pivot:** `Pivot!C3:F14` is month × channel built with `SUMIFS` (e.g. `C3 =SUMIFS(Sales_clean!$G$2:$G$1261, Sales_clean!$J$2:$J$1261, $B3, Sales_clean!$B$2:$B$1261, C$2)`).
- **Pivot vs total:** grand total `Pivot!G15` = **$2,520,078**, and `Pivot!G16` (= G15 − SUM of Sales_clean revenue) = **0**.
- **Chart in the workbook:** a stacked column chart (revenue by month × channel) and a ROAS line chart on the `Pivot` sheet.
- **My check in Excel:** [open `analysis.xlsx`, click `Sales_clean!K2` and `Pivot!C3`, confirm the `fx` bar shows the formula: ✓ / ✗]

## 4. One chart point against the source and the previous version
| Point | Source file / workbook | Chart before | Chart after | Match |
|---|---|---|---|---|
| Social ROAS, July 2025 | `Pivot!L9` = 1.966 (SUMIFS over Sales_clean: $43,154 revenue / $21,949 spend) | line point at ~1.97 (no label) | label **$1.97** | ✓ same |
| Social ROAS, June 2025 | `Pivot!L8` = 3.953 | line point at ~3.95 | label **$3.95** | ✓ same |
| Search ROAS, December 2025 | `Pivot!K14` = 5.35 | ~5.35 | label **$5.35** | ✓ same |

The rework changed layout only: title, labels, colours, no legend, no grid. No value moved, unlike the lesson's case where 49% became 46%.

**Report vs workbook:** December $373.4k = `Pivot!G14` (373,435); +15.1% = `Pivot!B18`; +161.7% = `Pivot!B19`; N2 24.8% = `Pivot!Q5` (274 / 1,103). All match the downloaded `report.docx`, which I opened rather than trusting a preview.

## 5. What each percentage is calculated from
| Number in the report | = | Base |
|---|---|---|
| December +15.1% | Dec revenue / Nov revenue − 1 = 373,435 / 324,344.5 − 1 | November 2025 revenue |
| December +161.7% | Dec / Jan − 1 = 373,435 / 142,712 − 1 | January 2025 revenue |
| November +47.0% | Nov / Oct − 1 = 324,344.5 / 220,665.5 − 1 | October 2025 revenue |
| Social −50% | Jul–Dec ROAS / Jan–Jun ROAS − 1 = 2.00 / 3.98 − 1 (−49.8%) | Social revenue per $1 of Social ad spend in H1 |
| Social spend +78% | Jul spend / Jun spend − 1 = 21,949 / 12,325 − 1 | June Social ad spend |
| N2 return rate 24.8% | sum(returns) / sum(orders), N2, Sep–Dec = 274 / 1,103 | **orders**, not reviews and not rows |
| Others 4.9–5.1% | same formula per warehouse, Sep–Dec | each warehouse's orders |
| 63% negative reviews | reviews rated 1–2 / all N2 reviews, Sep–Dec = 55 / 87 | **reviews** of N2 in Sep–Dec, not orders |
| 53 of 55 damage | 1–2★ N2 reviews mentioning damage / broken / crushed / torn packaging | the 55 negative N2 reviews |

## 6. A plausible claim the data does not prove
**"If we cut the Social budget back to the H1 level, revenue won't drop."** It sounds right, because since July each extra Social dollar brings only $2.00 instead of $3.98. But the file only shows revenue *recorded* under the Social channel, not revenue *caused* by it. Some of those buyers might have come through Search or Organic anyway, and some Search or Organic sales may have started from a Social ad. Spend and revenue also both rose in Q4, the season when everything grows.  
**How to test it:** cut Social spend in two regions (e.g. North and West) for 4 weeks and keep the other two as control. Compare total revenue (all channels) per region against the same weeks before the test.

Second example: "N2's packaging caused the autumn returns." Returns have no reason code, and 87 reviews are a self-selected sample of 1,103 orders. **Test:** pull return reasons for N2 Sep–Dec and check whether N2 changed packaging, carrier or staff in September.

## Bonus: where the data lives in my job (optional)
[3–5 lines: system, export button / report, file format, official API]
