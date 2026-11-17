# Journalism AI, surveillance and OSINT tooling catalogue

An assessed, ranked and evidenced catalogue of **361 open-source projects, datasets and services** used in investigative journalism, surveillance research and open-source investigation.

Every project carries a fourteen-field assessment, a six-dimension score, a maintenance classification with its evidence, a licence position verified against the licence file, and an explicit record of what could not be verified.

**Research verification dates: 2026-11-16 and 2026-11-17.** Each assessment records its own date. No project in this catalogue was installed or run — see [Methodology](docs/methodology.md) for what that means for the capability judgements.

## Who this is for

Engineers and technically-minded editors supporting independent journalism and media organisations, including media in exile, who can self-host, build integrations and run local AI. Hostile-state threat models and source protection are weighted accordingly: privacy and deployment control carry 15% of every score.

## Three research areas

| Pillar | Projects | Covers | Index |
|---|--:|---|---|
| **Journalism and AI** | 144 | segments A1, A2, A3, A4 | [journalism-ai.md](docs/journalism-ai.md) |
| **Surveillance and journalist protection** | 80 | segments B1, B2, B3 | [surveillance.md](docs/surveillance.md) |
| **OSINT and digital investigations** | 137 | segments C1, C2, C3 | [osint.md](docs/osint.md) |

## Summary statistics

Calculated from [`records/`](records/) at build time; 361 projects, 0 validation errors.

### Verdicts

| Verdict | Projects |
|---|--:|
| Adopt | 137 |
| Integrate | 90 |
| Pilot | 47 |
| Monitor | 46 |
| Reference only | 30 |
| Avoid for new deployment | 11 |

### Maintenance

| Status | Projects |
|---|--:|
| Actively maintained | 228 |
| Stable with low activity | 72 |
| Maintenance appears to be declining | 18 |
| Dormant | 25 |
| Archived or discontinued | 6 |
| Uncertain | 12 |

### Licence bucket

| Bucket | Projects |
|---|--:|
| verified-oss | 325 |
| source-available-restricted | 15 |
| proprietary-service | 12 |
| uncertain | 7 |
| source-available-weights | 2 |

### Evidence confidence

| Confidence | Projects |
|---|--:|
| high | 251 |
| medium | 97 |
| low | 13 |

23 assessments are marked **provisional**. 149 projects carry at least one **material blocker** — recorded separately from the score, so a project can rank well and still be unusable for a particular organisation. Both are listed in [Findings and limitations](docs/findings-and-limitations.md).

### Segments

| Segment | Projects |
|---|--:|
| A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow | 32 |
| A2 · Documents and language: OCR, transcription, translation, entities, entity resolution | 61 |
| A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation | 20 |
| A4 · Fact-checking support and media verification | 31 |
| B1 · Monitoring public information, narratives, disinformation, censorship and harassment | 27 |
| B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech | 20 |
| B3 · Protecting journalists and sources | 33 |
| C1 · Web and social research, archives and evidence capture | 45 |
| C2 · Image/video verification, geolocation, satellite, aviation and maritime | 50 |
| C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration | 42 |

## Navigation

| Page | Contents |
|---|---|
| [Complete ranking](docs/rankings.md) | All 361 projects ranked, with score breakdowns and distributions |
| [Journalism and AI](docs/journalism-ai.md) | Pillar index and the A1–A4 segment rankings |
| [Surveillance and journalist protection](docs/surveillance.md) | Pillar index and the B1–B3 segment rankings |
| [OSINT and digital investigations](docs/osint.md) | Pillar index and the C1–C3 segment rankings |
| [Project assessments](docs/projects/) | One page per project, keyed by stable project ID |
| [Methodology](docs/methodology.md) | Research method, verification standard, scoring rubric, confidence definitions |
| [Suggested stacks](docs/stacks.md) | Three tool combinations for different team shapes |
| [Findings and limitations](docs/findings-and-limitations.md) | Licensing, maintenance and pricing findings; blockers; unresolved questions; coverage gaps |
| [Complete consolidated report](report.md) | Everything in one file, including all 361 assessments |

### Data exports

| File | Format | Contents |
|---|---|---|
| [`catalogue.json`](catalogue.json) | JSON | Complete structured export — 361 projects with every field, plus computed ranks and summary counts |
| [`catalogue.csv`](catalogue.csv) | CSV | Spreadsheet-friendly export — 361 rows, 43 columns; list fields are pipe-separated |
| [`records/`](records/) | JSON | Canonical hand-authored records; everything else is generated from these |
| [`sources/evidence/`](sources/evidence/) | Markdown, text | Resolved research leads, pricing evidence, source-URL verification, retrieved licence texts |
| [`work/meta.jsonl`](work/meta.jsonl) | JSON Lines | GitHub metadata sweep over 583 candidate repositories, 2026-11-17 |

## The 20 projects to examine first

This is a curated shortlist, not the top 20 by score. It is ordered by what I would actually do
first, and it deliberately includes two items that score lower because they close a gap nothing
else covers.

