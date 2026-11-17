# TED — Tenders Electronic Daily (EU public procurement)

`SUR-B2-13` · **84/100** · overall rank 101 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 29) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 7) |
| **Subcategory** | Procurement records |
| **Type** | dataset |
| **Bucket** | `proprietary-service` |
| **Maintainer** | Publications Office of the European Union |
| **Maintenance** | Actively maintained |
| **Licence** | EU reuse terms apply to TED data (generally permissive with attribution under the Commission's reuse decision) — specific current terms NOT verified in this survey |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://ted.europa.eu/en/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 4/5 → **weighted 84/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Official EU portal publishing public-procurement notices above threshold from all member states, including contract notices, award notices and contracting-authority details, with search and bulk data access.

## Journalism / investigative use case

The primary record for European surveillance procurement: finding which ministry or police force bought interception, forensic or biometric systems, from which supplier and for how much. Award notices name the winning bidder and value, which is the documentary core of a surveillance-procurement story.

## 2. Audience

journalist, newsroom analyst, specialist investigator

## 3. Project type

dataset · bucket `proprietary-service`

## 4. Pros

- Official, authoritative and citable: a TED award notice is a primary document, which is far stronger than a vendor press release or a leaked slide
- Covers all EU member states in one place, so cross-border comparison of what different governments bought is tractable
- Bulk and API access exist alongside the web search, so systematic monitoring of procurement categories is possible rather than only ad-hoc lookups
- Free to access with no account required for search

## 5. Cons

- Only above-threshold procurement is published, and surveillance purchases are frequently structured below threshold, through framework agreements, through intermediaries, or exempted on national-security grounds — so absence from TED is not absence of purchase, and this is the central analytical limitation
- Notice text is terse and uses procurement vocabulary and CPV codes rather than product names, so identifying surveillance purchases requires knowing how they are described
- Session 1's recorded URL (ted.europa.eu/en/simple-search) returns 404; the current entry point is ted.europa.eu/en/ (verified 2026-11-17) — the portal has been restructured, which also affects saved searches and scraping code
- Not open-source software and not a dataset you control: access terms, structure and availability are the EU's to change, as the URL change demonstrates

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the session-1 URL now 404s while the portal root returns 200 (both verified 2026-11-17 and recorded in sources/evidence/b2-sources.md). TED's role in European procurement journalism is well established; the under-threshold and national-security exemptions are documented features of the EU procurement regime.

## 7. Assessment

Adopt it as a primary source and build a standing search on the relevant CPV codes and keywords rather than searching reactively. For your profile the analytical discipline matters most: a TED notice proves a purchase, while the absence of notices proves nothing, because national-security exemptions and framework agreements hide exactly the procurement you care about. Pair TED with national procurement portals, parliamentary questions and export-licence records to triangulate. Fix any saved searches or scrapers against the restructured portal.

## 8. Maintenance

**Actively maintained** — Portal verified live on 2026-11-17 (ted.europa.eu/en/ returns 200). It is an operational EU statutory publication service rather than a software project, so maintenance is institutional; the restructuring that broke the older URL is itself evidence of ongoing development.

## 9. Licensing

**Licence:** EU reuse terms apply to TED data (generally permissive with attribution under the Commission's reuse decision) — specific current terms NOT verified in this survey _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same. Verify the current reuse notice before republishing bulk data.

**Restrictions:** Not verified here. EU public-sector information is generally reusable with attribution, but confirm the current terms before publishing a derived dataset.

**Licence evidence:** https://ted.europa.eu/en/

## 10. Costs

Free to search and access. Infrastructure cost only if you build a monitoring pipeline over the bulk data. No fee verified.

## 11. Privacy and data flows

Searching the portal discloses your queries to the EU service in the ordinary way. The records concern public bodies and their suppliers, not individuals.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Above-threshold publication only; national-security exemptions hide much surveillance procurement

## 13. Alternatives

- National procurement portals for below-threshold and nationally exempted contracts
- data.europa.eu for related EU open datasets
- [Open Contracting Data Standard](SUR-B2-18.md)-formatted national publications where available

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `docs-reviewed`

- https://ted.europa.eu/en/
- `../sources/evidence/b2-sources.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |
| 9 | [Blacklight collector](SUR-B2-02.md) | 81 | Adopt |

---

← 100. [txtai](JAI-A2-55.md) · 102. [csvkit](JAI-A1-18.md) →
