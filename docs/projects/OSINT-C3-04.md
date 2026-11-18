# Overview

`OSINT-C3-04` · **64/100** · overall rank 295 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 112) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 34) |
| **Subcategory** | Document analysis platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Overview Project (Jonathan Stray lineage) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | AGPL-3.0 (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/overview/overview-server) · [Documentation](https://blog.overviewdocs.com/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 4/5 · usability 4/5 · licence+cost 4/5 → **weighted 64/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0: a modified instance offered to users obliges source publication. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No software fee. Self-hosting a Scala multi-service platform is a meaningful operational commitment for the capability delivered. Hosted service terms not verified. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/overview/overview-server/blob/master/LICENSE
- https://github.com/overview/overview-server
- `../sources/recovered/a1disc/notes.md`

---

## 1. Purpose

Document-analysis platform that clusters a document set by topic, provides tagging and full-text search, and presents a tree view so a reporter can explore a large collection by theme rather than one file at a time.

## Journalism / investigative use case

The original answer to 'I have ten thousand documents and three days': Overview clusters them into a navigable topic tree so a reporter can see the shape of the collection and read the interesting branches, which remains the right first move on an unfamiliar dump.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Topic-tree navigation is genuinely reporter-friendly — it answers 'what is in here' without requiring the reporter to know what to search for, which keyword search cannot do
- Built specifically for journalism by people who had watched reporters fail at document review, and the design shows it
- AGPL-3.0 (licence verified in session 1 by reading the text, resolving a NOASSERTION), with a long history and a sizeable repository
- Tagging and search alongside clustering means the exploration leads somewhere actionable

## 5. Cons

- Maintenance has clearly slowed, which is the dominant consideration: this is a mature platform whose active development period has passed, and deploying it means accepting that
- Scala and multi-service architecture make self-hosting a substantial undertaking relative to the capability — BERTopic plus Datasette achieves comparable exploration with components you already run
- Clustering quality is dated relative to current embedding-based topic modelling, so the topic tree is cruder than what BERTopic would produce today
- The hosted Overview service's status and terms were not verified in this survey

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: session 1's a1disc/notes.md independently recorded 'overview-server AGPL-3.0' after reading the licence text, resolving a GitHub NOASSERTION. The project's journalism lineage is well documented; its reduced development pace is evident from the repository.

## 7. Assessment

Reference only for new deployments, but the idea remains correct and worth reproducing: cluster first, then read. For your profile the modern equivalent is BERTopic for clustering plus Datasette or Datashare for search and tagging — components that are actively maintained and that you may already run. Overview's historical importance is that it established document clustering as a newsroom practice, and that practice is what to carry forward.

## 8. Maintenance

**Maintenance appears to be declining** — Verified via the GitHub API 2026-11-17 as live and non-archived, but with substantially reduced development activity and no current release cadence. Session 1 verified the AGPL-3.0 licence by reading the text. Declining rather than dormant; no deprecation notice.

## 9. Licensing

**Licence:** AGPL-3.0 (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified instance offered to users obliges source publication.

**Licence evidence:** https://github.com/overview/overview-server/blob/master/LICENSE

## 10. Costs

No software fee. Self-hosting a Scala multi-service platform is a meaningful operational commitment for the capability delivered. Hosted service terms not verified. Estimate.

## 11. Privacy and data flows

Self-hosted keeps documents internal. The hosted service would place them with the operator — terms unverified.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Development pace has declined; the architecture is heavy relative to modern alternatives

## 13. Alternatives

- [BERTopic](JAI-A2-04.md) plus Datasette for the same clustering-then-reading workflow with maintained components
- [ICIJ Datashare](JAI-A2-23.md) for search, tagging and entity extraction in a maintained platform
- [txtai](JAI-A2-55.md) for semantic exploration of a document set

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/overview/overview-server
- `../sources/recovered/a1disc/notes.md`

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

← 294. [Katna](OSINT-C2-11.md) · 296. [Photon](OSINT-C1-20.md) →
