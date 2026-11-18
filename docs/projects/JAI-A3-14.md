# promptfoo

`JAI-A3-14` · **85/100** · overall rank 96 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 39) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 6) |
| **Subcategory** | LLM evaluation and red-teaming |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | promptfoo |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/promptfoo/promptfoo) · [Documentation](https://www.promptfoo.dev/docs/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the tool; evaluated models carry their own terms. |
| **Restrictions** | None material for the open tool. Enterprise features and hosted services are separate commercial offerings. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Tool free. Evaluation consumes inference across every model and case combination — the main cost, and it scales multiplicatively. Local models make it a GPU-time expense rather than a per-token one. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/promptfoo/promptfoo/blob/main/LICENSE
- https://github.com/promptfoo/promptfoo
- https://www.promptfoo.dev/docs/

---

## 1. Purpose

Command-line and library tool for evaluating and comparing prompts, models and RAG configurations against test cases, with assertion types, side-by-side comparison and red-teaming for safety and prompt-injection testing.

## Journalism / investigative use case

Deciding which model and prompt to use, with evidence: run the same set of real newsroom tasks across several local models and prompt variants and compare outputs side by side — rather than choosing a model because it was in the news. The prompt-injection testing is separately valuable when documents come from hostile sources.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Side-by-side comparison across models and prompts on your own tasks is exactly how this decision should be made, and almost nobody does it — this makes it cheap enough to actually do
- Prompt-injection and red-teaming features address a genuine newsroom threat: a leaked document containing instructions aimed at your AI pipeline is a realistic attack, and testing for it is prudent
- MIT licensed with very active maintenance (0.125.1, 2026-10-25; pushed 2026-11-17) and strong adoption (27,370 stars)
- Configuration-as-YAML means an evaluation is a version-controlled artefact you can rerun when a model changes

## 5. Cons

- Assertion design is where the work is: a weak test set produces a confident wrong conclusion about which model is better, and the tool cannot supply domain judgement
- Commercial company with an enterprise offering, so some features and the hosted path are paid — check the boundary before depending on something
- Evaluation runs cost inference, and comparing several models across many cases multiplies that
- Red-teaming output needs interpretation: a model that fails an injection test may still be fine behind proper input handling, and vice versa

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 27,370 stars with release 0.125.1 (2026-10-25), pushed 2026-11-17, MIT licence. Strong adoption is evident; the enterprise offering is documented by the vendor.

## 7. Assessment

Adopt it for two specific decisions: which local model to standardise on, and whether your document-processing prompts are vulnerable to injection from hostile source material. For your profile the prompt-injection angle deserves emphasis — a newsroom pipeline that summarises documents from unknown sources is a realistic injection target, and a document instructing your model to exfiltrate or misreport is a plausible attack that nobody tests for. Build the evaluation set from real tasks.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 0.125.1 (2026-10-25), 27,370 stars, MIT licence. Same-day commits with a frequent release cadence under commercial maintenance.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the tool; evaluated models carry their own terms.

**Restrictions:** None material for the open tool. Enterprise features and hosted services are separate commercial offerings.

**Licence evidence:** https://github.com/promptfoo/promptfoo/blob/main/LICENSE

## 10. Costs

Tool free. Evaluation consumes inference across every model and case combination — the main cost, and it scales multiplicatively. Local models make it a GPU-time expense rather than a per-token one. Estimate.

## 11. Privacy and data flows

Evaluations run against whichever models you configure; using hosted providers sends your test cases (which may contain real document content) to them. Build evaluation sets from non-sensitive material, or use local models only.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Ragas](JAI-A3-13.md) for RAG-specific faithfulness metrics
- [Inspect AI](JAI-A3-15.md) for a more rigorous evaluation framework
- Manual side-by-side review of a dozen real cases, which is cruder and often sufficient to make the decision

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/promptfoo/promptfoo
- https://www.promptfoo.dev/docs/
- https://github.com/promptfoo/promptfoo/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [llama.cpp](JAI-A3-01.md) | 96 | Adopt |
| 2 | [Ollama](JAI-A3-02.md) | 94 | Adopt |
| 3 | [vLLM](JAI-A3-03.md) | 90 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 5 | [llm (Simon Willison's CLI)](JAI-A3-12.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |
| 9 | [Qdrant](JAI-A3-07.md) | 82 | Integrate |

---

← 95. [PMTiles](JAI-A1-24.md) · 97. [Quarto](OSINT-C3-39.md) →
