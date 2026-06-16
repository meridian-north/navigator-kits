# RAW — TickerForum Financial Legal Corpus (antitrust enforcement slice)

> **This is the raw, sovereign layer. No narration. No model wrote these fields.**
> It is produced deterministically by `build_raw.py` from a controlled-token index.
> Feed this file to any LLM together with `NARRATION_PROMPT.md` to get a narrated study.
> The narration is attributed to whatever model runs it — it is NOT part of this raw layer.

- index_version: `tickerforum_legal_index_v1`
- source_csv_sha256: `753790be53c764a6f6c8d414665018f3f1d76d90841da3b98b2036821b33e945`
- generated: 2026-06-16 · records: 12
- source article: Karl Denninger, *The Market Ticker*, 2026-06-14 — https://market-ticker.org/akcs-www?post=255563

## Signal vocabulary (controlled)

`WARN` binding law, ~0 criminal enforcement · `CAUTION` plausible/contested, civil-only · `WATCH` pending bill, not law · `LOW` enforced/no signal · `LORE` rhetoric, quarantined

## Records (six-axis facts — mechanical projection of schema fields)

### tff-001 — Sherman Act Section 2 — monopolization, attempt, conspiracy to monopolize
- **citation:** 15 USC 2  ·  **class:** statute_enacted  ·  **signal:** WARN
- **WHO:** big_tech, healthcare_providers, pharma, online_marketplaces
- **WHAT:** Sherman Act Section 2 — monopolization, attempt, conspiracy to monopolize (15 USC 2)
- **WHERE:** antitrust_monopolization, criminal_enforcement
- **WHEN:** 1890 · VERIFIED
- **HOW:** statute_enacted · signal=WARN
- **WHY:** L1_statute_index; binding_law_in_force; felony_on_its_face; penalty_100M_corp_1M_person_10yr_per_2004_amendment; indexed_presence_is_not_a_finding_of_violation; not_legal_advice
- **primary source:** https://www.law.cornell.edu/uscode/text/15/2

### tff-002 — Criminal Section 2 enforcement record — DOJ prosecutions over time
- **citation:** DOJ Antitrust Division  ·  **class:** enforcement_record  ·  **signal:** WARN
- **WHO:** big_tech, healthcare_providers, pharma
- **WHAT:** Criminal Section 2 enforcement record — DOJ prosecutions over time (DOJ Antitrust Division)
- **WHERE:** criminal_enforcement, regulatory_capture
- **WHEN:** 2024 · VERIFIED
- **HOW:** enforcement_record · signal=WARN
- **WHY:** L1_enforcement_index; 100plus_criminal_s2_cases_in_first_80yr; last_classic_case_1977; ~45yr_gap_to_US_v_Zito_2022; recent_pleas_were_probation_not_10yr_terms; supports_near_zero_imprisonment_claim; correlation_is_not_causation
- **primary source:** https://www.americanbar.org/groups/antitrust_law/resources/magazine/2022-summer/criminal-enforcement-section-2-sherman-act/

### tff-003 — Bringing in and harboring certain aliens — harboring, transporting, employing
- **citation:** 8 USC 1324  ·  **class:** statute_enacted  ·  **signal:** WARN
- **WHO:** employers_landlords, online_marketplaces
- **WHAT:** Bringing in and harboring certain aliens — harboring, transporting, employing (8 USC 1324)
- **WHERE:** immigration_labor, criminal_enforcement
- **WHEN:** 1952 · VERIFIED
- **HOW:** statute_enacted · signal=WARN
- **WHY:** L1_statute_index; binding_law_in_force; penalties_range_1_to_20yr_by_offense; harboring_transporting_up_to_5_10yr; employing_10plus_knowing_up_to_5yr; indexed_presence_is_not_a_finding_of_violation; not_legal_advice
- **primary source:** https://www.law.cornell.edu/uscode/text/8/1324

