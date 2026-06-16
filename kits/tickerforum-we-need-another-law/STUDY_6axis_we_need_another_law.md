---
title: "\"We Need ANOTHER Law!\" — A Six-Axis Legal-Corpus Study"
subtitle: "Who / What / Where / When / How / Why — a claim-navigator, not a claim-engine"
source_article: "Karl Denninger, The Market Ticker, 2026-06-14, in Corruption — https://market-ticker.org/akcs-www?post=255563"
corpus: meridian-north legal reference corpus (antitrust / enforcement slice)
posture: neutral on the politics · strong on the statutory record · method fully open
status: L1 — statute & enforcement index · June 2026
license: "Text: CC BY 4.0 · Code: Apache-2.0"
caveat: "not legal advice — indexed presence of a statute is not a finding of violation — a prosecution gap is a data point, not a verdict — pending bills are not law — editorial claims are graded, not adopted"
narration_layer: true
authored_by: "claude (frontier model) — this prose is a narration sweep, not the sovereign index"
raw_source: "raw/tickerforum_raw.md (deterministic, controlled-token index — the source of truth)"
note: "The facts, grades, and caveat tokens come from the raw index; this write-up is prose over them. Regenerate with any model via raw/NARRATION_PROMPT.md."
---

# "We Need ANOTHER Law!"

## A six-axis legal-corpus study

This is a navigation aid for a contested argument, not an endorsement of it. Karl Denninger's
June 14, 2026 Market Ticker post makes one structural claim and wraps it in heated rhetoric.
This study separates the two. The structural claim is testable against the statutory record:
**the conduct Congress keeps proposing "new laws" to address is, in large part, already
illegal under statutes on the books — and those statutes carry criminal penalties that are
almost never used.** The rhetoric — including a line calling for public executions — is
recorded at the bottom of the index as quarantined `lore`, neither adopted nor laundered into
a claim.

Every statute this study touches is graded, caveated, and traceable to a primary source.
Where the record earns a strong statement about *what the law says*, this study makes one.
It makes no statement about whether any specific company or person has violated any law,
because that is a question for a court, not a corpus — and saying otherwise would be the exact
category error the corpus exists to prevent.

The whole post turns out to be a clean teaching case for one idea: **a statute that is never
criminally enforced and a problem that gets a fresh bill every session are two faces of the
same gap.** That idea cuts in every direction. It is why "we need another law" can be both a
fair political move *and* an admission that the existing law went unused. It is also why a
near-zero prosecution count is not, by itself, proof that no crime occurred — absence of
enforcement and absence of violation are different facts, and the corpus refuses to collapse
them.

---

## WHO — the actors and their standing

The **author** is Karl Denninger, a long-running financial-and-political commentator writing
in his "Corruption" category. His standing is that of an informed critic, not a party or a
prosecutor; his assertions are indexed as `claim_editorial`, graded below statute and
enforcement record.

The **legislative actors** are Senators **Chuck Grassley** and **Amy Klobuchar**, who
reintroduced the American Innovation and Choice Online Act in June 2026, alongside companion
measures aimed at Apple's app-store fees and Google's ad-tech intermediation. The **opinion
piece** Denninger cites and attacks is by Mike Davis (Fox News opinion), whose subtitle
frames a "hidden tax" on online shopping carts.

The **named targets** of the underlying laws are not individuals but *cohorts*: large online
platforms (big_tech), consolidated health-care providers and the private-equity firms buying
them, pharmaceutical manufacturers, employers and landlords, medical schools, and — uniquely —
the government itself, via the **CMS / AMA** coding arrangement. In a legal corpus, "who" is
also *who has standing to bring a charge*. For the criminal statutes in play, that party is the
United States (DOJ) — which is precisely why Denninger's complaint lands on the executive: the
party with standing to prosecute is the party he says will not.

A note the corpus records but does not adjudicate: Denninger is an advocate with a known
worldview, and the piece is polemical. That is metadata, not disqualification. The narrow
statutory question — *is this conduct already illegal, and how often is the criminal provision
used?* — does not depend on his framing and can be checked independently.

