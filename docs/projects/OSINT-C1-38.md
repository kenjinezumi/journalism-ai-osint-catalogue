# SingleFile

`OSINT-C1-38` · **90/100** · overall rank 42 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 15) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 8) |
| **Subcategory** | Single-page capture |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Gildas Lormeau |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/gildas-lormeau/SingleFile) · [Documentation](https://github.com/gildas-lormeau/SingleFile#readme) |

**Scores** — relevance 5/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 90/100**

---

## 1. Purpose

Browser extension (and CLI) that saves a complete web page as a single self-contained HTML file with all assets inlined, preserving the page exactly as rendered.

## Journalism / investigative use case

One-click preservation of a page or social post exactly as rendered in your browser, including content behind a login you legitimately hold — the fastest capture available, and the one reporters will actually use because it takes one keystroke.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Lowest-friction capture in this catalogue: one click, one portable file that opens in any browser forever with no replay software
- Captures the rendered state including authenticated pages, so it reaches content crawlers cannot
- Extremely active (release v1.38.0 on 2026-11-17, same-day push) with a very large community (22,931 stars)
- A CLI exists, so the same engine can be scripted for bulk preservation of a URL list

## 5. Cons

- Not WARC: a single HTML snapshot lacks HTTP headers, request/response records and capture provenance, so it is materially weaker evidence than a WACZ and can be edited afterwards undetectably
- Inlining assets alters the document, so the file is a faithful rendering rather than a faithful record of what was transmitted
- AGPL-3.0 matters if you redistribute a modified version or embed the engine in a product
- 99 open issues reflecting the variety of pages users try to capture; very complex pages can produce large files

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 22,931 stars with 99 open issues, release v1.38.0 published 2026-11-17 with same-day push — one of the most actively maintained tools in this catalogue. Its evidentiary limitation relative to WARC is a general property of single-file snapshots, widely discussed in archiving practice.

## 7. Assessment

Deploy it to every reporter as the default 'save this now' action, and be explicit that it is a reading copy rather than evidence of record. The combination I would standardise for your profile: SingleFile for immediate, universal capture; ArchiveWeb.page or Scoop for the pages that will carry a story. The honest trade-off is that the weaker tool is the one people will actually use, so having both and knowing which is which matters more than mandating the stronger one.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.38.0 published the same day, 22,931 stars, 99 open issues. Same-day release and push with a very large user base — exceptional maintenance for a single-maintainer project.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Captured content belongs to the original publisher.

**Restrictions:** AGPL-3.0: redistributing a modified version or offering it as a network service obliges source publication. Ordinary use as an extension is unaffected.

**Licence evidence:** https://github.com/gildas-lormeau/SingleFile/blob/master/LICENSE

## 10. Costs

Free. No infrastructure. Disk for saved files.

## 11. Privacy and data flows

The saved file is written locally with no upload by default — a clean privacy position. As with any authenticated capture, a saved logged-in page may contain personal account context, so treat files accordingly.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ArchiveWeb.page](OSINT-C1-31.md) for WARC/WACZ capture of the same authenticated content
- [monolith](OSINT-C1-39.md) for a CLI-driven equivalent in bulk
- [Scoop](OSINT-C1-36.md) where provenance metadata is required

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/gildas-lormeau/SingleFile
- https://github.com/gildas-lormeau/SingleFile/blob/master/LICENSE

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
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 41. [OONI Explorer](SUR-B1-03.md) · 43. [vLLM](JAI-A3-03.md) →
