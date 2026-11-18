# AASIST

`JAI-A4-29` · **58/100** · overall rank 333 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 126) |
| **Segment** | A4 · Fact-checking support and media verification (rank 14) |
| **Subcategory** | Audio spoofing detection |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | Clova AI Research (clovaai) |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/clovaai/aasist) · [Documentation](https://github.com/clovaai/aasist#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 1/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 58/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | MIT — pretrained models shipped in-repository under the same licence. |
| **Restrictions** | None material. The ASVspoof 2019 LA dataset used for training/evaluation has its own separate terms. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Modest GPU or even CPU for inference on short clips. ASVspoof dataset obtained separately for any retraining. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/clovaai/aasist/blob/main/LICENSE
- https://github.com/clovaai/aasist

---

## 1. Purpose

Graph-attention-based anti-spoofing model for speech, detecting synthetic and converted voice using integrated spectro-temporal graph attention over raw audio.

## Journalism / investigative use case

Screening suspect voice notes, leaked 'audio recordings' of politicians and robocall clips for synthesis or voice-conversion artefacts — the audio half of verification, where there is far less tooling available than for video and where fabricated audio has already been used in elections.

## 2. Audience

engineer, specialist investigator

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- Addresses a genuine and growing gap: synthetic audio is cheaper to produce and harder to verify than video, and there are very few open tools
- MIT code with pretrained models shipped in-repository under the same licence — unusually clean licensing for this field, and the main reason to prefer it over the academic-licensed alternatives
- Fully local inference with no API keys, so a suspect recording stays in the newsroom
- Compact model that runs without heavy infrastructure

## 5. Cons

- Outputs a probabilistic spoofing score, NOT proof that audio is synthetic — and in a field where a false accusation against a politician is catastrophic, that distinction is everything
- The headline sub-1% EER figures are on ASVspoof 2019 logical access, a clean studio-condition benchmark; published in-the-wild performance is far worse, so the impressive number does not transfer
- Dormant: last push 2023-06-25, no releases or tags, 314 stars, 4 open issues — three years inactive, and the synthesis methods it was trained against are now superseded
- Requires the ASVspoof 2019 LA dataset (separate terms) for training or re-evaluation

## 6. Feedback (documented)

No individual user reports verified. Documented: MIT licence for code and in-repo pretrained models; dormancy since June 2023; the benchmark-versus-in-the-wild performance gap, which is consistent with the Deepfake-Eval-2024 finding of roughly 48% AUC degradation for audio models moved to in-the-wild data.

## 7. Assessment

The best-licensed option in a weak field, and worth having precisely because audio verification has so few alternatives — but its training predates current voice-cloning systems, so treat a negative result as nearly meaningless and a positive result as a lead. For your profile the practical posture on suspect audio is: run AASIST, run forced alignment or spectral inspection, and above all pursue provenance — who first posted it, what the earliest copy's metadata says, whether the purported speaker's circumstances fit. Detection alone should never carry a story.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2023-06-25, no releases or tags, 314 stars, 4 open issues. Three years inactive. Material here because the threat model (voice synthesis methods) has changed substantially since.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** MIT — pretrained models shipped in-repository under the same licence.

**Restrictions:** None material. The ASVspoof 2019 LA dataset used for training/evaluation has its own separate terms.

**Licence evidence:** https://github.com/clovaai/aasist/blob/main/LICENSE

## 10. Costs

No fee. Modest GPU or even CPU for inference on short clips. ASVspoof dataset obtained separately for any retraining. Estimate.

## 11. Privacy and data flows

Fully local inference with no API keys — the suspect recording never leaves your machine, which matters because the audio itself may identify a source.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Dormant since 2023; trained against pre-2024 synthesis methods

## 13. Alternatives

- [ASVspoof 2021 baseline systems](JAI-A4-30.md) for the official scoring code to compute your own EER — but licence unconfirmed
- Commercial audio-detection services, which upload the clip and whose accuracy claims deserve the same scepticism
- Provenance investigation and spectral/forced-alignment analysis as the primary approach

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/clovaai/aasist
- https://github.com/clovaai/aasist/blob/main/LICENSE

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

← 332. [DeepfakeBench](JAI-A4-25.md) · 334. [Full Fact AI Trust Benchmark](JAI-A4-15.md) →
