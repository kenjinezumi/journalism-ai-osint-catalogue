# trafilatura

`JAI-A1-01` · **91/100** · overall rank 36 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 12) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 2) |
| **Subcategory** | Article text extraction |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Adrien Barbaresi (adbar) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/adbar/trafilatura) · [Documentation](https://trafilatura.readthedocs.io/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 91/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. Extracted article text remains the publishers' copyright — a republication question, not a licence one. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU-only and fast; negligible infrastructure for tens of thousands of articles. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/adbar/trafilatura/blob/master/LICENSE
- https://github.com/adbar/trafilatura
- https://trafilatura.readthedocs.io/
- `../sources/evidence/leads.md`

---

## 1. Purpose

Python library and CLI that downloads web pages and extracts the main text, metadata, comments and publication dates, stripping navigation and boilerplate, with output to text, XML, JSON and TEI.

## Journalism / investigative use case

The extraction layer under any news-monitoring or narrative-tracking pipeline: fetch thousands of articles from a list of outlets and get clean text plus a reliable publication date, which is what makes 'how did this claim propagate across these fifty sites' answerable at all.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Publication-date extraction is the underrated feature and often the hardest part: narrative-propagation analysis is worthless without reliable dates, and trafilatura handles the messy real-world cases better than readability-style extractors
- Benchmarked against competing extractors by its own maintainer with published methodology, so quality claims are traceable rather than asserted
- Apache-2.0, actively maintained (v2.3.1, 2026-10-06; pushed 2026-11-17) with a clean tracker (57 open issues against 7,144 stars)
- Pure Python with a CLI, so it works both in a pipeline and for one-off extraction, and runs anywhere including air-gapped

## 5. Cons

- Extraction is heuristic: unusual layouts, paywalled stubs and JavaScript-rendered articles produce partial or empty results, so a pipeline needs failure handling and spot-checking rather than blind trust
- No JavaScript rendering, so dynamically loaded articles need a browser step (Playwright) before extraction
- Comment extraction quality varies a lot by site, and comments are often where the interesting material is
- It extracts; it does not crawl or schedule, so you still need Scrapy or a feed reader around it

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 7,144 stars with 57 open issues, release v2.3.1 (2026-10-06), pushed 2026-11-17, Apache-2.0. Notably, it is the maintained alternative to fhamborg/news-please, which this session confirmed is ARCHIVED (archived=true, last push 2026-04-14) despite still appearing in data-journalism recommendations.

## 7. Assessment

Adopt it as your default article extractor — and specifically in place of news-please, which is archived and still widely recommended. For your profile the combination that works is a feed reader or sitemap crawl for discovery, trafilatura for extraction, and a stored raw copy alongside the extracted text so you can re-extract when the heuristics improve or a failure is discovered. Log extraction failures explicitly rather than letting empty strings into the corpus.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v2.3.1 (2026-10-06), 7,144 stars, 57 open issues. Same-day commits with a 2.x release line and a single engaged academic maintainer with a long track record.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. Extracted article text remains the publishers' copyright — a republication question, not a licence one.

**Licence evidence:** https://github.com/adbar/trafilatura/blob/master/LICENSE

## 10. Costs

No fee. CPU-only and fast; negligible infrastructure for tens of thousands of articles. Estimate.

## 11. Privacy and data flows

Fetches pages directly from your host, so target sites see your requests. Processing is local. For monitoring a hostile outlet, use a dedicated egress.

## 12. Verdict

**Adopt**

## 13. Alternatives

- mozilla/readability for a JavaScript-ecosystem extractor
- [news-please](JAI-A1-02.md) — AVOID, archived as of 2026-04-14
- [Playwright](JAI-A1-08.md) plus trafilatura where articles are JavaScript-rendered

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/adbar/trafilatura
- https://trafilatura.readthedocs.io/
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 35. [ShadowFinder](OSINT-C2-17.md) · 37. [x-ray](JAI-A4-23.md) →
