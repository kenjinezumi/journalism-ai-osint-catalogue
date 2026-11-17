# sigma.js

`OSINT-C3-34` · **70/100** · overall rank 270 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 98) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 30) |
| **Subcategory** | Network visualisation (web) |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Alexis Jacomy and the sigma.js community |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/jacomyal/sigma.js) · [Documentation](https://www.sigmajs.org/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 70/100**

---

## 1. Purpose

JavaScript library for rendering interactive network graphs in the browser using WebGL, with layouts, camera controls and event handling, built on the graphology data structure.

## Journalism / investigative use case

Publishing an interactive network with a story: readers explore a corporate-ownership or co-sharing graph themselves, clicking entities to see details — which makes a complex network comprehensible in a way a static figure cannot.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- WebGL rendering handles graphs large enough to be interesting in the browser, where SVG-based libraries stall
- Pairs with graphology for in-browser graph manipulation, so filtering and metric computation can happen client-side as the reader explores
- MIT licensed with active maintenance and a focused scope, maintained by people embedded in the network-analysis community
- Interactive exploration lets a reader verify a claim about the network themselves, which is a genuine transparency gain over a static image

## 5. Cons

- Engineering effort: a published interactive network is a front-end project, not a configuration, and the design work (what is clickable, what is shown, how to avoid misleading layout) is substantial
- Same layout-misinterpretation risk as Gephi, amplified because readers will draw conclusions from positions you did not intend
- Large graphs still need thinning before publication, so the dataset shown is a curated subset and that curation needs explaining
- Bundle weight and GPU requirements affect readers on constrained devices — the same reach consideration as MapLibre versus Leaflet

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with active development. sigma.js is a recognised library in web network visualisation, used alongside graphology in the network-analysis ecosystem.

## 7. Assessment

Integrate it where an interactive network genuinely helps the reader — which is less often than it is used, since many networks are better communicated as a curated figure plus a table. For your profile, if you do publish one, state the edge definition in the interface itself and consider annotating the specific relationships the story relies on, so a reader exploring the graph finds the claims rather than inventing their own from the layout.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived with continuing development alongside the graphology data-structure library. Community-maintained with people active in the network-analysis field.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/jacomyal/sigma.js/blob/main/LICENSE.txt

## 10. Costs

No fee. Front-end development time is the real cost. Negligible hosting.

## 11. Privacy and data flows

Client-side rendering; the graph data is published to readers by definition, so what you include is a disclosure decision.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [Gephi](OSINT-C3-33.md) export to a static figure, which is simpler and often clearer
- Cytoscape.js as an alternative web graph library with different strengths
- A table plus a curated diagram, which for many networks communicates better than an interactive graph

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/jacomyal/sigma.js
- https://www.sigmajs.org/
- https://github.com/jacomyal/sigma.js/blob/main/LICENSE.txt

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

← 269. [RDFLib](JAI-A3-16.md) · 271. [unitedstates/congress](OSINT-C3-42.md) →
