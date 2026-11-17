# katana

`OSINT-C1-15` · **82/100** · overall rank 131 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 42) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 15) |
| **Subcategory** | Web crawling and URL discovery |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | ProjectDiscovery |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/projectdiscovery/katana) · [Documentation](https://github.com/projectdiscovery/katana#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 82/100**

---

## 1. Purpose

Fast Go web crawler with both standard and headless (Chromium) modes, JavaScript parsing, form filling and configurable scope, outputting discovered URLs and endpoints.

## Journalism / investigative use case

Enumerate every reachable page and document on a target site — PDFs, archives, staging paths, orphaned directories — before mirroring or analysis. This is how you find the procurement annex nobody linked from the navigation.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Headless mode parses JavaScript to find endpoints that static crawlers miss, which matters on modern government portals built as single-page applications
- Fast and scope-configurable, so you can crawl a large site without accidentally crawling the internet
- MIT, single Go binary, very actively maintained (pushed 2026-11-17) with an exceptionally clean tracker (28 open against 17,862 stars)
- Composes well: pipe its output into a WARC capture tool or a document downloader

## 5. Cons

- Discovers URLs rather than preserving content, so it must be paired with a capture tool for anything evidentiary — an easy step to forget
- Crawling from your own host makes a visible request pattern to the target, and an aggressive crawl can be mistaken for an attack or trigger blocking
- Form filling and headless crawling can have side effects on poorly built sites (triggering submissions, consuming resources) — real care is needed on live government systems
- Security-tooling heritage means defaults are tuned for penetration testing rather than polite journalism; rate limits need setting deliberately

## 6. Feedback (documented)

No individual user reports verified. Documented: 17,862 stars with 28 open issues and same-day commits (2026-11-17), release v1.8.0 (2026-10-05). ProjectDiscovery's suite has consistent release discipline, verifiable across its repositories.

## 7. Assessment

The right discovery tool for a target site, used with explicit politeness settings. For your profile the workflow I would standardise: katana to enumerate, a filter for document extensions, then browsertrix-crawler or wget --warc to capture the documents you want as evidence. Set rate limits and disable form interaction on live public-service sites — a crawl that degrades a council's website is both an ethical and a legal problem, and it will end the access.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.8.0 (2026-10-05), 17,862 stars, 28 open issues. Same-day commits, regular releases, very low backlog relative to adoption.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material for the code. Crawling engages the target's terms of service and, in some jurisdictions, computer-misuse law if done aggressively — a legal rather than licence consideration.

**Licence evidence:** https://github.com/projectdiscovery/katana/blob/main/LICENSE

## 10. Costs

No fee. Chromium for headless mode adds resource use. Negligible infrastructure.

## 11. Privacy and data flows

Direct HTTP(S) requests from your host to the target, so the target sees your IP and request pattern. For a sensitive target, crawl from a dedicated egress rather than the newsroom's address.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Photon](OSINT-C1-20.md) for a lighter Python crawler focused on harvesting contacts and links
- [Scrapy](OSINT-C1-16.md) when you need structured extraction rather than URL discovery
- [browsertrix-crawler](OSINT-C1-29.md) when capture fidelity rather than enumeration is the goal

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/projectdiscovery/katana
- https://github.com/projectdiscovery/katana/blob/main/LICENSE

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

← 130. [edgartools](OSINT-C3-17.md) · 132. [LlamaIndex](JAI-A3-04.md) →
