# adsb-history

`OSINT-C2-48` · **85/100** · overall rank 82 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 26) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 12) |
| **Subcategory** | Aviation tracking (historical analysis) |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/adsb-history) · [Documentation](https://github.com/bellingcat/adsb-history#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## 1. Purpose

Tool to collect and query historical ADS-B aircraft data by geographic region, altitude and time, to identify specific aircraft and movement trends.

## Journalism / investigative use case

The analytical layer over aircraft data: find every aircraft that circled a given area below a given altitude over a period — the standard method for identifying surveillance aircraft, which loiter in orbits over neighbourhoods rather than flying point to point.

## 2. Audience

specialist investigator, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Implements the specific query that surveillance-aircraft reporting depends on — region plus altitude plus loitering pattern — rather than leaving you to write it
- Works against historical data, so you can investigate past activity rather than only watching live, which is what most such stories require
- MIT licensed and built by Bellingcat, whose investigators have done substantial published work on surveillance aircraft
- Actively maintained (pushed 2026-11-09) and small enough to adapt

## 5. Cons

- Depends on third-party historical ADS-B data sources, whose availability, coverage and terms are outside your control — the data dependency is the real risk, not the code
- No releases (100 stars, 8 open issues), so pinning relies on commits and the project is small
- Aircraft with disabled or spoofed ADS-B are invisible, and military and some state aircraft routinely are, so this method finds the surveillance aircraft that transmit and systematically misses those that do not
- Identifying an aircraft's operator from a registration requires separate research (civil registries, FAA/EASA records), which this does not do

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 100 stars with 8 open issues, no releases, last push 2026-11-09, MIT licence. Bellingcat's published surveillance-aircraft investigations are the relevant context for the technique's effectiveness, though I verified no specific use of this tool.

## 7. Assessment

Adopt for aviation-related investigation — it encodes a method that would otherwise take you days to work out. For your profile combine it with your own dump1090 receiver where possible, because that gives you a data source nobody can withdraw, and with registry research to get from a tail number to an operator. State clearly in published work that aircraft without ADS-B are invisible to the method, since that limitation is the obvious line of attack on such a story.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-09, no releases or tags, 100 stars, 8 open issues. Recent commits from an institutional maintainer; small project maintained alongside Bellingcat's investigative needs.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Historical ADS-B data comes from third-party sources with their own terms; check the source you configure before republishing raw data.

**Restrictions:** None on the code. Data-source terms are the constraint on redistribution.

**Licence evidence:** https://github.com/bellingcat/adsb-history/blob/main/LICENSE

## 10. Costs

No software fee. Historical ADS-B data access may involve paid tiers depending on the source — not priced in this survey. Negligible compute.

## 11. Privacy and data flows

Queries go to whichever historical data source you configure, disclosing the regions and periods you are investigating. Your own receiver data (via dump1090) avoids this entirely.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Running your own dump1090 receiver for data nobody can withdraw
- Commercial ADS-B history APIs directly, with their own costs and terms
- ADSBexchange-style community data, noting access terms vary

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/bellingcat/adsb-history
- https://github.com/bellingcat/adsb-history/blob/main/LICENSE

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

← 81. [OONI Probe CLI / probe-engine](SUR-B1-01.md) · 83. [androidqf](SUR-B3-09.md) →
