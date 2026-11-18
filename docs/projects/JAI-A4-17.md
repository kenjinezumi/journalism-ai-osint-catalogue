# PhotoHolmes

`JAI-A4-17` · **59/100** · overall rank 327 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 123) |
| **Segment** | A4 · Fact-checking support and media verification (rank 11) |
| **Subcategory** | Image forensics harness |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | photoholmes (Universidad de la República, Uruguay) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 (base library only) |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Mixed |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/photoholmes/photoholmes) · [Documentation](https://github.com/photoholmes/photoholmes#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 2/5 → **weighted 59/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | Apache-2.0 (base library only) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Varies per bundled method; the README flags TruFor as restricted to non-profit use. Several bundled methods carry non-OSI academic terms. |
| **Restrictions** | Material: the harness is permissive but the methods inside it are not uniformly so. A commercial newsroom must audit and selectively disable methods. Do not treat the Apache-2.0 badge as covering the ensemble. |
| **Open-source status** | **Mixed** — Open-source code, restricted model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. GPU helpful for some methods; per-method weights downloaded from third-party hosts. Cost is engineer time for the licence audit and integration. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/photoholmes/photoholmes/blob/main/LICENSE
- https://github.com/photoholmes/photoholmes

---

## 1. Purpose

Python library that packages multiple published image-forgery detection and localisation methods behind a common interface, with preprocessing, benchmarking and a plugin structure for adding methods.

## Journalism / investigative use case

Lets an engineer embedded in a verification team run several published localisation methods over one contested image and compare heatmaps, rather than trusting a single model — and, just as usefully, benchmark honestly how badly each method degrades on recompressed social-media copies.

## 2. Audience

engineer, specialist investigator

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Method ensembling with a common interface is the correct epistemic approach to image forensics: agreement across independent methods is informative, a single heatmap is not
- The benchmarking capability lets you measure degradation on platform-recompressed images, which is the condition that actually matters and which papers rarely report
- Apache-2.0 for the harness, and the README explicitly flags that bundled methods carry their own terms — honest licence signposting that is rare in research code

## 5. Cons

- Apache-2.0 covers the harness only: individual methods carry their own, sometimes non-commercial licences, and the README specifically flags TruFor as restricted to non-profit use — so the ensemble as a whole may not be commercially usable
- Outputs are probabilistic localisation maps and scores from research models, NOT conclusive proof of manipulation; heatmaps are highly suggestive to non-experts and easy to over-read
- Low activity (pushed 2026-01-05, no releases, 53 stars) and a small academic team — you would own maintenance
- Per-method pretrained weights are fetched from third-party hosts (HuggingFace, authors' links), which is a supply-chain and availability risk

## 6. Feedback (documented)

No individual user reports verified. Documented: the README's own licence warnings about bundled methods (including TruFor's non-profit restriction); 53 stars with 3 open issues; last push 2026-01-05.

## 7. Assessment

The right structure for forensic work and worth adopting if you have an engineer who can own it — the per-method licence audit is the task to do first, method by method, before anything reaches publication. For your profile the pragmatic configuration is to enable only the permissively licensed methods and accept a smaller ensemble, since a non-commercial method's output in a commercially published story is a licence breach. Every output is a lead requiring non-forensic corroboration.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-01-05, no releases or tags, 53 stars, 3 open issues. Ten months since last push; small academic project with a complete initial release. Not classified declining because the harness is functionally complete and the issue count is low, but there is no evidence of ongoing work.

## 9. Licensing

**Licence:** Apache-2.0 (base library only) _(SPDX verified)_

**Model / data licence:** Varies per bundled method; the README flags TruFor as restricted to non-profit use. Several bundled methods carry non-OSI academic terms.

**Restrictions:** Material: the harness is permissive but the methods inside it are not uniformly so. A commercial newsroom must audit and selectively disable methods. Do not treat the Apache-2.0 badge as covering the ensemble.

**Licence evidence:** https://github.com/photoholmes/photoholmes/blob/main/LICENSE

## 10. Costs

No fee. GPU helpful for some methods; per-method weights downloaded from third-party hosts. Cost is engineer time for the licence audit and integration. Estimate.

## 11. Privacy and data flows

Inference is local, so case images need not leave the newsroom — a significant advantage over the InVID plugin's forensics panels. Weight downloads from third-party hosts are the only external touchpoint and can be pre-staged.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Bundled methods carry mixed and partly non-commercial licences — per-method audit required before commercial publication

## 13. Alternatives

- [Sherloq](OSINT-C2-12.md) for a GUI workbench usable by a non-engineer, fully local
- [CAT-Net](JAI-A4-19.md) for JPEG-specific splicing detection with CC-BY-4.0 weights
- [TruFor](JAI-A4-18.md) for reliability-mapped localisation — but non-commercial licence only

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/photoholmes/photoholmes
- https://github.com/photoholmes/photoholmes/blob/main/LICENSE

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

← 326. [Froide](JAI-A1-29.md) · 328. [recon-ng](OSINT-C3-30.md) →
