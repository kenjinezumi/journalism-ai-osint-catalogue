# brozzler

`OSINT-C1-23` · **72/100** · overall rank 254 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 88) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 27) |
| **Subcategory** | Archival web crawling |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Internet Archive |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/internetarchive/brozzler) · [Documentation](https://github.com/internetarchive/brozzler#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 2/5 · licence+cost 5/5 → **weighted 72/100**

---

## 1. Purpose

Distributed crawler that drives real Chrome instances, proxying all traffic through warcprox to produce WARCs, with RethinkDB coordinating jobs across workers.

## Journalism / investigative use case

Archive JavaScript-dependent pages at scale where a plain crawler would capture empty shells — for example a dynamic procurement portal or a mapping application whose content only exists after script execution.

## 2. Audience

engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Browser-based capture through a recording proxy gives both fidelity (the page as rendered) and WARC provenance (the actual HTTP exchanges) — the combination that makes dynamic captures evidentiary
- Distributed worker model scales to large jobs, unlike single-browser capture tools
- Apache-2.0 and actively released (v1.10.0, 2026-11-14, same-day push) under Internet Archive stewardship
- Pairs with warcprox, which the same organisation maintains, so the components are coherent

## 5. Cons

- Operationally complex multi-service deployment: Chrome instances, warcprox, RethinkDB and workers — the heaviest capture stack here, and RethinkDB in particular is an unusual dependency with its own maintenance history
- Internet Archive internal priorities drive development, so feature direction may not match a newsroom's needs
- 63 open issues and documentation aimed at operators already familiar with the IA stack
- Browser-based crawling is resource-hungry: capture throughput per machine is far below a static crawler's

## 6. Feedback (documented)

No individual user reports verified. Documented: 824 stars with 63 open issues, release v1.10.0 on 2026-11-14 with same-day push. Used in production by the Internet Archive, which is verifiable from the organisation's tooling and is the strongest provenance available.

## 7. Assessment

Capable but hard to justify for a newsroom when browsertrix-crawler delivers comparable browser-based WARC/WACZ capture with a far simpler Docker deployment. I would choose brozzler only if you are already operating in an Internet-Archive-aligned stack or need its distributed worker model for very large dynamic crawls. For your profile, browsertrix-crawler is the pragmatic default and this is the fallback at scale.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v1.10.0 published the same day, 824 stars, 63 open issues. Current releases under institutional maintenance with production use at the Internet Archive.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/internetarchive/brozzler/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: multiple worker machines running Chrome plus warcprox and a RethinkDB instance — materially more expensive per captured page than static crawling. Assumptions: self-hosted, moderate crawl volume.

## 11. Privacy and data flows

Captured traffic is proxied through warcprox into WARC files you hold. Note that proxying everything means credentials and session tokens used during capture are written into the WARC — treat the output as sensitive.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md) — recommended: same capability class, much simpler deployment
- Heritrix for static domain-scale crawling
- [ArchiveWeb.page](OSINT-C1-31.md) for manual capture of individual dynamic pages

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/internetarchive/brozzler
- https://github.com/internetarchive/brozzler/blob/master/LICENSE

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

← 253. [Autopsy](SUR-B3-18.md) · 255. [Frictionless Data (frictionless-py)](OSINT-C3-40.md) →
