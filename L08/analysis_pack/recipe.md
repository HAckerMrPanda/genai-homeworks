# Recipe: rebuild the sales charts for next month

**Script:** `recipe.py` (next to this file; Python 3 + pandas + matplotlib)  
**Tested on:** `northstar_sales_2026-01.csv` (100 rows, 2026-01-01 to 2026-01-31), run in the chat on 2026-11-14  
**Output:** `charts/recipe_2026-01/01_revenue.png`, `02_roas.png`, `03_returns.png`

## Prompt (paste with next month's CSV)
```text
Here is next month's Northstar sales file (CSV, same columns as the 2025 Sales sheet:
order_date, channel, category, region, warehouse, orders, revenue, ad_spend, returns).
One row = one day x channel x category x region x warehouse, not one order.
Run recipe.py on it and show me the three charts and the printed tables:
1) revenue by day (or by month if the file covers several months), with the total in the title;
2) revenue per $1 of ad spend for Search and Social = sum(revenue) / sum(ad_spend); Email and Organic buy no ads, so skip them;
3) return rate by warehouse = sum(returns) / sum(orders), sorted, highest warehouse in the accent colour.
Before charting, report: rows in, rows with unreadable dates, exact duplicates removed, rows after cleaning.
There is no Reviews sheet in this file: do not produce any review findings, just say they are skipped.
```

## How to run locally
```bash
python recipe.py northstar_sales_2026-01.csv charts/recipe_2026-01
```

## Actual output (January 2026)
```text
rows in: 100, bad dates dropped: 0, rows after cleaning: 100
         revenue  ad_spend  roas
channel
Search   37827.5   7105.07  5.32
Social   42615.0  21444.02  1.99
           returns  orders   rate
warehouse
S1              34     722   4.71
W1              36     746   4.83
N1              32     632   5.06
C1              36     636   5.66
N2              30     121  24.79
Reviews chart skipped: the sales CSV contains no reviews.
```
January total revenue: **$147.1k**. Both 2025 problems continue: Social returns **$1.99** per $1 (Search **$5.32**), and N2 returns **24.8%** (30 / 121 orders) against 4.7–5.7% elsewhere.

## What the recipe does not rebuild
- **Chart 3's review part.** The January file has sales only and no `Reviews` sheet, so the script makes no review chart and no review statistics. The return-rate chart is rebuilt; the "what customers say about N2" part is not.
- **"By month" view.** With a single month there is nothing to compare month to month, so chart 1 switches to revenue by day. Days with no rows (7, 10, 25 January) are simply absent from the axis, not shown as zero.
- **Month-over-month ROAS.** Chart 2 becomes one value per channel for the month instead of a 12-month line.

No errors on this file. The script drops rows with unreadable dates and exact duplicates and prints how many. It reads dates as ISO (`2026-01-31`); a `10/05/2025`-style text date like the one in the 2025 file would be **dropped**, not fixed, so check the "bad dates dropped" line.
