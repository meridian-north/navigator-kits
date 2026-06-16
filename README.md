# Meridian North — Public Previews

Open previews of what the Meridian North evidence corpora can do. This repository is the
**public face**: facts and method in the open; the scored signal and the full corpora stay
private. Every kit here is a claim-**navigator**, not a claim-engine — *leads, not verdicts.*
**Not legal or medical advice.**

## What this repo is — and is not

**Is:** self-contained "kits" built from **public primary sources only** (statutes, public
filings, public posts). Each kit indexes a single topic across six axes (who / what / where /
when / how / why), grades its evidence, embeds caveats, and ships a SHA-256 manifest so any
output is reproducible.

**Is not:** the private engine. These kits contain **no** scored corpora, **no**
change-propensity signal, and **no** full corpus database. That is the model, and the model
stays private. *Open the method; keep the model.*

## Kits

| Kit | Topic | Source |
|-----|-------|--------|
| [`tickerforum-we-need-another-law`](kits/tickerforum-we-need-another-law/) | Antitrust enforcement gap — statutes on the books vs. prosecutions brought | Karl Denninger, *The Market Ticker*, 2026-06-14 |

Open any kit's folder and open its `tickerforum_legal_review.html` (or the kit's `index.html`)
in a browser — data is inlined, so it works with no server.

## Discipline (carried from the corpus standard)

- **No model in the result path.** Statute text is verbatim from primary sources; the SHA-256
  chain is the provenance.
- **Navigator, not advice.** Public framing stays "leads not verdicts, navigator not advice."
- **Indexed presence ≠ violation. A prosecution gap is a data point, not a verdict. Pending
  bills are not law. Editorial claims are graded, not adopted.**

## Verify any kit

```
cd kits/<kit-name>
sha256sum -c MANIFEST_SHA256.txt
```
Each kit's webform also includes an in-browser SHA-256 verifier (runs locally).

## License

- **Method / code / webforms:** Apache-2.0 (see `LICENSE`)
- **Text / study write-ups:** CC BY 4.0

*Private-first, open later — never the reverse. What is published here was chosen to be public.*
