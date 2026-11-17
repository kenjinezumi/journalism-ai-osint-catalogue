# Molly

`SUR-B3-24` · **80/100** · overall rank 151 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 41) |
| **Segment** | B3 · Protecting journalists and sources (rank 24) |
| **Subcategory** | Secure communications |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Molly project (mollyim) |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mollyim/mollyim-android) · [Documentation](https://molly.im/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 80/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Hardened fork of Signal for Android that adds database encryption at rest with a separate passphrase, automatic locking, memory wiping, and a build free of proprietary Google dependencies.

## Journalism / investigative use case

Signal for a journalist whose device may be seized: Molly encrypts the local message database behind a passphrase and locks automatically, so a seized or borrowed phone does not immediately surrender the message history that standard Signal keeps accessible once the device is unlocked.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Addresses the specific gap that matters most in device seizure: standard Signal's local database is protected only by device encryption, so an unlocked phone exposes the history, while Molly requires a separate passphrase
- A Google-free build (Molly-FOSS) matters for de-Googled and GrapheneOS devices, which is the configuration many high-risk journalists use
- AGPL-3.0, actively maintained (pushed 2026-11-16) with a substantial community (3,838 stars) and builds tracking upstream Signal releases
- Keeps Signal protocol compatibility, so contacts need not change anything

## 5. Cons

- A third-party fork of a security-critical application: you are trusting the Molly maintainers' build and patches in addition to Signal's, which is a genuine supply-chain consideration for the most sensitive use
- Running a modified client against Signal's servers is contrary to the service's terms, so there is a (small, historically untested) risk of access disruption
- Release cadence trails upstream Signal (v8.19.2-4 from 2026-07-31 against Signal's November release), meaning a period without upstream security fixes after each Signal update
- Android only; iOS users have no equivalent, so a mixed-device team cannot standardise on it

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,838 stars, release v8.19.2-4 (2026-07-31), pushed 2026-11-16, AGPL-3.0. The release-version gap against upstream Signal (8.19 versus 8.35) is visible in the API data and is the key operational caveat.

## 7. Assessment

Recommend it selectively — for journalists at genuine risk of device seizure, on Android, who will manage a second passphrase. The at-rest protection is a real improvement over standard Signal for that threat. But the trailing release cadence is a serious counter-consideration: a fork that is sixteen minor versions behind upstream may lack recent security fixes, so check the current gap before deploying and re-check periodically. For most users, standard Signal plus disappearing messages plus strong device encryption is the better trade.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v8.19.2-4 (2026-07-31), 3,838 stars, AGPL-3.0. Commits are current but the published release trails upstream Signal (v8.35.2) by a substantial margin — activity is clear, release timeliness is the concern.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0. Separately, Signal's terms of service address use of modified clients against its servers — a service-terms rather than licence question.

**Licence evidence:** https://github.com/mollyim/mollyim-android/blob/main/LICENSE

## 10. Costs

Free. No infrastructure. Cost is the user managing an additional passphrase and the administrator tracking the upstream version gap.

## 11. Privacy and data flows

Improves on Signal specifically at rest (encrypted local database, auto-lock, memory wiping). In transit it is Signal, with the same phone-number disclosure. The Google-free build removes a dependency on proprietary services.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Release cadence trails upstream Signal — verify the current version gap before deploying

## 13. Alternatives

- Standard Signal with disappearing messages and strong device encryption for most users
- [SimpleX Chat](SUR-B3-25.md) where identifier-free contact is the requirement
- GrapheneOS plus standard Signal for a hardened device rather than a hardened client

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/mollyim/mollyim-android
- https://molly.im/
- https://github.com/mollyim/mollyim-android/blob/main/LICENSE

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

← 150. [Meedan Check](JAI-A4-01.md) · 152. [Presidio](JAI-A2-40.md) →
