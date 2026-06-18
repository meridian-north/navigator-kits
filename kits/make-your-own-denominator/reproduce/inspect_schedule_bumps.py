#!/usr/bin/env python3
"""
inspect_schedule_bumps.py  — model-free edition (multi-year)
Does the all-cause infant death count rise at the 2/4/6-month vaccination ages?

NO MODEL. NO SMOOTHING. NO THRESHOLD. NO VERDICT.
We do not fit a curve. We do not smooth. We do not declare "flag." We show the RAW
daily counts and put each vaccination-age window next to its OWN immediately-adjacent
raw windows (equal width). The clean model-free question: does the AT-AGE window exceed
BOTH neighbors? On a declining curve it normally won't; a real post-shot bump would.
We tally that across every year you've gathered. You read the numbers and judge.

Reads out/allcause_age_long.csv (every year you've run through gather_nber_lbid.py).
Pure stdlib.

USAGE:
  python3 inspect_schedule_bumps.py            # ±7-day windows, raw strip ±14
  python3 inspect_schedule_bumps.py --half 3   # change the window half-width you view
  python3 inspect_schedule_bumps.py --quiet    # summary only (skip per-year raw strips)
"""

import argparse, csv, statistics
from collections import defaultdict
from pathlib import Path

LONG = Path(__file__).resolve().parent / "out" / "allcause_age_long.csv"
SCHEDULE = {"2 months (dose 1)": 61, "4 months (dose 2)": 122, "6 months (dose 3)": 183}


def load():
    keys = defaultdict(dict)
    if not LONG.exists():
        return keys
    with LONG.open() as f:
        for r in csv.DictReader(f):
            keys[(r["country"], r["year"])][int(r["age_days"])] = int(r["all_cause_deaths"])
    return keys


def wsum(by_day, lo, hi):
    return sum(by_day.get(d, 0) for d in range(lo, hi + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--half", type=int, default=7)
    ap.add_argument("--strip", type=int, default=14)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--exclude", default="", help="comma-separated years to drop (e.g. mis-parsed 2002)")
    args = ap.parse_args()
    W, S = args.half, args.strip
    width = 2 * W + 1

    keys = load()
    if not keys:
        print(f"no {LONG} — run gather_nber_lbid.py first."); return
    drop = {y.strip() for y in args.exclude.split(",") if y.strip()}
    if drop:
        keys = {k: v for k, v in keys.items() if k[1] not in drop}
        print(f"(excluding year(s): {', '.join(sorted(drop))})")

    # collect per (age, year): before, at, after, exceeds_both
    agg = {label: [] for label in SCHEDULE}

    for (country, year), by_day in sorted(keys.items(), key=lambda kv: (kv[0][0], int(kv[0][1]))):
        if not args.quiet:
            print(f"\n=== {country} {year} — raw all-cause infant deaths near the vaccination ages ===")
            print(f"    no model · no smoothing · no threshold · window ±{W} days (your choice, shown)")
        for label, age in SCHEDULE.items():
            before = wsum(by_day, age - W - width, age - W - 1)
            at     = wsum(by_day, age - W, age + W)
            after  = wsum(by_day, age + W + 1, age + W + width)
            nb = (before + after) / 2.0
            ratio = (at / nb) if nb else float("nan")
            exceeds_both = (at > before) and (at > after)
            agg[label].append((year, before, at, after, ratio, exceeds_both))
            if not args.quiet:
                print(f"\n  {label} — day {age}")
                days = list(range(age - S, age + S + 1))
                for i in range(0, len(days), 10):
                    chunk = days[i:i+10]
                    print("      " + "  ".join(f"{d}:{by_day.get(d,0)}" for d in chunk))
                mark = "  <-- AT-AGE exceeds BOTH neighbors" if exceeds_both else ""
                print(f"    window sums ({width} d each): before={before}  AT-AGE={at}  after={after}{mark}")
                print(f"    AT-AGE / mean(before,after) = {ratio:.2f}   (raw arithmetic, no cutoff)")

    # ---- model-free multi-year summary ----
    print(f"\n========== MULTI-YEAR SUMMARY (model-free) · {len(keys)} year(s) · window ±{W} d ==========")
    print("  The only clean bump test with no model: does AT-AGE exceed BOTH adjacent windows?")
    print("  (On a declining curve it normally won't; a real post-shot bump would, repeatedly.)\n")
    print(f"  {'vaccination age':<20}{'yrs AT-AGE > both':>18}{'median ratio':>15}{'min':>7}{'max':>7}")
    for label in SCHEDULE:
        rows = agg[label]
        nb_both = sum(1 for t in rows if t[5])
        rs = [t[4] for t in rows]
        med = statistics.median(rs) if rs else float("nan")
        print(f"  {label:<20}{f'{nb_both} of {len(rows)}':>18}{med:>15.2f}{min(rs):>7.2f}{max(rs):>7.2f}")
    print("\n  Read it plainly — and note the exposure is NOT fixed across years (the schedule")
    print("  and formulations changed: DTP->DTaP, thimerosal removed ~2001, PCV/Hib/rotavirus")
    print("  added, COVID only recently). So DO NOT pool years into one average. Two patterns:")
    print("   - a CONSTANT, schedule-timing effect would put 'AT-AGE > both' in MOST years and")
    print("     lift the median clearly above 1;")
    print("   - a FORMULATION- or LOT-specific effect would NOT be constant: it would make ONE")
    print("     year (or a few) STAND OUT — watch the max column and any single high year, not")
    print("     the median. Pooling would hide exactly this; the per-year tally is the right lens.")
    print("  Either way this is a LEAD, not a verdict: which product/lot a standout year implicates")
    print("  is unanswerable from all-cause deaths-by-age alone. It needs the linked vaccination")
    print("  records (product, lot, date) — the withheld denominator. Timing only; neutral on safety.")
    print("  ANTI-PLACEBO LIMIT (disclosed): the adjacent windows are NOT a true placebo — on the")
    print("  dense infant schedule they are themselves near shots. So this catches a SHARP, localized")
    print("  spike (it flags rotavirus/intussusception, MMR/febrile-seizure) but is BLIND to a DIFFUSE")
    print("  effect smeared across the comparison window. Beating that needs a true unvaccinated")
    print("  baseline — matched, denominated, linked records. That is exactly what is withheld.")


if __name__ == "__main__":
    main()
