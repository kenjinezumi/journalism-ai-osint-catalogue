# wetterdienst

`OSINT-C2-42` · **80/100** · overall rank 159 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 53) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 24) |
| **Subcategory** | Weather data access |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | earthobservations |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/earthobservations/wetterdienst) · [Documentation](https://wetterdienst.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 80/100**

---

## 1. Purpose

Python library providing a unified interface to open weather and climate data from many national and international providers, including DWD, NOAA, ECCC, IMGW and others, with station metadata and interpolation.

## Journalism / investigative use case

Authoritative weather verification from the originating national service rather than an aggregator — which matters when a published claim will be challenged, because citing the national meteorological agency's own record is far stronger than citing a third-party API.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Goes to the national services directly, so your citation is the authoritative record — the decisive advantage for a contested published claim
- Unified interface across many providers removes the need to learn each agency's idiosyncratic portal and format, which is otherwise days of work per country
- MIT licensed with exceptionally active maintenance (v0.191.0 released 2026-11-17, same-day push)
- Includes station metadata and interpolation helpers, so you can report distance-to-station honestly

## 5. Cons

- Very high version number with frequent releases (v0.191.0) suggests a rapidly moving API, so pinning is essential and upgrades may break your code
- Provider coverage is strongest for Germany (DWD) and uneven elsewhere, reflecting its origins — check your region before relying on it
- 63 open issues and a small community (457 stars), so you will read source for unusual providers
- Each provider's data model differs underneath the unified interface, so results are not always directly comparable across countries

## 6. Feedback (documented)

No individual user reports verified — 457 stars means limited community signal. Documented: release v0.191.0 on 2026-11-17 with same-day push, 63 open issues, MIT licence. The very high minor version indicates a long sequence of small releases rather than instability per se.

## 7. Assessment

The right choice when the weather claim matters enough to need the national service's own record — which, for a contested verification, it usually does. For your profile I would use meteostat for quick triage and wetterdienst for anything heading to publication, pinning the version because the release cadence is brisk. Report the station identifier, distance and interval in the story so the reader can verify independently.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v0.191.0 published the same day, 457 stars, 63 open issues. Same-day release and push with a very high release count; unambiguously active, with API churn as the trade-off.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Each national service's data carries its own terms; DWD and NOAA data are generally open with attribution, others vary.

**Restrictions:** Code permissive. Per-provider data terms apply to republication — check the specific agency before publishing a derived dataset.

**Licence evidence:** https://github.com/earthobservations/wetterdienst/blob/main/LICENSE

## 10. Costs

No fee. Negligible compute; some providers' bulk downloads are large. No paid dependencies.

## 11. Privacy and data flows

Requests go to the national services, which see your station and date queries — a weak indication of your area of interest and generally unproblematic.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [meteostat](OSINT-C2-40.md) for faster, simpler station access
- [Open-Meteo](OSINT-C2-41.md) for reanalysis coverage where no station exists
- Direct agency portals for a one-off query

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/earthobservations/wetterdienst
- https://wetterdienst.readthedocs.io/
- https://github.com/earthobservations/wetterdienst/blob/main/LICENSE

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

← 158. [FAISS](JAI-A3-08.md) · 160. [stalkerware-indicators](SUR-B3-10.md) →
