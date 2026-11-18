# LlamaIndex

`JAI-A3-04` · **82/100** · overall rank 132 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 55) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 8) |
| **Subcategory** | RAG framework |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | LlamaIndex Inc. |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/run-llama/llama_index) · [Documentation](https://docs.llamaindex.ai/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 82/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the framework; embedding models, rerankers and LLMs carry their own licences. |
| **Restrictions** | Framework unrestricted. Imported licence risk from the models you configure, and the hosted LlamaCloud platform operates under separate commercial terms. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Framework free. Costs are the model and embedding infrastructure (a GPU host) or, if you configure hosted providers, their per-token charges (not priced here). Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/run-llama/llama_index/blob/main/LICENSE
- https://github.com/run-llama/llama_index
- https://docs.llamaindex.ai/

---

## 1. Purpose

Data framework for retrieval-augmented generation: loaders for many sources, index structures, retrievers, rerankers, query engines and agent abstractions over document collections.

## Journalism / investigative use case

Building a question-answering interface over a document archive: a reporter asks 'what did the ministry say about the contract in 2019' and the system retrieves relevant passages and drafts an answer with citations back to specific documents. The citation requirement is what makes it usable in journalism at all.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Citation-aware retrieval is the feature that matters: an answer with document and page references can be checked, and an answer without them cannot be used in journalism
- Very large loader ecosystem, so getting a corpus into an index is usually configuration rather than code
- MIT licensed with enormous activity (52,926 stars, v0.14.26 released 2026-11-13, pushed 2026-11-14) and a well-funded maintainer
- Pluggable at every layer, so the whole pipeline — embeddings, vector store, model — can be local

## 5. Cons

- Abstraction churn is real: the framework has repeatedly reorganised its APIs and package structure, so code written a year ago often needs rewriting, and tutorials age badly
- RAG output remains model output: retrieved context reduces hallucination without eliminating it, and a confidently wrong answer with correct-looking citations is the characteristic failure mode — which is more dangerous in journalism than no answer
- Commercial company behind it with a hosted platform, so some convenient paths lead to paid services and feature direction follows the business
- Easy to build something impressive and unreliable: the framework makes a demo trivial and a trustworthy system hard, and the gap is mostly evaluation work it does not do for you

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 52,926 stars with release v0.14.26 (2026-11-13), pushed 2026-11-14, MIT licence. The API-churn pattern is visible in the project's own migration documentation across major versions.

## 7. Assessment

Use it, with an evaluation discipline attached: build a set of questions with known correct answers from your own corpus and measure retrieval and answer quality before anyone relies on the system. For your profile the architecture to insist on is fully local (local embeddings, local vector store, local model via vLLM) and citation-mandatory — an answer without a document reference should be suppressed rather than shown. Pin the version; this framework breaks across upgrades more than most.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v0.14.26 (2026-11-13), 52,926 stars, MIT licence. Very frequent releases under commercial maintenance; the churn that follows is the practical cost.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the framework; embedding models, rerankers and LLMs carry their own licences.

**Restrictions:** Framework unrestricted. Imported licence risk from the models you configure, and the hosted LlamaCloud platform operates under separate commercial terms.

**Licence evidence:** https://github.com/run-llama/llama_index/blob/main/LICENSE

## 10. Costs

Framework free. Costs are the model and embedding infrastructure (a GPU host) or, if you configure hosted providers, their per-token charges (not priced here). Estimate.

## 11. Privacy and data flows

Can be fully local, and for source material must be: the default convenience path uses hosted embedding and LLM providers, which would send your documents to them. Configure local components deliberately and verify no fallback to a hosted default.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Default configurations use hosted embedding and model providers — must be explicitly made local for source material

## 13. Alternatives

- [Haystack](JAI-A3-05.md) for a more stable, production-oriented RAG framework
- [txtai](JAI-A2-55.md) for a lighter all-in-one option
- Direct retrieval plus a prompt, which for many newsroom cases is sufficient and far more transparent

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/run-llama/llama_index
- https://docs.llamaindex.ai/
- https://github.com/run-llama/llama_index/blob/main/LICENSE

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
| 9 | [Qdrant](JAI-A3-07.md) | 82 | Integrate |

---

← 131. [katana](OSINT-C1-15.md) · 133. [webchanges](SUR-B1-17.md) →
