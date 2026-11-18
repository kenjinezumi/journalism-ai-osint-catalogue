# openstates-scrapers

`OSINT-C3-13` · **77/100** · overall rank 192 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 63) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 15) |
| **Subcategory** | Legislative records |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Open States |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/openstates/openstates-scrapers) · [Documentation](https://docs.openstates.org/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 77/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Collected legislative records are public documents; Open States' own data terms apply to the published API and bulk data and were not verified here. |
| **Restrictions** | Code permissive as published. Confirm the data terms before republishing bulk extracts. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee for the code. API access terms and limits not verified in this survey. Running scrapers yourself is a continuing maintenance cost. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/openstates/openstates-scrapers
- https://docs.openstates.org/

---

## 1. Purpose

Collection of scrapers covering US state legislatures, collecting bills, votes, legislators, committees and events into a normalised schema published via the Open States API and bulk downloads.

## Journalism / investigative use case

Tracking legislation across states: find every state where a similar surveillance or press-freedom bill has been introduced, who sponsored it and how it was voted — the comparative analysis that reveals a coordinated legislative campaign rather than a local initiative.

## 2. Audience

newsroom analyst, engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Cross-state normalisation is what makes comparative legislative analysis possible, and model-bill tracking across states is a recurring and important story type
- Covers sponsors, votes and committees rather than only bill text, so the political analysis (who pushed it, who voted how) is supported
- Data is published via an API and bulk downloads, so you can use the output without running the scrapers
- Open-source with institutional maintenance and a long operating history

## 5. Cons

- Fifty-plus jurisdictions means continuous scraper breakage, and coverage quality varies by state — some legislatures publish badly and the data reflects that
- US only, and the architecture encodes US legislative structure
- Normalisation inevitably loses state-specific procedural detail, so for a single-state story the original source is better
- API terms and any limits were not verified in this survey

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under Open States' maintenance. The project's data is used in civic-technology and journalism contexts, which is documented by the organisation.

## 7. Assessment

Use the API and bulk data rather than running the scrapers, unless a state you care about is broken and you intend to fix it. For your profile the high-value application is model-bill detection: near-identical legislative text appearing across several states is strong evidence of a coordinated campaign, and this dataset plus a text-similarity comparison (datasketch or RapidFuzz) surfaces it systematically. Verify API terms before building a dependency.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under Open States' institutional maintenance, with continuous per-state scraper work supporting an operating data service. Maintenance means ongoing repair rather than releases.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Collected legislative records are public documents; Open States' own data terms apply to the published API and bulk data and were not verified here.

**Restrictions:** Code permissive as published. Confirm the data terms before republishing bulk extracts.

**Licence evidence:** https://github.com/openstates/openstates-scrapers

## 10. Costs

No fee for the code. API access terms and limits not verified in this survey. Running scrapers yourself is a continuing maintenance cost. Estimate.

## 11. Privacy and data flows

Public legislative records; no privacy dimension beyond ordinary web access.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- US only; per-state coverage quality varies

## 13. Alternatives

- Open States API and bulk downloads instead of running scrapers — the recommended path
- LegiScan or similar commercial services for broader coverage at cost
- National parliamentary open-data portals for non-US jurisdictions

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/openstates/openstates-scrapers
- https://docs.openstates.org/

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

← 191. [MLflow](JAI-A3-19.md) · 193. [Sigstore Cosign](JAI-A3-20.md) →
