# dedupe

`JAI-A2-11` · **73/100** · overall rank 236 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 96) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 50) |
| **Subcategory** | Entity resolution |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | dedupe.io / Forest Gregg and Derek Eder |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/dedupeio/dedupe) · [Documentation](https://docs.dedupe.io/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 2/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 73/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Python library for fuzzy deduplication and record linkage that uses active learning: it asks a human to label borderline pairs, learns blocking predicates and comparison weights, then clusters records.

## Journalism / investigative use case

The classic newsroom tool for collapsing duplicate rows in a messy registry, donor list or permit database. The active-learning console is the point: a reporter who knows the domain supplies the match/no-match judgements, so the resolution encodes editorial knowledge rather than an engineer's guess.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Active learning puts the domain expert in the loop, which is the right division of labour for newsroom data and produces defensible clusters
- Long lineage in civic-tech and data journalism; the CSV wrappers (csvdedupe) let an analyst work without writing code
- Learns blocking predicates automatically, removing the hardest part of naive record linkage
- MIT, local, no infrastructure

## 5. Cons

- No tagged release since v3.0.3 and the repository has not been pushed since 2025-07-29 — the clearest maintenance warning in this subcategory
- Does not scale comfortably past a few million records; memory and training time become the binding constraint where Splink would not
- Results depend on the labelling session, so two reporters can produce different clusters from the same data — reproducibility requires saving and version-controlling the training file
- Documentation assumes statistical familiarity; the m/u and blocking concepts are not explained in reporter-friendly terms

## 6. Feedback (documented)

No individual user reports verified. The documented signal is negative and checkable: last push 2025-07-29 with no release since v3.0.3 against 4,530 stars and 93 open issues — a widely used library whose maintenance has visibly slowed. The commercial dedupe.io hosted service is a separate product from this library and its continued operation does not evidence library maintenance.

## 7. Assessment

I would not start a new project on dedupe in 2026. Splink does the same job with better scaling, active maintenance and auditable match weights, and is the honest recommendation for your profile. Keep dedupe in the catalogue because existing newsroom pipelines use it and because the active-learning UX is still the most reporter-friendly way to resolve a small, messy list — but treat it as a tool with a succession plan.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false, pushed_at 2025-07-29 (over 15 months stale), no GitHub release object, latest tag 'wide_windows_build', 4,530 stars, 93 open issues. Classified declining rather than dormant because the project is a finished library in wide use and no deprecation notice exists; but the absence of both commits and releases for over a year against an open issue backlog is substantive evidence, not a quiet-mature pattern.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None. Note the hosted dedupe.io service is a separate commercial product under its own terms — the MIT licence covers only this library.

**Licence evidence:** https://github.com/dedupeio/dedupe/blob/main/LICENSE

## 10. Costs

Library free. The hosted dedupe.io service is priced separately and was not verified in this survey (not publicly confirmed here). Operating cost is analyst labelling time — typically an hour or two per dataset — plus CPU.

## 11. Privacy and data flows

Fully local; the library makes no network calls. Do not confuse it with the hosted dedupe.io service, which would involve uploading your data to a third party.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- No commits or releases since July 2025 — unsuitable as a new long-term dependency

## 13. Alternatives

- [Splink](JAI-A2-48.md) — recommended replacement: scales further, actively maintained, auditable match weights
- [RapidFuzz](JAI-A2-43.md) plus manual blocking for small one-off jobs
- [nomenklatura](JAI-A2-30.md) if your data is already mapped to FollowTheMoney

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/dedupeio/dedupe
- https://docs.dedupe.io/
- https://github.com/dedupeio/dedupe/blob/main/LICENSE

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

← 235. [Overpass API](OSINT-C2-23.md) · 237. [Marginalia Search](OSINT-C1-05.md) →
