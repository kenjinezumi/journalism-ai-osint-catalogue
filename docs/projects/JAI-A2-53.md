# Tabula

`JAI-A2-53` · **74/100** · overall rank 228 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 92) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 49) |
| **Subcategory** | Table extraction (no-code) |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Tabula / Manuel Aristarán, Mike Tigas, Jeremy Merrill (OpenNews lineage) |
| **Maintenance** | Dormant |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/tabulapdf/tabula) · [Documentation](https://tabula.technology/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 1/5 · privacy 5/5 · usability 5/5 · licence+cost 5/5 → **weighted 74/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

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
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free. Requires a Java runtime. No infrastructure.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/tabulapdf/tabula/blob/master/LICENSE
- https://github.com/tabulapdf/tabula
- https://tabula.technology/

---

## 1. Purpose

Desktop application (served as a local web UI) that lets a user draw selection boxes around tables in a PDF and export them as CSV, TSV or JSON.

## Journalism / investigative use case

The canonical no-code newsroom tool: a reporter draws a box around a table in a PDF budget or disclosure filing and gets a CSV, with no engineer, no command line and no cloud service involved. For a one-off table in a document that matters today, this remains the fastest path from PDF to spreadsheet.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Reporters can use it unaided, which is the entire point and is still unmatched for direct manual table extraction
- Runs entirely on localhost with nothing uploaded, so it is safe for sensitive documents in a way that web-based PDF converters are not
- Single Java download, no installation complexity, works offline
- Long journalism lineage (OpenNews/Knight-Mozilla origin) and the libraries beneath it (tabula-java, tabula-py) remain active

## 5. Cons

- GUI development has largely stalled: last push 2025-03-14 and the latest release v1.2.1 dates from 2018-06-04, with 541 open issues — the clearest 'frozen tool' profile in this segment
- Text-layer PDFs only; no OCR, so scans need OCRmyPDF first and reporters will not know why it 'does not work'
- Manual selection does not scale beyond a handful of documents — there is no batch mode in the GUI
- Java runtime dependency is increasingly awkward on managed newsroom laptops

## 6. Feedback (documented)

No individual user reports verified. The documented evidence is the maintenance gap itself: 7,496 stars, 541 open issues, last push March 2025, last release June 2018. The project's own ecosystem has shifted to tabula-java and tabula-py, which remain usable — so this is a GUI that has stopped evolving rather than a dead capability.

## 7. Assessment

Still worth keeping on reporters' machines because the capability is real and the alternative for a non-coder is manual retyping. But I would not treat it as a maintained tool: no releases in over seven years and 541 open issues means any bug you hit is permanent. For anything repeatable, move to Camelot or pdfplumber in a pipeline. If a newsroom standardises on it, accept that it is frozen software being used because it still works.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2025-03-14, latest release v1.2.1 (2018-06-04), 7,496 stars, 541 open issues. No release for over seven years, no push for twenty months, and a very large backlog. Classified dormant rather than archived because no deprecation notice exists and the underlying libraries (tabula-java/tabula-py) are maintained separately; the GUI itself is not being developed.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/tabulapdf/tabula/blob/master/LICENSE

## 10. Costs

Free. Requires a Java runtime. No infrastructure.

## 11. Privacy and data flows

Fully local — the UI is served from localhost and nothing is uploaded. This remains its strongest property and the reason to prefer it over any web-based PDF-to-CSV service.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- No release since 2018 and 541 open issues — frozen GUI; use the maintained libraries for anything new

## 13. Alternatives

- [Camelot](JAI-A2-06.md) for scripted extraction with confidence scores
- [pdfplumber](JAI-A2-39.md) for coordinate-level control and auditable extraction
- tabula-py / tabula-java — the maintained libraries from the same lineage, usable in a pipeline

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/tabulapdf/tabula
- https://tabula.technology/
- https://github.com/tabulapdf/tabula/blob/master/LICENSE

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

← 227. [OpenTimestamps](OSINT-C3-41.md) · 229. [DVC (Data Version Control)](OSINT-C3-38.md) →
