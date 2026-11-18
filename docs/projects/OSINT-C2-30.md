# Pelias

`OSINT-C2-30` · **70/100** · overall rank 268 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 97) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 39) |
| **Subcategory** | Geocoding |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Pelias contributors (originally Mapzen) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/pelias/api) · [Documentation](https://pelias.io/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 70/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Mixed by source: OpenStreetMap is ODbL 1.0; OpenAddresses sources carry a range of per-source licences, some with attribution or redistribution conditions; Who's on First is CC-BY. These differ and must be checked per region you import. |
| **Restrictions** | Code is MIT. The data licensing is genuinely mixed and is the item needing attention: an OpenAddresses import can include sources whose terms restrict redistribution, so publishing a derived dataset requires per-source review. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Infrastructure estimate: several services plus Elasticsearch — realistically two or more VMs for a country-scale deployment, more operational attention than Photon. Assumptions: self-hosted, regional imports.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/pelias/api/blob/master/LICENSE
- https://github.com/pelias/api
- https://pelias.io/

---

## 1. Purpose

Modular open-source geocoder that blends multiple data sources — OpenStreetMap, OpenAddresses, Who's on First, geonames — behind a single API, with autocomplete and structured query support.

## Journalism / investigative use case

Geocoding where OSM alone is insufficient: blending OpenAddresses and other sources gives materially better address coverage in several countries, which matters when your dataset is national property or company registrations and Nominatim's coverage has gaps.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Multi-source blending is the architectural advantage: OpenAddresses in particular fills address gaps that OSM leaves, improving match rates on national registry data
- Structured query support (separate fields for street, city, postcode) materially improves accuracy over free-text geocoding of registry data
- MIT licensed with a modular design, so you can import only the sources relevant to your region
- Still maintained (v7.11.0, 2026-09-25; pushed 2026-10-21) after the original sponsor (Mapzen) wound down — a community continuation that survived

## 5. Cons

- Multi-service architecture (api, placeholder, pip, libpostal, Elasticsearch, importers) is the heaviest geocoding deployment of the three here — meaningfully more operational work than Photon
- Small community for the api repository (259 stars) with 137 open issues, and documentation is spread across many repositories, making orientation slow
- Blending sources introduces its own ambiguity: the same place can appear from several sources with different geometries, and deduplication quality varies
- Original corporate sponsor is gone, so long-term direction depends on a modest community — a continuity consideration for infrastructure you would run for years

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 259 stars with 137 open issues, release v7.11.0 (2026-09-25), pushed 2026-10-21, MIT licence. The project survived the shutdown of its original sponsor (Mapzen), which is itself evidence of community commitment, though the contributor base is modest.

## 7. Assessment

Choose it only when coverage genuinely requires multi-source blending — for example national address work in a country where OpenAddresses is strong and OSM is weak. Otherwise Photon is substantially less work for comparable results on dirty data. For your profile I would test match rates for your specific country on both before committing, since that empirical answer, not the architecture, determines which is right.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-21, latest release v7.11.0 (2026-09-25), 259 stars, 137 open issues. Recent release and commits, but a modest contributor base post-Mapzen and a substantial backlog across a multi-repository project. Stable rather than actively developed.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Mixed by source: OpenStreetMap is ODbL 1.0; OpenAddresses sources carry a range of per-source licences, some with attribution or redistribution conditions; Who's on First is CC-BY. These differ and must be checked per region you import.

**Restrictions:** Code is MIT. The data licensing is genuinely mixed and is the item needing attention: an OpenAddresses import can include sources whose terms restrict redistribution, so publishing a derived dataset requires per-source review.

**Licence evidence:** https://github.com/pelias/api/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure estimate: several services plus Elasticsearch — realistically two or more VMs for a country-scale deployment, more operational attention than Photon. Assumptions: self-hosted, regional imports.

## 11. Privacy and data flows

Self-hosted, so geocoding stays internal. Public demo instances see your queries.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Mixed data-source licensing requires per-source review before publishing derived datasets

## 13. Alternatives

- [Photon](OSINT-C1-20.md) for a lighter self-hosted geocoder with good typo tolerance
- [Nominatim](OSINT-C2-28.md) as the OSM reference implementation
- libpostal alone for address parsing if your bottleneck is normalisation rather than lookup

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/pelias/api
- https://pelias.io/
- https://github.com/pelias/api/blob/master/LICENSE

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

← 267. [Metabigor](OSINT-C1-09.md) · 269. [RDFLib](JAI-A3-16.md) →
