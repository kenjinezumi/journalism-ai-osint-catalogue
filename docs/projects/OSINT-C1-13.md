# OSINT Framework

`OSINT-C1-13` · **59/100** · overall rank 330 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 131) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 41) |
| **Subcategory** | Tool directory |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | lockfale |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/lockfale/OSINT-Framework) · [Documentation](https://osintframework.com/) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 3/5 · privacy 2/5 · usability 4/5 · licence+cost 5/5 → **weighted 59/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a — links only. |
| **Restrictions** | None. Forking and pruning is explicitly easy under MIT, which is the recommended use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Many linked services are paid or freemium, and their costs are not catalogued — a hidden cost of following the tree.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/lockfale/OSINT-Framework/blob/master/LICENSE
- https://github.com/lockfale/OSINT-Framework
- https://osintframework.com/

---

## 1. Purpose

Interactive tree-structured directory of OSINT resources and tools organised by the identifier or artefact you start from — username, email, domain, phone number, image.

## Journalism / investigative use case

Starting point for choosing a collection method or source type when you know the identifier you hold but not the tooling — a reporter with a phone number and no idea what can be done with it finds the categories of approach in a minute.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- The 'start from the identifier you hold' structure matches how an investigation actually begins, which is why it remains the most-used orientation resource in this field (12,467 stars)
- Broad coverage across identifier types, including categories a newcomer would not think to look for
- MIT licensed and self-hostable as a static site, so you can fork and prune it into a newsroom-specific version
- Still maintained (pushed 2026-10-31), unusual for a link directory of this age

## 5. Cons

- A directory, not a tool: it tells you what exists, not whether it works, and link quality and freshness vary widely — several categories point to dead or hostile services
- No maintenance or trust signalling on entries, so a reporter cannot tell a maintained tool from an abandoned one or a data broker from a research resource
- 194 open issues, many of them link-rot and submission requests, indicating curation lags submissions
- Linking out to third-party services means following a link can disclose your interest to a commercial data broker — a risk a newcomer will not anticipate

## 6. Feedback (documented)

No individual user reports verified. Documented: 12,467 stars with 194 open issues, last push 2026-10-31, no releases. The large open-issue count on a link directory is itself evidence of curation lag.

## 7. Assessment

Useful for orientation and actively harmful if used uncritically, because it does not distinguish a maintained open tool from a paid people-search broker that will log your query. For your profile the valuable move is to fork it, strip the categories you will never use and the services you consider unsafe, and keep an internal version with your own trust annotations. Use this catalogue's assessments for anything you intend to deploy.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-31, no releases, 12,467 stars, 194 open issues. Episodic curation updates with a large pending backlog; the project is alive but curation does not keep pace with link rot.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a — links only.

**Restrictions:** None. Forking and pruning is explicitly easy under MIT, which is the recommended use.

**Licence evidence:** https://github.com/lockfale/OSINT-Framework/blob/master/LICENSE

## 10. Costs

No fee. Many linked services are paid or freemium, and their costs are not catalogued — a hidden cost of following the tree.

## 11. Privacy and data flows

No investigative data flows of its own; it is a link index. The risk is downstream: linked third-party services, including commercial people-search brokers, will see your queries and may retain them. Brief reporters before pointing them at it.

## 12. Verdict

**Reference only**

## 13. Alternatives

- This catalogue for maintenance- and licence-verified assessments
- Bellingcat's online investigation toolkit for a curated, practitioner-maintained list
- A pruned internal fork with trust annotations

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/lockfale/OSINT-Framework
- https://osintframework.com/
- https://github.com/lockfale/OSINT-Framework/blob/master/LICENSE

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

← 329. [Bellingcat smart-image-sorter](OSINT-C2-15.md) · 331. [UniversalFakeDetect](JAI-A4-20.md) →
