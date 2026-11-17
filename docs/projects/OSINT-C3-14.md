# Querido Diário

`OSINT-C3-14` · **83/100** · overall rank 120 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 38) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 7) |
| **Subcategory** | Official gazette records |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Knowledge Brasil |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/okfn-brasil/querido-diario) · [Documentation](https://queridodiario.ok.org.br/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 83/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Collection of scrapers and a platform that gather Brazilian municipal official gazettes, extract their text and make them searchable across thousands of municipalities.

## Journalism / investigative use case

Searching thousands of municipal gazettes at once: contracts, appointments, emergency decrees and payments are published in local gazettes that nobody reads, and making them searchable turns an invisible record into a reportable one — for example finding the same contractor awarded emergency contracts across dozens of municipalities.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Addresses a genuinely invisible public record: municipal gazettes are legally published and practically unread, so systematic search finds material no one has looked at
- Civic-tech model with a large contributor community adding municipalities, which is how coverage of thousands of jurisdictions becomes feasible
- Directly transferable architecture: the one-scraper-per-municipality pattern applies to any country with decentralised official publication, which is most of them
- Open Knowledge Brasil's institutional maintenance plus community contribution gives it both direction and capacity

## 5. Cons

- Brazil-specific in coverage, so elsewhere it is a template rather than a resource
- Thousands of scrapers means continuous breakage and uneven coverage, with the honest consequence that absence of a gazette for a municipality means nothing
- Gazette text quality varies enormously — many are scanned PDFs of poor quality, so OCR errors propagate into search results
- Running the full platform is a substantial undertaking; using the public service is the sensible path

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under Open Knowledge Brasil's maintenance with a visible community-contribution model. The platform operates publicly, which is the relevant evidence.

## 7. Assessment

Directly useful for Brazil and valuable everywhere as a model — the architecture is the transferable asset. For your profile, if you cover a country with decentralised official publication, this is the project to study before building: the per-jurisdiction scraper plus shared search pattern is proven, and the community-contribution model is how coverage scales beyond what one newsroom can maintain. Use the public service for Brazilian work rather than self-hosting.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under Open Knowledge Brasil's maintenance, with a community-contribution model adding and repairing municipal scrapers continuously. Maintenance means ongoing scraper work supporting an operating public service.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Gazette content is official public record; the aggregated search service's terms were not verified here.

**Restrictions:** Code permissive as published.

**Licence evidence:** https://github.com/okfn-brasil/querido-diario

## 10. Costs

No fee. Public service free to use. Self-hosting thousands of scrapers plus search is a major commitment. Estimate.

## 11. Privacy and data flows

Public records; queries to the public service disclose your search terms to the operator.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Brazil-specific coverage; per-municipality coverage is uneven

## 13. Alternatives

- Building the equivalent for your own jurisdictions using this architecture — the more widely applicable use
- egazette for Indian gazette collection with a similar purpose
- National official-journal portals where centralised publication exists

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/okfn-brasil/querido-diario
- https://queridodiario.ok.org.br/

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
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 119. [PySTAC](OSINT-C2-44.md) · 121. [rigour](JAI-A2-44.md) →
