# python-overpy

`OSINT-C2-25` · **75/100** · overall rank 210 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 68) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 30) |
| **Subcategory** | OpenStreetMap querying |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | DinoTools |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/DinoTools/python-overpy) · [Documentation](https://python-overpy.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 75/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | OpenStreetMap data is ODbL 1.0. |
| **Restrictions** | None on the code; ODbL obligations attach to published derived databases. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Negligible compute. Public Overpass instances are free but rate-limited; a local instance is the cost consideration.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/DinoTools/python-overpy/blob/master/LICENSE
- https://github.com/DinoTools/python-overpy
- https://python-overpy.readthedocs.io/

---

## 1. Purpose

Python wrapper for the Overpass API that submits queries and parses the response into typed node, way and relation objects.

## Journalism / investigative use case

Scripted, repeatable OSM queries inside an investigation pipeline — for example iterating a list of 200 claimed incident coordinates and extracting the nearby tagged features for each, which is impractical by hand in overpass-turbo.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Typed result objects remove the tedious JSON parsing that otherwise clutters OSM scripts
- MIT licensed, small, and simple enough to read entirely — easy to audit and to replace if needed
- Still maintained (pushed 2026-11-02), which is reassuring given that its upstream Overpass API has slowed
- Works against any Overpass instance including your own, so the privacy decision is yours

## 5. Cons

- No release objects (latest tag 0.7), so pinning relies on tags or PyPI versions rather than release notes
- Inherits Overpass API rate limits and availability, so batch work against a public instance will be throttled and should not be relied on for deadline work
- Thin wrapper: it adds convenience, not capability, and you still need to write Overpass QL
- Small community (266 stars, 29 open issues) with limited examples for investigative patterns

## 6. Feedback (documented)

No individual user reports verified. Documented: 266 stars with 29 open issues, no releases, latest tag 0.7, last push 2026-11-02, MIT licence.

## 7. Assessment

Integrate it for scripted OSM work, pointed at your own Overpass instance rather than a public one if the coordinates are sensitive. For your profile the batch pattern — iterate coordinates, extract nearby features, score candidate matches against what a photograph shows — is a genuinely strong semi-automated geolocation approach, and this library is the simplest way to build it. Plan around rate limits by running against a local extract.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-02, no releases, latest tag 0.7, 266 stars, 29 open issues. Recent commits on a small, feature-complete wrapper; low velocity is appropriate to its scope.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** OpenStreetMap data is ODbL 1.0.

**Restrictions:** None on the code; ODbL obligations attach to published derived databases.

**Licence evidence:** https://github.com/DinoTools/python-overpy/blob/master/LICENSE

## 10. Costs

No fee. Negligible compute. Public Overpass instances are free but rate-limited; a local instance is the cost consideration.

## 11. Privacy and data flows

Queries go to whichever Overpass instance you configure — public instances see your coordinates, your own instance does not.

## 12. Verdict

**Integrate**

## 13. Alternatives

- OSMPythonTools for a richer but GPL-3.0 and slower-moving alternative
- Direct HTTP requests to Overpass, which is barely harder
- [OSMnx](OSINT-C2-26.md) where the target is street networks rather than arbitrary features

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/DinoTools/python-overpy
- https://python-overpy.readthedocs.io/
- https://github.com/DinoTools/python-overpy/blob/master/LICENSE

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

← 209. [libratom](JAI-A1-13.md) · 211. [Ragas](JAI-A3-13.md) →
