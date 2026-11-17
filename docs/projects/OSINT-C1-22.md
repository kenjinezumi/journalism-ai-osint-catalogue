# Heritrix 3

`OSINT-C1-22` · **85/100** · overall rank 86 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 27) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 11) |
| **Subcategory** | Archival web crawling |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Internet Archive |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (GitHub API reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/internetarchive/heritrix3) · [Documentation](https://heritrix.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 85/100**

---

## 1. Purpose

The Internet Archive's production archival crawler: a Java system for large-scale, politeness-respecting WARC crawls with fine-grained scope control and a web operator interface.

## Journalism / investigative use case

Large-scale archival crawls of whole domains where the capture must be WARC-based and defensible — for example preserving an entire ministry site, with request and response headers intact, before an anticipated purge.

## 2. Audience

engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- WARC output with full request/response fidelity is the evidentiary gold standard, and Heritrix is the reference implementation used by national libraries and the Internet Archive itself
- Scope control and politeness configuration are unmatched, which matters when crawling a large public-sector domain you must not degrade
- Actively maintained (release 3.18.0, 2026-10-06; pushed 2026-11-17) with a small backlog for a project of this size (44 open issues)
- Institutional provenance means your capture methodology can be described in terms an archivist or a court would recognise

## 5. Cons

- Steep learning curve: the Spring-based configuration model and the operator UI are unlike anything else in this catalogue, and a first successful crawl takes real effort
- Weak on dynamic and JavaScript-dependent content — it captures what a non-executing fetcher sees, so modern single-page portals come out hollow; browsertrix-crawler is the right tool there
- Java plus substantial storage, and WARC collections need an index (OutbackCDX) and a replay front end (pywb) before anyone can read them — the full stack is three components
- GitHub reports SPDX NOASSERTION despite Apache-2.0, so licence records need the file reference

## 6. Feedback (documented)

No individual user reports verified in this survey. The institutional usage evidence is strong and verifiable: Heritrix is the Internet Archive's own crawler and is used across the IIPC web-archiving community. 3,351 stars, 44 open issues, release 3.18.0 (2026-10-06).

## 7. Assessment

The right choice for domain-scale archival capture where defensibility matters, and over-engineered for anything smaller. For your profile I would reserve it for a planned preservation project — an at-risk government domain, a complete site before litigation — and use browsertrix-crawler for social and dynamic material. Budget for the whole stack: Heritrix to crawl, OutbackCDX to index, pywb to serve, or the collection is unusable by reporters.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 3.18.0 (2026-10-06), SPDX NOASSERTION (Apache-2.0 per repository), 3,351 stars, 44 open issues. Current releases and commits under Internet Archive stewardship with a web-archiving community behind it.

## 9. Licensing

**Licence:** Apache-2.0 (GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Captured content belongs to the original publishers.

**Restrictions:** None material. Confirm the licence file reference for compliance records given the SPDX gap.

**Licence evidence:** https://github.com/internetarchive/heritrix3

## 10. Costs

No fee. Infrastructure estimate: a JVM host plus substantial storage — WARC collections are large (expect the raw site size plus overhead), and a domain crawl can be hundreds of GB. Add storage for the CDX index. Assumptions: self-hosted, single-domain crawls.

## 11. Privacy and data flows

WARCs are written to your own storage. Your crawler is visible to the target, and a Heritrix crawl is identifiable by its user agent — configure it honestly, since misrepresenting a crawler is both an ethical and potentially legal problem.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md) for high-fidelity capture of dynamic and social content
- wget --warc for small WARC captures without the operational overhead
- [grab-site](OSINT-C1-24.md) for steerable rapid-response crawls — with its maintenance caveat

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/internetarchive/heritrix3
- https://heritrix.readthedocs.io/

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

← 85. [LibreTranslate](JAI-A2-27.md) · 87. [n8n](JAI-A1-17.md) →
