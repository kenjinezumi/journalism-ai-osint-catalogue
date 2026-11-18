# bellingcat/EDGAR

`OSINT-C3-16` · **70/100** · overall rank 266 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 95) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 29) |
| **Subcategory** | Corporate filings |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Bellingcat |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/bellingcat/EDGAR) · [Documentation](https://github.com/bellingcat/EDGAR#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 2/5 · privacy 4/5 · usability 4/5 · licence+cost 4/5 → **weighted 70/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | SEC filings are US government-published public records. |
| **Restrictions** | Copyleft on the tool; immaterial for internal use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. EDGAR access is free with fair-use rate limits. Negligible compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/bellingcat/EDGAR/blob/main/LICENSE
- https://github.com/bellingcat/EDGAR
- `../sources/evidence/leads.md`

---

## 1. Purpose

Tool for searching the US Securities and Exchange Commission's EDGAR full-text and filing-index systems, retrieving filings by company, form type, date and text content.

## Journalism / investigative use case

Searching the full text of US corporate filings for a name, address or phrase: finding every SEC filing that mentions a particular individual, shell company or address is a standard step in corporate investigation and is awkward through EDGAR's own interface.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Full-text search across filings is the capability that matters: a name appearing in an obscure exhibit is often the link an investigation needs, and EDGAR's web interface makes that hard to find systematically
- Built by Bellingcat for investigators, so the interface assumes a research task rather than a financial-analysis one
- GPL-3.0 with a tagged release (v2.1.2, 2025-05-15) and a clear scope
- Free access to a rich official dataset — SEC filings are public and unusually detailed about corporate structure and related parties

## 5. Cons

- Maintenance has slowed: last push and release both 2025-05-15, eighteen months before this survey, and EDGAR's interfaces do change
- US-registered entities only, so it covers a specific slice of global corporate activity — though an important one, since many international structures touch US markets
- Full-text coverage in EDGAR does not extend uniformly across all historical filings, so an absence is not evidence
- Narrow tool: it finds filings, and reading and interpreting them is the work

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 216 stars, release v2.1.2 (2025-05-15) with the last push the same day, GPL-3.0. Session 1's candidate path bellingcat/edgar-tool is a 404; the correct repository is bellingcat/EDGAR (verified 2026-11-17).

## 7. Assessment

Useful for the specific task of full-text searching SEC filings, with the caveat that eighteen months without maintenance against a changing official interface warrants a liveness check before you rely on it. For your profile the alternatives are worth knowing: edgartools is more actively maintained and offers richer parsing, so I would test both and prefer whichever currently works, treating this as the simpler option for pure search.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2025-05-15, latest release v2.1.2 published the same day, 216 stars, GPL-3.0. Eighteen months without activity on a tool that depends on an official interface which does change — declining rather than dormant, but verify it still works.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** SEC filings are US government-published public records.

**Restrictions:** Copyleft on the tool; immaterial for internal use.

**Licence evidence:** https://github.com/bellingcat/EDGAR/blob/main/LICENSE

## 10. Costs

No fee. EDGAR access is free with fair-use rate limits. Negligible compute.

## 11. Privacy and data flows

Queries go to the SEC, disclosing your search terms to a US government system. Unremarkable for most work; consider it if the subject is sensitive.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Eighteen months without maintenance against a changing official interface

## 13. Alternatives

- [edgartools](OSINT-C3-17.md) for a more actively maintained Python interface with richer parsing
- sec-edgar-downloader for bulk filing retrieval
- EDGAR's own full-text search for one-off queries

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/bellingcat/EDGAR
- https://github.com/bellingcat/EDGAR/blob/main/LICENSE
- `../sources/evidence/leads.md`

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

← 265. [sentinelhub-py](OSINT-C2-43.md) · 267. [Metabigor](OSINT-C1-09.md) →
