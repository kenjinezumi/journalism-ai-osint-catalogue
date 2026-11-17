# Amnesty International investigations (indicators of compromise)

`SUR-B3-11` · **76/100** · overall rank 196 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 52) |
| **Segment** | B3 · Protecting journalists and sources (rank 28) |
| **Subcategory** | Threat indicators |
| **Type** | dataset |
| **Bucket** | `uncertain` |
| **Maintainer** | Amnesty International Security Lab (AmnestyTech) |
| **Maintenance** | Stable with low activity |
| **Licence** | NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found (2026-11-17) |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/AmnestyTech/investigations) · [Documentation](https://securitylab.amnesty.org/) |

**Scores** — relevance 5/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 2/5 → **weighted 76/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Repository of indicators of compromise published alongside Amnesty's technical investigations into mercenary spyware and targeted surveillance of civil society.

## Journalism / investigative use case

The authoritative indicator source for MVT checks: when Amnesty publishes an investigation into a new spyware campaign targeting journalists, the IOCs land here and can be fed directly into a device examination — which is how a newsroom keeps its device checks current rather than relying on last year's indicators.

## 2. Audience

specialist investigator

## 3. Project type

dataset · bucket `uncertain`

## 4. Pros

- Authoritative provenance: these are the indicators from the investigations that publicly established spyware targeting of journalists, published by the organisation that did the forensic work
- Designed to be consumed by MVT, so updating your detection capability is a matter of pulling new indicator files
- Each indicator set is tied to a published investigation, so you can read the methodology behind the detection rather than trusting an opaque list
- Public and free, which matters because commercial threat intelligence covering the same ground is expensive and not citable

## 5. Cons

- No licence detected in this survey, so redistribution terms are unresolved — a recurring problem with indicator repositories and a real constraint if you build tooling
- Last push 2024-12-16: the repository is a publication archive rather than a continuously updated feed, so it is not a live indicator source and newer campaigns may be published elsewhere (for example in Security Lab reports directly)
- Indicator-based detection only finds known campaigns; the absence of a match says nothing about a novel implant
- No releases or versioning, so pinning an indicator-set state for a reproducible examination requires recording a commit hash yourself

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,733 stars with 6 open issues, no releases, no detected licence, last push 2024-12-16. Amnesty Security Lab's investigations are extensively documented publicly and are the basis of several confirmed cases of journalist targeting.

## 7. Assessment

Essential as a reference and insufficient as your only indicator source, precisely because the repository has not been pushed in nearly two years — check securitylab.amnesty.org directly for newer publications rather than assuming this mirror is current. For your profile the practical arrangement is to pull indicators from here plus stalkerware-indicators, record the commit hashes used in each examination, and maintain a relationship with Amnesty Security Lab or Access Now for cases beyond your capacity, since they see campaigns before indicators are public.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2024-12-16, no releases, no detected licence, 1,733 stars, 6 open issues. Nearly two years since the last push. Classified stable-low rather than dormant because it is a publication archive tied to reports rather than a maintained feed — but it should not be treated as current indicator intelligence.

## 9. Licensing

**Licence:** NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found (2026-11-17) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same — indicator data accompanying published research.

**Restrictions:** Unresolved. Consuming indicators for your own examinations is low risk; redistribution is unclear. Amnesty's published reports have their own terms.

**Licence evidence:** https://github.com/AmnestyTech/investigations

## 10. Costs

No fee. Negligible.

## 11. Privacy and data flows

Static data; consuming it discloses nothing (note that cloning from GitHub is visible to GitHub, which is unremarkable).

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- No licence; repository not pushed since December 2024 — do not treat as a live indicator feed

## 13. Alternatives

- securitylab.amnesty.org directly for the most current publications
- [stalkerware-indicators](SUR-B3-10.md) for consumer monitoring apps
- Citizen Lab publications for additional campaign documentation

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/AmnestyTech/investigations
- https://securitylab.amnesty.org/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |

---

← 195. [tippecanoe](JAI-A1-23.md) · 197. [Censored Planet data analysis pipeline](SUR-B1-09.md) →
