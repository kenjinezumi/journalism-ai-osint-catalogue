# Andriller

`SUR-B3-17` · **51/100** · overall rank 344 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 78) |
| **Segment** | B3 · Protecting journalists and sources (rank 33) |
| **Subcategory** | Device forensics (Android) |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Denis Sazonov (den4uk) |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/den4uk/andriller) · [Documentation](https://github.com/den4uk/andriller#readme) |

**Scores** — relevance 2/5 · capability 2/5 · maintenance 1/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 51/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None, but the code is stale. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Not worth the deployment effort.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/den4uk/andriller/blob/master/LICENSE
- https://github.com/den4uk/andriller

---

## 1. Purpose

Collection of forensic tools for Android devices with a graphical interface, performing data extraction, lock-screen cracking for older devices and decoding of application databases into reports.

## Journalism / investigative use case

Historically a graphical alternative for Android extraction and app-database decoding, usable by someone without command-line forensics experience — relevant now mainly as a reference point when evaluating what a GUI-driven Android examination would look like.

## 2. Audience

specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Graphical interface lowered the barrier for Android examination relative to CLI tooling, which was its main contribution
- Application-database decoders covered messaging and social apps in a form directly useful to an investigator
- MIT licensed with a sizeable historical community (1,633 stars) and a clean issue tracker at the point it stopped

## 5. Cons

- DORMANT: last push 2022-06-27 and release 3.6.3 (2022-04-30) — over four years without activity, during which Android's security model, app database formats and ADB behaviour have all changed substantially
- Android forensics is the fastest-moving area in this segment, so a four-year-old tool's decoders are substantially obsolete
- Lock-screen cracking features target old Android versions and are irrelevant to current devices, while potentially raising legal questions about use
- Unmaintained security-adjacent software on a forensic workstation is itself a risk

## 6. Feedback (documented)

No individual user reports verified. Documented: 1,633 stars with 13 open issues, release 3.6.3 (2022-04-30), last push 2022-06-27, MIT licence. The four-year gap is decisive given the pace of change in Android internals.

## 7. Assessment

Avoid for new deployment — ALEAPP plus androidqf covers the same ground with current parsers and active maintenance. The reason to keep it in the catalogue is that it still appears in digital-forensics tool lists and training material, and anyone following those recommendations should know it has not been maintained since 2022. If a GUI is genuinely required for your analysts, Autopsy is the maintained option.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2022-06-27, latest release 3.6.3 (2022-04-30), 1,633 stars, 13 open issues. Over four years inactive in the fastest-changing area of mobile forensics.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None, but the code is stale.

**Licence evidence:** https://github.com/den4uk/andriller/blob/master/LICENSE

## 10. Costs

No fee. Not worth the deployment effort.

## 11. Privacy and data flows

Local processing. Running unmaintained forensic software on a workstation handling sensitive device data is itself a security consideration.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Dormant since 2022; Android internals have changed substantially since

## 13. Alternatives

- [ALEAPP](SUR-B3-16.md) — recommended: current Android artefact parsing, actively maintained
- [androidqf](SUR-B3-09.md) for acquisition
- [Autopsy](SUR-B3-18.md) where a graphical forensic platform is required

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/den4uk/andriller
- https://github.com/den4uk/andriller/blob/master/LICENSE

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

← 343. [SelfBlendedImages (SBI)](JAI-A4-27.md) · 345. [diffengine](SUR-B1-25.md) →
