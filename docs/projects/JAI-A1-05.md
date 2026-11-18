# RSSHub

`JAI-A1-05` · **89/100** · overall rank 46 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 17) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 3) |
| **Subcategory** | Feed generation |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | DIYgod and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/DIYgod/RSSHub) · [Documentation](https://docs.rsshub.app/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 4/5 → **weighted 89/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Content in generated feeds belongs to the source publishers. |
| **Restrictions** | AGPL-3.0: a modified instance served to others obliges source publication. Separately, individual routes may scrape sites whose terms prohibit it — a terms rather than licence question, and one worth considering per route. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: a small Node service; resource use scales with the number and frequency of routes you poll. Assumptions: self-hosted, moderate route count.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/DIYgod/RSSHub/blob/master/LICENSE
- https://github.com/DIYgod/RSSHub
- https://docs.rsshub.app/

---

## 1. Purpose

Extensible feed-generation service with several thousand community-maintained routes that produce RSS feeds for websites and platforms that provide none, including social platforms, forums and government sites.

## Journalism / investigative use case

Making unmonitorable sources monitorable: a ministry page with no feed, a regional forum, a company's announcements section, a social account — RSSHub generates a feed so your existing reader and alerting pipeline can watch it. This is what closes the gap between 'we should monitor that' and 'we do'.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Route breadth is the asset: several thousand community routes mean the obscure source you need is often already covered, and writing a new route is modest work
- Turns the feed reader you already run into a universal monitoring system, which is far cheaper than per-source change detection
- Extremely active (release dated 2026-11-17 with same-day push, 47,071 stars) and an exceptionally low open-issue count for its size (25)
- Self-hostable, so your monitored sources stay private and you are not rate-limited by a public instance

## 5. Cons

- Routes scrape third-party sites, so they break when sites change — with thousands of routes, some are always broken, and a silently broken route looks like 'no news' rather than an error
- AGPL-3.0 network copyleft applies to a modified public instance, which matters if you offer feeds to partners
- Scraping platforms may breach their terms of service, and for social platforms specifically the routes exist in a grey area that can stop working abruptly
- Public instances see which sources you monitor, and are heavily rate-limited — self-hosting is effectively required for serious use

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 47,071 stars with only 25 open issues and a release on 2026-11-17 with same-day push, AGPL-3.0. The very low issue count against enormous scale suggests aggressive triage; route breakage is handled through continuous community contribution rather than issue accumulation.

## 7. Assessment

Adopt and self-host — the combination of FreshRSS plus a private RSSHub covers an enormous share of newsroom monitoring need at almost no cost. For your profile the operational discipline that matters is detecting silent route failure: a monitoring system that quietly stops reporting is worse than none, so add a staleness check that alerts when a feed produces nothing for an unexpected period. Treat social-platform routes as fragile by nature.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v2026.11.17-8661.cf95739 published the same day, 47,071 stars, 25 open issues. Continuous-delivery release scheme with same-day commits and a very large contributor community.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Content in generated feeds belongs to the source publishers.

**Restrictions:** AGPL-3.0: a modified instance served to others obliges source publication. Separately, individual routes may scrape sites whose terms prohibit it — a terms rather than licence question, and one worth considering per route.

**Licence evidence:** https://github.com/DIYgod/RSSHub/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a small Node service; resource use scales with the number and frequency of routes you poll. Assumptions: self-hosted, moderate route count.

## 11. Privacy and data flows

Self-hosting keeps your monitored-source list private, which matters because that list reveals your editorial interests. Your instance's requests are visible to the scraped sites.

## 12. Verdict

**Adopt**

## 13. Alternatives

- rss-bridge as an alternative feed generator with a different route set
- [changedetection.io](SUR-B1-15.md) for sources where no route exists and you only need change alerts
- Direct API access where a source offers one

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/DIYgod/RSSHub
- https://docs.rsshub.app/
- https://github.com/DIYgod/RSSHub/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 45. [Qubes OS](SUR-B3-20.md) · 47. [SearXNG](OSINT-C1-01.md) →
