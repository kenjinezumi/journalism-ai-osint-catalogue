# SearXNG

`OSINT-C1-01` · **89/100** · overall rank 47 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 16) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 9) |
| **Subcategory** | Meta-search |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | SearXNG community |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/searxng/searxng) · [Documentation](https://docs.searxng.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 4/5 → **weighted 89/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0: if you modify SearXNG and offer it over a network, you must publish your modified source. Running it unmodified for your newsroom carries no obligation. Some upstream engines' terms of service prohibit automated querying — a terms question separate from the licence. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: one small VM or container; some engines require API keys with their own quotas and costs (not priced here). Operating effort is low but non-zero — expect occasional engine breakage to investigate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/searxng/searxng/blob/master/LICENSE
- https://github.com/searxng/searxng
- https://docs.searxng.org/

---

## 1. Purpose

Self-hosted privacy-respecting metasearch engine that queries dozens of upstream engines and aggregates the results, with no user profiling and configurable engine selection.

## Journalism / investigative use case

Run queries across dozens of engines from one self-hosted instance, compare result sets to see what each engine suppresses or elevates, and avoid personalised results during research — which matters because a logged-in Google session quietly shapes what an investigation finds.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Eliminates search personalisation as a confounder, so two reporters researching the same subject see the same thing and results are reproducible enough to describe in a methodology note
- Querying many engines at once routinely surfaces results that a single engine buries — the practical core of search-based OSINT
- Largest and most active community in this subcategory (39,634 stars, pushed 2026-11-17), so engine-scraper breakage gets fixed quickly, which is the dominant failure mode here
- Self-hosting keeps query logs on your own infrastructure instead of with a search provider — a real operational-security gain when your queries reveal an investigation

## 5. Cons

- Result completeness varies by engine health: scrapers break, engines rate-limit, and an empty result set can mean 'nothing found' or 'engine broken' with no clear distinction
- No persistent archiving of results, so you must capture anything you intend to cite with a separate tool
- Queries still leave your instance to upstream engines, so the engines see the query (from your server's IP) even though they do not see a user profile — self-hosting changes who correlates, not whether queries are visible
- AGPL-3.0 network copyleft applies if you modify and expose an instance to others; 208 open issues reflects constant engine maintenance

## 6. Feedback (documented)

No individual user reports verified in this survey. The checkable signals are strong: 39,634 stars, 208 open issues and same-day commits on 2026-11-17 — the open-issue count is characteristic of a project whose scrapers constantly need repair as engines change. Widely recommended in OSINT training material.

## 7. Assessment

Adopt and self-host — this is the cheapest meaningful improvement to search-based research, and the de-personalisation property alone justifies it. For your profile two configuration points matter: run it behind your own network so the upstream engines see your server rather than a reporter's home connection, and set an explicit expectation that an engine returning nothing may be broken, not empty. Pair with SingleFile or Scoop to preserve anything you will cite.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, no release objects (continuous-delivery model), 39,634 stars, 208 open issues. Daily commits from a large community; the absence of versioned releases is a deliberate rolling-release choice rather than a maintenance gap.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: if you modify SearXNG and offer it over a network, you must publish your modified source. Running it unmodified for your newsroom carries no obligation. Some upstream engines' terms of service prohibit automated querying — a terms question separate from the licence.

**Licence evidence:** https://github.com/searxng/searxng/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: one small VM or container; some engines require API keys with their own quotas and costs (not priced here). Operating effort is low but non-zero — expect occasional engine breakage to investigate.

## 11. Privacy and data flows

Self-hosting keeps query logs local and removes profiling. The residual exposure is real and should be understood: queries are forwarded to upstream engines from your instance's IP, so a sustained investigation produces a visible query pattern attributable to your organisation's address. Consider routing through Tor or a dedicated egress if that matters.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [4get](OSINT-C1-02.md) for a lighter-weight self-hosted metasearch
- [LibreY](OSINT-C1-03.md) where even SearXNG is more than you want to operate
- [Marginalia Search](OSINT-C1-05.md) for a deliberately non-commercial index that surfaces different material

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/searxng/searxng
- https://docs.searxng.org/
- https://github.com/searxng/searxng/blob/master/LICENSE

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

← 46. [RSSHub](JAI-A1-05.md) · 48. [Tella](OSINT-C3-06.md) →