| # | Project | Why first |
|---|---|---|
| 1 | **Dangerzone** ([SUR-B3-03](docs/projects/SUR-B3-03.md), 92) | Nothing else protects you at the point of first contact with an unknown document. Automate it at ingest before adopting anything else in the document pillar. |
| 2 | **ICIJ Datashare** ([JAI-A2-25](docs/projects/JAI-A2-25.md), 92) | Desktop mode is the shortest path from "we received a dump" to "reporters are searching it" with no infrastructure. Try it before considering OpenAleph. |
| 3 | **OpenAleph** ([JAI-A2-35](docs/projects/JAI-A2-35.md), 93) | If your investigations are entity-centric, this is the platform — and this session settled the fork question: OpenAleph released 5.4.0 on 2026-11-16, upstream Aleph last released 4.1.7 in October 2025. |
| 4 | **whisper.cpp + Buzz** ([JAI-A2-59](docs/projects/JAI-A2-59.md) / [JAI-A2-05](docs/projects/JAI-A2-05.md)) | A single binary and a desktop app that together stop interviews being uploaded to cloud transcription. The behavioural change is the point. |
| 5 | **SecureDrop** ([SUR-B3-01](docs/projects/SUR-B3-01.md), 92) | If you solicit documents from sources at real risk, this is the standard. Adopt it properly or say publicly what you do not offer. |
| 6 | **mat2** ([SUR-B3-07](docs/projects/SUR-B3-07.md), 94) | Metadata stripping on the publication path. Two open issues, release 0.15.0, and it prevents a failure that has burned sources. |
| 7 | **x-ray** ([JAI-A4-23](docs/projects/JAI-A4-23.md), 86) | Sweep incoming documents for failed redactions, and sweep your own before release. Both directions matter. |
| 8 | **FreshRSS + RSSHub** ([JAI-A1-03](docs/projects/JAI-A1-03.md) / [JAI-A1-05](docs/projects/JAI-A1-05.md), 94 / 91) | The cheapest substantial monitoring capability in the catalogue. Self-hosted, so your feed list is not a product dataset. |
| 9 | **llama.cpp + Ollama** ([JAI-A3-01](docs/projects/JAI-A3-01.md) / [JAI-A3-02](docs/projects/JAI-A3-02.md), 96 / 94) | One GPU host with an OpenAI-compatible endpoint makes "does this document leave the building" an infrastructure decision taken once. |
| 10 | **browsertrix-crawler + ReplayWeb.page** ([OSINT-C1-29](docs/projects/OSINT-C1-29.md) / [OSINT-C1-32](docs/projects/OSINT-C1-32.md), 94 / 94) | Capture that holds up and replay that a lawyer can open from a single file with no software. |
| 11 | **Scoop** ([OSINT-C1-36](docs/projects/OSINT-C1-36.md), 90) | Provenance-attested capture for the specific pages a story cites. Verify the signing format with Harvard LIL before relying on it legally — this survey did not. |
| 12 | **EFF Rayhunter** ([SUR-B3-13](docs/projects/SUR-B3-13.md), 88) | Makes IMSI-catcher detection possible on tens-of-dollars hardware. Baseline before treating anomalies as detections. |
| 13 | **OpenSanctions + yente** ([OSINT-C3-01](docs/projects/OSINT-C3-01.md) / [JAI-A2-61](docs/projects/JAI-A2-61.md), 94 / 84) | Screening on your own infrastructure so you do not tell a vendor whom you are investigating. Settle the CC-BY-NC data licence in writing first. |
| 14 | **Splink** ([JAI-A2-48](docs/projects/JAI-A2-48.md), 86) | Replace dedupe. Auditable match weights are the difference between a defensible linkage and an assertion. |
| 15 | **bellingcat/osm-search + streetlevel** ([OSINT-C2-27](docs/projects/OSINT-C2-27.md) / [OSINT-C2-32](docs/projects/OSINT-C2-32.md), 88 / 82) | The two halves of practical photo geolocation. Note that streetlevel uses providers' internal interfaces and discloses your coordinates. |
| 16 | **ShadowFinder** ([OSINT-C2-17](docs/projects/OSINT-C2-17.md), 91) | Physics-based falsification of a claimed time and place. Use the local CLI, not the documented Colab route. |
| 17 | **CryptPad** ([SUR-B3-27](docs/projects/SUR-B3-27.md), 92) | Replaces the shared planning document on a third-party cloud — the most common and least-discussed leak in investigative work. |
| 18 | **Datasette + DuckDB** ([JAI-A2-09](docs/projects/JAI-A2-09.md) / [JAI-A1-19](docs/projects/JAI-A1-19.md), 93 / 86) | Fastest route from extracted data to something reporters can search, and from a large file to SQL on a laptop. |
| 19 | **Haystack** ([JAI-A3-05](docs/projects/JAI-A3-05.md), 86) | If you build document question-answering, build it on an auditable pipeline with built-in evaluation. Measure faithfulness before anyone relies on it. |
| 20 | **PMTiles + MapLibre** ([JAI-A1-24](docs/projects/JAI-A1-24.md) / [JAI-A1-22](docs/projects/JAI-A1-22.md), 87 / 87) | Self-hosted map publishing with no tile server and no third-party provider watching your readers. Build the pipeline once. |

