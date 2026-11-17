# unitedstates/congress

`OSINT-C3-42` · **70/100** · overall rank 271 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 99) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 31) |
| **Subcategory** | Legislative records |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | unitedstates project (civic-tech community) |
| **Maintenance** | Stable with low activity |
| **Licence** | Public domain / CC0 (unitedstates project convention — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/unitedstates/congress) · [Documentation](https://github.com/unitedstates/congress#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 70/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Collection of scrapers and parsers for US Congressional data — bills, votes, amendments, committee activity and member information — producing structured JSON from official sources.

## Journalism / investigative use case

Tracking US federal legislation systematically: who sponsored a surveillance bill, how committee membership shaped it, which amendments were quietly added — the structured record that makes legislative accountability reporting possible without reading the Congressional Record by hand.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Structured output from official sources means the data is authoritative and the parsing is auditable — important when a story turns on who voted how
- Covers amendments and committee activity, not just final votes, which is where legislative influence actually operates and where most coverage stops
- Public-domain or permissively licensed civic-tech project with a long history, feeding several downstream services
- Free against free official sources, so the whole capability costs only compute

## 5. Cons

- Civic-tech community maintenance means activity is episodic and depends on volunteer attention — a real continuity question for a scraping project against changing official sites
- US federal only
- Congressional data structures are genuinely complex (bill versions, amendment trees, procedural votes), so the structured output still requires domain knowledge to interpret correctly
- Several downstream services (GovTrack, ProPublica's congress API historically) wrap this data more conveniently, so direct use is often unnecessary

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under the unitedstates civic-tech project. Its role as an upstream source for several congressional-data services is documented by those projects.

## 7. Assessment

Integrate it if you cover US federal legislation and need the structured record, but check first whether a downstream API gives you the same data with less work. For your profile the broader transferable point is the same as for openstates and querido-diario: legislative accountability depends on structured records, and where your jurisdiction does not publish them, building the collection is a durable public good as well as a reporting asset.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived under civic-tech community maintenance with episodic activity. Classified stable-low: a long-lived project whose maintenance depends on volunteer attention, which is a continuity consideration for scraper-based collection.

## 9. Licensing

**Licence:** Public domain / CC0 (unitedstates project convention — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Congressional records are US government public records.

**Restrictions:** None material — the unitedstates project convention is public-domain dedication, which is unusually permissive.

**Licence evidence:** https://github.com/unitedstates/congress

## 10. Costs

No fee. Negligible compute; the real cost is scraper maintenance if you extend it. Estimate.

## 11. Privacy and data flows

Public records; scraping official sites is unremarkable.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- US federal only; volunteer maintenance against changing official sites

## 13. Alternatives

- GovTrack or a congressional-data API for the same data with less maintenance
- [openstates-scrapers](OSINT-C3-13.md) for state rather than federal legislatures
- Congress.gov directly for one-off lookups

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/unitedstates/congress

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 270. [sigma.js](OSINT-C3-34.md) · 272. [WebScrapBook](OSINT-C1-40.md) →
