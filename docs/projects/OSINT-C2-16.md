# GeoCLIP

`OSINT-C2-16` · **79/100** · overall rank 167 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 55) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 25) |
| **Subcategory** | Image geolocation (model) |
| **Type** | model |
| **Bucket** | `verified-oss` |
| **Maintainer** | Vicente Vivanco Cepeda and collaborators |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/VicenteVivan/geo-clip) · [Documentation](https://github.com/VicenteVivan/geo-clip#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 79/100**

---

## 1. Purpose

CLIP-based model that predicts GPS coordinates for an image by aligning image embeddings with a learned location embedding space, returning ranked candidate locations.

## Journalism / investigative use case

Narrowing the search space when geolocating a photo with no metadata: GeoCLIP proposes candidate regions, which an investigator then confirms or rejects by matching buildings, signage, vegetation and terrain against satellite and street-level imagery. It replaces 'somewhere in the world' with 'check these three regions first'.

## 2. Audience

specialist investigator, engineer

## 3. Project type

model · bucket `verified-oss`

## 4. Pros

- Dramatically narrows the search space, which is the real bottleneck in manual geolocation — an investigator with three candidate regions can work; one with none cannot
- MIT licensed with pretrained weights distributed in the package, so there is no separate weights-licence trap
- Inference is local once installed, so case images need not be sent to a geolocation API — a significant privacy advantage over hosted services
- Actively maintained (v1.3.0 released 2026-10-25, same-day push)

## 5. Cons

- Produces a probabilistic guess over coordinates, NEVER a location fact or proof — and the README states no per-image accuracy figures, so you cannot quantify confidence for a specific photo
- Biased toward locations well represented in training data, which means tourist and urban scenes work far better than rural areas in under-photographed countries — precisely where much conflict reporting happens
- Benchmark accuracy says nothing about any individual image, and a confident-looking top candidate can be entirely wrong
- Narrow function: it proposes, it does not verify, so the labour-intensive confirmation step remains entirely manual

## 6. Feedback (documented)

No individual user reports verified. Documented: 420 stars with 9 open issues, release v1.3.0 on 2026-10-25 with same-day push, MIT licence with weights distributed in the package; the README's absence of per-image accuracy figures is itself the relevant disclosure.

## 7. Assessment

Adopt as a search-space-narrowing aid with a hard rule that its output never appears in a story as a location claim. For your profile the honest framing for reporters is: GeoCLIP tells you where to look, satellite and street-level imagery tell you where it is. Be especially sceptical of its output for rural locations in under-represented regions, which is where the training bias bites and where its confidence is least warranted.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-25, latest release v1.3.0 published the same day, 420 stars, 9 open issues. Recent release with a clean tracker; research-origin project sustaining a release cadence.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Not separately stated; pretrained weights are distributed with the MIT-licensed package.

**Restrictions:** None identified. Note the model derives from CLIP, whose own terms flow through in principle — worth checking if you redistribute weights.

**Licence evidence:** https://github.com/VicenteVivan/geo-clip/blob/main/LICENSE

## 10. Costs

No fee. PyTorch plus CLIP backbone; GPU helpful. Weights download on first use. Estimate.

## 11. Privacy and data flows

Inference is local once installed, so case images need not be sent to a geolocation API — the decisive advantage over hosted image-geolocation services, which would receive your unpublished imagery.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [ShadowFinder](OSINT-C2-17.md) for shadow-based chronolocation when a shadow and timestamp are visible
- Manual geolocation against satellite imagery and Mapillary/street-level panoramas
- [LoFTR](OSINT-C2-34.md) or hloc for feature-matching a candidate location against reference imagery

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/VicenteVivan/geo-clip
- https://github.com/VicenteVivan/geo-clip/blob/main/LICENSE

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

← 166. [Argos Translate](JAI-A2-03.md) · 168. [Open Contracting Data Standard](SUR-B2-18.md) →
