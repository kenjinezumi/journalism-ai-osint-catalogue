# pagodo

`OSINT-C1-07` · **36/100** · overall rank 359 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 137) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 45) |
| **Subcategory** | Search dorking |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | opsdisk |
| **Maintenance** | Archived or discontinued |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/opsdisk/pagodo) · [Documentation](https://github.com/opsdisk/pagodo#readme) |

**Scores** — relevance 2/5 · capability 1/5 · maintenance 0/5 · privacy 2/5 · usability 3/5 · licence+cost 4/5 → **weighted 36/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | The GHDB dork catalogue is maintained by Offensive Security under its own terms, not covered by pagodo's licence. |
| **Restrictions** | GPL-3.0 on the code. GHDB content terms are separate. Automated querying breaches Google's terms of service — a terms rather than licence issue, but a real one. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Not operable for its primary purpose.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/opsdisk/pagodo/blob/master/LICENSE
- https://github.com/opsdisk/pagodo

---

## 1. Purpose

Tool that scraped the Google Hacking Database for dork patterns and ran them against Google to find exposed files, directories and interfaces on a target domain.

## Journalism / investigative use case

Reference implementation of bulk dorking workflows; its GHDB scraper still documents dork syntax that remains useful for manual searching — for example finding exposed procurement spreadsheets or misconfigured document directories on a target's domain.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- The GHDB dork catalogue it scrapes remains a genuinely useful reference for manual search syntax, independent of the automation
- Clean, readable implementation of the dorking workflow, with GPL-3.0 licensing
- Had a long run as the standard tool in this niche, so understanding it explains most dorking tooling you will encounter

## 5. Cons

- ARCHIVED: the GitHub API confirms archived=true as of this survey, with the final release v2.8.0 on 2026-11-01 — the maintainer wound it down rather than abandoning it quietly
- Automated Google dorking is broadly non-functional as of late 2026 because of Google's anti-scraping measures, so the core capability no longer works regardless of code quality
- Dork queries issued directly to Google from your IP are a visible, attributable pattern — and in an investigation that pattern can be linked to you
- Depends on GHDB (Offensive Security), a third-party catalogue whose availability and terms you do not control

## 6. Feedback (documented)

No individual user reports verified. Decisive documented facts: archived=true per the GitHub API on 2026-11-17 with a final release v2.8.0 (2026-11-01); 3,418 stars with 0 open issues. The practical collapse of automated Google dorking in 2026 is corroborated by the same pattern in dorks_hunter and Whoogle.

## 7. Assessment

Reference only. The honest conclusion for your work is that dorking is now a manual technique: keep the GHDB syntax patterns to hand and run them by hand through SearXNG or directly, accepting low volume. Do not build a pipeline on automated dorking — it will fail and, worse, will fail intermittently in ways that look like 'nothing found'. If exposed-file discovery matters, katana or a targeted crawl of the domain is the reliable substitute.

## 8. Maintenance

**Archived or discontinued** — GitHub API 2026-11-17: archived=true, pushed_at 2026-11-01, latest release v2.8.0 (2026-11-01), 3,418 stars, 0 open issues. Archived with a final release — an orderly wind-down. The upstream capability (Google scraping) is independently blocked.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** The GHDB dork catalogue is maintained by Offensive Security under its own terms, not covered by pagodo's licence.

**Restrictions:** GPL-3.0 on the code. GHDB content terms are separate. Automated querying breaches Google's terms of service — a terms rather than licence issue, but a real one.

**Licence evidence:** https://github.com/opsdisk/pagodo/blob/master/LICENSE

## 10. Costs

No fee. Not operable for its primary purpose.

## 11. Privacy and data flows

Dork queries were issued directly to Google from your IP — a highly visible and attributable pattern. Anyone reviving this approach should consider that the search provider can profile the campaign.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Archived; automated Google dorking is non-functional as of late 2026

## 13. Alternatives

- Manual dorking through SearXNG at low volume
- [katana](OSINT-C1-15.md) for crawling a target domain to enumerate files and paths directly
- [uncover](OSINT-C1-10.md) for exposed-infrastructure discovery via scan databases (paid API keys)

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/opsdisk/pagodo
- https://github.com/opsdisk/pagodo/blob/master/LICENSE

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

← 358. [CooRnet](JAI-A4-14.md) · 360. [NewsDiffs](SUR-B1-26.md) →