### tff-004 — Employer / harboring enforcement record — officers and directors imprisoned
- **citation:** DOJ / DHS practice  ·  **class:** enforcement_record  ·  **signal:** WARN
- **WHO:** employers_landlords
- **WHAT:** Employer / harboring enforcement record — officers and directors imprisoned (DOJ / DHS practice)
- **WHERE:** criminal_enforcement, immigration_labor
- **WHEN:** 2025 · POINTER_ONLY
- **HOW:** enforcement_record · signal=WARN
- **WHY:** L2_enforcement_pointer; corporate_officer_imprisonment_for_employment_harboring_is_rare; most_actions_civil_fines_or_worker_focused; denominator_context_required; absence_of_prosecution_is_a_data_point_not_proof_of_innocence
- **primary source:** https://www.justice.gov/sites/default/files/criminal-hrsp/legacy/2011/01/31/1324.pdf

### tff-005 — American Innovation and Choice Online Act (AICOA) — reintroduced
- **citation:** S.4746 (119th Congress)  ·  **class:** bill_pending  ·  **signal:** WATCH
- **WHO:** big_tech
- **WHAT:** American Innovation and Choice Online Act (AICOA) — reintroduced (S.4746 (119th Congress))
- **WHERE:** antitrust_monopolization, app_store_fees, ad_tech_intermediation
- **WHEN:** 2026 · VERIFIED
- **HOW:** bill_pending · signal=WATCH
- **WHY:** L1_bill_index; introduced_not_enacted; Grassley_Klobuchar_June_2026; covers_platforms_175B_revenue_34pct_reach; failed_twice_prior; pending_is_not_law; new_law_layered_on_existing_unenforced_15USC2
- **primary source:** https://www.judiciary.senate.gov/press/rep/releases/grassley-klobuchar-introduce-bipartisan-legislation-to-lower-prices-expand-consumer-choice-and-restore-online-competition-in-the-digital-marketplace

### tff-006 — Open App Markets Act — app-store fee and sideloading bill
- **citation:** S.2153 (119th Congress)  ·  **class:** bill_pending  ·  **signal:** WATCH
- **WHO:** big_tech
- **WHAT:** Open App Markets Act — app-store fee and sideloading bill (S.2153 (119th Congress))
- **WHERE:** app_store_fees, antitrust_monopolization
- **WHEN:** 2025 · VERIFIED
- **HOW:** bill_pending · signal=WATCH
- **WHY:** L1_bill_index; introduced_not_enacted; targets_15_30pct_app_store_commission_and_payment_lock_in; prior_versions_cleared_committee_no_floor_vote; pending_is_not_law
- **primary source:** https://www.congress.gov/bill/119th-congress/senate-bill/2153/text

### tff-007 — AMERICA Act — ad-tech / Google ad-intermediation divestiture bill
- **citation:** AMERICA Act (S.1073-equiv)  ·  **class:** bill_pending  ·  **signal:** WATCH
- **WHO:** big_tech
- **WHAT:** AMERICA Act — ad-tech / Google ad-intermediation divestiture bill (AMERICA Act (S.1073-equiv))
- **WHERE:** ad_tech_intermediation, antitrust_monopolization
- **WHEN:** 2025 · POINTER_ONLY
- **HOW:** bill_pending · signal=WATCH
- **WHY:** L2_bill_pointer; targets_ad_exchange_intermediation_conflict; exact_bill_number_unconfirmed_this_pass; referenced_as_Google_ad_monopoly_bill; pending_is_not_law; verify_before_citing
- **primary source:** https://www.congress.gov/

