# Ollama

`JAI-A3-02` · **94/100** · overall rank 14 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 4) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 2) |
| **Subcategory** | Local LLM inference |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Ollama |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (application) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ollama/ollama) · [Documentation](https://docs.ollama.com/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 94/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Application that packages local model serving behind a simple CLI and HTTP API, handling model download, quantisation selection, memory management and concurrent requests, with an OpenAI-compatible endpoint.

## Journalism / investigative use case

The practical way to give a newsroom local AI: one command installs it, one command pulls a model, and every internal tool has an OpenAI-compatible endpoint on the local network — which is the difference between local AI being a project and being available.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Removes essentially all operational friction from local inference: model management, memory handling and serving are automatic, which is why it has become the default
- OpenAI-compatible API means existing tools work unchanged, so you can redirect a pipeline from a hosted provider to local inference by changing a base URL
- MIT licensed with enormous adoption (187,366 stars) and a very fast release cadence (v0.40.16, 2026-11-09; pushed 2026-11-17)
- Cross-platform desktop and server support, so a reporter can run a model on a laptop and the newsroom can run one on a server with the same interface

## 5. Cons

- Abstracts away quantisation and model-variant choices, which is convenient and means teams often do not know which quantisation they are running — and that affects output quality materially
- Model library convenience encourages pulling models without checking their licences: the library includes weights with restrictive terms alongside permissive ones, and the pull command does not make you read them
- Fast release cadence with occasional behavioural changes, so pin the version for anything production
- Defaults are tuned for convenience rather than for maximum throughput or minimum memory; a heavily used server benefits from vLLM or direct llama.cpp tuning

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 187,366 stars with release v0.40.16 (2026-11-09) and a push on 2026-11-17, MIT licence. Its position as the default local-model runner is evident from adoption scale.

## 7. Assessment

Adopt it — the usability gain is what actually gets local AI deployed, and deployment is the point. For your profile two governance items matter more than the technology. First, record which model and quantisation each workflow uses, because 'we summarised with a local model' is not a reproducible methodology. Second, check the licence of every model you pull: the convenience of `ollama pull` is exactly how a non-commercial-weights model ends up behind a published story.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v0.40.16 (2026-11-09), 187,366 stars, MIT licence. Same-day commits with near-weekly releases and commercial backing.

## 9. Licensing

**Licence:** MIT (application) _(SPDX verified)_

**Model / data licence:** VARIES AND MATTERS: models in the library carry their own licences, from Apache-2.0 and MIT through to restrictive community licences with usage conditions. Verify each model you pull.

**Restrictions:** Application unrestricted. The real exposure is model licences, which `ollama pull` does not surface prominently — a commercially operated newsroom must check each model's terms before output reaches publication.

**Licence evidence:** https://github.com/ollama/ollama/blob/main/LICENSE

## 10. Costs

No fee. Hardware is the cost: a GPU host for useful speed on larger models, or a capable laptop for small ones. One shared server serves a small newsroom. Estimate.

## 11. Privacy and data flows

Local inference with no document content leaving your infrastructure. Model pulls contact Ollama's registry, which discloses which models you fetch (not your data) and can be pre-staged for air-gapped use.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Model licences in the library vary and are easy to overlook — verify before publishing work derived from a pulled model

## 13. Alternatives

- [llama.cpp](JAI-A3-01.md) directly for control over quantisation and server behaviour
- [vLLM](JAI-A3-03.md) for high-throughput GPU serving
- Hosted APIs for non-sensitive work only

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ollama/ollama
- https://docs.ollama.com/
- https://github.com/ollama/ollama/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [llama.cpp](JAI-A3-01.md) | 96 | Adopt |
| 3 | [vLLM](JAI-A3-03.md) | 90 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 5 | [llm (Simon Willison's CLI)](JAI-A3-12.md) | 85 | Adopt |
| 6 | [promptfoo](JAI-A3-14.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |
| 9 | [Qdrant](JAI-A3-07.md) | 82 | Integrate |

---

← 13. [OCRmyPDF](JAI-A2-33.md) · 15. [PySceneDetect](OSINT-C2-10.md) →
