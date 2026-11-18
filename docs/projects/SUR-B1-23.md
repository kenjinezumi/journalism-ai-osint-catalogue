# shot-scraper

`SUR-B1-23` · **83/100** · overall rank 122 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 33) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 6) |
| **Subcategory** | Scheduled capture and monitoring |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Simon Willison |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/simonw/shot-scraper) · [Documentation](https://shot-scraper.datasette.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 83/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CI minutes if run in GitHub Actions (free tier is usually sufficient for modest schedules; current limits not verified here) or a small host. Playwright browser downloads add disk. Negligible.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/simonw/shot-scraper/blob/main/LICENSE
- https://github.com/simonw/shot-scraper
- https://shot-scraper.datasette.io/

---

## 1. Purpose

CLI wrapper over Playwright that takes screenshots of web pages, extracts content by executing JavaScript against them, and is designed to be driven from YAML configuration in CI.

## Journalism / investigative use case

Run a scheduled job that screenshots or extracts a government page and commits the result to Git, turning every quiet edit into a dated, diffable commit you can point at in a story — a monitoring system built from a CLI, a repository and a cron schedule.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- The git-commit-as-monitoring pattern is elegant and cheap: version history gives you dated evidence, diffs and an audit trail with no bespoke platform
- JavaScript extraction means you can pull a specific value (a number from a dashboard, a row from a table) and commit that, making the diff semantically meaningful rather than pixel noise
- Apache-2.0, actively released (1.12, 2026-09-13), excellent documentation, and composes naturally with git-history and Datasette for querying the time series
- Trivial to run in GitHub Actions or any CI, so there is no server to operate

## 5. Cons

- No notification or diff-review layer — you assemble alerting yourself from git tooling or CI, which is fine for an engineer and a barrier for anyone else
- Requires comfort with YAML, Git and CI, so it is not a reporter-facing tool
- Screenshots alone are not text-diffable, so you must pair them with JavaScript or text extraction to get meaningful diffs — a design decision people get wrong initially
- If the monitoring repository is public, the monitored URLs and captured content become public, which can disclose an investigation's targets

## 6. Feedback (documented)

No individual user reports verified. Documented: 2,609 stars with 63 open issues, release 1.12 (2026-09-13), last push 2026-10-14. The git-commit monitoring pattern is documented by the maintainer and widely used alongside Datasette tooling in data-journalism contexts.

## 7. Assessment

My preferred lightweight monitoring approach for an engineer-led team, because the evidence artefact (a git history) is simultaneously the audit trail and the alerting substrate. For your profile the one rule that matters: keep the monitoring repository private unless you intend your targets to be public, since a public repo of watched URLs is a map of your investigations. Add text extraction alongside screenshots so diffs are readable.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-14, latest release 1.12 (2026-09-13), 2,609 stars, 63 open issues. Regular releases from a maintainer with a strong track record of long-term project care.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/simonw/shot-scraper/blob/main/LICENSE

## 10. Costs

No fee. CI minutes if run in GitHub Actions (free tier is usually sufficient for modest schedules; current limits not verified here) or a small host. Playwright browser downloads add disk. Negligible.

## 11. Privacy and data flows

Outputs land in your repository or local disk. The critical consideration is repository visibility: if the repo is public, the monitored URLs and captured content become public. Private repositories keep both internal.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [changedetection.io](SUR-B1-15.md) for a UI and built-in alerting
- [webchanges](SUR-B1-17.md) for CLI monitoring with notification backends included
- [Scoop](OSINT-C1-36.md) where you need provenance-attested single-page captures rather than a time series

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/simonw/shot-scraper
- https://shot-scraper.datasette.io/
- https://github.com/simonw/shot-scraper/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 121. [rigour](JAI-A2-44.md) · 123. [VeraCrypt](SUR-B3-22.md) →
