#!/usr/bin/env python3
"""
build_raw.py — emit the SOVEREIGN raw layer from the kit's index CSV.

No model, no narration, deterministic. Reads data/tickerforum_legal_index_v1.csv
and writes:
  raw/tickerforum_raw.json   machine-readable records, caveat split into token list
  raw/tickerforum_raw.md     human/LLM-readable raw dump (six-axis facts + tokens + pointers)

The raw layer is what grep + the webform + a local node can produce without a frontier
model. It is the portable payload you drop into ANY LLM (with NARRATION_PROMPT.md) to get
the narrated study. Improve THIS (richer fields, better tokens) and every narration improves.
"""
import csv, json, os, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "data", "tickerforum_legal_index_v1.csv")
OUT  = os.path.join(HERE, "raw")
os.makedirs(OUT, exist_ok=True)

# six-axis derivation is PURELY mechanical from existing schema fields — no judgment added.
AXIS = {
    "WHO":   lambda r: r["cohorts"].replace("|", ", "),
    "WHAT":  lambda r: f'{r["title"]} ({r["citation"]})',
    "WHERE": lambda r: r["mechanism_nodes"].replace("|", ", "),
    "WHEN":  lambda r: f'{r["year"]} · {r["retrieval_status"]}',
    "HOW":   lambda r: f'{r["source_class"]} · signal={r["enforcement_signal"]}',
    "WHY":   lambda r: "; ".join(t for t in r["caveat"].split(";")),
}

def load():
    with open(SRC, newline="") as fh:
        return list(csv.DictReader(fh))

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(8192), b""):
            h.update(b)
    return h.hexdigest()

def main():
    rows = load()
    src_hash = sha256(SRC)
    stamp = datetime.date.today().isoformat()

    # ---- JSON ----
    records = []
    for r in rows:
        records.append({
            "id": r["id"],
            "title": r["title"],
            "citation": r["citation"],
            "year": int(r["year"]),
            "source_class": r["source_class"],
            "id_kind": r["id_kind"],
            "verified": r["verified"],
            "retrieval_status": r["retrieval_status"],
            "mechanism_nodes": r["mechanism_nodes"].split("|"),
            "cohorts": r["cohorts"].split("|"),
            "enforcement_signal": r["enforcement_signal"],
            "caveat_tokens": [t for t in r["caveat"].split(";") if t],
            "link": r["link"] if "link" in r else "",
        })
    raw_obj = {
        "corpus": "tickerforum-financial-legal (antitrust enforcement slice)",
        "index_version": "tickerforum_legal_index_v1",
        "source_csv_sha256": src_hash,
        "generated": stamp,
        "layer": "RAW — sovereign, deterministic, no model in the result path",
        "authored_by": "deterministic generator (build_raw.py) over a controlled-token index",
        "record_count": len(records),
        "records": records,
    }
    with open(os.path.join(OUT, "tickerforum_raw.json"), "w") as fh:
        json.dump(raw_obj, fh, indent=2)

    # ---- Markdown (LLM-ready payload) ----
    L = []
    L.append("# RAW — TickerForum Financial Legal Corpus (antitrust enforcement slice)\n")
    L.append("> **This is the raw, sovereign layer. No narration. No model wrote these fields.**")
    L.append("> It is produced deterministically by `build_raw.py` from a controlled-token index.")
    L.append("> Feed this file to any LLM together with `NARRATION_PROMPT.md` to get a narrated study.")
    L.append("> The narration is attributed to whatever model runs it — it is NOT part of this raw layer.\n")
    L.append(f"- index_version: `tickerforum_legal_index_v1`")
    L.append(f"- source_csv_sha256: `{src_hash}`")
    L.append(f"- generated: {stamp} · records: {len(records)}")
    L.append(f"- source article: Karl Denninger, *The Market Ticker*, 2026-06-14 — https://market-ticker.org/akcs-www?post=255563\n")
    L.append("## Signal vocabulary (controlled)\n")
    L.append("`WARN` binding law, ~0 criminal enforcement · `CAUTION` plausible/contested, civil-only · "
             "`WATCH` pending bill, not law · `LOW` enforced/no signal · `LORE` rhetoric, quarantined\n")
    L.append("## Records (six-axis facts — mechanical projection of schema fields)\n")
    for r in rows:
        L.append(f"### {r['id']} — {r['title']}")
        L.append(f"- **citation:** {r['citation']}  ·  **class:** {r['source_class']}  ·  **signal:** {r['enforcement_signal']}")
        for ax in ("WHO", "WHAT", "WHERE", "WHEN", "HOW", "WHY"):
            L.append(f"- **{ax}:** {AXIS[ax](r)}")
        link = r.get("link", "")
        if link:
            L.append(f"- **primary source:** {link}")
        L.append("")
    md = "\n".join(L)
    with open(os.path.join(OUT, "tickerforum_raw.md"), "w") as fh:
        fh.write(md)

    print(f"raw written: {len(records)} records · source_sha={src_hash[:12]}…")
    print("  raw/tickerforum_raw.json")
    print("  raw/tickerforum_raw.md")

if __name__ == "__main__":
    main()
