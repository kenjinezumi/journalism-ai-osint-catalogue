# txtai

`JAI-A2-55` · **85/100** · overall rank 100 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 42) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 24) |
| **Subcategory** | Semantic search framework |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | NeuML |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/neuml/txtai) · [Documentation](https://neuml.github.io/txtai/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Varies by the model selected; not individually verified. |
| **Restrictions** | Code unrestricted. Licence risk is imported with whichever embedding or LLM model you configure. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. GPU recommended for bulk embedding; FAISS/HNSW indexes are local files. If you configure a hosted LLM provider you incur its token charges — not priced here. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/neuml/txtai/blob/master/LICENSE
- https://github.com/neuml/txtai
- https://neuml.github.io/txtai/

---

## 1. Purpose

All-in-one embeddings database and workflow framework combining vector search, sparse/hybrid search, graph components, pipelines for summarisation and transcription, and an API server.

## Journalism / investigative use case

A single dependency that gives a small newsroom semantic search, clustering and summarisation over an extracted corpus without assembling four separate systems — the pragmatic answer when there is no engineering team to integrate sentence-transformers, FAISS, a search API and a UI.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Breadth per unit of integration effort is the selling point: index, hybrid search, graph and pipelines in one package, which suits a one-engineer newsroom
- Hybrid sparse-plus-dense search addresses semantic search's recall problem better than pure vector search, which matters when you must evidence completeness
- Very actively developed (v9.14.0, 2026-10-06) with an exceptionally clean tracker (40 open issues against 13,555 stars)
- Apache-2.0 with a local-first default and an embeddable API server

## 5. Cons

- Breadth means you inherit opinions: the pipeline abstractions are convenient until you need something slightly different, at which point assembling the components yourself would have been simpler
- GPU recommended for embedding large corpora; CPU indexing of a leak-scale corpus is slow
- If LLM summarisation pipelines are enabled, outputs can hallucinate and must never be quoted without checking the source document — the framework makes this easy to enable and easy to forget
- Model licences depend entirely on what you select and were not individually verified

## 6. Feedback (documented)

No individual user reports verified. Documented: 13,555 stars with 40 open issues and a release on 2026-10-06 — a strong issue-throughput signal for a framework of this scope. No journalism deployment verified.

## 7. Assessment

A good fit for your profile specifically where time-to-capability matters more than architectural control: it collapses a week of integration into a day. I would use it for an internal research index over an already-extracted corpus, with local models only and LLM pipelines disabled by default. For a long-lived flagship archive I would still prefer explicit components (Solr or OpenSearch plus sentence-transformers) because you will eventually need to control each layer.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v9.14.0 (2026-10-06), 13,555 stars, 40 open issues. High release cadence on a 9.x line with a very small backlog.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Varies by the model selected; not individually verified.

**Restrictions:** Code unrestricted. Licence risk is imported with whichever embedding or LLM model you configure.

**Licence evidence:** https://github.com/neuml/txtai/blob/master/LICENSE

## 10. Costs

No fee. GPU recommended for bulk embedding; FAISS/HNSW indexes are local files. If you configure a hosted LLM provider you incur its token charges — not priced here. Estimate.

## 11. Privacy and data flows

Fully local with local models. The configuration risk is explicit: pointing it at hosted LLM or embedding providers sends document text off-site. Review the configuration before processing source material.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [sentence-transformers](JAI-A2-45.md) plus FAISS for explicit control
- [Datasette](JAI-A2-09.md) where the corpus is structured rather than textual
- [Apache Solr](JAI-A2-01.md) or OpenSearch for full-document scale with mature operations

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/neuml/txtai
- https://neuml.github.io/txtai/
- https://github.com/neuml/txtai/blob/master/LICENSE

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

← 99. [Tesseract OCR](JAI-A2-54.md) · 101. [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) →
