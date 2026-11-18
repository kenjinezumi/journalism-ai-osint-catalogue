# AnalyticsRelationships

`SUR-B2-09` · **67/100** · overall rank 283 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 71) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 17) |
| **Subcategory** | Infrastructure attribution |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Josué Encinar (Josue87) |
| **Maintenance** | Uncertain |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Josue87/AnalyticsRelationships) · [Documentation](https://github.com/Josue87/AnalyticsRelationships#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 2/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 67/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a. Third-party reverse-analytics services have their own terms. |
| **Restrictions** | Permissive as published; the operative constraints are the third-party services' terms of use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** No fee. Negligible compute. The third-party services it queries may have rate limits or paid tiers (not verified in this survey).

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Josue87/AnalyticsRelationships

---

## 1. Purpose

Tool that extracts analytics identifiers (Google Analytics, Tag Manager and similar) from a website and searches for other domains using the same identifier, revealing sites under common management.

## Journalism / investigative use case

One of the most productive attribution techniques in disinformation and front-company investigation: a network of ostensibly unrelated news sites sharing a single Google Analytics property is strong evidence of common operation, and this automates finding that overlap.

## 2. Audience

specialist investigator, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Shared analytics identifiers are among the strongest technical links between websites, because they imply shared administrative access rather than merely similar technology — materially better evidence than a shared CDN or framework
- Automates a technique that is otherwise manual and tedious, which is what makes it usable across a list of suspected sites
- Small, readable tool that can be adapted, with no infrastructure requirement
- Directly serves the B2 purpose: mapping which entities operate which online properties

## 5. Cons

- Depends on third-party reverse-analytics search services whose coverage, availability and terms are outside your control — the capability can degrade without warning
- Shared identifiers can also result from a shared web developer or agency rather than common ownership, so the finding needs corroboration before it becomes an attribution in print
- Small project with a modest community, so maintenance and continuity are uncertain and you may end up owning it
- Queries disclose the domains you are investigating to the reverse-analytics services used

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with a small community. The underlying technique is well established in published open-source investigations into website networks, which is the relevant evidence that it works.

## 7. Assessment

Adopt the technique, and use this tool as the convenient implementation while remaining ready to do it by hand. For your profile the methodological discipline is what matters: a shared analytics ID is a hypothesis of common operation, and before publishing you want a second independent link (registration data, certificate overlap, shared hosting, content reuse) plus an explanation of why a shared agency is not the simpler explanation.

## 8. Maintenance

**Uncertain** — Verified via the GitHub API 2026-11-17 as live and non-archived, but with a small community and no substantial release cadence. Because the capability depends on third-party reverse-analytics services rather than on the code, repository activity is a weak indicator of whether the tool still works — classified Uncertain for that reason rather than inferring health from either direction.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Third-party reverse-analytics services have their own terms.

**Restrictions:** Permissive as published; the operative constraints are the third-party services' terms of use.

**Licence evidence:** https://github.com/Josue87/AnalyticsRelationships

## 10. Costs

No fee. Negligible compute. The third-party services it queries may have rate limits or paid tiers (not verified in this survey).

## 11. Privacy and data flows

Queries disclose the domains under investigation to the reverse-analytics services. Use a dedicated egress for sensitive attribution work.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Depends on third-party reverse-analytics services whose availability and terms are outside your control

## 13. Alternatives

- Manual extraction of analytics identifiers plus a reverse-lookup service, which is the same technique without a dependency
- Certificate-transparency overlap (certstream, crt.sh) for an attribution signal that leaves no trace with third parties
- DNS and WHOIS history for registration-based attribution

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/Josue87/AnalyticsRelationships

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

← 282. [Mihari](SUR-B2-11.md) · 284. [Hierarchical-Localization (hloc)](OSINT-C2-35.md) →
