# OONI Data (oonidata / oonipipeline)

`SUR-B1-05` · **76/100** · overall rank 198 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 54) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 14) |
| **Subcategory** | Censorship data pipeline |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Observatory of Network Interference (OONI) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause (in the oonidata/ and oonipipeline/ subpackages; the repository root has NO LICENSE file, so GitHub reports none) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ooni/data) · [Documentation](https://github.com/ooni/data#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 2/5 · licence+cost 4/5 → **weighted 76/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-3-Clause (in the oonidata/ and oonipipeline/ subpackages; the repository root has NO LICENSE file, so GitHub reports none) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | OONI measurement data published as open data; confirm current terms for redistribution. |
| **Restrictions** | Code is BSD-3-Clause per subpackage licence files, but the missing root LICENSE is a compliance-review irritant — document the subpackage paths if your legal team requires it. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Infrastructure: bulk object storage for the archive (tens to hundreds of GB depending on scope) plus an analytics store. Estimate; assumes self-hosted ClickHouse or cloud equivalent.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ooni/data

---

## 1. Purpose

Tooling to download OONI's raw measurement archive in bulk and transform it into analysis-ready observation tables, with a pipeline component targeting an analytics data store.

## Journalism / investigative use case

The tool to reach for when a story needs a country-wide or multi-year blocking dataset rather than individual measurements — for example reconstructing exactly when a set of news domains started being tampered with across every ISP in a country.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Bulk access is qualitatively different from API queries: it lets you do the longitudinal analysis that produces a 'when did this start' finding
- Derives structured observation tables, so the hard interpretive work of turning raw measurements into comparable rows is already done
- Actively developed (pushed 2026-11-16) with a current tag line (v5.1.0)

## 5. Cons

- GitHub reports no licence for this repository because the root has no LICENSE file — the BSD-3-Clause text sits in the oonidata/ and oonipipeline/ subpackages, so repo-level licence clarity is poor and a compliance reviewer will flag it
- Release objects are badly stale (v0.2.3 from 2022-11-14 against tag v5.1.0), so versioning signals are confusing
- Requires bulk object storage for the measurement archive and a ClickHouse-class analytics store for the pipeline — real infrastructure
- Tiny community (11 stars, 31 open issues); you will be reading source

## 6. Feedback (documented)

No individual user reports verified. Documented: the root-level licence gap with BSD-3-Clause text present only in subpackages (verified session 1, retained); the release-versus-tag discrepancy; 11 stars.

## 7. Assessment

Worth the effort only for a specific longitudinal story, and I would plan it as a project rather than a tool: provision storage, pull the archive for the countries and date range you need, build the observation tables, then analyse in DuckDB or ClickHouse. Resolve the licence question by citing the subpackage LICENSE files explicitly in your compliance notes — the code is BSD-3-Clause, the repository packaging is just untidy.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v0.2.3 (2022-11-14), latest tag v5.1.0, SPDX none at root, 11 stars, 31 open issues. Current commits and tag progression under institutional maintenance; release objects abandoned.

## 9. Licensing

**Licence:** BSD-3-Clause (in the oonidata/ and oonipipeline/ subpackages; the repository root has NO LICENSE file, so GitHub reports none) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** OONI measurement data published as open data; confirm current terms for redistribution.

**Restrictions:** Code is BSD-3-Clause per subpackage licence files, but the missing root LICENSE is a compliance-review irritant — document the subpackage paths if your legal team requires it.

**Licence evidence:** https://github.com/ooni/data

## 10. Costs

No fee. Infrastructure: bulk object storage for the archive (tens to hundreds of GB depending on scope) plus an analytics store. Estimate; assumes self-hosted ClickHouse or cloud equivalent.

## 11. Privacy and data flows

Pulls already-public OONI measurements to local or cloud storage; no new measurement is performed, so no risk to anyone in-country. Your download pattern is visible to OONI's storage provider.

## 12. Verdict

**Integrate**

## 13. Alternatives

- OONI measurements API for smaller, targeted queries
- Censored Planet's published BigQuery tables for an independent longitudinal source
- IODA for outage timelines rather than per-URL blocking

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/ooni/data

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

← 197. [Censored Planet data analysis pipeline](SUR-B1-09.md) · 199. [Helsinki-NLP OPUS-MT](JAI-A2-21.md) →
