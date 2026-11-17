# stalkerware-indicators

`SUR-B3-10` · **79/100** · overall rank 160 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 44) |
| **Segment** | B3 · Protecting journalists and sources (rank 26) |
| **Subcategory** | Threat indicators |
| **Type** | dataset |
| **Bucket** | `uncertain` |
| **Maintainer** | Association Échap (AssoEchap) |
| **Maintenance** | Actively maintained |
| **Licence** | NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found (2026-11-17) |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/AssoEchap/stalkerware-indicators) · [Documentation](https://github.com/AssoEchap/stalkerware-indicators#readme) |

**Scores** — relevance 5/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 2/5 → **weighted 79/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Curated indicator set for consumer stalkerware and monitoring apps — package names, certificates, network indicators and YARA rules — maintained for use with MVT and antivirus tooling.

## Journalism / investigative use case

Extends device checks beyond state-grade spyware to the commercial monitoring apps that are far more commonly used against journalists by employers, partners and local actors — a threat that MVT's mercenary-spyware indicators do not cover and that is statistically much more likely.

## 2. Audience

specialist investigator

## 3. Project type

dataset · bucket `uncertain`

## 4. Pros

- Covers the threat most likely to be present on a journalist's device: commercial stalkerware is cheap, widely sold and used against individuals, unlike Pegasus-class implants
- Designed to plug into MVT, so it extends an existing workflow rather than requiring a new one
- Maintained by an organisation focused on technology-facilitated abuse, with current updates (pushed 2026-11-02) and a focused community (401 stars)
- Includes network indicators and YARA rules as well as package names, so detection is multi-layered

## 5. Cons

- No licence detected by the GitHub API and none found in this survey — so redistribution and inclusion in a product are legally unresolved, which matters if you build internal tooling around it
- Indicator lists are inherently incomplete and lag new stalkerware; a clean result is weak evidence of absence
- No releases, so you track the default branch and cannot pin a verified indicator-set version — awkward for reproducible examinations
- Detecting stalkerware on a device raises immediate safety questions (the installer often has physical access to the person) that are outside the tool's scope but inside yours

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 401 stars with 10 open issues, no releases, no detected licence, last push 2026-11-02. Échap's focus on technology-facilitated abuse is documented by the organisation; the indicator set is referenced in the stalkerware-detection community.

## 7. Assessment

Use it alongside MVT — the coverage gap it fills is the one most likely to matter for an individual journalist. For your profile two points stand out. First, the unresolved licence means you should consume the indicators rather than redistribute them in a product, and ask Échap if you need clarity. Second, and more important: if a check finds stalkerware, the person's immediate physical safety may be at risk from whoever installed it, so have a safety plan and a referral route before you run the check, not after.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-02, no releases or tags, no detected licence, 401 stars, 10 open issues. Indicator updates within the last month from a focused organisation; maintenance assessed on update recency since indicator sets have no release cadence.

## 9. Licensing

**Licence:** NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found (2026-11-17) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same — this is an indicator dataset, not software.

**Restrictions:** Unresolved. Consuming the indicators for your own examinations is the low-risk use; redistributing them or embedding them in a distributed product is legally unclear. Clarify with the maintainer if needed.

**Licence evidence:** https://github.com/AssoEchap/stalkerware-indicators

## 10. Costs

No fee. Negligible — it is a data repository.

## 11. Privacy and data flows

Static indicator data; using it discloses nothing. The sensitivity lies in the examination it supports, not the dataset.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- No licence — redistribution legally unresolved

## 13. Alternatives

- Amnesty International's published indicators of compromise for mercenary spyware
- [Exodus Privacy](SUR-B2-01.md) for tracker analysis of installed Android apps
- Commercial anti-stalkerware products, which detect more but report to a vendor

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/AssoEchap/stalkerware-indicators

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

← 159. [wetterdienst](OSINT-C2-42.md) · 161. [EDGI web-monitoring-db](SUR-B1-20.md) →
