# Gephi

`OSINT-C3-33` · **80/100** · overall rank 149 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 49) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 12) |
| **Subcategory** | Network visualisation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Gephi Consortium |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 and CDDL dual licensing (project licensing — confirm from the repository licence files) |
| **Licence type** | Dual-licensed |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/gephi/gephi) · [Documentation](https://gephi.org/users/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 80/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Dual-licensed |
| **Exact licence (as recorded)** | GPL-3.0 and CDDL dual licensing (project licensing — confirm from the repository licence files) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | Copyleft on the application; immaterial for desktop analytical use. The dual-licence structure is worth reading if you distribute plugins. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. An analyst workstation with adequate RAM; large graphs need more. Java runtime. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/gephi/gephi
- https://gephi.org/users/

---

## 1. Purpose

Desktop application for interactive network visualisation and exploration, with force-directed layouts, filtering, community detection, statistics and publication-quality export.

## Journalism / investigative use case

Exploring and presenting a network: load a co-sharing graph or a corporate-ownership network, apply a layout, colour by community, filter to the dense core, and export a figure for publication — the step that turns an edge list into something a reader can understand.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Interactive layout and filtering is how you actually understand a network — static analysis tells you metrics, but seeing the structure is what generates the reporting questions
- No-code operation makes it usable by an analyst without Python, which widens who can do network work in a newsroom
- Publication-quality export means the figure in the story comes from the same tool as the analysis, reducing the chance of a mismatch
- Long-established standard in network visualisation with a consortium behind it, widely taught

## 5. Cons

- Force-directed layouts are seductive and misleading: visual proximity is an artefact of the layout algorithm and its random seed, not a measure of relationship strength, and readers (and journalists) consistently over-read it
- Java desktop application with a history of version and platform friction, and performance degrades on large graphs — tens of thousands of nodes is comfortable, hundreds of thousands is not
- Development pace is modest, with long gaps between releases historically
- Easy to produce a beautiful graphic that supports a claim the data does not, which is the central risk in network journalism

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under consortium governance with modest release cadence. Gephi's standing as the standard network-visualisation tool is well established in both research and journalism.

## 7. Assessment

Adopt it for exploration and figure production, with an explicit rule about what the figure claims. For your profile the discipline that matters: a published network graphic must state how edges were defined, and the caption should not imply that visual clustering means organisational relationship unless you have evidence beyond the layout. Compute the metrics in NetworkX or igraph and use Gephi to see and show the structure — not to discover claims.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived under Gephi Consortium governance, with a modest release cadence consistent with the project's long history. Classified stable-low: a mature application maintained rather than actively expanded.

## 9. Licensing

**Licence:** GPL-3.0 and CDDL dual licensing (project licensing — confirm from the repository licence files) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Copyleft on the application; immaterial for desktop analytical use. The dual-licence structure is worth reading if you distribute plugins.

**Licence evidence:** https://github.com/gephi/gephi

## 10. Costs

No fee. An analyst workstation with adequate RAM; large graphs need more. Java runtime. Estimate.

## 11. Privacy and data flows

Entirely local; graph data stays on the machine. Some plugins fetch external data — check before use on a sensitive graph.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [sigma.js](OSINT-C3-34.md) or Cytoscape.js for web-published interactive networks
- Cytoscape for biological-network-oriented analysis with different algorithm emphasis
- [NetworkX](OSINT-C3-31.md) plus matplotlib for scripted, reproducible figures

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/gephi/gephi
- https://gephi.org/users/

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

← 148. [streetlevel](OSINT-C2-32.md) · 150. [Meedan Check](JAI-A4-01.md) →
