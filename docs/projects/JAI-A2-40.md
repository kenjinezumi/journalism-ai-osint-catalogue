# Presidio

`JAI-A2-40` · **80/100** · overall rank 152 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 62) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 36) |
| **Subcategory** | PII detection and redaction |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | data-privacy-stack (transferred from microsoft/presidio) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/data-privacy-stack/presidio) · [Documentation](https://microsoft.github.io/presidio/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 80/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a for the framework; the NER backends you plug in carry their own model licences (spaCy, Stanza, transformers checkpoints). |
| **Restrictions** | Code unrestricted. Imported licence risk from the chosen NER model — a CC-BY-NC checkpoint would contaminate commercial use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. CPU-viable; GPU helps for transformer backends at volume. Optional Tesseract for image redaction. No paid dependencies unless you configure a hosted LLM recogniser. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/data-privacy-stack/presidio/blob/main/LICENSE
- https://github.com/data-privacy-stack/presidio
- https://microsoft.github.io/presidio/
- `../sources/evidence/leads.md`

---

## 1. Purpose

Framework for detecting and anonymising personally identifiable information in text and images, combining NER models, regex recognisers, checksum validators and context words, with pluggable anonymisation operators.

## Journalism / investigative use case

Works in both directions, which is why it matters here: find names, national IDs, IBANs and phone numbers inside a leak to map what sensitive data it contains, and redact them before publishing documents or sharing a corpus with a partner outlet — the step that prevents a collaboration from becoming a data breach.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Bidirectional utility (discovery and redaction) fits the real newsroom need: you must understand a leak's PII before you can decide what to publish
- Pluggable recognisers mean you can add country-specific identifier formats (tax numbers, passport patterns) that matter for a specific investigation
- Image redaction support covers scanned documents, not just text — a common gap in PII tooling
- Active and frequently released (2.2.366, 2026-10-27) with a large user base (11,917 stars)

## 5. Cons

- Recall on unusual name forms and non-English entities depends entirely on the chosen NER backend; out of the box it will miss transliterated names that an investigation hinges on
- Governance recently changed hands — microsoft/presidio now redirects to data-privacy-stack/presidio (verified this session) — so pin versions and watch the new stewardship before depending on it long-term
- Redaction is best-effort and must never be treated as a guarantee; published redactions need human review, and the tool's confidence scores can create false assurance
- 290 open issues; integration problems are common because the quality ceiling is set by components you supply

## 6. Feedback (documented)

No individual user reports verified. Documented and checkable: the repository transfer from Microsoft to data-privacy-stack, confirmed by API redirect on 2026-11-17 — a governance change that was not announced in the catalogue's prior data and is material for dependency planning. 11,917 stars, 290 open issues, release 2026-10-27.

## 7. Assessment

Use it as an assistive scanner, never as a redaction authority. For your profile the right pattern is: Presidio to produce a candidate list of PII locations, a human to adjudicate each one, and PyMuPDF to apply true redactions that remove underlying text. The governance transfer is worth monitoring for a release or two — the code is MIT and the community is large, so the risk is drift rather than disappearance.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release 2.2.366 (2026-10-27), 11,917 stars, 290 open issues. Note the transfer: microsoft/presidio redirects to data-privacy-stack/presidio. Activity is current; the stewardship change is the item to watch rather than a decline signal.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the framework; the NER backends you plug in carry their own model licences (spaCy, Stanza, transformers checkpoints).

**Restrictions:** Code unrestricted. Imported licence risk from the chosen NER model — a CC-BY-NC checkpoint would contaminate commercial use.

**Licence evidence:** https://github.com/data-privacy-stack/presidio/blob/main/LICENSE

## 10. Costs

No fee. CPU-viable; GPU helps for transformer backends at volume. Optional Tesseract for image redaction. No paid dependencies unless you configure a hosted LLM recogniser. Estimate.

## 11. Privacy and data flows

Local by default and appropriate for sensitive corpora. One configuration risk: optional LLM-based recognisers would send text to a third party if enabled — review before use. Note the inherent irony that a PII tool mishandled becomes a PII exposure.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [mat2](SUR-B3-07.md) for stripping file metadata rather than document content
- [PyMuPDF](JAI-A2-42.md) for applying genuine, text-removing redactions
- [x-ray](JAI-A4-23.md) to detect failed redactions in PDFs before publication

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/data-privacy-stack/presidio
- https://microsoft.github.io/presidio/
- `../sources/evidence/leads.md`

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

← 151. [Molly](SUR-B3-24.md) · 153. [Sherloq](OSINT-C2-12.md) →
