# SuperGlue (pretrained network)

`OSINT-C2-33` · **53/100** · overall rank 340 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 134) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 50) |
| **Subcategory** | Image feature matching |
| **Type** | model |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | Magic Leap |
| **Maintenance** | Dormant |
| **Licence** | NOT OSS — Magic Leap 'SOFTWARE LICENSE AGREEMENT: ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY' (licence blob read 2026-11-17; GitHub reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/magicleap/SuperGluePretrainedNetwork) · [Documentation](https://github.com/magicleap/SuperGluePretrainedNetwork#readme) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 1/5 · privacy 4/5 · usability 2/5 · licence+cost 0/5 → **weighted 53/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Graph-neural-network feature matcher that pairs keypoints between two images, widely used to establish whether two photographs show the same place or object from different viewpoints.

## Journalism / investigative use case

In principle the strongest available method for confirming a geolocation hypothesis: match keypoints between a photograph and a street-level panorama or satellite image to establish that they show the same building or street from different angles — turning a visual hunch into a demonstrable correspondence.

## 2. Audience

specialist investigator, engineer

## 3. Project type

model · bucket `source-available-restricted`

## 4. Pros

- Technically the reference feature matcher of its generation, widely cited and effective at matching across viewpoint, lighting and season changes
- The capability it provides — demonstrable keypoint correspondence between two images — is the most rigorous geolocation confirmation available short of ground truth
- Well-documented with reproducible demos, so the method is understandable and the output is visually explainable to an editor

## 5. Cons

- BLOCKER, verified in this session: the LICENSE is a Magic Leap 'SOFTWARE LICENSE AGREEMENT — ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY' agreement between the licensee's academic institution or non-profit and Magic Leap. A commercially operated newsroom cannot use it
- Dormant: last push 2024-08-30, no releases, 60 open issues against 4,107 stars — no maintenance and no prospect of a licence change
- GitHub reports SPDX NOASSERTION, so automated licence scanning does not flag the restriction — it is easy to adopt this by accident, which is why it is recorded as a lead
- Superseded technically as well: newer matchers (LightGlue and successors) are faster and often better, so the restriction costs you less than it would have in 2021

## 6. Feedback (documented)

No individual user reports verified. The decisive documented fact, established in this session by reading the licence blob: the agreement is restricted to academic or non-profit noncommercial research use only (recorded in sources/evidence/leads.md as lead L9). 4,107 stars with 60 open issues and no activity since August 2024.

## 7. Assessment

Avoid for new deployment in a commercial newsroom — this is a licence conclusion, not a technical one, and it is the most easily missed blocker in the geolocation toolchain because the restriction is invisible to SPDX scanners. Use LoFTR (Apache-2.0) or Hierarchical-Localization (Apache-2.0) instead, while checking that an hloc pipeline you enable does not itself pull SuperGlue weights. If you work with a university partner, they can use it under their own institutional licence.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-08-30, no releases or tags, SPDX NOASSERTION (actual: Magic Leap noncommercial academic agreement), 4,107 stars, 60 open issues. Over two years without activity from a corporate research lab; no indication of further work.

## 9. Licensing

**Licence:** NOT OSS — Magic Leap 'SOFTWARE LICENSE AGREEMENT: ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY' (licence blob read 2026-11-17; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same agreement covers the pretrained weights.

**Restrictions:** Commercial use prohibited. The agreement is explicitly between an academic institution or non-profit (or an individual acting as such) and Magic Leap. A commercially operated newsroom has no licence, and NGO status does not automatically qualify — read the agreement before assuming it does.

**Licence evidence:** https://github.com/magicleap/SuperGluePretrainedNetwork/blob/master/LICENSE

## 10. Costs

No fee for permitted academic/non-profit use; no commercial licence path is published. GPU for inference.

## 11. Privacy and data flows

Local inference, so case images stay on your machine — which is of little use given the licence position.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- Noncommercial academic-only licence — unusable by a commercial newsroom, and invisible to SPDX scanners

## 13. Alternatives

- [LoFTR](OSINT-C2-34.md) (Apache-2.0) — recommended permissive alternative for detector-free matching
- Hierarchical-Localization / hloc (Apache-2.0) for a full localisation pipeline, but verify which matcher weights you enable
- A university partner operating SuperGlue under their own institutional licence

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/magicleap/SuperGluePretrainedNetwork/blob/master/LICENSE
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

← 339. [blockhash-python](OSINT-C2-09.md) · 341. [X-FACT](JAI-A4-08.md) →
