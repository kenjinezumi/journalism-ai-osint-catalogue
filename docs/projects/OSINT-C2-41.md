# Open-Meteo

`OSINT-C2-41` · **75/100** · overall rank 215 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 71) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 31) |
| **Subcategory** | Weather API (self-hostable) |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open-Meteo |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/open-meteo/open-meteo) · [Documentation](https://open-meteo.com/en/docs) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 5/5 · privacy 4/5 · usability 4/5 · licence+cost 3/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Open-source weather API server providing forecasts and historical reanalysis data from multiple national models, available as a hosted free-for-non-commercial-use service or self-hosted.

## Journalism / investigative use case

Historical weather verification using reanalysis data, which gives a value for any coordinate rather than only at station locations — addressing meteostat's sparse-coverage weakness, at the cost of using a model estimate rather than an observation.

## 2. Audience

engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Reanalysis coverage means you get a weather estimate for any coordinate, including regions with no nearby station — which is where verification is hardest
- Self-hostable under AGPL-3.0, so queries about sensitive coordinates need not go to a third party
- Actively developed (1.8.0, 2026-11-03; pushed 2026-11-17) with a substantial community (6,682 stars)
- Multiple underlying national models available, so you can compare estimates rather than trusting one

## 5. Cons

- The hosted service is explicitly 'free for non-commercial use' per the repository description, so a commercially operated newsroom using the free tier needs to check its position — and the self-hosted path or a paid tier may be required
- Reanalysis is a model estimate, not an observation: it is spatially complete but can be wrong locally, so it is weaker evidence than a nearby station reading and should be described as modelled
- AGPL-3.0 network copyleft applies if you modify and expose an instance
- Self-hosting requires downloading substantial model data, so it is a real infrastructure commitment rather than a quick deployment; 151 open issues

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 6,682 stars with 151 open issues, release 1.8.0 (2026-11-03), pushed 2026-11-17, AGPL-3.0; the repository describes the hosted service as 'Free Weather Forecast API for non-commercial use', which is the key commercial-use caveat.

## 7. Assessment

Use it for the coverage gap meteostat leaves, with two decisions made explicitly. First, the commercial-use question on the hosted free tier: verify your position or self-host, because a commercially operated outlet relying on a non-commercial free tier is a licensing exposure. Second, in published work describe reanalysis values as modelled estimates and prefer a station observation where one exists — a reader can check a station reading, and that is worth more than spatial completeness.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 1.8.0 (2026-11-03), 6,682 stars, 151 open issues. Same-day commits and recent releases with a large community and an operating hosted service.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** Underlying weather models come from national services (DWD, NOAA, ECMWF and others) with their own terms, several requiring attribution and some restricting commercial redistribution.

**Restrictions:** AGPL-3.0 on the server. The material caveat is the hosted service's stated non-commercial framing — confirm your position before a commercially operated newsroom depends on the free tier. Underlying model data terms vary by source and need checking before republication.

**Licence evidence:** https://github.com/open-meteo/open-meteo/blob/main/LICENSE

## 10. Costs

Self-hosting: no software fee but substantial model-data download and storage, plus a server — a real infrastructure commitment (estimate: hundreds of GB and a dedicated VM, depending on which models and history you need). Hosted service free for non-commercial use with paid tiers above that — current prices not verified in this survey.

## 11. Privacy and data flows

Self-hosting keeps coordinate queries private. The hosted API receives the coordinates and dates you query, which indicates your area and period of interest.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Hosted service is framed as free for non-commercial use — commercial newsrooms must self-host or verify their position

## 13. Alternatives

- [meteostat](OSINT-C2-40.md) for station observations, which are stronger evidence where available
- [wetterdienst](OSINT-C2-42.md) for European national-service data at fine granularity
- National agency archives directly for maximum authority in a published claim

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/open-meteo/open-meteo
- https://open-meteo.com/en/docs
- https://github.com/open-meteo/open-meteo/blob/main/LICENSE

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

← 214. [igraph](OSINT-C3-32.md) · 216. [OutbackCDX](OSINT-C1-44.md) →
