# Make Your Own Denominator — reproduce it yourself

Open method. Every number on the kit page traces to a cited public source or a hashed input file. No model is
smuggled in as if the data produced it. Leads, not verdicts.

## What this is

A public, browser-based demonstration that the standard vaccine-safety engine (observed-vs-expected) works —
and that the one thing standing between it and continuous, checkable monitoring is **access to the
denominated, linked data**, which exists but is not reproducibly public.

- **The positive control** — the engine catches real, accepted signals: rotavirus → intussusception and
  MMR/MMRV → febrile seizures (with the dose-response). If it can find the real ones, its silence elsewhere
  indicts the missing data, not the method.
- **The honest null** — the same logic on 19 years of real US all-cause infant deaths (NCHS Linked
  Birth/Infant Death public-use files), with **no model, no smoothing, no threshold, years not pooled**, shows
  no sharp localized excess at the 2/4/6-month vaccination ages. It does not prove safety; it is, by
  disclosed design (see the anti-placebo limit), blind to a diffuse effect — which is the case for opening the
  linked data, not closing it.

## Run it

```
pip install requests           # only used by the NBER/NCHS pull helper

# positive control — engine catches the real signals (cited public figures)
python3 intussusception_positive_control.py

# pull 19 years of real public data and run the model-free schedule check
bash gather_all_years.sh
python3 inspect_schedule_bumps.py --quiet --exclude 2002
```

Outputs land in `out/`: `allcause_age_long.csv` (the sovereign, hash-pinned long table), derived views, a
SHA-256 manifest, and an `ABSENCES.csv` ledger of anything the open record would not release. `2002` is
auto-excluded by a built-in quality check (an age-coding artifact in that one file — flagged, not hidden).

## Data sources (primary)

- NCHS Linked Birth/Infant Death public-use files — all-cause infant deaths by single day of age.
  1995–2013 via NBER (`data.nber.org/linkpe/`); 2023 via NCHS FTP
  (`ftp.cdc.gov/.../period-cohort-linked/`). Age-at-death column `aged`/`AGEDX`.
- Positive controls: Yih, *NEJM* 2014;370:503 (PMID 24422676); Weintraub, *NEJM* 2014;370:513
  (doi:10.1056/NEJMoa1311738); Klein, *Pediatrics* 2010 (PMID 20587679); Vestergaard, *JAMA* 2004.

## The ask

Open the denominated, linked data (vaccination dates + outcome dates by age), de-identified — dates and ages,
not identities. Require reproducible signal analyses (code, pinned data, hashes). Fund the open rebuild of the
automated EHR surveillance that was built and proven in 2011 (ESP:VAERS) and shelved.

*A navigator, not medical or legal advice. Counts of reports are not rates; a correlation is not a cause.
Method: Apache-2.0 · Text: CC BY 4.0 · Meridian North / Garrison Node.*
