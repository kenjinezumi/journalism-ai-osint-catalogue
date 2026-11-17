# smolagents

`JAI-A3-11` · **69/100** · overall rank 277 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 107) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 19) |
| **Subcategory** | Agent framework |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Hugging Face |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/huggingface/smolagents) · [Documentation](https://huggingface.co/docs/smolagents/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 69/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Minimal agent library where agents write and execute code to use tools, with a small core, support for many model backends and sandboxed execution options.

## Journalism / investigative use case

A deliberately small agent framework for research tasks: give a model a few tools (search your archive, fetch a page, run a calculation) and let it chain them, with little enough machinery that you can read the whole framework and understand what it did.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Minimal by design, so the framework is readable in an afternoon — which matters enormously when you must explain to an editor how an AI-assisted finding was produced
- Code-writing agents are a powerful pattern for data work: the agent can compute rather than guess, and the code it wrote is an auditable artefact
- Apache-2.0 from Hugging Face with strong adoption (30,404 stars) and active development (pushed 2026-11-17)
- Backend-agnostic, so it runs against a local model via llama.cpp or vLLM without modification

## 5. Cons

- Code-executing agents are a serious security consideration: an agent that writes and runs code on your infrastructure, with access to your archive, is an attack surface and needs sandboxing that the library supports but does not force
- Release cadence is uneven: v1.26.0 dates from 2026-05-29 against commits in November 2026, so the published release lags development considerably
- Minimalism means you build the guardrails: rate limits, tool permissions, output validation and human checkpoints are yours to add
- Agent reliability remains the fundamental issue — a code-writing agent can produce confidently wrong analysis, and the code it wrote looks authoritative

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 30,404 stars with release v1.26.0 (2026-05-29) against a push on 2026-11-17, Apache-2.0. The release-versus-commit gap is visible in the API data.

## 7. Assessment

The agent framework I would choose for your context, specifically because you can read it — explicability is worth more than capability in a newsroom tool. Two non-negotiables if you deploy it: sandbox code execution properly (container with no network and no access to source material unless explicitly mounted), and treat agent-written code as an artefact to review, since it is simultaneously the method and the thing that could be wrong. Pin to a commit given the release lag.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.26.0 (2026-05-29), 30,404 stars, Apache-2.0. Same-day commits with a release nearly six months old — active development, lagging release engineering.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a for the library; models carry their own terms.

**Restrictions:** None material.

**Licence evidence:** https://github.com/huggingface/smolagents/blob/main/LICENSE

## 10. Costs

Library free. Model inference costs apply and agent loops multiply them. Sandboxing infrastructure (containers or a dedicated VM) is a modest additional cost. Estimate.

## 11. Privacy and data flows

Local-model configuration keeps content internal. The sharper risk is the agent's own access: an agent with tools that read your archive and fetch URLs could exfiltrate content through a crafted request, so network egress from the sandbox should be denied by default.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Code-executing agents require deliberate sandboxing and egress denial before touching source material

## 13. Alternatives

- [LangGraph](JAI-A3-10.md) where explicit state machines and human interrupts are needed
- A scripted pipeline with no agent, which for most tasks is sufficient and fully predictable
- OpenHands or similar for software-engineering agents rather than research tasks

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/huggingface/smolagents
- https://huggingface.co/docs/smolagents/
- https://github.com/huggingface/smolagents/blob/main/LICENSE

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

← 276. [SiteOne Crawler](OSINT-C1-19.md) · 278. [4get](OSINT-C1-02.md) →
