# Qdrant

`JAI-A3-07` · **82/100** · overall rank 134 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 56) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 9) |
| **Subcategory** | Vector database |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Qdrant |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/qdrant/qdrant) · [Documentation](https://qdrant.tech/documentation/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 82/100**

---

## 1. Purpose

Vector similarity search engine and database written in Rust, with payload filtering, quantisation, snapshots, distributed deployment and a REST and gRPC API.

## Journalism / investigative use case

The storage layer for semantic search over a document archive: millions of passage embeddings with metadata filters, so a reporter can search semantically within a date range or a specific document set rather than across everything.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Payload filtering combined with vector search is the feature that matters for investigative use: 'semantically similar passages, but only in documents from this ministry in 2019' is a normal journalistic query and a hard technical one
- Rust implementation with quantisation support keeps memory requirements manageable at millions of vectors, which decides whether a corpus fits on your hardware
- Apache-2.0 with very active maintenance (v1.20.2, 2026-11-16; pushed 2026-11-17) and strong adoption (35,603 stars)
- Snapshots make the index backup-able and portable, which matters when the index represents substantial embedding compute

## 5. Cons

- Another stateful service to operate alongside whatever search engine you already run — and for many newsroom corpora, a vector extension in OpenSearch or pgvector avoids that
- Commercial company with a managed cloud offering, the usual open-core direction consideration
- Embedding storage is only as good as the embedding model, and switching models means re-embedding the entire corpus — a cost that is easy to underestimate when choosing a model
- At small corpus sizes (tens of thousands of documents) a dedicated vector database is unnecessary overhead compared with FAISS or an in-memory index

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 35,603 stars with release v1.20.2 (2026-11-16) and a push on 2026-11-17, Apache-2.0. Strong adoption in the RAG ecosystem is evident from the metrics.

## 7. Assessment

Adopt it when your corpus genuinely needs a vector database — millions of passages with filtered search — and use pgvector or FAISS below that threshold. For your profile the decision that costs most is the embedding model, not the database: choose it once with care (multilingual-e5-large is a reasonable default with a clear licence), because re-embedding a leak-scale corpus is days of GPU time. Keep the index on infrastructure you control.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.20.2 (2026-11-16), 35,603 stars, Apache-2.0. Same-day commits and frequent releases under well-funded commercial maintenance.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a. Embeddings are derived from your documents using a model whose licence applies to that use.

**Restrictions:** None material for the database. The managed cloud service is a separate commercial product.

**Licence evidence:** https://github.com/qdrant/qdrant/blob/master/LICENSE

## 10. Costs

No fee for self-hosting. Infrastructure: RAM-proportional to vector count (quantisation reduces this substantially) plus disk — one VM for several million vectors. Managed cloud priced separately (not verified). Estimate.

## 11. Privacy and data flows

Self-hosted, local, no external calls. The index itself is disclosive about your corpus, so it needs the same protection as the documents.

## 12. Verdict

**Integrate**

## 13. Alternatives

- pgvector if you already run PostgreSQL — usually the right answer below millions of vectors
- [FAISS](JAI-A3-08.md) for an in-process index with no service to operate
- OpenSearch or Solr vector search if you already run one for keyword search

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/qdrant/qdrant
- https://qdrant.tech/documentation/
- https://github.com/qdrant/qdrant/blob/master/LICENSE

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

← 133. [webchanges](SUR-B1-17.md) · 135. [Blacklight collector](SUR-B2-02.md) →
