# gdelt-doc-api

`JAI-A1-15` · **60/100** · overall rank 320 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 119) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 29) |
| **Subcategory** | News archive research |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Alex Smith (alex9smith) |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/alex9smith/gdelt-doc-api) · [Documentation](https://github.com/alex9smith/gdelt-doc-api#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 1/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 60/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python client for the GDELT 2.0 Document API, providing keyword and theme search over GDELT's global news monitoring with volume time series and article lists.

## Journalism / investigative use case

Rapid global coverage checks: establish whether a claim or event was reported anywhere worldwide and when it first appeared, across many languages — useful both for narrative-tracking and for finding the earliest report of an incident you are verifying.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Global, multilingual coverage with a simple query interface, which makes 'has anyone reported this anywhere' answerable in seconds
- Volume time series is directly useful for narrative-propagation analysis and for finding the inflection point when a story broke
- MIT licensed, tiny dependency surface, free to use with no API key for the Document API
- Earliest-mention lookup is a practical verification technique that complements reverse-image search for claim provenance

## 5. Cons

- Dormant: last push 2025-04-22 with release 1.12.0 (2025-04-03), nineteen months before this survey — a thin client over a stable API, so the risk is low but real
- GDELT's own data has well-known quirks: automated event coding and theme extraction produce noise, duplicate articles are common, and source quality is unweighted
- Dependent on GDELT's free API remaining available and unchanged; a thin client offers no protection if it does not
- Small community (234 stars) and 2 open issues — minimal support

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 234 stars with 2 open issues, release 1.12.0 (2025-04-03), last push 2025-04-22, MIT licence. GDELT's noise characteristics are widely documented in media-research literature rather than being a criticism of this client.

## 7. Assessment

Keep it for quick global coverage checks and first-mention lookups, where it is genuinely fast and useful. For your profile the discipline is to treat GDELT output as a pointer rather than a measurement: duplicate and low-quality sources inflate volume, so never publish a GDELT count as a finding — use it to find the articles, then read them. The dormancy is acceptable for a thin client, and reimplementing it against the API would take an afternoon if it breaks.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2025-04-22, latest release 1.12.0 (2025-04-03), 234 stars, 2 open issues. Nineteen months inactive. Low practical risk because it is a thin wrapper over an external API with a stable interface.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** GDELT data terms apply to the underlying archive and were not verified in this survey; article content remains the publishers' copyright.

**Restrictions:** Client unrestricted. Check GDELT's own terms before republishing data derived from it.

**Licence evidence:** https://github.com/alex9smith/gdelt-doc-api/blob/main/LICENSE

## 10. Costs

No fee; the GDELT Document API is free. Negligible compute.

## 11. Privacy and data flows

Queries go to GDELT, disclosing your search terms to that service.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Dormant client; GDELT data noise means counts are not publishable as findings

## 13. Alternatives

- Media Cloud for a curated archive with better source metadata
- Direct GDELT BigQuery access for large-scale analysis, at Google Cloud query cost
- Your own targeted corpus where precision matters more than breadth

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/alex9smith/gdelt-doc-api
- https://github.com/alex9smith/gdelt-doc-api/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 319. [Microsoft Planetary Computer](OSINT-C2-45.md) · 321. [grab-site](OSINT-C1-24.md) →
