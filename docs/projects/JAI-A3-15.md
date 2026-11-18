# Inspect AI

`JAI-A3-15` · **77/100** · overall rank 190 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 77) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 11) |
| **Subcategory** | LLM evaluation |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | UK AI Security Institute (UKGovernmentBEIS) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/UKGovernmentBEIS/inspect_ai) · [Documentation](https://inspect.aisi.org.uk/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 77/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the framework; evaluated models carry their own terms. |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Framework free. Evaluation inference is the cost; rigorous evaluation over many samples is substantial. Local models convert this to GPU time. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/LICENSE
- https://github.com/UKGovernmentBEIS/inspect_ai
- https://inspect.aisi.org.uk/

---

## 1. Purpose

Framework for large language model evaluations with datasets, solvers, scorers and a log viewer, designed for rigorous and reproducible evaluation including multi-turn and tool-use tasks.

## Journalism / investigative use case

Building a defensible evaluation of whether a model is fit for an editorial task: a structured, reproducible evaluation with a viewable log of every sample, which is what you want when the question 'can we trust this for fact-checking support' has to be answered to an editor rather than asserted.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Built by a government AI-safety institute for rigorous evaluation, so the design prioritises reproducibility and auditability over convenience — which is the right priority for a journalism assurance question
- The log viewer makes every sample inspectable, so you can read the actual failures rather than only a score, and failures are where the editorial judgement lives
- MIT licensed with very active maintenance (0.3.290, 2026-11-14; pushed 2026-11-17) and institutional backing
- Supports tool use and multi-turn evaluation, so agentic workflows can be evaluated rather than only single prompts

## 5. Cons

- Smaller community than promptfoo (3,276 stars) and oriented to AI-safety research conventions, so there is less newsroom-adjacent material and more conceptual overhead
- Rigour costs effort: defining datasets, solvers and scorers properly is a project, not an afternoon, and a half-built Inspect evaluation is no better than a quick promptfoo comparison
- Very high release number with frequent releases, so pinning is essential
- Evaluation inference costs apply as with any evaluation framework

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,276 stars with release 0.3.290 (2026-11-14), pushed 2026-11-17, MIT licence, maintained by the UK AI Security Institute. The institutional provenance is unusual in this category and is the main reason to take it seriously despite the smaller community.

## 7. Assessment

Worth adopting when an AI deployment decision needs to be defensible rather than merely informed — for example before placing a model anywhere near fact-checking or source-material triage. For your profile the practical split is promptfoo for quick comparative decisions and Inspect for the one or two evaluations you would want to show an editor, a funder or a court. The log viewer is the feature that makes an evaluation persuasive to a non-technical reader.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 0.3.290 (2026-11-14), 3,276 stars, MIT licence. Same-day commits with a very frequent release cadence under government-institute maintenance.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the framework; evaluated models carry their own terms.

**Restrictions:** None material.

**Licence evidence:** https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/LICENSE

## 10. Costs

Framework free. Evaluation inference is the cost; rigorous evaluation over many samples is substantial. Local models convert this to GPU time. Estimate.

## 11. Privacy and data flows

Runs against configured models; a local model keeps evaluation content internal. Logs contain full samples, so if your evaluation uses real document content the logs need protecting accordingly.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [promptfoo](JAI-A3-14.md) for faster, lighter comparative evaluation
- [Ragas](JAI-A3-13.md) for RAG-specific faithfulness metrics
- lm-evaluation-harness for standard academic benchmarks, which are less relevant to newsroom tasks

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/UKGovernmentBEIS/inspect_ai
- https://inspect.aisi.org.uk/
- https://github.com/UKGovernmentBEIS/inspect_ai/blob/main/LICENSE

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

← 189. [Zoekplaatje](OSINT-C1-11.md) · 191. [MLflow](JAI-A3-19.md) →
