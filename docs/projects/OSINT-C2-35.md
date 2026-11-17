# Hierarchical-Localization (hloc)

`OSINT-C2-35` · **67/100** · overall rank 284 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 104) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 40) |
| **Subcategory** | Visual localisation pipeline |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Computer Vision and Geometry Group, ETH Zurich (cvg) |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 (framework) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/cvg/Hierarchical-Localization) · [Documentation](https://github.com/cvg/Hierarchical-Localization#readme) |

**Scores** — relevance 3/5 · capability 5/5 · maintenance 3/5 · privacy 4/5 · usability 1/5 · licence+cost 3/5 → **weighted 67/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Modular visual-localisation toolbox that combines image retrieval, local feature extraction and matching, and structure-from-motion to estimate the camera pose of a query image within a reference reconstruction.

## Journalism / investigative use case

The most rigorous available approach to placing a photograph: build a reference reconstruction of a candidate area from panoramas or collected imagery, then localise the query photograph within it, yielding an estimated camera position rather than just a 'same place' judgement.

## 2. Audience

specialist investigator, engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Produces an estimated camera pose, which is a stronger and more specific result than pairwise matching — you can say where the photographer stood, not merely that the places match
- Modular design lets you swap retrieval and matching components, so you can deliberately select Apache-2.0 parts and avoid restricted ones
- Apache-2.0 on the framework itself, with substantial community adoption (4,268 stars) and relatively recent activity (pushed 2025-12-10)
- Backed by a serious academic group with published methodology, so the technique is citable

## 5. Cons

- Its default and documented pipelines can pull SuperGlue weights, which carry Magic Leap's noncommercial academic licence — so an out-of-the-box hloc run may import a restriction the Apache-2.0 framework licence does not cover. This is the specific trap to avoid
- Heavy: structure-from-motion over a reference set is computationally expensive and requires building a reconstruction before you can localise anything
- Slowing cadence: last release v1.4 (2023-07-20) and last push 2025-12-10, with 174 open issues — maintained but not briskly
- Substantial expertise required; this is the most technically demanding item in this segment and not usable without a computer-vision-literate engineer

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 4,268 stars with 174 open issues, release v1.4 (2023-07-20), last push 2025-12-10, Apache-2.0. The SuperGlue licence interaction is a finding of this session (lead L9): hloc's framework licence is permissive but its component weights are not uniformly so.

## 7. Assessment

The right tool for a high-stakes geolocation where an estimated camera position would materially strengthen the story — and worth the effort only then. For your profile the mandatory step before use is a component audit: configure hloc with Apache-2.0 matchers (LoFTR or a permissive alternative) and explicitly disable SuperGlue, because the default path imports a noncommercial licence silently. Document the component choices in the methodology note so the result is both reproducible and licence-clean.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2025-12-10, latest release v1.4 (2023-07-20), 4,268 stars, 174 open issues. Nearly a year since the last push and over three years since a release, but substantial community use and no deprecation. Stable-low rather than declining, with the caveat that an unmaintained CV pipeline accumulates dependency debt.

## 9. Licensing

**Licence:** Apache-2.0 (framework) _(SPDX verified)_

**Model / data licence:** MIXED AND MATERIAL: the framework is Apache-2.0, but default pipelines can fetch SuperGlue weights under Magic Leap's noncommercial academic agreement. Component weights must be audited individually.

**Restrictions:** The framework imposes nothing, but enabling SuperGlue imports a noncommercial restriction that would bar commercial publication. Select and document permissive components explicitly.

**Licence evidence:** https://github.com/cvg/Hierarchical-Localization/blob/master/LICENSE

## 10. Costs

No fee. Significant GPU and compute for reconstruction and localisation; engineer time is the dominant cost. Estimate; assumes self-hosted GPU and an existing reference imagery set.

## 11. Privacy and data flows

Local processing of local imagery. Note that assembling the reference set (downloading many panoramas for a candidate area) discloses that area of interest to the imagery provider.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Default pipelines can pull noncommercially licensed SuperGlue weights — component audit required

## 13. Alternatives

- [LoFTR](OSINT-C2-34.md) alone for pairwise matching without reconstruction — much simpler
- Manual geolocation against panoramas, which remains the standard practice
- A university partner with existing hloc expertise and an institutional licence covering SuperGlue

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/cvg/Hierarchical-Localization
- https://github.com/cvg/Hierarchical-Localization/blob/master/LICENSE
- `../sources/evidence/leads.md`

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

← 283. [AnalyticsRelationships](SUR-B2-09.md) · 285. [Montreal Forced Aligner](JAI-A2-29.md) →
