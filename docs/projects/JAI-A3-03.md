# vLLM

`JAI-A3-03` · **90/100** · overall rank 43 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 15) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 3) |
| **Subcategory** | Local LLM inference (serving) |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | vLLM project (PyTorch Foundation) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/vllm-project/vllm) · [Documentation](https://docs.vllm.ai/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 90/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the server; model weights carry their own licences. |
| **Restrictions** | Server unrestricted. Model licence obligations apply independently. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. GPU hardware or rental is the cost and it is the dominant one — a capable GPU host is the main AI infrastructure line in a newsroom budget. Estimate; assumes self-hosted.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/vllm-project/vllm/blob/main/LICENSE
- https://github.com/vllm-project/vllm
- https://docs.vllm.ai/

---

## 1. Purpose

High-throughput LLM inference and serving engine using paged attention and continuous batching, with an OpenAI-compatible API and support for many model architectures and quantisation schemes.

## Journalism / investigative use case

Serving a local model to a whole newsroom or processing a large document corpus: continuous batching means dozens of concurrent requests or a million-document extraction job complete in a fraction of the time a single-stream engine would take.

## 2. Audience

engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Throughput is the decisive advantage: for corpus-scale work (extracting entities or claims across a whole leak) vLLM's batching is the difference between days and hours on the same GPU
- OpenAI-compatible server, so it drops into the same architecture as Ollama or llama.cpp with better scaling characteristics
- Apache-2.0 under PyTorch Foundation governance with enormous activity (97,101 stars, v0.34.0 released 2026-11-16, pushed 2026-11-17)
- Required by several document tools in this catalogue (Marker, Surya, olmOCR), so you may need it regardless

## 5. Cons

- GPU-only and VRAM-hungry: it is server infrastructure, not something that runs on a reporter's laptop, so it complements rather than replaces llama.cpp
- Operationally heavier than Ollama — model loading, memory configuration and version-to-model compatibility all need attention, and mismatches fail confusingly
- Very fast release cadence with a large surface, so pinning and testing are necessary; model-architecture support changes between versions
- Python/CUDA dependency stack is the usual source of deployment pain, particularly in reproducible or air-gapped setups

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 97,101 stars with release v0.34.0 (2026-11-16) and a push on 2026-11-17, Apache-2.0 under PyTorch Foundation governance. Its use as the inference backend for Marker, Surya and olmOCR is verifiable from those projects' documentation.

## 7. Assessment

Adopt it where you have GPUs and either concurrency or corpus scale — that is the specific case it wins, and it wins decisively. For your profile the clean architecture is vLLM on the GPU server for batch and shared use, Ollama or llama.cpp on laptops for individual work, and the same OpenAI-compatible interface everywhere so tools do not care which they are talking to. Note that several document tools here require it, which may settle the decision for you.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v0.34.0 (2026-11-16), 97,101 stars, Apache-2.0. Same-day commits and releases under foundation governance with broad industry contribution.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a for the server; model weights carry their own licences.

**Restrictions:** Server unrestricted. Model licence obligations apply independently.

**Licence evidence:** https://github.com/vllm-project/vllm/blob/main/LICENSE

## 10. Costs

No fee. GPU hardware or rental is the cost and it is the dominant one — a capable GPU host is the main AI infrastructure line in a newsroom budget. Estimate; assumes self-hosted.

## 11. Privacy and data flows

Local serving with no external calls; documents stay on your infrastructure. Model weights downloaded once and pre-stageable.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Ollama](JAI-A3-02.md) for simpler operation at lower throughput
- [llama.cpp](JAI-A3-01.md) for CPU and laptop deployment
- SGLang as an alternative high-throughput server

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/vllm-project/vllm
- https://docs.vllm.ai/
- https://github.com/vllm-project/vllm/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [llama.cpp](JAI-A3-01.md) | 96 | Adopt |
| 2 | [Ollama](JAI-A3-02.md) | 94 | Adopt |
| 4 | [Haystack](JAI-A3-05.md) | 85 | Adopt |
| 5 | [llm (Simon Willison's CLI)](JAI-A3-12.md) | 85 | Adopt |
| 6 | [promptfoo](JAI-A3-14.md) | 85 | Adopt |
| 7 | [RAGFlow](JAI-A3-06.md) | 85 | Pilot |
| 8 | [LlamaIndex](JAI-A3-04.md) | 82 | Pilot |
| 9 | [Qdrant](JAI-A3-07.md) | 82 | Integrate |

---

← 42. [SingleFile](OSINT-C1-38.md) · 44. [spaCy](JAI-A2-47.md) →
