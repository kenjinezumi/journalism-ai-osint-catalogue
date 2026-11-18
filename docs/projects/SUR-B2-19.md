# OpenCellID

`SUR-B2-19` · **63/100** · overall rank 299 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 73) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 19) |
| **Subcategory** | Cellular infrastructure dataset |
| **Type** | dataset |
| **Bucket** | `proprietary-service` |
| **Maintainer** | OpenCellID / Unwired Labs |
| **Maintenance** | Uncertain |
| **Licence** | Not verified in this survey — OpenCellID has historically offered data under a Creative Commons licence with API access tiers operated by Unwired Labs; confirm current terms before use |
| **Licence type** | Proprietary |
| **Open-source status** | Proprietary |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://docs.opencellid.org/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 2/5 · privacy 3/5 · usability 4/5 · licence+cost 2/5 → **weighted 63/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Proprietary |
| **Exact licence (as recorded)** | Not verified in this survey — OpenCellID has historically offered data under a Creative Commons licence with API access tiers operated by Unwired Labs; confirm current terms before use |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same. |
| **Restrictions** | Unverified and material: a CC-BY-SA-style licence would impose share-alike obligations on a derived dataset, and commercial API terms may restrict redistribution. Confirm before publishing derived data. |
| **Open-source status** | **Proprietary** — Hosted service or proprietary software — governed by service terms, not a software licence |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Additional costs** | API access tiers not verified (a free tier existed historically); bulk download avoids per-query cost |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** Not verified in this survey. Historically a free tier with API keys and paid tiers above it; confirm current pricing before planning. No software cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://docs.opencellid.org/
- `../sources/evidence/b2-sources.md`

> **Unresolved:** the price is not established by these records — this is not a statement that it is free.

---

## 1. Purpose

Crowdsourced database of cell-tower locations and identifiers (MCC, MNC, LAC, cell ID) worldwide, with an API and bulk downloads for looking up or reverse-looking-up cell identifiers.

## Journalism / investigative use case

Two uses in surveillance work: corroborating Rayhunter or SnoopSnitch anomalies against known tower infrastructure to distinguish a legitimate cell from a suspected simulator, and resolving cell identifiers found in device records or leaked location data into physical locations.

## 2. Audience

specialist investigator, engineer

## 3. Project type

dataset · bucket `proprietary-service`

## 4. Pros

- Provides the reference layer that makes cell-site anomaly detection interpretable: an unknown cell ID at a location where no tower is recorded is a meaningful signal, and without a reference database it is just noise
- Bulk downloads allow offline lookup, which matters both for privacy and for field use without connectivity
- Global crowdsourced coverage means it reaches places commercial datasets neglect
- Documentation is clear and the API is straightforward to integrate

## 5. Cons

- Crowdsourced coverage is uneven and ages: a genuine new tower may be absent, producing a false 'unknown cell' signal — so absence from OpenCellID is weak evidence of a simulator and must not be reported as detection
- Operated by a commercial company (Unwired Labs), and access terms including any free-tier limits were NOT verified in this survey — treat as unknown pending a check
- Position estimates are derived from crowdsourced observations, so tower locations carry error that matters when you are reasoning about coverage areas
- Queries disclose which cell identifiers and areas you are investigating to the operator

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: docs.opencellid.org verified live on 2026-11-17 (200). The database's crowdsourced nature and the resulting coverage variability are documented characteristics rather than criticisms.

## 7. Assessment

Integrate it as the reference layer behind any cellular-surveillance work, with the limitation stated explicitly in anything you publish: an unrecorded cell is not evidence of an IMSI catcher, because the database is incomplete. For your profile the practical approach is to download bulk data for your regions of interest so lookups are offline and private, and to treat OpenCellID agreement as corroboration while treating disagreement as a question rather than a finding. Verify the access terms before building a dependency.

## 8. Maintenance

**Uncertain** — Documentation site verified live on 2026-11-17 (200), but this survey did not verify current access terms, free-tier limits or data-update cadence. The database is crowdsourced and commercially operated; classified Uncertain because continuity and terms for a commercially operated community dataset cannot be assessed from a documentation fetch alone.

## 9. Licensing

**Licence:** Not verified in this survey — OpenCellID has historically offered data under a Creative Commons licence with API access tiers operated by Unwired Labs; confirm current terms before use _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same.

**Restrictions:** Unverified and material: a CC-BY-SA-style licence would impose share-alike obligations on a derived dataset, and commercial API terms may restrict redistribution. Confirm before publishing derived data.

**Licence evidence:** https://docs.opencellid.org/

## 10. Costs

Not verified in this survey. Historically a free tier with API keys and paid tiers above it; confirm current pricing before planning. No software cost.

## 11. Privacy and data flows

API queries disclose the cell identifiers and areas you are investigating to the operator. Bulk download and offline lookup avoids this entirely and is the configuration to prefer for sensitive work.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Licence and access terms unverified; crowdsourced coverage gaps mean an unknown cell is not evidence of a simulator

## 13. Alternatives

- National regulator tower registries where published, which are authoritative rather than crowdsourced
- Mozilla Location Service-style datasets where still available
- Rayhunter's own anomaly analysis without external corroboration, accepting weaker conclusions

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `docs-reviewed`

_Marked provisional: the evidence does not support a firm score._

- https://docs.opencellid.org/
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

← 298. [WhatWeb](SUR-B2-08.md) · 300. [Alaveteli](JAI-A1-28.md) →
