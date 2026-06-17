# Compute estimate — BitNet on the legal corpus

**Headline: ~41 million local BitNet tokens (order: tens of millions) to score the deep legal
corpus.** This is an *estimate* with stated assumptions, not a logged total — no single ledger
captured the cumulative figure, so it is reconstructed from the real corpus dimensions below. The
point is the order of magnitude and the provenance: this work ran **locally, deterministically,
and signed** on the milspec model — not in the cloud.

## Measured inputs (real, from the corpus)

- Corpus: U.S. Code Titles 4 & 42, deep layer (`usc_section_lookup.json`, 9.43 MB)
- **6,381 sections** across editions **1994, 2000, 2006, 2012, 2018** (+ 3 derived fields `_f/_l/_n`)
- **46,001 (section × edition) units** — the real number of things BitNet had to read and verdict
- **~8.9 M characters of statute text ≈ ~2.2 M tokens** to read the content once

## Assumptions (tune these — the estimate scales linearly)

| Knob | Value | Why |
|------|-------|-----|
| chars per token | 4 | standard rough rule |
| wrapper overhead / call | 220 tok | composer context + beacon scan + tenet checks + system preamble, per call, × 46,001 units |
| verdict output / unit | 30 tok | ternary verdict + short rationale |
| passes | 3 | routing → ternary verdict → BitNet-vs-72B disagreement precompute (per `BUILD_SHEET.md`) |

## The arithmetic

```
read content once          ~2,225,000 tok
wrapper overhead   220 × 46,001  = ~10,120,000 tok
verdict output      30 × 46,001  =  ~1,380,000 tok
--------------------------------------------------
one pass                        ~13,725,000 tok
× 3 passes                      ~41,200,000 tok   ← estimate
```

Plausible range, flexing passes (2–4) and overhead (150–300): **~25 M to ~60 M tokens.** Central
estimate **~41 M**.

## Why it matters (the contrast)

| Layer | ~Tokens | Where | Provable? |
|-------|---------|-------|-----------|
| **Deep corpus scoring** | **~41,000,000** | local BitNet (milspec) | **Yes** — deterministic, weight-attested, signable |
| This kit's prose authoring | ~28,300 | cloud (Cowork) | No |
| This kit's A/B narration run | ~622 | local BitNet (milspec) | Yes |

The sovereign, deterministic lifting — **~41 million tokens** — was done on a 2-billion-parameter
model running offline, where every verdict is byte-replayable and Beacon-signable. The cloud was
touched only for the thin narration layer (~28 K), which is exactly the part we label non-milspec
and fence behind the raw layer. **The heavy work is the cheap-to-verify work.**

*Estimate, openly. Re-run with your own knobs above. Leads, not verdicts. Not legal advice.*
