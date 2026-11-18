# RSS-Bridge

`JAI-A1-06` · **78/100** · overall rank 180 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 72) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 16) |
| **Subcategory** | Feed generation |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | RSS-Bridge community |
| **Maintenance** | Actively maintained |
| **Licence** | Unlicense |
| **Licence type** | Public domain |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/RSS-Bridge/rss-bridge) · [Documentation](https://rss-bridge.github.io/rss-bridge/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Public domain |
| **Exact licence (as recorded)** | Unlicense |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Feed content belongs to the source publishers. |
| **Restrictions** | None whatsoever — public-domain dedication. Bridges may scrape sites whose terms prohibit it, which is a separate consideration. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. A small PHP host; negligible.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/RSS-Bridge/rss-bridge/blob/master/UNLICENSE
- https://github.com/RSS-Bridge/rss-bridge
- https://rss-bridge.github.io/rss-bridge/

---

## 1. Purpose

PHP service with community-maintained 'bridges' that generate RSS, Atom and JSON feeds from websites and platforms lacking them.

## Journalism / investigative use case

The same gap-filling role as RSSHub, with a different bridge catalogue — so between the two, a source that neither covers is genuinely rare. Useful specifically where RSSHub lacks a route for a European or niche source that RSS-Bridge happens to support.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Unlicense (public domain) — the most permissive licence in this subcategory, so there is no copyleft consideration at all when deploying or modifying it
- Different bridge catalogue from RSSHub, so running both maximises source coverage for little extra cost
- Simple PHP deployment that runs on modest shared hosting, lowering the barrier where container infrastructure is unavailable
- Actively maintained (pushed 2026-11-15) with a substantial community (9,353 stars)

## 5. Cons

- Release cadence has lapsed: the latest release object dates from 2025-08-05 against current commits, so you track the default branch and have no pinnable version
- Same structural fragility as all feed generators: bridges break when sites change, and 291 open issues largely reflect that churn
- Smaller bridge catalogue than RSSHub, so it is a complement rather than a substitute
- PHP deployment is a different operational idiom from a Node or Go stack, which adds a second thing to maintain if you also run RSSHub

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 9,353 stars with 291 open issues, latest release 2025-08-05 against a push on 2026-11-15, Unlicense. The release gap alongside current commits is visible in the API data and is the notable operational caveat.

## 7. Assessment

Integrate it as a secondary feed generator where RSSHub has no route — the marginal cost is a small PHP container and the marginal coverage is real. For your profile the Unlicense is worth noting: it is the one tool in this segment you can modify and redistribute with no obligation whatsoever, which makes it a reasonable base if you ever want to build a newsroom-specific feed generator. Track the default branch and pin by commit.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-15, latest release dated 2025-08-05, 9,353 stars, 291 open issues. Commits are current; release engineering has lapsed, which is a pinning inconvenience rather than an activity concern.

## 9. Licensing

**Licence:** Unlicense _(SPDX verified)_

**Model / data licence:** n/a. Feed content belongs to the source publishers.

**Restrictions:** None whatsoever — public-domain dedication. Bridges may scrape sites whose terms prohibit it, which is a separate consideration.

**Licence evidence:** https://github.com/RSS-Bridge/rss-bridge/blob/master/UNLICENSE

## 10. Costs

No fee. A small PHP host; negligible.

## 11. Privacy and data flows

Self-hosting keeps your monitored-source list private; your instance's requests are visible to scraped sites.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [RSSHub](JAI-A1-05.md) as the primary generator with a larger route catalogue
- [changedetection.io](SUR-B1-15.md) for change alerts where no feed can be generated
- Writing a small bespoke scraper for a single critical source, which is often simpler than maintaining a bridge

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/RSS-Bridge/rss-bridge
- https://rss-bridge.github.io/rss-bridge/
- https://github.com/RSS-Bridge/rss-bridge/blob/master/UNLICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 179. [ImageHash](OSINT-C2-05.md) · 181. [browsertrix-behaviors](OSINT-C1-34.md) →
