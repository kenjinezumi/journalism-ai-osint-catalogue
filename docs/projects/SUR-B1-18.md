# Klaxon (self-hosted)

`SUR-B1-18` · **72/100** · overall rank 248 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 63) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 20) |
| **Subcategory** | Web change monitoring |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | The Marshall Project |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/themarshallproject/klaxon) · [Documentation](https://github.com/themarshallproject/klaxon#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 2/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 72/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Self-hosted Rails application that lets non-technical users select page elements to watch via a point-and-click browser extension and receive email alerts when the selected content changes.

## Journalism / investigative use case

Give reporters without command-line skills a point-and-click way to watch FOIA disclosure logs, court dockets and agency pages and get alerted to newsworthy edits — built by a newsroom for exactly this purpose, which shows in the workflow assumptions.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Built by a working newsroom for reporters, so the selection and alerting flow matches how journalists actually monitor sources — the clearest journalism-native design in this subcategory
- The browser-extension selector removes the CSS/XPath barrier entirely, which is the single biggest obstacle to reporters self-serving on monitoring
- Watch list, snapshots and diffs live in the newsroom's own PostgreSQL instance, so monitored content stays internal
- Still receiving maintenance (pushed 2026-11-16) with 683 stars — the largest community of the newsroom-built options

## 5. Cons

- The README explicitly warns it 'may break unexpectedly' and may miss a change or fail to send mail — an honest disclosure that nonetheless means you cannot rely on absence of an alert
- Individual-user support has been discontinued, and recent repository activity is dependency maintenance rather than development, so the project is being kept alive rather than advanced
- Rails plus PostgreSQL plus SendGrid or SMTP is a real deployment, and the documented path assumes Heroku — awkward if you self-host elsewhere
- Email-only alerting by default (with optional Slack/Discord webhooks), so routing into a newsroom workflow takes extra work

## 6. Feedback (documented)

No individual user reports verified, but the project's own README contains the significant documented caveat — that it may break unexpectedly, miss changes or fail to send mail — and notes that individual-user support is discontinued. 683 stars, 16 open issues, release v0.7.0 (2026-03-09), last push 2026-11-16 consisting of dependency maintenance.

## 7. Assessment

Valuable for its reporter-facing design and worth deploying if you have Rails capacity and want journalists monitoring their own beats — that self-service property is what makes monitoring actually happen. But take the README's warning seriously: treat it as best-effort notification, never as a guarantee, and pair critical watches with a second tool. If you have no Rails capability, changedetection.io reaches a similar outcome with less deployment friction.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v0.7.0 (2026-03-09), 683 stars, 16 open issues. Recent pushes are dependency maintenance rather than feature work, individual-user support is discontinued per the project, and the README warns of unreliability. Declining rather than dormant: the lights are on, nobody is building.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/themarshallproject/klaxon/blob/master/LICENSE

## 10. Costs

No software fee. Infrastructure estimate: a Rails host plus PostgreSQL, plus an email-sending service (SendGrid or similar — small monthly cost, rates not verified here). Heroku was the documented deployment target, which carries its own hosting charges. Operating effort is moderate.

## 11. Privacy and data flows

Watch list, snapshots and diffs live in your own PostgreSQL instance. Alert emails route through the configured mail provider, which sees the alert content — choose an internal mail path for sensitive watches.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Project's own README warns it may break and may miss changes; individual-user support discontinued

## 13. Alternatives

- [changedetection.io](SUR-B1-15.md) — recommended alternative with a UI and much more active maintenance
- Klaxon Cloud (DocumentCloud add-on) if you want no infrastructure at all
- [webchanges](SUR-B1-17.md) where an engineer manages the watchlist on reporters' behalf

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/themarshallproject/klaxon
- https://github.com/themarshallproject/klaxon/blob/master/LICENSE

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

← 247. [asn (nitefood)](OSINT-C3-27.md) · 249. [Klaxon Cloud (DocumentCloud Add-On)](SUR-B1-19.md) →
