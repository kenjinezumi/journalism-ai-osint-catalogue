# Community Forensics

`JAI-A4-21` · **65/100** · overall rank 291 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 112) |
| **Segment** | A4 · Fact-checking support and media verification (rank 6) |
| **Subcategory** | Synthetic image detection |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | Jeongsoo Park / Owens Lab (University of Michigan) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (code) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/JeongsooP/Community-Forensics) · [Documentation](https://github.com/JeongsooP/Community-Forensics#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 5/5 → **weighted 65/100**

---

## 1. Purpose

Synthetic-image detector trained on a dataset assembled from thousands of community-published generative models, aimed at generalising beyond the handful of generators most detectors see.

## Journalism / investigative use case

The most defensible currently available open detector baseline for 'is this image synthetic?' triage, because its training distribution covers thousands of generators rather than a handful — still a lead generator for reporting, not an adjudicator.

## 2. Audience

engineer, specialist investigator

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- Training-distribution breadth is the right response to the generalisation problem that defeats most detectors — thousands of generators rather than a curated few
- MIT code and MIT weights (stated on the OwensLab/commfor-model-384 HuggingFace model card), so it is commercially usable without licence review
- Inference runs locally after download, so case images need not be sent to a detection service
- Recent enough (pushed 2026-01-06) to cover a meaningful span of modern generators

## 5. Cons

- Output is a probability — an assistive signal that cannot establish whether an image was AI-generated, and is not conclusive proof
- The repository does not document accuracy bounds, calibration or per-generator performance, so you cannot state an error rate when an editor asks for one
- Low activity and tiny community (64 stars, 2 open issues, no releases) — you would own any maintenance
- Weights and datasets are fetched from HuggingFace and Dropbox-hosted checkpoints, which is a supply-chain and availability risk

## 6. Feedback (documented)

No individual user reports verified. Documented: MIT weights stated on the OwensLab/commfor-model-384 HuggingFace card (read session 1, retained); 64 stars; no documented calibration in the repository, which is itself the significant gap.

## 7. Assessment

If you must have an open synthetic-image detector, this is the one I would use, because the training breadth is the only property that correlates with real-world performance and the licence is clean. But I would deploy it with an explicit internal policy: the score goes in the reporting notes, never in the story, and a synthetic-media claim requires non-forensic corroboration. The absence of documented calibration means you cannot honestly publish a confidence figure derived from it.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-01-06, no releases or tags, 64 stars, 2 open issues. Ten months since last push; an academic release that appears complete rather than abandoned, but with no evidence of ongoing work.

## 9. Licensing

**Licence:** MIT (code) _(SPDX verified)_

**Model / data licence:** MIT, stated on the OwensLab/commfor-model-384 HuggingFace model card.

**Restrictions:** None material — unusually clean for a forensic model. The training dataset aggregates outputs from many third-party generators, whose own terms are a residual consideration if you redistribute the dataset.

**Licence evidence:** https://huggingface.co/OwensLab/commfor-model-384

## 10. Costs

No fee. GPU for practical inference throughput; weight and dataset downloads from HuggingFace and Dropbox. Estimate.

## 11. Privacy and data flows

Weights and datasets fetched from HuggingFace and Dropbox; after download, inference runs locally so case images need not leave your infrastructure.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [UniversalFakeDetect](JAI-A4-20.md) as a second baseline for comparison
- [Deepfake-Eval-2024](JAI-A4-31.md) for the in-the-wild degradation figures that contextualise any score
- Provenance-based verification (C2PA, reverse search, source contact) which is more reliable than detection

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/JeongsooP/Community-Forensics
- https://huggingface.co/OwensLab/commfor-model-384

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 290. [Carrot2](JAI-A2-07.md) · 292. [GraphSense](OSINT-C3-21.md) →
