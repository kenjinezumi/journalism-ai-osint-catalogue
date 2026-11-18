# FreshRSS

`JAI-A1-03` · **94/100** · overall rank 10 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 2) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 1) |
| **Subcategory** | Feed aggregation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | FreshRSS community |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/FreshRSS/FreshRSS) · [Documentation](https://freshrss.github.io/FreshRSS/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 94/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0: a modified instance offered to users obliges source publication. Running the release for your newsroom is unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: a small PHP host with a database — comfortably the cheapest substantial capability in this catalogue. Operating effort is low. Assumptions: a few hundred feeds, small team.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/FreshRSS/FreshRSS/blob/edge/LICENSE
- https://github.com/FreshRSS/FreshRSS
- https://freshrss.github.io/FreshRSS/

---

## 1. Purpose

Self-hosted feed aggregator supporting RSS, Atom and scraped sources, with multi-user accounts, filtering rules, full-text retrieval, labels and a REST API compatible with mobile readers.

## Journalism / investigative use case

The newsroom's monitoring backbone: hundreds of feeds — government press-release pages, court listings, regulatory bulletins, target company blogs, regional outlets — read in one place with filters that surface the handful of items that matter, and an API so a monitoring pipeline can consume the same stream.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Self-hosted means your reading list — which is a map of your editorial interests — stays private, unlike a commercial reader where it is a product dataset
- Filtering rules and labels make several hundred feeds manageable, which is the difference between a monitoring system and an unread inbox
- REST API lets a pipeline consume the same curated stream reporters read, so monitoring and automation share one source of truth
- AGPL-3.0, very actively maintained (1.30.4, 2026-10-21; pushed 2026-11-17) with a large community (16,610 stars)

## 5. Cons

- 680 open issues and a PHP application with a broad feature surface, so operating it means staying current with updates
- Feed discovery is your problem: many government and corporate pages have no feed, so RSSHub or rss-bridge is needed alongside it
- Full-text retrieval of articles whose feeds carry only excerpts works variably and can look like scraping to the publisher
- Multi-user but not collaborative: there is no shared annotation or assignment, so turning an interesting item into newsroom action happens elsewhere

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 16,610 stars with 680 open issues, release 1.30.4 (2026-10-21), pushed 2026-11-17, AGPL-3.0. A long-established self-hosted reader with a large community; the issue count reflects feature breadth and user base.

## 7. Assessment

Adopt it — a curated, self-hosted feed layer is the single highest-return piece of monitoring infrastructure a newsroom can run, and it costs almost nothing. For your profile the design that pays off is treating feeds as a shared asset: maintain the feed list in version control, use labels that map to beats, and expose the API to your own alerting so a reporter and a script see the same items. Pair with RSSHub for sources that lack feeds.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 1.30.4 (2026-10-21), 16,610 stars, 680 open issues. Same-day commits with a regular release cadence from an established community team.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified instance offered to users obliges source publication. Running the release for your newsroom is unaffected.

**Licence evidence:** https://github.com/FreshRSS/FreshRSS/blob/edge/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a small PHP host with a database — comfortably the cheapest substantial capability in this catalogue. Operating effort is low. Assumptions: a few hundred feeds, small team.

## 11. Privacy and data flows

Self-hosted, so your feed list and reading behaviour stay internal. Your server fetches the feeds, so publishers see your server rather than individual reporters — an incidental privacy benefit.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Miniflux](JAI-A1-04.md) for a lighter, more opinionated self-hosted reader
- [RSSHub](JAI-A1-05.md) or rss-bridge to generate feeds for sources that lack them
- [changedetection.io](SUR-B1-15.md) where the source has neither a feed nor a generator

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/FreshRSS/FreshRSS
- https://freshrss.github.io/FreshRSS/
- https://github.com/FreshRSS/FreshRSS/blob/edge/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 9. [ArchiveWeb.page](OSINT-C1-31.md) · 11. [geopandas](OSINT-C2-21.md) →
