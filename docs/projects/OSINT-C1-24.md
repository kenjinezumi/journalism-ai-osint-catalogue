# grab-site

`OSINT-C1-24` · **60/100** · overall rank 321 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 126) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 40) |
| **Subcategory** | Rapid-response archiving |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | ArchiveTeam |
| **Maintenance** | Dormant |
| **Licence** | MIT (GitHub API reports NOASSERTION) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ArchiveTeam/grab-site) · [Documentation](https://github.com/ArchiveTeam/grab-site#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 60/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (GitHub API reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material; confirm the licence file for records. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Disk for WARCs. Hidden cost is install effort on a current system.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ArchiveTeam/grab-site
- https://github.com/ArchiveTeam/wpull

---

## 1. Purpose

Archival crawler built on wpull that produces WARCs with a live dashboard, allowing the operator to add ignore patterns and adjust scope while the crawl is running.

## Journalism / investigative use case

Rapid-response archiving of a site at risk of deletion, with the ability to steer the crawl while it runs — which matters when you have minutes rather than hours and need to avoid wasting the window on a calendar or a session-ID trap.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Live steering during a crawl is the distinguishing feature and genuinely valuable under time pressure: you can see the crawl falling into a trap and exclude it without restarting
- WARC output, so captures are evidentiary rather than loose files
- Developed by ArchiveTeam, whose entire purpose is rapid preservation of at-risk sites, so the design priorities match the emergency use case
- Large community for a specialist tool (1,617 stars)

## 5. Cons

- Eighteen months since the last push (2025-05-23) and it depends on wpull, which was itself last pushed in April 2024 — a dormant dependency under a slowing project is a compounding risk
- 103 open issues and no release objects (latest tag 2.2.7), so there is no supported version to pin
- GitHub reports SPDX NOASSERTION despite MIT, so licence records need the file reference
- Python dependency chain of this age is increasingly awkward to install on current systems

## 6. Feedback (documented)

No individual user reports verified. Documented: last push 2025-05-23, 1,617 stars, 103 open issues, no releases, SPDX NOASSERTION; its dependency wpull was last pushed 2024-04-29 (verified separately in this catalogue). The dependency's dormancy is the more serious signal.

## 7. Assessment

The steering capability is worth knowing about, but I would not make it the rapid-response tool of record given the dormant wpull dependency. For your profile the more reliable emergency path is browsertrix-crawler with a prepared configuration, or `wget --warc` for a quick WARC with no setup — both maintained. If you do keep grab-site, containerise it now while it still installs, because the Python chain will get harder.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2025-05-23, no release objects, latest tag 2.2.7, SPDX NOASSERTION, 1,617 stars, 103 open issues. Eighteen months without commits, and its core dependency wpull last pushed 2024-04-29. Both layers stalled, so dormant rather than merely low-activity.

## 9. Licensing

**Licence:** MIT (GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** None material; confirm the licence file for records.

**Licence evidence:** https://github.com/ArchiveTeam/grab-site

## 10. Costs

No fee. Disk for WARCs. Hidden cost is install effort on a current system.

## 11. Privacy and data flows

WARC and logs are written locally; nothing is uploaded. The target sees your crawl.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Dormant since May 2025; depends on wpull, dormant since April 2024

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md) with a prepared config for maintained rapid capture
- wget --warc for an immediate, dependency-free WARC
- [ArchiveBot](OSINT-C1-26.md) to mobilise community capacity for a very large at-risk site

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ArchiveTeam/grab-site
- https://github.com/ArchiveTeam/wpull

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

← 320. [gdelt-doc-api](JAI-A1-15.md) · 322. [news-please](JAI-A1-02.md) →
