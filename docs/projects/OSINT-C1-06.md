# YaCy

`OSINT-C1-06` · **66/100** · overall rank 289 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 108) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 33) |
| **Subcategory** | Self-hosted search index |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | YaCy community |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-2.0-or-later (GitHub API reports NOASSERTION) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/yacy/yacy_search_server) · [Documentation](https://yacy.net/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 66/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Peer-to-peer search engine that crawls and indexes websites locally, usable as a standalone private index or federated with other peers.

## Journalism / investigative use case

Build a private searchable index over a defined set of target sites — ministries, forums, company websites — for repeatable full-text investigation, so a query runs against your own crawl rather than against whatever a commercial engine currently chooses to show.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- A private index over chosen sites is qualitatively different from search: results are reproducible, complete within your crawl, and unaffected by engine ranking changes — which makes 'this phrase appears nowhere on the ministry's site' a statement you can actually support
- Crawled content stays local, so your research targets are not disclosed to any search provider
- Mature, long-lived project still receiving commits (pushed 2026-11-03) under GPL-2.0-or-later
- Can run in standalone mode with no peer-to-peer participation, keeping the deployment self-contained

## 5. Cons

- Heavy resource use: a serious index needs substantial disk and RAM, and the Java stack is not light
- Relevance ranking is noticeably weaker than commercial engines, so finding things in a large index takes more query craft
- Dated UI and 248 open issues, with no release objects (latest tag Release_1.941) and SPDX NOASSERTION despite the GPL licence — assessment requires reading the repository rather than its metadata
- P2P mode shares index fragments with other peers, which would disclose aspects of your crawl — this must be deliberately disabled for investigative use

## 6. Feedback (documented)

No individual user reports verified. Documented: 4,110 stars with 248 open issues, last push 2026-11-03, no release objects, latest tag Release_1.941, SPDX NOASSERTION. A long-running community project with a large accumulated backlog.

## 7. Assessment

Niche but genuinely valuable for one task: exhaustive, reproducible search over a bounded set of sites you care about. For your profile I would deploy it in standalone mode (P2P off, explicitly verified) over the ministries, registries and company sites relevant to a long-running beat, and treat it as an evidentiary instrument rather than a discovery one. If you only need discovery, SearXNG is far less work.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-03, no release objects, latest tag Release_1.941, 4,110 stars, 248 open issues. Commits continue but the large backlog and informal release process indicate a mature community project running at low velocity rather than active development.

## 9. Licensing

**Licence:** GPL-2.0-or-later (GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Your crawl contains third-party content subject to the original publishers' rights.

**Restrictions:** GPL-2.0-or-later on the software. Crawling may engage target sites' terms of service — a separate consideration from the licence.

**Licence evidence:** https://github.com/yacy/yacy_search_server

## 10. Costs

No fee. Infrastructure estimate: a JVM host with substantial disk for the index — a few hundred GB for a meaningful multi-site crawl, scaling with scope. Assumptions: standalone mode, text-focused index.

## 11. Privacy and data flows

Crawled content is stored locally and queries never leave your machine in standalone mode — the strongest privacy position in this subcategory. P2P mode shares index fragments with other peers and must be disabled for investigative work. Note that your crawler's requests are visible to the target sites.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- P2P mode would disclose index fragments — must be explicitly disabled

## 13. Alternatives

- [Apache Solr](JAI-A2-01.md) plus your own crawler (Heritrix, browsertrix-crawler) for more control and better ranking
- [SearXNG](OSINT-C1-01.md) for discovery rather than exhaustive search
- [Marginalia Search](OSINT-C1-05.md) where you want someone else's independent index

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/yacy/yacy_search_server
- https://yacy.net/

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

← 288. [pHash](OSINT-C2-08.md) · 290. [Carrot2](JAI-A2-07.md) →
