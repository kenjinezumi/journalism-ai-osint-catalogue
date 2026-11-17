# n8n

`JAI-A1-17` · **85/100** · overall rank 87 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 32) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 7) |
| **Subcategory** | Workflow automation |
| **Type** | platform |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | n8n GmbH |
| **Maintenance** | Actively maintained |
| **Licence** | Sustainable Use Licence (fair-code) — NOT an OSI open-source licence; GitHub reports NOASSERTION |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/n8n-io/n8n) · [Documentation](https://docs.n8n.io/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 5/5 · licence+cost 2/5 → **weighted 85/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Visual workflow-automation platform with hundreds of integrations, code nodes, scheduling and native AI/agent capabilities, self-hostable or used as a hosted service.

## Journalism / investigative use case

Building newsroom automation that non-engineers can read and modify: a visual workflow that watches a source, extracts data, calls a language model for classification and posts to a channel — with the logic visible to an editor rather than hidden in a script.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `source-available-restricted`

## 4. Pros

- Integration breadth and a genuinely usable visual editor mean workflows are accessible to colleagues who would never read a script, which affects whether automation survives staff changes
- Native AI and agent nodes make language-model steps a first-class part of a workflow, which is where newsroom automation is heading
- Enormous community (210,772 stars) and very active development (n8n@2.48.4, 2026-11-13; pushed 2026-11-17)
- Self-hostable, so data and credentials can stay on your infrastructure

## 5. Cons

- LICENCE BLOCKER for some uses: n8n is under the Sustainable Use Licence (fair-code), NOT an OSI open-source licence — session 1 recorded this independently and GitHub reports NOASSERTION. It restricts commercial redistribution and offering n8n as a service, which matters if you want to provide workflows to partner organisations
- 1,267 open issues and very rapid development, so pinning and upgrade testing are necessary
- Visual workflows at scale become hard to review and diff, and credentials embedded in workflows need careful handling
- Commercial-product gravity: the hosted service and enterprise features are the vendor's business, and feature availability can shift between tiers

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 210,772 stars with 1,267 open issues, release n8n@2.48.4 (2026-11-13), pushed 2026-11-17, SPDX NOASSERTION. Session 1's a1disc/notes.md independently recorded 'n8n Sustainable Use License (fair-code)' after reading the licence — a finding carried forward here, and the decisive consideration for anyone assuming it is open source.

## 7. Assessment

Capable and widely adopted, and not open source — which is the fact to be clear about. For internal newsroom automation the Sustainable Use Licence is unlikely to bite, so it is usable; if you intend to host workflows for partner organisations or build a product, read the licence properly first or choose Huginn, which is MIT. For your profile I would default to Huginn on licence grounds unless n8n's AI nodes and visual editor are decisive for your team's ability to maintain the automation.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release n8n@2.48.4 (2026-11-13), 210,772 stars, 1,267 open issues, SPDX NOASSERTION. Same-day commits and frequent releases under well-funded commercial maintenance.

## 9. Licensing

**Licence:** Sustainable Use Licence (fair-code) — NOT an OSI open-source licence; GitHub reports NOASSERTION _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a for the platform; AI nodes use whichever model provider you configure, under that provider's terms.

**Restrictions:** Material: the Sustainable Use Licence permits internal business use but restricts commercial redistribution and hosting n8n as a service for third parties. A newsroom running it internally is fine; a newsroom offering workflow hosting to partners should read the licence and probably choose differently.

**Licence evidence:** https://github.com/n8n-io/n8n/blob/master/LICENSE.md

## 10. Costs

Self-hosting the community edition has no licence fee under the Sustainable Use Licence. Hosted n8n Cloud and enterprise editions are priced per workflow-execution or per seat (not verified in this survey). If AI nodes call hosted models, those token costs apply. Estimate.

## 11. Privacy and data flows

Self-hosting keeps workflow data and credentials internal. Two exposure points to manage: AI nodes pointed at hosted model providers send content to them, and integration credentials stored in n8n make the instance a high-value target.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Sustainable Use Licence (fair-code) is not open source and restricts offering n8n as a service to third parties

## 13. Alternatives

- [Huginn](JAI-A1-16.md) for an MIT-licensed self-hosted equivalent — recommended on licence grounds
- Scripted pipelines in version control for engineer-maintained automation
- Apache Airflow or Dagster where the workload is data-pipeline rather than event automation

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/n8n-io/n8n/blob/master/LICENSE.md
- `../sources/recovered/a1disc/notes.md`

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
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |
| 9 | [MapLibre GL JS](JAI-A1-22.md) | 85 | Adopt |

---

← 86. [Heritrix 3](OSINT-C1-22.md) · 88. [Camelot](JAI-A2-06.md) →
