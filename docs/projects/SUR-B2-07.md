# webappanalyzer

`SUR-B2-07` · **71/100** · overall rank 261 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 66) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 14) |
| **Subcategory** | Technology fingerprinting |
| **Type** | dataset |
| **Bucket** | `verified-oss` |
| **Maintainer** | Enthec (community continuation of Wappalyzer's open-source line) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (community continuation licensing — verify the repository licence file for your records) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/enthec/webappanalyzer) · [Documentation](https://github.com/enthec/webappanalyzer#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 71/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (community continuation licensing — verify the repository licence file for your records) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | The fingerprint ruleset is the deliverable; check its terms before redistributing it as a dataset. |
| **Restrictions** | Permissive as published; confirm from the repository before embedding the ruleset in a distributed product, since the lineage from a formerly commercial project warrants a check. |
| **Open-source status** | **Open source** — Open data licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Negligible — it is a data repository. Cost is building or adopting a detection engine.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/enthec/webappanalyzer
- `../sources/recovered/cat/consolidate.py`

---

## 1. Purpose

Maintained ruleset identifying the technologies behind a website — frameworks, analytics, CDNs, CRM and marketing platforms — continuing the open fingerprint database after Wappalyzer's open-source version was discontinued.

## Journalism / investigative use case

Establishing which commercial services a government or company website runs on, which is how you show that a state agency processes citizen data through a foreign CRM or that a propaganda network shares a single obscure analytics platform — the technology stack is both a privacy story and a network-attribution signal.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

dataset · bucket `verified-oss`

## 4. Pros

- Technology fingerprinting serves two distinct investigative purposes at once: documenting third-party data processing, and linking apparently unrelated sites that share unusual infrastructure
- Community continuation of a discontinued commercial open-source project, so the fingerprint database remains usable without a vendor subscription — a genuine rescue
- Plain ruleset data rather than a service, so you can apply it in your own pipeline and keep the analysis private
- Maintained with current updates and an identifiable steward (Enthec)

## 5. Cons

- It is a ruleset, not a tool: you need a detection engine to apply it, so there is integration work before you get results
- Fingerprint rules produce false positives and miss in-house or unusual technologies, so attribution of a shared platform should be verified by another signal before publication
- Community continuations carry continuity risk — the original line was discontinued once, and this is a smaller effort than the commercial product
- Technology detection from the client side sees only what the page exposes, so server-side processing arrangements remain invisible

## 6. Feedback (documented)

No individual user reports verified in this survey. The relevant documented context is the lineage: Wappalyzer's open-source version was discontinued and this is the community continuation, which session 1 recorded in its FORKS map and which this session retained. Maintenance was verified from the repository metadata.

## 7. Assessment

Integrate it as the fingerprint database behind whatever detection you run, and treat its output as a lead. For your profile the more interesting use is the second one: shared unusual infrastructure across several sites is a strong hypothesis of common operation, which is how disinformation-network attribution often starts — but confirm with registration data, certificate overlap or analytics identifiers before publishing a link.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as a live, non-archived repository receiving updates, maintained by Enthec as the community continuation of Wappalyzer's discontinued open-source fingerprint database. Maintenance here means ruleset updates rather than software releases, so cadence is assessed on commit activity.

## 9. Licensing

**Licence:** MIT (community continuation licensing — verify the repository licence file for your records) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** The fingerprint ruleset is the deliverable; check its terms before redistributing it as a dataset.

**Restrictions:** Permissive as published; confirm from the repository before embedding the ruleset in a distributed product, since the lineage from a formerly commercial project warrants a check.

**Licence evidence:** https://github.com/enthec/webappanalyzer

## 10. Costs

No fee. Negligible — it is a data repository. Cost is building or adopting a detection engine.

## 11. Privacy and data flows

Applying the ruleset locally keeps your analysis private; the detection requests themselves are visible to the target sites.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [WhatWeb](SUR-B2-08.md) for a self-contained fingerprinting CLI
- [SiteOne Crawler](OSINT-C1-19.md) for a report-oriented technology inventory
- [AnalyticsRelationships](SUR-B2-09.md) specifically for linking sites via shared analytics identifiers

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/enthec/webappanalyzer
- `../sources/recovered/cat/consolidate.py`

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

← 260. [overpass-turbo](OSINT-C2-24.md) · 262. [MinerU](JAI-A1-11.md) →
