# LoFTR

`OSINT-C2-34` · **66/100** · overall rank 286 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 105) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 41) |
| **Subcategory** | Image feature matching |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | ZJU3DV (Zhejiang University) |
| **Maintenance** | Dormant |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/zju3dv/LoFTR) · [Documentation](https://zju3dv.github.io/loftr/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 1/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 66/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Apache-2.0 per the repository; weights published by the authors under the same terms. |
| **Restrictions** | None identified — the key contrast with SuperGlue. Verify the specific weights file you download, since research repositories occasionally distribute additional checkpoints under different terms. |
| **Open-source status** | **Open source** — Open model weights |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. GPU needed for practical throughput; weights are a modest download. Engineering time to containerise and integrate is the real cost. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/zju3dv/LoFTR/blob/master/LICENSE
- https://github.com/zju3dv/LoFTR
- https://zju3dv.github.io/loftr/

---

## 1. Purpose

Detector-free local feature matching using transformers, establishing dense correspondences between two images without first detecting keypoints, which works better on low-texture surfaces.

## Journalism / investigative use case

The permissively licensed route to confirming a geolocation hypothesis by matching a photograph against a panorama or satellite image. Detector-free matching is particularly useful on the low-texture surfaces common in built environments — plain walls, roads, fields — where keypoint detectors find nothing.

## 2. Audience

specialist investigator, engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- Apache-2.0 for both code and the published weights, which makes it the commercially usable alternative to SuperGlue — the single most important property for your context
- Detector-free design handles low-texture scenes better than keypoint-based matchers, which is a real advantage on building façades and open ground
- Matching output is visually explainable: you can show an editor the correspondence lines between two images, which is persuasive and checkable

## 5. Cons

- Dormant: last push 2024-05-31, no releases, 95 open issues against 2,981 stars — over two years without maintenance, and the dependency stack of that period will need pinning
- Research code rather than a tool: no CLI ergonomics, and integrating it into a repeatable workflow is engineering work
- Correspondence quality degrades with large viewpoint or seasonal differences, and a confident-looking match set can still be wrong — it is evidence to be assessed, not proof
- GPU effectively required for practical use, and inference on many candidate pairs is slow

## 6. Feedback (documented)

No individual user reports verified. Documented: 2,981 stars with 95 open issues, no releases, last push 2024-05-31, Apache-2.0 per the GitHub API. Its standing as a leading detector-free matcher is established in the computer-vision literature; the Apache-2.0 position is the practically decisive fact here.

## 7. Assessment

The matcher I would use, on licence grounds, despite the dormancy — and the dormancy is tolerable because the weights and method are fixed artefacts rather than a service. For your profile the sensible approach is to containerise it once with pinned dependencies and treat it as a stable internal capability. Present output as a correspondence analysis supporting a geolocation, with the match visualisation published alongside the claim so readers can judge it.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2024-05-31, no releases or tags, 95 open issues, 2,981 stars, Apache-2.0. Over two years without commits. Mitigated by the nature of the artefact: fixed weights plus a research implementation degrade only through dependency rot, which pinning addresses.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** Apache-2.0 per the repository; weights published by the authors under the same terms.

**Restrictions:** None identified — the key contrast with SuperGlue. Verify the specific weights file you download, since research repositories occasionally distribute additional checkpoints under different terms.

**Licence evidence:** https://github.com/zju3dv/LoFTR/blob/master/LICENSE

## 10. Costs

No fee. GPU needed for practical throughput; weights are a modest download. Engineering time to containerise and integrate is the real cost. Estimate.

## 11. Privacy and data flows

Local inference — case images and reference panoramas stay on your machine, which matters because the alternative (a hosted matching service) would receive both.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Dormant since mid-2024 — pin dependencies and expect to own maintenance

## 13. Alternatives

- [Hierarchical-Localization (hloc)](OSINT-C2-35.md) for a full pipeline, checking which matcher weights it pulls
- SuperGlue — avoid: noncommercial licence
- Manual visual comparison, which remains the fallback and is what the match analysis supports rather than replaces

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/zju3dv/LoFTR
- https://zju3dv.github.io/loftr/
- https://github.com/zju3dv/LoFTR/blob/master/LICENSE

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

← 285. [Montreal Forced Aligner](JAI-A2-29.md) · 287. [imagededup](OSINT-C2-07.md) →
