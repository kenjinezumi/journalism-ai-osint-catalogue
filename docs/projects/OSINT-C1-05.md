# Marginalia Search

`OSINT-C1-05` · **73/100** · overall rank 237 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 81) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 25) |
| **Subcategory** | Independent search index |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Viktor Lofgren (MarginaliaSearch) |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 (per project documentation; GitHub API reports NOASSERTION) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MarginaliaSearch/MarginaliaSearch) · [Documentation](https://search.marginalia.nu/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 73/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 (per project documentation; GitHub API reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | The index is the project's own crawl; crawled content belongs to the original publishers. |
| **Restrictions** | AGPL-3.0 network copyleft would apply to a modified self-hosted instance. Confirm the licence file before forking, given the SPDX gap. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Free to use the public instance. Self-hosting requires large storage and CPU for crawling and indexing — a substantial infrastructure commitment, not quantified here because it depends entirely on index scope.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/MarginaliaSearch/MarginaliaSearch
- https://search.marginalia.nu/

---

## 1. Purpose

Independent search engine with its own crawler and index that deliberately de-prioritises commercial content, surfacing small, text-heavy, non-commercial websites.

## Journalism / investigative use case

Surface obscure personal pages, forums and old sites that mainstream engines suppress — useful for finding early traces of a person or organisation, the self-published page from 2009, or the small forum where a subject once posted under their own name.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- A genuinely independent index, not a proxy over Google or Bing, so it finds material the major engines have dropped or never ranked — the single most useful property for background research on an individual
- The deliberate anti-commercial ranking bias is the feature: it inverts the SEO filter that buries exactly the amateur and archival pages an investigation wants
- Self-hostable in principle (AGPL-3.0), so a newsroom could run its own index over chosen corpora
- Actively developed (pushed 2026-11-16) by a maintainer with a sustained multi-year commitment

## 5. Cons

- Deliberately partial index: it is not a Google replacement and will miss mainstream coverage entirely, so it complements rather than substitutes
- Self-hosting requires large storage and CPU for the index — realistically out of reach for most newsrooms, so in practice you use the public instance
- Release metadata is stale (v24.10.0 from 2024-10-14) and GitHub reports SPDX NOASSERTION, so the AGPL-3.0 label rests on project documentation rather than a detected licence file
- Queries to the public instance go to its operator; the operator is a small independent project rather than an organisation with a formal privacy programme

## 6. Feedback (documented)

No individual user reports verified. Documented: 2,240 stars with 31 open issues, pushed 2026-11-16, release object v24.10.0 (2024-10-14), SPDX NOASSERTION. Marginalia has a strong reputation among researchers for surfacing non-commercial web content, reflected in its community following.

## 7. Assessment

Worth adding to your standard research routine specifically for person and organisation background, where its index composition is a real advantage over mainstream search. Use the public instance and treat the operator as a third party who sees your queries — for a sensitive subject, query through Tor. Do not plan to self-host unless you have serious storage to spare; the public instance is the practical product.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v24.10.0 (2024-10-14), SPDX NOASSERTION, 2,240 stars, 31 open issues. Current commits and a continuously operated public service; the stale release object reflects a service-first rather than release-first project.

## 9. Licensing

**Licence:** AGPL-3.0 (per project documentation; GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** The index is the project's own crawl; crawled content belongs to the original publishers.

**Restrictions:** AGPL-3.0 network copyleft would apply to a modified self-hosted instance. Confirm the licence file before forking, given the SPDX gap.

**Licence evidence:** https://github.com/MarginaliaSearch/MarginaliaSearch

## 10. Costs

Free to use the public instance. Self-hosting requires large storage and CPU for crawling and indexing — a substantial infrastructure commitment, not quantified here because it depends entirely on index scope.

## 11. Privacy and data flows

Queries to the public instance go to the operator; self-hosting keeps everything local. No personalisation or profiling is applied, but the operator is a small project rather than an institution — route sensitive queries through Tor.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [SearXNG](OSINT-C1-01.md) to query many engines including, where available, independent ones
- [YaCy](OSINT-C1-06.md) for a self-hosted index over a defined set of target sites
- Internet Archive full-text search for historical web material

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/MarginaliaSearch/MarginaliaSearch
- https://search.marginalia.nu/

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

← 236. [dedupe](JAI-A2-11.md) · 238. [ProofMode](SUR-B3-32.md) →
