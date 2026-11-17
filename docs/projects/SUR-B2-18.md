# Open Contracting Data Standard

`SUR-B2-18` · **79/100** · overall rank 168 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 47) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 10) |
| **Subcategory** | Procurement data standard |
| **Type** | dataset |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open Contracting Partnership |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 for the standard and schemas (confirm the repository licence file for your records) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/open-contracting/standard) · [Documentation](https://www.open-contracting.org/data-standard/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 79/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Open data standard for publishing structured information about public contracting across the whole process — planning, tender, award, contract and implementation — with schemas, extensions and validation tooling.

## Journalism / investigative use case

The common format that makes cross-country procurement analysis possible: where governments publish OCDS data, you can compare surveillance purchases across jurisdictions using one schema instead of writing a parser per country. It also defines the fields to demand when a government's procurement data is unusable.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

dataset · bucket `verified-oss`

## 4. Pros

- Standardisation is the enabling condition for comparative procurement journalism, and OCDS is the standard that has actually been adopted by a meaningful number of governments
- Covers the full contracting lifecycle including planning and implementation, so you can report on modifications and overruns rather than only awards — where surveillance contracts often grow quietly
- Validation tooling and extensions mean you can check a government's published data against the standard and demonstrate where it is deficient, which is itself a story
- Open standard with public schemas and an institutional steward, so it is a durable reference rather than a vendor format

## 5. Cons

- A standard, not a dataset: its usefulness depends entirely on whether the governments you cover publish in it, and adoption is uneven — many do not
- Publishers implement partially, so OCDS-labelled data frequently omits the fields you most want (supplier identifiers, contract documents, modifications)
- Session 1's recorded URL (standards.open-contracting.org) did not respond in this survey; the working entry point is open-contracting.org/data-standard/ (verified 2026-11-17)
- Engineer-facing: working with OCDS data means schema work, and the pay-off only arrives when several publishers are compared

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the session-1 URL did not respond while open-contracting.org/data-standard/ returned 200 (both checked 2026-11-17, recorded in sources/evidence/b2-sources.md). OCDS adoption by national procurement authorities is documented by the Open Contracting Partnership.

## 7. Assessment

Integrate it where your jurisdictions publish OCDS — it removes the per-country parser problem that otherwise makes comparative procurement work prohibitive. For your profile there is a second, advocacy-adjacent use worth knowing: validating a government's procurement publication against the standard produces a concrete, citable account of what it conceals, which is a reportable finding in its own right and a strong basis for a transparency request.

## 8. Maintenance

**Actively maintained** — Standard documentation verified live on 2026-11-17 (open-contracting.org/data-standard/ returns 200); the standard repository and its schema versioning are maintained by the Open Contracting Partnership with a published versioning policy. Maintenance here means schema and extension governance rather than software releases.

## 9. Licensing

**Licence:** Apache-2.0 for the standard and schemas (confirm the repository licence file for your records) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Published OCDS datasets carry each publisher's own licence, which varies by government and must be checked per source.

**Restrictions:** The standard is openly licensed. The data is the variable: individual publishers' licences differ and some restrict reuse, so check per jurisdiction before republishing.

**Licence evidence:** https://github.com/open-contracting/standard

## 10. Costs

No fee. Engineer time for schema work; negligible infrastructure.

## 11. Privacy and data flows

A standard and public datasets about public bodies; no privacy dimension beyond ordinary web access.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Value depends on publisher adoption, which is uneven and often partial

## 13. Alternatives

- TED for EU procurement in its own format
- National procurement portals directly, accepting per-country parsing
- OpenCorporates or national registries to resolve supplier identities that OCDS data often leaves ambiguous

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `docs-reviewed`

- https://www.open-contracting.org/data-standard/
- https://github.com/open-contracting/standard
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
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |

---

← 167. [GeoCLIP](OSINT-C2-16.md) · 169. [eyecite](JAI-A2-16.md) →
