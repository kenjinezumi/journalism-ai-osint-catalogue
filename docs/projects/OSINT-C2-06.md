# ThreatExchange (PDQ / TMK+PDQF / vPDQ and HMA)

`OSINT-C2-06` · **78/100** · overall rank 177 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 57) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 27) |
| **Subcategory** | Perceptual hashing at scale |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Meta (repository transferred from facebook/ThreatExchange) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause (repository LICENSE; README notes pdq/cpp/CImg.h carries its own separate licence and tmk/LICENSE.txt is BSD-2-Clause) — GitHub reports NOASSERTION |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/meta/ThreatExchange) · [Documentation](https://github.com/meta/ThreatExchange#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 78/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-3-Clause (repository LICENSE; README notes pdq/cpp/CImg.h carries its own separate licence and tmk/LICENSE.txt is BSD-2-Clause) — GitHub reports NOASSERTION |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a. Hash banks you obtain from partners carry their own terms. |
| **Restrictions** | Mixed sub-licences mean a per-directory review is needed before redistribution. The CImg dependency in the C++ PDQ implementation is the specific item to check, since CImg's own licence is not BSD. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. FFmpeg 4.1+ recommended for video hashing; optional OpenMP and FAISS. HMA implies container or cloud infrastructure — a small service for newsroom volumes. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/meta/ThreatExchange/blob/main/LICENSE
- https://github.com/meta/ThreatExchange
- `../sources/evidence/leads.md`

---

## 1. Purpose

Collection of production perceptual-hashing algorithms (PDQ for images, TMK+PDQF and vPDQ for video) plus Hasher-Matcher-Actioner, a deployable service for hashing and matching media against hash banks.

## Journalism / investigative use case

Industry-standard hashing for a collaborative or newsroom-scale image and video corpus: hash incoming media and match against a bank of previously verified or previously debunked content, including across organisations. TMK+PDQF in particular makes video-level matching practical, which is how you trace a clip's spread across platforms.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- PDQ is materially more robust than classic perceptual hashes to cropping, overlays and recompression — the transformations media actually undergoes in circulation
- Video hashing (TMK+PDQF, vPDQ) addresses a real gap: almost nothing else open lets you match video at scale
- Hasher-Matcher-Actioner provides a deployable service rather than just algorithms, with releases (hma-v1.2.2, 2026-11-04) and active development
- BSD-3-Clause on the repository, so the algorithms are freely usable — note the pdq/cpp/CImg.h and tmk/LICENSE.txt sub-licences called out in the README

## 5. Cons

- These are near-duplicate matching tools, NOT manipulation or AI-generation detectors: a match means 'substantially the same media as something in the bank' and says nothing about authenticity — a distinction that is persistently misunderstood
- Video hashing degrades under re-encoding and editing, so matching across platform re-uploads is imperfect
- GitHub reports SPDX NOASSERTION because of the mixed sub-licences, so a compliance review needs the per-directory detail rather than a single label
- HMA deployment implies container or cloud infrastructure; connecting a signal-exchange API means exchanging hashes with a third party under partner terms

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,411 stars with 58 open issues, release hma-v1.2.2 (2026-11-04), pushed 2026-11-09; the repository transfer facebook/ThreatExchange → meta/ThreatExchange was confirmed by API redirect on 2026-11-17. PDQ is widely used in industry content-matching, which is the relevant production context.

## 7. Assessment

The right hashing foundation for a newsroom that handles media at volume or collaborates across organisations — PDQ for images, vPDQ for video, and HMA only if the volume justifies a service. For your profile the critical governance point is bank hygiene: a hash bank of 'previously debunked' content is an editorial asset that must be curated, because an incorrect entry silently mislabels future media. Keep hashing local and treat any hash exchange with a platform as a separate decision with its own terms.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-09, latest release hma-v1.2.2 (2026-11-04), SPDX NOASSERTION (BSD-3-Clause repository licence with separate sub-licences), 1,411 stars, 58 open issues. Current releases under corporate maintenance; transfer from the facebook org confirmed.

## 9. Licensing

**Licence:** BSD-3-Clause (repository LICENSE; README notes pdq/cpp/CImg.h carries its own separate licence and tmk/LICENSE.txt is BSD-2-Clause) — GitHub reports NOASSERTION _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Hash banks you obtain from partners carry their own terms.

**Restrictions:** Mixed sub-licences mean a per-directory review is needed before redistribution. The CImg dependency in the C++ PDQ implementation is the specific item to check, since CImg's own licence is not BSD.

**Licence evidence:** https://github.com/meta/ThreatExchange/blob/main/LICENSE

## 10. Costs

No fee. FFmpeg 4.1+ recommended for video hashing; optional OpenMP and FAISS. HMA implies container or cloud infrastructure — a small service for newsroom volumes. Estimate.

## 11. Privacy and data flows

Hashing and local matching need no network. Connecting an exchange API sends and receives hashes (not images) with a third party under partner terms — a deliberate decision, and note that a hash still reveals that you hold a matching image.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [ImageHash](OSINT-C2-05.md) for simpler local image hashing
- [imagededup](OSINT-C2-07.md) for corpus-scale deduplication
- [pHash](OSINT-C2-08.md) where audio or video fingerprinting with a different algorithm is wanted

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/meta/ThreatExchange
- https://github.com/meta/ThreatExchange/blob/main/LICENSE
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

← 176. [PyBGPStream / libbgpstream](SUR-B1-08.md) · 178. [git-history](JAI-A1-32.md) →
