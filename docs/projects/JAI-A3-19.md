# MLflow

`JAI-A3-19` · **77/100** · overall rank 191 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 78) |
| **Segment** | A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation (rank 12) |
| **Subcategory** | Experiment tracking and provenance |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Databricks and community (Linux Foundation) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mlflow/mlflow) · [Documentation](https://mlflow.org/docs/latest/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 77/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. Databricks' managed MLflow is a separate commercial service. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Infrastructure: a tracking server, a database and artefact storage — one VM plus object storage for a newsroom. Managed offerings priced separately (not verified). Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/mlflow/mlflow/blob/master/LICENSE.txt
- https://github.com/mlflow/mlflow
- https://mlflow.org/docs/latest/

---

## 1. Purpose

Platform for machine-learning lifecycle management: experiment tracking, parameter and metric logging, artefact storage, model registry and, in recent versions, LLM tracing and evaluation.

## Journalism / investigative use case

Provenance for AI-assisted analysis: when a model classified ten thousand documents and three of those classifications informed a story, MLflow records which model version, parameters and prompt produced them — so an editor's question about how a finding was produced has a recorded answer rather than a recollection.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Experiment tracking turns AI-assisted analysis from an undocumented process into a recorded one, which is a genuine editorial requirement that almost no newsroom currently meets
- Model registry and artefact storage mean the exact model and parameters behind a published finding can be retrieved months later — the practical definition of reproducibility
- Apache-2.0 under Linux Foundation governance with very active development (v3.18.0, 2026-11-04; pushed 2026-11-17) and strong adoption (28,853 stars)
- LLM tracing support in recent versions extends the same provenance model to prompt-based work, which is where newsroom AI actually sits

## 5. Cons

- Designed for machine-learning teams, so the conceptual model (experiments, runs, registered models) takes translation to fit newsroom analysis workflows
- Operating a tracking server plus artefact storage is real infrastructure for a benefit that is organisational rather than immediately visible — it will be skipped unless someone insists
- Databricks' commercial interest shapes direction, and the managed offering is the vendor's product
- For simple prompt-based work, simonw/llm's SQLite logging gives most of the provenance benefit at a fraction of the effort

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 28,853 stars with release v3.18.0 (2026-11-04), pushed 2026-11-17, Apache-2.0 under Linux Foundation governance. Adoption in ML engineering is well established; journalism use is unestablished here.

## 7. Assessment

Worth adopting if you run model-based analysis at any scale, chiefly as an accountability measure rather than a productivity one — the value appears when a published finding is challenged. For your profile, start with the lighter option: simonw/llm's automatic SQLite logging covers prompt-based work with no infrastructure, and MLflow becomes worthwhile when you are training or fine-tuning models, or running classification at a scale where version drift is a real risk.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v3.18.0 (2026-11-04), 28,853 stars, Apache-2.0. Same-day commits and frequent releases under foundation governance with substantial corporate contribution.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. Databricks' managed MLflow is a separate commercial service.

**Licence evidence:** https://github.com/mlflow/mlflow/blob/master/LICENSE.txt

## 10. Costs

No fee. Infrastructure: a tracking server, a database and artefact storage — one VM plus object storage for a newsroom. Managed offerings priced separately (not verified). Estimate.

## 11. Privacy and data flows

Self-hosted keeps experiment data and artefacts internal. Note that logged artefacts may include document content, so the tracking store inherits the sensitivity of what you process.

## 12. Verdict

**Monitor**

## 13. Alternatives

- simonw/llm's SQLite prompt logging for lightweight provenance on prompt-based work — recommended starting point
- DVC for data and pipeline versioning rather than experiment tracking
- A disciplined notebook plus version control, which is cruder but genuinely used

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/mlflow/mlflow
- https://mlflow.org/docs/latest/
- https://github.com/mlflow/mlflow/blob/master/LICENSE.txt

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

← 190. [Inspect AI](JAI-A3-15.md) · 192. [openstates-scrapers](OSINT-C3-13.md) →
