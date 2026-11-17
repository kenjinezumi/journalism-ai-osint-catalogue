# Media Cloud API client

`JAI-A1-14` · **77/100** · overall rank 187 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 75) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 18) |
| **Subcategory** | News archive research |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Media Cloud |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (client) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mediacloud/api-client) · [Documentation](https://mediacloud.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 77/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python client for the Media Cloud Online News Archive and Directory, providing search over a large multi-country corpus of news content with source metadata and aggregate counts over time.

## Journalism / investigative use case

Answering how coverage of a topic developed across outlets and countries without building your own news archive: query attention over time, compare which outlets covered a claim, and identify when a narrative entered mainstream coverage — a media-analysis capability that would otherwise take months of collection.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Access to an existing large, multi-country news archive removes the collection problem entirely, which is the expensive part of media analysis
- Source directory with country and media-type metadata lets you frame comparisons properly rather than treating all outlets as equivalent
- Apache-2.0 client with active maintenance (v5.2.0 released 2026-10-06 with same-day push) and a clean tracker
- Academic provenance with published methodology, so analyses built on it are citable

## 5. Cons

- Dependent on Media Cloud's service, access terms and continued funding — a research-institution dependency whose continuity is outside your control and which has changed shape before
- Archive coverage is uneven by country and period, so an absence of coverage in the data may reflect collection gaps rather than editorial silence; this is the central analytical trap
- Access requires an API key and terms that were NOT verified in this survey — check before building on it
- Small client community (89 stars), so you will read source for unusual queries

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 89 stars with 3 open issues, release v5.2.0 (2026-10-06) with same-day push, Apache-2.0. Media Cloud's use in academic media research is well established; its current access terms were not verified here.

## 7. Assessment

Integrate it for media-attention analysis, treating coverage gaps as the main methodological risk — always check whether the outlets you expect are actually in the collection for the period you are analysing, and say so in the methodology note. For your profile it is the pragmatic alternative to building a news archive, which is a project you should not start unless Media Cloud's coverage genuinely fails you. Verify the access terms first.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-06, latest release v5.2.0 published the same day, 89 stars, 3 open issues. Current releases tracking an operating service; the client is small and the service is the substantive dependency.

## 9. Licensing

**Licence:** Apache-2.0 (client) _(SPDX verified)_

**Model / data licence:** Media Cloud archive access terms apply and were NOT verified in this survey; the underlying news content remains the publishers' copyright.

**Restrictions:** Client permissive. Archive access terms unverified — confirm before publishing derived datasets, and note that republishing article text raises publisher copyright separately.

**Licence evidence:** https://github.com/mediacloud/api-client/blob/main/LICENSE

## 10. Costs

Client free. API access terms and any tiers not verified in this survey; historically free for research use with a key. Confirm before planning.

## 11. Privacy and data flows

Queries go to Media Cloud, disclosing the topics and outlets you are researching to a third party. Not a concern for most media analysis; relevant if the topic itself is sensitive.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Service dependency with unverified access terms; uneven archive coverage by country and period

## 13. Alternatives

- GDELT for a different large-scale news-event archive with its own biases
- Building a targeted corpus with trafilatura plus Scrapy where coverage must be exact
- Internet Archive full-text search for historical web content

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/mediacloud/api-client
- https://mediacloud.org/
- https://github.com/mediacloud/api-client/blob/main/LICENSE

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

← 186. [FollowTheMoney (alephdata 3.x line)](JAI-A2-18.md) · 188. [CooRTweet](JAI-A4-13.md) →
