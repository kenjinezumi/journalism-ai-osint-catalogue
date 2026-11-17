# BERTopic

`JAI-A2-04` · **82/100** · overall rank 127 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 54) |
| **Segment** | A2 · Documents and language: OCR, transcription, translation, entities, entity resolution (rank 31) |
| **Subcategory** | Topic modelling and corpus triage |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Maarten Grootendorst |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MaartenGr/BERTopic) · [Documentation](https://maartengr.github.io/BERTopic/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 82/100**

---

## 1. Purpose

Topic modelling pipeline that embeds documents, reduces dimensionality with UMAP, clusters with HDBSCAN and derives human-readable topic labels via class-based TF-IDF.

## Journalism / investigative use case

The strongest current answer to 'what is actually in this dump': cluster 200,000 leaked emails into a few hundred labelled themes, see which clusters are unexpected, and drill into those first instead of reading chronologically.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Produces topic labels a reporter can read, which is what makes it usable in a newsroom where raw LDA output is not
- Modular by design — you can swap in a local embedding model, so the whole pipeline stays offline
- Strong documentation with worked examples for dynamic (over-time) and hierarchical topic modelling, both directly useful for narrative-change stories
- Active release cadence and a 1.0 beta line, with the maintainer visibly responsive in the repo

## 5. Cons

- UMAP/HDBSCAN memory grows sharply past a few hundred thousand documents; at leak scale you need sampling, incremental fitting or a different approach, and this is the most common practical failure
- Topic labels are statistical artefacts and over-merge or split in ways that mislead if taken at face value — every cluster needs human interpretation before it informs reporting
- 480 open issues suggests support load exceeds maintainer capacity, so expect to debug integration problems yourself
- Results are sensitive to embedding model and UMAP random state; two runs can tell slightly different stories, which is awkward if you need a reproducible methodology note

## 6. Feedback (documented)

No individual deployment reports verified. The 480 open issues against 7,963 stars is itself documented evidence of a single-maintainer project with heavy user demand. I did not verify any specific newsroom deployment, so treat journalism adoption as plausible rather than evidenced.

## 7. Assessment

Genuinely useful for the triage problem, and I would pilot it on a real corpus before committing, specifically to measure the memory ceiling on your hardware. For your profile the key design decision is to fix the embedding model locally (e.g. multilingual-e5 via sentence-transformers) so no document text leaves the perimeter, and to record the random seed and model version in the methodology note so the clustering is reproducible if challenged.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release v0.17.4 (2025-12-03) with a v1.0.0b1 tag since, 7,963 stars, 480 open issues. Active commits and a 1.0 beta in flight; the large open-issue backlog indicates responsiveness limits rather than abandonment.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** Depends entirely on the embedding model you choose; not fixed by BERTopic and not verified here.

**Restrictions:** None from BERTopic itself. The licence risk is imported with the embedding model — a CC-BY-NC checkpoint would contaminate commercial use.

**Licence evidence:** https://github.com/MaartenGr/BERTopic/blob/master/LICENSE

## 10. Costs

No fee. Embedding is the cost driver: a GPU shortens a 200k-document embedding run from many hours to tens of minutes. Expect a GPU VM for hours, or a long CPU run, per corpus. Estimate only; assumptions are a mid-size sentence-transformer and a single pass.

## 11. Privacy and data flows

Local if and only if the embedding backend is local. Selecting an API-based embedding provider sends every document to a third party — a catastrophic default for leak material, and the one configuration choice that must be reviewed.

## 12. Verdict

**Pilot**

## 13. Alternatives

- [txtai](JAI-A2-55.md) for a lighter all-in-one semantic search plus clustering
- [Carrot2](JAI-A2-07.md) for labelling result sets rather than whole corpora
- [datasketch](JAI-A2-10.md) first, to collapse near-duplicates before topic modelling

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/MaartenGr/BERTopic
- https://maartengr.github.io/BERTopic/
- https://github.com/MaartenGr/BERTopic/blob/master/LICENSE

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

← 126. [InVID-WeVerify Verification Plugin](JAI-A4-04.md) · 128. [Crawlee](OSINT-C1-17.md) →
