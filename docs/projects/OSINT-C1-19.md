# SiteOne Crawler

`OSINT-C1-19` · **69/100** · overall rank 276 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 102) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 31) |
| **Subcategory** | Site inventory and analysis |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Jan Reges (janreges) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/janreges/siteone-crawler) · [Documentation](https://crawler.siteone.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 69/100**

---

## 1. Purpose

PHP-based crawler that inventories a website's structure, assets, third-party components, security headers and performance characteristics, and can export an offline copy or a sitemap.

## Journalism / investigative use case

Inventory a target site's structure, assets and third-party components, and keep an offline copy for reference — the third-party-component inventory is the investigative hook, since it reveals which trackers, analytics and foreign services a government or company site loads.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Third-party component inventory is directly useful for the surveillance-adjacent story: which analytics, tracking and data-processing services a public-sector site embeds
- Produces a readable report rather than raw data, so a non-engineer can act on the findings
- MIT licensed, single-command operation, with a current release (v2.5.1, 2026-06-27) and a small backlog
- Covers security headers and performance alongside structure, giving a broad picture in one pass

## 5. Cons

- Analysis and export focus rather than archival WARC output, so it is not an evidence-capture tool
- Vendor-led project (SiteOne) with a commercial website behind it, so direction follows the vendor's interests — not a problem for the MIT code, but a continuity consideration
- PHP toolchain is an odd fit for most newsroom stacks
- Last push 2026-09-27 with the release three months earlier; modest community (1,015 stars) means limited third-party knowledge to draw on

## 6. Feedback (documented)

No individual user reports verified. Documented: 1,015 stars with 17 open issues, release v2.5.1 (2026-06-27), latest tag v2.6.1, last push 2026-09-27, MIT licence.

## 7. Assessment

Worth running once against sites you are investigating, specifically for the third-party component list — that single output can seed a story about what a ministry's website sends to whom. For tracker analysis specifically, Blacklight and Exodus Privacy give you a stronger, journalism-oriented account. I would treat SiteOne as a general reconnaissance report rather than a core tool, and not build a pipeline on it.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-27, latest release v2.5.1 (2026-06-27), latest tag v2.6.1, 1,015 stars, 17 open issues. Two months since last push with a tag ahead of the release; steady vendor-led maintenance at modest velocity.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/janreges/siteone-crawler/blob/main/LICENSE

## 10. Costs

No fee. Negligible compute; disk for offline copies.

## 11. Privacy and data flows

Direct crawl of the target with reports written locally; nothing uploaded. The target sees your crawl.

## 12. Verdict

**Monitor**

## 13. Alternatives

- Blacklight (the-markup/blacklight-collector) for journalism-oriented tracker analysis
- [Exodus Privacy](SUR-B2-01.md) for the mobile-app equivalent
- [katana](OSINT-C1-15.md) plus manual review for structure enumeration

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/janreges/siteone-crawler
- https://crawler.siteone.io/
- https://github.com/janreges/siteone-crawler/blob/main/LICENSE

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

← 275. [security-misc (Kicksecure)](SUR-B3-21.md) · 277. [smolagents](JAI-A3-11.md) →
