# NetworkX

`OSINT-C3-31` · **88/100** · overall rank 57 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 19) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 4) |
| **Subcategory** | Link analysis |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | NetworkX developers (NumFOCUS) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/networkx/networkx) · [Documentation](https://networkx.org/documentation/stable/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 88/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-3-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU and memory proportional to graph size; pure-Python performance is the limiting factor rather than cost. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/networkx/networkx/blob/main/LICENSE.txt
- https://github.com/networkx/networkx
- https://networkx.org/documentation/stable/

---

## 1. Purpose

Python library for creating, manipulating and analysing graphs and networks, with a comprehensive collection of algorithms for centrality, community detection, paths, flows and structural analysis.

## Journalism / investigative use case

The analytical layer for any relationship question: compute who sits at the centre of a corporate network, find the shortest ownership path between two entities, detect communities in a co-sharing network, or identify the broker whose removal disconnects a cluster — the findings that turn a graph picture into a reportable claim.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Algorithm breadth is the point: centrality, community detection and path analysis are what produce findings, and NetworkX implements essentially all of them with documented definitions you can cite
- Pure Python with a clear API, so a data journalist can compute a betweenness centrality without learning a graph database
- BSD-3-Clause under NumFOCUS governance with exceptional maintenance (release 3.6.1 2026-02-13 era line, pushed 2026-11-17) — stable, long-lived and institutionally supported
- Integrates with the whole Python data stack and exports to Gephi for visualisation, so analysis and presentation connect cleanly

## 5. Cons

- Pure Python means performance limits: graphs beyond a few hundred thousand edges become slow, where igraph or a graph database is appropriate
- Centrality metrics are easy to compute and easy to over-interpret — 'most central' is a mathematical property of your graph construction, not a finding about real-world importance, and that distinction is routinely lost in published network journalism
- Graph construction decisions (what counts as an edge, which entities are included) determine the results entirely, and the library cannot help you make them defensibly
- No visualisation worth publishing; Gephi or a web library is needed for the graphic

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under NumFOCUS-affiliated governance with same-day commits. NetworkX is the standard Python graph library, well established across scientific computing and data journalism.

## 7. Assessment

Adopt it as the standard link-analysis tool — the algorithms are what produce findings and the documentation lets you cite definitions precisely. For your profile the methodological discipline matters more than the code: state how edges were defined, publish the construction rules, and never present a centrality score as a claim about real-world power without corroboration. Move to igraph when performance binds.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived with same-day commits, under NumFOCUS-affiliated community governance and a long, consistent release history. Among the most dependable maintenance profiles in this catalogue.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/networkx/networkx/blob/main/LICENSE.txt

## 10. Costs

No fee. CPU and memory proportional to graph size; pure-Python performance is the limiting factor rather than cost. Estimate.

## 11. Privacy and data flows

Entirely local, no network calls.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [igraph](OSINT-C3-32.md) for substantially better performance on large graphs
- [Gephi](OSINT-C3-33.md) for interactive visualisation and layout
- Neo4j where the graph is persistent and queried by several people

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/networkx/networkx
- https://networkx.org/documentation/stable/
- https://github.com/networkx/networkx/blob/main/LICENSE.txt

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 56. [MediaInfo](OSINT-C2-04.md) · 58. [libpff](JAI-A1-12.md) →
