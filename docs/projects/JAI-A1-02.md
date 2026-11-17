# news-please

`JAI-A1-02` · **60/100** · overall rank 322 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 120) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 30) |
| **Subcategory** | News crawling and extraction |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Felix Hamborg (fhamborg) |
| **Maintenance** | Archived or discontinued |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/fhamborg/news-please) · [Documentation](https://github.com/fhamborg/news-please#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 0/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 60/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Integrated news crawler and information extractor that discovers articles from sitemaps and RSS, extracts text, title, author and date, and stores results in files, Elasticsearch or a database.

## Journalism / investigative use case

Historically the one-step answer to building a news corpus: point it at a list of outlets and get structured articles without assembling a crawler and an extractor yourself. Still the design people reach for when asked to build a news-monitoring dataset.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Integrated discovery plus extraction plus storage was genuinely convenient, which is why it became a standard recommendation in computational-journalism and media-research work
- Apache-2.0 with CommonCrawl integration, so it could build historical corpora as well as monitor forward — a capability few alternatives match
- Large community (2,493 stars) and an academic lineage with published use in media-research literature

## 5. Cons

- ARCHIVED: the GitHub API reports archived=true with the last push 2026-04-14, so it is read-only and will receive no fixes — a decisive fact that most of the material recommending it has not caught up with
- News-site structures and sitemap conventions change continuously, so an archived news crawler degrades quickly and silently (fewer articles found, not visible errors)
- No releases were ever published, so there is no version to pin even if you fork it
- Scrapy-based with an ageing dependency chain that will become harder to install

## 6. Feedback (documented)

No individual user reports verified. The decisive documented fact, established in this session: archived=true per the GitHub API on 2026-11-17, last push 2026-04-14, 2,493 stars, 10 open issues — recorded in sources/evidence/leads.md L10. This is a project still widely recommended in data-journalism teaching material that is now frozen.

## 7. Assessment

Avoid for new deployment and flag it if you see it recommended — the archival is recent enough that it has not propagated into the guidance people follow. For your profile the replacement is straightforward and arguably better: Scrapy or a sitemap crawl for discovery, trafilatura for extraction, your own storage. That is a day's work and leaves you with maintained components. Keep news-please in the catalogue precisely so the archival is visible.

## 8. Maintenance

**Archived or discontinued** — GitHub API 2026-11-17: archived=true, pushed_at 2026-04-14, no releases, 2,493 stars, 10 open issues. Archived by the maintainer — unambiguous, and the single most consequential maintenance finding in the A1 segment given how widely the project is still recommended.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None, but the code is frozen. Forking is permitted and would be the only way forward.

**Licence evidence:** https://github.com/fhamborg/news-please/blob/master/LICENSE

## 10. Costs

No fee. Not worth operating; any use means accepting fork-and-maintain responsibility.

## 11. Privacy and data flows

Crawls target sites directly from your host; storage is local or your own Elasticsearch.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Archived as of 2026-04-14 — read-only, and news-site changes will silently degrade coverage

## 13. Alternatives

- [trafilatura](JAI-A1-01.md) plus Scrapy — the recommended replacement, both actively maintained
- [Scrapy](OSINT-C1-16.md) with a sitemap spider plus your own extraction
- Media Cloud for an existing news archive rather than building your own

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/fhamborg/news-please
- `../sources/evidence/leads.md`

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

← 321. [grab-site](OSINT-C1-24.md) · 323. [VFRAME](OSINT-C2-14.md) →
