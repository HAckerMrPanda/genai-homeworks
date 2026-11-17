"""Rebuild the Northstar sales charts from a monthly sales CSV.

Usage: python recipe.py northstar_sales_2026-01.csv out_dir
Input columns: order_date, channel, category, region, warehouse, orders, revenue, ad_spend, returns
Makes: 01_revenue.png, 02_roas.png, 03_returns.png. The reviews chart is NOT built:
the monthly sales file has no Reviews data, so no review findings are produced.
"""
import sys
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ACCENT, GREY = "#eb6834", "#b9b7b0"
plt.rcParams.update({"font.size": 10, "text.parse_math": False})


def load(path):
    df = pd.read_csv(path)
    rows_in = len(df)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", dayfirst=False)
    bad_dates = int(df["order_date"].isna().sum())
    df = df.dropna(subset=["order_date"]).drop_duplicates()
    print(f"rows in: {rows_in}, bad dates dropped: {bad_dates}, rows after cleaning: {len(df)}")
    return df


def main(src, out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    df = load(src)
    period = f"{df.order_date.min():%Y-%m-%d} to {df.order_date.max():%Y-%m-%d}"
    one_month = df.order_date.dt.to_period("M").nunique() == 1
    key = df.order_date.dt.day if one_month else df.order_date.dt.month
    unit = "day of month" if one_month else "month"

    rev = df.groupby(key)["revenue"].sum()
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=120)
    ax.bar(rev.index.astype(str), rev.values / 1000, color=GREY)
    ax.set_title(f"Revenue ${rev.sum()/1000:,.1f}k by {unit}, {period}", loc="left", fontweight="bold")
    ax.set_ylabel("Revenue, $k"); ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "01_revenue.png"); plt.close(fig)

    paid = df[df.channel.isin(["Search", "Social"])]
    g = paid.groupby("channel")[["revenue", "ad_spend"]].sum()
    g["roas"] = g.revenue / g.ad_spend
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=120)
    ax.barh(g.index, g.roas, color=[ACCENT if c == "Social" else GREY for c in g.index])
    for c, r in g.iterrows():
        ax.text(r.roas + 0.05, c, f"${r.roas:.2f} per $1", va="center")
    ax.set_title(f"Revenue per $1 of ads, {period}", loc="left", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "02_roas.png"); plt.close(fig)

    w = df.groupby("warehouse")[["returns", "orders"]].sum()
    w["rate"] = w.returns / w.orders * 100
    w = w.sort_values("rate")
    top = w.rate.idxmax()
    fig, ax = plt.subplots(figsize=(8, 3.8), dpi=120)
    ax.barh(w.index, w.rate, color=[ACCENT if i == top else GREY for i in w.index])
    for i, r in w.iterrows():
        ax.text(r.rate + 0.3, i, f"{r.rate:.1f}% ({int(r.returns)}/{int(r.orders)})", va="center")
    ax.set_title(f"Return rate by warehouse (returns / orders), {period}", loc="left", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(out / "03_returns.png"); plt.close(fig)

    print(g.round(2).to_string()); print(w.round(2).to_string())
    print("Reviews chart skipped: the sales CSV contains no reviews.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
