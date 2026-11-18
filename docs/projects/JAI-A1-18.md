# csvkit

`JAI-A1-18` · **84/100** · overall rank 102 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 43) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 11) |
| **Subcategory** | Data journalism tooling |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Christopher Groskopf and wireservice contributors |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/wireservice/csvkit) · [Documentation](https://csvkit.readthedocs.io/) |

**Scores** — relevance 5/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Negligible resources for files it handles comfortably.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/wireservice/csvkit/blob/master/COPYING
- https://github.com/wireservice/csvkit
- https://csvkit.readthedocs.io/

---

## 1. Purpose

Suite of command-line tools for converting to and working with CSV: format conversion, SQL querying, joining, statistics, searching and cleaning, designed to compose in a shell pipeline.

## Journalism / investigative use case

The data journalist's shell toolkit: convert a government Excel release to CSV, inspect its columns and types, query it with SQL, join it to another release and produce summary statistics — all without opening a spreadsheet or writing a script, which is how most newsroom data work actually starts.

## 2. Audience

newsroom analyst, journalist, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Composable command-line design means a data-cleaning recipe is a shell pipeline you can save, share and rerun — reproducibility for people who would never write Python
- csvstat and csvlook give immediate, honest visibility into a dataset's shape and problems, which is the step reporters most often skip
- Written by and for data journalists (the wireservice lineage), so the tools match newsroom problems rather than general data engineering
- MIT licensed with a long track record and wide packaging

## 5. Cons

- Performance on very large files is poor: csvkit loads and processes in ways that become impractical above a few hundred megabytes, where you want DuckDB or VisiData instead
- Maintenance cadence has slowed considerably over the years, with development now largely corrective rather than feature-adding
- Type inference can surprise: it will guess a column is numeric or a date and silently change your data's meaning, which matters when a leading-zero identifier becomes an integer
- Shell-only, so it suits terminal-comfortable users and excludes others

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with a long release history and slowed recent development. csvkit's standing in data journalism is well established through the wireservice ecosystem and its presence in the field's teaching materials.

## 7. Assessment

Adopt it for the quick inspect-convert-join work that constitutes most newsroom data handling, and switch to DuckDB or VisiData above a few hundred megabytes. For your profile the specific hazard to teach is type inference: run csvstat first, and when a column holds identifiers with leading zeros or long numbers, force it to text, because a silently mangled identifier column has produced published errors before.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with a long release history and reduced recent activity. A mature, feature-complete toolkit where low velocity reflects completion rather than neglect, though it means performance limitations will not be addressed.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/wireservice/csvkit/blob/master/COPYING

## 10. Costs

No fee. Negligible resources for files it handles comfortably.

## 11. Privacy and data flows

Entirely local, no network calls.

## 12. Verdict

**Adopt**

## 13. Alternatives

- DuckDB for the same SQL-over-CSV capability at much larger scale
- [VisiData](JAI-A2-57.md) for interactive terminal exploration
- xsv or qsv for high-performance CSV processing

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/wireservice/csvkit
- https://csvkit.readthedocs.io/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 101. [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) · 103. [Hush Line](SUR-B3-06.md) →
