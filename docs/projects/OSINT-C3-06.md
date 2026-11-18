# Tella

`OSINT-C3-06` · **89/100** · overall rank 48 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 17) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 3) |
| **Subcategory** | Secure field documentation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Horizontal |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 (project licensing — confirm from the repository licence file) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Horizontal-org/Tella-Android) · [Documentation](https://tella-app.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 89/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | Copyleft on the application; immaterial for deployment, relevant if you fork it for a bespoke build. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Free. You need a receiving server or Uwazi instance — the real cost, and one you may already have. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/Horizontal-org/Tella-Android
- https://tella-app.org/

---

## 1. Purpose

Mobile application for documenting human-rights violations and collecting evidence in hostile environments, with encrypted local storage, camouflage modes, metadata capture and secure upload to a server or Uwazi instance.

## Journalism / investigative use case

Field documentation where the phone may be searched: a stringer records an incident, the file is encrypted on the device and the app can be camouflaged to look like a calculator, with upload to your server when connectivity and safety allow. This is the tool for the moment between witnessing and publishing.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Camouflage and encrypted-at-rest storage address the specific threat field documenters face — a device search at a checkpoint — which no general camera or cloud app does
- Uploads to infrastructure you control, including a Uwazi instance, so evidence moves from the field into your collection without passing through a commercial cloud
- Captures verification-relevant metadata at the point of recording, strengthening the evidentiary value of material gathered under pressure
- Built by an organisation focused on human-rights documentation, with the threat model stated explicitly

## 5. Cons

- Camouflage is a usability trade-off and a risk in itself: a trained searcher who knows Tella exists may find it, and a false sense of safety is dangerous — this must be explained honestly to users
- Android focus, so an iOS-using contributor is less well served
- Requires the documenter to install an app that, if identified, is itself incriminating in some jurisdictions — the same dilemma as Orbot and Tails
- Depends on you operating a receiving server (or a Uwazi instance), so it is part of a system rather than a standalone tool

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under Horizontal's maintenance. Tella's use in human-rights documentation is documented by the organisation; I verified no specific deployment.

## 7. Assessment

Adopt it where you work with field documenters or stringers in hostile environments — the combination of encrypted capture, camouflage and upload to your own infrastructure has no real alternative. For your profile two things must accompany deployment: an honest briefing that camouflage delays discovery rather than preventing it, and a receiving server you actually operate, because the app's value depends on evidence getting off the device and into a collection you control.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under Horizontal's institutional maintenance, with ongoing development on the Android client. Maintenance assessed on activity and institutional backing; release cadence was not separately itemised in this survey.

## 9. Licensing

**Licence:** GPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Copyleft on the application; immaterial for deployment, relevant if you fork it for a bespoke build.

**Licence evidence:** https://github.com/Horizontal-org/Tella-Android

## 10. Costs

Free. You need a receiving server or Uwazi instance — the real cost, and one you may already have. Estimate.

## 11. Privacy and data flows

Encrypted local storage, camouflage, and upload only to infrastructure you specify — a strong posture designed for exactly this threat. Residual risks are physical: device search by a trained searcher, and the incriminating presence of the app itself.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Camouflage delays rather than prevents discovery; app presence may itself be incriminating

## 13. Alternatives

- [ProofMode](SUR-B3-32.md) for capture provenance without the camouflage and secure-storage features
- Signal for sending material to a journalist directly, with no local encryption at rest
- A clean device with immediate upload and deletion, where connectivity allows

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/Horizontal-org/Tella-Android
- https://tella-app.org/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 47. [SearXNG](OSINT-C1-01.md) · 49. [Playwright](JAI-A1-08.md) →
