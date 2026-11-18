# VFRAME

`OSINT-C2-14` · **60/100** · overall rank 323 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 127) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 47) |
| **Subcategory** | Conflict-footage triage |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Adam Harvey (vframeio) |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/vframeio/vframe) · [Documentation](https://vframe.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 1/5 · licence+cost 5/5 → **weighted 60/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Custom detection models are domain-specific and may be distributed separately; their terms were not verified in this survey. |
| **Restrictions** | Code permissive. Model availability and terms are the open question. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure; staff effort |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. NVIDIA GPU strongly recommended; no paid API. The real cost would be training a detector for your object class — annotation labour plus GPU time. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/vframeio/vframe/blob/main/LICENSE
- https://github.com/vframeio/vframe
- https://vframe.io/

---

## 1. Purpose

Computer-vision toolkit for human-rights investigation, providing object-detection pipelines over large video archives with custom models trained for specific munitions and objects.

## Journalism / investigative use case

Triage very large conflict-footage archives by flagging frames likely to contain a specific object, such as a cluster-munition remnant, so investigators review a shortlist instead of thousands of hours of video — work that is otherwise simply not done because nobody can watch it all.

## 2. Audience

specialist investigator, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Purpose-built for human-rights investigation rather than adapted from generic CV, with custom models for munitions identification — a genuinely unusual and valuable specialisation
- Addresses an intractable problem: conflict-footage archives are too large to review manually, so a shortlist is the difference between evidence found and evidence lost
- MIT licensed with local processing of local archives, appropriate for sensitive material
- The methodology (train a detector for a specific object class relevant to one investigation) is reusable even if the code is not

## 5. Cons

- Long dormancy: last push 2023-05-28, no releases, 76 stars — three and a half years quiet, and dependency rot in a deep-learning project of that age is near-certain
- Detector outputs are probabilistic signals requiring human confirmation of every hit, never conclusive identification — and misidentifying a munition type in print would be a serious error
- Custom models are domain-specific and may not be distributed with the repository, so the capability depends on model availability not just code
- NVIDIA GPU strongly recommended, and the deep-learning runtime of that era will need pinning or rebuilding

## 6. Feedback (documented)

No individual user reports verified. Documented: 76 stars with 0 open issues, no releases, last push 2023-05-28, MIT licence. The project's human-rights-investigation orientation is documented on vframe.io; VFRAME's munitions-detection work is known in the open-source-investigation community, though I verified no specific deployment.

## 7. Assessment

Reference only as software, but important as a methodology for your work. The idea — train a narrow detector for the specific object an investigation turns on, and use it to produce a review shortlist — is sound and reproducible today with maintained tooling (YOLO-family models, or a fine-tuned vision model) in far less time than reviving a 2023 pipeline. If you have a conflict-footage archive problem, I would rebuild the approach rather than the code, and keep human confirmation of every hit as an absolute rule.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2023-05-28, no releases or tags, 76 stars, 0 open issues. Three and a half years without activity on a deep-learning project; the dependency stack of that period (CUDA, framework versions) makes reuse a porting exercise.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Custom detection models are domain-specific and may be distributed separately; their terms were not verified in this survey.

**Restrictions:** Code permissive. Model availability and terms are the open question.

**Licence evidence:** https://github.com/vframeio/vframe/blob/main/LICENSE

## 10. Costs

No fee. NVIDIA GPU strongly recommended; no paid API. The real cost would be training a detector for your object class — annotation labour plus GPU time. Estimate.

## 11. Privacy and data flows

Local processing of local archives, which is essential for conflict footage that may identify victims or witnesses.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Dormant since 2023; deep-learning dependency stack requires porting

## 13. Alternatives

- A fine-tuned modern object detector (YOLO-family) built with maintained tooling for the same purpose
- [Bellingcat smart-image-sorter](OSINT-C2-15.md) for zero-shot triage without training
- [Atlos](OSINT-C2-36.md) for the collaborative verification workflow around such archives

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/vframeio/vframe
- https://vframe.io/
- https://github.com/vframeio/vframe/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [ExifTool](OSINT-C2-01.md) | 96 | Adopt |
| 2 | [geopandas](OSINT-C2-21.md) | 94 | Adopt |
| 3 | [PySceneDetect](OSINT-C2-10.md) | 94 | Adopt |
| 4 | [QGIS](OSINT-C2-19.md) | 91 | Adopt |
| 5 | [ShadowFinder](OSINT-C2-17.md) | 91 | Adopt |
| 6 | [MediaInfo](OSINT-C2-04.md) | 88 | Adopt |
| 7 | [osm-search](OSINT-C2-27.md) | 87 | Adopt |
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |

---

← 322. [news-please](JAI-A1-02.md) · 324. [FEVER platform and baselines](JAI-A4-06.md) →
