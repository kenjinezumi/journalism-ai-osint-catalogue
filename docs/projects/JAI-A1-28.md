# Alaveteli

`JAI-A1-28` · **63/100** · overall rank 300 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 113) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 28) |
| **Subcategory** | Freedom of information |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | mySociety |
| **Maintenance** | Stable with low activity |
| **Licence** | AGPL-3.0-or-later (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mysociety/alaveteli) · [Documentation](https://alaveteli.org/docs/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 2/5 · usability 3/5 · licence+cost 4/5 → **weighted 63/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0-or-later (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Request and response content published on an instance is public; the underlying disclosed documents remain subject to the releasing body's terms. |
| **Restrictions** | AGPL-3.0-or-later: a modified public instance obliges source publication — which, for a platform whose purpose is public deployment, is a real obligation rather than a theoretical one. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No software fee. Running an instance: a Rails host, a database, reliable mail infrastructure and moderation staff time — the staff cost dominates and is ongoing. Not a small commitment. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/mysociety/alaveteli/blob/develop/LICENSE.txt
- https://github.com/mysociety/alaveteli
- https://alaveteli.org/docs/
- `../sources/recovered/a1disc/notes.md`

---

## 1. Purpose

Platform for running a public freedom-of-information request site: users submit requests to public bodies, correspondence is published automatically, and the resulting archive of requests and responses becomes a public resource.

## Journalism / investigative use case

Two uses: running a national FOI platform (as WhatDoTheyKnow and its many deployments do), and mining an existing deployment's archive — because every request and response is public, an Alaveteli instance is a searchable corpus of what public bodies have disclosed and refused.

## 2. Audience

engineer, newsroom analyst, journalist

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Publishing requests and responses by default creates a public accountability record, which is a genuinely different model from private FOI correspondence and produces a reusable archive
- Deployed nationally in many countries, so the model is proven and the codebase handles real administrative complexity (public-body registers, refusal handling, appeals)
- AGPL-3.0-or-later (licence verified in session 1 by reading the text) with mySociety's long institutional record in civic technology
- The archive of an existing instance is immediately useful to a journalist without running anything: searching prior requests shows what a body has already disclosed

## 5. Cons

- Running an instance is a substantial undertaking: a Rails application plus mail handling, a public-body register to maintain, and moderation of user-submitted content including the legal exposure that brings
- Publishing everything by default is the wrong model for a journalist's own sensitive requests, since it tells the target and competitors what you are asking
- Maintenance is steady rather than brisk, and the deployment documentation assumes operational competence with Rails and mail infrastructure
- Jurisdiction-specific configuration (bodies, laws, timescales) is significant work for a new country deployment

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: session 1's a1disc/notes.md independently recorded 'alaveteli AGPL-3.0-or-later' after reading the licence text, resolving a NOASSERTION. The platform's national deployments are documented by mySociety and constitute strong evidence that the model works at scale.

## 7. Assessment

For your profile the realistic value is as a source rather than software: mine existing Alaveteli instances for what bodies have already disclosed before filing your own requests, which saves time and reveals the body's refusal patterns. Running an instance makes sense only as a civic-infrastructure project, not as newsroom tooling, and the publish-by-default model is actively wrong for a sensitive investigation — file those directly and privately.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived, with mySociety's continued institutional maintenance. Release cadence is modest; the platform is mature and deployments are long-lived. Session 1 verified the licence by reading the text.

## 9. Licensing

**Licence:** AGPL-3.0-or-later (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Request and response content published on an instance is public; the underlying disclosed documents remain subject to the releasing body's terms.

**Restrictions:** AGPL-3.0-or-later: a modified public instance obliges source publication — which, for a platform whose purpose is public deployment, is a real obligation rather than a theoretical one.

**Licence evidence:** https://github.com/mysociety/alaveteli/blob/develop/LICENSE.txt

## 10. Costs

No software fee. Running an instance: a Rails host, a database, reliable mail infrastructure and moderation staff time — the staff cost dominates and is ongoing. Not a small commitment. Estimate.

## 11. Privacy and data flows

Deliberately public: requests and responses are published, and requester names are typically visible. This is the point of the platform and the reason not to use it for a sensitive journalistic request.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Publish-by-default model is unsuitable for sensitive journalistic requests

## 13. Alternatives

- [Froide](JAI-A1-29.md) for the German-lineage equivalent with a similar model
- [MuckRock](OSINT-C3-15.md) for a US FOI platform with both public and private request options
- Filing requests directly and privately for sensitive investigations

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/mysociety/alaveteli
- https://alaveteli.org/docs/
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
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 299. [OpenCellID](SUR-B2-19.md) · 301. [SpiderFoot](OSINT-C3-29.md) →
