# DeepfakeBench

`JAI-A4-25` · **58/100** · overall rank 332 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 125) |
| **Segment** | A4 · Fact-checking support and media verification (rank 13) |
| **Subcategory** | Deepfake detection benchmark |
| **Type** | prototype |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | SCLBD (Sun Yat-sen University) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | CC-BY-NC-4.0 (GitHub API reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/SCLBD/DeepfakeBench) · [Documentation](https://github.com/SCLBD/DeepfakeBench#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 2/5 · privacy 4/5 · usability 2/5 · licence+cost 1/5 → **weighted 58/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Unified benchmark and training framework implementing many published face-manipulation detectors with standardised preprocessing, training and cross-dataset evaluation.

## Journalism / investigative use case

The practical way a technically staffed newsroom or research partner can run several published detectors over the same suspect video and see whether they agree, instead of trusting one black-box score — and the reference for how badly detectors generalise outside their training data.

## 2. Audience

engineer

## 3. Project type

prototype · bucket `source-available-restricted`

## 4. Pros

- Standardised preprocessing and evaluation is the methodological contribution: it makes detector comparisons meaningful, where published numbers otherwise are not comparable
- Implements many detectors in one framework, so an ensemble-of-opinions workflow is practical rather than a multi-week integration
- The project's own framing is honest — cross-dataset generalisation remains the open problem — which is exactly the message a newsroom needs
- Substantial community for a research framework (1,142 stars) with a tagged release (v1.0.3)

## 5. Cons

- CC-BY-NC-4.0 licence on the framework: non-commercial only, so a commercially operated newsroom cannot use it as infrastructure without permission — and GitHub reports NOASSERTION, so this is easy to miss
- Benchmark datasets must be obtained separately under their own agreements, and the repository marks some as not rights-cleared — a compounding legal complication
- Outputs are probabilistic scores, NEVER conclusive proof of manipulation; detectors scoring near-perfectly in-domain degrade sharply in the wild
- Activity has slowed (pushed 2025-08-20, release 2024-05-27) with 101 open issues; heavy PyTorch/CUDA setup

## 6. Feedback (documented)

No individual user reports verified. Documented: the CC-BY-NC-4.0 framework licence and the repository's own notes that some datasets are not rights-cleared (recorded session 1, retained); 1,142 stars with 101 open issues; last push 2025-08-20.

## 7. Assessment

Use it through a research partner rather than in-house if your outlet is commercial — the NC licence plus the dataset rights questions make direct use legally untidy. Its real value to you is the published finding rather than the software: detector agreement is informative, detector scores are not, and in-the-wild performance is far below reported figures. For an editor conversation, DeepfakeBench plus Deepfake-Eval-2024 together make the case for not publishing on detector output.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2025-08-20, latest release v1.0.3 (2024-05-27), SPDX NOASSERTION (actual licence CC-BY-NC-4.0), 1,142 stars, 101 open issues. Fifteen months since last push and over two years since the release, with a growing backlog.

## 9. Licensing

**Licence:** CC-BY-NC-4.0 (GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** CC-BY-NC-4.0 for the framework; per-dataset terms vary and the repository marks some datasets as not rights-cleared.

**Restrictions:** Non-commercial only — a blocker for commercially operated newsrooms. NGO or non-profit status does not automatically satisfy NonCommercial where output is commercially published. Separately, some bundled dataset references are not rights-cleared, so dataset acquisition carries its own risk.

**Licence evidence:** https://github.com/SCLBD/DeepfakeBench

## 10. Costs

No fee for non-commercial use. Requires GPU/CUDA infrastructure and large dataset downloads obtained under separate agreements. Engineer time for setup is substantial. Estimate.

## 11. Privacy and data flows

Local training and inference. Dataset acquisition involves third-party request forms and downloads, which discloses your interest to dataset custodians but not your case material.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- CC-BY-NC-4.0 — non-commercial only
- Some referenced datasets are not rights-cleared

## 13. Alternatives

- A research partner running it on your behalf under the NC licence
- [Community Forensics](JAI-A4-21.md) for an MIT-licensed single-detector baseline
- [Deepfake-Eval-2024](JAI-A4-31.md) for the in-the-wild performance figures to cite

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/SCLBD/DeepfakeBench

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

← 331. [UniversalFakeDetect](JAI-A4-20.md) · 333. [AASIST](JAI-A4-29.md) →
