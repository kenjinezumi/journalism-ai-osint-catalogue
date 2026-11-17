# meteostat

`OSINT-C2-40` · **86/100** · overall rank 80 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 25) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 11) |
| **Subcategory** | Historical weather data |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Meteostat |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/meteostat/meteostat) · [Documentation](https://dev.meteostat.net/python/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 5/5 · privacy 5/5 · usability 5/5 · licence+cost 5/5 → **weighted 86/100**

---

## 1. Purpose

Python library providing access to historical weather and climate observations from thousands of stations worldwide, with hourly, daily and monthly aggregation.

## Journalism / investigative use case

Weather-based verification and falsification: check whether it was raining, snowing or clear at the claimed place and time of a photograph or video. Wet ground in a clip said to be from a day with no recorded precipitation within 50km is a concrete inconsistency, and dry ground on a day of heavy rain is equally telling.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Weather is an independent, record-based constraint on imagery claims — stronger than any model-based detection and checkable by a reader against the same public records
- Global station coverage with a simple Python interface, so a check takes a few lines rather than navigating a meteorological agency's portal
- MIT licensed with active maintenance (v2.2.3 released 2026-11-11, same-day push) and a very clean tracker (10 open issues)
- Repository renamed from meteostat-python to meteostat (transfer verified by redirect), so the canonical path is current

## 5. Cons

- Station coverage is sparse in exactly the regions where verification is often hardest, and interpolating between distant stations weakens the inference considerably
- Local weather can diverge sharply from the nearest station — a convective shower is kilometres wide — so 'no recorded rain' is weaker evidence than it appears
- Hourly data availability varies by station and era, so historical checks in some regions return daily aggregates only
- Small project (669 stars) dependent on upstream agency data pipelines whose continuity is outside its control

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 669 stars with 10 open issues, release v2.2.3 on 2026-11-11 with same-day push, MIT licence; repository transfer meteostat/meteostat-python → meteostat/meteostat confirmed by API redirect on 2026-11-17.

## 7. Assessment

Adopt as a routine verification check — it is cheap, independent and based on records a reader can inspect. For your profile the honest framing in published work is to name the station, its distance from the claimed location, and the measurement interval, because that lets the reader judge the inference. Treat a near-station match as corroboration and a mismatch as a question to put to the source rather than a conclusion, unless the distance is small and the weather event large.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-11, latest release v2.2.3 published the same day, 669 stars, 10 open issues. Frequent releases and a near-empty tracker; the project also operates a hosted bulk-data interface.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Underlying observations come from national meteorological services (NOAA, DWD and others) under their own terms; Meteostat documents the sources and their licences.

**Restrictions:** Code permissive. Check the source agency's attribution requirements before republishing observation data as a dataset; most require attribution.

**Licence evidence:** https://github.com/meteostat/meteostat/blob/main/LICENSE

## 10. Costs

No fee for the library and bulk data. Negligible compute. Meteostat offers a hosted API with paid tiers for higher volume — prices not verified in this survey.

## 11. Privacy and data flows

Bulk data access and local computation disclose nothing about your case. Using the hosted API sends your station and date queries to Meteostat, which weakly indicates your area of interest.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [wetterdienst](OSINT-C2-42.md) for direct access to European national weather services with finer granularity
- [Open-Meteo](OSINT-C2-41.md) for a simpler API including historical reanalysis
- National meteorological agency archives directly, which carry more authority for a published claim

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/meteostat/meteostat
- https://dev.meteostat.net/python/
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

← 79. [feedparser](JAI-A1-07.md) · 81. [OONI Probe CLI / probe-engine](SUR-B1-01.md) →
