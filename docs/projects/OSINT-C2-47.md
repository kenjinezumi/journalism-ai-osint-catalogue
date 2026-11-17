# dump1090 (FlightAware fork)

`OSINT-C2-47` · **81/100** · overall rank 137 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 44) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 20) |
| **Subcategory** | Aviation tracking (ADS-B receiver) |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | FlightAware |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-2.0-or-later (licence blob read 2026-11-17 — 'licensed under the GPL, v2 or later', with the maintainer inviting contact for GPL-incompatible uses; GitHub reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/flightaware/dump1090) · [Documentation](https://github.com/flightaware/dump1090#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 81/100**

---

## 1. Purpose

Mode S and ADS-B decoder for RTL-SDR software-defined radio receivers, decoding aircraft transponder broadcasts into position, altitude, speed and identity data with a local web map.

## Journalism / investigative use case

Independent aircraft tracking from your own receiver: record every aircraft overhead with timestamps, including flights that commercial tracking sites filter, block or do not cover. For reporting on surveillance aircraft, rendition flights or military movements, your own receiver is evidence nobody can retract.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Your own receiver produces your own data, which cannot be blocked, filtered or withdrawn — the decisive advantage over commercial tracking sites that honour blocking requests from aircraft owners
- Hardware cost is trivial (an RTL-SDR dongle and an antenna), making this one of the cheapest independent evidence-collection capabilities available to a newsroom
- GPL-2.0-or-later (licence resolved in this session; GitHub reports NOASSERTION) with active maintenance (pushed 2026-11-03, tag v11.1) and a maintainer who explicitly invites contact for GPL-incompatible uses
- The FlightAware fork is the practically maintained line in a family of forks, so it is the right starting point

## 5. Cons

- Coverage is line-of-sight from your antenna — typically 100-400km in good conditions — so a single receiver sees only its own region, and building wider coverage means recruiting receivers
- Aircraft can disable or spoof ADS-B transmission, and military aircraft frequently do, so absence of a track means nothing and presence can be falsified
- Requires hardware, an antenna with a reasonable sky view, and some radio literacy — a real setup effort rather than a software install
- GitHub reports NOASSERTION so automated licence scanning does not resolve it, and the fork landscape (antirez, MalcolmRobb, FlightAware) confuses newcomers about which to use

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,153 stars with 86 open issues, latest tag v11.1, pushed 2026-11-03, licence resolved by reading the blob to GPL-2.0-or-later with the maintainer inviting contact for GPL-incompatible use. The fork lineage (antirez original, MalcolmRobb last pushed 2024-08-14, FlightAware current) was verified via the API.

## 7. Assessment

Adopt if aviation is a live beat — the cost is negligible and the independence is the point. For your profile the strongest pattern is a small network: two or three receivers at reporters' homes or offices covering an airport or a flight corridor, feeding a shared store, which gives you coverage a single site cannot. Pair with bellingcat/adsb-history for querying accumulated data, and never treat absence of a track as evidence an aircraft did not fly.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-03, no release objects, latest tag v11.1, SPDX NOASSERTION (GPL-2.0-or-later per the licence blob), 1,153 stars, 86 open issues. Corporate-maintained fork with current commits; by comparison antirez/dump1090 last pushed 2026-02-15 and MalcolmRobb/dump1090 2024-08-14.

## 9. Licensing

**Licence:** GPL-2.0-or-later (licence blob read 2026-11-17 — 'licensed under the GPL, v2 or later', with the maintainer inviting contact for GPL-incompatible uses; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. The ADS-B data you receive is broadcast in the clear; your recordings are your own.

**Restrictions:** GPL-2.0-or-later on the software. Note that receiving and recording broadcast ADS-B is lawful in most jurisdictions but not all — check local radio law before deploying, as this is a legal rather than licence question.

**Licence evidence:** https://github.com/flightaware/dump1090/blob/master/LICENSE

## 10. Costs

No software fee. Hardware: an RTL-SDR dongle and antenna (tens of dollars/euros each, prices not verified here) plus a small always-on computer such as a Raspberry Pi. Storage grows with traffic volume — modest. Among the best capability-per-cost ratios in this catalogue.

## 11. Privacy and data flows

Entirely local reception and decoding: nothing is transmitted unless you choose to feed an aggregator. Feeding FlightAware or similar networks shares your data and your receiver's location with them — a deliberate choice, and one to decline if your receiver's location should stay private.

## 12. Verdict

**Adopt**

## 13. Alternatives

- readsb or tar1090 as modern alternatives in the same ecosystem
- bellingcat/adsb-history for querying historical ADS-B without running a receiver
- Commercial tracking APIs, which are easier but filterable and withdrawable

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/flightaware/dump1090
- https://github.com/flightaware/dump1090/blob/master/LICENSE
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

← 136. [c2pa-rs / c2patool](OSINT-C2-13.md) · 138. [EDGI web-monitoring-diff](SUR-B1-21.md) →
