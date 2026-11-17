# PMTiles

`JAI-A1-24` · **85/100** · overall rank 95 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 38) |
| **Segment** | A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow (rank 10) |
| **Subcategory** | Map publishing |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Protomaps |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause for the reference implementations; the PMTiles SPECIFICATION is public domain or CC0 where applicable; bundled sample tilesets have their own terms (licence blob read 2026-11-17; GitHub reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/protomaps/PMTiles) · [Documentation](https://docs.protomaps.com/pmtiles/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 85/100**

---

## 1. Purpose

Single-file archive format for map tiles that supports HTTP range requests, allowing a whole tileset to be served from static storage with no tile server, plus reference implementations in several languages.

## Journalism / investigative use case

Self-hosting map tiles with no infrastructure: put one PMTiles file on static storage or a CDN and serve an interactive map, which removes both the tile-server operations and the third-party tile provider that would otherwise see every reader's map viewport.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Eliminates tile-server infrastructure entirely — a single file on static hosting is the cheapest and most durable way to publish maps, and it keeps working long after a story is published
- Removes the reader-privacy problem: no third-party tile provider sees your audience's map interactions, which matters for sensitive stories
- Licence resolved in this survey and unusually favourable: BSD-3-Clause for the reference implementations and the SPECIFICATION ITSELF IS PUBLIC DOMAIN / CC0 — so the format carries no lock-in at all
- Very clean tracker (19 open issues against 3,233 stars) and an established maintainer in the open-mapping space

## 5. Cons

- Last push 2026-09-16 with no release objects at all, so pinning means tracking commits — modest risk for a format implementation, but poor release hygiene
- Requires tile production upstream (tippecanoe or Protomaps' own tooling), so it is one component of a pipeline rather than a complete solution
- HTTP range requests must be supported by your hosting, which most static hosts do but some configurations break
- Bundled sample tilesets in the repository have their own licence terms, as the licence file notes — a detail to check if you use them

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,233 stars with 19 open issues, no release objects, pushed 2026-09-16, SPDX NOASSERTION with the licence blob read 2026-11-17 stating BSD-3-Clause for the reference implementations, the specification in the public domain or CC0, and separate terms for sample tilesets.

## 7. Assessment

Adopt it as the default way to publish maps — the combination of no server, no third-party tile provider and a public-domain specification is as close to a free lunch as this catalogue contains. For your profile the pipeline to build once is tippecanoe to tiles, PMTiles as the archive, static storage to serve, MapLibre or Leaflet to render. After that, every map is a build step rather than a project, and no reader's viewport leaves your infrastructure.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-16, no release objects, 3,233 stars, 19 open issues. Two months since last push with a very clean tracker; a format specification plus reference implementations, where stability is appropriate and the public-domain specification insulates you from maintainer risk.

## 9. Licensing

**Licence:** BSD-3-Clause for the reference implementations; the PMTiles SPECIFICATION is public domain or CC0 where applicable; bundled sample tilesets have their own terms (licence blob read 2026-11-17; GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Sample tilesets in the repository are subject to their own licence terms, as the licence file states explicitly.

**Restrictions:** Essentially none: implementations are permissive and the format itself is unencumbered, so there is no lock-in risk. Check the terms of any bundled sample tileset you use.

**Licence evidence:** https://github.com/protomaps/PMTiles/blob/main/LICENSE

## 10. Costs

No fee. Static storage for the tile archive — pennies per month for a national-scale tileset on object storage. The cheapest map-publishing path available. Estimate.

## 11. Privacy and data flows

Serving from your own static storage means no third-party provider sees reader map requests — the strongest reader-privacy position for interactive maps, and the main non-cost reason to adopt it.

## 12. Verdict

**Adopt**

## 13. Alternatives

- A tile server (martin, tileserver-gl) where dynamic tile generation is genuinely needed
- MBTiles plus a server for the older equivalent workflow
- Commercial tile providers, accepting cost and reader-privacy exposure

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/protomaps/PMTiles/blob/main/LICENSE
- https://docs.protomaps.com/pmtiles/
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [FreshRSS](JAI-A1-03.md) | 94 | Adopt |
| 2 | [trafilatura](JAI-A1-01.md) | 91 | Adopt |
| 3 | [RSSHub](JAI-A1-05.md) | 89 | Adopt |
| 4 | [Playwright](JAI-A1-08.md) | 89 | Adopt |
| 5 | [libpff](JAI-A1-12.md) | 87 | Adopt |
| 6 | [feedparser](JAI-A1-07.md) | 86 | Adopt |
| 7 | [n8n](JAI-A1-17.md) | 85 | Monitor |
| 8 | [DuckDB spatial extension](JAI-A1-19.md) | 85 | Adopt |

---

← 94. [Photon (komoot geocoder)](OSINT-C2-29.md) · 96. [promptfoo](JAI-A3-14.md) →
