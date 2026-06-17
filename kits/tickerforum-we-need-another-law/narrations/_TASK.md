# Shared narration task (identical across all models)

Every narration in this folder is the **same prompt** over the **same raw records**. Only the
model changes. This is the A/B: hold the raw layer fixed, swap the narrator, compare.

## Prompt given to each model

> You are a legal-corpus narrator. Using ONLY the raw records below, write a 2-paragraph
> plain-language summary of the antitrust "enforcement gap" finding. Rules: do not invent facts
> not in the records; distinguish "already illegal" from "successfully prosecuted"; be a
> navigator not an advisor; do not claim any named party committed a crime. End with the exact
> line: "Leads, not verdicts. Not legal advice."
>
> RAW RECORDS:
> - 15 USC 2 (Sherman Act §2): monopolizing or attempting to is a felony; penalty up to $100M
>   corp / $1M person / 10 years. signal=WARN (binding law, near-zero criminal enforcement).
> - Criminal §2 enforcement record: 100+ criminal cases in the Act's first 80 years; none from
>   1977 to 2022; the two recent cases ended in probation, not decade sentences.
> - 8 USC 1324: harboring/transporting/employing aliens, penalties 1 to 20 years;
>   corporate-officer imprisonment is rare. signal=WARN.
> - AICOA (S.4746, 2026), Open App Markets Act (S.2153, 2025), AMERICA Act (S.1060, 2025):
>   pending bills, not yet law. signal=WATCH.
> - CPT/CMS mandate: the government requires providers to license the AMA's copyrighted billing
>   codes to bill federal programs. signal=WARN.

The records are a distilled slice of `../raw/tickerforum_raw.md`. Source of truth is the raw
layer; these narrations are swept on top and attributed.
