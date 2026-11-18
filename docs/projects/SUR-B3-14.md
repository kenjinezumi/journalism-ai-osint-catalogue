# libimobiledevice

`SUR-B3-14` · **81/100** · overall rank 141 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 39) |
| **Segment** | B3 · Protecting journalists and sources (rank 22) |
| **Subcategory** | Device forensics (iOS access) |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | libimobiledevice project |
| **Maintenance** | Actively maintained |
| **Licence** | LGPL-2.1 |
| **Licence type** | Weak copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/libimobiledevice/libimobiledevice) · [Documentation](https://libimobiledevice.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 81/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Weak copyleft |
| **Exact licence (as recorded)** | LGPL-2.1 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | LGPL-2.1 permits linking from your own tooling provided the library remains replaceable; modifications must be shared. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. A Linux forensic workstation and storage for backups (tens of GB per device). Build-from-source effort is the hidden cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/libimobiledevice/libimobiledevice/blob/master/COPYING.LESSER
- https://github.com/libimobiledevice/libimobiledevice
- https://libimobiledevice.org/

---

## 1. Purpose

Cross-platform protocol library and tools for communicating with iOS devices without jailbreaking — creating backups, reading device information, mounting filesystems and accessing diagnostic services.

## Journalism / investigative use case

The acquisition layer for iOS device checks on Linux: create the encrypted backup that MVT analyses, read device identifiers and diagnostics, and do it from a forensic workstation rather than requiring macOS and iTunes.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Enables iOS forensic acquisition on Linux, which is what makes a dedicated forensic workstation (rather than a journalist's Mac) practical — a meaningful operational-security improvement
- Reverse-engineered protocol implementation maintained over many years, with very active development (pushed 2026-11-17) and a large user base (8,352 stars)
- LGPL-2.1, so it can be linked from your own tooling without copyleft contamination
- Underpins MVT's iOS workflow, so it is a dependency you will have whether you install it deliberately or not

## 5. Cons

- 850 open issues — by far the largest backlog in this segment — reflecting the difficulty of tracking Apple's protocol changes across iOS versions
- Breakage after iOS releases is a recurring pattern: a new iOS version can render acquisition unreliable until the library catches up, which is exactly when you may need it
- Release cadence lags development (1.4.0 from 2025-10-10 against commits in November 2026), so you often need to build from source
- Low-level and engineer-facing; errors are cryptic and diagnosing a failed acquisition takes experience

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 8,352 stars with 850 open issues, release 1.4.0 (2025-10-10), pushed 2026-11-17, LGPL-2.1. The large backlog alongside daily commits is characteristic of a reverse-engineering project chasing a moving proprietary target.

## 7. Assessment

Adopt as infrastructure for iOS device checks, and plan around the iOS-version lag: keep a note of which library version successfully acquired from which iOS version, and expect to build from source after a major iOS release. For your profile the broader point is that iOS acquisition capability is a dependency on a volunteer reverse-engineering effort — worth supporting, and worth having a fallback (a macOS machine for backups) when a check cannot wait for the library to catch up.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 1.4.0 (2025-10-10), 8,352 stars, 850 open issues. Same-day commits with infrequent releases; the backlog is intrinsic to chasing Apple's undocumented protocols rather than evidence of neglect.

## 9. Licensing

**Licence:** LGPL-2.1 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** LGPL-2.1 permits linking from your own tooling provided the library remains replaceable; modifications must be shared.

**Licence evidence:** https://github.com/libimobiledevice/libimobiledevice/blob/master/COPYING.LESSER

## 10. Costs

No fee. A Linux forensic workstation and storage for backups (tens of GB per device). Build-from-source effort is the hidden cost.

## 11. Privacy and data flows

Entirely local device communication; nothing is transmitted. The backups it creates are extremely sensitive and should be encrypted at rest with a short retention period.

## 12. Verdict

**Integrate**

## 13. Alternatives

- macOS Finder/iTunes backups where a Mac is available and acceptable
- [iLEAPP](SUR-B3-15.md) for parsing the acquired data
- Commercial forensic suites (Cellebrite class) — avoid for journalist device checks: expensive, vendor-dependent and inappropriate for a consent-based protective examination

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/libimobiledevice/libimobiledevice
- https://libimobiledevice.org/
- https://github.com/libimobiledevice/libimobiledevice/blob/master/COPYING.LESSER

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

← 140. [ICIJ extract](JAI-A2-24.md) · 142. [Neo4j Community Edition](OSINT-C3-35.md) →
