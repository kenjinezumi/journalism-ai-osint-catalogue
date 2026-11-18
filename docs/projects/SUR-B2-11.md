# Mihari

`SUR-B2-11` · **67/100** · overall rank 282 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 70) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 16) |
| **Subcategory** | Infrastructure monitoring and pivoting |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | ninoseki |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ninoseki/mihari) · [Documentation](https://github.com/ninoseki/mihari#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 2/5 · usability 3/5 · licence+cost 3/5 → **weighted 67/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Data comes from the configured commercial and public sources under their own terms, several of which restrict redistribution. |
| **Restrictions** | Permissive as published. The binding constraints are the scan vendors' API terms, which typically prohibit redistributing their data — relevant if you want to publish a dataset of findings. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | **Mandatory paid dependency** — mandatory paid dependency; self-hosted infrastructure |
| **Cost conditions** | **Mandatory paid dependency**; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Software free. Real cost is paid API subscriptions to scan databases (Shodan, Censys, FOFA and similar — prices not verified in this survey) plus a small VM. Budget the data, not the tool.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/ninoseki/mihari

---

## 1. Purpose

Framework for continuous threat-hunting that runs saved queries against many data sources (scan databases, certificate logs, passive DNS, URL scanners), deduplicates results into alerts and tracks artefacts over time.

## Journalism / investigative use case

Turning one-off infrastructure discovery into a standing watch: define queries describing a surveillance vendor's infrastructure patterns and have Mihari alert you when new matching hosts appear across several data sources — the difference between finding a vendor's servers once and tracking how its estate changes over a year.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Multi-source querying with deduplication is the right architecture for infrastructure monitoring, because no single scan database has adequate coverage and manually reconciling them is unsustainable
- Artefact tracking over time builds a longitudinal picture, which is what supports a story about how an operation grew or moved
- Self-hosted, so your queries and watchlists remain private — important when the watchlist is effectively a list of your investigative targets
- Alerting model fits a beat rather than a project: it keeps working while you do other things

## 5. Cons

- Depends on API keys for the underlying scan databases (Shodan, Censys and similar), several of which are paid — so the real cost is the data subscriptions, not the tool
- Your queries are sent to those commercial providers, which therefore learn your investigative targets — the same exposure as uncover, compounded by the fact that monitoring is continuous rather than one-off
- Security-operations orientation means the concepts (artefacts, alerts, enrichers) take orientation for a journalist, and the documentation assumes that background
- Small project relative to its ambition, so continuity depends on a single maintainer

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with an active development pattern. Mihari is known in the threat-intelligence community as a lightweight alternative to commercial hunting platforms, which is the relevant adjacent context.

## 7. Assessment

Worth piloting if surveillance-industry infrastructure is a sustained beat rather than an occasional story — the longitudinal tracking is what produces findings competitors do not have. For your profile the decisive considerations are budget and disclosure: paid scan-database subscriptions are the real cost, and continuous querying tells those vendors exactly who you are watching, so use accounts and egress that are not attributable to your newsroom and consider whether passive sources (certificate transparency, passive DNS) can carry more of the load.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with ongoing development from a single maintainer. Classified stable-low because the project is small and maintenance depends on one person, while the capability depends on external data sources rather than on code velocity.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Data comes from the configured commercial and public sources under their own terms, several of which restrict redistribution.

**Restrictions:** Permissive as published. The binding constraints are the scan vendors' API terms, which typically prohibit redistributing their data — relevant if you want to publish a dataset of findings.

**Licence evidence:** https://github.com/ninoseki/mihari

## 10. Costs

Software free. Real cost is paid API subscriptions to scan databases (Shodan, Censys, FOFA and similar — prices not verified in this survey) plus a small VM. Budget the data, not the tool.

## 11. Privacy and data flows

Self-hosting keeps the system private, but the queries themselves go to commercial providers who learn your continuous watchlist. This is the central trade-off and should drive your choice of data sources.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Continuous querying discloses your investigative watchlist to commercial scan vendors; several required APIs are paid

## 13. Alternatives

- [certstream-server](SUR-B2-10.md) plus your own filtering for a fully passive, no-disclosure watch
- [uncover](OSINT-C1-10.md) for one-off multi-database queries rather than continuous monitoring
- Commercial threat-intelligence platforms, which are more capable, expensive and equally disclosing

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/ninoseki/mihari

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |

---

← 281. [Awesome Website Change Monitoring](SUR-B1-24.md) · 283. [AnalyticsRelationships](SUR-B2-09.md) →
