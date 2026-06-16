# navigator-kits — Meridian North public previews

Open previews of what the Meridian North evidence corpora can do. This repository is the
**public face**: facts and method in the open; the scored signal and the full corpora stay
private. Every kit is a claim-**navigator**, not a claim-engine — *leads, not verdicts.*
**Not legal or medical advice.**

## The two-layer architecture (read this first)

Each kit is built in two layers, kept deliberately separate so you always know what a machine
produced versus what a model wrote:

**1. RAW — the sovereign layer.** A controlled-token index (CSV/JSON) plus a deterministic
export (`raw/*.md`, `raw/*.json`) and the webform that queries it. No model sits in this path.
Facts, evidence grades, enforcement signals, caveat **tokens**, and primary-source pointers are
all *stored fields* — a local node, plain `grep`, or the static webform can deliver every bit of
it offline. This layer is SHA-pinned and reproducible: same index → same output, always. **This
is the part we improve over time** — richer fields, sharper tokens, more records.

**2. NARRATION — the sweep on top.** The readable six-axis study (and any prose copy) is written
by a named model *over* the raw layer. It is model-agnostic: run it on Claude, Grok, Gemini, or a
local model (Qwen / Ollama / BitNet) via each kit's `raw/NARRATION_PROMPT.md`. The narration is
**attributed and swappable** — it carries an `authored_by` stamp and is never the source of
truth. Improve the raw layer and every narration improves, whoever writes it.

```
RAW (sovereign, no model, improves over time)  ──feeds──►  NARRATION (any LLM, attributed, swappable)
   index + tokens + webform + grep + SHA                      six-axis study, prose caveats
```

Why the split matters: it keeps us honest. A reader can take the raw payload and regenerate the
prose with their own model, or trust only the sovereign layer and ignore the prose entirely. No
frontier-model polish is ever smuggled in as if `grep` produced it.

## Kits

| Kit | Topic | Source |
|-----|-------|--------|
| [`tickerforum-we-need-another-law`](kits/tickerforum-we-need-another-law/) | Antitrust enforcement gap — statutes on the books vs. prosecutions brought | Karl Denninger, *The Market Ticker*, 2026-06-14 |

Each kit folder contains: `raw/` (the sovereign payload + narration prompt), a self-contained
`tickerforum_legal_review.html` webform (data inlined — works with no server), the controlled
index under `data/`, the narrated study, figures, and a SHA-256 manifest.

## What this repo is — and is not

**Is:** self-contained kits built from **public primary sources only** (statutes, public
filings, public posts), indexed across six axes (who / what / where / when / how / why), graded,
caveated, SHA-verifiable.

**Is not:** the private engine. These kits contain **no** scored corpora, **no** change-propensity
signal, and **no** full corpus database. That is the model, and the model stays private.
*Open the method; keep the model.*

## Verify any kit

```bash
cd kits/<kit-name>
sha256sum -c MANIFEST_SHA256.txt          # check every shipped file
python3 build_raw.py                       # regenerate the raw layer deterministically
```
Each kit's webform also includes an in-browser SHA-256 verifier (runs locally).

## License

- **Method / code / webforms / raw generators:** Apache-2.0 (see `LICENSE`)
- **Text / narrated studies:** CC BY 4.0 (attributed narration layer)

*Private-first, open later — never the reverse. What is published here was chosen to be public.*
