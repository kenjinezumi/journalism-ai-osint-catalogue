# OpenRefine

`JAI-A2-36` · **87/100** · overall rank 59 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 23) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 14) |
| **Subcategory** | Data cleaning and reconciliation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenRefine community (Code for Science & Society fiscal host) |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/OpenRefine/OpenRefine) · [Documentation](https://openrefine.org/docs) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 3/5 · usability 5/5 · licence+cost 5/5 → **weighted 87/100**

---

## 1. Purpose

Desktop application for exploring, cleaning and transforming messy tabular data, with faceting, clustering algorithms, a transformation expression language (GREL), undo/redo history and a reconciliation framework for linking values to external identifier services.

## Journalism / investigative use case

The most accessible tool in this pillar: a reporter with no code can cluster 4,000 variant company names in a leaked spreadsheet down to 900 real entities, then reconcile them to Wikidata or a self-hosted yente instance for stable identifiers — and the operation history is an auditable record of every change made to the data.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Reporters genuinely use it unaided — the clustering UI is the rare case where a statistical operation is exposed in terms a non-engineer can judge
- The operation-history JSON is an underrated accountability feature: you can replay, review or publish exactly what was done to the data
- Reconciliation framework is extensible, and pointing it at your own yente instance keeps identifier lookups inside the perimeter
- Long-lived, institutionally stewarded and still actively developed (pushed 2026-11-17; release 3.10.1 2026-03-04)

## 5. Cons

- Reconciliation is the leak risk in an otherwise offline tool: it sends cell values to a web service, and the default suggestions are public endpoints — for a confidential list this is an exfiltration path hiding inside a cleaning workflow
- Clustering is heuristic and over-merges distinct entities with similar names; accepting clusters uncritically creates false identities in the data
- Large datasets strain the JVM heap, and the practical ceiling (hundreds of thousands of rows) is well below leak scale
- No probabilistic record linkage — it clusters within a column but does not link two datasets with match weights, so Splink is still needed

## 6. Feedback (documented)

No individual user reports verified. Documented signals: 12,109 stars, 738 open issues, continuous commits with a slower release cadence (3.10.1 in March 2026). OpenRefine's role in data journalism is long-established and reflected in its documentation and training materials; I verified no specific newsroom testimonial.

## 7. Assessment

Adopt it and train reporters on it — the capability-per-hour-of-training ratio is the best in the catalogue. Then write one rule: reconciliation is disabled or pointed only at an internal yente/Wikidata mirror for any dataset derived from source material. That single control turns the tool's one serious privacy flaw into a non-issue, and it is a configuration change, not a code change.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 3.10.1 (2026-03-04), 12,109 stars, 738 open issues. Daily commits with a slow, deliberate release cadence typical of a mature desktop application; the large backlog reflects a decade of accumulated requests rather than recent neglect.

## 9. Licensing

**Licence:** BSD-3-Clause _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material. Reconciliation services you connect to have their own terms.

**Licence evidence:** https://github.com/OpenRefine/OpenRefine/blob/master/LICENSE.txt

## 10. Costs

Free. Runs on a reporter's laptop; JVM heap is the only tuning concern. No paid dependencies unless you use a commercial reconciliation service.

## 11. Privacy and data flows

Cleaning and clustering are entirely local. The material exception is reconciliation, which transmits the cell values being reconciled to a third-party web service — this must be treated as a policy-controlled action for sensitive data, not a routine step.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [VisiData](JAI-A2-57.md) for terminal-based exploration of larger files
- [Splink](JAI-A2-48.md) or nomenklatura for cross-dataset probabilistic linkage
- [Datasette](JAI-A2-09.md) for sharing the cleaned result with the team

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/OpenRefine/OpenRefine
- https://openrefine.org/docs
- https://github.com/OpenRefine/OpenRefine/blob/master/LICENSE.txt

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

← 58. [libpff](JAI-A1-12.md) · 60. [osm-search](OSINT-C2-27.md) →
