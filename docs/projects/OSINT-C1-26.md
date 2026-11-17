# ArchiveBot

`OSINT-C1-26` · **62/100** · overall rank 309 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 121) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 38) |
| **Subcategory** | Community rapid archiving |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | ArchiveTeam |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ArchiveTeam/ArchiveBot) · [Documentation](https://wiki.archiveteam.org/index.php/ArchiveBot) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 1/5 · usability 3/5 · licence+cost 5/5 → **weighted 62/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

IRC-driven distributed archiving system where volunteers request crawls of at-risk sites, which are executed across ArchiveTeam's pipeline fleet and ingested into Internet Archive collections.

## Journalism / investigative use case

Mobilise community archiving capacity when a large site must be preserved faster than one newsroom can manage — for example a government portal announced for shutdown, where thousands of pages must be captured in days.

## 2. Audience

journalist, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Access to capacity no newsroom has: ArchiveTeam's pipeline fleet can crawl at a scale and speed a single organisation cannot match
- Captures land in public ArchiveTeam/Internet Archive collections, so the preservation is durable and third-party attested rather than sitting on your disk
- Mature, long-running community infrastructure still receiving commits (pushed 2026-09-08)
- Costs you nothing but a request

## 5. Cons

- Not a private tool: you are requesting work from a community, with public IRC logs, so your interest in a specific site becomes public immediately — disqualifying when the target should not know
- Captures are ingested into public collections, so you cannot use it for material you intend to hold confidentially
- No control over timing or completeness: the community decides what gets crawled and how
- 194 open issues against 429 stars, and operating your own instance is impractical — this is a service you ask for, not software you run

## 6. Feedback (documented)

No individual user reports verified. Documented: 429 stars with 194 open issues, last push 2026-09-08, MIT licence. ArchiveTeam's track record in rescuing at-risk sites is extensively documented on its own wiki, which is the relevant context for whether a request is likely to be actioned.

## 7. Assessment

A genuinely useful escalation route for public-interest preservation at scale, with one hard constraint you must internalise: requesting a crawl is a public act. For your profile the decision rule is clean — if the target knowing you are interested is harmless or even helpful (an announced shutdown of a public dataset), use ArchiveBot; if it would compromise an investigation, capture it yourself with browsertrix-crawler and accept the smaller scale.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-08, no releases, 429 stars, 194 open issues. Two months since last push on long-lived community infrastructure; the large backlog is characteristic of volunteer-operated systems. The operational service rather than the repository is the artefact.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a. Captures enter public Internet Archive collections under their terms.

**Restrictions:** None material for the code. The operational consequence is the point: captures become public.

**Licence evidence:** https://github.com/ArchiveTeam/ArchiveBot/blob/master/LICENSE

## 10. Costs

Free. You are using donated community capacity, which carries an etiquette obligation rather than a monetary one.

## 11. Privacy and data flows

Not private: requests are made over a public IRC channel with public logs, and captures are ingested into public ArchiveTeam/Internet Archive collections. Treat any request as a public disclosure of your interest.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Requests and captures are public — unusable for confidential investigation

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md) or Heritrix for private capture under your own control
- [ArchiveBox](OSINT-C1-28.md) for a private self-hosted archive
- Direct Internet Archive 'Save Page Now' for individual pages

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/ArchiveTeam/ArchiveBot
- https://wiki.archiveteam.org/index.php/ArchiveBot

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

← 308. [CouncilSearcher](OSINT-C1-14.md) · 310. [DataIndex.us (Federal Data Terminations Tracker)](SUR-B1-27.md) →
