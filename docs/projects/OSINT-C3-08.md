# ICIJ Prophecies

`OSINT-C3-08` · **74/100** · overall rank 224 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 76) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 22) |
| **Subcategory** | Collaborative data verification |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | International Consortium of Investigative Journalists |
| **Maintenance** | Stable with low activity |
| **Licence** | AGPL-3.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ICIJ/prophecies) · [Documentation](https://github.com/ICIJ/prophecies#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 74/100**

---

## 1. Purpose

Collaborative data-checking application where a team is served records to verify or correct, with task assignment, progress tracking, inter-annotator comparison and a record of who checked what.

## Journalism / investigative use case

The step nobody builds and everybody needs: when an extracted dataset of 50,000 records must be human-verified before publication, Prophecies turns that into assigned tasks with progress tracking and an audit trail — rather than a shared spreadsheet where nobody knows what has been checked.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Addresses the real bottleneck in data-driven investigation — human verification at scale — which no other tool in this catalogue tackles directly
- Inter-annotator comparison surfaces disagreement between checkers, which is how you find systematically ambiguous records rather than discovering them after publication
- Built by ICIJ for its own cross-border projects, so the collaboration model assumes distributed teams in different time zones and organisations
- Produces an audit trail of who verified which record, which is exactly what you want when a published figure is challenged

## 5. Cons

- Small project with limited external community, so deployment support is thin and you will read source
- Requires a defined verification task: it is for checking records against a rule, not for open-ended analysis, so framing the task well is the prerequisite and takes thought
- Yet another platform to deploy alongside your document and search systems, and the value only appears when there is a large verification job to do
- Development cadence follows ICIJ's project needs rather than a public roadmap

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under ICIJ maintenance. ICIJ builds it for its own cross-border investigations, which is the most relevant provenance available for a collaborative-verification tool.

## 7. Assessment

Worth piloting when you have a verification job large enough to need coordination — which arrives sooner than teams expect, typically the first time an extraction produces thousands of records that must be checked before publication. For your profile the alternative is a disciplined spreadsheet with an assignment column, which works up to a point and then silently fails; Prophecies is what you deploy when it has failed once. The audit trail is the durable benefit.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived under ICIJ's maintenance, with activity following the organisation's project cycles rather than a public release cadence. Classified stable-low: institutionally maintained for internal use, published openly.

## 9. Licensing

**Licence:** AGPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Copyleft would apply to a modified hosted instance; immaterial for internal deployment.

**Licence evidence:** https://github.com/ICIJ/prophecies

## 10. Costs

No fee. A Django-class deployment plus a database — modest. The dominant cost is the human verification labour it organises, which it makes visible rather than reduces. Estimate.

## 11. Privacy and data flows

Self-hosted; records under verification stay internal. The assignment data reveals who in your team is working on what, which is minor but worth knowing in a multi-organisation collaboration.

## 12. Verdict

**Pilot**

## 13. Alternatives

- A structured spreadsheet with assignment and status columns, which works for smaller jobs
- [Datasette](JAI-A2-09.md) with a custom form plugin for a lighter bespoke verification interface
- Label Studio for annotation-oriented verification tasks

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/ICIJ/prophecies

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

← 223. [Perma](OSINT-C1-37.md) · 225. [Internet Health Report (IHR)](SUR-B1-13.md) →
