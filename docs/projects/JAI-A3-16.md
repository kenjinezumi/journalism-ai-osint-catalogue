# RDFLib

`JAI-A3-16` · **70/100** · overall rank 269 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 106) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 18) |
| **Subcategory** | Knowledge graphs |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | RDFLib team |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/RDFLib/rdflib) · [Documentation](https://rdflib.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 70/100**

---

## 1. Purpose

Python library for working with RDF: parsers and serialisers for many formats, an in-memory and pluggable store, SPARQL 1.1 query and update support, and graph manipulation.

## Journalism / investigative use case

Working with linked-data sources an investigation actually encounters: querying Wikidata via SPARQL for structured facts about companies and officials, consuming government linked-data releases, or building a small RDF graph that connects entities across datasets with explicit, inspectable relationships.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- SPARQL support means you can query Wikidata directly for structured entity data — company registrations, officeholders, ownership statements — which is a substantial free data source for investigations
- Explicit triple-based relationships make a knowledge graph auditable: every edge has a stated provenance and type, unlike an inferred embedding-based relation
- BSD-3-Clause with long-term active maintenance (7.6.0 released 2026-02-13; pushed 2026-11-17) and a stable community (2,563 stars)
- Format breadth means you can consume whatever serialisation a government or academic source publishes

## 5. Cons

- RDF has a steep conceptual overhead for the payoff in most newsroom work: for connecting entities across two datasets, a relational table or a property graph is usually simpler and clearer
- In-memory store limits graph size, and scaling means a triple store (Oxigraph, Jena) which is another service to run
- SPARQL is unfamiliar to most data journalists, so the practical barrier is skills rather than software
- Release cadence is slow (February 2026 release against November commits), consistent with a mature library but awkward for pinning

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 2,563 stars with release 7.6.0 (2026-02-13), pushed 2026-11-17, BSD-3-Clause. RDFLib is the standard Python RDF library, which is well established in the linked-data ecosystem.

## 7. Assessment

Integrate it specifically for Wikidata and linked-data access rather than as a knowledge-graph strategy — querying Wikidata for structured entity facts is the concrete, high-value use and it does not require adopting RDF for your own data. For your profile I would keep investigation graphs in FollowTheMoney or a property graph where the vocabulary fits investigative practice, and use RDFLib as the bridge to external structured sources.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 7.6.0 (2026-02-13), 2,563 stars, BSD-3-Clause. Same-day commits on a mature library with a slow deliberate release cadence — stability rather than stagnation.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** n/a. Wikidata content is CC0; other linked-data sources vary.

**Restrictions:** None material for the library. Note that Wikidata's CC0 licensing makes it unusually safe to build on, which is part of its value.

**Licence evidence:** https://github.com/RDFLib/rdflib/blob/main/LICENSE

## 10. Costs

No fee, negligible resources for modest graphs. A triple store for larger graphs is additional infrastructure. Estimate.

## 11. Privacy and data flows

Local library. SPARQL queries to Wikidata or another endpoint disclose your queries to that endpoint — relevant if the entities you are researching are sensitive, in which case a local Wikidata mirror is the alternative.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Direct SPARQL HTTP queries to Wikidata without the library, for simple lookups
- FollowTheMoney plus nomenklatura for investigative entity modelling
- [Oxigraph](JAI-A3-17.md) as a lightweight triple store when the graph outgrows memory

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/RDFLib/rdflib
- https://rdflib.readthedocs.io/
- https://github.com/RDFLib/rdflib/blob/main/LICENSE

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

← 268. [Pelias](OSINT-C2-30.md) · 270. [sigma.js](OSINT-C3-34.md) →
