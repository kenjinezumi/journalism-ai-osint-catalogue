# Surya

`JAI-A2-52` · **78/100** · overall rank 172 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 69) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 42) |
| **Subcategory** | OCR and layout models |
| **Type** | model |
| **Bucket** | `source-available-weights` |
| **Maintainer** | Datalab (datalab-to, transferred from VikParuchuri) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 (code) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/datalab-to/surya) · [Documentation](https://github.com/datalab-to/surya#readme) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 3/5 · usability 3/5 · licence+cost 2/5 → **weighted 78/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Document OCR model suite covering text detection and recognition in 90+ languages, layout analysis, reading-order detection, table structure recognition and LaTeX/maths OCR.

## Journalism / investigative use case

High-accuracy local alternative to commercial document AI for messy multi-column reports, forms and financial tables — the model layer that makes Marker's output good, usable directly when you want the structured layout data rather than Markdown.

## 2. Audience

engineer

## 3. Project type

model · bucket `source-available-weights`

## 4. Pros

- Accuracy on complex layouts is at the top of the open field, materially better than Tesseract on multi-column and tabular material
- Covers detection, recognition, layout, reading order and table structure in one model family, so you are not stitching four research repos together
- Extremely active (v0.24.0, 2026-11-13) with a remarkably clean tracker — 2 open issues against 21,599 stars
- Runs entirely locally on your own GPU, so documents never reach a vendor

## 5. Cons

- Code is Apache-2.0 but the WEIGHTS are not open source: the README badge labels them OpenRAIL-M and links to datalab.to/pricing, where commercial use requires a licence above $5M in revenue OR funding — not an OSI licence and a real compliance decision
- The auto-spawned inference server can be pointed at a remote OpenAI-compatible endpoint, which is an exfiltration path that must be explicitly closed when handling source material
- GPU needed for real throughput; CPU inference is impractical for corpus-scale work
- As a model suite rather than a tool, you must write the orchestration — or use Marker, which inherits the same licence question

## 6. Feedback (documented)

No individual user reports verified. Checkable facts: 21,599 stars with 2 open issues (exceptional triage); and the vendor pricing page stating the threshold verbatim — '$5M for Marker and Surya' — verified 2026-11-16 and recorded in sources/recovered/cat/pricing.tsv.

## 7. Assessment

Technically excellent and licence-constrained in exactly the same way as Marker. My recommendation for your profile: if you are under the revenue/funding threshold, use Marker (which wraps Surya) rather than Surya directly, unless you specifically need the layout JSON. If you are over the threshold or cannot be certain, use Docling instead and accept a modest accuracy cost. Either way, pin the inference server to localhost so the remote-endpoint option cannot be triggered by configuration drift.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-13, latest release v0.24.0 published the same day, 21,599 stars, 2 open issues. Same-day push and release with near-zero backlog; commercially backed by Datalab.

## 9. Licensing

**Licence:** Apache-2.0 (code) _(SPDX verified)_

**Model / data licence:** OpenRAIL-M for the weights (README 'Model License: OpenRAIL-M' linking to datalab.to/pricing). NOT OSI-approved. Commercial use above $5M revenue OR funding requires a paid licence.

**Restrictions:** Revenue/funding threshold on weights; OpenRAIL-M additionally imposes use-based behavioural restrictions that flow downstream on redistribution. The Apache-2.0 code licence does not cure this.

**Licence evidence:** https://www.datalab.to/pricing

## 10. Costs

Code free; weights free below the threshold, otherwise a commercial licence at a price not publicly listed (quote required). Datalab's hosted API is priced separately: Free $0 with a $20/$10 monthly allowance, Team $400/month, Enterprise custom (verified 2026-11-16, USD). Self-hosted: one GPU host.

## 11. Privacy and data flows

Local inference; first-run weight download from HuggingFace. The material risk is the configurable remote inference endpoint — verify it points at localhost before processing source material.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Weights are OpenRAIL-M with a $5M revenue-or-funding commercial threshold

## 13. Alternatives

- [Marker](JAI-A2-28.md) for the full conversion pipeline over these same models
- [Docling](JAI-A2-12.md) where a clean permissive position on weights is required
- PaddleOCR for CJK/Arabic with Apache-2.0 code (weights unverified)

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/datalab-to/surya
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

← 171. [Atlos](OSINT-C2-36.md) · 173. [certstream-server](SUR-B2-10.md) →
