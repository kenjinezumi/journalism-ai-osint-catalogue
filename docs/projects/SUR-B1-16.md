# urlwatch

`SUR-B1-16` · **80/100** · overall rank 155 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 42) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 9) |
| **Subcategory** | Web change monitoring |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Thomas Perl (thp) |
| **Maintenance** | Stable with low activity |
| **Licence** | BSD-3-Clause (LICENSE file read directly; GitHub API reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/thp/urlwatch) · [Documentation](https://urlwatch.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 80/100**

---

## 1. Purpose

Command-line tool that fetches URLs or runs shell commands on a schedule, applies filters to normalise the content, and reports diffs via email, Slack, Matrix, stdout and other backends.

## Journalism / investigative use case

Script a reproducible watchlist of statute, regulation or guidance pages in version control, and receive diffs by email, Slack, Matrix or stdout when an official page is edited — the engineer's answer to monitoring, where the watchlist itself is reviewable as code.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Configuration as code means your watchlist is version-controlled and reviewable, which is a genuine methodological advantage over a UI-managed list — you can show what you were watching on a given date
- Filter pipeline (html2text, jq, CSS selectors, regex) is powerful enough to suppress boilerplate churn that would otherwise drown real changes
- Can watch command output, not just URLs, so an API endpoint or a database query becomes monitorable with no extra tooling
- Mature and stable with a large user base (3,148 stars) and a small backlog relative to that

## 5. Cons

- CLI and text-first with no web UI or multi-user triage, so it does not scale to a team reviewing changes together
- No built-in archiving of the captured snapshot as evidence — you get a diff, not a dated preservation copy, so pair it with a capture tool if the change may be disputed
- Four-month gap since last push (2026-07-10) and GitHub reports SPDX NOASSERTION despite a BSD-3-Clause licence, with no GitHub release objects (latest tag 2.29)
- The maintainer has signalled interest in a successor project over the years, so long-term direction is less certain than the install base suggests

## 6. Feedback (documented)

No individual user reports verified. Documented: 3,148 stars with 85 open issues; last push 2026-07-10; SPDX NOASSERTION at the API level with the licence resolved to BSD-3-Clause by reading the file (session-1 verification, retained). webchanges exists explicitly as a more actively developed fork-descendant, which is itself a signal about urlwatch's cadence.

## 7. Assessment

Choose it when you want the watchlist in git and the whole thing auditable — that is a real advantage for a methodology note. But given the four-month quiet period and the existence of webchanges as a more actively developed descendant, I would evaluate webchanges first for a new deployment. Whichever you pick, add a capture step (Scoop or ArchiveBox) so you hold dated evidence of the before state, not just a diff.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-07-10, no GitHub release objects, latest tag 2.29, SPDX NOASSERTION (licence resolved to BSD-3-Clause by file inspection), 3,148 stars, 85 open issues. Four months quiet on a mature, feature-complete tool; not declining, but webchanges is the more active line.

## 9. Licensing

**Licence:** BSD-3-Clause (LICENSE file read directly; GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/thp/urlwatch/blob/master/COPYING

## 10. Costs

No fee. Runs as a cron job on any small host. Optional Playwright for browser jobs adds resource cost. Negligible.

## 11. Privacy and data flows

Snapshot cache and diffs stay on the local machine; only the configured reporter transmits content off-box. Choosing stdout or a local mailbox keeps everything internal — the most private option in this subcategory.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [webchanges](SUR-B1-17.md) — the more actively developed descendant, recommended for new deployments
- [changedetection.io](SUR-B1-15.md) for a UI and visual diffing
- [shot-scraper](SUR-B1-23.md) plus git for screenshot-and-commit monitoring

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/thp/urlwatch
- https://urlwatch.readthedocs.io/

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

← 154. [Skyfield](OSINT-C2-38.md) · 156. [name-variant-search](OSINT-C1-12.md) →
