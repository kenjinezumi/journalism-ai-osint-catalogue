# browsertrix-crawler

`OSINT-C1-29` · **94/100** · overall rank 7 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 4) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 3) |
| **Subcategory** | High-fidelity capture |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/browsertrix-crawler) · [Documentation](https://crawler.docs.browsertrix.com/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 94/100**

---

## 1. Purpose

Dockerised browser-based crawler that drives Chromium to produce high-fidelity WARC/WACZ captures, with configurable scope, behaviours for dynamic pages and sitemap support.

## Journalism / investigative use case

Capture modern government portals, dashboards and interactive document viewers faithfully enough that the archived copy still behaves like the live page when a disputed change is later examined — the capture tool of record for anything built as a single-page application.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Highest practical capture fidelity in this catalogue for dynamic content, because it records what a real browser actually fetched and rendered
- Single Docker image with declarative configuration, which makes it dramatically easier to operate than brozzler for comparable capability
- WACZ output is a single portable file that ReplayWeb.page can open with no server, so sharing a capture with an editor or lawyer is trivial
- Very actively maintained (v1.15.4, 2026-11-11) by the organisation that defines much of current web-archiving practice

## 5. Cons

- No change detection or alerting — it is capture infrastructure, so monitoring must be built around it
- Resource-hungry: browser-based capture is far slower and more memory-intensive per page than static crawling, which caps throughput
- AGPL-3.0 has network-service implications if you expose a modified version, which is worth a legal check before building a capture service for partners
- Requires Docker familiarity and 152 open issues reflect the complexity of behaviours across many site types

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,197 stars with 152 open issues, release v1.15.4 (2026-11-11), pushed 2026-11-14. Webrecorder's tooling is the de facto standard in modern web archiving, verifiable from IIPC and institutional archive adoption.

## 7. Assessment

Adopt as your capture tool of record for anything dynamic or disputed. For your profile the combination that works is browsertrix-crawler for capture, WACZ as the artefact, and ReplayWeb.page for handing a capture to a colleague or lawyer who has no infrastructure. Write the capture configuration into version control alongside the investigation notes, so the methodology is reproducible — that is what makes the capture defensible rather than merely good.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v1.15.4 (2026-11-11), 1,197 stars, 152 open issues. Frequent releases from a funded organisation whose core mission this is.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Captured content belongs to the original publishers.

**Restrictions:** AGPL-3.0: offering a modified version as a network service obliges source publication. Running it internally to produce captures carries no obligation.

**Licence evidence:** https://github.com/webrecorder/browsertrix-crawler/blob/main/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a Docker host with several GB of RAM per concurrent browser plus storage for WACZ output; capture throughput is low enough that large crawls need either patience or parallel workers. Assumptions: self-hosted, moderate crawl sizes.

## 11. Privacy and data flows

WARC/WACZ output is written to storage you control (local disk or S3-compatible); nothing is sent to Webrecorder unless you choose their hosted service. Note that captures of logged-in sessions will contain session material — treat output as sensitive.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Browsertrix](OSINT-C1-30.md) (platform) for a managed, team-scale version of the same crawler
- [brozzler](OSINT-C1-23.md) for a distributed Internet-Archive-aligned alternative
- [ArchiveWeb.page](OSINT-C1-31.md) for manual one-page capture by a non-engineer

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/webrecorder/browsertrix-crawler
- https://crawler.docs.browsertrix.com/
- https://github.com/webrecorder/browsertrix-crawler/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |
| 9 | [SearXNG](OSINT-C1-01.md) | 89 | Adopt |

---

← 6. [yt-dlp](OSINT-C1-45.md) · 8. [OpenSanctions (dataset)](OSINT-C3-01.md) →
