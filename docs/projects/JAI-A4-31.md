# Deepfake-Eval-2024

`JAI-A4-31` · **47/100** · overall rank 348 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 135) |
| **Segment** | A4 · Fact-checking support and media verification (rank 22) |
| **Subcategory** | In-the-wild deepfake evaluation |
| **Type** | dataset |
| **Bucket** | `uncertain` |
| **Maintainer** | Nuria Chandra and collaborators |
| **Maintenance** | Dormant |
| **Licence** | NOT CONFIRMED — no licence for code or data visible on the repository page |
| **Licence type** | Unresolved |
| **Open-source status** | Unverified |
| **Software price** | **No software fee** |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/nuriachandra/Deepfake-Eval-2024) · [Documentation](https://github.com/nuriachandra/Deepfake-Eval-2024#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 1/5 · privacy 4/5 · usability 2/5 · licence+cost 1/5 → **weighted 47/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Unresolved |
| **Exact licence (as recorded)** | NOT CONFIRMED — no licence for code or data visible on the repository page |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | NOT confirmed — dataset distributed via HuggingFace under terms not stated at the repository page. |
| **Restrictions** | Unresolved for both code and data. Citing the published finding is unproblematic; redistributing the dataset is not advisable until terms are confirmed. The underlying media is third-party content with its own rights. |
| **Open-source status** | **Unverified** — Licence could not be confirmed — reuse legally unresolved |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Dataset retrieval from HuggingFace; no runtime service. Minimal cost.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/nuriachandra/Deepfake-Eval-2024

> **Unresolved:** the licence could not be confirmed from the evidence gathered.

---

## 1. Purpose

Benchmark of in-the-wild deepfake media collected from real circulation in 2024, with documentation and labels, used to measure how published detectors perform outside curated academic datasets.

## Journalism / investigative use case

The citation to reach for when an editor or vendor claims a detector is '98% accurate'. Its central finding is that open-source state-of-the-art detector AUC drops by roughly 50% for video, 48% for audio and 45% for image models when moved from academic benchmarks to in-the-wild media.

## 2. Audience

newsroom analyst, engineer, specialist investigator

## 3. Project type

dataset · bucket `uncertain`

## 4. Pros

- Supplies the single most useful number in this entire subcategory for newsroom decision-making: detectors lose roughly half their apparent accuracy on real circulating media
- In-the-wild collection methodology is what makes it credible where FF++ and similar curated datasets are not
- Directly actionable editorially: it justifies a policy of not publishing synthetic-media claims on detector output

## 5. Cons

- No licence for code or data was visible on the repository page, so redistribution and commercial use are legally unresolved; the dataset is distributed via HuggingFace under terms not confirmed at the repo page
- The repository contains no fine-tuning or evaluation code — only documentation and labels — so it is a finding and a label set, not a runnable benchmark
- Dormant and tiny (last push 2025-03-05, 17 stars, 1 open issue), so the finding has limited independent replication so far
- A 2024 snapshot: generator and detector landscapes move fast, so the specific percentages will drift even if the direction holds

## 6. Feedback (documented)

No individual user reports verified. The documented central finding — roughly 50% video, 48% audio and 45% image AUC degradation moving from academic benchmarks to in-the-wild media — is the project's own reported result, recorded in session 1 and retained here as a project claim rather than an independently replicated measurement. The licence absence was verified by inspection.

## 7. Assessment

Low as software, high as evidence — and I would score it provisionally for that reason. For your work its value is to settle an argument: it gives you a citable basis for telling an editor that detector output is a lead and not a finding, which protects the newsroom from publishing a false synthetic-media claim. Cite it as a project-reported result, note the licence uncertainty, and do not redistribute the dataset.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2025-03-05, no releases, no detected licence, 17 stars, 1 open issue. Twenty months inactive. As a labelled snapshot its usefulness is less time-dependent than code, but the figures themselves age.

## 9. Licensing

**Licence:** NOT CONFIRMED — no licence for code or data visible on the repository page _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** NOT confirmed — dataset distributed via HuggingFace under terms not stated at the repository page.

**Restrictions:** Unresolved for both code and data. Citing the published finding is unproblematic; redistributing the dataset is not advisable until terms are confirmed. The underlying media is third-party content with its own rights.

**Licence evidence:** https://github.com/nuriachandra/Deepfake-Eval-2024

## 10. Costs

No fee. Dataset retrieval from HuggingFace; no runtime service. Minimal cost.

## 11. Privacy and data flows

Dataset retrieval from HuggingFace; no runtime service and no case material involved.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- No licence for code or data — redistribution legally unresolved
- No evaluation code included

## 13. Alternatives

- [DeepfakeBench](JAI-A4-25.md) for a runnable evaluation framework — non-commercial licence
- [UniversalFakeDetect](JAI-A4-20.md) for a cross-generator generalisation baseline
- Your own small in-the-wild test set assembled from cases your newsroom has handled

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/nuriachandra/Deepfake-Eval-2024

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

← 347. [LAA-Net](JAI-A4-28.md) · 349. [ASVspoof 2021 baseline systems](JAI-A4-30.md) →
