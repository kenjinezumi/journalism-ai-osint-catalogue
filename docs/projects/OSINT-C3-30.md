# recon-ng

`OSINT-C3-30` · **59/100** · overall rank 328 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 129) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 42) |
| **Subcategory** | OSINT automation |
| **Type** | framework |
| **Bucket** | `verified-oss` |
| **Maintainer** | Tim Tomes (lanmaster53) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | GPL-3.0 (project licensing — confirm from the repository licence file) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/lanmaster53/recon-ng) · [Documentation](https://github.com/lanmaster53/recon-ng/wiki) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 3/5 · usability 3/5 · licence+cost 4/5 → **weighted 59/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 (project licensing — confirm from the repository licence file) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Third-party sources have their own terms. |
| **Restrictions** | Copyleft on the framework; immaterial for internal use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee. API keys for several modules, some paid (not priced here). Negligible compute.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/lanmaster53/recon-ng
- https://github.com/lanmaster53/recon-ng/wiki

---

## 1. Purpose

Modular reconnaissance framework with a Metasploit-style interactive console, independent modules for discovery and enrichment, and a workspace database for accumulating results.

## Journalism / investigative use case

Reconnaissance where you choose each step: run a specific module against a target, see what it returns, then decide the next module — which keeps the disclosure footprint under control, unlike an automated scan that queries everything at once.

## 2. Audience

engineer, specialist investigator

## 3. Project type

framework · bucket `verified-oss`

## 4. Pros

- Explicit per-module execution is the operational-security advantage over SpiderFoot: you know exactly which third party you just told about your target, because you chose it
- Workspace database accumulates findings across sessions, so a long investigation's reconnaissance builds rather than restarting
- Modular architecture makes writing a module for a source specific to your region a contained task
- Long-established with a familiar console idiom for anyone with security-tooling background

## 5. Cons

- Maintenance has slowed considerably, and several modules depend on sources whose access has degraded or disappeared — so module breakage is common and often silent
- Console idiom is unfamiliar to journalists and the learning curve is steeper than a CLI tool with flags
- Many modules require API keys, some paid
- Security-tooling framing throughout, so adapting the mental model to journalism takes effort

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with reduced activity. The broader degradation of search-engine and free-API sources documented elsewhere in this catalogue (pagodo, dorks_hunter, theHarvester) affects recon-ng's modules equally.

## 7. Assessment

Monitor rather than adopt: the deliberate per-module approach is the right instinct, but the framework's slowed maintenance against degraded sources means many modules no longer work. For your profile the same discipline is better achieved with a small set of individually maintained tools you invoke explicitly — subfinder, httpx, asn — where you can see each tool's health rather than discovering a module has silently returned nothing.

## 8. Maintenance

**Maintenance appears to be declining** — Verified via the GitHub API 2026-11-17 as live and non-archived, but with substantially reduced activity relative to the project's earlier period and a module ecosystem dependent on sources that have degraded. Declining rather than dormant; no deprecation notice.

## 9. Licensing

**Licence:** GPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Third-party sources have their own terms.

**Restrictions:** Copyleft on the framework; immaterial for internal use.

**Licence evidence:** https://github.com/lanmaster53/recon-ng

## 10. Costs

No fee. API keys for several modules, some paid (not priced here). Negligible compute.

## 11. Privacy and data flows

Better than an automated scanner because you choose each module and therefore each disclosure. Individual modules may actively probe — check before running.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- Slowed maintenance against degraded data sources means silent module failure

## 13. Alternatives

- A curated set of individually maintained CLI tools, which is what I would actually use
- [SpiderFoot](OSINT-C3-29.md) for automated breadth, accepting the disclosure
- [Maltego](OSINT-C3-36.md) for a graph-oriented commercial alternative

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/lanmaster53/recon-ng
- https://github.com/lanmaster53/recon-ng/wiki

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

← 327. [PhotoHolmes](JAI-A4-17.md) · 329. [Bellingcat smart-image-sorter](OSINT-C2-15.md) →
