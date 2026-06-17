# navigator-kits — Meridian North public previews

**▶ Live site: https://meridian-north.github.io/navigator-kits/**
That hub is the front door — open it to browse every kit. (This page is just the code behind it.)

Open previews of what the Meridian North evidence corpora can do. This repository is the public face:
facts and method in the open; the scored signal and the full corpora stay private. Every kit is a
claim-**navigator**, not a claim-engine — leads, not verdicts. **Not legal or medical advice.**

## The kits (all live)

### Pharmacovigilance & public health
| Kit | Live link |
|---|---|
| Kennedy–Miller VAERS Review | https://meridian-north.github.io/vaers-1990-2026-searchable/kennedy-miller-kit/kennedy_miller_vaers_review.html |
| 5-Minute VAERS — proof of concept | https://meridian-north.github.io/vaers-1990-2026-searchable/five-minute-vaers/ |
| White paper: *The Engine Already Exists* | https://meridian-north.github.io/vaers-1990-2026-searchable/five-minute-vaers/the-engine-already-exists.html |
| VAERS Reader (1990–2026) | https://meridian-north.github.io/vaers-1990-2026-searchable/vaers_reader.html |

### Supplements & cancer
| Kit | Live link |
|---|---|
| Supplements & Cancer Treatment | https://meridian-north.github.io/cc-cancer-corpus/ |

### Law
| Kit | Live link |
|---|---|
| Legal Reference Corpus | https://meridian-north.github.io/navigator-kits/kits/legal-reference-corpus/ |
| US Code Self-Help Portal | https://meridian-north.github.io/navigator-kits/kits/usc-time-travel-portal/ |
| SSA ↔ USC Citation Resolver | https://meridian-north.github.io/navigator-kits/kits/ssa-usc-resolver/ |
| Legal Time-Travel Navigator | https://meridian-north.github.io/navigator-kits/kits/legal-time-travel/ |
| USC Section Time-Travel Lookup | https://meridian-north.github.io/navigator-kits/kits/usc-section-lookup/ |
| USC Section Growth Dashboard | https://meridian-north.github.io/navigator-kits/kits/usc-growth-curve/ |
| TickerForum — "We Need ANOTHER Law!" | https://meridian-north.github.io/navigator-kits/kits/tickerforum-we-need-another-law/ |

*(The pharmacovigilance and supplements kits are hosted in sibling repos; the law kits live in this
repo under `kits/`. The hub links them all in one place.)*

## How the corpus kits are built — two layers, kept separate

So you always know what a machine produced versus what a model wrote:

1. **RAW — the sovereign layer.** A controlled-token index (CSV/JSON) plus a deterministic export
   and the webform that queries it. **No model sits in this path.** Facts, evidence grades, signals,
   caveat tokens, and primary-source pointers are stored fields — grep, a local node, or the static
   webform delivers every bit offline. SHA-pinned and reproducible: same index → same output, always.
2. **NARRATION — the sweep on top.** The readable six-axis study is written by a *named* model over
   the raw layer, model-agnostic (Claude / Grok / Gemini / local) via each kit's
   `raw/NARRATION_PROMPT.md`. Attributed and swappable; never the source of truth.

```
RAW (sovereign, no model, improves over time) ──feeds──► NARRATION (any LLM, attributed, swappable)
   index + tokens + webform + grep + SHA                  six-axis study, prose caveats
```

A reader can take the raw payload and regenerate the prose with their own model, or trust only the
sovereign layer and ignore the prose entirely. No frontier-model polish is ever smuggled in as if
grep produced it.

## What this repo is — and is not

- **Is:** self-contained kits built from public primary sources only (statutes, public filings, public
  posts, official datasets), indexed across six axes (who / what / where / when / how / why), graded,
  caveated, SHA-verifiable.
- **Is not:** the private engine. No scored corpora, no change-propensity signal, no full corpus
  database. That is the model, and the model stays private. **Open the method; keep the model.**

## Verify any kit

```
cd kits/<kit-name>
sha256sum -c MANIFEST_SHA256.txt   # check every shipped file (where present)
```
Each corpus webform also includes an in-browser SHA-256 verifier (runs locally).

## License
- Method / code / webforms / raw generators: **Apache-2.0**
- Text / narrated studies: **CC BY 4.0** (attributed narration layer)

*Private-first, open later — never the reverse. What is published here was chosen to be public.*
