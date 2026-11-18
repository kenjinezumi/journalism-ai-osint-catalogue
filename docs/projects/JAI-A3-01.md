# llama.cpp

`JAI-A3-01` · **96/100** · overall rank 2 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 1) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 1) |
| **Subcategory** | Local LLM inference |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Georgi Gerganov / ggml-org |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ggml-org/llama.cpp) · [Documentation](https://github.com/ggml-org/llama.cpp#readme) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 96/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the engine. Model weights carry their own licences, which vary enormously — this is where the licence risk in local AI actually sits. |
| **Restrictions** | Engine unrestricted. The engine licence does not launder a restricted model licence: running a non-commercial or restricted-weights model locally is still bound by those weights' terms. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. The cost is hardware: a GPU with sufficient VRAM for your chosen model (or substantial RAM for CPU inference at lower speed). One shared GPU host serves a small newsroom. Estimate; assumes self-hosted.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ggml-org/llama.cpp/blob/master/LICENSE
- https://github.com/ggml-org/llama.cpp

---

## 1. Purpose

C/C++ inference engine for large language models using the ggml/GGUF format, with quantisation, CPU and GPU backends across many platforms, and an OpenAI-compatible server.

## Journalism / investigative use case

The foundation of any newsroom AI capability that must not send documents to a vendor: run a capable instruction model on your own hardware for summarisation, claim extraction, translation assistance or redaction detection, with leaked material never leaving the building.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Makes local inference genuinely practical on ordinary hardware through aggressive quantisation — which is what turns 'we should process this locally' into something that finishes
- OpenAI-compatible server means tools written against hosted APIs (kuroi, Loki-style pipelines, your own code) can be pointed at your own model with a configuration change rather than a rewrite
- MIT licensed with extraordinary activity (135,527 stars, v1.0.0 released 2026-11-13, pushed 2026-11-17) and backends for CPU, CUDA, Metal, Vulkan and more
- Single binary with no Python dependency, so it deploys on a hardened or air-gapped machine where a framework install is impractical

## 5. Cons

- Fast-moving with frequent breaking changes in quantisation formats and server APIs, so pinning is essential and upgrades need testing — the 1.0.0 release is recent and the history before it was volatile
- Quantisation costs quality in ways that vary by model and task, and the loss is rarely measured by the people deploying it — a quantised model that summarises badly will do so plausibly
- Engineer-facing: you supply the model, choose the quantisation and operate the server, and model selection has more effect on output quality than anything the engine does
- Running a local model does not make its output reliable: hallucination is a property of the model, and local deployment removes the privacy problem without touching the accuracy one

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 135,527 stars with release v1.0.0 (2026-11-13) and a push on 2026-11-17, MIT licence. Its role as the standard local-inference engine is verifiable from the ecosystem built on it, including Ollama and most desktop LLM applications.

## 7. Assessment

Adopt it as the inference layer for every AI capability you want without a vendor — this is the single component that makes local AI a realistic newsroom choice. For your profile the right pattern is one GPU host running llama.cpp's OpenAI-compatible server, with every internal tool pointed at it, so the decision 'does this document leave the building' is made once in infrastructure rather than repeatedly by users. Pin the version, and evaluate your chosen quantisation on real tasks rather than assuming parity with the full model.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.0.0 (2026-11-13), 135,527 stars. Same-day commits at very high velocity with a newly reached 1.0; the maintenance concern is churn, not neglect.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the engine. Model weights carry their own licences, which vary enormously — this is where the licence risk in local AI actually sits.

**Restrictions:** Engine unrestricted. The engine licence does not launder a restricted model licence: running a non-commercial or restricted-weights model locally is still bound by those weights' terms.

**Licence evidence:** https://github.com/ggml-org/llama.cpp/blob/master/LICENSE

## 10. Costs

No fee. The cost is hardware: a GPU with sufficient VRAM for your chosen model (or substantial RAM for CPU inference at lower speed). One shared GPU host serves a small newsroom. Estimate; assumes self-hosted.

## 11. Privacy and data flows

Entirely local inference with no telemetry and no external calls — the whole point. Model weights are downloaded once and can be pre-staged for air-gapped operation.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Ollama](JAI-A3-02.md) for a much easier operational wrapper around the same engine
- [vLLM](JAI-A3-03.md) where GPU throughput for many concurrent requests matters more than footprint
- Hosted model APIs — appropriate only for non-sensitive material

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ggml-org/llama.cpp
- https://github.com/ggml-org/llama.cpp/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [Ollama](JAI-A3-02.md) | 94 | Adopt |
| 3 | [vLLM](JAI-A3-03.md) | 90 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 5 | [llm (Simon Willison's CLI)](JAI-A3-12.md) | 85 | Adopt |
| 6 | [promptfoo](JAI-A3-14.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |
| 9 | [Qdrant](JAI-A3-07.md) | 82 | Integrate |

---

← 1. [ExifTool](OSINT-C2-01.md) · 3. [mitmproxy](SUR-B2-06.md) →
