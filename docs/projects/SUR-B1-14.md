# Internet Society Pulse

`SUR-B1-14` · **62/100** · overall rank 311 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 75) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 24) |
| **Subcategory** | Shutdown reporting dashboard |
| **Type** | platform |
| **Bucket** | `proprietary-service` |
| **Maintainer** | Internet Society |
| **Maintenance** | Uncertain |
| **Licence** | Not verified — dashboard code is not public; the public pulse-data repository carries no licence file |
| **Licence type** | Proprietary |
| **Open-source status** | Proprietary |
| **Software price** | **No software fee** |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/InternetSociety/pulse-data) · [Documentation](https://pulse.internetsociety.org/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 4/5 · usability 5/5 · licence+cost 2/5 → **weighted 62/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Proprietary |
| **Exact licence (as recorded)** | Not verified — dashboard code is not public; the public pulse-data repository carries no licence file |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Upstream measurement providers' terms apply to the underlying data; Pulse's own presentation terms were not verified in this survey. |
| **Restrictions** | Unverified. Do not assume figures may be redistributed as a dataset; cite and link rather than republish. |
| **Open-source status** | **Proprietary** — Hosted service or proprietary software — governed by service terms, not a software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** Free to use. No infrastructure. Not self-hostable.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/InternetSociety/pulse-data
- https://pulse.internetsociety.org/

---

## 1. Purpose

Hosted dashboard aggregating third-party measurement sources into country-level views of internet shutdowns, resilience, enabling technologies and market concentration, with a shutdown timeline.

## Journalism / investigative use case

A no-code entry point for a reporter who needs a credible country shutdown timeline and citable summary figures in minutes, without running or interpreting raw measurements — the fastest route to a defensible number for a deadline piece.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

platform · bucket `proprietary-service`

## 4. Pros

- Fastest path from question to citable figure for a non-technical reporter, with an institutional name (Internet Society) behind the attribution
- The shutdown timeline is curated, so it provides context and precedent that raw measurement data does not
- Draws on multiple upstream measurement providers (OONI, IODA, M-Lab and others), so figures are not single-source

## 5. Cons

- Classified adjacent rather than open source: the dashboard's code is not public and the one public repository (pulse-data) carries no licence, with 0 stars and 0 open issues — so reuse terms are unverified and self-hosting is impossible
- Figures are derived from other people's measurements, so you are citing a secondary source — for a contested claim you should go to the primary data (OONI, IODA) and cite that instead
- No API-level guarantees or published methodology depth comparable to the primary projects, so reproducing a figure can be difficult
- Dependency risk: a hosted dashboard can change its methodology or disappear, and your published figure cannot then be reproduced

## 6. Feedback (documented)

No individual user reports verified. Documented: the public pulse-data repository has no licence, 0 stars and 0 open issues, and the dashboard code is not published — verified via the GitHub API on 2026-11-17. The dashboard itself is live and maintained by the Internet Society.

## 7. Assessment

Use it as a starting point and a sanity check, not as your citation. For your profile the right habit is to find the figure on Pulse, then trace it back to OONI or IODA and cite the primary measurement with a permalink — that way the claim survives both official denial and the dashboard changing. Reserve direct Pulse citation for context and precedent rather than for the central factual claim of a story.

## 8. Maintenance

**Uncertain** — GitHub API 2026-11-17: InternetSociety/pulse-data archived=false, pushed_at 2026-09-19, no releases, no detected licence, 0 stars, 0 open issues. The dashboard is live but its code is not public, so repository-based maintenance assessment is not possible. Classified Uncertain deliberately rather than assuming continuity from the organisation's reputation.

## 9. Licensing

**Licence:** Not verified — dashboard code is not public; the public pulse-data repository carries no licence file _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Upstream measurement providers' terms apply to the underlying data; Pulse's own presentation terms were not verified in this survey.

**Restrictions:** Unverified. Do not assume figures may be redistributed as a dataset; cite and link rather than republish.

**Licence evidence:** https://github.com/InternetSociety/pulse-data

## 10. Costs

Free to use. No infrastructure. Not self-hostable.

## 11. Privacy and data flows

Presents aggregated public measurement data; visiting the dashboard sends no measurement traffic of your own. Ordinary web-analytics exposure applies.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Code not public and public repository unlicensed — reuse terms unverified, not self-hostable

## 13. Alternatives

- [OONI Explorer](SUR-B1-03.md) and IODA for primary, citable measurements
- Access Now's shutdown tracking for advocacy-grade timelines with their own terms
- Internet Health Report for structural dependency context

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `docs-reviewed`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/InternetSociety/pulse-data
- https://pulse.internetsociety.org/

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

← 310. [DataIndex.us (Federal Data Terminations Tracker)](SUR-B1-27.md) · 312. [mapillary_tools](OSINT-C2-31.md) →