## WHAT — the objects of the dispute

There are three distinct kinds of object here, and conflating them is the most common error the
post invites:

**1. Binding statutes already in force.** The centerpiece is **Sherman Act §2, 15 USC §2**
(record `tff-001`), which makes it a *felony* to "monopolize, or attempt to monopolize, or
combine or conspire to monopolize." Denninger quotes the penalty verbatim and correctly:
up to **$100,000,000 for a corporation, $1,000,000 for an individual, or 10 years'
imprisonment** — the figures set by the Antitrust Criminal Penalty Enhancement and Reform Act
of 2004. The second binding statute is **8 USC §1324** (`tff-003`), the harboring/transporting/
employing-aliens provision, whose penalties range from one to twenty years depending on the
offense. Both are real, in force, and not struck as unconstitutional — exactly as the post says.

**2. Bills that are *not* law.** AICOA (`tff-005`, S.4746), the Open App Markets Act
(`tff-006`, S.2153), and the ad-tech "AMERICA Act" (`tff-007`) are *introduced, not enacted*.
The corpus flags these `bill_pending / WATCH`. This is the heart of the post's title: each is a
proposed new law aimed at conduct the §2 felony arguably already reaches.

**3. A government practice.** The **AMA CPT / CMS licensing mandate** (`tff-008`) is neither
statute nor bill but an *arrangement*: HIPAA designated the AMA's copyrighted CPT code set as
the national billing standard, so any provider who bills a federal program must license a
private party's copyright. This is the post's strongest specific example and it is well
documented — Senator Bill Cassidy, M.D., demanded an accounting of the AMA's "monopoly"
profits in 2025. The *fact* (a government mandate to license a private copyright) is solid; the
*characterization* (that this is a prosecutable monopoly) is contested and indexed as such.

## WHERE — the mechanism nodes

"Where" in this corpus is not geography; it is the **place in the legal machinery** where each
claim lives. Six nodes carry the entire post:

- **antitrust_monopolization** — the §2 felony and every "monopoly" framing downstream of it.
- **criminal_enforcement** — the gap node: where a statute's *teeth* (indictment, conviction,
  prison) either bite or do not. This is the node the entire post is really about.
- **licensing_mandate / copyright_lock_in** — the CPT/CMS mechanism: monopoly created and
  *enforced by the government itself*, which Denninger correctly notes is the one place where
  "nobody can actually bring a charge."
- **private_equity_rollup** — the consolidation mechanism behind the health-care claims.
- **app_store_fees / ad_tech_intermediation** — the specific Big-Tech conduct the pending bills
  target.
- **immigration_labor** — the §1324 mechanism, included by the author as a parallel case of an
  unused criminal statute.

The mechanism map is what makes the "one law leads to another" graphic possible: every pending
bill in the index connects back to an existing, lightly-enforced statute through one of these
nodes.

## WHEN — the timeline

The statutes are old; the enforcement is new or absent. **15 USC §2** dates to **1890**; its
criminal use has a sharp shape. The DOJ brought **100-plus criminal §2 cases in the Act's first
~80 years**, with the last classic prosecution in **1977** — then **nothing for roughly 45
years** until *United States v. Zito* (2022) and a second guilty plea in 2024 (`tff-002`).
Crucially, those two recent cases ended in **probation-level resolutions, not decade-long
sentences**. So Denninger's pointed questions — "how many people are doing or have done 10
years?" and "how many criminally charged in the last fifty?" — are answered by the record as
**effectively zero on the 10-year sentence**, and **very nearly zero on criminal charges** until
the 2022 revival. The post's "Zero" is rhetorically rounded but substantially correct.

**8 USC §1324** dates to **1952**; criminal exposure for *corporate officers and directors* of
employers (as opposed to smugglers or the workers themselves) is rare. **AICOA** was first
introduced in 2021, failed twice, and was **reintroduced June 2026** — the news hook for the
post. The throughline: the binding law is decades old and dormant; the proposed replacements
are fresh each session.

## HOW — evidence class and the enforcement-signal vocabulary

