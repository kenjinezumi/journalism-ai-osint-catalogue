# USAspending.gov (custom award data)

`SUR-B2-14` · **86/100** · overall rank 71 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 24) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 5) |
| **Subcategory** | Procurement records |
| **Type** | dataset |
| **Bucket** | `proprietary-service` |
| **Maintainer** | US Department of the Treasury / Bureau of the Fiscal Service |
| **Maintenance** | Actively maintained |
| **Licence** | US federal government works are generally not subject to copyright in the United States; specific portal terms NOT verified in this survey |
| **Licence type** | Proprietary |
| **Open-source status** | Proprietary |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://www.usaspending.gov/download_center/custom_award_data) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 86/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Proprietary |
| **Exact licence (as recorded)** | US federal government works are generally not subject to copyright in the United States; specific portal terms NOT verified in this survey |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same. |
| **Restrictions** | Generally none for US government data, which is unusually favourable for republication. Confirm the portal's terms before publishing a derived dataset. |
| **Open-source status** | **Proprietary** — Hosted service or proprietary software — governed by service terms, not a software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Free. Cost is storage and compute for bulk analysis, plus entity-resolution effort. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://www.usaspending.gov/download_center/custom_award_data
- `../sources/evidence/b2-sources.md`

---

## 1. Purpose

Official US federal spending portal with searchable and bulk-downloadable award data covering contracts, grants and subawards, including recipient, agency, amount, date and product/service codes.

## Journalism / investigative use case

Establishing which US federal agencies bought surveillance and forensic technology, from whom and for how much — including the Cellebrite, Magnet Forensics and biometric-system contracts that recur in surveillance reporting. The custom download lets you extract an entire category of spending for analysis rather than clicking through records.

## 2. Audience

newsroom analyst, specialist investigator, engineer

## 3. Project type

dataset · bucket `proprietary-service`

## 4. Pros

- Authoritative primary data with recipient names, amounts and dates, downloadable in bulk — the strongest openly available procurement dataset of any jurisdiction
- Product and service codes (PSC) and NAICS classification let you isolate a technology category systematically rather than keyword-guessing
- Subaward data is included, which is how you find the integrator-to-vendor relationships that keep a surveillance supplier's name off the prime contract
- US federal government works are generally public domain, so republication and derived datasets are straightforward

## 5. Cons

- Classified and some national-security procurement is excluded or redacted, so the most sensitive surveillance purchases may simply be absent — the same structural limitation as TED
- Data quality is uneven: recipient naming is inconsistent, requiring entity resolution (rigour plus Splink) before aggregate figures are trustworthy
- Large bulk downloads are unwieldy, and the custom-download interface imposes limits that shape how you have to query
- US only, so it is irrelevant for non-US procurement questions except where a US supplier or subsidiary is involved

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the download-centre URL was verified live on 2026-11-17 (200). USAspending is widely used in US accountability journalism, and the inconsistent-recipient-naming problem is a well-known characteristic of the dataset rather than a criticism of the portal.

## 7. Assessment

Adopt it as the primary source for US surveillance procurement and plan for entity resolution as a first-class step — the names are messy enough that aggregate totals are wrong without it. For your profile the high-value technique is combining prime and subaward data: a vendor absent from prime contracts often appears as a subcontractor, and that linkage is where the story usually is. Note that absence of a contract is not evidence of no purchase, given classified procurement.

## 8. Maintenance

**Actively maintained** — Portal and download centre verified live on 2026-11-17 (200). A statutory US government service with continuous publication; maintenance is institutional rather than release-based.

## 9. Licensing

**Licence:** US federal government works are generally not subject to copyright in the United States; specific portal terms NOT verified in this survey _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same.

**Restrictions:** Generally none for US government data, which is unusually favourable for republication. Confirm the portal's terms before publishing a derived dataset.

**Licence evidence:** https://www.usaspending.gov/download_center/custom_award_data

## 10. Costs

Free. Cost is storage and compute for bulk analysis, plus entity-resolution effort. Estimate.

## 11. Privacy and data flows

Public records about agencies and corporate recipients. Your queries are visible to the portal.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Classified and some national-security procurement excluded; recipient naming requires entity resolution before aggregation

## 13. Alternatives

- [SAM.gov](SUR-B2-15.md) for entity registration and contract-opportunity data
- FPDS for the underlying federal procurement data feed
- State and municipal procurement portals for local surveillance purchases, which are often where the interesting ones are

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `docs-reviewed`

- https://www.usaspending.gov/download_center/custom_award_data
- `../sources/evidence/b2-sources.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |
| 9 | [Blacklight collector](SUR-B2-02.md) | 81 | Adopt |

---

← 70. [Outline](SUR-B3-31.md) · 72. [GDAL](OSINT-C2-20.md) →
