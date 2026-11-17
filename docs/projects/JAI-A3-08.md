# FAISS

`JAI-A3-08` · **80/100** · overall rank 158 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 63) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 10) |
| **Subcategory** | Vector search library |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Meta AI Research |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/facebookresearch/faiss) · [Documentation](https://faiss.ai/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 80/100**

---

## 1. Purpose

Library for efficient similarity search and clustering of dense vectors, with many index types trading memory against accuracy and speed, and GPU acceleration.

## Journalism / investigative use case

In-process vector search with no service to run: embed a corpus, build a FAISS index, and query it from the same Python process — the right level of infrastructure for a single investigation's document set, and what sentence-transformers examples assume.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- No service to operate: an index is a file and a process, which suits per-investigation corpora and air-gapped machines where running a database is impractical
- Wide range of index types lets you trade memory for accuracy explicitly, which matters when a corpus must fit on available hardware
- MIT licensed with very active maintenance (v1.16.0, 2026-11-10; pushed 2026-11-17) and long institutional backing (41,767 stars)
- The reference implementation in this space, so its behaviour is well understood and widely documented

## 5. Cons

- No metadata filtering: FAISS searches vectors, so 'similar passages from 2019 only' requires filtering outside the index, which is awkward and slow at scale — Qdrant's main advantage
- No persistence model beyond saving index files, so updates, deletions and incremental additions need application-level handling
- Library-level: there is no API, no auth and no multi-user access, so sharing search with reporters means building something around it
- Index-type selection and training parameters materially affect recall, and a badly configured index silently misses results — which in investigative search is the dangerous failure

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 41,767 stars with release v1.16.0 (2026-11-10) and a push on 2026-11-17, MIT licence. Its status as the standard vector-search library is evident from its use across the ecosystem including txtai and sentence-transformers examples.

## 7. Assessment

Adopt it for per-investigation corpora and scripted analysis, and move to Qdrant or pgvector when you need filtering, persistence or multi-user access. For your profile the practical warning is recall: an approximate index can silently omit relevant passages, so for completeness-sensitive work either use an exact index (feasible for modest corpora) or pair semantic search with keyword search and tell reporters that neither alone is exhaustive.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.16.0 (2026-11-10), 41,767 stars, MIT licence. Same-day commits with regular releases under long-term corporate research maintenance.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/facebookresearch/faiss/blob/main/LICENSE

## 10. Costs

No fee. RAM proportional to vectors and index type; GPU optional. No service infrastructure. Estimate.

## 11. Privacy and data flows

In-process and local; index files stay with you. Suitable for air-gapped work.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Qdrant](JAI-A3-07.md) where metadata filtering and persistence matter
- pgvector to keep vectors beside relational data
- HNSWlib for a lighter approximate-nearest-neighbour library

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/facebookresearch/faiss
- https://faiss.ai/
- https://github.com/facebookresearch/faiss/blob/main/LICENSE

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

← 157. [Tor Browser Launcher](SUR-B3-29.md) · 159. [wetterdienst](OSINT-C2-42.md) →
