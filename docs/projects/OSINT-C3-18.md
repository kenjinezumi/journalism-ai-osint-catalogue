# Arelle

`OSINT-C3-18` · **72/100** · overall rank 252 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 87) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 27) |
| **Subcategory** | Financial data processing |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Arelle Project / XBRL community |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Arelle/Arelle) · [Documentation](https://arelle.readthedocs.io/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 72/100**

---

## 1. Purpose

Open-source XBRL platform for loading, validating and querying XBRL financial reports against taxonomies, with validation plugins for regulatory filing rules in several jurisdictions.

## Journalism / investigative use case

Rigorous processing of structured financial filings: load a company's XBRL report, validate it against the regulator's taxonomy, and extract facts with their full context (period, unit, dimension) — which is how you avoid the misreading that makes a financial story wrong.

## 2. Audience

engineer, specialist investigator

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Validation against official taxonomies is the distinguishing capability: it tells you whether a filing is internally consistent and correctly tagged, which is both a data-quality check and occasionally a story
- Handles the full XBRL context model (periods, units, dimensions), so extracted facts carry the qualifications that make them meaningful — the detail that simpler extractors drop
- Covers multiple jurisdictions' filing rules through plugins, so it extends beyond US EDGAR to European and other regulatory regimes
- Long-established open-source project with institutional involvement from the XBRL community

## 5. Cons

- XBRL is a genuinely complex standard and Arelle exposes that complexity rather than hiding it — the learning curve is the main cost and it is substantial for a journalist
- Designed for filing-preparation and regulatory validation, so the workflow assumes accounting expertise rather than investigative questions
- Heavy and slow relative to simpler extractors; for 'what was revenue in 2024' edgartools is far quicker
- Maintenance cadence is steady rather than brisk, consistent with a mature standards-oriented project

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with continuing development. Arelle's standing in the XBRL community is well established; journalism use is specialist and unverified here.

## 7. Assessment

Reach for it only when financial precision is central and the jurisdiction's XBRL taxonomy matters — a story turning on how a company classified a liability, for example. For your profile the realistic division is edgartools for extraction and exploratory analysis, Arelle when a figure must be defensible to an accountant, and an actual accountant consulted before publication either way. The validation capability is the reason it is in the catalogue.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with continuing but modest development, consistent with a mature standards-implementation project. Classified stable-low: the standard evolves slowly and so does the implementation.

## 9. Licensing

**Licence:** Apache-2.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Taxonomies are published by regulators under their own terms.

**Restrictions:** Permissive as published.

**Licence evidence:** https://github.com/Arelle/Arelle

## 10. Costs

No fee. Compute for loading and validating large filings; taxonomies are free downloads. The real cost is the expertise to use it correctly. Estimate.

## 11. Privacy and data flows

Local processing. Taxonomy downloads contact regulators' servers.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [edgartools](OSINT-C3-17.md) for faster, more accessible US filing extraction
- Direct XBRL parsing for a single known filing structure
- An accountant, which for a financial story is not an alternative but a requirement

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/Arelle/Arelle
- https://arelle.readthedocs.io/

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

← 251. [rtl-ais](OSINT-C2-49.md) · 253. [Autopsy](SUR-B3-18.md) →
