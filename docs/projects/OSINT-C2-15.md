# Bellingcat smart-image-sorter

`OSINT-C2-15` · **59/100** · overall rank 329 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 130) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 48) |
| **Subcategory** | Image triage |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Dormant |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/smart-image-sorter) · [Documentation](https://github.com/bellingcat/smart-image-sorter#readme) |

**Scores** — relevance 3/5 · capability 2/5 · maintenance 1/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 59/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

CLI that classifies images into user-defined categories using zero-shot vision-language models, sorting a directory of images into labelled folders.

## Journalism / investigative use case

Triage a large unsorted image dump by describing the categories you care about in plain words — 'military vehicle', 'street protest', 'document scan' — and letting the model bucket images for review, turning an unreviewable folder into a prioritised queue.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Zero-shot labels mean no training data and no annotation, so an analyst can define investigation-specific categories in minutes
- Runs locally after weight download with no paid API, so a sensitive image dump is not uploaded anywhere
- Apache-2.0 and simple enough to adapt; built by Bellingcat for practising investigators
- GPU helpful but not required, so it works on an analyst workstation

## 5. Cons

- Zero-shot classification is an unreliable triage aid, not a labelling authority: accuracy varies sharply with label wording and it fails on fine-grained military or technical distinctions — exactly the distinctions investigations often need
- Every bucket needs human review, so it reorders work rather than reducing it — valuable, but not the labour saving people expect
- Dormant: last push 2024-08-14, no releases, 68 stars — over two years quiet, and the underlying model landscape has moved considerably since
- Model weights are GB-scale downloads, which is a practical constraint on a field machine

## 6. Feedback (documented)

No individual user reports verified — 68 stars means minimal community signal. Documented: no releases, last push 2024-08-14, Apache-2.0. The accuracy limitations of zero-shot classification on fine-grained categories are a documented property of the method rather than a defect of this implementation.

## 7. Assessment

The idea is right and the implementation is stale. For your profile I would reimplement the same pattern against a current vision-language model — it is a short script — and gain substantially better accuracy, since zero-shot classification has improved markedly since 2024. Keep the core discipline either way: the model produces a review order, never a label you act on, and fine-grained technical identification (which munition, which uniform) must be done by a human expert.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-08-14, no releases or tags, 68 stars, 0 open issues. Over two years without activity; because the value depends on the underlying model, staleness here means using a model generation behind what is available.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Depends on the vision-language model selected; weights fetched from third-party hubs and not individually verified in this survey.

**Restrictions:** Code permissive. The imported risk is the model licence — verify the specific checkpoint before commercial use.

**Licence evidence:** https://github.com/bellingcat/smart-image-sorter/blob/main/LICENSE

## 10. Costs

No fee and no paid API. GB-scale model weight download; GPU helpful but not required. Estimate.

## 11. Privacy and data flows

Local inference after weights download; images are not uploaded if run locally, which is the property that makes it usable on a sensitive dump.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Dormant since 2024; model generation behind current capability

## 13. Alternatives

- Reimplementing the pattern with a current vision-language model — recommended
- [imagededup](OSINT-C2-07.md) first, to collapse duplicates before classification
- [VFRAME](OSINT-C2-14.md)'s approach (a trained narrow detector) where a specific object class matters and accuracy is critical

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/bellingcat/smart-image-sorter
- https://github.com/bellingcat/smart-image-sorter/blob/main/LICENSE

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

← 328. [recon-ng](OSINT-C3-30.md) · 330. [OSINT Framework](OSINT-C1-13.md) →
