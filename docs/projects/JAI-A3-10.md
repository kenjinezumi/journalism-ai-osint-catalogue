# LangGraph

`JAI-A3-10` · **74/100** · overall rank 231 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 94) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 16) |
| **Subcategory** | Agent orchestration |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | LangChain Inc. |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/langchain-ai/langgraph) · [Documentation](https://langchain-ai.github.io/langgraph/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 3/5 · usability 3/5 · licence+cost 5/5 → **weighted 74/100**

---

## 1. Purpose

Library for building stateful, multi-step language-model applications as explicit graphs with persistence, human-in-the-loop interrupts, checkpointing and streaming.

## Journalism / investigative use case

Research-agent workflows where a human must be able to intervene: a multi-step document-analysis process that pauses for a reporter to approve or correct an intermediate conclusion before continuing — which is the only responsible shape for an agentic system in journalism.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Human-in-the-loop interrupts are first-class rather than bolted on, which is precisely the control journalism needs: the system stops and asks rather than proceeding on a wrong inference
- Explicit graph structure and checkpointing make a multi-step process inspectable and resumable, so you can audit what the system did at each step — essential if its output informs a story
- MIT licensed with very active development (1.2.22, 2026-11-14; pushed 2026-11-17) and strong adoption (45,068 stars)
- State persistence means a long-running analysis survives interruption, which matters for corpus-scale work

## 5. Cons

- Agentic complexity is the central risk: a graph with several model-driven decision points is hard to explain and hard to test, and journalism needs explicable processes more than capable ones
- Inherits LangChain's ecosystem and company, including the paid platform for deployment and observability — so the production path leads toward a commercial service
- Building reliable agents requires substantial evaluation work the framework does not do, and the gap between a working demo and a trustworthy tool is large
- Rapid development pace means pinning is necessary and patterns change between versions

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 45,068 stars with release 1.2.22 (2026-11-14), pushed 2026-11-17, MIT licence. Strong adoption is clear from the metrics; the agentic-reliability concern is a general property of the approach rather than a defect of this implementation.

## 7. Assessment

Pilot it for one well-scoped workflow with mandatory human checkpoints — for example a document-triage process that proposes classifications a reporter confirms. For your profile the governing principle should be that an agent may gather and propose but never conclude: every published claim traces to a human decision with the evidence in front of them. Used that way LangGraph's interrupt model is genuinely useful; used to automate judgement it is a liability.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 1.2.22 (2026-11-14), 45,068 stars, MIT licence. Same-day commits and frequent releases under commercial maintenance.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the framework; models carry their own terms.

**Restrictions:** Framework unrestricted. LangGraph Platform is a separate commercial offering.

**Licence evidence:** https://github.com/langchain-ai/langgraph/blob/main/LICENSE

## 10. Costs

Framework free. Model inference is the cost — multi-step agents multiply token or GPU consumption per task, often by an order of magnitude over a single call, which is easy to underestimate. Estimate.

## 11. Privacy and data flows

Configuration-dependent as with LangChain: local models keep everything internal, hosted providers do not. Checkpointed state persists intermediate content, so the state store needs the same protection as the source documents.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [smolagents](JAI-A3-11.md) for a much smaller agent framework with less machinery
- A plain scripted pipeline with explicit human review steps, which is often sufficient and always clearer
- [Haystack](JAI-A3-05.md) pipelines where the task is retrieval rather than multi-step reasoning

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/langchain-ai/langgraph
- https://langchain-ai.github.io/langgraph/
- https://github.com/langchain-ai/langgraph/blob/main/LICENSE

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

← 230. [LangChain](JAI-A3-09.md) · 232. [M-Lab NDT server, ndt7 client and MSAK](SUR-B1-11.md) →
