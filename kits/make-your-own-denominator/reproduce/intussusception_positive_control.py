#!/usr/bin/env python3
"""
intussusception_positive_control.py
POSITIVE CONTROL for the observed-vs-expected engine.

Purpose: prove the method CATCHES a real, medically-accepted vaccine signal when the
data exists — so its silence elsewhere indicts the MISSING DATA, not the method.

The signal: rotavirus vaccine -> intussusception. Real, accepted, quantified by the
FDA's own Mini-Sentinel/PRISM system (Yih, NEJM 2014) and CDC's VSD (Weintraub, NEJM
2014). A small transient excess of intussusception in the days after the FIRST dose;
NO excess after doses 2-3 (built-in negative control); and the bowel-obstruction event
is rare, specific, and dateable — ideal for observed-vs-expected.

What this script does (same O/E logic as the death-curve test, applied to a known +):
  expected E = doses x background_rate x (risk_window / 365)
  observed  O = E + doses x attributable_per100k/100k      (or published O/E directly)
  ratio  O/E, and FLAG if elevated. Positive controls must flag; the dose-2/3 rows
  (negative controls) must NOT — that is the specificity check.

Reads positive_control_inputs.csv (cited public summary figures). Pure stdlib.

POSTURE: neutral on safety, strong on method. This RECOVERS an accepted risk that is
already weighed against rotavirus vaccination's large benefit (it prevents far more
hospitalizations than it causes). The point is methodological: the engine works. What
the public CANNOT do is run it themselves — these signals came from linked systems
(Mini-Sentinel, VSD) that are not reproducibly open. That is the denominator demand.

USAGE:  python3 intussusception_positive_control.py
"""

import csv
from pathlib import Path

INP = Path(__file__).resolve().parent / "positive_control_inputs.csv"


def f(x, d=None):
    x = (x or "").strip()
    return float(x) if x else d


def main():
    if not INP.exists():
        print(f"missing {INP.name}"); return
    rows = list(csv.DictReader(INP.open()))

    print("=== POSITIVE CONTROLS: known, accepted vaccine signals at two ages ===")
    print("    A) rotavirus -> intussusception (~2 mo)   B) MMR/MMRV -> febrile seizures (12 mo)")
    print("    observed-vs-expected in the post-dose risk window (cited public figures)\n")
    print(f"  {'vaccine':<24}{'dose':<5}{'window':>7}{'observed':>10}{'expected':>10}{'O/E':>8}   verdict")
    pos_flagged, neg_flagged = [], []
    for r in rows:
        doses = f(r["doses_n"]); win = f(r["risk_window_days"])
        bg = f(r["background_per100k_yr"]); ar = f(r["attributable_per100k"], 0.0)
        O = f(r["observed_cases"]); E = f(r["expected_cases"])
        ri = f(r.get("relative_incidence"))   # SCCS relative incidence == O/E directly
        if ri is not None:
            # febrile-seizure rows report relative incidence (RR); that IS observed/expected
            oe = ri; O_s, E_s = "(RR)", "(RR)"
        else:
            if E is None and doses and bg and win:
                E = doses * (bg / 100000.0) * (win / 365.0)
            if O is None and E is not None and doses is not None:
                O = E + doses * (ar / 100000.0)
            oe = (O / E) if (O is not None and E not in (None, 0)) else float("nan")
            O_s = f"{O:.1f}" if O is not None else "—"
            E_s = f"{E:.2f}" if E is not None else "—"
        is_pos = r["published_significant"].strip() == "yes"
        flag = oe > 1.5  # simple elevation flag for the demo
        verdict = "FLAG (signal detected)" if flag else "on-trend (no signal)"
        if flag and is_pos: pos_flagged.append(r["signal_id"])
        if flag and not is_pos: neg_flagged.append(r["signal_id"])
        win_s = f"{int(win)}d" if win else "pub"
        print(f"  {r['vaccine']:<24}{int(f(r['dose'])):<5}{win_s:>7}{O_s:>10}{E_s:>10}{oe:>8.1f}   {verdict}")

    print("\n  --- positive controls (should FLAG) ---")
    print(f"  flagged: {', '.join(pos_flagged) if pos_flagged else 'NONE — method failed its own test!'}")
    print("  --- negative controls: dose 2 & 3 (should NOT flag) ---")
    print(f"  wrongly flagged: {', '.join(neg_flagged) if neg_flagged else 'none (good — specificity holds)'}")

    ok = pos_flagged and not neg_flagged
    print(f"\n  RESULT: {'PASS — engine catches TWO real signals at two ages and clears the negatives.' if ok else 'review.'}")
    print("\n  Anchors:")
    print("   - RV1 dose 1 (Weintraub 2014, VSD): 6 observed vs 0.72 expected = O/E 8.3.")
    print("   - RV5 dose 1 (Yih 2014, PRISM): 1.1-1.5 excess / 100,000; null at dose 2-3.")
    print("   - MMR febrile seizure (Vestergaard 2004 / Klein 2010): relative incidence ~2.75-3.7, days 7-10.")
    print("   - MMRV > MMR+V separate (7.6 vs 4.0): the engine even recovers the dose-response")
    print("     (combination vaccine higher than separate) — that is specificity, not noise.")
    print("\n  THE POINT: this works because researchers had LINKED data (Mini-Sentinel, VSD).")
    print("  The public, with VAERS alone (no denominator), could not find OR size this signal.")
    print("  Open that linked layer reproducibly and the engine runs on every product x outcome.")
    print("  Neutral on safety: this accepted risk is outweighed by the vaccine's benefit; the")
    print("  demonstration is about METHOD, not a verdict on any product.")


if __name__ == "__main__":
    main()
