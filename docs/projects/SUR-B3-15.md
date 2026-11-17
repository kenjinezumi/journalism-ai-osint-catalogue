# iLEAPP

`SUR-B3-15` · **88/100** · overall rank 54 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 16) |
| **Segment** | B3 · Protecting journalists and sources (rank 12) |
| **Subcategory** | Device forensics (iOS parsing) |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Alexis Brignoni (abrignoni) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/abrignoni/iLEAPP) · [Documentation](https://github.com/abrignoni/iLEAPP#readme) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 88/100**

---

## 1. Purpose

iOS Logs, Events And Plist Parser: processes iOS backups and filesystem extractions into readable reports covering app usage, locations, connections, notifications, installed applications and hundreds of other artefact types.

## Journalism / investigative use case

Going beyond spyware indicators to understand what actually happened on a device: when a journalist believes their phone was accessed at a border crossing, iLEAPP's artefact timeline — unlocks, connections, app launches, file access — is how you establish what was done and when.

## 2. Audience

specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Breadth of artefact coverage is the point: hundreds of parsers mean you can reconstruct device activity in detail rather than only checking for known malware, which is what a 'was my phone searched?' question requires
- MIT licensed and extremely actively maintained (v2026.4.6, 2026-11-03; pushed 2026-11-17) with a healthy tracker (48 open issues against 1,452 stars)
- Produces HTML and structured reports usable by a non-forensic colleague, which matters when explaining findings to a journalist or a lawyer
- Community-driven parser contributions mean coverage of new iOS artefacts appears quickly

## 5. Cons

- Interpretation is the hard part and the tool does not help with it: an artefact timeline is extremely easy to over-read, and attributing an event to a hostile actor rather than ordinary device behaviour requires real expertise
- Output volume is large — hundreds of artefact categories — so triage skill determines whether an examination is useful or just exhausting
- Designed for law-enforcement-style forensics, so the framing and defaults assume an investigative rather than protective context; the ethical posture is yours to supply
- Requires a prior acquisition (libimobiledevice or a macOS backup), so it is one stage of a chain

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,452 stars with 48 open issues, release v2026.4.6 (2026-11-03), pushed 2026-11-17, MIT licence. iLEAPP is widely used in the digital-forensics community, which is relevant adjacent credibility; its journalism use is not separately evidenced here.

## 7. Assessment

Adopt for the specific case where you need to know what happened on a device rather than merely whether known spyware is present — border searches, suspected physical access, device handover after detention. For your profile the limiting factor is expertise, not tooling: budget for forensic training or a relationship with a practitioner, because an over-read timeline presented to a frightened journalist does harm. Pair with MVT (indicators) and document consent as you would for MVT even though the licence does not require it.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v2026.4.6 (2026-11-03), 1,452 stars, 48 open issues. Same-day commits with date-versioned releases; a very active community-contributed parser ecosystem.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material — notably unrestricted compared with MVT in the same workflow.

**Licence evidence:** https://github.com/abrignoni/iLEAPP/blob/main/LICENSE

## 10. Costs

No fee. A forensic workstation and storage. The dominant cost is analyst expertise and time per examination. Estimate.

## 11. Privacy and data flows

Local processing of an acquired backup. The data is the most sensitive you will handle — full device activity history — so encryption at rest, minimal retention, documented disposal and restricted access are essential regardless of licence requirements.

## 12. Verdict

**Pilot**

## 13. Alternatives

- MVT for spyware-indicator checks specifically
- [ALEAPP](SUR-B3-16.md) for the Android equivalent
- A professional forensic practitioner where the stakes or the complexity are high

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/abrignoni/iLEAPP
- https://github.com/abrignoni/iLEAPP/blob/main/LICENSE

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

← 53. [yente](JAI-A2-61.md) · 55. [MobSF (Mobile Security Framework)](SUR-B2-04.md) →
