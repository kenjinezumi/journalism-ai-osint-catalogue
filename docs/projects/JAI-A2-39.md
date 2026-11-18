# pdfplumber

`JAI-A2-39` · **91/100** · overall rank 33 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 11) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 8) |
| **Subcategory** | PDF text and table extraction |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Jeremy Singer-Vine |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/jsvine/pdfplumber) · [Documentation](https://github.com/jsvine/pdfplumber#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 91/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure; staff effort |
| **Cost conditions** | Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee, no infrastructure beyond Python. Cost is engineer time per document family.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/jsvine/pdfplumber/blob/stable/LICENSE.txt
- https://github.com/jsvine/pdfplumber

---

## 1. Purpose

Python library built on pdfminer.six that exposes every character, line, rectangle and curve in a PDF with coordinates, plus table-detection strategies and a visual debugging renderer.

## Journalism / investigative use case

Built by a data journalist and widely used in newsrooms: character-level coordinates let you reconstruct layout-dependent documents — disclosure forms, tabular filings, court dockets — exactly, and the visual debugger makes the extraction auditable, so you can show an editor why a figure was read from a particular cell.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Coordinate-level access is the capability that makes stubborn, layout-dependent documents extractable at all when generic parsers fail
- The visual debugger is a genuine accountability feature: you can render exactly what the extractor saw, which makes a published number defensible
- Written by and for data journalists, so the API shape matches newsroom problems (per-page, per-word, crop-and-extract)
- Pure Python with a light dependency chain — easy to install, audit and run anywhere, including air-gapped

## 5. Cons

- No OCR: text-layer PDFs only, so scans must go through OCRmyPDF first
- Table detection needs per-document strategy tuning (explicit lines versus text alignment); it is not a one-call solution at corpus scale
- Slow on very large files because it models every character, which becomes a real constraint on thousand-page documents
- 137 open issues against 10,910 stars with the last push 2026-10-15 — healthy but single-maintainer, so response times vary

## 6. Feedback (documented)

No individual user reports verified. The relevant documented context is authorship and adoption: created by a data journalist (formerly BuzzFeed News) and 10,910 stars; it is the standard recommendation in data-journalism teaching materials. I verified no specific newsroom testimonial.

## 7. Assessment

Adopt it as the default PDF-extraction library for bespoke work and pair it with Camelot for ruled tables. For your profile its distinguishing value is auditability: when a story turns on a number read out of a PDF, being able to render the extraction region is the difference between a defensible figure and an assertion. Keep OCRmyPDF upstream for scans.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-15, latest release v0.11.10 (2026-06-15), 10,910 stars, 137 open issues. Regular point releases from a single maintainer over many years; a month since last push is normal cadence for a stable library.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/jsvine/pdfplumber/blob/stable/LICENSE.txt

## 10. Costs

No fee, no infrastructure beyond Python. Cost is engineer time per document family.

## 11. Privacy and data flows

Fully local, no network, no models. Suitable for air-gapped evidence handling.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [Camelot](JAI-A2-06.md) where tables have ruling lines and a confidence score is useful
- [PyMuPDF](JAI-A2-42.md) for speed and rasterisation — but note its AGPL licence
- pypdf for simple text and page manipulation under a BSD-style licence

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/jsvine/pdfplumber
- https://github.com/jsvine/pdfplumber/blob/stable/LICENSE.txt

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
| 9 | [Buzz](JAI-A2-05.md) | 90 | Adopt |

---

← 32. [noScribe](JAI-A2-31.md) · 34. [Scoop](OSINT-C1-36.md) →
