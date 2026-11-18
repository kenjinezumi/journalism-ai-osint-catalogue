# OONI Explorer

`SUR-B1-03` · **90/100** · overall rank 41 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 13) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 2) |
| **Subcategory** | Censorship measurement |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Observatory of Network Interference (OONI) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ooni/explorer) · [Documentation](https://explorer.ooni.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 90/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-3-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Displays OONI open measurement data; verify OONI's current data terms before bulk reuse. |
| **Restrictions** | None material for the code. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free to use. Self-hosting the front end is possible but pointless for most users since the data is OONI's. No cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ooni/explorer/blob/master/LICENSE
- https://github.com/ooni/explorer
- https://explorer.ooni.org/

---

## 1. Purpose

Web interface over OONI's measurement archive, providing per-country and per-network views of blocked sites and apps, anomaly and confirmed-blocking classifications, and permalinks to individual measurements.

## Journalism / investigative use case

The fastest route from 'is this site blocked in country X' to a citable, linkable public measurement. The per-measurement permalinks are usable directly as sourcing in a published story, which is rare — most network evidence cannot be cited by a reader.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Citable permalinks are the decisive feature: a reader or a lawyer can open the exact measurement your story relies on
- Requires no technical skill and no risk — browsing is read-only and runs no measurement from your machine
- Covers a long time series, so you can show when blocking started rather than only that it exists
- Maintained alongside the rest of the OONI stack with current commits

## 5. Cons

- Shows anomalies and confirmed-blocking classifications, not a verdict on who ordered a block — attribution is a reporting task, not a data lookup
- Low-coverage countries and networks can look quiet simply because nobody ran a probe there, and this absence is easy to misread as absence of censorship
- Release metadata is stale (v2.1.0 from 2020-10-20 against tag v2.6.1), so the published release objects understate maintenance
- 96 open issues; the UI is functional rather than polished for non-expert interpretation

## 6. Feedback (documented)

No individual user reports verified. Documented: the service is live and widely cited in censorship reporting and advocacy; the repository shows current commits (pushed 2026-11-17) alongside stale release objects, which is a release-hygiene artefact rather than a maintenance signal.

## 7. Assessment

Start here on any blocking question — it costs nothing and risks nobody, and often answers the question outright. The discipline to impose on yourself and your reporters: never write 'not blocked' from an empty Explorer result, because coverage gaps are the norm in exactly the countries that matter. Where coverage is missing, that is when commissioning a probe becomes worth its risk.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release object v2.1.0 (2020-10-20) but latest tag v2.6.1, 95 stars, 96 open issues. Judged on commit recency and the live service rather than release objects, which are not maintained for this front end.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** Displays OONI open measurement data; verify OONI's current data terms before bulk reuse.

**Restrictions:** None material for the code.

**Licence evidence:** https://github.com/ooni/explorer/blob/master/LICENSE

## 10. Costs

Free to use. Self-hosting the front end is possible but pointless for most users since the data is OONI's. No cost.

## 11. Privacy and data flows

Reads and displays already-public measurement data; browsing is read-only and no measurement runs from your browser. Your browsing of Explorer is visible to OONI's hosting in the ordinary way — consider Tor if even the query pattern is sensitive.

## 12. Verdict

**Adopt**

## 13. Alternatives

- OONI Probe CLI/app where coverage is missing and new measurement is justified
- IODA for outage-level rather than site-level evidence
- [Internet Society Pulse](SUR-B1-14.md) for a quick summary figure — but with unverified reuse terms

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ooni/explorer
- https://explorer.ooni.org/
- https://github.com/ooni/explorer/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 40. [EFF Rayhunter](SUR-B3-13.md) · 42. [SingleFile](OSINT-C1-38.md) →
