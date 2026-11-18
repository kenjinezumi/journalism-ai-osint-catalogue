# Scrapy

`OSINT-C1-16` · **95/100** · overall rank 4 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 2) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 1) |
| **Subcategory** | Structured web scraping |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Zyte and the Scrapy community |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/scrapy/scrapy) · [Documentation](https://docs.scrapy.org/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 95/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-3-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Collected content belongs to the source publishers. |
| **Restrictions** | None material for the framework. Scraping engages target sites' terms and, for personal data, data-protection law — both separate from the licence and both real considerations for a registry crawl. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure: a VM for long crawls; optional paid proxy or headless-browser services if the target blocks you (vendor costs not priced here). Engineer time is the main cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/scrapy/scrapy/blob/master/LICENSE
- https://github.com/scrapy/scrapy
- https://docs.scrapy.org/

---

## 1. Purpose

Mature Python framework for building web crawlers that extract structured data, with built-in request scheduling, throttling, retry handling, item pipelines and export formats.

## Journalism / investigative use case

Build repeatable bulk collection of structured public records — court listings, corporate registries, planning applications, classifieds — into datasets for analysis. This is the workhorse behind most data-journalism collection that is not a one-off script.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Handles the unglamorous parts properly: politeness delays, retries, deduplication, concurrency limits and resumable crawls — the things ad-hoc scripts get wrong and that determine whether a multi-day collection completes
- Enormous ecosystem and the best documentation in this category, so a new engineer can be productive in a day and the code is maintainable by the next person
- BSD-3-Clause and very actively maintained (release 2.20.0 on 2026-11-06, 65,442 stars) with a long track record of stability
- Item pipelines give you a clean place to validate and normalise records at collection time, which materially improves dataset quality

## 5. Cons

- Developer tool: no UI, no archiving or evidentiary output by default, so a Scrapy dataset is analysis input rather than evidence of what a page said
- No JavaScript rendering natively — dynamic sites need scrapy-playwright or a separate headless step, which adds complexity
- Learning the framework's conventions (spiders, items, middlewares) is an upfront cost that a simple requests script avoids for small jobs
- 176 open issues; large-site crawls still require hand-tuning of throttling to avoid blocking or harming the target

## 6. Feedback (documented)

No individual user reports verified in this survey, but Scrapy's use in data journalism is extensively documented in the field's teaching materials and in newsroom open-source repositories (openstates-scrapers, querido-diario and similar projects are Scrapy-based, which is verifiable from those repositories).

## 7. Assessment

Adopt as the standard for any collection you expect to run more than once. For your profile the decisive feature is resumability and throttling: a registry crawl that takes four days and can be paused is the difference between a dataset and a failed attempt. Always add a separate evidentiary capture for the specific pages a story will cite — Scrapy gives you data, not proof of what was published.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 2.20.0 (2026-11-06), 65,442 stars, 176 open issues. Regular releases over more than a decade with commercial backing (Zyte) and a broad contributor base.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** n/a. Collected content belongs to the source publishers.

**Restrictions:** None material for the framework. Scraping engages target sites' terms and, for personal data, data-protection law — both separate from the licence and both real considerations for a registry crawl.

**Licence evidence:** https://github.com/scrapy/scrapy/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure: a VM for long crawls; optional paid proxy or headless-browser services if the target blocks you (vendor costs not priced here). Engineer time is the main cost.

## 11. Privacy and data flows

Requests go from your infrastructure to the targets, and data is stored locally. The target sees your IP and pattern. For personal data in registries, your own data-protection obligations attach to the collected dataset — treat it as regulated material, not just files.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Crawlee](OSINT-C1-17.md) for a JavaScript/TypeScript-native equivalent with browser support built in
- [katana](OSINT-C1-15.md) for URL discovery rather than structured extraction
- requests plus BeautifulSoup for genuinely one-off small jobs

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/scrapy/scrapy
- https://docs.scrapy.org/
- https://github.com/scrapy/scrapy/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 3. [mitmproxy](SUR-B2-06.md) · 5. [Signal (Android client)](SUR-B3-23.md) →
