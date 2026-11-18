# rigour

`JAI-A2-44` · **83/100** · overall rank 121 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 51) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 30) |
| **Subcategory** | Name and identifier normalisation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenSanctions |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/opensanctions/rigour) · [Documentation](https://github.com/opensanctions/rigour#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 83/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Bundled reference datasets (country codes, legal forms) — permissive, derived from public standards. |
| **Restrictions** | None material. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, negligible resources.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/opensanctions/rigour/blob/main/LICENSE
- https://github.com/opensanctions/rigour

---

## 1. Purpose

Library of data-cleaning primitives for investigative data: name normalisation and fingerprinting, company-type canonicalisation, address parsing, country and language code handling, and identifier validation (IBAN, LEI, ISIN, tax numbers).

## Journalism / investigative use case

The unglamorous preprocessing that decides whether matching works at all: turning 'OOO Rosneft-Trading Ltd.' and 'ROSNEFT TRADING LIMITED' into the same key before any fuzzy scorer sees them, and validating that a claimed IBAN or company number in a leak is structurally real.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Encodes domain knowledge that is tedious and error-prone to reimplement: legal-form suffixes across dozens of jurisdictions, company-type equivalences, identifier checksums
- Supersedes the widely cited 'fingerprints' package — using rigour instead is itself a useful piece of knowledge, since fingerprints is the one most tutorials reference
- Identifier validation catches fabricated or mistyped IBANs/LEIs in a dataset, a cheap integrity check that catches real data problems
- Actively released (v2.6.2, 2026-11-07) under MIT by the organisation that runs the largest open sanctions dataset

## 5. Cons

- Normalisation rules are tuned for Latin-script corporate and sanctions data and are weaker on CJK and Arabic name forms, so non-Western corpora need additional handling
- Small community (73 stars, 16 open issues) — effectively an OpenSanctions internal library published openly, so documentation assumes their context
- Normalisation is lossy: the fingerprint is a matching key, not a display value, and conflating the two corrupts published names
- Bundled reference datasets (country codes, legal forms) go stale and are updated on the maintainer's cadence, not yours

## 6. Feedback (documented)

No individual user reports verified. Production evidence is structural and checkable: rigour is a dependency of nomenklatura and the OpenSanctions pipeline, which processes a continuously updated multi-source entity dataset.

## 7. Assessment

Adopt it as the first stage of any name-matching work — the quality gain from correct normalisation exceeds what a better fuzzy scorer gives you, and it is the cheapest improvement available. For your profile the specific action is to replace any use of the older fingerprints package with rigour. For CJK and Arabic material, supplement with uroman or script-specific handling rather than trusting the defaults.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-07, latest release v2.6.2 published the same day, 73 stars, 16 open issues. Frequent releases driven by production needs at OpenSanctions; small but current.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Bundled reference datasets (country codes, legal forms) — permissive, derived from public standards.

**Restrictions:** None material.

**Licence evidence:** https://github.com/opensanctions/rigour/blob/main/LICENSE

## 10. Costs

No fee, negligible resources.

## 11. Privacy and data flows

Entirely local, no network calls.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [nomenklatura](JAI-A2-30.md) for the resolution stage that follows normalisation
- [RapidFuzz](JAI-A2-43.md) for the scoring stage
- [uroman](JAI-A2-56.md) for romanising non-Latin scripts before normalisation

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/opensanctions/rigour
- https://github.com/opensanctions/rigour/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OCRmyPDF](JAI-A2-33.md) | 94 | Adopt |
| 2 | [whisper.cpp](JAI-A2-59.md) | 94 | Adopt |
| 3 | [OpenAleph](JAI-A2-35.md) | 93 | Adopt |
| 4 | [Datasette](JAI-A2-09.md) | 93 | Adopt |
| 5 | [ICIJ Datashare](JAI-A2-23.md) | 92 | Adopt |
| 6 | [Docling](JAI-A2-12.md) | 91 | Adopt |
| 7 | [noScribe](JAI-A2-31.md) | 91 | Adopt |
| 8 | [pdfplumber](JAI-A2-39.md) | 91 | Adopt |

---

← 120. [Querido Diário](OSINT-C3-14.md) · 122. [shot-scraper](SUR-B1-23.md) →
