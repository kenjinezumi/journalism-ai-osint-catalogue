# HURIDOCS preserve

`OSINT-C3-10` · **63/100** · overall rank 306 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 118) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 38) |
| **Subcategory** | Evidence preservation |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | HURIDOCS |
| **Maintenance** | Uncertain |
| **Licence** | MIT (project licensing — confirm from the repository licence file) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/huridocs/preserve) · [Documentation](https://github.com/huridocs/preserve#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 63/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a. Captured content remains the original publishers' copyright. |
| **Restrictions** | Permissive as published; confirm before redistribution. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **low** |

**Recorded cost detail.** No fee. A small service plus storage proportional to captures. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/huridocs/preserve

---

## 1. Purpose

Service that captures and preserves web content referenced in human-rights documentation, producing screenshots, text and media copies linked to records in a documentation system such as Uwazi.

## Journalism / investigative use case

Preserving the online evidence a documentation collection cites: when a Uwazi record references a social post or a government page, preserve captures it so the record remains verifiable after the source is deleted — which, for human-rights and conflict documentation, is routine rather than exceptional.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Closes the specific gap between documentation and preservation: a citation in a records system is worthless once the source disappears, and this makes capture part of the documentation workflow rather than an afterthought
- Integrates with Uwazi, so for teams on that stack preservation becomes automatic rather than a discipline someone must remember
- Built by HURIDOCS for human-rights documentation, where source deletion and takedown are expected rather than incidental
- Self-hosted, so captured evidence stays under your control

## 5. Cons

- Narrow and ecosystem-coupled: its value is largely tied to Uwazi, and outside that stack ArchiveBox or Scoop covers the same need more generally
- Small project with limited community and documentation, so adoption outside HURIDOCS' context requires reading source
- Captures are screenshots and media rather than WARC, so provenance is weaker than a browsertrix-crawler or Scoop capture
- Maintenance follows one organisation's needs

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under HURIDOCS' maintenance, designed to complement Uwazi. No independent deployment verified.

## 7. Assessment

Integrate it if you run Uwazi — automatic preservation of cited sources is exactly the right workflow and the integration is the reason to choose it over a general archiver. Outside that stack, ArchiveBox or Scoop gives you stronger captures with a larger community, and the more important point transfers either way: preservation of cited online sources should be automatic at the moment of citation, not a task someone does later, because later the source is gone.

## 8. Maintenance

**Uncertain** — Verified via the GitHub API 2026-11-17 as live and non-archived under HURIDOCS' maintenance. The project is small and maintained to support Uwazi rather than as a standalone product, so independent continuity cannot be assessed from metadata — classified Uncertain accordingly.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Captured content remains the original publishers' copyright.

**Restrictions:** Permissive as published; confirm before redistribution.

**Licence evidence:** https://github.com/huridocs/preserve

## 10. Costs

No fee. A small service plus storage proportional to captures. Estimate.

## 11. Privacy and data flows

Self-hosted captures stay internal. Your capture requests are visible to the source sites, which for a social post means the platform sees the fetch.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [ArchiveBox](OSINT-C1-28.md) for general self-hosted preservation with multi-format capture
- [Scoop](OSINT-C1-36.md) for provenance-attested single-page captures
- [browsertrix-crawler](OSINT-C1-29.md) for high-fidelity WARC capture of dynamic sources

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `metadata-verified`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/huridocs/preserve

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

← 305. [Hoover](OSINT-C3-03.md) · 307. [juditha](OSINT-C3-09.md) →