Statute text is shown verbatim from primary sources (Cornell LII / uscode.house.gov); no model
sits in the result path. Each record carries a **source_class** grade —
`statute_enacted` > `enforcement_record` > `agency_practice` > `bill_pending` >
`claim_editorial` > `lore` — so the reader always knows whether they are looking at law, a
prosecution statistic, a government practice, a proposed bill, the author's argument, or his
rhetoric.

Interaction-style **enforcement signals** (the legal analog of the cancer corpus's
WARN/CAUTION/WATCH/LOW) are keyed to the gap between law-on-the-books and law-in-action:

- **WARN** — binding law in force; conduct plausibly within reach; **criminal enforcement at or
  near zero**. (`15 USC §2`, `8 USC §1324`, the CPT/CMS mandate.)
- **CAUTION** — plausible violation, contested or civil-only enforcement, not adjudicated as the
  author frames it. (PE rollups, tuition/capacity, pharma & marketplaces.)
- **WATCH** — pending legislation or active scrutiny; not yet law.
- **LOW** — enforced, or no signal.
- **LORE** — editorial rhetoric, quarantined, not adjudicated.

A signal is a *reading flag*, never a verdict. "WARN" means *read this gap carefully*, not
*a crime has been proven*.

## WHY — the gap, named honestly

The post's "why" is its real payload, and it deserves a fair hearing **and** a fair rebuttal,
because contested ≠ dismissed.

**The author's case (steelmanned):** If conduct is already a felony and Congress responds to
that conduct by proposing *another* law rather than prosecuting under the existing one, then the
new bill is theater — it signals action while leaving the dormant criminal statute dormant. The
CPT/CMS example sharpens this to its strongest point: here the government does not merely fail to
prosecute a monopoly, it *mandates and enforces one*, which no private antitrust suit can easily
reach. On the bare statutory record, these observations are largely accurate.

**The counter-case the corpus is obligated to record:** A near-zero criminal count is **not**
proof that crimes went unpunished. Criminal §2 monopolization requires proving specific intent
and willful acquisition of monopoly power beyond a reasonable doubt — a far higher bar than the
civil standard, which is why DOJ has historically routed monopoly cases through **civil**
enforcement (structural relief, injunctions) rather than indictment. "Zero people doing 10
years" may reflect a deliberate, defensible prosecutorial policy choice as much as a failure of
will. Likewise, the PE-rollup, tuition, and pharma claims describe **real consolidation trends**
but assert a *per se criminal* characterization that no court has adjudicated. And new
legislation is not always redundant: AICOA and the app-store bill create **conduct rules and
private/agency rights of action** that a §2 criminal case does not, lowering the proof burden
rather than duplicating it.

Both readings fit the same facts. The corpus does not pick a winner. It does insist on the one
distinction that makes the argument legible: **"already illegal" and "successfully prosecuted"
are different claims, and the space between them is exactly the gap worth studying.**

---

## Quarantine note — the rhetoric (record `tff-012`)

The post contains a passage calling for officials at CMS, Congress, and the AMA to be "convicted
and executed on the National Mall." This is indexed as `lore / LORE`, **quarantined**: recorded
for completeness, **not** adopted as a claim, **not** endorsed, and **not** treated as part of
the legal argument. A neutral claim-navigator records that the language exists and marks it as
hyperbolic rhetoric outside the statutory record. Extrajudicial punishment has no place in the
index except as an artifact of the source, flagged as such.

---

## What this study does and does not do

It **does**: confirm the two cited statutes are real, in force, and quoted accurately; confirm
the criminal-enforcement record is sparse to the point that the author's "Zero" is substantially
fair; confirm the pending bills are not law; confirm the CPT/CMS mandate is a documented
government-enforced licensing arrangement under active Senate scrutiny.

It **does not**: conclude that any named company or person has committed a crime; endorse the
author's remedy or rhetoric; or treat a prosecution gap as a verdict in either direction.

*Leads, not verdicts. Not legal advice. The method is open; check it against the primary
sources linked in the index.*
