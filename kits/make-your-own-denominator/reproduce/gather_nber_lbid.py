#!/usr/bin/env python3
"""
gather_nber_lbid.py
US all-cause infant deaths by age-at-death — from the NCHS/NBER Linked Birth/Infant
Death public-use files. COMPLIANT BULK ROUTE that bypasses CDC WONDER (no API, no 429):
the flat files are downloadable public-use data, no application required.

CANONICAL OUTPUT — one sovereign, tidy, long-format CSV
-------------------------------------------------------
  out/allcause_age_long.csv   schema:
      country, year, age_days, all_cause_deaths, basis, source, sha256, caveat
This is the RAW layer per CLAUDE.md: no model in the path, grep-able, SHA-pinned,
append-safe across years/countries, and reproducible (same input file -> same rows).
Re-running a (country, year) UPSERTS — old rows for that key are replaced, never duped.

DERIVED VIEWS (regenerated FROM the long CSV — never edited by hand, never a 2nd truth)
  out/derived_byday_<country>_<year>.csv      age_days, all_cause_deaths
  out/derived_bymonth_<country>_<year>.csv     month_bin, all_cause_deaths, post_neonatal
  out/MANIFEST_SHA256.txt                       sha per input file
  out/ABSENCES.csv                              recorded refusals / missing inputs

VERIFIED LAYOUT (period linked file, 2019+ ; primary source)
------------------------------------------------------------
NCHS "User Guide to the 2023 Period / 2022 Cohort Linked Birth/Infant Death Public Use
File" (ftp.cdc.gov/.../period-cohort-linked/23PE22CO_linkedUG.pdf):
  cols 1356-1358 (3)  AGEDX  Age at Death in Days  000 = 0 days ; 001-364 = days
We use AGEDX (exact days) — least ambiguous field — and bin months ourselves.
CONFIRM byte positions per data year; NCHS shifts columns between revisions.

KIND-GATHERER DISCIPLINE: source-of-record only · SHA per input · recorded-absence-is-
a-result · HOST-RUN (files are large). We use the official public-use download; we do
not defeat any control.

USAGE
-----
  python3 gather_nber_lbid.py --infile ~/Downloads/<numerator_file>.dat --year 2022
  python3 gather_nber_lbid.py --rebuild-views      # just regenerate derived views from long CSV
"""

import argparse, csv, gzip, hashlib, io, os
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(exist_ok=True)
LONG = OUT / "allcause_age_long.csv"
LONG_COLS = ["country", "year", "age_days", "all_cause_deaths", "basis", "source", "sha256", "caveat"]

CAVEAT = ("age_is_objective_date_arithmetic;cause_label_not_used;all_cause_basis;"
          "reported_is_a_floor_not_a_rate;denominator=live_births_join_pending;"
          "indexed_presence_is_not_efficacy")

LAYOUTS = {  # 1-based inclusive byte spans; confirm per year vs the NCHS user guide
    # "2019+" span is SOURCE-VERIFIED for the 2022-cohort/2023-period file from the
    # matching NCHS guide 23PE22CO_linkedUG.pdf. Get 2018-2023 from NCHS VitalStats
    # Online (NBER stops at 2017). For NBER years <=2013 the positions DIFFER — add a
    # per-year layout here from that year's LinkPE<YY>Guide.pdf, or use the .csv mirror
    # and read column AGEDX by name instead of by byte offset.
    "2019+": {"AGEDX": (1356, 1358)},
}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def open_maybe_gz(p: Path):
    if str(p).endswith(".gz"):
        return io.TextIOWrapper(gzip.open(p, "rb"), encoding="latin-1", errors="replace")
    return open(p, "r", encoding="latin-1", errors="replace")


def fw(line, span):
    a, b = span
    return line[a - 1:b]


# candidate column names for "age at death in days" across NBER/NCHS csv vintages
AGE_COL_CANDIDATES = ["agedx", "aged", "age_d", "aged_days", "ageddays"]


