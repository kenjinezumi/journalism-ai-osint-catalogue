# llm (Simon Willison's CLI)

`JAI-A3-12` · **85/100** · overall rank 91 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 36) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 5) |
| **Subcategory** | LLM command-line tooling |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Simon Willison |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/simonw/llm) · [Documentation](https://llm.datasette.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the tool; models and providers carry their own terms. |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Tool free. Model costs depend on the backend — local inference on your GPU, or hosted per-token charges (not priced here). Negligible tool overhead.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/simonw/llm/blob/main/LICENSE
- https://github.com/simonw/llm
- https://llm.datasette.io/

---

## 1. Purpose

Command-line tool and Python library for interacting with language models — local and remote — with a plugin system, prompt templates, logging of every prompt and response to SQLite, and piping into shell workflows.

## Journalism / investigative use case

Scriptable AI in a shell pipeline with an audit trail: pipe a document into a model, get structured output, and have every prompt and response automatically logged to SQLite — which means an AI-assisted analysis has a complete, queryable record of exactly what was asked and answered.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Automatic SQLite logging of every prompt and response is the standout feature for journalism: it gives you a provenance record of AI use without any discipline required from the user, and you can query it later with Datasette
- Shell-pipeline design composes with the rest of a Unix toolkit, so AI becomes one step in a pipeline rather than a separate application
- Apache-2.0 with very active maintenance (0.37.3, 2026-11-16; pushed 2026-11-17) and a plugin ecosystem covering local models (llama.cpp, Ollama) and hosted providers
- Prompt templates make a repeatable extraction task into a saved, version-controllable artefact

## 5. Cons

- CLI-first, so it serves engineers and terminal-comfortable analysts rather than reporters
- The logging database accumulates the full content of every prompt — which for source documents means a second copy of sensitive material in an easily overlooked location that needs the same protection as the originals
- Plugin quality varies, and model-specific features are exposed unevenly across providers
- Single-maintainer project, though with an exceptional track record of long-term care

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 12,769 stars, release 0.37.3 (2026-11-16), pushed 2026-11-17, Apache-2.0. The prompt-logging design is documented by the maintainer and is unusual among LLM tools.

## 7. Assessment

Adopt it as the standard way your team invokes models from a shell, largely for the audit trail — being able to show exactly which prompt produced a figure is the difference between an explicable method and an assertion. For your profile there is one control to apply immediately: the logs database contains full document content, so put it on encrypted storage with the same access restrictions as your source material, and set a retention policy. People forget it exists.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 0.37.3 (2026-11-16), 12,769 stars, Apache-2.0. Same-day commits and a release within a day of the survey, from a maintainer with a long record of sustained project care.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a for the tool; models and providers carry their own terms.

**Restrictions:** None material.

**Licence evidence:** https://github.com/simonw/llm/blob/main/LICENSE

## 10. Costs

Tool free. Model costs depend on the backend — local inference on your GPU, or hosted per-token charges (not priced here). Negligible tool overhead.

## 11. Privacy and data flows

Depends on the configured model: local plugins keep everything internal, hosted providers do not. The specific privacy item to manage is the SQLite log, which stores full prompt and response content and therefore constitutes a copy of whatever documents you processed.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Direct HTTP calls to a local OpenAI-compatible endpoint, without the logging benefit
- [LangChain](JAI-A3-09.md) where provider abstraction inside an application matters more than shell composition
- [Ollama](JAI-A3-02.md)'s own CLI for simple interactive use

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/simonw/llm
- https://llm.datasette.io/
- https://github.com/simonw/llm/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [llama.cpp](JAI-A3-01.md) | 96 | Adopt |
| 2 | [Ollama](JAI-A3-02.md) | 94 | Adopt |
| 3 | [vLLM](JAI-A3-03.md) | 90 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 6 | [promptfoo](JAI-A3-14.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |
| 9 | [Qdrant](JAI-A3-07.md) | 82 | Integrate |

---

← 90. [Haystack](JAI-A3-05.md) · 92. [MapLibre GL JS](JAI-A1-22.md) →
