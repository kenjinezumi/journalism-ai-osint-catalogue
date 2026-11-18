# ImageHash

`OSINT-C2-05` · **78/100** · overall rank 179 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 58) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 28) |
| **Subcategory** | Perceptual hashing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Johannes Buchner |
| **Maintenance** | Stable with low activity |
| **Licence** | BSD-2-Clause |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/JohannesBuchner/imagehash) · [Documentation](https://github.com/JohannesBuchner/imagehash#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-2-Clause |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU only; negligible. Storage for the hash index is trivial relative to the images.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/JohannesBuchner/imagehash/blob/master/LICENSE
- https://github.com/JohannesBuchner/imagehash

---

## 1. Purpose

Python library implementing classic perceptual hashes — average, perceptual (DCT), difference, wavelet and colour hashes — for comparing images by visual similarity.

## Journalism / investigative use case

Build an in-house index of images you have already seen or debunked, then test whether a newly circulating image is a re-post, a crop or a lightly edited variant — the local alternative to pasting a sensitive image into a commercial reverse-image service, which would disclose it.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Keeps reverse-image comparison entirely in-house, which is the decisive property when the image is source-supplied and must not be uploaded to Google or Yandex
- Several hash algorithms with different robustness profiles, so you can compare and choose rather than trusting one
- Tiny dependency surface (Pillow, NumPy, SciPy) and simple enough to audit fully
- Large user base (3,887 stars) with a modest backlog (29 open issues)

## 5. Cons

- A hash match is a probabilistic similarity signal, not provenance and not proof — it says two files look alike, not which came first or whether either is authentic
- Classic perceptual hashes degrade under cropping, overlays, heavy recompression and rotation, which is exactly what happens to images in circulation — PDQ is more robust
- Release metadata is confusing: the GitHub release object is v4.1.0 (2021-03-25) while the current tag is v4.3.2, so pinning requires care
- No index or storage layer — you build the matching infrastructure around it

## 6. Feedback (documented)

No individual user reports verified. Documented: 3,887 stars with 29 open issues, release object v4.1.0 (2021-03-25) against tag v4.3.2, last push 2026-10-12. The release/tag divergence is visible in the API and is a genuine pinning annoyance.

## 7. Assessment

Adopt for the in-house image index — the privacy argument makes it clearly preferable to commercial reverse search for unpublished material. For your profile I would use PDQ (from ThreatExchange) as the primary hash because of its robustness to crops and overlays, and keep ImageHash for its algorithm variety and simplicity. Store hashes with the provenance of each image, since the index's value is knowing where you saw something first.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-12, release object v4.1.0 (2021-03-25), latest tag v4.3.2, 3,887 stars, 29 open issues. Commits within the last month but release engineering has lapsed; a mature library at low velocity.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/JohannesBuchner/imagehash/blob/master/LICENSE

## 10. Costs

No fee. CPU only; negligible. Storage for the hash index is trivial relative to the images.

## 11. Privacy and data flows

Local only; no external service required. The index itself is a record of what your newsroom has examined, so protect it accordingly.

## 12. Verdict

**Adopt**

## 13. Alternatives

- ThreatExchange PDQ for crop- and overlay-robust hashing at scale
- [imagededup](OSINT-C2-07.md) for corpus deduplication with CNN embeddings as an option
- [blockhash-python](OSINT-C2-09.md) where a documented interoperable algorithm matters more than accuracy

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/JohannesBuchner/imagehash
- https://github.com/JohannesBuchner/imagehash/blob/master/LICENSE

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

← 178. [git-history](JAI-A1-32.md) · 180. [RSS-Bridge](JAI-A1-06.md) →
