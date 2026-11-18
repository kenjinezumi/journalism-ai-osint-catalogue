# Oxigraph

`JAI-A3-17` · **73/100** · overall rank 244 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 100) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 17) |
| **Subcategory** | Knowledge graphs |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Oxigraph contributors (Tpt) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/oxigraph/oxigraph) · [Documentation](https://docs.rs/oxigraph/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 73/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Loaded data carries its own licence — Wikidata is CC0, other sources vary. |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Disk and memory proportional to graph size; a Wikidata subset plus investigation data fits comfortably on one machine. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/oxigraph/oxigraph/blob/main/LICENSE-APACHE
- https://github.com/oxigraph/oxigraph
- https://docs.rs/oxigraph/

---

## 1. Purpose

RDF triple store written in Rust with SPARQL 1.1 query and update support, available as an embeddable library, a Python binding and a standalone HTTP server.

## Journalism / investigative use case

A local SPARQL endpoint for investigation data: load a Wikidata subset plus your own entity statements into one store and query across them, so a question like 'which companies in my leak have a Wikidata-recorded director who also holds public office' becomes a single query.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Embeddable and lightweight, so a local triple store is a file and a process rather than a Java service — a materially lower operational bar than Jena or Blazegraph
- SPARQL 1.1 including update means you can combine external linked data with your own assertions in one queryable graph, which is the useful pattern
- Apache-2.0 with steady active maintenance (v0.5.13, 2026-10-22; pushed 2026-11-15) and a clean, focused codebase (2,050 stars)
- Rust implementation gives predictable performance and memory behaviour at the scale a newsroom graph reaches

## 5. Cons

- RDF and SPARQL skills remain the barrier, and the tool does nothing to lower it — the conceptual cost is the same as with RDFLib
- Smaller community than the established Java triple stores, so there is less guidance for unusual queries or performance tuning
- Scales well for newsroom-sized graphs but is not a competitor to large-scale distributed triple stores if your graph becomes very large
- Effectively a single-maintainer project, which for a store holding investigation data is a continuity consideration

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 2,050 stars with release v0.5.13 (2026-10-22), pushed 2026-11-15, Apache-2.0. Oxigraph is known in the RDF community as the lightweight modern alternative to Java triple stores.

## 7. Assessment

The right triple store if you decide RDF is the correct model for an investigation graph — and the embeddability is what makes that decision affordable. For your profile I would reach for it in one specific scenario: when you want to combine a Wikidata subset with your own entity assertions and query across both, which is genuinely powerful and hard to do otherwise. For most entity work, FollowTheMoney plus a relational store remains simpler.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-15, latest release v0.5.13 (2026-10-22), 2,050 stars, Apache-2.0. Regular releases with current commits from a focused maintainer.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a. Loaded data carries its own licence — Wikidata is CC0, other sources vary.

**Restrictions:** None material.

**Licence evidence:** https://github.com/oxigraph/oxigraph/blob/main/LICENSE-APACHE

## 10. Costs

No fee. Disk and memory proportional to graph size; a Wikidata subset plus investigation data fits comfortably on one machine. Estimate.

## 11. Privacy and data flows

Fully local, so queries over sensitive investigation data disclose nothing — the key advantage over querying a public SPARQL endpoint with your entity names.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [RDFLib](JAI-A3-16.md)'s in-memory store for small graphs
- Apache Jena or Blazegraph for larger, more established triple stores
- Neo4j Community or DuckDB for property-graph and relational approaches that most teams find easier

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/oxigraph/oxigraph
- https://docs.rs/oxigraph/
- https://github.com/oxigraph/oxigraph/blob/main/LICENSE-APACHE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [llama.cpp](JAI-A3-01.md) | 96 | Adopt |
| 2 | [Ollama](JAI-A3-02.md) | 94 | Adopt |
| 3 | [vLLM](JAI-A3-03.md) | 90 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 5 | [llm (Simon Willison's CLI)](JAI-A3-12.md) | 85 | Adopt |
| 6 | [promptfoo](JAI-A3-14.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |

---

← 243. [Juriscraper](OSINT-C3-12.md) · 245. [py-wacz](OSINT-C1-43.md) →
