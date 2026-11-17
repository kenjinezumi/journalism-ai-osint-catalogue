# MobSF (Mobile Security Framework)

`SUR-B2-04` · **88/100** · overall rank 55 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 17) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 2) |
| **Subcategory** | Mobile app analysis |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Ajin Abraham and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MobSF/Mobile-Security-Framework-MobSF) · [Documentation](https://mobsf.github.io/docs/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 88/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Automated mobile application security framework performing static and dynamic analysis of Android, iOS and Windows apps, including code review, permission and API analysis, network traffic capture and malware checks.

## Journalism / investigative use case

The deep-analysis step when a story concerns a specific application: take the state-promoted contact-tracing app, the mandatory border app or a suspected stalkerware package and establish what it collects, which endpoints it contacts and what capabilities it holds — with dynamic analysis showing actual behaviour rather than declared permissions.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Static plus dynamic analysis in one framework is the right combination for app investigation: static finds capability, dynamic shows conduct, and a story needs both
- Covers iOS as well as Android, which closes the gap Exodus Privacy leaves
- Outstanding maintenance for a tool of this complexity: release v4.6.6 (2026-11-15), pushed 2026-11-17, and only 2 open issues against 22,249 stars — an exceptional triage record
- GPL-3.0 and self-hosted, so the app you are analysing and the fact you are analysing it stay private

## 5. Cons

- GPL-3.0 limits embedding in a proprietary newsroom product; immaterial for internal analysis but relevant if you build a service
- Dynamic analysis requires an emulator or a real device and a working intercept setup, which is a meaningful operational commitment and the part that most often fails
- Security-tooling orientation means output is dense and framed for penetration testers; translating it into a journalistic finding requires expertise
- Analysing an app may breach its terms of service and, in some jurisdictions, reverse-engineering restrictions — a legal question to settle before starting, not after

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 22,249 stars with just 2 open issues, release v4.6.6 (2026-11-15), pushed 2026-11-17, GPL-3.0. The issue-throughput ratio is among the best in the catalogue and is strong evidence of active, disciplined maintenance.

## 7. Assessment

Adopt where app investigation is a recurring need — the combination of maintenance quality, coverage and self-hosting makes it the strongest option in this subcategory. For your profile two practical points: get a legal view on reverse-engineering in your jurisdiction before you analyse a commercial or state app, and invest the setup time in dynamic analysis, because 'the app sent your location to this endpoint' is a far stronger published claim than 'the app requests location permission'.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v4.6.6 (2026-11-15), 22,249 stars, 2 open issues. Same-day commits, release within two days of the survey, near-zero backlog at very large scale.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Bundled signature and rule sets have their own sources.

**Restrictions:** GPL-3.0: distributing a modified version or a product incorporating it triggers source obligations. Internal use is unaffected.

**Licence evidence:** https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure: a workstation or VM for static analysis plus an emulator or test device for dynamic analysis. Analyst time dominates. Estimate.

## 11. Privacy and data flows

Entirely self-hosted, so neither the app binary nor your interest in it is disclosed to a third party — the key advantage over online app-scanning services.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Reverse-engineering an app may engage terms of service and local law — obtain a legal view first

## 13. Alternatives

- [Exodus Privacy](SUR-B2-01.md) for fast Android tracker identification without a full analysis
- [Apktool](SUR-B2-05.md) plus manual review for targeted reverse engineering
- [mitmproxy](SUR-B2-06.md) alone to observe app traffic without full static analysis

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/MobSF/Mobile-Security-Framework-MobSF
- https://mobsf.github.io/docs/
- https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |
| 9 | [Blacklight collector](SUR-B2-02.md) | 81 | Adopt |

---

← 54. [iLEAPP](SUR-B3-15.md) · 56. [MediaInfo](OSINT-C2-04.md) →
