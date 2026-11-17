# OONI backend

`SUR-B1-04` · **75/100** · overall rank 202 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 56) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 15) |
| **Subcategory** | Censorship measurement infrastructure |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Observatory of Network Interference (OONI) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ooni/backend) · [Documentation](https://api.ooni.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 2/5 · licence+cost 5/5 → **weighted 75/100**

---

## 1. Purpose

Server-side components of the OONI system: the measurements API, the collector that receives probe submissions, and the test helpers that probes use to distinguish network interference from ordinary failure.

## Journalism / investigative use case

Data teams query the OONI measurements API to pull structured blocking counts per country, ASN and URL over time for charts and trend reporting, instead of hand-collecting from the web interface — the route from anecdote to a quantified story about press blocking.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- The measurements API is the practical deliverable for a newsroom data team: structured, filterable, open access to a decade of censorship measurement
- BSD-3-Clause and actively developed (pushed 2026-11-17), with the API documented and stable enough to build dashboards against
- Test-helper architecture is what makes OONI's blocking classifications defensible, so understanding it helps you interpret the data honestly

## 5. Cons

- Operationally heavy to self-host and not meant as a desktop tool — in practice you consume the hosted API rather than run this
- Two older repositories in this lineage are archived or dormant, so older tutorials point at dead code — a real navigation problem
- Release objects are badly stale (v1.3.6 from 2019-03-26) with 198 open issues, so the repository is hard to assess from metadata alone
- Querying the hosted API discloses your research interest to OONI's infrastructure

## 6. Feedback (documented)

No individual user reports verified. Documented: 198 open issues and release objects seven years old against current commits — a repository where metadata signals mislead and the live API is the real artefact. 60 stars.

## 7. Assessment

Treat the API as the product and this repository as its documentation. For your profile the useful work is a small internal client that pulls per-country, per-ASN blocking counts for the outlets you care about and charts them over time — that is a publishable monitoring capability built in a day. Self-hosting the backend is not something I would recommend; there is no benefit over querying OONI unless you are running an independent measurement network.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.3.6 (2019-03-26), 60 stars, 198 open issues. Current commits with abandoned release tagging; the live API's operation is the stronger evidence. Noted that sibling repositories in this lineage are archived.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** OONI measurement data is published as open data; confirm current terms for bulk redistribution.

**Restrictions:** None material.

**Licence evidence:** https://github.com/ooni/backend/blob/master/LICENSE

## 10. Costs

No fee to use the hosted API. Self-hosting would require ClickHouse/PostgreSQL-class stores and significant ops — not recommended. Estimate.

## 11. Privacy and data flows

The hosted API ingests probe submissions including ASN, network name and country and republishes them as open data. As a consumer, your queries are visible to OONI's infrastructure.

## 12. Verdict

**Integrate**

## 13. Alternatives

- OONI Data (oonidata/oonipipeline) for bulk dataset construction rather than API queries
- [OONI Explorer](SUR-B1-03.md) for one-off human lookups
- Censored Planet's published BigQuery tables for an independent measurement source

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ooni/backend
- https://api.ooni.io/
- https://github.com/ooni/backend/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |

---

← 201. [news-homepages](JAI-A1-31.md) · 203. [OWASP Amass](OSINT-C3-22.md) →
