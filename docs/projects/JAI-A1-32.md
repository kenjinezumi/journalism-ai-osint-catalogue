# git-history

`JAI-A1-32` · **78/100** · overall rank 178 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 71) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 15) |
| **Subcategory** | Change analysis |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Simon Willison |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/simonw/git-history) · [Documentation](https://datasette.io/tools/git-history) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 78/100**

---

## 1. Purpose

Tool that analyses the history of a file tracked in git — typically a scraped data file committed on a schedule — and converts it into a SQLite database of versions and item-level changes.

## Journalism / investigative use case

The analysis half of git-scraping: once shot-scraper or a cron job has been committing a government dataset daily for months, git-history turns that commit log into a queryable record of every change — when a row appeared, changed value, or was quietly deleted.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Converts a git history into item-level change records, which is exactly the question journalists ask of official data: what changed, when, and what disappeared
- Completes the git-scraping pattern into something analysable, turning a monitoring habit into a dataset with provenance built in
- Apache-2.0 and composes with Datasette, so the resulting database is immediately browsable and shareable
- Small, focused tool that does one thing clearly

## 5. Cons

- Dormant-adjacent: release 0.7 and last push both 2025-12-21, nearly a year before this survey — a small tool, but its development has stopped
- Only useful if you have already been committing data on a schedule, so the value depends on a habit established months earlier — the tool cannot recover history you did not capture
- Assumes a reasonably stable file structure: a scraped file whose schema changes will produce confusing item histories
- Small community (228 stars, 21 open issues)

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 228 stars with 21 open issues, release 0.7 (2025-12-21) with the last push the same day, Apache-2.0. The git-scraping pattern it supports is documented by the maintainer and widely adopted in data journalism.

## 7. Assessment

Adopt the pattern immediately even if you use the tool later — the important action is to start committing the datasets you care about on a schedule now, because you cannot reconstruct a history you did not capture. git-history then makes that archive analysable. Its stalled development is low risk for a tool of this size, and the Datasette pairing means the output is useful to non-engineers.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2025-12-21, latest release 0.7 published the same day, 228 stars, 21 open issues. Eleven months since any activity on a small, complete tool. Classified stable-low rather than dormant given its narrow scope and minimal dependency surface.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/simonw/git-history/blob/main/LICENSE

## 10. Costs

No fee, negligible resources.

## 11. Privacy and data flows

Operates on local git repositories; no network calls. Note that if the scraped data repository is public, the monitored datasets and their history are public too.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Writing SQL against the git log yourself for bespoke change analysis
- [EDGI web-monitoring-diff](SUR-B1-21.md) for HTML page diffs rather than structured data
- [Datasette](JAI-A2-09.md) to publish the resulting change database

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/simonw/git-history
- https://datasette.io/tools/git-history
- https://github.com/simonw/git-history/blob/main/LICENSE

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

← 177. [ThreatExchange (PDQ / TMK+PDQF / vPDQ and HMA)](OSINT-C2-06.md) · 179. [ImageHash](OSINT-C2-05.md) →
