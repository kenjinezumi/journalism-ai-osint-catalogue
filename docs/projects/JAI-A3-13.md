# Ragas

`JAI-A3-13` · **75/100** · overall rank 211 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 85) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 14) |
| **Subcategory** | RAG evaluation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Vibrant Labs AI (transferred from explodinggradients) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/vibrantlabsai/ragas) · [Documentation](https://docs.ragas.io/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Evaluation framework for retrieval-augmented generation measuring faithfulness, answer relevance, context precision and recall, with synthetic test-set generation and support for custom metrics.

## Journalism / investigative use case

Answering the question an editor should ask before any AI document tool is trusted: how often does it produce an answer unsupported by the retrieved documents? Ragas' faithfulness metric measures exactly that, which is the difference between deploying a RAG system on evidence and on hope.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Faithfulness measurement addresses the specific failure that matters in journalism — an answer not supported by the source — rather than general quality, so the metric maps onto editorial risk
- Synthetic test-set generation lowers the barrier to having any evaluation at all, which most deployments skip entirely
- Apache-2.0 with active maintenance (v0.4.4, 2026-11-14; pushed 2026-11-14) and substantial adoption (16,354 stars)
- Transfer verified this session: explodinggradients/ragas now redirects to vibrantlabsai/ragas, so the canonical path is current

## 5. Cons

- Most metrics use a language model as judge, so you are evaluating one model's output with another model's judgement — useful as a relative signal, weak as an absolute measure, and this is routinely over-interpreted
- Governance moved to a company (transfer verified 2026-11-17), which is a direction-and-continuity item to monitor for a project you would depend on for assurance
- Synthetic test sets are generated from your documents by a model, so they inherit its blind spots; a human-written evaluation set from real reporting questions is substantially better
- Running evaluation costs inference, and a thorough evaluation over a large corpus is a real compute expense

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 16,354 stars, release v0.4.4 (2026-11-14), pushed the same day, Apache-2.0; the repository transfer explodinggradients/ragas → vibrantlabsai/ragas was confirmed by API redirect on 2026-11-17 and recorded in leads.md L10.

## 7. Assessment

Adopt the practice of measuring faithfulness before trusting any RAG system, and use Ragas as the convenient way to do it — while building a human-written evaluation set from your own reporting questions as the authoritative measure. For your profile the number worth putting in front of an editor is the faithfulness rate on your own corpus: if the system produces unsupported answers in a meaningful fraction of cases, that is a reason to restrict it to retrieval-with-citations rather than generated answers.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v0.4.4 published the same day, 16,354 stars, Apache-2.0, with the organisation transfer confirmed by redirect. Active releases; the governance change is the item to watch.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a for the library; judge models carry their own terms and costs.

**Restrictions:** None material. Note the organisation transfer when recording provenance.

**Licence evidence:** https://github.com/vibrantlabsai/ragas/blob/main/LICENSE

## 10. Costs

Library free. Evaluation consumes model inference — with a local model this is GPU time, with a hosted judge it is per-token charges (not priced here). A thorough evaluation of a large corpus is a real expense. Estimate.

## 11. Privacy and data flows

Depends on the judge model: a local judge keeps your documents and answers internal, a hosted judge sends both to that provider — which for source material would be a serious disclosure made in the name of quality assurance.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- LLM-as-judge metrics are relative signals, not absolute measures; a hosted judge would disclose source documents

## 13. Alternatives

- A hand-written evaluation set with manual scoring, which is more laborious and more trustworthy
- [promptfoo](JAI-A3-14.md) for broader prompt and model comparison
- DeepEval as an alternative evaluation framework

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/vibrantlabsai/ragas
- https://docs.ragas.io/
- `../sources/evidence/leads.md`

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

← 210. [python-overpy](OSINT-C2-25.md) · 212. [sugartrail](OSINT-C3-19.md) →
