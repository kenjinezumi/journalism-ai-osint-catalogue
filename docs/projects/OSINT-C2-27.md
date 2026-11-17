# osm-search

`OSINT-C2-27` · **87/100** · overall rank 60 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 20) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 7) |
| **Subcategory** | Feature-based geolocation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/osm-search) · [Documentation](https://osm-search.bellingcat.com/) |
| **Also known as** | Bellingcat OSM Search |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 3/5 · privacy 4/5 · usability 5/5 · licence+cost 5/5 → **weighted 87/100**

---

## 1. Purpose

Tool that searches OpenStreetMap for combinations of features in proximity to each other, returning candidate locations where the specified features all occur nearby.

## Journalism / investigative use case

The core feature-based geolocation workflow made usable: a photograph shows a church, a football pitch and a water tower, so you search for places where all three occur within a given radius and get a shortlist of candidate locations to check against satellite imagery.

## 2. Audience

journalist, newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Implements exactly the technique practising geolocation investigators use, with an interface a non-engineer can operate — removing the Overpass QL barrier entirely
- Proximity-combination search is the highest-leverage geolocation method available for photographs with identifiable landmarks, and this is the most accessible implementation of it
- MIT licensed and built by Bellingcat, whose investigators use these methods daily
- Self-hostable, so the queries (and hence the case) need not go to a third party

## 5. Cons

- Results depend entirely on OSM tagging completeness: a water tower that nobody mapped will not be found, and in under-mapped regions the method degrades sharply — which is where conflict reporting often is
- Candidate lists still require manual verification against imagery, so it narrows rather than solves — and a confident shortlist can anchor an investigator on a wrong region
- Small project (217 stars, 11 open issues) with no releases and last push 2026-07-07, so it is maintained at low velocity
- Using the hosted version discloses the feature combination you are searching for, which is a meaningful hint about your case

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 217 stars with 11 open issues, no releases, last push 2026-07-07, MIT licence. The feature-proximity geolocation method it implements is extensively documented in Bellingcat's published investigations, which is strong contextual evidence that the technique works.

## 7. Assessment

Adopt — and self-host it if geolocation work is routine for you, both for privacy and because the hosted instance is a dependency. For your profile the realistic expectation is that it works well in Europe and well-mapped regions and poorly where OSM coverage is thin; in those areas the fallback is manual satellite survey of plausible regions, informed by GeoCLIP. Always treat the shortlist as hypotheses and verify each against imagery before narrowing.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-07-07, no releases or tags, 217 stars, 11 open issues. Four months since last push on a small focused tool from an institutional maintainer; functionally complete rather than abandoned.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** OpenStreetMap data is ODbL 1.0.

**Restrictions:** None on the code; ODbL obligations attach to published derived OSM datasets.

**Licence evidence:** https://github.com/bellingcat/osm-search/blob/main/LICENSE

## 10. Costs

No fee. Self-hosting needs an Overpass instance or access to one — the real infrastructure consideration. Estimate.

## 11. Privacy and data flows

The hosted version discloses your searched feature combinations to the operator and to the Overpass instance behind it. Self-hosting with your own Overpass keeps the case private.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [overpass-turbo](OSINT-C2-24.md) for hand-written equivalent queries
- [GeoCLIP](OSINT-C2-16.md) to narrow the region before feature search
- Manual satellite survey where OSM coverage is inadequate

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/bellingcat/osm-search
- https://osm-search.bellingcat.com/
- https://github.com/bellingcat/osm-search/blob/main/LICENSE

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
| 8 | [GDAL](OSINT-C2-20.md) | 86 | Adopt |
| 9 | [rasterio](OSINT-C2-22.md) | 86 | Adopt |

---

← 59. [OpenRefine](JAI-A2-36.md) · 61. [SecureDrop Workstation](SUR-B3-02.md) →
