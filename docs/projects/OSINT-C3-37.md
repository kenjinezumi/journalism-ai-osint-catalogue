# Timesketch

`OSINT-C3-37` · **81/100** · overall rank 146 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 47) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 11) |
| **Subcategory** | Collaborative timeline analysis |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Google (open source) |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/google/timesketch) · [Documentation](https://timesketch.org/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 5/5 → **weighted 81/100**

---

## 1. Purpose

Collaborative forensic timeline-analysis platform where investigators import timestamped events from many sources, search and filter them, tag and comment on entries, and build a shared narrative timeline.

## Journalism / investigative use case

Building a shared, evidenced chronology on a complex investigation: import timestamped events from documents, logs, flight records, filings and messages, then let several reporters tag, annotate and query them together — which is how a multi-strand investigation's timeline stops living in one person's notebook.

## 2. Audience

newsroom analyst, specialist investigator, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Collaborative timeline analysis is a genuine gap in newsroom tooling: every complex investigation needs a chronology, and almost all of them are maintained as a document that goes stale
- Tagging and commenting on individual events with attribution means the timeline carries its own evidence and reasoning, which is what makes it defensible later
- Apache-2.0 and self-hostable, actively maintained by Google's security team with real production use in incident response
- Search and filtering over large event sets means the timeline scales past what a document can hold

## 5. Cons

- Designed for digital forensics and incident response, so the import formats and vocabulary assume log data rather than documents, filings and human events — adapting it to journalistic sources means writing importers
- Operational commitment: OpenSearch plus PostgreSQL plus the application, comparable to running a search platform
- Corporate-maintained open source with no commercial obligation to the project, so continuity depends on one team's priorities within a large company
- The learning curve and forensic framing will deter the reporters who would most benefit from a shared timeline

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived under Google maintenance. Timesketch's use in digital forensics and incident response is well documented; journalism use is uncommon and unverified here.

## 7. Assessment

Worth piloting on one complex investigation, specifically because the shared-chronology problem is real and under-served — but expect to write importers to get journalistic sources in. For your profile the pragmatic alternative is a disciplined Datasette-over-SQLite timeline with a fixed schema, which lacks the collaborative tagging but costs a day rather than a deployment. Choose Timesketch if the investigation is long and several people need to work the chronology together.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under Google's maintenance with continuing development. Corporate-maintained open source with production use in incident response; continuity depends on internal priorities rather than a foundation.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/google/timesketch/blob/master/LICENSE

## 10. Costs

No fee. Infrastructure: OpenSearch plus PostgreSQL plus the application — one well-provisioned VM minimum, more as event volume grows. Importer development is the other real cost. Estimate.

## 11. Privacy and data flows

Self-hosted; timeline data and annotations stay internal. The timeline will contain your investigative reasoning as well as evidence, so it is a sensitive artefact deserving the same protection as source material.

## 12. Verdict

**Pilot**

## 13. Alternatives

- A structured SQLite timeline published with Datasette, which is far cheaper and lacks collaboration features
- A shared spreadsheet with a fixed schema and discipline, which is what most investigations actually use
- Aeon Timeline or similar commercial tools, accepting proprietary software and local-only storage

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/google/timesketch
- https://timesketch.org/
- https://github.com/google/timesketch/blob/master/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 145. [pywb](OSINT-C1-27.md) · 147. [Privacy Badger](SUR-B3-33.md) →
