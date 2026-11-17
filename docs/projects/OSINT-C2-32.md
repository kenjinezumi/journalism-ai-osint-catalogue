# streetlevel

`OSINT-C2-32` · **80/100** · overall rank 148 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 48) |
| **Segment** | C2 · Image/video verification, geolocation, satellite, aviation and maritime (rank 21) |
| **Subcategory** | Street-level imagery |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | sk-zk |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/sk-zk/streetlevel) · [Documentation](https://streetlevel.readthedocs.io/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 2/5 · usability 4/5 · licence+cost 4/5 → **weighted 80/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python library for downloading panoramas and metadata from several street-level imagery services, including Google Street View, Apple Look Around, Yandex Panorama and Mapillary, via their internal or public interfaces.

## Journalism / investigative use case

The practical workhorse of photograph geolocation: pull panoramas for a candidate location and compare building façades, signage and street furniture against the image you are trying to place — and pull the capture dates, which tell you whether a feature visible in your photo existed when the panorama was taken.

## 2. Audience

specialist investigator, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Multi-provider coverage including Apple Look Around and Yandex Panorama is the key advantage: Yandex coverage of Russia, Central Asia and parts of the Middle East is far better than Google's, which matters enormously for reporting on those regions
- Programmatic panorama download enables systematic comparison across many candidate locations, which manual Street View browsing cannot
- Capture-date metadata is exposed, which is essential for temporal reasoning about what a photograph shows
- MIT licensed, actively maintained (v0.13.0 on 2026-11-12, same-day push) with a very clean tracker (5 open issues)

## 5. Cons

- Works against providers' internal or undocumented interfaces, which may breach their terms of service and can break without notice — a legal and reliability consideration you must take knowingly
- Requests go directly to the imagery providers, so Google, Apple or Yandex see which locations you are examining — and for Yandex in particular, that disclosure may reach a jurisdiction you are investigating
- Small project (249 stars) with a single maintainer, so continuity depends on one person against several moving upstream targets
- No licence clarity on the imagery itself: panoramas remain the providers' copyrighted content, so republishing them in a story is a separate rights question

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 249 stars with 5 open issues, release v0.13.0 on 2026-11-12 with same-day push, MIT licence. The reliance on providers' internal interfaces is inherent to the approach and is the acknowledged fragility.

## 7. Assessment

Genuinely valuable for geolocation in regions where Google coverage is absent, and the Yandex access in particular has no real substitute. For your profile three cautions apply together: route requests through an egress not identifiable as your newsroom, be aware that querying Yandex discloses your interest to a Russian service, and treat panorama images as third-party copyrighted material requiring a rights decision before publication. Expect breakage and keep manual browsing as a fallback.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-12, latest release v0.13.0 published the same day, 249 stars, 5 open issues. Frequent releases and a near-empty tracker from an engaged single maintainer — strong activity, with single-maintainer concentration as the risk.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the library. Downloaded panoramas remain the imagery providers' copyrighted content.

**Restrictions:** Code permissive. The substantive constraints are external: providers' terms of service may prohibit programmatic access, and panorama imagery is copyrighted, so republication in a story needs a rights assessment or fair-dealing judgement.

**Licence evidence:** https://github.com/sk-zk/streetlevel/blob/main/LICENSE

## 10. Costs

No fee and no API keys for the internal interfaces — which is precisely why terms-of-service risk substitutes for monetary cost. Negligible compute; storage for panoramas.

## 11. Privacy and data flows

Requests go directly to Google, Apple, Yandex or Mapillary, disclosing the coordinates you are examining. The Yandex case deserves particular thought in hostile-state reporting. Use a dedicated egress.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Uses providers' internal interfaces — terms-of-service risk and breakage; queries disclose target coordinates to the providers

## 13. Alternatives

- Manual browsing of Street View, Look Around and Yandex Panorama — slower, same disclosure, no terms risk from automation
- Mapillary API for openly licensed crowd-sourced imagery
- Satellite imagery via sentinelhub-py where street-level is unavailable

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/sk-zk/streetlevel
- https://streetlevel.readthedocs.io/
- https://github.com/sk-zk/streetlevel/blob/main/LICENSE

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

← 147. [Privacy Badger](SUR-B3-33.md) · 149. [Gephi](OSINT-C3-33.md) →
