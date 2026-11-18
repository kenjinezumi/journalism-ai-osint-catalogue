# SpiderFoot

`OSINT-C3-29` · **63/100** · overall rank 301 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 115) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 36) |
| **Subcategory** | OSINT automation |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Steve Micallef (smicallef) |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT (project licensing — confirm from the repository licence file; open edition alongside a commercial product) |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/smicallef/spiderfoot) · [Documentation](https://www.spiderfoot.net/documentation/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 2/5 · usability 4/5 · licence+cost 3/5 → **weighted 63/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT (project licensing — confirm from the repository licence file; open edition alongside a commercial product) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Third-party data sources have their own terms; several restrict redistribution of results. |
| **Restrictions** | Permissive as published. Data-source terms are the practical constraint, particularly for breach-data modules whose use and republication raise separate legal and ethical questions. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid API keys for many modules (realistic capability has a recurring cost); self-hosted infrastructure |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** No fee for the open edition. Many modules require paid API keys (not priced here), so realistic capability has a recurring cost. SpiderFoot HX is a separate commercial product. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/smicallef/spiderfoot
- https://www.spiderfoot.net/documentation/

---

## 1. Purpose

OSINT automation platform with 200-plus modules that take a seed (domain, IP, email, name) and query many data sources automatically, correlating results into an entity graph with a web interface.

## Journalism / investigative use case

Automated first-pass reconnaissance on an entity: give it a company domain and it queries dozens of sources — DNS, certificates, breach data, social platforms, scan databases — assembling a correlated picture that would take a day by hand.

## 2. Audience

engineer, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Module breadth means a single scan covers ground that would otherwise require a dozen tools, which is genuinely time-saving on a new target
- Correlation into an entity graph surfaces relationships between findings rather than leaving you with a dozen separate outputs
- Web interface makes it usable by an investigator who is not comfortable in a terminal, which widens who can run reconnaissance
- Open source and self-hosted, so scan results stay with you

## 5. Cons

- Automated breadth is also the problem: a full scan queries many third-party services, disclosing your target to all of them, and some modules actively probe — so the operational-security footprint of one click is large and poorly visible
- Output volume is substantial and noisy; the correlation helps but separating signal from parked domains, breach-data false positives and stale records takes real work
- Many modules need API keys, several paid, so an unconfigured SpiderFoot delivers much less than its module count suggests
- Commercial version (SpiderFoot HX) exists, so the open edition's feature boundary and development priority warrant checking

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. SpiderFoot is well known in the OSINT community and the commercial HX edition is documented by the vendor.

## 7. Assessment

Pilot it with modules deliberately selected rather than running everything — the default breadth makes a single scan a broad disclosure of your target to dozens of third parties, which for a surveillance-industry investigation is the wrong trade. For your profile the better pattern is usually a small set of chosen tools (subfinder, httpx, asn, certstream) whose disclosure you understand, with SpiderFoot reserved for low-sensitivity targets where speed matters more than discretion.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived, with activity patterns consistent with an open edition maintained alongside a commercial product. Classified stable-low; verify the open edition's current development before depending on it.

## 9. Licensing

**Licence:** MIT (project licensing — confirm from the repository licence file; open edition alongside a commercial product) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Third-party data sources have their own terms; several restrict redistribution of results.

**Restrictions:** Permissive as published. Data-source terms are the practical constraint, particularly for breach-data modules whose use and republication raise separate legal and ethical questions.

**Licence evidence:** https://github.com/smicallef/spiderfoot

## 10. Costs

No fee for the open edition. Many modules require paid API keys (not priced here), so realistic capability has a recurring cost. SpiderFoot HX is a separate commercial product. Estimate.

## 11. Privacy and data flows

The weakest point: a broad scan discloses your target to dozens of third-party services simultaneously, and active modules touch the target directly. Select modules deliberately and use a dedicated egress.

## 12. Verdict

**Monitor**

## Material blockers

_Tracked separately from the score._

- A full scan discloses the target to many third parties at once and includes active probing

## 13. Alternatives

- A curated chain (subfinder, httpx, asn, certstream) whose disclosure footprint you understand
- [Maltego](OSINT-C3-36.md) for graph-based OSINT with commercial transforms
- [recon-ng](OSINT-C3-30.md) for a modular framework with explicit per-module execution

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/smicallef/spiderfoot
- https://www.spiderfoot.net/documentation/

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

← 300. [Alaveteli](JAI-A1-28.md) · 302. [Alegre (Meedan)](JAI-A4-02.md) →
