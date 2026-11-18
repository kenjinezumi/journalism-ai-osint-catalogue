# Atlos

`OSINT-C2-36` · **78/100** · overall rank 171 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 56) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 26) |
| **Subcategory** | Collaborative visual verification |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Atlos |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/atlosdotorg/atlos) · [Documentation](https://docs.atlos.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 2/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Media and incident records you store are third-party content with their own rights and, often, serious privacy implications. |
| **Restrictions** | GPL-3.0: a modified self-hosted instance offered to users obliges source publication. Internal use unaffected. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No software fee. Self-hosting estimate: an Elixir/Phoenix application plus PostgreSQL and media storage — one moderate VM plus storage growing with media volume, and the dominant cost is the unfamiliar stack's operational learning. Hosted pricing was not verified in this survey. Assumptions: self-hosted, moderate incident volume.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/atlosdotorg/atlos/blob/main/LICENSE
- https://github.com/atlosdotorg/atlos
- https://docs.atlos.org/

---

## 1. Purpose

Collaborative workspace for visual investigations: ingests media, tracks per-incident verification status, assigns work, records geolocation and metadata findings, and maintains an auditable history of who concluded what.

## Journalism / investigative use case

The missing workflow layer for large-scale visual verification: a team documenting hundreds of incidents in a conflict can track which videos have been geolocated, by whom, with what confidence and what evidence — replacing the spreadsheet that every such project otherwise collapses into.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Solves the organisational problem that defeats large verification projects — tracking status, attribution and evidence across hundreds of incidents — which no other tool in this catalogue addresses
- Auditable per-incident history means a published dataset of verified incidents can withstand scrutiny about how each conclusion was reached, which matters enormously for accountability work
- GPL-3.0 and self-hostable, so sensitive incident data and contributor identities stay under your control
- Purpose-built for human-rights and conflict documentation rather than adapted from generic case management

## 5. Cons

- Small project: 97 stars with 92 open issues and the last release v1.2.17 (2025-09-29) against a 2026-10-23 push — a high backlog ratio and slowing release cadence for infrastructure holding an investigation's core records
- Elixir/Phoenix stack is unusual in most newsrooms, so self-hosting requires someone willing to learn it — a real adoption barrier
- Hosted option means incident data and contributor activity sit with a third party, which for conflict documentation involving witness-supplied media is a significant decision
- Workflow-focused: it organises verification but performs none of it, so it sits on top of the rest of this segment's tooling

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 97 stars with 92 open issues, release v1.2.17 (2025-09-29), last push 2026-10-23, GPL-3.0. Atlos positions itself for conflict and human-rights documentation; I verified no specific deployment, so adoption claims are unestablished here.

## 7. Assessment

The right answer if you run a project documenting many incidents, and the only serious open option for that workflow — but adopt it with eyes open about project scale. For your profile: pilot it self-hosted if someone can own an Elixir deployment, keep a documented export path so the records are not trapped if the project slows further, and prefer self-hosting over the hosted service wherever witness-supplied media is involved. The alternative is a well-disciplined Datasette-over-SQLite workflow, which is less capable but fully under your control.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-23, latest release v1.2.17 (2025-09-29), 97 stars, 92 open issues. Commits continue but no release in fourteen months and an open-issue count approaching the star count — a small team under strain. Declining rather than dormant, and worth monitoring because the data it would hold is critical.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Media and incident records you store are third-party content with their own rights and, often, serious privacy implications.

**Restrictions:** GPL-3.0: a modified self-hosted instance offered to users obliges source publication. Internal use unaffected.

**Licence evidence:** https://github.com/atlosdotorg/atlos/blob/main/LICENSE

## 10. Costs

No software fee. Self-hosting estimate: an Elixir/Phoenix application plus PostgreSQL and media storage — one moderate VM plus storage growing with media volume, and the dominant cost is the unfamiliar stack's operational learning. Hosted pricing was not verified in this survey. Assumptions: self-hosted, moderate incident volume.

## 11. Privacy and data flows

Self-hosting keeps incident records, media and contributor activity under your control — important because this data can identify witnesses and victims. The hosted option places all of that with a third party, which for conflict documentation is a decision requiring explicit justification.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [Datasette](JAI-A2-09.md) over a disciplined SQLite schema for a lower-tech but fully controlled equivalent
- [Uwazi](OSINT-C3-05.md) for human-rights documentation with a document rather than incident focus
- A shared spreadsheet with strict conventions — what Atlos exists to replace, and what most projects actually use

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/atlosdotorg/atlos
- https://docs.atlos.org/
- https://github.com/atlosdotorg/atlos/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |

---

← 170. [RapidFuzz](JAI-A2-43.md) · 172. [Surya](JAI-A2-52.md) →
