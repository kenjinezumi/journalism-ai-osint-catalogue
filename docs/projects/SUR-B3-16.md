# ALEAPP

`SUR-B3-16` · **84/100** · overall rank 106 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 32) |
| **Segment** | B3 · Protecting journalists and sources (rank 20) |
| **Subcategory** | Device forensics (Android parsing) |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Alexis Brignoni (abrignoni) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/abrignoni/ALEAPP) · [Documentation](https://github.com/abrignoni/ALEAPP#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 84/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Workstation and storage; analyst time dominates. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/abrignoni/ALEAPP/blob/main/LICENSE
- https://github.com/abrignoni/ALEAPP

---

## 1. Purpose

Android Logs Events And Protobuf Parser: processes Android extractions into readable reports across app usage, locations, accounts, connections, notifications and many other artefact types.

## Journalism / investigative use case

The Android counterpart for understanding device activity after a suspected search, seizure or unauthorised access — reconstructing what applications ran, what accounts were present and what connections were made, from an androidqf or filesystem extraction.

## 2. Audience

specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Fills the Android gap that matters because Android is the dominant platform for journalists in much of the world, where iOS-centric tooling leaves them unserved
- MIT licensed with very active maintenance (v2026.4.5, 2026-11-03; pushed 2026-11-17) and a healthy tracker (37 open issues)
- Same reporting model as iLEAPP, so an analyst learns one workflow for both platforms
- Community parser contributions keep pace with Android's rapid artefact changes

## 5. Cons

- Android artefact availability depends heavily on what the acquisition captured, which without root is substantially less than an iOS backup — so reports are thinner and gaps are common
- Android fragmentation across vendors and versions means parser coverage is uneven: a Chinese-market device may yield far less than a Pixel
- Same interpretation risk as iLEAPP, amplified by sparser data — fewer artefacts make over-reading more likely
- Requires a prior acquisition step and forensic literacy; not usable by a journalist directly

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,052 stars with 37 open issues, release v2026.4.5 (2026-11-03), pushed 2026-11-17, MIT licence. Widely used in the digital-forensics community alongside iLEAPP.

## 7. Assessment

Adopt alongside androidqf for Android cases, with realistic expectations: the examination will be shallower than an iOS one and you should say so when reporting a result. For your profile the honest framing for Android users is that protective examination is less capable on their platform, which should influence advice — a journalist at high risk may be better served by a well-configured iPhone or GrapheneOS device than by a stock Android phone you can only partially examine.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v2026.4.5 (2026-11-03), 1,052 stars, 37 open issues. Same-day commits with date-versioned releases from an active maintainer and contributor community.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/abrignoni/ALEAPP/blob/main/LICENSE

## 10. Costs

No fee. Workstation and storage; analyst time dominates. Estimate.

## 11. Privacy and data flows

Local processing of acquired data, which is highly sensitive personal information requiring encrypted storage, minimal retention and documented disposal.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [androidqf](SUR-B3-09.md) plus MVT for indicator-focused checks
- [iLEAPP](SUR-B3-15.md) for the iOS equivalent
- [Autopsy](SUR-B3-18.md) for a broader forensic platform with a graphical interface

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/abrignoni/ALEAPP
- https://github.com/abrignoni/ALEAPP/blob/main/LICENSE

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

← 105. [Nextcloud](SUR-B3-28.md) · 107. [Nominatim](OSINT-C2-28.md) →
