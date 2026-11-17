# EDGI web-monitoring-db

`SUR-B1-20` · **79/100** · overall rank 161 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 45) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 10) |
| **Subcategory** | Government page monitoring platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Environmental Data and Governance Initiative (EDGI) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/edgi-govdata-archiving/web-monitoring-db) · [Documentation](https://github.com/edgi-govdata-archiving/web-monitoring-db#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 79/100**

---

## 1. Purpose

Rails and PostgreSQL service that stores versions of monitored web pages, computes and serves diffs, and provides an annotation workflow for analysts to classify whether a change is substantive.

## Journalism / investigative use case

The newsroom-grade pipeline for monitoring thousands of government pages at once, with an annotation workflow so analysts can separate boilerplate churn from substantive policy rewording before anything reaches reporters — the capability that made EDGI's tracking of US environmental-policy page changes publishable.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- The analyst annotation workflow is the distinguishing feature and the reason this exists: at thousands of pages, the bottleneck is human triage, not detection, and no other tool here addresses it
- Proven at exactly this scale by EDGI's own long-running government-page monitoring programme, which produced published findings — the most relevant provenance available
- Uses the Internet Archive Wayback Machine as a version source, so you inherit historical coverage rather than only monitoring forward from today
- Actively maintained (pushed 2026-11-13) with a clear separation between storage/annotation (this) and diffing (web-monitoring-diff)

## 5. Cons

- A multi-repository distributed system (db + ui + processing + diff + ops) that needs real engineering and ops capacity — the heaviest deployment in this subcategory and overkill below a few hundred monitored pages
- GPL-3.0 copyleft is a constraint some newsroom legal teams will want to review, particularly if you expose a modified instance
- It is a monitoring platform, not a notification tool: alerting and reporter-facing presentation are things you build around it
- Small community (24 stars, 14 open issues) and no release objects, so operational support comes from reading the code and EDGI's documentation

## 6. Feedback (documented)

No individual user reports verified. The documented provenance is strong: EDGI operates a public instance and has used this stack for sustained government-page monitoring with published outputs. 24 stars, 14 open issues, last push 2026-11-13, no releases.

## 7. Assessment

The right answer when monitoring becomes a programme rather than a few watches — and for an outlet tracking state rewriting of official records, that threshold arrives quickly. For your profile I would scope it as a project with named analyst capacity, because deploying it without people to work the annotation queue reproduces the problem it solves. Pair with web-monitoring-diff and keep the version source pointed at Wayback so you get history for free.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, no release objects, 24 stars, 14 open issues. Current commits from an organisation that operates the software publicly; small community but demonstrably in production use.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Page versions sourced from the Internet Archive are subject to IA's terms and the original publishers' rights.

**Restrictions:** GPL-3.0: distributing a modified version obliges source release; hosting a modified instance for third parties is the case to review with legal counsel.

**Licence evidence:** https://github.com/edgi-govdata-archiving/web-monitoring-db/blob/main/LICENSE

## 10. Costs

No software fee. Infrastructure estimate: Rails app servers, PostgreSQL sized to version storage (which grows with page count × capture frequency), Redis/Sidekiq workers, plus the diff service — realistically several VMs and meaningful storage for thousands of pages. Dominant cost is analyst time working the annotation queue. Assumptions: self-hosted, Wayback as version source.

## 11. Privacy and data flows

Page versions, diffs and analyst annotations are held in your own PostgreSQL database. EDGI's public instance is a separate deployment. Monitoring public government pages raises no subject-privacy issue; your watch list does reveal editorial priorities, so protect the instance accordingly.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [changedetection.io](SUR-B1-15.md) for a far lighter deployment below the triage threshold
- web-monitoring-diff alone if you have your own storage and only need diffs
- Klaxon for reporter-driven rather than analyst-driven monitoring

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/edgi-govdata-archiving/web-monitoring-db
- https://github.com/edgi-govdata-archiving/web-monitoring-db/blob/main/LICENSE

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

← 160. [stalkerware-indicators](SUR-B3-10.md) · 162. [httpx](OSINT-C3-24.md) →
