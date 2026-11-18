# Photon

`OSINT-C1-20` · **64/100** · overall rank 296 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 113) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 35) |
| **Subcategory** | Web reconnaissance |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | s0md3v |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/s0md3v/Photon) · [Documentation](https://github.com/s0md3v/Photon#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 64/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | GPL-3.0 limits embedding in proprietary tooling. Note that harvested personal data carries data-protection obligations independent of the licence. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Negligible compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/s0md3v/Photon/blob/master/LICENSE
- https://github.com/s0md3v/Photon

---

## 1. Purpose

Fast Python crawler that harvests URLs, email addresses, social handles, document links, subdomains and JavaScript files from a target site in a single pass.

## Journalism / investigative use case

Harvest contact details, document links and handles scattered across a target website in one pass — useful for building a contact list for a company under investigation, or for finding the PDFs buried in an agency site.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Single-pass extraction of several artefact types (emails, handles, documents, subdomains) is efficient for reconnaissance, where you otherwise run four tools
- Optionally queries the Internet Archive CDX, so it finds URLs that no longer exist on the live site — a genuinely useful investigative addition
- Lightweight pure-Python with no heavy dependencies, so it runs anywhere
- Large user base (13,350 stars) and a readable codebase

## 5. Cons

- Light maintenance cadence relative to its age: the last release v1.3.0 dates from 2019-04-05, with the last push 2026-10-17 — commits continue but release engineering stopped years ago
- No JavaScript rendering, so modern dynamic sites yield little
- Harvesting email addresses and handles creates a personal-data collection with attendant data-protection obligations that reporters rarely consider
- 61 open issues; security-tooling heritage means defaults are not tuned for politeness

## 6. Feedback (documented)

No individual user reports verified. Documented: 13,350 stars with 61 open issues, release v1.3.0 (2019-04-05), last push 2026-10-17. The seven-year gap between the last release and current commits is the notable signal.

## 7. Assessment

Still useful for its specific harvesting job, with two cautions for your work. First, the lack of releases means pinning to a commit rather than a version. Second and more important: the output is a personal-data set (emails, names, handles), so treat it as regulated material with a retention decision, not as a scratch file — that is a discipline most OSINT tooling ignores and that a newsroom cannot. Pair with katana for completeness on dynamic sites.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-17, latest release v1.3.0 (2019-04-05), 13,350 stars, 61 open issues. Commits within the last month but no release in seven years — a maintained-but-unreleased pattern. Classified stable-low rather than declining because activity is current.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** GPL-3.0 limits embedding in proprietary tooling. Note that harvested personal data carries data-protection obligations independent of the licence.

**Licence evidence:** https://github.com/s0md3v/Photon/blob/master/LICENSE

## 10. Costs

No fee. Negligible compute.

## 11. Privacy and data flows

Crawls the target directly with results written to local JSON/text, so the target sees your requests. The more significant privacy issue is on your side: you are creating a collection of other people's contact details, which needs a retention and protection decision.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [katana](OSINT-C1-15.md) for more thorough modern URL discovery
- [theHarvester](OSINT-C3-28.md) for email and host harvesting from public sources rather than a site crawl
- Manual review for small targets, avoiding the personal-data collection entirely

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/s0md3v/Photon
- https://github.com/s0md3v/Photon/blob/master/LICENSE

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

← 295. [Overview](OSINT-C3-04.md) · 297. [SSLyze](OSINT-C3-26.md) →
