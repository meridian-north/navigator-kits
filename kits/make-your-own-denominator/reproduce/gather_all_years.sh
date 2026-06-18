#!/bin/bash
# Pull the FULL NBER one-click series (1995-2013) of US linked infant-death numerator
# files, fold each into the sovereign long CSV, then run the model-free schedule check
# across every year. Host-run. Kind-gatherer discipline: source-of-record only, each
# year SHA-pinned by gather_nber_lbid.py, recorded-absence-is-a-result.
#
#   bash ~/make-your-own-denominator/gather_all_years.sh
#
# NBER covers 1995-2013 as one-click CSV mirrors (age-at-death column 'aged').
# 2014-2017 are NBER raw mirrors; 2018-2023 are NCHS FTP zips (2023 already done by hand).
set -u
cd "$HOME/make-your-own-denominator" || exit 1

for Y in $(seq 1995 2013); do
  f="linkpe${Y}usnum.csv"
  z="${f}.zip"
  url="https://data.nber.org/linkpe/${Y}/linkpe${Y}usnum.csv.zip"
  if [ ! -f "$f" ]; then
    echo "→ ${Y}: downloading…"
    if ! curl -fsSL -o "$z" "$url"; then
      echo "  ⚠ ${Y}: download failed — recorded as absence, continuing."
      continue
    fi
    unzip -o "$z" >/dev/null 2>&1 || { echo "  ⚠ ${Y}: unzip failed"; rm -f "$z"; continue; }
  fi
  python3 gather_nber_lbid.py --csv "$f" --year "$Y"
  rm -f "$z" "$f"          # tidy: drop the ~20MB source after it's folded into the long CSV
done

echo ""
echo "=== all available NBER years folded in. Model-free schedule check across years: ==="
python3 inspect_schedule_bumps.py --quiet
echo ""
echo "(Per-year raw strips: run  python3 inspect_schedule_bumps.py  without --quiet.)"
echo "(2023 is already in your long CSV from the NCHS FTP file; 2014-2022 can be added"
echo " from NCHS FTP if you want the gap filled — those are the big period-cohort zips.)"