### tff-008 — AMA CPT coding license mandate — HIPAA-designated billing standard
- **citation:** HIPAA 45 CFR 162 / CMS-AMA license  ·  **class:** agency_practice  ·  **signal:** WARN
- **WHO:** CMS_AMA, healthcare_providers
- **WHAT:** AMA CPT coding license mandate — HIPAA-designated billing standard (HIPAA 45 CFR 162 / CMS-AMA license)
- **WHERE:** licensing_mandate, copyright_lock_in, regulatory_capture
- **WHEN:** 2000 · VERIFIED
- **HOW:** agency_practice · signal=WARN
- **WHY:** L1_practice_index; CPT_copyrighted_by_AMA; HIPAA_designated_CPT_national_standard; providers_must_license_to_bill_government; Sen_Cassidy_MD_demanded_accounting_of_monopoly_profits_2025; govt_mandate_of_private_copyright_is_the_documented_fact; monopoly_characterization_is_contested
- **primary source:** https://www.cms.gov/license/ama

### tff-009 — Private-equity rollup of physician, dental and clinical practices
- **citation:** editorial claim (Denninger)  ·  **class:** claim_editorial  ·  **signal:** CAUTION
- **WHO:** healthcare_providers
- **WHAT:** Private-equity rollup of physician, dental and clinical practices (editorial claim (Denninger))
- **WHERE:** private_equity_rollup, antitrust_monopolization
- **WHEN:** 2026 · POINTER_ONLY
- **HOW:** claim_editorial · signal=CAUTION
- **WHY:** L3_editorial_claim; PE_consolidation_of_practices_is_documented_trend; characterization_as_per_se_15USC2_violation_is_author_argument_not_adjudicated; plausible_mechanism_limited_case_law; correlation_is_not_causation
- **primary source:** https://market-ticker.org/akcs-www?post=255563

### tff-010 — College tuition / medical-school capacity controls as collusion
- **citation:** editorial claim (Denninger)  ·  **class:** claim_editorial  ·  **signal:** CAUTION
- **WHO:** medical_schools, consumers
- **WHAT:** College tuition / medical-school capacity controls as collusion (editorial claim (Denninger))
- **WHERE:** antitrust_monopolization, regulatory_capture
- **WHEN:** 2026 · POINTER_ONLY
- **HOW:** claim_editorial · signal=CAUTION
- **WHY:** L3_editorial_claim; residency_slot_and_accreditation_capacity_limits_are_real; antitrust_framing_is_author_argument; some_tuition_antitrust_suits_exist_eg_568_cartel; not_adjudicated_as_to_this_claim; contested_not_dismissed
- **primary source:** https://market-ticker.org/akcs-www?post=255563

### tff-011 — Pharmaceutical and online-marketplace monopolization
- **citation:** editorial claim (Denninger)  ·  **class:** claim_editorial  ·  **signal:** CAUTION
- **WHO:** pharma, online_marketplaces
- **WHAT:** Pharmaceutical and online-marketplace monopolization (editorial claim (Denninger))
- **WHERE:** antitrust_monopolization, app_store_fees
- **WHEN:** 2026 · POINTER_ONLY
- **HOW:** claim_editorial · signal=CAUTION
- **WHY:** L3_editorial_claim; ongoing_FTC_DOJ_civil_actions_exist_eg_Amazon; criminal_15USC2_route_author_prefers_is_largely_unused; civil_vs_criminal_distinction_is_the_crux; not_adjudicated
- **primary source:** https://market-ticker.org/akcs-www?post=255563

### tff-012 — Author remedy rhetoric — extrajudicial punishment language
- **citation:** editorial rhetoric (Denninger)  ·  **class:** lore  ·  **signal:** LORE
- **WHO:** CMS_AMA
- **WHAT:** Author remedy rhetoric — extrajudicial punishment language (editorial rhetoric (Denninger))
- **WHERE:** regulatory_capture
- **WHEN:** 2026 · VERIFIED
- **HOW:** lore · signal=LORE
- **WHY:** L4_rhetoric_quarantine; hyperbolic_gallows_humor; NOT_indexed_as_a_legal_claim_or_endorsed; recorded_for_completeness_not_adjudicated; corpus_neutral_navigator_not_claim_engine
- **primary source:** https://market-ticker.org/akcs-www?post=255563
