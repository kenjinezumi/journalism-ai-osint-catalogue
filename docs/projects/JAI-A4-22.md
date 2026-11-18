# Noiseprint

`JAI-A4-22` · **46/100** · overall rank 350 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 137) |
| **Segment** | A4 · Fact-checking support and media verification (rank 24) |
| **Subcategory** | Camera fingerprint forensics |
| **Type** | model |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | GRIP-UNINA (University of Naples Federico II) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | NOT OSS — custom GRIP-UNINA terms: LICENSE.txt restricts use to informational and non-profit purposes |
| **Licence type** | Restricted / non-OSI |
| **Open-source status** | Source available |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/grip-unina/noiseprint) · [Documentation](https://grip-unina.github.io/noiseprint/) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 2/5 · privacy 4/5 · usability 1/5 · licence+cost 1/5 → **weighted 46/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Restricted / non-OSI |
| **Exact licence (as recorded)** | NOT OSS — custom GRIP-UNINA terms: LICENSE.txt restricts use to informational and non-profit purposes |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same custom non-commercial terms. |
| **Restrictions** | Commercial use not permitted without separate permission; redistribution restricted. Do not assume a commercially published investigation is 'informational' use. |
| **Open-source status** | **Source available** — Restricted model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee for permitted use. Hidden cost is the environment: a TensorFlow 1.2.1 pin realistically means a dedicated container and hours of engineer time.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/grip-unina/noiseprint
- https://grip-unina.github.io/noiseprint/

---

## 1. Purpose

CNN that extracts a camera-model noise fingerprint from an image, enabling detection of regions whose fingerprint differs from the rest of the frame or from a claimed camera model.

## Journalism / investigative use case

Testing whether a photo's noise fingerprint is consistent with the camera model it is claimed to come from, or whether part of the frame carries a different fingerprint from the rest — a splicing indicator independent of JPEG block artefacts, which makes it a genuinely complementary second opinion to CAT-Net.

## 2. Audience

specialist investigator

## 3. Project type

model · bucket `source-available-restricted`

## 4. Pros

- Provides a signal independent of compression artefacts, so it can corroborate or contradict JPEG-based methods rather than merely repeating them
- Camera-model consistency testing addresses a specific, answerable question ('is this from the device claimed?') rather than a vague authenticity score
- Local inference with author-provided weights, no third-party service documented

## 5. Cons

- NOT open source: LICENSE.txt restricts use to informational and non-profit purposes, copyright GRIP-UNINA — the same restriction as TruFor and a blocker for commercial newsroom use
- TensorFlow 1.2.1 pin makes installation genuinely painful in 2026; you will fight the environment before you see a result
- Open PR backlog and limited maintenance (pushed 2026-03-27, no releases, 158 stars, 16 open issues)
- Noise fingerprints are destroyed by resizing and platform recompression, so the method applies only to images close to original — a narrow slice of real cases

## 6. Feedback (documented)

No individual user reports verified. Documented: the LICENSE.txt restriction to informational and non-profit use (read session 1, retained); the TensorFlow 1.2.1 pin stated in the repository; 16 open issues including an open PR backlog.

## 7. Assessment

Specialist, legally restricted and operationally awkward — I would not deploy it in a commercial newsroom. Where it genuinely helps is in partnership with an academic forensics group, which is also the context its licence contemplates. For your profile the actionable alternative is to build the camera-consistency check differently: ExifTool plus MediaInfo for declared device metadata, CAT-Net for compression-based splicing, and an expert partner when a case warrants PRNU-class analysis.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2026-03-27, no releases or tags, 158 stars, 16 open issues including unmerged PRs. Eight months since last push, a long-obsolete framework pin, and unaddressed contributions — declining rather than merely low-activity.

## 9. Licensing

**Licence:** NOT OSS — custom GRIP-UNINA terms: LICENSE.txt restricts use to informational and non-profit purposes _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same custom non-commercial terms.

**Restrictions:** Commercial use not permitted without separate permission; redistribution restricted. Do not assume a commercially published investigation is 'informational' use.

**Licence evidence:** https://github.com/grip-unina/noiseprint

## 10. Costs

No fee for permitted use. Hidden cost is the environment: a TensorFlow 1.2.1 pin realistically means a dedicated container and hours of engineer time.

## 11. Privacy and data flows

Local inference, no third-party service documented. Suitable for sensitive images on an isolated machine, if you can get it running.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Non-commercial licence
- TensorFlow 1.2.1 dependency pin

## 13. Alternatives

- [CAT-Net](JAI-A4-19.md) for commercially usable splicing detection
- [TruFor](JAI-A4-18.md) for stronger localisation if non-profit use applies
- Collaboration with an academic image-forensics group for PRNU-class camera analysis

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/grip-unina/noiseprint
- https://grip-unina.github.io/noiseprint/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |

---

← 349. [ASVspoof 2021 baseline systems](JAI-A4-30.md) · 351. [dorks_hunter](OSINT-C1-08.md) →
