# CouncilSearcher

`OSINT-C1-14` · **63/100** · overall rank 308 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 120) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 37) |
| **Subcategory** | Local-government records search |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/CouncilSearcher) · [Documentation](https://github.com/bellingcat/CouncilSearcher#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 2/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 63/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Tool that searches across UK and Ireland local-council meeting records and transcripts for keywords or named individuals.

## Journalism / investigative use case

Local-government accountability reporting: find what a named councillor actually said about an issue across many meeting transcripts — work that otherwise means opening dozens of PDFs on dozens of council websites.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Targets a genuinely under-served area: local-government records are where accountability journalism has thinned most, and they are fragmented across hundreds of sites
- Cross-council search is the specific capability that makes a pattern story possible ('fourteen councils discussed the same contractor')
- MIT licensed, small and readable, so adapting the approach to another jurisdiction is feasible
- Built by Bellingcat with practising investigators in mind

## 5. Cons

- Scoped to UK and Ireland, so it is irrelevant outside those jurisdictions and the code would need real work to generalise
- Small project with light maintenance: 17 stars, 7 open issues, last push 2026-01-07 — ten months before this survey
- Depends on council websites and transcript sources whose structures change, so coverage will silently degrade
- No releases, so there is no version to pin

## 6. Feedback (documented)

No individual user reports verified — 17 stars means there is minimal community signal. Documented: last push 2026-01-07, 7 open issues, no releases, MIT licence.

## 7. Assessment

Relevant only if your work touches UK or Irish local government, in which case it is worth trying despite light maintenance — the alternative is manual PDF trawling. The more generalisable value for your profile is the pattern: a cross-jurisdiction transcript index is a high-value, low-glamour capability, and building one for the jurisdictions you cover (using Scrapy for collection and Datasette or Solr for search) is a realistic project with a clear accountability payoff.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-01-07, no releases, 17 stars, 7 open issues. Ten months without activity on a tool whose data sources (council websites) change continuously — for a scraper-dependent project this is a material decline signal rather than benign stability.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Council records are public documents subject to the relevant jurisdiction's terms.

**Restrictions:** None material.

**Licence evidence:** https://github.com/bellingcat/CouncilSearcher/blob/main/LICENSE

## 10. Costs

No fee. Minimal compute; storage for fetched records.

## 11. Privacy and data flows

Fetches public council records to local storage. Your requests are visible to the council websites, which is unremarkable for public records.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- UK/Ireland only; scraper-dependent with ten months of no maintenance

## 13. Alternatives

- [Scrapy](OSINT-C1-16.md) plus Datasette to build an equivalent index for your own jurisdictions
- mySociety tooling (TheyWorkForYou, Alaveteli) for UK parliamentary and FOI material
- Manual search for a one-off question about a single council

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/bellingcat/CouncilSearcher
- https://github.com/bellingcat/CouncilSearcher/blob/main/LICENSE

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

← 307. [juditha](OSINT-C3-09.md) · 309. [ArchiveBot](OSINT-C1-26.md) →
