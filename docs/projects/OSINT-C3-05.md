# Uwazi

`OSINT-C3-05` · **94/100** · overall rank 17 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 10) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 2) |
| **Subcategory** | Document collection platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | HURIDOCS |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/huridocs/uwazi) · [Documentation](https://uwazi.io/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 94/100**

---

## 1. Purpose

Document and entity management platform built for human-rights documentation, with customisable entity templates, relationships, multilingual interfaces, full-text search and public or private publishing.

## Journalism / investigative use case

Building a structured, publishable collection of documents and entities around a long-running investigation: court filings linked to defendants linked to incidents, with a custom data model, in several languages, publishable as a public resource when the reporting is done.

## 2. Audience

newsroom analyst, specialist investigator, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Customisable entity templates and relationships mean you model your investigation's actual structure rather than fitting it to someone else's schema — a real advantage over fixed-model platforms
- Built by a human-rights documentation organisation, so multilingual support, evidence handling and the private-to-public publishing transition are designed in rather than retrofitted
- MIT licensed with exceptional maintenance: release 1.229.312 on 2026-11-16 and same-day pushes, independently recorded in session 1's ground_truth.tsv
- Serves both the working-collection and the published-resource purposes, so a long investigation's archive becomes its public legacy without a migration

## 5. Cons

- Operational commitment: a Node and MongoDB application with Elasticsearch for search, so it is a platform to run rather than a tool to install
- Flexibility is double-edged — a badly designed entity model is hard to change later, so the modelling decision at the start matters more than with a fixed-schema system
- Oriented to curated collections rather than bulk leak triage: it is for the documents you have decided matter, not for the first pass over 500,000 files
- Smaller community than the big document platforms, though with strong institutional backing

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: release 1.229.312 (2026-11-16) with same-day push, MIT licence — independently recorded in session 1's ground_truth.tsv as MIT, active, with the same release line. HURIDOCS deploys Uwazi with human-rights organisations, which is documented by the organisation.

## 7. Assessment

Adopt it for long-running structured investigations, particularly where the output should become a public resource — that combination is what Uwazi does better than anything else here. For your profile the decisive design step is the entity model: spend real time on it before loading data, because the schema encodes your investigative questions. Keep bulk triage elsewhere (Datashare, OpenAleph) and move the documents that matter into Uwazi.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17 and session 1's independent check: archived=false, pushed_at 2026-11-16, latest release 1.229.312 (2026-11-16), MIT. Same-day release and push with a very high release count indicating continuous delivery, under institutional maintenance by HURIDOCS.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/huridocs/uwazi/blob/production/LICENSE

## 10. Costs

No software fee. Infrastructure estimate: Node application, MongoDB and Elasticsearch — one well-provisioned VM for a moderate collection, more as it grows. HURIDOCS offers hosting and support services (prices not verified). Assumptions: self-hosted, curated collection scale.

## 11. Privacy and data flows

Self-hosted with private collections by default and an explicit publishing step, which is the right model for material that starts sensitive and becomes public. Residual risk is ordinary platform security.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ICIJ Datashare](JAI-A2-23.md) for bulk document triage before curation
- [OpenAleph](JAI-A2-35.md) where cross-dataset entity resolution matters more than custom modelling
- [DocumentCloud](JAI-A2-13.md) for publishing documents without the entity layer

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/huridocs/uwazi
- https://uwazi.io/
- `../sources/recovered/cat/ground_truth.tsv`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 16. [ReplayWeb.page](OSINT-C1-32.md) · 18. [whisper.cpp](JAI-A2-59.md) →
