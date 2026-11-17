# edgartools

`OSINT-C3-17` · **82/100** · overall rank 130 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 41) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 9) |
| **Subcategory** | Corporate filings |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Dwight Gunning (dgunning) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/dgunning/edgartools) · [Documentation](https://github.com/dgunning/edgartools#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 82/100**

---

## 1. Purpose

Python library for accessing SEC EDGAR data with a high-level API over companies, filings and financial statements, parsing structured data out of filings including XBRL financial facts.

## Journalism / investigative use case

Going beyond finding filings to extracting their content: pull the actual financial figures, related-party disclosures, officer lists and ownership tables from filings into structured data, which is what turns a corporate investigation from reading PDFs into analysis.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Structured extraction of financial facts and filing sections is the substantive advantage: analysing a company's disclosures across years requires parsed data, not documents
- High-level API means common tasks (get a company's filings, extract a statement) are a line or two rather than a parsing project
- Actively maintained with a frequent release cadence, which matters because EDGAR's structures and XBRL conventions change
- Open source and free against a free official data source, so the whole corporate-filings capability costs nothing but time

## 5. Cons

- Parsing financial filings is intrinsically error-prone: XBRL tagging quality varies by filer, and a mis-extracted figure that looks plausible is the characteristic failure — any published number needs checking against the filing
- US-registered entities only
- Single-maintainer project, so continuity depends on one person despite the good current cadence
- The high-level API hides parsing decisions, which is convenient and means you may not notice when an extraction is wrong

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with an active release cadence. No journalism deployment verified.

## 7. Assessment

Adopt it for structured corporate-filings work — it is the better-maintained of the two EDGAR options here and the structured extraction is where the analytical value is. For your profile the discipline that matters is verification: extract at scale to find the pattern, then open the underlying filing and confirm every figure that reaches print, because XBRL tagging errors by filers are common and the library cannot detect them.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived with an active release cadence from a single committed maintainer. Maintenance is current; the bus factor is the residual risk.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** SEC filings are US government-published public records.

**Restrictions:** Permissive as published.

**Licence evidence:** https://github.com/dgunning/edgartools

## 10. Costs

No fee. EDGAR access free with fair-use rate limits. Negligible compute.

## 11. Privacy and data flows

Requests go to the SEC, disclosing the companies you are researching to a US government system.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [bellingcat/EDGAR](OSINT-C3-16.md) for simpler full-text search, with its maintenance caveat
- sec-edgar-downloader for bulk document retrieval without parsing
- [Arelle](OSINT-C3-18.md) for rigorous XBRL processing where financial precision is critical

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/dgunning/edgartools

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

← 129. [DuckDuckGo Tracker Radar](SUR-B2-03.md) · 131. [katana](OSINT-C1-15.md) →
