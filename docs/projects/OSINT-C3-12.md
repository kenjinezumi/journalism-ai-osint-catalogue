# Juriscraper

`OSINT-C3-12` · **73/100** · overall rank 243 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 82) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 25) |
| **Subcategory** | Court records scraping |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Free Law Project |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause (project licensing — confirm from the repository licence file) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/freelawproject/juriscraper) · [Documentation](https://github.com/freelawproject/juriscraper#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 73/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | BSD-2-Clause (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Retrieved court records are generally public documents. |
| **Restrictions** | Permissive as published. Scraping court sites is ordinary access to public records, though rate limits and courtesy apply. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. Negligible compute; the real cost is scraper maintenance if you extend it. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/freelawproject/juriscraper

---

## 1. Purpose

Library of scrapers for US federal and state court websites, retrieving opinions, oral arguments and docket information in a normalised format, maintained per court.

## Journalism / investigative use case

Monitoring courts that CourtListener does not cover well, or building your own alerting on a specific court's filings — the per-court scraper model means you can add a court that matters to your beat rather than waiting for coverage.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Per-court scraper architecture is the right design for a fragmented jurisdiction landscape, and the normalised output means courts become comparable
- Maintained by the organisation that depends on it operationally for CourtListener, so the scrapers are exercised daily against real sites
- BSD-family licence with a long history and active maintenance, so it is a dependency you can build on
- Adding a court is a contained task, so extending coverage to a court on your beat is realistic rather than a project

## 5. Cons

- Court websites change constantly, so scraper breakage is continuous — the maintenance burden is intrinsic and visible in the project's issue flow
- US only, and the architecture encodes US court conventions, so adapting it to another jurisdiction would be a substantial rewrite
- Engineer-facing with no interface, so it is infrastructure for a monitoring system you build
- For most purposes CourtListener's API gives you the same data without running scrapers, so Juriscraper is for the gaps

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under Free Law Project's maintenance, with scrapers exercised in CourtListener's production ingest — which is the strongest form of evidence that they work.

## 7. Assessment

Integrate it only to fill gaps CourtListener leaves, or to monitor a specific court with your own alerting. For your profile the general lesson is the one warn-scraper also teaches: per-jurisdiction scrapers are a continuing maintenance commitment, and the honest way to run them is to accept that cost explicitly or to rely on an organisation that already does — which, for US courts, is Free Law Project.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under Free Law Project's maintenance, with continuous per-court fixes driven by CourtListener's production requirements. Maintenance here means ongoing scraper repair rather than feature releases.

## 9. Licensing

**Licence:** BSD-2-Clause (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Retrieved court records are generally public documents.

**Restrictions:** Permissive as published. Scraping court sites is ordinary access to public records, though rate limits and courtesy apply.

**Licence evidence:** https://github.com/freelawproject/juriscraper

## 10. Costs

No fee. Negligible compute; the real cost is scraper maintenance if you extend it. Estimate.

## 11. Privacy and data flows

Your scraping is visible to the court websites, which is unremarkable for public records.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [CourtListener](OSINT-C3-11.md)'s API, which covers most needs without running scrapers
- Writing a single bespoke scraper for one court you care about
- National court portals and their own alerting where available

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/freelawproject/juriscraper

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

← 242. [sherpa-onnx](JAI-A2-46.md) · 244. [Oxigraph](JAI-A3-17.md) →
