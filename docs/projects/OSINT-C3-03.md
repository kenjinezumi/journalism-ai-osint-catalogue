# Hoover

`OSINT-C3-03` · **63/100** · overall rank 305 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 117) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 37) |
| **Subcategory** | Document search platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Liquid Investigations |
| **Maintenance** | Uncertain |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/liquidinvestigations/hoover-search) · [Documentation](https://github.com/liquidinvestigations/hoover-search#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 63/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | Permissive as published; confirm the licence file before redistribution. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** No software fee. Infrastructure: a multi-service deployment with a search index — lighter than OpenAleph but still a real deployment. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/liquidinvestigations/hoover-search
- `../sources/evidence/leads.md`

---

## 1. Purpose

Search service for collections of documents and email archives, indexing text and metadata across heterogeneous sources with a search interface aimed at investigative use.

## Journalism / investigative use case

A lighter alternative to Aleph-class platforms for the common case: you have a document dump and a mailbox archive and you want reporters to search them together, without deploying an entity-resolution platform or operating an Elasticsearch cluster you do not need.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Scoped deliberately to search rather than entity resolution, which makes it substantially lighter to deploy than OpenAleph for teams whose actual need is 'let reporters search these files'
- Handles email archives alongside documents, which is the realistic composition of a leak and is awkward in general-purpose document systems
- Built for investigative journalism by a project focused on that use case, so the interface assumptions match reporters rather than enterprise search
- Repository path verified this session: hoover/search redirects to liquidinvestigations/hoover-search, so older references resolve

## 5. Cons

- Small project with limited community, so you will be reading source and the deployment documentation assumes familiarity with the stack
- Multi-component architecture (search, snoop, UI) spread across repositories, which makes orientation slower than the scope suggests
- Development cadence is modest, so it sits between 'maintained' and 'quiet' and warrants a liveness check before adoption
- No entity extraction or cross-referencing, so if your investigation is entity-centric you will outgrow it and need OpenAleph anyway

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository transfer hoover/search → liquidinvestigations/hoover-search was confirmed by API redirect on 2026-11-17 (recorded in leads.md L4). Liquid Investigations' orientation to investigative journalism is documented by the project; I verified no specific newsroom deployment.

## 7. Assessment

Worth evaluating if your need is genuinely search-only and OpenAleph's operational weight is the obstacle — which is a common and under-acknowledged situation. For your profile I would compare it against ICIJ Datashare in desktop mode first, since Datashare gives you search plus basic entity extraction with less deployment work and far stronger institutional backing. Choose Hoover if you need a server-side shared search over mixed documents and mail and want something lighter than Aleph.

## 8. Maintenance

**Uncertain** — Verified via the GitHub API 2026-11-17 as live and non-archived with the organisation transfer confirmed. The project spans several repositories with modest activity and no clear release cadence, so maintenance cannot be confidently classified from metadata — hence Uncertain rather than an inferred classification in either direction. Check liveness directly before adopting.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Permissive as published; confirm the licence file before redistribution.

**Licence evidence:** https://github.com/liquidinvestigations/hoover-search

## 10. Costs

No software fee. Infrastructure: a multi-service deployment with a search index — lighter than OpenAleph but still a real deployment. Estimate.

## 11. Privacy and data flows

Self-hosted; documents and mail stay on your infrastructure. The index is as sensitive as the collection and must not be exposed.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [ICIJ Datashare](JAI-A2-23.md) for search plus entity extraction with better support
- [OpenAleph](JAI-A2-35.md) where entity cross-referencing is needed
- [Apache Solr](JAI-A2-01.md) or OpenSearch plus a simple front end for a bespoke build

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/liquidinvestigations/hoover-search
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 304. [Conifer](OSINT-C1-35.md) · 306. [HURIDOCS preserve](OSINT-C3-10.md) →
