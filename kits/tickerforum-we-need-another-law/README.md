# TickerForum Financial Legal Corpus — "We Need ANOTHER Law!" Kit

A six-axis (who / what / where / when / how / why) legal-corpus kit built over Karl Denninger's
June 14, 2026 Market Ticker post [*"We Need ANOTHER Law!"*](https://market-ticker.org/akcs-www?post=255563).
It runs the article through the Meridian North legal-corpus logic: every statute, bill, and claim
is indexed, graded, caveated, and traced to a primary source.

**Posture:** neutral on the politics · strong on the statutory record · method fully open.
A claim-**navigator**, not a claim-engine. **Not legal advice.**

## The one finding (and its limits)

Denninger's structural claim checks out against the record: **the conduct Congress keeps writing
new bills to address is, in large part, already a felony under statutes on the books — and those
criminal provisions are almost never used.** Sherman Act §2 (15 USC §2) carries up to 10 years'
imprisonment; the DOJ brought 100+ criminal §2 cases in the Act's first ~80 years, then **none
from 1977 to 2022**, and the two revival cases ended in probation, not decade sentences. His
"Zero" is rhetorically rounded but substantially fair.

What the corpus **will not** do is convert that gap into a verdict. A near-zero prosecution count
is not proof that crimes went unpunished — criminal monopolization carries a far higher bar than
civil enforcement, and DOJ's historical preference for civil structural relief is a defensible
policy choice, not necessarily a failure of will. *"Already illegal" and "successfully prosecuted"
are different facts; the space between them is the whole study.* His extrajudicial-punishment
rhetoric is quarantined as `lore`, recorded but neither adopted nor endorsed.

## Contents

| File | What it is |
|------|------------|
| `STUDY_6axis_we_need_another_law.md` | The six-axis study — the substantive centerpiece |
| `tickerforum_legal_review.html` | Self-contained interactive webform (open in any browser, no server) |
| `data/tickerforum_legal_index_v1.csv` | The statute/claim index — 12 records, embedded caveats |
| `data/enforcement_gap.csv` | Backing data for Figure 1 |
| `fig1_enforcement_gap.png` | Law on the books vs. law in action |
| `fig2_one_law_chain.png` | "One law leads to another" — each bill → its dormant parent statute |
| `fig3_mechanism_crossroads.png` | Where the post's claims cluster by mechanism |
| `make_figures.py` | Deterministic figure generator (re-runs from the CSV) |
| `MANIFEST_SHA256.txt` | SHA-256 of every file — milspec replayability |

## The three graphics (in sequence)

1. **Enforcement Gap** — per statute: binding since when, criminal cases in the modern era,
   persons serving 10-year terms. The visual answer to "how many are doing 10 years?": effectively zero.
2. **One Law → Another** — each pending bill (AICOA S.4746, Open App Markets S.2153, the ad-tech
   AMERICA Act) drawn back to the existing, lightly-enforced §2 felony it layers on top of.
3. **Mechanism Crossroads** — co-occurrence of mechanism nodes; `antitrust_monopolization` and
   `criminal_enforcement` carry the load, and the CPT/CMS lane is the one where no private party
   can bring a charge.

The same charts render live inside the webform (Enforcement Gap and One Law → Another tabs).

## Enforcement-signal vocabulary

The legal analog of the cancer corpus's WARN/CAUTION/WATCH/LOW, keyed to the law-on-the-books vs.
law-in-action gap:

- **WARN** — binding law in force, conduct plausibly within reach, **criminal enforcement ~0**
- **CAUTION** — plausible violation, contested or civil-only, not adjudicated as framed
- **WATCH** — pending legislation / active scrutiny; not yet law
- **LOW** — enforced, or no signal
- **LORE** — editorial rhetoric, quarantined, not adjudicated

A signal is a reading flag, never a verdict. "WARN" means *read this gap carefully*, not *a crime
has been proven*.

## Source-class grades (loud, not silent)

`statute_enacted` > `enforcement_record` > `agency_practice` > `bill_pending` >
`claim_editorial` > `lore`. Statute text is verbatim from primary sources (Cornell LII /
uscode.house.gov); **no model sits in the result path**. Editorial claims are graded *below*
statute and never elevated to law.

## Run it

Open `tickerforum_legal_review.html` in any browser — data is inlined, so it works over
`file://` and over a shared public link with no server and no account.

## Verify

```
sha256sum -c MANIFEST_SHA256.txt        # check every file
```
The webform also includes an in-browser SHA-256 verifier (SubtleCrypto, runs locally — nothing
leaves your machine).

## Provenance & primary sources

- Article: Karl Denninger, *The Market Ticker*, 2026-06-14 — https://market-ticker.org/akcs-www?post=255563
- 15 USC §2 — https://www.law.cornell.edu/uscode/text/15/2
- 8 USC §1324 — https://www.law.cornell.edu/uscode/text/8/1324
- AICOA reintroduction (Grassley & Klobuchar, June 2026) — Senate Judiciary release
- Open App Markets Act, S.2153 (119th) — congress.gov
- AMA CPT / CMS licensing mandate — cms.gov/license/ama

*Leads, not verdicts. Not legal advice. The method is open; check it against the primary sources.*
