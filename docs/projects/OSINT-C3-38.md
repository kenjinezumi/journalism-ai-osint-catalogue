# DVC (Data Version Control)

`OSINT-C3-38` · **74/100** · overall rank 229 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 78) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 24) |
| **Subcategory** | Data versioning and provenance |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Treeverse (transferred from Iterative) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/treeverse/dvc) · [Documentation](https://dvc.org/doc) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 74/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Remote storage costs depend on the backend — object storage you control, or a commercial provider at their rates (not priced here). Compute is negligible. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/treeverse/dvc/blob/main/LICENSE
- https://github.com/treeverse/dvc
- https://dvc.org/doc
- `../sources/evidence/leads.md`

---

## 1. Purpose

Version-control system for data and machine-learning pipelines that tracks large files and datasets alongside git, with reproducible pipeline definitions, remote storage backends and experiment tracking.

## Journalism / investigative use case

Provenance for investigative datasets: a leak extraction, a cleaned registry and a derived analysis each versioned and reproducible, so six months later you can show exactly which version of which dataset produced a published figure — and re-run the pipeline to confirm it.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Solves the reproducibility problem that quietly undermines data journalism: datasets change, cleaning scripts evolve, and without versioning a published figure cannot be reproduced even by its author
- Pipeline definitions make the transformation chain from raw to published explicit, which doubles as a methodology description you can share with an editor or a reader
- Works alongside git rather than replacing it, so the workflow is familiar and the data stays out of the repository
- Apache-2.0 with remote-storage support including S3-compatible and local backends, so sensitive data need not touch a commercial cloud

## 5. Cons

- Repository transferred from Iterative to Treeverse (verified by redirect 2026-11-17), following corporate change — governance continuity is a monitoring item for infrastructure you would depend on for years, and pinned URLs should be updated
- Conceptual overhead: DVC's pipeline and cache model takes real learning, and for a single analysis a documented script plus a dated data copy achieves much of the benefit
- Designed for machine-learning workflows, so some concepts (experiments, metrics) map awkwardly onto investigative data work
- Remote storage configuration is where sensitive data could leak to a commercial backend by default — the configuration needs deliberate attention

## 6. Feedback (documented)

No individual user reports verified in this survey. The documented finding from this session: iterative/dvc redirects to treeverse/dvc (verified 2026-11-17, recorded in leads.md L4), following Iterative's acquisition — a governance change rather than a licence change, with the project remaining Apache-2.0 per the API.

## 7. Assessment

Worth adopting if you run recurring data pipelines and want published figures to be reproducible — which is a standard you should want. For your profile the lighter alternative deserves consideration first: a dated immutable copy of each input dataset plus a scripted, version-controlled transformation achieves most of the provenance benefit with no new tooling. Adopt DVC when pipelines become complex enough that the manual discipline fails. Point storage at infrastructure you control and update references to the treeverse path.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: live and non-archived at treeverse/dvc with the iterative/dvc path redirecting, Apache-2.0 per the API. Active development continues under the new organisation; the governance transfer is the item to monitor rather than a maintenance concern today.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/treeverse/dvc/blob/main/LICENSE

## 10. Costs

No fee. Remote storage costs depend on the backend — object storage you control, or a commercial provider at their rates (not priced here). Compute is negligible. Estimate.

## 11. Privacy and data flows

Data stays wherever you point the remote. The risk is a default or convenient configuration sending sensitive datasets to a commercial cloud backend — configure local or self-hosted S3-compatible storage deliberately.

## 12. Verdict

**Monitor**

## 13. Alternatives

- Dated immutable data copies plus version-controlled transformation scripts — the low-tech approach that often suffices
- git-annex or git-lfs for large-file versioning without the pipeline model
- Snakemake or a Makefile for reproducible pipelines without data versioning

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/treeverse/dvc
- https://dvc.org/doc
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 228. [Tabula](JAI-A2-53.md) · 230. [LangChain](JAI-A3-09.md) →
