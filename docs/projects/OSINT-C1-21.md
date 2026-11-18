# Hyphe

`OSINT-C1-21` · **70/100** · overall rank 264 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 93) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 28) |
| **Subcategory** | Web corpus and network mapping |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Sciences Po médialab |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/medialab/hyphe) · [Documentation](https://hyphe.medialab.sciences-po.fr/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 2/5 · privacy 4/5 · usability 2/5 · licence+cost 4/5 → **weighted 70/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Crawled content belongs to the original publishers. |
| **Restrictions** | AGPL-3.0 network copyleft if you modify and expose an instance. Internal use unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: a Docker host with MongoDB and crawler components — one reasonably sized VM for a modest corpus. The dominant cost is analyst curation time, realistically days per corpus. Assumptions: self-hosted, single-analyst workflow.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/medialab/hyphe/blob/master/LICENSE
- https://github.com/medialab/hyphe
- https://hyphe.medialab.sciences-po.fr/

---

## 1. Purpose

Research web crawler that builds a curated corpus of websites with human decisions about inclusion, aggregating pages into 'web entities' and producing a link network between them.

## Journalism / investigative use case

Map an ecosystem — a disinformation network, a lobbying cluster, a set of linked front organisations — by curating which sites belong to the corpus and visualising how they link. The curation step is what makes the resulting network defensible rather than an artefact of crawler scope.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Human-in-the-loop corpus curation is the methodological point: the researcher decides what counts as an entity, so the resulting network reflects a defensible definition rather than crawler accident
- Aggregating many URLs into web entities matches how investigations think (an organisation, not a hostname), which is unusual and valuable
- Produces a link network directly exportable to Gephi for analysis and publication
- Built by a social-science methods lab with a long record in network mapping, so the data model is designed for this analysis

## 5. Cons

- Heavy install (Docker, MongoDB, ScrapyD components) and six months since the last push (2026-05-18) with the last release in July 2025 — slowing cadence for a complex multi-service system
- Curation is manual and labour-intensive: a meaningful corpus takes days of analyst attention, which is the real cost and the reason projects stall
- Link networks invite over-interpretation — a hyperlink is not a relationship, and published network graphs are routinely read as proving coordination
- Small community (392 stars) and research-oriented documentation

## 6. Feedback (documented)

No individual user reports verified. Documented: 392 stars with 56 open issues, release v1.12.2 (2025-07-07), last push 2026-05-18. médialab tools are used in academic and journalistic network research, which is credible adjacent context.

## 7. Assessment

The right instrument when the story is the shape of a network and you can commit analyst time to curation. For your profile I would pilot it on a bounded question (for example, which sites link to a known disinformation outlet and how they cluster) rather than as standing infrastructure, given the install weight and slowing cadence. Be disciplined in publication: state the inclusion criteria, and never present a hyperlink graph as evidence of coordination without corroborating evidence.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-05-18, latest release v1.12.2 (2025-07-07), 392 stars, 56 open issues. Six months without commits and sixteen months since the last release, on a multi-service system with a Docker/MongoDB dependency surface that ages. Declining rather than dormant; no deprecation notice.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Crawled content belongs to the original publishers.

**Restrictions:** AGPL-3.0 network copyleft if you modify and expose an instance. Internal use unaffected.

**Licence evidence:** https://github.com/medialab/hyphe/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a Docker host with MongoDB and crawler components — one reasonably sized VM for a modest corpus. The dominant cost is analyst curation time, realistically days per corpus. Assumptions: self-hosted, single-analyst workflow.

## 11. Privacy and data flows

Crawled pages and the link graph are stored in your own instance. Your crawler is visible to the target sites, which for a disinformation-network investigation means the targets can see they are being crawled — consider a dedicated egress.

## 12. Verdict

**Pilot**

## 13. Alternatives

- minet plus Gephi for a lighter scripted approach to the same network question
- [Gephi](OSINT-C3-33.md) alone if you already have the link data
- 4CAT for platform-centric rather than website-centric network mapping

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/medialab/hyphe
- https://hyphe.medialab.sciences-po.fr/
- https://github.com/medialab/hyphe/blob/master/LICENSE

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

← 263. [Exiv2](OSINT-C2-03.md) · 265. [sentinelhub-py](OSINT-C2-43.md) →
