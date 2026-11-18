# Global Fishing Watch API client

`OSINT-C2-50` · **83/100** · overall rank 115 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 35) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 17) |
| **Subcategory** | Maritime behaviour analysis |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Global Fishing Watch |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (client library) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/GlobalFishingWatch/gfw-api-python-client) · [Documentation](https://globalfishingwatch.org/our-apis/documentation) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 83/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 (client library) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Global Fishing Watch data terms apply and were NOT verified in this survey — confirm attribution and redistribution conditions before publishing derived data. |
| **Restrictions** | Client is permissive. The data terms are the unresolved item: GFW publishes data for public-interest use but with its own conditions, which must be read before republication. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Client free. API access requires a token; current access tiers and any limits were NOT verified in this survey — historically available free for research and journalism, which should be confirmed. Negligible compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/main/LICENSE
- https://github.com/GlobalFishingWatch/gfw-api-python-client
- https://globalfishingwatch.org/our-apis/documentation

---

## 1. Purpose

Python client for Global Fishing Watch APIs, providing access to processed vessel-tracking data including apparent fishing effort, vessel identity, port visits, encounters, loitering events and AIS gaps.

## Journalism / investigative use case

Maritime investigation at ocean scale: identify vessels that met at sea (encounters), loitered in a protected area, visited a sanctioned port, or went dark for a period — the behavioural events that constitute illegal fishing, sanctions evasion and trans-shipment stories, already extracted from raw AIS.

## 2. Audience

specialist investigator, newsroom analyst, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Provides derived behavioural events — encounters, loitering, AIS gaps, port visits — which is the hard analytical work already done; deriving these from raw AIS yourself is a major project
- Global coverage including satellite AIS, so it answers open-ocean questions that a local receiver cannot
- Apache-2.0 client with institutional backing from an organisation whose purpose is public-interest transparency, and actively maintained (pushed 2026-11-16)
- The AIS-gap detection is directly investigative: a vessel going dark near a sanctioned port is a lead that this data surfaces systematically

## 5. Cons

- Requires an API token and the data terms are Global Fishing Watch's, not an open licence — confirm attribution and redistribution conditions before publishing a derived dataset (terms not verified in this survey)
- The derived events are model outputs: 'apparent fishing effort' is inferred from movement patterns and can be wrong, so an event is a lead requiring corroboration rather than a finding
- Your queries disclose which vessels and areas you are investigating to GFW — an organisation with a transparency mission, but still a third party
- Tiny community (35 stars, 4 open issues) and a modest release cadence (v1.4.0, 2026-01-13), so you will be reading source

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 35 stars with 4 open issues, release v1.4.0 (2026-01-13), pushed 2026-11-16, Apache-2.0 on the client. Global Fishing Watch data has been used in published investigative reporting on illegal fishing, which is relevant context for the data's credibility, though its terms were not verified here.

## 7. Assessment

Adopt for any maritime investigation — the behavioural-event layer is genuinely hard to reproduce and this is the practical way to get it. For your profile, settle the data terms in writing before you plan to publish a derived dataset, and treat every event as a hypothesis: 'apparent fishing' and 'loitering' are inferences, and the published claim should rest on the vessel's documented behaviour plus corroboration (satellite imagery, port records, company filings), not on the classification alone.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v1.4.0 (2026-01-13), 35 stars, 4 open issues. Current commits with an institutional maintainer that operates the underlying service; small client library tracking an active API.

## 9. Licensing

**Licence:** Apache-2.0 (client library) _(SPDX verified)_

**Model / data licence:** Global Fishing Watch data terms apply and were NOT verified in this survey — confirm attribution and redistribution conditions before publishing derived data.

**Restrictions:** Client is permissive. The data terms are the unresolved item: GFW publishes data for public-interest use but with its own conditions, which must be read before republication.

**Licence evidence:** https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/main/LICENSE

## 10. Costs

Client free. API access requires a token; current access tiers and any limits were NOT verified in this survey — historically available free for research and journalism, which should be confirmed. Negligible compute.

## 11. Privacy and data flows

Queries go to Global Fishing Watch, disclosing the vessels and sea areas you are investigating. GFW's mission is transparency rather than commerce, which lowers but does not remove the concern.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Data terms and current access tiers not verified — confirm before publishing derived datasets

## 13. Alternatives

- [rtl-ais](OSINT-C2-49.md) for independent local AIS reception in a chokepoint
- Commercial satellite AIS providers for raw open-ocean data, at cost
- Deriving encounters and gaps yourself from raw AIS — substantially more work

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/GlobalFishingWatch/gfw-api-python-client
- https://globalfishingwatch.org/our-apis/documentation
- https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |

---

← 114. [CTranslate2](JAI-A2-08.md) · 116. [Browsertrix](OSINT-C1-30.md) →
