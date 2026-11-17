# Playwright

`JAI-A1-08` · **89/100** · overall rank 49 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 18) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 4) |
| **Subcategory** | Browser automation |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Microsoft |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/microsoft/playwright) · [Documentation](https://playwright.dev/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 89/100**

---

## 1. Purpose

Browser-automation framework driving Chromium, Firefox and WebKit with a unified API, auto-waiting, network interception, tracing and headless or headed operation.

## Journalism / investigative use case

Reaching the content that simple HTTP requests cannot: government portals behind JavaScript, dashboards that render client-side, document viewers that paginate via XHR, and forms that must be filled to produce a report. It is also the engine under browsertrix-crawler, shot-scraper and Crawlee.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Network interception is the underused feature for investigative work: rather than scraping rendered HTML, you can capture the JSON API calls a dashboard makes and get structured data directly
- Cross-browser support matters more than it sounds — some government portals work only in specific engines, and WebKit coverage occasionally rescues an otherwise inaccessible source
- Apache-2.0 with exceptional maintenance (v1.65.1, 2026-11-13; pushed 2026-11-17) and only 71 open issues against 100,396 stars — outstanding triage at enormous scale
- Tracing and video capture make a scraping run auditable, which is useful when you need to show how data was obtained

## 5. Cons

- Resource-heavy relative to HTTP scraping: each browser instance costs hundreds of megabytes, so large crawls need orchestration and patience
- Browser automation is detectable, and portals increasingly block it — so you may win access and lose it again, which makes a brittle dependency for ongoing monitoring
- Browser binaries are large downloads tied to Playwright versions, which complicates air-gapped and reproducible deployments
- General-purpose: it is included here for the concrete journalism use case, but most of its documentation and community are about software testing

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 100,396 stars with 71 open issues, release v1.65.1 (2026-11-13), pushed 2026-11-17, Apache-2.0. Its role in journalism tooling is verifiable from dependency relationships: browsertrix-crawler, shot-scraper and Crawlee all build on it.

## 7. Assessment

Adopt it for the specific cases that defeat plain HTTP, and resist using it where requests would do — the resource and brittleness costs are real. For your profile the highest-leverage technique is network interception: find the underlying API call a portal makes, then call that directly without the browser, which is faster, more stable and often yields cleaner data than the rendered page. Use Playwright to discover the API, not necessarily to run the collection.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.65.1 (2026-11-13), 100,396 stars, 71 open issues. Same-day commits, near-weekly releases, corporate backing, and an exceptionally low backlog for the scale.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. Note that automating access to a site may breach its terms of service — separate from the licence.

**Licence evidence:** https://github.com/microsoft/playwright/blob/main/LICENSE

## 10. Costs

No fee. Infrastructure: browser instances are memory-hungry (budget several hundred MB each) plus disk for browser binaries. For large crawls this is the dominant cost. Estimate.

## 11. Privacy and data flows

Requests originate from your host, so targets see your IP and an automatable browser fingerprint. Processing is local. Use a dedicated egress for sensitive targets.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Direct HTTP requests to the underlying API once discovered — faster and more stable
- [Crawlee](OSINT-C1-17.md) for a crawling framework that wraps Playwright with queueing and anti-blocking
- Puppeteer for a Chromium-only alternative

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/microsoft/playwright
- https://playwright.dev/
- https://github.com/microsoft/playwright/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 48. [Tella](OSINT-C3-06.md) · 50. [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) →
