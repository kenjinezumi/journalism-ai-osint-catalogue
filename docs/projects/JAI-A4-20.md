# UniversalFakeDetect

`JAI-A4-20` · **59/100** · overall rank 331 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 124) |
| **Segment** | A4 · Fact-checking support and media verification (rank 12) |
| **Subcategory** | Synthetic image detection |
| **Type** | prototype |
| **Bucket** | `verified-oss` |
| **Maintainer** | Wisconsin AI Vision lab |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/WisconsinAIVision/UniversalFakeDetect) · [Documentation](https://github.com/WisconsinAIVision/UniversalFakeDetect#readme) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 5/5 → **weighted 59/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Not separately stated; weights distributed by the authors under the repository terms. Evaluation datasets aggregate third-party generator outputs whose own terms may vary. |
| **Restrictions** | Code MIT. Residual uncertainty on the aggregated evaluation datasets, which include outputs from generators with their own terms of service. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Roughly 72GB of dataset downloads plus CLIP weights; GPU for evaluation. Bandwidth and storage are the notable costs. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/WisconsinAIVision/UniversalFakeDetect/blob/main/LICENSE
- https://github.com/WisconsinAIVision/UniversalFakeDetect

---

## 1. Purpose

Method and reference implementation showing that a linear classifier on frozen CLIP features generalises across image generators better than purpose-trained detectors, with evaluation sets across many generator families.

## Journalism / investigative use case

A baseline for teams testing whether any synthetic-image detector holds up on their own case material — valuable mainly as the honest yardstick for cross-generator generalisation claims, which is the axis on which vendor detectors fail.

## 2. Audience

engineer

## 3. Project type

prototype · bucket `verified-oss`

## 4. Pros

- The finding itself is the value: a simple CLIP-feature classifier generalising better than specialised detectors is a strong reason to distrust vendor claims about bespoke detection models
- MIT licensed with author-distributed weights, so it can be run and cited freely
- Evaluation across many generator families makes it a usable generalisation test rather than a single-generator demo

## 5. Cons

- A score is a probabilistic signal, NOT evidence or proof that an image was AI-generated — and because the method is simple, non-experts over-trust it
- The repository notes that its released diffusion evaluation set is reduced to 1k real / 1k fake per domain versus 10k in the paper, so published numbers are not reproducible from the release as distributed
- Predates the current generation of image models, so its own generalisation claims need re-testing against 2025-2026 generators
- Requires CLIP weights and author-hosted datasets of roughly 72GB across 20 categories — a substantial download; 24 open issues, no releases

## 6. Feedback (documented)

No individual user reports verified. Documented from the repository itself: the reduced released evaluation set versus the paper (1k versus 10k per domain), which is an honest disclosure by the authors and a real reproducibility limit. 381 stars, 24 open issues, last push 2026-08-19.

## 7. Assessment

Use it as a measuring stick, not a detector. Concretely, for your work: when someone offers an AI-image detector, test it and this baseline on the same set of images from generators neither has seen, and expect both to degrade sharply. The Deepfake-Eval-2024 finding (roughly 45-50% AUC drops in the wild) is the number to keep in mind. Never publish a synthetic-media claim on detector output alone.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-08-19, no releases or tags, 381 stars, 24 open issues. Three months since last push; a research release receiving light maintenance.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Not separately stated; weights distributed by the authors under the repository terms. Evaluation datasets aggregate third-party generator outputs whose own terms may vary.

**Restrictions:** Code MIT. Residual uncertainty on the aggregated evaluation datasets, which include outputs from generators with their own terms of service.

**Licence evidence:** https://github.com/WisconsinAIVision/UniversalFakeDetect/blob/main/LICENSE

## 10. Costs

No fee. Roughly 72GB of dataset downloads plus CLIP weights; GPU for evaluation. Bandwidth and storage are the notable costs. Estimate.

## 11. Privacy and data flows

Dataset and CLIP weight downloads from third-party hosts; classification runs locally, so case images stay in the newsroom.

## 12. Verdict

**Reference only**

## 13. Alternatives

- [Community Forensics](JAI-A4-21.md) for a broader-training-distribution open baseline with MIT weights
- [Deepfake-Eval-2024](JAI-A4-31.md) for the in-the-wild degradation figures to cite
- Non-forensic verification — provenance, reverse search, source contact — which remains more reliable than any detector

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/WisconsinAIVision/UniversalFakeDetect
- https://github.com/WisconsinAIVision/UniversalFakeDetect/blob/main/LICENSE

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

← 330. [OSINT Framework](OSINT-C1-13.md) · 332. [DeepfakeBench](JAI-A4-25.md) →