Two deliberate inclusions below their score: **Rayhunter** (88) and **Scoop** (90) rank outside
the top 20 by points but close capability gaps nothing else in the catalogue covers.

Two high scorers deliberately *not* in the shortlist: **mitmproxy** (96) and **ExifTool** (96)
are superb and you almost certainly already have them — they rank first on ubiquity and
reliability, which is exactly why they need no examination.

## Reading an assessment

### Verdicts

| Verdict | Meaning |
|---|---|
| **Adopt** | Deploy it; the assessment states any conditions |
| **Integrate** | Worth building into a pipeline or stack as a component |
| **Pilot** | Promising, but evaluate on your own material before committing |
| **Monitor** | Not now; a specific change would alter the judgement |
| **Reference only** | Useful to read, cite or learn from, not to deploy |
| **Avoid for new deployment** | Do not build on it; a named alternative is given |

### Evidence confidence

Recorded separately from the score and never folded into it.

| Confidence | Meaning |
|---|---|
| **high** | Primary sources verified — licence file read, API metadata captured, official pricing page retrieved |
| **medium** | Official documentation or README reviewed; some fields inferred from reliable secondary sources |
| **low** | Limited or conflicting evidence; several fields unverified |

An assessment marked **provisional** still carries a score for comparability, with the gap stated in its Evidence section.

### Material blockers

A licence, dependency or operational-security problem that would stop a deployment. Blockers are listed in their own field on each project page and are **not** folded into the score, so they stay visible on projects that otherwise rank well — a non-commercial model licence, a withdrawn platform API, or a tool that uploads source material by default.

### Maintenance classifications

| Status | Basis |
|---|---|
| **Actively maintained** | Substantive commits plus releases, issue throughput, or institutional backing with a security process |
| **Stable with low activity** | Mature and functionally complete; low velocity is appropriate, not a penalty |
| **Maintenance appears to be declining** | Activity has slowed materially against an open backlog, with no deprecation notice |
| **Dormant** | No substantive activity for an extended period; dependency rot likely |
| **Archived or discontinued** | `archived=true` on the API, or the upstream capability has been withdrawn |
| **Uncertain** | Maintenance cannot be evidenced — typically a hosted service with no public repository |

A recent push does not establish active maintenance, and infrequent commits do not establish abandonment. Each classification states its reasoning.

## Repository layout

```
README.md                  this page (generated)
report.md                  complete consolidated report (generated)
catalogue.json             structured export (generated)
catalogue.csv              tabular export (generated)
build.py                   generator — reads records/ + narrative/, writes everything else
records/                   canonical project records, hand-authored JSON
narrative/                 hand-authored prose fragments composed into the pages
docs/                      browsable pages (generated)
  methodology.md
  rankings.md
  journalism-ai.md  surveillance.md  osint.md
  stacks.md
  findings-and-limitations.md
  projects/                one page per project, named by project ID
sources/evidence/          research leads, pricing, URL verification, licence texts
sources/recovered/         first-session research artefacts, preserved unmodified
work/                      metadata sweep output and the scripts that produced it
STATE.md                   project state, open questions and next actions
```

## Updating and regenerating

The canonical data is [`records/`](records/) and the prose fragments in [`narrative/`](narrative/). **Do not hand-edit** `README.md`, `report.md`, `catalogue.json`, `catalogue.csv` or anything under `docs/` — they are overwritten on every build.

To change an assessment, edit the project's object in the relevant `records/<SEGMENT>-NN.json` file. To add a project, append an object with all required fields and a new unused ID in the segment's series. Then:

```sh
python3 build.py
```

The build validates every record before writing anything: required fields present, verdict and maintenance status drawn from the controlled vocabularies, all six scores integers in 0–5, and no duplicate project IDs. It prints a validation-error count and a per-segment breakdown. The committed state builds with **zero validation errors**; treat any error as a blocker rather than a warning.

Ranks, counts, distribution tables, cross-references and all three exports are derived at build time, so they cannot drift from the records. Project IDs are stable and are the primary key across the records, the exports, the per-project pages and the cross-references between assessments.

## Status and intended use

This is a research catalogue prepared for internal use and possible later publication. It records judgements and the evidence behind them; it does not constitute an audit, a security review or a legal opinion. Licence summaries are research notes read from licence files on the dates stated — they are not legal advice, and several entries flag questions that need a lawyer rather than another survey. Prices were read from vendor pages on the dates stated and change without notice.

No licence has been chosen for this repository yet. That is a decision to take before any publication, and it needs to account for the third-party licence texts preserved under [`sources/evidence/licences/`](sources/evidence/licences/), which remain under their original terms.

