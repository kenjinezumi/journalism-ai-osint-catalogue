# Crawlee

`OSINT-C1-17` · **82/100** · overall rank 128 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 40) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 14) |
| **Subcategory** | Structured web scraping |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Apify |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/apify/crawlee) · [Documentation](https://crawlee.dev/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 82/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material for the library. The Apify platform and paid proxy services operate under their own commercial terms. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Library free. Optional paid dependencies are the real cost driver: proxy providers and the Apify cloud are usage-priced (rates not verified in this survey). Self-hosted browser crawling needs more CPU and RAM than HTTP crawling — budget accordingly.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/apify/crawlee/blob/master/LICENSE.md
- https://github.com/apify/crawlee
- https://crawlee.dev/

---

## 1. Purpose

Node.js and Python crawling library with unified HTTP and browser (Playwright/Puppeteer) crawlers, automatic request queueing, proxy rotation, session management and anti-blocking features.

## Journalism / investigative use case

Collect JavaScript-heavy public pages — dynamic dashboards, infinite-scroll listings, map-based registries — that simple HTTP crawlers cannot render. For a TypeScript-centric newsroom stack it is the natural collection layer.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Browser and HTTP crawling behind one API, with automatic fallback, so you do not maintain two codebases for static and dynamic targets
- Session and proxy management is built in, which is what makes sustained collection from blocking-prone targets practical
- Apache-2.0, very actively maintained (pushed 2026-11-17, v4.0.0-rc.2 in progress, 26,475 stars) with a clean tracker
- Native TypeScript support means it fits a modern newsroom web stack without a language switch

## 5. Cons

- Engineering-heavy with no investigative UI or evidence packaging — same gap as Scrapy
- Optional paid proxy providers and the Apify cloud platform are the vendor's commercial path; using them means proxy vendors see your target URLs, a disclosure worth weighing
- Node/browser resource footprint is heavier than Scrapy's for equivalent static crawling
- Rapid major-version movement (4.0 release candidates) means pinning and migration planning are necessary

## 6. Feedback (documented)

No individual user reports verified. Documented: 26,475 stars with 145 open issues, release v3.18.2 (2026-09-29) with v4.0.0-rc.2 tagged, same-day pushes. Commercially backed by Apify, whose business model is the hosted platform — which explains both the strong maintenance and the pull toward paid services.

## 7. Assessment

The right choice if your stack is TypeScript or if the targets are genuinely dynamic; Scrapy remains better for large static collection with a Python team. For your profile the thing to watch is the commercial gravity: the anti-blocking story leads naturally to paid proxies, and routing an investigation's target URLs through a proxy vendor is a disclosure. Self-host the egress where the targets are sensitive.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v3.18.2 (2026-09-29), tag v4.0.0-rc.2, 26,475 stars, 145 open issues. Same-day commits, active major-version development, commercial backing.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material for the library. The Apify platform and paid proxy services operate under their own commercial terms.

**Licence evidence:** https://github.com/apify/crawlee/blob/master/LICENSE.md

## 10. Costs

Library free. Optional paid dependencies are the real cost driver: proxy providers and the Apify cloud are usage-priced (rates not verified in this survey). Self-hosted browser crawling needs more CPU and RAM than HTTP crawling — budget accordingly.

## 11. Privacy and data flows

Target requests go via your host or, if configured, third-party proxies — in which case the proxy vendor sees the target URLs and timing. That is a meaningful disclosure for a sensitive investigation and should be a deliberate choice.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Scrapy](OSINT-C1-16.md) for Python teams and large static crawls
- [katana](OSINT-C1-15.md) for enumeration rather than extraction
- [Playwright](JAI-A1-08.md) directly for a handful of dynamic pages where a framework is overkill

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/apify/crawlee
- https://crawlee.dev/
- https://github.com/apify/crawlee/blob/master/LICENSE.md

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |

---

← 127. [BERTopic](JAI-A2-04.md) · 129. [DuckDuckGo Tracker Radar](SUR-B2-03.md) →
