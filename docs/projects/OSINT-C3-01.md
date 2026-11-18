# OpenSanctions (dataset)

`OSINT-C3-01` · **94/100** · overall rank 8 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 5) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 1) |
| **Subcategory** | Sanctions and PEP data |
| **Type** | dataset |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | OpenSanctions Datenbanken GmbH |
| **Maintenance** | Actively maintained |
| **Licence** | MIT (code) |
| **Licence type** | Mixed (code vs weights/data) |
| **Open-source status** | Source available |
| **Software price** | **No software fee** — code free (MIT); the DATA is CC-BY-NC-4.0 — commercial use requires a paid licence, price not publicly listed (verified 2026-11-16) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/opensanctions/opensanctions) · [Documentation](https://www.opensanctions.org/docs/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 3/5 → **weighted 94/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Mixed (code vs weights/data) |
| **Exact licence (as recorded)** | MIT (code) |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | Data is CC-BY-NC 4.0; commercial use requires a paid licence (Screening Licence and Reseller/OEM are quote-only; the Screening API uses prepaid credit bundles with free credits on signup). |
| **Restrictions** | Material and the central consideration: NonCommercial bars commercial exploitation of the data, and NGO or journalism status does not automatically satisfy it. Publishing an article informed by the data is ordinary journalistic use; building a paid product or client-facing screening service on it is not. 'OpenSanctions is open source' is true of the code only. |
| **Open-source status** | **Source available** — Restricted data licence |
| **Software price** | **No software fee** — code free (MIT); the DATA is CC-BY-NC-4.0 — commercial use requires a paid licence, price not publicly listed (verified 2026-11-16) |
| **Additional costs** | **Mandatory paid dependency** — mandatory paid data licence for commercial use (quote); optional hosted Screening API (prepaid credits); self-hosted Elasticsearch |
| **Cost conditions** | **Mandatory paid dependency**; Optional paid hosting or commercial licence; Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Code and non-commercial data use free. Commercial data licence: quote required, not publicly listed (verified 2026-11-16). Self-hosting needs an Elasticsearch/OpenSearch node for yente. Hosted Screening API sold in prepaid credit bundles. Estimate for self-hosting: one 8-16GB VM.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://www.opensanctions.org/licensing/
- https://github.com/opensanctions/opensanctions/blob/main/LICENSE
- `../sources/evidence/leads.md`
- `../sources/evidence/pricing.md`

---

## 1. Purpose

Continuously built dataset of sanctioned entities, politically exposed persons, companies of interest and related entities, assembled from hundreds of official sources and published in FollowTheMoney format with the build pipeline open-sourced.

## Journalism / investigative use case

The screening layer for any investigation involving money or power: check a leaked client list, shareholder register or property dataset against sanctions and PEP data to find the names that matter. It is the difference between a spreadsheet of 40,000 names and a shortlist of twelve.

## 2. Audience

newsroom analyst, specialist investigator, engineer

## 3. Project type

dataset · bucket `source-available-restricted`

## 4. Pros

- Breadth and currency: hundreds of official source lists consolidated and rebuilt continuously, which no newsroom could replicate and which commercial screening vendors charge heavily for
- Published in FollowTheMoney, so it joins directly to your own entity data through nomenklatura and yente without a mapping project
- Code is MIT and the build pipeline is public (pushed 2026-11-17), so the provenance of every entity is traceable to its source list — which matters when a screening hit informs a published allegation
- Self-hostable with yente, so screening happens on your infrastructure and your query targets stay private

## 5. Cons

- LICENCE BLOCKER for commercial use: the DATA is CC-BY-NC 4.0 and commercial use requires a paid licence, with the Screening Licence and Reseller/OEM options quote-only (verified on the vendor licensing page). A commercially operated newsroom cannot assume its use is non-commercial
- PEP designation is a status, not an allegation: a match means a person holds or held public office or is connected to someone who does, and reporting it as suspicion would be wrong
- Entity matching produces candidates requiring adjudication — name collisions are frequent, especially for common names in transliteration, so a hit is a question not a finding
- No GitHub releases (continuous build), so pinning a dataset state for a reproducible analysis means recording the build date yourself

## 6. Feedback (documented)

No individual user reports verified in this survey. The decisive documented facts: code licence MIT (licence blob read 2026-11-17, copyright OpenSanctions Datenbanken GmbH with earlier Friedrich Lindenberg and Journalism Development Network copyrights), and data CC-BY-NC 4.0 with commercial use requiring a paid licence and quote-only enterprise tiers (vendor licensing page, verified 2026-11-16). Recorded in sources/evidence/leads.md L6 and pricing.md.

## 7. Assessment

Adopt the capability and settle the data licence explicitly in writing — that is the whole decision. Self-host with yente so query targets stay internal, and resolve whether your outlet's use is non-commercial before building a workflow on it; if it is not, price the commercial licence rather than relying on an optimistic reading of CC-BY-NC. Editorially, treat every match as a lead requiring identity confirmation, and never publish a PEP match as an implication of wrongdoing.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, no release objects (continuous build model), 878 stars, MIT code licence. Daily commits on the build pipeline with a commercial entity dependent on the dataset's currency — the strongest possible maintenance incentive.

## 9. Licensing

**Licence:** MIT (code) _(SPDX verified)_

**Model / data licence:** Data is CC-BY-NC 4.0; commercial use requires a paid licence (Screening Licence and Reseller/OEM are quote-only; the Screening API uses prepaid credit bundles with free credits on signup).

**Restrictions:** Material and the central consideration: NonCommercial bars commercial exploitation of the data, and NGO or journalism status does not automatically satisfy it. Publishing an article informed by the data is ordinary journalistic use; building a paid product or client-facing screening service on it is not. 'OpenSanctions is open source' is true of the code only.

**Licence evidence:** https://www.opensanctions.org/licensing/

## 10. Costs

Code and non-commercial data use free. Commercial data licence: quote required, not publicly listed (verified 2026-11-16). Self-hosting needs an Elasticsearch/OpenSearch node for yente. Hosted Screening API sold in prepaid credit bundles. Estimate for self-hosting: one 8-16GB VM.

## 11. Privacy and data flows

Self-hosting with yente keeps your screening queries entirely private — the decisive advantage over hosted screening APIs, which learn exactly whom you are investigating. The dataset itself concerns public figures and sanctioned entities.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Data is CC-BY-NC 4.0 — commercial-use licence required, price not publicly listed

## 13. Alternatives

- [yente](JAI-A2-61.md) for the self-hosted screening API over this data
- Official sanctions lists directly (OFAC, EU, UN) for a licence-free but far more laborious approach
- Commercial screening vendors, which are expensive and disclose your query targets

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/opensanctions/opensanctions/blob/main/LICENSE
- https://www.opensanctions.org/licensing/
- `../sources/evidence/leads.md`
- `../sources/evidence/pricing.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 7. [browsertrix-crawler](OSINT-C1-29.md) · 9. [ArchiveWeb.page](OSINT-C1-31.md) →
