# Marker

`JAI-A2-28` · **86/100** · overall rank 66 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 27) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 18) |
| **Subcategory** | Document parsing and layout |
| **Type** | cli |
| **Bucket** | `source-available-weights` |
| **Maintainer** | Datalab (datalab-to, transferred from VikParuchuri) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (code) |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Mixed |
| **Software price** | **No fee below threshold** — code free; weights free below USD 5M revenue OR funding, commercial licence above (price not publicly listed). Hosted Datalab API: Free USD 0 with USD 20/10 monthly allowance, Team USD 400/month (verified 2026-11-16) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/datalab-to/marker) · [Documentation](https://github.com/datalab-to/marker#readme) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 2/5 → **weighted 86/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | Apache-2.0 (code) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | OpenRAIL-M for the Surya/Datalab weights (README 'Model License: OpenRAIL-M' linking to datalab.to/pricing). NOT OSI-approved. Commercial use above $5M revenue OR funding requires a paid licence. |
| **Restrictions** | Revenue/funding threshold on the weights is the material restriction; OpenRAIL-M also imposes use-based behavioural restrictions that flow downstream on redistribution. Code licence does not cure the weights licence. |
| **Open-source status** | **Mixed** — Open-source code, restricted model weights |
| **Software price** | **No fee below threshold** — code free; weights free below USD 5M revenue OR funding, commercial licence above (price not publicly listed). Hosted Datalab API: Free USD 0 with USD 20/10 monthly allowance, Team USD 400/month (verified 2026-11-16) |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Code free. Weights free below the threshold; above it, a commercial licence is required at a price not publicly listed (quote required). Datalab's hosted API: Free $0 pay-as-you-go with a $20/$10 monthly allowance, Team $400/month, Enterprise custom (vendor page, verified 2026-11-16, USD). Self-hosted infrastructure: one GPU host; if the LLM mode is used against a third-party API, add those token costs (not priced here).

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://www.datalab.to/pricing
- https://github.com/datalab-to/marker
- `../sources/recovered/cat/pricing.tsv`
- `../sources/evidence/leads.md`

---

## 1. Purpose

Converts PDFs, Office files and images to Markdown, JSON or HTML using the Surya model family for layout, reading order, table structure and OCR, with optional LLM-assisted accuracy enhancement.

## Journalism / investigative use case

Workhorse for turning a heterogeneous leak — mixed PDFs, Office files, scans — into clean Markdown that is searchable, diffable and quotable, with page-level traceability back to the original. In practice the best-quality local conversion available for messy real-world documents.

## 2. Audience

engineer

## 3. Project type

cli · bucket `source-available-weights`

## 4. Pros

- Conversion quality on messy multi-column and tabular documents is at or near the top of the open field, which directly reduces the downstream reading burden on reporters
- Apache-2.0 code, very active (v2.2.0, 2026-11-12), 40,946 stars — exceptional momentum and responsiveness (82 open issues)
- Handles the full pipeline (layout, reading order, tables, OCR) rather than requiring you to assemble four components
- Page-level provenance in the output makes extracted passages citable back to the source document

## 5. Cons

- The weights are NOT open source: the README labels them OpenRAIL-M and links to datalab.to/pricing, where commercial use above $5M in revenue OR funding (for Marker and Surya) requires a paid licence — verified on the vendor page 2026-11-16
- The accuracy-boosting LLM mode sends page content to an external provider unless pointed at a self-hosted model — an exfiltration path that must be explicitly closed for source material
- GPU effectively required for useful throughput on large corpora; CPU conversion of a big dump is impractical
- Two-tier licensing means your compliance position depends on your organisation's revenue and funding, which can change mid-project

## 6. Feedback (documented)

No individual user reports verified. Documented, checkable facts: 40.9k stars with 82 open issues (strong adoption and triage); and the vendor's own pricing page stating the commercial threshold verbatim — 'free for commercial use if your company is under the threshold on both revenue and funding: $2M for Chandra and $5M for Marker and Surya' (verified 2026-11-16, recorded in sources/recovered/cat/pricing.tsv).

## 7. Assessment

Technically my first choice for conversion quality, but the weights licence makes it a conditional recommendation. For a small independent newsroom or an exile outlet under the thresholds, adopt it and document the revenue/funding position in writing. For a larger publisher, or where you cannot be certain of funding levels across a consortium, Docling is the safer default even at some quality cost. Disable the LLM enhancement mode by configuration for any sensitive corpus.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v2.2.0 (2026-11-12), 40,946 stars, 82 open issues. Frequent releases, commercially backed by Datalab, low issue backlog relative to size.

## 9. Licensing

**Licence:** Apache-2.0 (code) _(SPDX verified)_

**Model / data licence:** OpenRAIL-M for the Surya/Datalab weights (README 'Model License: OpenRAIL-M' linking to datalab.to/pricing). NOT OSI-approved. Commercial use above $5M revenue OR funding requires a paid licence.

**Restrictions:** Revenue/funding threshold on the weights is the material restriction; OpenRAIL-M also imposes use-based behavioural restrictions that flow downstream on redistribution. Code licence does not cure the weights licence.

**Licence evidence:** https://www.datalab.to/pricing

## 10. Costs

Code free. Weights free below the threshold; above it, a commercial licence is required at a price not publicly listed (quote required). Datalab's hosted API: Free $0 pay-as-you-go with a $20/$10 monthly allowance, Team $400/month, Enterprise custom (vendor page, verified 2026-11-16, USD). Self-hosted infrastructure: one GPU host; if the LLM mode is used against a third-party API, add those token costs (not priced here).

## 11. Privacy and data flows

Local by default. Two explicit external paths: first-run weight download, and the optional LLM-enhancement mode which transmits page content to whatever endpoint is configured. The hosted Datalab API is a third-party custody decision and is inappropriate for unpublished source material.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Weights are OpenRAIL-M with a $5M revenue-or-funding commercial threshold — a licence decision, not a technical one

## 13. Alternatives

- [Docling](JAI-A2-12.md) — recommended where the weights licence is unacceptable or revenue exceeds the threshold
- [Surya](JAI-A2-52.md) directly for the underlying OCR/layout models without Marker's orchestration
- [PaddleOCR / PP-StructureV3](JAI-A2-37.md) for CJK and Arabic-heavy corpora

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/datalab-to/marker
- https://www.datalab.to/pricing
- `../sources/recovered/cat/pricing.tsv`
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

← 65. [Splink](JAI-A2-48.md) · 67. [Citizen Lab publication directory](SUR-B2-20.md) →
