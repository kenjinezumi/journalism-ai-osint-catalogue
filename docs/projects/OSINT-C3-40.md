# Frictionless Data (frictionless-py)

`OSINT-C3-40` · **72/100** · overall rank 255 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 89) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 28) |
| **Subcategory** | Data packaging and validation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Knowledge Foundation |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/frictionlessdata/frictionless-py) · [Documentation](https://framework.frictionlessdata.io/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 72/100**

---

## 1. Purpose

Python framework implementing the Frictionless Data specifications for describing, validating, extracting and transforming tabular datasets, with schema inference and detailed validation reports.

## Journalism / investigative use case

Publishing a dataset with a schema and a validation report: when you release the data behind an investigation, a Data Package declares the fields, types and constraints and proves the data conforms — which pre-empts the 'your data is wrong' response and makes the dataset reusable by others.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Validation reports are a concrete quality artefact: publishing one alongside a dataset demonstrates that you checked types, missing values and constraints rather than asserting the data is clean
- Schema declaration makes a published dataset genuinely reusable, which is how an investigation's data becomes a resource other journalists build on
- Open specification with multiple language implementations, so a Data Package you publish is consumable without your toolchain
- Open Knowledge Foundation stewardship aligns with open-data publication rather than a commercial product

## 5. Cons

- Tabular data only, so documents, graphs and media collections are out of scope — it addresses one slice of investigative data publication
- Adoption outside the open-data community is modest, so a Data Package is less immediately recognisable to a general audience than a plain CSV plus a readme
- Schema inference is a starting point that needs human correction, and an auto-inferred schema published uncorrected can misdescribe the data
- Maintenance cadence is steady rather than brisk, consistent with specification-implementation work

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under Open Knowledge Foundation stewardship. Frictionless adoption in the open-data community is documented by the project; journalism adoption is modest and unverified here.

## 7. Assessment

Integrate it when you publish datasets, which for an accountability outlet should be routine — the validation report plus declared schema is cheap to produce and materially raises the credibility and reusability of a released dataset. For your profile the minimum viable version is worth doing even without the framework: publish a schema description, a validation summary and a stated provenance for every dataset you release, and frictionless-py simply makes that systematic.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived under Open Knowledge Foundation stewardship with steady rather than frequent development, consistent with implementing a stable specification. Classified stable-low.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. The specifications themselves are openly licensed.

**Restrictions:** Permissive as published.

**Licence evidence:** https://github.com/frictionlessdata/frictionless-py

## 10. Costs

No fee, negligible resources.

## 11. Privacy and data flows

Local processing. The consideration is what you publish: a validation report describes your data's structure, which is usually harmless and occasionally reveals more about collection methods than intended.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Great Expectations for heavier data-validation pipelines
- A hand-written schema and readme alongside a CSV, which is the practical minimum
- CSV on the Web standards for a W3C-aligned alternative

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/frictionlessdata/frictionless-py
- https://framework.frictionlessdata.io/

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

← 254. [brozzler](OSINT-C1-23.md) · 256. [Hyperaudio Lite](JAI-A2-22.md) →
