# blockhash-python

`OSINT-C2-09` · **54/100** · overall rank 339 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 133) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 49) |
| **Subcategory** | Perceptual hashing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Commons Machinery |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/commonsmachinery/blockhash-python) · [Documentation](https://github.com/commonsmachinery/blockhash-python#readme) |

**Scores** — relevance 2/5 · capability 2/5 · maintenance 1/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 54/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python implementation of the blockhash perceptual-hashing algorithm, which divides an image into blocks and derives a hash from block median values.

## Journalism / investigative use case

A simple, dependency-light hash for deduplicating image sets where a documented, interoperable algorithm matters more than peak accuracy — for example when two organisations need to compare hashes and must agree on the exact algorithm.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- The algorithm is simply and publicly specified, so hashes are reproducible across independent implementations — useful for cross-organisation comparison where PDQ's complexity is a barrier
- Minimal dependencies (Pillow only) and short enough to read in full, which makes it auditable
- MIT licensed with no restrictions at all

## 5. Cons

- Dormant: last push 2023-10-31, no releases, 131 stars — three years without activity
- Superseded in practice by ImageHash and PDQ; blockhash is less robust than PDQ to cropping and overlays, which is the condition that matters
- Similarity signal only, with all the usual caveats about hashes proving nothing about authenticity
- Tiny community means no support and no ecosystem

## 6. Feedback (documented)

No individual user reports verified. Documented: 131 stars with 4 open issues, no releases, last push 2023-10-31, MIT licence.

## 7. Assessment

Hard to justify today: ImageHash covers the same ground with more algorithms and active maintenance, and PDQ is better where robustness matters. The one scenario where blockhash earns its place is cross-organisation interoperability with a partner who has already implemented it — the specification's simplicity is its only remaining advantage. For your profile I would default to PDQ and ImageHash.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2023-10-31, no releases or tags, 131 stars, 4 open issues. Three years without activity. Low practical risk given the trivial dependency surface, but no reason to choose it.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/commonsmachinery/blockhash-python/blob/master/LICENSE

## 10. Costs

No fee, negligible resources.

## 11. Privacy and data flows

Entirely local.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Dormant since 2023 and superseded by better-maintained alternatives

## 13. Alternatives

- [ImageHash](OSINT-C2-05.md) — recommended: more algorithms, maintained
- ThreatExchange PDQ for robustness to crops and overlays
- [imagededup](OSINT-C2-07.md) for corpus-scale deduplication

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/commonsmachinery/blockhash-python
- https://github.com/commonsmachinery/blockhash-python/blob/master/LICENSE

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

← 338. [wpull](OSINT-C1-25.md) · 340. [SuperGlue (pretrained network)](OSINT-C2-33.md) →
