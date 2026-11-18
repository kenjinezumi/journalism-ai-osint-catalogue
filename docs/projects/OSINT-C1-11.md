# Zoekplaatje

`OSINT-C1-11` · **77/100** · overall rank 189 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 62) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 19) |
| **Subcategory** | Search-results capture |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Digital Methods Initiative (University of Amsterdam) |
| **Maintenance** | Actively maintained |
| **Licence** | MPL-2.0 (GitHub API reports NOASSERTION) |
| **Licence type** | Weak copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/digitalmethodsinitiative/zoekplaatje) · [Documentation](https://github.com/digitalmethodsinitiative/zoekplaatje#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 77/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Weak copyleft |
| **Exact licence (as recorded)** | MPL-2.0 (GitHub API reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a. Captured SERP content belongs to the engines and publishers. |
| **Restrictions** | MPL-2.0 file-level copyleft on modifications. Capturing SERPs may engage engine terms of service — a separate question from the licence, and worth considering before a large collection campaign. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. No infrastructure. Cost is analyst time performing searches.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/digitalmethodsinitiative/zoekplaatje

---

## 1. Purpose

Firefox extension that records the search-engine results pages a user visits — result order, snippets, ads, timestamps — and exports them as structured data for analysis.

## Journalism / investigative use case

Document what a search engine actually showed, when, and in what order — the evidence base for algorithmic-bias, search-manipulation and disinformation-ranking stories, where the claim is about the ranking itself and a screenshot is not enough.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Captures ranking order and snippet text as structured data, which is precisely the artefact an algorithmic-accountability story needs and which no screenshot provides
- Data stays local in the browser and is exported by the user, so the capture process itself leaks nothing
- Built by a research group with a methodological track record in platform studies, so the data model is designed for analysis rather than display
- Still receiving commits (pushed 2026-11-17), unusual longevity for a research extension

## 5. Cons

- Very small user base (14 stars) and Firefox-only, so it is a specialist instrument rather than general tooling
- Engine coverage is limited to implemented parsers, and engines change their markup frequently — a parser that silently stops matching produces empty captures
- Manual: someone must actually perform the searches, so systematic comparison across accounts, locations or times requires disciplined protocol design by you
- GitHub reports SPDX NOASSERTION despite MPL-2.0, so compliance records need the file reference

## 6. Feedback (documented)

No individual user reports verified — 14 stars means there is no community signal to report. Documented: MPL-2.0 with SPDX NOASSERTION, release v1.12 (2026-01-23), last push 2026-11-17. DMI tools are used in academic platform research, which is relevant adjacent credibility.

## 7. Assessment

A narrow instrument that is close to irreplaceable when your story is about search ranking. For your profile the methodological work matters more than the tool: define the protocol (which queries, from which accounts, locations and times) before collecting, because the finding lives or dies on comparability. Verify the parser is capturing before running a campaign — a silent parser failure would waste the whole collection.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.12 (2026-01-23), SPDX NOASSERTION (MPL-2.0 per repository), 14 stars, 8 open issues. Same-day commits from an institutional research group; tiny community but current maintenance.

## 9. Licensing

**Licence:** MPL-2.0 (GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Captured SERP content belongs to the engines and publishers.

**Restrictions:** MPL-2.0 file-level copyleft on modifications. Capturing SERPs may engage engine terms of service — a separate question from the licence, and worth considering before a large collection campaign.

**Licence evidence:** https://github.com/digitalmethodsinitiative/zoekplaatje

## 10. Costs

No fee. No infrastructure. Cost is analyst time performing searches.

## 11. Privacy and data flows

Captured SERP data is stored locally in the browser and exported by the user — nothing is uploaded. Note that the searches themselves are visible to the engines in the normal way, so the search campaign has a visible footprint even if the capture does not.

## 12. Verdict

**Pilot**

## 13. Alternatives

- 4CAT for broader platform data collection and analysis
- [shot-scraper](SUR-B1-23.md) for scripted screenshot evidence of SERPs (weaker as structured data)
- Manual screenshots plus a disciplined logging spreadsheet for very small studies

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/digitalmethodsinitiative/zoekplaatje

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

← 188. [CooRTweet](JAI-A4-13.md) · 190. [Inspect AI](JAI-A3-15.md) →
