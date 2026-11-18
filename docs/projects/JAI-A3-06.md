# RAGFlow

`JAI-A3-06` · **85/100** · overall rank 98 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 40) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 7) |
| **Subcategory** | RAG platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | InfiniFlow |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/infiniflow/ragflow) · [Documentation](https://ragflow.io/docs/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Embedded parsing and embedding models carry their own licences and were NOT individually verified in this survey. |
| **Restrictions** | Platform permissive. Verify the licences of bundled or auto-downloaded models before commercial publication of derived work. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure estimate: a multi-container deployment plus a vector store and a GPU for local models — comparable to running a search platform. Hosted option priced separately (not verified). Assumptions: self-hosted, moderate corpus.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/infiniflow/ragflow/blob/main/LICENSE
- https://github.com/infiniflow/ragflow
- https://ragflow.io/docs/

---

## 1. Purpose

Deployable RAG platform with deep document understanding, a web interface for corpus management and chat, visual chunking inspection, citation display and agent workflows.

## Journalism / investigative use case

Giving reporters a working document-chat interface without building one: deploy RAGFlow, upload a corpus, and a journalist can ask questions and see which passages the answer came from — with the chunking visible, so you can diagnose why a bad answer happened.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- A complete product rather than a framework: reporters get a usable interface immediately, which is the gap between RAG as an engineering project and RAG as a newsroom tool
- Visible chunking and citation display are genuinely well judged for this use case — being able to see what the system retrieved is how a journalist decides whether to trust an answer
- Apache-2.0 with very large adoption (94,307 stars), a 1.0 release (2026-11-06) and same-day commits, plus an almost empty issue tracker
- Self-hostable with local model support, so the whole system can stay inside the perimeter

## 5. Cons

- Heavy multi-service deployment (document parsing, vector store, web application, workers), so it is a platform commitment comparable to OpenAleph rather than a quick install
- Commercial company behind it with a hosted offering, so open-version feature boundaries warrant checking before you depend on something
- The polished interface invites uncritical use: a reporter seeing a fluent cited answer may not check the citations, which makes editorial guidance more important than with a developer-facing framework
- Deep-document-understanding components may pull models whose licences need verification, and the convenience of the pipeline obscures what is being used

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 94,307 stars with only 9 open issues, release v1.0.0 (2026-11-06), pushed 2026-11-17, Apache-2.0. The adoption scale and near-empty tracker are both notable; the hosted-offering relationship is documented by the vendor.

## 7. Assessment

Pilot it if you want reporters to have document chat and can support the deployment — it is the most complete self-hostable option and the citation visibility is the right design. For your profile the controls that matter are editorial rather than technical: train reporters that the citation is the answer and the prose is a convenience, and audit a sample of answers against the underlying documents before the tool is trusted on a live investigation. Verify which models the parsing pipeline pulls.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.0.0 (2026-11-06), 94,307 stars, 9 open issues. Same-day commits, a 1.0 milestone and a near-empty backlog at very large scale, under commercial maintenance.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Embedded parsing and embedding models carry their own licences and were NOT individually verified in this survey.

**Restrictions:** Platform permissive. Verify the licences of bundled or auto-downloaded models before commercial publication of derived work.

**Licence evidence:** https://github.com/infiniflow/ragflow/blob/main/LICENSE

## 10. Costs

No fee. Infrastructure estimate: a multi-container deployment plus a vector store and a GPU for local models — comparable to running a search platform. Hosted option priced separately (not verified). Assumptions: self-hosted, moderate corpus.

## 11. Privacy and data flows

Self-hostable with local models, which is the configuration to use for source material. Check that no component defaults to a hosted embedding or LLM provider.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [Haystack](JAI-A3-05.md) plus a simple interface for an auditable, engineer-controlled alternative
- [ICIJ Datashare](JAI-A2-23.md) or OpenAleph where search rather than generative answers is what reporters need
- [txtai](JAI-A2-55.md) for a much lighter semantic-search deployment

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/infiniflow/ragflow
- https://ragflow.io/docs/
- https://github.com/infiniflow/ragflow/blob/main/LICENSE

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
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |
| 9 | [Qdrant](JAI-A3-07.md) | 82 | Integrate |

---

← 97. [Quarto](OSINT-C3-39.md) · 99. [Tesseract OCR](JAI-A2-54.md) →
