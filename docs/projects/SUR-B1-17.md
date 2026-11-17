# webchanges

`SUR-B1-17` · **82/100** · overall rank 133 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 36) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 7) |
| **Subcategory** | Web change monitoring |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Mike Borsetti (mborsetti) |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (repository licence file; GitHub API reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/mborsetti/webchanges) · [Documentation](https://webchanges.readthedocs.io/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 4/5 · licence+cost 5/5 → **weighted 82/100**

---

## 1. Purpose

Actively developed descendant of urlwatch that monitors web pages and documents, with HTML-formatted diff reports, PDF and image text extraction, JSON handling, Playwright-based browser fetching and optional AI-generated change summaries.

## Journalism / investigative use case

Monitor official documents and dashboards that urlwatch handles poorly — PDF text, images, JSON APIs — and receive readable HTML diffs of what an agency altered. The PDF capability matters because many governments publish changes as new PDFs rather than edited pages.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- PDF and image text extraction is the decisive differentiator: monitoring a PDF-published register or guidance document is a common journalism need that most watchers cannot meet
- HTML-formatted diff reports are materially easier for a non-engineer to read than urlwatch's text output, so alerts can go to reporters directly
- Most actively developed tool in this subcategory by release cadence — v3.40.0 released on 2026-11-15, same-day push
- MIT licensed and configuration-as-code, retaining urlwatch's auditability advantage

## 5. Cons

- Effectively a single-maintainer project with a small user base (50 stars) — excellent cadence but a bus factor of one, which matters for a monitoring system you depend on
- No web UI or collaborative review, so like urlwatch it does not support team triage
- The optional AI summary feature introduces a third-party data-sharing decision: enabling it sends monitored content to an LLM provider, which newsrooms should review before use rather than discover later
- GitHub reports SPDX NOASSERTION despite the MIT licence, so compliance records need the file reference

## 6. Feedback (documented)

No individual user reports verified — 50 stars means there is little community signal to report. Documented: release v3.40.0 on 2026-11-15 with same-day push and only 6 open issues, which is an exceptional cadence-to-backlog ratio; the AI-summary feature's third-party dependency is documented by the project.

## 7. Assessment

My recommendation for a new CLI-based monitoring deployment, ahead of urlwatch, on cadence and PDF support. Two conditions for your context: leave the AI summary feature off unless you have deliberately chosen a self-hosted model endpoint, and accept the single-maintainer risk by keeping your configuration portable — the config format is close enough to urlwatch's that migration is feasible if the project stops.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-15, latest release v3.40.0 published the same day, SPDX NOASSERTION (licence MIT per the repository file), 50 stars, 6 open issues. Frequent releases and a near-empty tracker; the risk is maintainer concentration, not activity.

## 9. Licensing

**Licence:** MIT (repository licence file; GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a — the optional AI summary feature uses whichever LLM provider you configure, under that provider's terms.

**Restrictions:** None material.

**Licence evidence:** https://github.com/mborsetti/webchanges/blob/main/LICENSE

## 10. Costs

No fee. Small host; optional Playwright/Chromium adds resources. If the AI summary feature is enabled, you incur that provider's token charges (not priced here). Negligible otherwise.

## 11. Privacy and data flows

Snapshots and diffs are held locally; content leaves the machine only via configured reporters or, if enabled, the AI summary feature — which transmits monitored content to an LLM provider. Treat that feature as off by default for sensitive monitoring.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [urlwatch](SUR-B1-16.md) for the longer-established, larger-community option
- [changedetection.io](SUR-B1-15.md) for a web UI and visual diffs
- [EDGI web-monitoring-db](SUR-B1-20.md) for team-scale triage

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/mborsetti/webchanges
- https://webchanges.readthedocs.io/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |
| 9 | [urlwatch](SUR-B1-16.md) | 80 | Integrate |

---

← 132. [LlamaIndex](JAI-A3-04.md) · 134. [Qdrant](JAI-A3-07.md) →