def detect_age_col(header, override=None):
    if override:
        return override if override in header else None
    low = {h.lower(): h for h in header}
    for c in AGE_COL_CANDIDATES:
        if c in low:
            return low[c]
    return None


def tabulate_csv(path, age_col_override):
    """Read an NBER/NCHS csv mirror; tabulate all-cause deaths by age-in-days by COLUMN NAME."""
    by_day, total, kept = Counter(), 0, 0
    with open_maybe_gz(path) as fh:
        rdr = csv.DictReader(fh)
        col = detect_age_col(rdr.fieldnames or [], age_col_override)
        if not col:
            print("  ! could not auto-detect the age-at-death-in-days column.")
            print(f"    columns present: {', '.join(rdr.fieldnames or [])}")
            print("    re-run with --age-col <name> (the one holding age in DAYS, 0-364).")
            return None, 0, 0, None
        for row in rdr:
            total += 1
            raw = (row.get(col) or "").strip()
            if not raw.isdigit():
                continue
            d = int(raw)
            if d > 364:
                continue
            kept += 1
            by_day[d] += 1
    return by_day, kept, total, col


def day_to_month_bin(days: int) -> str:
    m = int(days // 30.44)
    return f"{m:02d}mo" if m <= 11 else "12mo+"


def record_absence(country, year, what, source, reason):
    ab = OUT / "ABSENCES.csv"
    new = not ab.exists()
    with ab.open("a", newline="") as f:
        w = csv.writer(f)
        if new: w.writerow(["country", "year", "what", "source", "reason"])
        w.writerow([country, year, what, source, reason])
    print(f"  ✎ recorded absence: {country} {year} — {reason}")


def read_long():
    if not LONG.exists():
        return []
    with LONG.open(newline="") as f:
        return list(csv.DictReader(f))


def write_long(rows):
    rows.sort(key=lambda r: (r["country"], int(r["year"]), int(r["age_days"])))
    with LONG.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=LONG_COLS); w.writeheader(); w.writerows(rows)


def upsert_long(country, year, by_day, source, sha):
    """Replace all rows for (country, year), then append the fresh ones. No dupes."""
    rows = [r for r in read_long() if not (r["country"] == country and r["year"] == str(year))]
    for d in range(0, 365):
        rows.append({"country": country, "year": str(year), "age_days": str(d),
                     "all_cause_deaths": str(by_day.get(d, 0)), "basis": "all_cause",
                     "source": source, "sha256": sha, "caveat": CAVEAT})
    write_long(rows)


