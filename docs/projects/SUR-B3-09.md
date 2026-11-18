# androidqf

`SUR-B3-09` · **85/100** · overall rank 83 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 27) |
| **Segment** | B3 · Protecting journalists and sources (rank 17) |
| **Subcategory** | Device forensics |
| **Type** | cli |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | MVT Project |
| **Maintenance** | Actively maintained |
| **Licence** | MVT License 1.1 — NOT OSI-approved, with the same §3.0 Consensual Use Restriction as MVT; GitHub reports NOASSERTION |
| **Licence type** | Restricted / non-OSI |
| **Open-source status** | Source available |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mvt-project/androidqf) · [Documentation](https://github.com/mvt-project/androidqf#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 3/5 → **weighted 85/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Restricted / non-OSI |
| **Exact licence (as recorded)** | MVT License 1.1 — NOT OSI-approved, with the same §3.0 Consensual Use Restriction as MVT; GitHub reports NOASSERTION |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a |
| **Restrictions** | Identical to MVT: explicit, uncoerced, fully informed consent from the Data Owner, including disclosure of privacy implications and the data retention and disposal policy. Non-consensual acquisition is prohibited. |
| **Open-source status** | **Source available** — Source published under a restricted, non-OSI licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. ADB-capable workstation and storage for collected artefacts. Analyst time dominates. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/mvt-project/androidqf/blob/main/LICENSE
- `../sources/evidence/leads.md`
- `../sources/recovered/cat/ground_truth.tsv`

---

## 1. Purpose

Android Quick Forensics: a cross-platform tool that rapidly collects a standard set of forensic artefacts from an Android device over ADB — installed packages, processes, settings, logs and selected files — for later analysis.

## Journalism / investigative use case

The acquisition step for Android device checks: collect a consistent artefact set from a journalist's or source's phone in minutes, then analyse it with MVT. Android acquisition is otherwise ad hoc, and consistency is what makes results comparable across devices and over time.

## 2. Audience

specialist investigator, engineer

## 3. Project type

cli · bucket `source-available-restricted`

## 4. Pros

- Standardised collection makes Android checks repeatable and comparable, which matters when you examine many devices or re-examine one over time
- Fast and field-practical: a single binary over ADB, no jailbreak or root required for the standard artefact set
- Same licence family and project as MVT, so acquisition and analysis are designed together
- Maintained (v1.8.3, 2026-05-12; pushed 2026-11-07) with a small backlog (18 open issues)

## 5. Cons

- Same MVT License 1.1 consensual-use restriction as MVT, verified from the licence blob — informed consent and retention disclosure are contractual obligations, and the licence is not OSI-approved
- Android's model limits what is collectable without root, so the artefact set is shallower than an iOS backup — meaning a sophisticated implant is more likely to be missed on Android than on iOS
- Release cadence is slower than MVT's (v1.8.3 from May 2026 against MVT's November release), so pairing versions needs attention
- Small community (387 stars); interpreting collected artefacts still requires MVT plus forensic literacy

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 387 stars with 18 open issues, release v1.8.3 (2026-05-12), pushed 2026-11-07, MVT License 1.1 (same licence blob text as MVT, read 2026-11-17 and recorded in leads.md L1). Session 1's ground_truth.tsv independently recorded the same licence and release.

## 7. Assessment

Adopt it as the Android acquisition step whenever you run device checks — the consistency is worth it and there is no better open option. For your profile, carry the same consent process as MVT (the licence requires it identically) and be explicit with Android users that the check is shallower than an iPhone check, because that honesty matters when you report a clean result. Where the stakes are high, escalate Android cases to a specialist lab rather than relying on a quick collection.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-07, latest release v1.8.3 (2026-05-12), 387 stars, 18 open issues. Current commits with a six-month-old release; maintained in step with MVT but at a slower release cadence.

## 9. Licensing

**Licence:** MVT License 1.1 — NOT OSI-approved, with the same §3.0 Consensual Use Restriction as MVT; GitHub reports NOASSERTION _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Identical to MVT: explicit, uncoerced, fully informed consent from the Data Owner, including disclosure of privacy implications and the data retention and disposal policy. Non-consensual acquisition is prohibited.

**Licence evidence:** https://github.com/mvt-project/androidqf/blob/main/LICENSE

## 10. Costs

No fee. ADB-capable workstation and storage for collected artefacts. Analyst time dominates. Estimate.

## 11. Privacy and data flows

Local collection and storage. The collected set is sensitive personal data about the device owner, so encrypted storage, short retention and documented disposal are required — contractually as well as ethically under this licence.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- MVT License 1.1 §3.0 consensual-use restriction; not OSI-approved

## 13. Alternatives

- [ALEAPP](SUR-B3-16.md) for deeper parsing of collected Android artefacts
- MVT for the indicator analysis this feeds
- A specialist forensic lab for high-stakes Android cases

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/mvt-project/androidqf/blob/main/LICENSE
- `../sources/evidence/leads.md`
- `../sources/recovered/cat/ground_truth.tsv`

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

← 82. [adsb-history](OSINT-C2-48.md) · 84. [OONI Probe Multiplatform](SUR-B1-02.md) →
