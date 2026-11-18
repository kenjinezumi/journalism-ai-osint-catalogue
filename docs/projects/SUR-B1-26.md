# NewsDiffs

`SUR-B1-26` · **34/100** · overall rank 360 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 80) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 27) |
| **Subcategory** | Stealth-edit tracking |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | Eric Price (ecprice) and collaborators |
| **Maintenance** | Dormant |
| **Licence** | MIT per session-1 inspection, but mixed per-file licensing was found and GitHub reports NOASSERTION — reuse requires file-by-file review |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ecprice/newsdiffs) · [Documentation](http://www.newsdiffs.org/) |

**Scores** — relevance 2/5 · capability 1/5 · maintenance 1/5 · privacy 3/5 · usability 1/5 · licence+cost 2/5 → **weighted 34/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT per session-1 inspection, but mixed per-file licensing was found and GitHub reports NOASSERTION — reuse requires file-by-file review |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | Unclear in aggregate. Do not vendor code from it without reviewing each file's header. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Not deployable on a supported runtime without substantial porting work.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ecprice/newsdiffs
- http://www.newsdiffs.org/

---

## 1. Purpose

Django application that scrapes news articles from configured sites on a schedule, stores every version, and publishes a public archive of detected post-publication edits.

## Journalism / investigative use case

The canonical prior art for stealth-edit tracking and a useful reference for how to structure per-site parsers and a public diff archive — not a tool to deploy today, but the project that established the practice of holding news organisations accountable for silent revisions.

## 2. Audience

engineer

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- Historically important: it demonstrated that systematic post-publication edit tracking is feasible and newsworthy, and the public-archive model shaped later work
- Per-site parser architecture is a reasonable design for the problem, and reading it saves you rediscovering the same structure
- 506 stars reflect genuine historical influence in this space

## 5. Cons

- Effectively abandoned: the last default-branch commit dates to 2018 and the stack targets Python 2.6+ with old Django versions — an end-of-life runtime that cannot be deployed safely
- GitHub reports SPDX NOASSERTION, and session-1 inspection found mixed per-file licensing, so reuse needs file-by-file review
- The README itself notes you must be a programmer to add a parser for each new site, so it never scaled beyond its curators
- 36 open issues, no releases; the public site's continuity is outside your control

## 6. Feedback (documented)

No individual user reports verified. Documented: last default-branch commit 2018 (with a 2026-04-13 push reflecting incidental repository activity rather than development), Python 2.6+ requirement, mixed per-file licensing and SPDX NOASSERTION, 506 stars with 36 open issues.

## 7. Assessment

Reference only, and specifically a cautionary one: per-site scrapers are a maintenance treadmill, which is why this project stopped. For your profile the lesson is to prefer feed- or sitemap-driven detection and generic diffing over bespoke parsers, and to accept lower coverage in exchange for a system that survives. If post-publication edit tracking matters to your beat, build it on webchanges or shot-scraper with a sitemap crawl rather than reviving this.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2026-04-13 but the default-branch development history ends in 2018; no releases, SPDX NOASSERTION, 506 stars, 36 open issues. Python 2.6+ and old Django make it non-deployable. The recent push date is misleading and is the reason push recency alone is not used for classification in this catalogue.

## 9. Licensing

**Licence:** MIT per session-1 inspection, but mixed per-file licensing was found and GitHub reports NOASSERTION — reuse requires file-by-file review _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Unclear in aggregate. Do not vendor code from it without reviewing each file's header.

**Licence evidence:** https://github.com/ecprice/newsdiffs

## 10. Costs

No fee. Not deployable on a supported runtime without substantial porting work.

## 11. Privacy and data flows

Self-hosted; the original project published detected diffs publicly on its own website. A revival would need an explicit decision about publication.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Python 2.6-era stack, abandoned since 2018, mixed per-file licensing

## 13. Alternatives

- [webchanges](SUR-B1-17.md) or changedetection.io for maintained monitoring
- [shot-scraper](SUR-B1-23.md) plus git for a version history of specific articles
- [EDGI web-monitoring-db](SUR-B1-20.md) for a platform with analyst triage

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ecprice/newsdiffs
- http://www.newsdiffs.org/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |

---

← 359. [pagodo](OSINT-C1-07.md) · 361. [ClaimsKG extractor](JAI-A4-09.md) →