def rebuild_views():
    """Regenerate every derived view strictly FROM the long CSV (single source of truth)."""
    rows = read_long()
    keys = defaultdict(dict)  # (country,year) -> {day: count}
    for r in rows:
        keys[(r["country"], r["year"])][int(r["age_days"])] = int(r["all_cause_deaths"])
    for (country, year), by_day in keys.items():
        with (OUT / f"derived_byday_{country}_{year}.csv").open("w", newline="") as f:
            w = csv.writer(f); w.writerow(["age_days", "all_cause_deaths"])
            for d in range(0, 365): w.writerow([d, by_day.get(d, 0)])
        bymonth = Counter()
        for d, c in by_day.items(): bymonth[day_to_month_bin(d)] += c
        with (OUT / f"derived_bymonth_{country}_{year}.csv").open("w", newline="") as f:
            w = csv.writer(f); w.writerow(["month_bin", "all_cause_deaths", "post_neonatal(>=28d)"])
            for m in [f"{i:02d}mo" for i in range(12)] + ["12mo+"]:
                pn = "yes" if (m != "00mo") else "no"  # 00mo spans 0-30d; flag the rest post-neonatal-ish
                w.writerow([m, bymonth.get(m, 0), pn])
        pn = {d: c for d, c in by_day.items() if 28 <= d <= 364}
        if pn:
            peak = max(pn, key=pn.get)
            print(f"  {country} {year}: post-neonatal all-cause peak ~{peak} d "
                  f"(~{day_to_month_bin(peak)}), n={pn[peak]}")
    print(f"  rebuilt {len(keys)} derived view-pair(s) from {LONG.name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", help="local NCHS/NBER linked FIXED-WIDTH numerator file (.dat/.gz)")
    ap.add_argument("--csv", help="local NBER/NCHS CSV mirror (reads age-at-death by column NAME — "
                                  "robust for any year, e.g. NBER 2013 linkpe2013usnum.csv)")
    ap.add_argument("--age-col", help="explicit age-in-days column name for --csv mode (if auto-detect fails)")
    ap.add_argument("--year")
    ap.add_argument("--country", default="USA")
    ap.add_argument("--layout", default="2019+", choices=list(LAYOUTS),
                    help="byte layout for --infile; default verified for 2022 cohort/2023 period file")
    ap.add_argument("--rebuild-views", action="store_true",
                    help="regenerate derived views from the long CSV and exit")
    args = ap.parse_args()

    if args.rebuild_views:
        rebuild_views(); return

    if not args.year or not (args.infile or args.csv):
        ap.error("need --year and one of --infile (.dat) or --csv (.csv)  (or use --rebuild-views)")

    src = Path(os.path.expanduser(args.csv or args.infile))
    if not src.exists():
        record_absence(args.country, args.year, "all-cause deaths by age-in-days",
                       str(src), "input file not found — download from NBER/NCHS first")
        return

    sha = sha256_file(src)
    if args.csv:
        by_day, kept, total, used_col = tabulate_csv(src, args.age_col)
        if by_day is None:
            return
        print(f"  csv mode: age column = '{used_col}'")
        source_label = f"NBER/NCHS linked csv mirror {src.name} (col {used_col})"
    else:
        span = LAYOUTS[args.layout]["AGEDX"]
        by_day = Counter(); total = kept = 0
        with open_maybe_gz(src) as fh:
            for line in fh:
                total += 1
                raw = fw(line, span).strip()
                if not raw.isdigit():
                    continue
                d = int(raw)
                if d > 364:
                    continue
                kept += 1
                by_day[d] += 1
        source_label = f"NCHS/NBER linked fixed-width file {src.name} (AGEDX {span[0]}-{span[1]})"

    # QC guard: auto-flag a mis-parsed year (age-coding quirk / sentinel value) instead of
    # letting it ride. The post-neonatal (28-364 d) peak should sit ~28-40 d with a busiest-
    # day count well under ~200; anything else is almost certainly a parse problem.
    pn = {d: c for d, c in by_day.items() if 28 <= d <= 364}
    if pn:
        pn_peak = max(pn, key=pn.get); pn_max = pn[pn_peak]
        if pn_peak > 45 or pn_max > 200:
            print(f"  ⚠ QC WARNING: {args.country} {args.year} looks MIS-PARSED — post-neonatal peak at "
                  f"day {pn_peak} (n={pn_max}); expected ~28-40 d, n<200. Likely an age-coding quirk/"
                  f"sentinel in this year's file. REVIEW or EXCLUDE before quoting.")
            record_absence(args.country, args.year, "QC: implausible age distribution",
                           source_label, f"pn_peak_day={pn_peak};pn_peak_n={pn_max}")
    upsert_long(args.country, args.year, by_day, source_label, sha)
    with (OUT / "MANIFEST_SHA256.txt").open("a") as f:
        f.write(f"{sha}  {src.name}  ({args.country} {args.year}; {source_label})\n")

    print(f"✓ {args.country} {args.year}: {kept:,} infant-death records of {total:,} lines "
          f"upserted into {LONG.name} (input sha {sha[:16]}…)")
    rebuild_views()
    print(f"  canonical: {LONG.name}  |  derived views regenerated  |  one sovereign schema")


if __name__ == "__main__":
    main()
