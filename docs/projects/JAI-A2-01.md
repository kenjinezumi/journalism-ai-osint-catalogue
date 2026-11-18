# Apache Solr

`JAI-A2-01` · **84/100** · overall rank 113 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 47) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 27) |
| **Subcategory** | Search and indexing |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Apache Software Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/apache/solr) · [Documentation](https://solr.apache.org/guide/) |

**Scores** — relevance 3/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. Permissive, patent grant included, safe to embed in a commercial newsroom product. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No software fee. Cost is infrastructure plus operator time: a single-node index over a few million documents is comfortable on one 8-16GB-RAM VM plus SSD sized at roughly 30-50% of extracted text volume (estimate, assumptions: text-only index, no stored originals). SolrCloud with ZooKeeper triples the node count. Budget engineer time for schema design and an index-rebuild runbook; that labour, not licensing, is the dominant cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/apache/solr/blob/main/LICENSE.txt
- https://github.com/apache/solr
- https://solr.apache.org/guide/

---

## 1. Purpose

Mature Lucene-based search server with sharding, faceting, highlighting and a rich query DSL, run as a standalone service or a SolrCloud cluster.

## Journalism / investigative use case

The licence-clean index layer under a bespoke leak archive at multi-million-document scale: ICIJ's own extract/Datashare lineage targets Solr, so a newsroom can index millions of OCR'd pages and give reporters sub-second faceted search without Elastic's licence questions.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Apache-2.0 end to end, so no repeat of the Elasticsearch relicensing problem that forced rework on several newsroom stacks
- Proven at the document volumes investigative work actually hits; faceting and highlighting are first-class rather than bolted on
- Schema, analysers and per-language text processing are explicit and auditable, which matters when you must explain why a reporter's search missed a document
- ASF governance means releases, CVE handling and a long deprecation runway rather than a single vendor's roadmap

## 5. Cons

- No reporter-facing UI whatsoever — you must build one or front it with something like Blacklight, which is real engineering effort before a journalist sees value
- Sharding, schema design and JVM/heap tuning need genuine operational expertise; a badly sized Solr is slower than a well-sized Postgres FTS
- 288 open issues and no GitHub 'latest release' object (releases are published via ASF channels and git tags such as releases/solr/10.1.0), so release tracking is less convenient than a GitHub-native project
- ZooKeeper dependency for SolrCloud adds a second stateful system to operate

## 6. Feedback (documented)

No newsroom-specific user reports were collected in this survey. The strongest documented deployment signal is architectural rather than anecdotal: ICIJ's extract pipeline targets Solr, and Blacklight-on-Solr is the standard pattern in library/archive projects. Treat as inference from project documentation, not a sourced testimonial.

## 7. Assessment

For your profile this is a component, not a product: worth adopting if you are building a custom archive you expect to run for years and want zero licence ambiguity, and worth skipping if OpenAleph or Datashare already gives you the UI you need. The real cost is the front end. My judgement is that most small newsrooms should consume Solr indirectly (via Datashare/extract) and only stand it up directly when a bespoke schema or multi-tenant separation is the requirement.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest git tag releases/solr/10.1.0, 1,703 stars, 288 open issues. ASF project with formal release process and security mailing list. Judged active on substantive commit flow plus a current 10.x line, not on push recency alone.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. Permissive, patent grant included, safe to embed in a commercial newsroom product.

**Licence evidence:** https://github.com/apache/solr/blob/main/LICENSE.txt

## 10. Costs

No software fee. Cost is infrastructure plus operator time: a single-node index over a few million documents is comfortable on one 8-16GB-RAM VM plus SSD sized at roughly 30-50% of extracted text volume (estimate, assumptions: text-only index, no stored originals). SolrCloud with ZooKeeper triples the node count. Budget engineer time for schema design and an index-rebuild runbook; that labour, not licensing, is the dominant cost.

## 11. Privacy and data flows

Fully self-hosted, no outbound calls, no telemetry in the core server. Residual risks are yours to manage: Solr admin APIs must never be exposed (historic RCE classes of bug exist in older versions), and query logs can themselves disclose what reporters are searching for, so log retention needs a policy.

## 12. Verdict

**Integrate**

## 13. Alternatives

- OpenSearch (Apache-2.0 fork of Elasticsearch, closer API compatibility with Aleph/Datashare defaults)
- [Datasette](JAI-A2-09.md) for anything that fits SQLite
- [OpenAleph](JAI-A2-35.md) if you want the whole archive product rather than an index

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/apache/solr
- https://solr.apache.org/guide/
- https://github.com/apache/solr/blob/main/LICENSE.txt

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |

---

← 112. [SunCalc](OSINT-C2-18.md) · 114. [CTranslate2](JAI-A2-08.md) →
