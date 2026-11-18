# GraphSense

`OSINT-C3-21` · **64/100** · overall rank 292 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 109) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 33) |
| **Subcategory** | Blockchain analysis |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Iknaio / GraphSense community (AIT origin) |
| **Maintenance** | Uncertain |
| **Licence** | MIT (project licensing — confirm from the repository licence file; open-core model with commercial involvement) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/graphsense/graphsense-lib) · [Documentation](https://graphsense.github.io/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 2/5 · privacy 4/5 · usability 2/5 · licence+cost 4/5 → **weighted 64/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file; open-core model with commercial involvement) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Tag datasets have their own provenance and terms, which matter because tags drive attribution. |
| **Restrictions** | Permissive as published; verify which components are open and which are commercial before designing around it. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** No software fee. Infrastructure is substantial: blockchain ingestion and clustering at scale needs a cluster with large storage — the dominant cost and the practical barrier for a newsroom. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/graphsense/graphsense-lib
- https://graphsense.github.io/

---

## 1. Purpose

Open-source cryptocurrency analytics platform providing address clustering, entity tagging, transaction-flow analysis and an API across several blockchains.

## Journalism / investigative use case

The open alternative to commercial blockchain analytics: cluster addresses into entities, apply tags, and trace flows between them — giving you the entity-level view that raw transaction data lacks, with clustering heuristics you can inspect rather than trust.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Address clustering is the capability that makes blockchain analysis useful, and having it open means the heuristics are inspectable — which is the difference between a defensible published claim and citing a black box
- Multi-blockchain coverage with an API, so it is a platform rather than a single-chain script
- Academic origin (AIT) with published methodology, so the clustering approach can be cited and critiqued
- Open source, so a newsroom is not dependent on a commercial analytics subscription whose methods it cannot examine

## 5. Cons

- Heavy infrastructure: ingesting and clustering blockchain data requires substantial compute and storage, realistically a cluster rather than a VM — this is the main barrier and it is high
- Clustering heuristics are probabilistic: co-spending and other patterns suggest common control without proving it, and publishing a cluster as 'this entity' overstates the evidence
- Entity tagging depends on tag data whose sources and quality vary, and a wrong tag propagates into a wrong attribution
- Commercial entity (Iknaio) involvement, so the open-core boundary and direction warrant checking before you build on it

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. GraphSense's academic lineage and published methodology are documented by the project; I verified no newsroom deployment.

## 7. Assessment

Worth knowing about rather than deploying, unless cryptocurrency is a sustained beat and you have real infrastructure — the ingestion cost is the obstacle. For your profile the realistic path on a crypto story is ethereum-etl for targeted flow analysis plus conventional reporting for attribution, with GraphSense considered only if clustering at scale becomes central. If you do publish cluster-based claims, state the heuristic and its limits explicitly, because the clustering is the contestable step.

## 8. Maintenance

**Uncertain** — Verified via the GitHub API 2026-11-17 as live and non-archived, but the project spans several repositories with a commercial entity involved and no clear single release cadence. Open-core boundary and continuity could not be assessed from metadata — classified Uncertain rather than inferred.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file; open-core model with commercial involvement) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Tag datasets have their own provenance and terms, which matter because tags drive attribution.

**Restrictions:** Permissive as published; verify which components are open and which are commercial before designing around it.

**Licence evidence:** https://github.com/graphsense/graphsense-lib

## 10. Costs

No software fee. Infrastructure is substantial: blockchain ingestion and clustering at scale needs a cluster with large storage — the dominant cost and the practical barrier for a newsroom. Estimate.

## 11. Privacy and data flows

Self-hosted analysis keeps your investigation private, which is the main advantage over commercial platforms that see every address you query.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Substantial ingestion infrastructure required; clustering heuristics are probabilistic and must be stated as such

## 13. Alternatives

- [ethereum-etl](OSINT-C3-20.md) plus your own analysis for targeted flow work at far lower cost
- Commercial analytics for attribution, accepting proprietary methods, cost and query disclosure
- Collaboration with an academic group that already operates a GraphSense instance

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/graphsense/graphsense-lib
- https://graphsense.github.io/

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

← 291. [Community Forensics](JAI-A4-21.md) · 293. [warcprox](OSINT-C1-42.md) →
