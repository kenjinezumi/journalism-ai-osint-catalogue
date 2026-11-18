# Whoogle Search

`OSINT-C1-04` · **39/100** · overall rank 355 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 136) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 44) |
| **Subcategory** | Meta-search |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Ben Busby (benbusby) |
| **Maintenance** | Archived or discontinued |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/benbusby/whoogle-search) · [Documentation](https://github.com/benbusby/whoogle-search#readme) |

**Scores** — relevance 2/5 · capability 1/5 · maintenance 0/5 · privacy 3/5 · usability 3/5 · licence+cost 4/5 → **weighted 39/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None, but the code is frozen and non-functional for its primary purpose. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. The viable fallback path (Google Custom Search API) is a paid dependency beyond 100 free queries per day — rates not verified in this survey.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/benbusby/whoogle-search/blob/main/LICENSE
- https://github.com/benbusby/whoogle-search

---

## 1. Purpose

Self-hosted, ad-free, JavaScript-free front end that proxied Google search results without cookies or tracking.

## Journalism / investigative use case

Historically used to query Google without a personalised session; now mainly a reference for why self-hosted Google front-ends are no longer viable, which is itself a useful fact when planning a research stack.

## 2. Audience

engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Solved a real problem well while it worked: Google results without a session, cookies or personalisation
- MIT licensed with a clean, small codebase worth reading if you are building any search proxy
- Large user base at archival (11,551 stars) with essentially no open issues, indicating it was finished rather than neglected

## 5. Cons

- ARCHIVED: GitHub API confirms archived=true, last push 2026-08-14 — read-only, no further development
- Depends on a Google scraping path that Google has closed, so the core function is broken rather than merely unmaintained
- The documented fallback is the paid Google Custom Search API (100 free queries per day, then paid), which defeats the original purpose and introduces a vendor dependency
- Any fork inherits the same blocked scraping path, so forking does not solve the problem

## 6. Feedback (documented)

No individual user reports verified. The decisive documented facts: archived=true per the GitHub API on 2026-11-17, and the project's own documentation of the Google Custom Search API fallback (100 free queries/day then paid) as the alternative to the blocked scraping path. 11,551 stars, 1 open issue, release v1.2.4 (2026-04-15).

## 7. Assessment

Reference only, and a clear data point for your planning: direct Google access is no longer available to self-hosted tooling, so a research stack must be built on metasearch across accessible engines (SearXNG), on independent indexes (Marginalia, YaCy), or on paid API access. Anyone proposing a Google-scraping component in 2026 should be shown this entry. Do not deploy.

## 8. Maintenance

**Archived or discontinued** — GitHub API 2026-11-17: archived=true, pushed_at 2026-08-14, latest release v1.2.4 (2026-04-15), 11,551 stars, 1 open issue. Archived by the maintainer, and the underlying capability is blocked upstream by Google — both code and function are dead.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None, but the code is frozen and non-functional for its primary purpose.

**Licence evidence:** https://github.com/benbusby/whoogle-search/blob/main/LICENSE

## 10. Costs

No fee. The viable fallback path (Google Custom Search API) is a paid dependency beyond 100 free queries per day — rates not verified in this survey.

## 11. Privacy and data flows

Queries were proxied from your instance to Google. With the Custom Search API fallback, queries go to Google under an API key tied to your account — a weaker privacy position than the original design.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Archived; the Google scraping path it depends on is closed

## 13. Alternatives

- [SearXNG](OSINT-C1-01.md) — the maintained replacement for the general need
- [Marginalia Search](OSINT-C1-05.md) or YaCy for independent indexes not dependent on Google
- Paid Google Custom Search API if Google results are genuinely required, accepting the cost and the account linkage

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/benbusby/whoogle-search
- https://github.com/benbusby/whoogle-search/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |

---

← 354. [FaceForensics++](JAI-A4-26.md) · 356. [Loki (OpenFactVerification)](JAI-A4-10.md) →
