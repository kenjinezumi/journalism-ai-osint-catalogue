# warn-scraper

`JAI-A1-30` · **75/100** · overall rank 220 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 89) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 24) |
| **Subcategory** | Public records scraping |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Big Local News (Stanford) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (licence blob read 2026-11-17, Copyright 2025 Big Local News; GitHub reports NOASSERTION — also independently recorded in session 1's a1disc/notes.md) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/biglocalnews/warn-scraper) · [Documentation](https://warn-scraper.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 75/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 (licence blob read 2026-11-17, Copyright 2025 Big Local News; GitHub reports NOASSERTION — also independently recorded in session 1's a1disc/notes.md) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Collected notices are US state government records, generally freely usable. |
| **Restrictions** | Code permissive. Collected public records carry no material restriction in this case. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Negligible compute. The real cost is maintenance of per-state scrapers if you fork or extend it. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/biglocalnews/warn-scraper/blob/main/LICENSE
- https://github.com/biglocalnews/warn-scraper
- https://warn-scraper.readthedocs.io/
- `../sources/recovered/a1disc/notes.md`

---

## 1. Purpose

Command-line scraper that collects WARN Act notices — statutory advance notifications of US plant closings and mass layoffs — from every state agency that publishes them, normalising them into a single dataset.

## Journalism / investigative use case

A working model of sustained public-records collection: layoff notices are published by fifty separate state agencies in fifty formats, and this consolidates them into one dataset that supports both local stories ('which employers in this county are cutting jobs') and national analysis.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Solves a real and recurring local-news need across every US state, and the consolidated dataset is directly usable for both local and national reporting
- Demonstrates the pattern worth copying: one scraper per jurisdiction, normalised into a shared schema, released as a package — the right architecture for any multi-jurisdiction records problem
- Licence resolved: Apache-2.0 (read from the licence blob; GitHub reports NOASSERTION, and session 1 independently recorded Apache-2.0)
- Actively maintained with a frequent release cadence (1.2.178, 2026-10-26; pushed 2026-11-13) by an academic data-journalism programme

## 5. Cons

- State agency sites change constantly, so 73 open issues against 45 stars mostly reflects per-state breakage — the maintenance burden of multi-jurisdiction scraping is the honest lesson here
- US only, so it is a template rather than a resource for other countries
- Small community, and the long-term dependency is on one academic programme's funding
- Normalisation across fifty formats necessarily loses state-specific detail, so for a single-state story the original source may be better

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 45 stars with 73 open issues, release 1.2.178 (2026-10-26), pushed 2026-11-13, SPDX NOASSERTION with the licence blob read 2026-11-17 confirming Apache-2.0 (Copyright 2025 Big Local News) — consistent with session 1's independent reading. The high issue-to-star ratio is itself the evidence about per-jurisdiction scraper maintenance.

## 7. Assessment

Directly useful if you cover the US, and more broadly useful as a template: the one-scraper-per-jurisdiction-into-a-shared-schema pattern is how you build a durable public-records asset, and the open issue count is an honest warning about the ongoing cost. For your profile I would copy the architecture for whichever multi-jurisdiction records matter in your region, and budget continuing maintenance rather than treating collection as a one-off project.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release 1.2.178 (2026-10-26), 45 stars, 73 open issues. Very frequent releases (a 1.2.178 version number reflects continuous per-state fixes) under an academic programme; the backlog is intrinsic to scraping fifty changing sites.

## 9. Licensing

**Licence:** Apache-2.0 (licence blob read 2026-11-17, Copyright 2025 Big Local News; GitHub reports NOASSERTION — also independently recorded in session 1's a1disc/notes.md) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Collected notices are US state government records, generally freely usable.

**Restrictions:** Code permissive. Collected public records carry no material restriction in this case.

**Licence evidence:** https://github.com/biglocalnews/warn-scraper/blob/main/LICENSE

## 10. Costs

No fee. Negligible compute. The real cost is maintenance of per-state scrapers if you fork or extend it. Estimate.

## 11. Privacy and data flows

Scrapes public government sites; no personal data beyond what the notices themselves contain (employer names and layoff counts, sometimes with contact details).

## 12. Verdict

**Integrate**

## 13. Alternatives

- Copying the architecture for your own jurisdictions — the more transferable use
- [Scrapy](OSINT-C1-16.md) for building equivalent collectors from scratch
- [openstates-scrapers](OSINT-C3-13.md) as another multi-jurisdiction public-records collection model

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/biglocalnews/warn-scraper
- https://warn-scraper.readthedocs.io/
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

← 219. [Turf.js](JAI-A1-26.md) · 221. [DocumentCloud](JAI-A2-13.md) →
