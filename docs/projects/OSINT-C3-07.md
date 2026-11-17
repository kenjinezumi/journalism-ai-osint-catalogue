# Ushahidi Platform

`OSINT-C3-07` · **75/100** · overall rank 206 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 66) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 17) |
| **Subcategory** | Crowdsourced incident mapping |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Ushahidi |
| **Maintenance** | Stable with low activity |
| **Licence** | AGPL-3.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ushahidi/platform) · [Documentation](https://docs.ushahidi.com/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Platform for collecting, verifying and mapping crowdsourced reports from SMS, email, web forms and social media, with workflow for review and categorisation and a map-based public view.

## Journalism / investigative use case

Running a public reporting channel around an unfolding event: election irregularities, protest incidents, service failures — collected from the public via multiple channels, triaged by a desk, and mapped. It is the established tool for turning distributed observation into a reviewable dataset.

## 2. Audience

newsroom analyst, journalist, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Multi-channel intake including SMS is the distinguishing capability and matters enormously where smartphone penetration or connectivity is limited — a reporting channel that works on a feature phone
- Built-in verification workflow means crowdsourced reports are triaged rather than published raw, which is the difference between journalism and a rumour map
- Long institutional history with deployments across many elections and crises, so the model is proven and the pitfalls are documented
- Open source and self-hostable, so reports and reporter identities stay under your control

## 5. Cons

- Crowdsourced reports are unverified by nature, and the platform's map view makes them look authoritative — the editorial discipline around publication matters more than the software, and this is where deployments fail
- Operational commitment: a PHP/API platform plus SMS gateway integration, and the SMS channel in particular has real per-message costs and telecom relationships
- Submitter safety is a serious consideration: a public reporting channel in a repressive environment collects identifying information about people reporting on their government, and that database becomes a target
- Development pace has moderated relative to the platform's peak years, so check liveness before a time-critical deployment

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under Ushahidi's maintenance. The platform's election and crisis deployments are extensively documented publicly, which is strong evidence that the model works at scale.

## 7. Assessment

Pilot it for a defined event where public reporting adds something a newsroom cannot gather itself — elections are the canonical case. For your profile the two decisions that matter are editorial and security, not technical: publish only triaged reports and label verification status visibly, and treat the submitter database as source material requiring the same protection, because in a repressive context a list of people who reported on the state is exactly what an adversary wants. Budget SMS costs explicitly.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived under Ushahidi's institutional maintenance, with moderated development activity compared with the platform's earlier years. Classified stable-low: a mature platform with continuing institutional backing rather than active feature development.

## 9. Licensing

**Licence:** AGPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Submitted reports are user-contributed content whose handling is your responsibility as data controller.

**Restrictions:** AGPL-family copyleft would apply to a modified hosted instance. The weightier obligations are data-protection ones arising from collecting reports from identifiable members of the public.

**Licence evidence:** https://github.com/ushahidi/platform

## 10. Costs

No software fee. Infrastructure plus — significantly — SMS gateway costs, which are per-message and can be substantial at scale during an event (rates vary by country and provider; not priced here). Staff cost for triage is the other major item. Estimate.

## 11. Privacy and data flows

Self-hosting keeps reports and submitter details under your control, which is essential. The database is highly sensitive: it identifies people who reported on events, often adversely to their government, and should be treated with source-protection discipline including minimal retention.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Submitter database is a high-value target in repressive environments; SMS channel has real per-message costs

## 13. Alternatives

- A simple form plus a spreadsheet for a small, short event
- [Tella](OSINT-C3-06.md) for documentation by trained contributors rather than open crowdsourcing
- [Atlos](OSINT-C2-36.md) for verification workflow over media rather than open report intake

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/ushahidi/platform
- https://docs.ushahidi.com/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 205. [uncover](OSINT-C1-10.md) · 207. [Citizen Lab URL test lists](SUR-B1-06.md) →
