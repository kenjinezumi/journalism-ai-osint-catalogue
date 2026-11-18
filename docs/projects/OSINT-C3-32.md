# igraph

`OSINT-C3-32` · **75/100** · overall rank 214 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 70) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 20) |
| **Subcategory** | Link analysis |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | igraph development team |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-2.0 (project licensing — confirm from the repository licence file) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/igraph/igraph) · [Documentation](https://igraph.org/c/doc/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 75/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-2.0 (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-2.0 copyleft: embedding in a distributed product triggers obligations. Internal analysis is unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. CPU and memory proportional to graph size, with much better constants than NetworkX. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/igraph/igraph
- https://igraph.org/c/doc/

---

## 1. Purpose

C library for graph analysis with bindings for Python, R and Mathematica, implementing a wide range of algorithms with performance suitable for large graphs.

## Journalism / investigative use case

The same link analysis as NetworkX at a scale NetworkX cannot reach: community detection and centrality over a co-sharing network of millions of edges, or a corporate graph assembled from a national register, where pure-Python performance would make the analysis impractical.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- C implementation gives order-of-magnitude performance over NetworkX on large graphs, which is what makes million-edge analysis feasible on a workstation
- R bindings matter for this field: much coordinated-behaviour and network research is in R, so igraph lets you use published methods directly (CooRTweet depends on it)
- Comprehensive algorithm coverage comparable to NetworkX, so switching for performance does not mean losing capability
- Long-established with GPL-2.0 licensing and stable maintenance

## 5. Cons

- GPL-2.0 copyleft is a consideration if you embed it in a distributed product, though not for internal analysis
- C library plus bindings means installation is less trivial than a pure-Python package, particularly on Windows
- Same interpretive hazard as NetworkX: performance makes it easier to compute metrics over large graphs and no easier to interpret them responsibly
- API differs from NetworkX, so porting an analysis between them is real work rather than a rename

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with continuing development. igraph's use in network science is well established, and CooRTweet's dependency on the R bindings is verifiable from that project.

## 7. Assessment

Adopt it when graph size defeats NetworkX, and specifically when you want to use R-based published methods for coordinated-behaviour analysis — that is a concrete reason to have it. For your profile the pragmatic approach is NetworkX by default for its API clarity, igraph when a computation does not finish, and the same methodological discipline about edge definition and interpretation in both cases.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived with continuing development across the C core and language bindings. A long-established project with consistent maintenance.

## 9. Licensing

**Licence:** GPL-2.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** GPL-2.0 copyleft: embedding in a distributed product triggers obligations. Internal analysis is unaffected.

**Licence evidence:** https://github.com/igraph/igraph

## 10. Costs

No fee. CPU and memory proportional to graph size, with much better constants than NetworkX. Estimate.

## 11. Privacy and data flows

Entirely local, no network calls.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [NetworkX](OSINT-C3-31.md) for clearer Python API at smaller scale
- graph-tool for another high-performance option with different licensing
- Neo4j or DuckDB where persistence and querying matter more than algorithm breadth

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/igraph/igraph
- https://igraph.org/c/doc/

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

← 213. [eScriptorium](JAI-A2-15.md) · 215. [Open-Meteo](OSINT-C2-41.md) →
