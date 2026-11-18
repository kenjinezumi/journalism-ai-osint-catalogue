# rtl-ais

`OSINT-C2-49` · **72/100** · overall rank 251 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 86) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 34) |
| **Subcategory** | Maritime tracking (AIS receiver) |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Daniel Giardini (dgiardini) |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL (from source headers: derived from rtl_fm by Kyle Keen, AISDecoder by Astra Paging/AISHub and GNUAIS; GitHub reports NOASSERTION) |
| **Licence type** | Unresolved |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/dgiardini/rtl-ais) · [Documentation](https://github.com/dgiardini/rtl-ais#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 72/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Unresolved |
| **Exact licence (as recorded)** | GPL (from source headers: derived from rtl_fm by Kyle Keen, AISDecoder by Astra Paging/AISHub and GNUAIS; GitHub reports NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a. Received AIS broadcasts are transmitted in the clear; your recordings are your own. |
| **Restrictions** | GPL from the upstream lineage. Receiving AIS is lawful in most jurisdictions; confirm local radio law before deploying, as with any SDR receiver. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Dedicated hardware; self-hosted infrastructure |
| **Cost conditions** | Dedicated hardware; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No software fee. Hardware: RTL-SDR dongle plus a VHF antenna (tens of dollars/euros) and a small always-on computer. Storage is modest. Satellite AIS, if you need open-ocean coverage, is a commercial service not priced here.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/dgiardini/rtl-ais/blob/master/LICENCE
- https://github.com/dgiardini/rtl-ais
- `../sources/evidence/leads.md`

> **Unresolved:** the licence could not be confirmed from the evidence gathered.

---

## 1. Purpose

Software-defined-radio AIS receiver that tunes both marine AIS frequencies with an RTL-SDR dongle and decodes vessel position reports to NMEA output.

## Journalism / investigative use case

Independent vessel tracking from your own receiver: record AIS broadcasts from ships in range with timestamps, including vessels whose tracks are obscured, delayed or absent from commercial platforms. For reporting on sanctions-evading tankers, illegal fishing or arms shipments, locally received AIS is evidence you hold directly.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Dual-frequency reception in one dongle is the technical point — AIS uses two channels and single-channel receivers miss roughly half the traffic
- Your own receiver cannot be filtered or rate-limited, unlike commercial AIS platforms which delay or withhold data for some vessels and regions
- Trivial hardware cost (an RTL-SDR and a VHF antenna), making independent maritime monitoring affordable for a small newsroom near a port or strait
- GPL licensed (resolved from source headers in this session) and still receiving commits (pushed 2026-08-05)

## 5. Cons

- Coverage is VHF line-of-sight — realistically 20-60km from a coastal antenna — so it monitors a strait or port approach, not an ocean; open-water tracking needs satellite AIS, which is commercial
- AIS is self-reported and routinely manipulated: vessels switch off transponders (going dark), spoof positions and transmit false identities, which is itself often the story but means a track is a claim rather than a fact
- No releases since v0.3 (2018-08-01) despite recent commits, so versioning signals are weak, and GitHub reports NOASSERTION for the licence
- Requires an antenna with sea view and some radio setup; decoding output is NMEA, so you need downstream tooling to make it useful

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 311 stars with 4 open issues, release v0.3 (2018-08-01), last push 2026-08-05, SPDX NOASSERTION with GPL established from source headers (derived from rtl_fm, AISDecoder and GNUAIS lineage, read 2026-11-17).

## 7. Assessment

Adopt if you have a coastal or strait location and a maritime beat — the independence argument is identical to ADS-B and the hardware cost is just as low. For your profile the realistic framing is that a local receiver documents a chokepoint extremely well and the open ocean not at all, so it complements rather than replaces commercial or satellite AIS. The analytically valuable signal is often the gap: a vessel that goes dark in your coverage area and reappears elsewhere is a documented AIS interruption, which is a reportable fact.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-08-05, latest release v0.3 (2018-08-01), 311 stars, 4 open issues. Commits within the last four months but no release in eight years; a small, functionally complete C tool. Stable rather than dormant given current commits.

## 9. Licensing

**Licence:** GPL (from source headers: derived from rtl_fm by Kyle Keen, AISDecoder by Astra Paging/AISHub and GNUAIS; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Received AIS broadcasts are transmitted in the clear; your recordings are your own.

**Restrictions:** GPL from the upstream lineage. Receiving AIS is lawful in most jurisdictions; confirm local radio law before deploying, as with any SDR receiver.

**Licence evidence:** https://github.com/dgiardini/rtl-ais/blob/master/LICENCE

## 10. Costs

No software fee. Hardware: RTL-SDR dongle plus a VHF antenna (tens of dollars/euros) and a small always-on computer. Storage is modest. Satellite AIS, if you need open-ocean coverage, is a commercial service not priced here.

## 11. Privacy and data flows

Entirely local reception and decoding; nothing transmitted unless you feed an aggregator. Note that contributing to AISHub or similar networks shares your receiver's location.

## 12. Verdict

**Pilot**

## 13. Alternatives

- Global Fishing Watch API for processed vessel-behaviour data over wide areas
- Commercial satellite AIS providers for open-ocean coverage, at cost
- AISHub community data, noting its contribution requirements

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/dgiardini/rtl-ais
- https://github.com/dgiardini/rtl-ais/blob/master/LICENCE
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

← 250. [PyExifTool](OSINT-C2-02.md) · 252. [Arelle](OSINT-C3-18.md) →
