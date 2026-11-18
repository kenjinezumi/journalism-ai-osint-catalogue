# SAM.gov

`SUR-B2-15` · **73/100** · overall rank 239 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 62) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 13) |
| **Subcategory** | Procurement records |
| **Type** | dataset |
| **Bucket** | `proprietary-service` |
| **Maintainer** | US General Services Administration |
| **Maintenance** | Actively maintained |
| **Licence** | US federal government works are generally not subject to copyright in the United States; portal terms and API usage conditions NOT verified in this survey |
| **Licence type** | Proprietary |
| **Open-source status** | Proprietary |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://sam.gov/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 3/5 · usability 3/5 · licence+cost 5/5 → **weighted 73/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Proprietary |
| **Exact licence (as recorded)** | US federal government works are generally not subject to copyright in the United States; portal terms and API usage conditions NOT verified in this survey |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same. |
| **Restrictions** | Not verified here. API access conditions and any registration requirements should be checked before building a monitoring pipeline. |
| **Open-source status** | **Proprietary** — Hosted service or proprietary software — governed by service terms, not a software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Free. API access may require registration. Infrastructure only if you build monitoring. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://sam.gov/
- `../sources/evidence/b2-sources.md`

---

## 1. Purpose

Official US system for award management: entity registrations for organisations doing business with the federal government, contract opportunities, exclusions (debarment) and assistance listings, with APIs and bulk extracts.

## Journalism / investigative use case

Resolving who a surveillance supplier actually is: the entity registration gives legal name, address, ownership and business-size declarations, which is how you connect a contract award to a corporate structure — and the exclusions list tells you whether a vendor has been debarred.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

dataset · bucket `proprietary-service`

## 4. Pros

- Entity registration data links a contracting name to a legal entity with an address and identifiers, which is the bridge between procurement records and corporate-registry research
- Contract-opportunity notices show what agencies are about to buy, so you can report a surveillance procurement before it is awarded — considerably more valuable than reporting it afterwards
- Exclusions (debarment) records are a direct accountability signal about a vendor's standing
- Free, official and API-accessible, so monitoring is possible rather than only searching

## 5. Cons

- Registration and API access increasingly require accounts and, for some data, approval — which creates a record of your interest and can be a barrier for a non-US organisation
- The interface is bureaucratic and the data model (UEI, CAGE codes, NAICS) takes learning before queries are productive
- Self-declared registration data, so ownership and business-size declarations are the vendor's own claims and need verification against registries
- US only, and the ownership detail is thinner than a proper corporate registry — it identifies the entity rather than mapping its structure

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: sam.gov verified live on 2026-11-17 (200). SAM.gov is the mandatory registration system for US federal contractors, which is what makes its entity data authoritative for that purpose.

## 7. Assessment

Use it as the entity-resolution layer alongside USAspending rather than as a standalone source — USAspending tells you what was bought, SAM.gov tells you who the seller legally is, and together they support a nameable story. For your profile the opportunity notices are the underused half: a standing watch on relevant NAICS and keyword terms surfaces surveillance procurement at the solicitation stage, which is both earlier and more newsworthy than an award.

## 8. Maintenance

**Actively maintained** — Portal verified live on 2026-11-17 (200). A mandatory statutory US government system under continuous operation; maintenance is institutional.

## 9. Licensing

**Licence:** US federal government works are generally not subject to copyright in the United States; portal terms and API usage conditions NOT verified in this survey _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same.

**Restrictions:** Not verified here. API access conditions and any registration requirements should be checked before building a monitoring pipeline.

**Licence evidence:** https://sam.gov/

## 10. Costs

Free. API access may require registration. Infrastructure only if you build monitoring. Estimate.

## 11. Privacy and data flows

Public records about organisations. Registering for API access creates an identifiable account, which discloses your organisation's interest — consider how that account is attributed.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Some data and API access require registration, creating a record of your interest

## 13. Alternatives

- USAspending for the award data itself
- State corporate registries and OpenCorporates for genuine ownership structure
- FPDS for the raw federal procurement feed

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `docs-reviewed`

- https://sam.gov/
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

← 238. [ProofMode](SUR-B3-32.md) · 240. [NVIDIA NeMo Speech](JAI-A2-32.md) →
