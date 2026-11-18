# Awesome Website Change Monitoring

`SUR-B1-24` · **68/100** · overall rank 281 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 69) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 22) |
| **Subcategory** | Tool landscape reference |
| **Type** | dataset |
| **Bucket** | `verified-oss` |
| **Maintainer** | Environmental Data and Governance Initiative (EDGI) |
| **Maintenance** | Stable with low activity |
| **Licence** | CC0-1.0 |
| **Licence type** | Public domain |
| **Open-source status** | Open source |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring) · [Documentation](https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 68/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Public domain |
| **Exact licence (as recorded)** | CC0-1.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | CC0-1.0 — public domain dedication, so free to copy into internal docs. |
| **Restrictions** | None whatsoever. |
| **Open-source status** | **Open source** — Open data licence |
| **Software price** | **Unknown / not verified** — not established by the records |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** None to read. Note that the commercial services it catalogues have their own pricing, none of which was verified in this survey.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring/blob/main/LICENSE
- https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring

> **Unresolved:** the price is not established by these records — this is not a statement that it is free.

---

## 1. Purpose

Curated list of website change-monitoring tools and services, open-source and commercial, with a linked comparison spreadsheet.

## Journalism / investigative use case

The fastest way for a newsroom to see what monitoring options exist and which are abandoned before committing engineering time, and where commercial alternatives such as Fluxguard/Versionista, VisualPing, Wachete and PageFreezer are catalogued alongside open-source options.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

dataset · bucket `verified-oss`

## 4. Pros

- Covers commercial services alongside open-source tools, which is useful because the honest answer for some newsrooms is a paid service rather than a self-hosted deployment
- CC0-1.0, so you can copy and adapt it into internal documentation without any licence consideration
- Maintained by an organisation that actually runs monitoring at scale, so the curation reflects practical experience
- Points to a deeper comparison spreadsheet with feature-level detail that a README cannot carry

## 5. Cons

- Several entries are stale or unmaintained (NewsDiffs, NYTdiff, DiffEngine, Pagelyzer) and the list does not flag that — so it can send you toward dead tools, which this catalogue corrects
- Omits generalist tools journalists now often use, notably urlwatch, webchanges and the git-plus-screenshot pattern
- The substantive comparison lives in an external Google Spreadsheet linked from the README, so the authoritative content is not version-controlled with the list
- A list, not a tool: 515 stars and 16 open issues, last push 2026-08-11

## 6. Feedback (documented)

No individual user reports verified. Documented: CC0-1.0 licence; last push 2026-08-11; 515 stars with 16 open issues. The staleness of several listed entries was verified independently in this catalogue — diffengine (last release 2020) and NewsDiffs (default branch last commit 2018) are both listed without deprecation notes.

## 7. Assessment

Useful as a starting map, with the caveat that it does not distinguish live from dead. Read it alongside this catalogue's maintenance classifications rather than on its own. The genuinely valuable part for your profile is the commercial-service coverage: if your newsroom lacks ops capacity, a paid monitoring service may be the correct answer, and this list is the fastest way to see the field.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-08-11, no releases, 515 stars, 16 open issues. Three months since last push; a curated list updated episodically. Not declining, but entries have demonstrably aged without being marked.

## 9. Licensing

**Licence:** CC0-1.0 _(SPDX verified)_

**Model / data licence:** CC0-1.0 — public domain dedication, so free to copy into internal docs.

**Restrictions:** None whatsoever.

**Licence evidence:** https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring/blob/main/LICENSE

## 10. Costs

None to read. Note that the commercial services it catalogues have their own pricing, none of which was verified in this survey.

## 11. Privacy and data flows

No software and no data flows. The deeper comparison lives in an external Google Spreadsheet, so opening it discloses your interest to Google in the ordinary way.

## 12. Verdict

**Reference only**

## 13. Alternatives

- This catalogue's B1 segment for maintenance-verified assessments
- [changedetection.io](SUR-B1-15.md) or webchanges if you have already decided to self-host

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring
- https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring/blob/main/LICENSE

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

← 280. [GlotLID](JAI-A2-20.md) · 282. [Mihari](SUR-B2-11.md) →
