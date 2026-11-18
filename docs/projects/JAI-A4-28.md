# LAA-Net

`JAI-A4-28` · **49/100** · overall rank 347 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 134) |
| **Segment** | A4 · Fact-checking support and media verification (rank 21) |
| **Subcategory** | Deepfake detection |
| **Type** | prototype |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | University of Luxembourg SnT (10Ring) |
| **Maintenance** | Stable with low activity |
| **Licence** | SnT Academic License — README states copyright University of Luxembourg, academic use only; not OSI-approved |
| **Licence type** | Restricted / non-OSI |
| **Open-source status** | Source available |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/10Ring/LAA-Net) · [Documentation](https://github.com/10Ring/LAA-Net#readme) |

**Scores** — relevance 2/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 1/5 · licence+cost 1/5 → **weighted 49/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Restricted / non-OSI |
| **Exact licence (as recorded)** | SnT Academic License — README states copyright University of Luxembourg, academic use only; not OSI-approved |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Same academic licence applies to released weights. |
| **Restrictions** | Academic use only. Commercial newsroom use requires permission from the University of Luxembourg. Benchmark datasets are obtained separately under their own terms. |
| **Open-source status** | **Source available** — Source published under a restricted, non-OSI licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee for academic use; commercial use requires permission (terms not publicly listed). GPU with pinned older CUDA/PyTorch; significant setup time. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/10Ring/LAA-Net

---

## 1. Purpose

Localised artefact attention network for deepfake detection, designed to remain effective on low-quality and compressed video rather than only on pristine inputs.

## Journalism / investigative use case

A quality-agnostic detector aimed at the verification pain point most detectors fail on — compressed social-media re-uploads — making it relevant as a second or third opinion in a technical partner's detector ensemble, not as a standalone verdict tool.

## 2. Audience

engineer, specialist investigator

## 3. Project type

prototype · bucket `source-available-restricted`

## 4. Pros

- Explicitly targets compressed and low-quality input, which is the condition of essentially every video a journalist is asked to verify — most detectors are evaluated on pristine data and fail here
- Published with cross-dataset results, so the generalisation claim can be examined rather than taken on trust
- Local inference, so case video stays in the newsroom

## 5. Cons

- SnT Academic License: the README states the software is copyright University of Luxembourg under an academic licence (academic use only, not OSI-approved) — so it is not usable as commercial newsroom infrastructure without permission
- Outputs are probabilistic signals, not conclusive proof of manipulation, and reported numbers show the familiar family-wide spread across test sets
- Pinned older CUDA/PyTorch versions plus a facial alignment and landmark preprocessing chain — a painful install
- Low activity (pushed 2025-11-26, no releases, 180 stars, 16 open issues)

## 6. Feedback (documented)

No individual user reports verified. Documented from the repository README: the SnT academic licence with University of Luxembourg copyright, restricting use to academic purposes; 180 stars, 16 open issues, last push 2025-11-26.

## 7. Assessment

Same pattern as SBI and TruFor: the technically interesting work in this field sits behind academic licences that a commercial newsroom cannot use. If you have a university partner, LAA-Net is worth including in their ensemble precisely because of the compression robustness. In-house, it is off the table. This recurring licence pattern is itself a finding worth carrying into your planning: the deepfake-detection field has no credible, maintained, commercially usable open option today.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2025-11-26, no releases or tags, SPDX NOASSERTION, 180 stars, 16 open issues. Nearly twelve months since last push; a complete academic release.

## 9. Licensing

**Licence:** SnT Academic License — README states copyright University of Luxembourg, academic use only; not OSI-approved _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same academic licence applies to released weights.

**Restrictions:** Academic use only. Commercial newsroom use requires permission from the University of Luxembourg. Benchmark datasets are obtained separately under their own terms.

**Licence evidence:** https://github.com/10Ring/LAA-Net

## 10. Costs

No fee for academic use; commercial use requires permission (terms not publicly listed). GPU with pinned older CUDA/PyTorch; significant setup time. Estimate.

## 11. Privacy and data flows

Local inference; datasets obtained separately. Case material stays local.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Academic-only licence — not usable as commercial newsroom infrastructure

## 13. Alternatives

- A university partner running it under the academic licence
- [Community Forensics](JAI-A4-21.md) for commercially usable image-level detection
- Provenance and earliest-upload tracing instead of detection

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/10Ring/LAA-Net

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

← 346. [DEFAME](JAI-A4-11.md) · 348. [Deepfake-Eval-2024](JAI-A4-31.md) →
