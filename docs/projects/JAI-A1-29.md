# Froide

`JAI-A1-29` · **59/100** · overall rank 326 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 122) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 31) |
| **Subcategory** | Freedom of information |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Knowledge Foundation Deutschland (okfde) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/okfde/froide) · [Documentation](https://froide.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 2/5 · usability 3/5 · licence+cost 4/5 → **weighted 59/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Django-based freedom-of-information platform managing requests to public bodies, correspondence tracking, deadlines, publication of responses and a public-body database, powering FragDenStaat and similar sites.

## Journalism / investigative use case

The German-lineage FOI platform, and like Alaveteli valuable to a journalist primarily as an archive: FragDenStaat's public corpus of requests and responses is a searchable record of German administrative disclosure, which is a research resource before it is a tool.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Deadline and correspondence tracking is more developed than in some alternatives, reflecting the procedural detail of German FOI law — useful if you file many requests
- Django-based, which fits a Python newsroom stack better than a Rails deployment
- Powers a substantial national platform (FragDenStaat), so it is proven in production with real administrative complexity
- Open-source with an active civic-tech maintainer in OKF Deutschland

## 5. Cons

- Strongly oriented to German law and administrative practice, so deploying it elsewhere means substantial adaptation of bodies, deadlines and legal references
- Like Alaveteli, publication-oriented by default, which is the wrong posture for a sensitive journalistic request
- Self-hosting is a real Django deployment with mail handling and moderation obligations — a civic-infrastructure project rather than newsroom tooling
- Documentation and community are substantially German-language, which is a friction for a non-German-speaking team

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under OKF Deutschland's maintenance. FragDenStaat's operation is the production evidence; I verified no non-German deployment.

## 7. Assessment

Relevant chiefly if you work on Germany, where FragDenStaat's archive is a genuine research asset and worth searching before filing. As software, the same conclusion as Alaveteli applies: running an FOI platform is civic infrastructure, not newsroom tooling, and the publish-by-default model conflicts with investigative practice. For your profile, use the archives and file sensitive requests yourself.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived under institutional maintenance by OKF Deutschland, with steady rather than frequent development. Classified stable-low: a mature platform supporting an operating national service.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Published request and response content is public; disclosed documents remain subject to the releasing body's terms.

**Restrictions:** Permissive as published; confirm the licence file before redistribution.

**Licence evidence:** https://github.com/okfde/froide

## 10. Costs

No software fee. Running an instance: Django host, database, mail infrastructure and moderation staff — the staff cost dominates. Estimate.

## 11. Privacy and data flows

Publication-oriented by default, like Alaveteli; requests and responses are public.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- German-law orientation; publish-by-default unsuitable for sensitive requests

## 13. Alternatives

- [Alaveteli](JAI-A1-28.md) for the more widely deployed platform
- FragDenStaat's public archive as a research source without running anything
- Direct private requests for sensitive investigations

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/okfde/froide
- https://froide.readthedocs.io/

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

← 325. [Maltego](OSINT-C3-36.md) · 327. [PhotoHolmes](JAI-A4-17.md) →
