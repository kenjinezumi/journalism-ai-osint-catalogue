# Quarto

`OSINT-C3-39` · **85/100** · overall rank 97 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 30) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 5) |
| **Subcategory** | Reproducible publishing |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Posit PBC |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/quarto-dev/quarto-cli) · [Documentation](https://quarto.org/docs/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Rendering toolchain is a local install; LaTeX for PDF output is a large dependency. Negligible infrastructure beyond web hosting for published output. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/quarto-dev/quarto-cli/blob/main/COPYING.md
- https://github.com/quarto-dev/quarto-cli
- https://quarto.org/docs/

---

## 1. Purpose

Publishing system that renders documents combining prose with executable Python, R and Julia code into HTML, PDF, Word and websites, with cross-references, citations and parameterised reports.

## Journalism / investigative use case

Publishing a methodology alongside a story: a Quarto document contains the prose explanation, the actual analysis code and the figures it produces, rendered as a web page readers can inspect — which turns 'we analysed the data' into a verifiable account of how.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Executable documents mean the published methodology cannot drift from the analysis that produced the figures, which is the failure mode of hand-written methodology notes
- Multi-language support (Python, R) means a mixed newsroom can use one publishing system, and R matters here because much media-analysis methodology is written in it
- MIT licensed with very active development and strong commercial backing from Posit, plus excellent documentation
- Renders to HTML, PDF and websites from one source, so the same analysis serves a public methodology page and an internal memo

## 5. Cons

- Commercial backing by Posit means direction follows their strategy, though the MIT licence and large community limit lock-in risk
- Rendering toolchain (Pandoc, LaTeX for PDF, language runtimes) is heavy, and reproducible rendering across machines needs containerisation
- Publishing a methodology document exposes your analysis to scrutiny, which is the point and also a discipline — sloppy code published is worse than no code published
- Learning curve for the cross-reference and citation features, though basic use is immediate

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with very active development under Posit's maintenance. Quarto's adoption in data science and academic publishing is well established; its use for journalism methodology notes is a natural extension.

## 7. Assessment

Adopt it for methodology publication — this is the tool that makes 'show your work' practical, and for an outlet whose findings will be attacked, a published reproducible methodology is a strong defensive asset. For your profile I would make it standard practice for any data-driven story: the Quarto document is written as the analysis proceeds, published alongside the piece, and containerised so a reader with the data can reproduce the figures.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived with very active development under Posit PBC's commercial maintenance and a large user community across data science and academia.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/quarto-dev/quarto-cli/blob/main/COPYING.md

## 10. Costs

No fee. Rendering toolchain is a local install; LaTeX for PDF output is a large dependency. Negligible infrastructure beyond web hosting for published output. Estimate.

## 11. Privacy and data flows

Local rendering. The consideration is editorial rather than technical: a published methodology document reveals your data sources and analytical choices, which is usually desirable and occasionally discloses more about a source than intended — review before publishing.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Jupyter notebooks published as HTML, which is simpler and less polished
- Observable or a hand-written methodology page, which drifts from the code
- R Markdown for R-only workflows, which Quarto supersedes

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/quarto-dev/quarto-cli
- https://quarto.org/docs/
- https://github.com/quarto-dev/quarto-cli/blob/main/COPYING.md

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 96. [promptfoo](JAI-A3-14.md) · 98. [RAGFlow](JAI-A3-06.md) →
