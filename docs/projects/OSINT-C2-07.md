# imagededup

`OSINT-C2-07` · **66/100** · overall rank 287 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 106) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 42) |
| **Subcategory** | Image deduplication |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | idealo |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | Apache-2.0 |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/idealo/imagededup) · [Documentation](https://idealo.github.io/imagededup/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 66/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | Apache-2.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | CNN method uses pretrained weights fetched on first use; their licences were not individually verified in this survey. |
| **Restrictions** | Code permissive. Verify the CNN backbone's weights licence if you use that method commercially. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU sufficient for hashing; GPU optional and only helpful for CNN embeddings. Model weights fetched once. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/idealo/imagededup/blob/master/LICENSE
- https://github.com/idealo/imagededup
- https://idealo.github.io/imagededup/

---

## 1. Purpose

Python library for finding duplicate and near-duplicate images using either perceptual hashing or CNN embeddings, with evaluation tooling for threshold selection.

## Journalism / investigative use case

Deduplicate a large scraped image corpus before manual review, collapsing thousands of reposts into unique images so analyst time goes to genuinely new material — the image equivalent of datasketch's role in document triage.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Offers both hashing and CNN-embedding methods with evaluation tooling, so you can measure the trade-off on your own corpus rather than guessing a threshold
- Solves the actual bottleneck in image-corpus work, which is analyst attention rather than compute
- Apache-2.0 with reasonable documentation and a substantial user base (5,686 stars)
- Threshold evaluation support is unusual and genuinely useful — most dedup tools leave you to guess

## 5. Cons

- Duplicate groupings are similarity judgements requiring a tuned threshold; an untuned run will either merge distinct images or miss obvious reposts
- CNN embeddings cluster semantically similar but distinct images — two different protests look alike to the model — which is wrong for forensic identity and is the most common misuse
- Development has slowed: release v0.3.3.post2 and last push both 2025-08-15, fifteen months before this survey
- Deep-learning runtime needed for the CNN method, which is a heavy dependency for what is otherwise a simple library

## 6. Feedback (documented)

No individual user reports verified. Documented: 5,686 stars with 39 open issues, release v0.3.3.post2 (2025-08-15) with the last push the same day — a project that stopped cleanly at a release rather than drifting. The semantic-clustering behaviour of CNN embeddings is a documented property of the method, not a defect.

## 7. Assessment

Use the hashing method for forensic identity and avoid the CNN method for that purpose — use CNN embeddings only when you deliberately want semantic grouping (for example 'show me all the protest photos'). For your profile the dormancy is tolerable because the hashing path has essentially no dependency rot risk, but if you need the CNN path I would build it on sentence-transformers-style embeddings you control instead, so the model choice is explicit.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2025-08-15, latest release v0.3.3.post2 published the same day, 5,686 stars, 39 open issues. Fifteen months with no activity following a release; a corporate open-source project that appears to have been set aside. Declining rather than dormant given the clean final release.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** CNN method uses pretrained weights fetched on first use; their licences were not individually verified in this survey.

**Restrictions:** Code permissive. Verify the CNN backbone's weights licence if you use that method commercially.

**Licence evidence:** https://github.com/idealo/imagededup/blob/master/LICENSE

## 10. Costs

No fee. CPU sufficient for hashing; GPU optional and only helpful for CNN embeddings. Model weights fetched once. Estimate.

## 11. Privacy and data flows

Local processing; model weights fetched once from a third-party host. Images are not uploaded.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [ImageHash](OSINT-C2-05.md) plus your own index for a simpler, maintained hashing path
- ThreatExchange PDQ for more robust hashing at scale
- [Bellingcat smart-image-sorter](OSINT-C2-15.md) where semantic grouping is actually what you want

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/idealo/imagededup
- https://idealo.github.io/imagededup/
- https://github.com/idealo/imagededup/blob/master/LICENSE

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

← 286. [LoFTR](OSINT-C2-34.md) · 288. [pHash](OSINT-C2-08.md) →
