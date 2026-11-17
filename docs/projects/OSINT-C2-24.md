# overpass-turbo

`OSINT-C2-24` · **71/100** · overall rank 260 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 91) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 36) |
| **Subcategory** | OpenStreetMap querying |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Martin Raifer (tyrasd) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (licence blob read 2026-11-17, which notes bundled libraries have their own licences; GitHub reports NOASSERTION) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/tyrasd/overpass-turbo) · [Documentation](https://overpass-turbo.eu/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 2/5 · usability 5/5 · licence+cost 5/5 → **weighted 71/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Web-based interactive development environment for Overpass API queries, with a map view, query wizard, syntax highlighting and result export to GeoJSON, GPX and KML.

## Journalism / investigative use case

The practical way to develop a feature-based geolocation query: use the wizard to build 'all water towers in this bounding box', see results on the map immediately, refine, then export the candidates as GeoJSON for comparison against the photograph.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Interactive map feedback makes the Overpass query language learnable, which it is not from documentation alone — this is the tool that makes OSM querying accessible to a non-engineer
- The query wizard translates plain descriptions into Overpass QL, lowering the barrier substantially for one-off investigative queries
- Export to GeoJSON/KML means results flow straight into QGIS or a map for visual comparison
- MIT licensed (resolved in this session — GitHub reports NOASSERTION) and still maintained (pushed 2026-10-25)

## 5. Cons

- Using the public overpass-turbo.eu instance sends your queries and bounding boxes to that service, disclosing exactly which locations you are investigating — the same exposure as public Overpass instances
- No release objects at all (latest tag dated 2020-01-07) and 262 open issues against 1,269 stars, so versioning is informal and the backlog is substantial
- Depends on the Overpass API, which is itself showing declining maintenance — a two-layer dependency risk
- Browser-based with large result sets causing performance problems; it is a development tool rather than a batch interface

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,269 stars with 262 open issues, no releases, latest tag dated 2020-01-07, last push 2026-10-25; licence resolved to MIT by reading the blob, which also notes bundled libraries carry their own licences.

## 7. Assessment

Adopt for query development, then move the finished query to a private path for the actual work — that two-step is the privacy-preserving pattern. For your profile: develop interactively on the public instance using an innocuous nearby area, then run the real query against your own Overpass instance or a local extract so the genuine coordinates never reach a third party. The tool's value is pedagogical and exploratory, and it is excellent at that.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-25, no release objects, latest tag dated 2020-01-07, SPDX NOASSERTION (MIT per the licence blob), 1,269 stars, 262 open issues. Commits within the last month but no release engineering since 2020; a widely used tool maintained at minimal velocity.

## 9. Licensing

**Licence:** MIT (licence blob read 2026-11-17, which notes bundled libraries have their own licences; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** OpenStreetMap data is ODbL 1.0.

**Restrictions:** MIT on the application. ODbL obligations attach to exported OSM data if you publish a derived database.

**Licence evidence:** https://github.com/tyrasd/overpass-turbo/blob/gh-pages/LICENSE

## 10. Costs

No fee. The public instance is free and rate-limited; self-hosting the front end is a static deployment.

## 11. Privacy and data flows

Queries on the public instance are visible to that service and to the Overpass instance behind it, disclosing your area of interest. Self-host the front end and point it at your own Overpass instance for private work.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Public instance discloses queries and bounding boxes

## 13. Alternatives

- bellingcat/osm-search for a purpose-built journalistic proximity search
- [python-overpy](OSINT-C2-25.md) or OSMPythonTools for scripted querying
- A local OSM extract in PostGIS for fully private querying

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/tyrasd/overpass-turbo
- https://overpass-turbo.eu/

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

← 259. [kuroi](JAI-A4-24.md) · 261. [webappanalyzer](SUR-B2-07.md) →
