# changedetection.io

`SUR-B1-15` · **93/100** · overall rank 20 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 4) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 1) |
| **Subcategory** | Web change monitoring |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | dgtlmoon and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/dgtlmoon/changedetection.io) · [Documentation](https://changedetection.io/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 93/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. Note the project also sells a hosted version — that is a separate service under its own terms, not a licence restriction on the self-hosted code. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee for self-hosting. Infrastructure estimate: a small container; add a Playwright/Chromium container for JS-heavy pages, which roughly doubles the resource footprint. The project's hosted service is priced separately and was not verified in this survey. Operating effort is low.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/dgtlmoon/changedetection.io/blob/master/LICENSE
- https://github.com/dgtlmoon/changedetection.io
- https://changedetection.io/

---

## 1. Purpose

Self-hosted web-page change-detection service with CSS/XPath region selection, text and visual comparison, a browser-based fetcher for JavaScript-heavy pages, and notifications via Apprise to email, Slack, Discord and dozens of other channels.

## Journalism / investigative use case

Watch specific regions of agency pages, FOIA logs, press-release indexes or policy PDFs and get an alert with a diff when the wording quietly changes — the standard way a small newsroom notices that a government rewrote a page rather than announcing a change.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Region selection via CSS or XPath is what makes it usable on real government pages: you can watch the one table that matters and ignore the rotating banner that would otherwise fire alerts daily
- Largest community in this subcategory by a wide margin (35,859 stars) with frequent releases (0.70.3, 2026-11-09) — genuinely maintained rather than a weekend project
- Self-hosted with snapshots and diffs stored locally, and notifications routed wherever you choose
- Browser fetcher handles JavaScript-rendered portals that defeat simple HTTP watchers

## 5. Cons

- Per-URL watch model with no built-in editorial triage or annotation workflow, so a newsroom watching hundreds of pages has no way to separate reviewed from unreviewed changes — EDGI's platform exists precisely for that gap
- JS-heavy or bot-protected government portals may still block the fetcher, and diagnosing that is fiddly
- Frequent releases mean upgrade churn: 386 open issues and rapid version movement make pinning important
- Notification payloads can include page text, so an alert routed to a third-party service (Slack, Discord, email provider) discloses the monitored content to that provider

## 6. Feedback (documented)

No individual user reports verified in this survey. The quantitative signals are strong and checkable: 35,859 stars with 386 open issues and a release on 2026-11-09 — a large, active user base with a correspondingly large support load. Widely recommended in web-monitoring tool lists including EDGI's.

## 7. Assessment

My default recommendation for a small newsroom that wants page monitoring working this week. Two configuration decisions matter for your context: route notifications to an internal channel rather than a third-party chat service if the monitored pages are sensitive, and pin the version because the release cadence will otherwise surprise you. When the watch list grows past what one person can triage, graduate to EDGI's platform rather than adding more watches here.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 0.70.3 (2026-11-09), 35,859 stars, 386 open issues. Frequent point releases and daily commits; the large backlog reflects scale of use rather than neglect.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. Note the project also sells a hosted version — that is a separate service under its own terms, not a licence restriction on the self-hosted code.

**Licence evidence:** https://github.com/dgtlmoon/changedetection.io/blob/master/LICENSE

## 10. Costs

No fee for self-hosting. Infrastructure estimate: a small container; add a Playwright/Chromium container for JS-heavy pages, which roughly doubles the resource footprint. The project's hosted service is priced separately and was not verified in this survey. Operating effort is low.

## 11. Privacy and data flows

Snapshots and diffs stay in your self-hosted instance. The exposure point is notifications: payloads can include page text, so routing alerts through Slack, Discord or an external email provider discloses monitored content to them. Choose an internal channel for sensitive watches.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [urlwatch](SUR-B1-16.md) or webchanges for a CLI, version-controlled watchlist
- Klaxon for a reporter-facing point-and-click interface
- [EDGI web-monitoring-db](SUR-B1-20.md) when the watch list exceeds informal triage

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/dgtlmoon/changedetection.io
- https://changedetection.io/
- https://github.com/dgtlmoon/changedetection.io/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 19. [OpenAleph](JAI-A2-35.md) · 21. [Datasette](JAI-A2-09.md) →
