# news-homepages

`JAI-A1-31` · **76/100** · overall rank 201 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 83) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 20) |
| **Subcategory** | Media monitoring archive |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Ben Welsh (palewire) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/palewire/news-homepages) · [Documentation](https://palewi.re/docs/news-homepages/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 76/100**

---

## 1. Purpose

Toolkit and running archive that captures screenshots, full-text extracts, accessibility reports and hyperlink data from hundreds of news homepages on a schedule, publishing the results openly.

## Journalism / investigative use case

Studying editorial judgement over time: which stories a publication led with, how long a story stayed on the homepage, and how coverage differed across outlets on a given day — questions about media behaviour that require a systematic homepage archive nobody otherwise keeps.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Captures a record that genuinely does not exist elsewhere: homepage prominence over time is editorial evidence, and it disappears within hours if not captured
- Publishes the archive openly, so the research value is available without running anything — a rare and generous model
- GPL-3.0 with very active maintenance (0.0.124 released 2026-11-16, pushed the same day) by a well-known data journalist
- Multi-modal capture (screenshot, text, links, accessibility) means several kinds of analysis are possible from one archive

## 5. Cons

- Narrow analytical scope: it answers questions about homepage prominence, which is a specialised interest even within media research
- Capture is of the homepage as the capturing machine saw it, so personalisation, geography and A/B variation all affect what is recorded — a methodological caveat for any comparison
- Small project (163 stars, 28 open issues) dependent on one maintainer, though the published archive persists independently
- Storage grows continuously, so self-hosting a long-running capture is a real commitment

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 163 stars with 28 open issues, release 0.0.124 (2026-11-16) with same-day push, GPL-3.0. The maintainer is an established figure in data journalism and the archive is published openly, which is verifiable from the project site.

## 7. Assessment

Use the published archive rather than running your own capture unless you need outlets it does not cover — the research value is available for free and the storage commitment is someone else's. For your profile the interesting application is comparative: documenting that a state-aligned outlet led with a particular framing for days while independent outlets did not is a concrete, archived finding about editorial behaviour, and this is one of very few sources that supports it.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 0.0.124 published the same day, 163 stars, 28 open issues. Frequent releases reflecting continuous operation of the capture pipeline.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** Captured homepage content remains the publishers' copyright; the archive is published for research use.

**Restrictions:** GPL-3.0 on the toolkit. Republishing captured homepage screenshots raises publisher copyright, which is a fair-dealing judgement rather than a licence question.

**Licence evidence:** https://github.com/palewire/news-homepages/blob/main/LICENSE

## 10. Costs

No fee to use the published archive. Self-hosting capture: continuous browser automation plus growing storage — a real and open-ended commitment. Estimate.

## 11. Privacy and data flows

Captures public homepages; no personal data. Your own capture would be visible to the publishers as automated traffic.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Internet Archive captures for ad-hoc historical homepage lookups
- [shot-scraper](SUR-B1-23.md) plus git for capturing a small set of homepages yourself
- Media Cloud for article-level rather than homepage-level coverage analysis

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/palewire/news-homepages
- https://palewi.re/docs/news-homepages/
- https://github.com/palewire/news-homepages/blob/main/LICENSE

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

← 200. [SpyGuard](SUR-B3-12.md) · 202. [OONI backend](SUR-B1-04.md) →
