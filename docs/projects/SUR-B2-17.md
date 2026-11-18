# OpenSecrets lobbying data

`SUR-B2-17` · **78/100** · overall rank 174 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 49) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 12) |
| **Subcategory** | Lobbying records |
| **Type** | dataset |
| **Bucket** | `proprietary-service` |
| **Maintainer** | OpenSecrets (Center for Responsive Politics / Issue One) |
| **Maintenance** | Actively maintained |
| **Licence** | OpenSecrets data terms apply and were NOT verified in this survey — historically permitting non-commercial research use with attribution and requiring permission for bulk or commercial reuse |
| **Licence type** | Proprietary |
| **Open-source status** | Proprietary |
| **Software price** | **No software fee** |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://www.opensecrets.org/federal-lobbying) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 4/5 · licence+cost 3/5 → **weighted 78/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Proprietary |
| **Exact licence (as recorded)** | OpenSecrets data terms apply and were NOT verified in this survey — historically permitting non-commercial research use with attribution and requiring permission for bulk or commercial reuse |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same. Verify terms before republishing data or building a product. |
| **Restrictions** | Not verified here, and this matters: a research organisation's data terms commonly restrict bulk and commercial reuse, so a commercially operated newsroom should confirm its position before republishing OpenSecrets data as a dataset. |
| **Open-source status** | **Proprietary** — Hosted service or proprietary software — governed by service terms, not a software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** Free to read. API access and bulk data terms not verified in this survey; historically free for research use with registration. Confirm before planning.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://www.opensecrets.org/federal-lobbying
- `../sources/evidence/b2-sources.md`

---

## 1. Purpose

Cleaned, standardised and aggregated database of US federal lobbying and campaign-finance data built from official filings, with organisation profiles, issue breakdowns and an API.

## Journalism / investigative use case

The analysable version of US lobbying records: instead of reconciling inconsistent filing names yourself, you get a vendor's lobbying history aggregated under one organisation profile — which turns a week of data cleaning into an afternoon's analysis when reporting on a surveillance company's political spending.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

dataset · bucket `proprietary-service`

## 4. Pros

- Entity standardisation is the real product: OpenSecrets has already solved the name-matching problem that makes raw LDA data painful, and that is most of the work
- Organisation profiles combine lobbying with campaign-finance data, giving a fuller picture of a vendor's political activity than either dataset alone
- Long-established non-profit with a research mission, so the methodology is documented and the data is intended for exactly this use
- API access makes systematic analysis possible rather than page-by-page reading

## 5. Cons

- Secondary source: it is a cleaned derivative of official filings, so for a contested claim you should cite the underlying LDA filing and use OpenSecrets to find it
- The site returned 403 to automated requests in this survey (bot protection, not removal), so scripted access needs the API rather than scraping, and API terms were not verified here
- US federal focus, with state-level coverage thinner — so non-US and subnational surveillance-lobbying questions are out of scope
- Aggregation decisions (which subsidiaries roll up to which parent) are OpenSecrets' editorial choices, and they matter for the numbers you publish

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the federal-lobbying page returned HTTP 403 to curl on 2026-11-17, recorded as bot protection rather than unavailability. OpenSecrets data is extensively used in US political journalism, which is well established.

## 7. Assessment

Use it to find and frame, then cite the primary filing — that is the right division between a cleaned aggregate and an official record. For your profile the practical note is that the aggregation decisions are consequential: if you publish 'the company spent X on lobbying', check whether that figure includes subsidiaries and say so. Verify the current API terms before building anything, since this survey could not.

## 8. Maintenance

**Actively maintained** — Not confirmable by automated request (HTTP 403 to curl on 2026-11-17, consistent with bot protection on a live site). OpenSecrets is a long-operating research organisation publishing continuously; classification rests on that institutional record rather than on a verified fetch, hence medium confidence.

## 9. Licensing

**Licence:** OpenSecrets data terms apply and were NOT verified in this survey — historically permitting non-commercial research use with attribution and requiring permission for bulk or commercial reuse _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same. Verify terms before republishing data or building a product.

**Restrictions:** Not verified here, and this matters: a research organisation's data terms commonly restrict bulk and commercial reuse, so a commercially operated newsroom should confirm its position before republishing OpenSecrets data as a dataset.

**Licence evidence:** https://www.opensecrets.org/federal-lobbying

## 10. Costs

Free to read. API access and bulk data terms not verified in this survey; historically free for research use with registration. Confirm before planning.

## 11. Privacy and data flows

Public records about organisations and individuals in political activity. Your queries are visible to OpenSecrets.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Data reuse terms not verified — confirm before republishing as a dataset

## 13. Alternatives

- Senate LDA database for the primary filings you should cite
- LobbyFacts or EU Transparency Register data for European lobbying
- Direct FOI requests to agencies for meeting records, which reveal contact that lobbying filings summarise

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `docs-reviewed`

_Marked provisional: the evidence does not support a firm score._

- https://www.opensecrets.org/federal-lobbying
- `../sources/evidence/b2-sources.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |

---

← 173. [certstream-server](SUR-B2-10.md) · 175. [PaddleOCR / PP-StructureV3](JAI-A2-37.md) →
