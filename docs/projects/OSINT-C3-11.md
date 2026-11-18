# CourtListener

`OSINT-C3-11` · **84/100** · overall rank 104 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 31) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 6) |
| **Subcategory** | Court records |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Free Law Project |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/freelawproject/courtlistener) · [Documentation](https://www.courtlistener.com/help/api/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 84/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | Court opinions are generally public records; API terms govern bulk access and were not itemised in this survey. |
| **Restrictions** | AGPL-3.0 on the platform code. API terms and rate limits govern use of the service — check before heavy automated use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free to use the public service and API within limits; bulk access terms not verified in this survey. PACER itself charges per page, which RECAP mitigates. Self-hosting would be a substantial infrastructure and storage commitment and is not recommended. Estimate.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/freelawproject/courtlistener/blob/main/LICENSE
- https://github.com/freelawproject/courtlistener
- https://www.courtlistener.com/help/api/
- `../sources/recovered/a1disc/notes.md`

---

## 1. Purpose

Platform and public database of US federal and state court opinions, dockets and filings, with full-text search, citation analysis, alerts and a comprehensive REST API, plus the RECAP archive of PACER documents.

## Journalism / investigative use case

The primary route into US litigation: search dockets and filings across courts, set alerts on a case or a party, and pull documents through the API — including the RECAP archive, which holds PACER filings that would otherwise cost money per page to retrieve.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- The RECAP archive is the standout: PACER charges per page, and RECAP makes previously purchased filings free, which materially changes what court reporting is affordable
- Comprehensive API with alerts, so monitoring a case or a litigant is automatable rather than a manual check — the basis of a genuine court beat
- AGPL-3.0 (licence verified in session 1 by reading the text) and operated by a non-profit whose mission is open legal data, so the continuity incentives align with yours
- Citation analysis and the eyecite integration mean you can follow precedent and find related filings systematically

## 5. Cons

- US only, so it is irrelevant outside that jurisdiction except where a US case touches your story
- Coverage is uneven: state-court coverage is far thinner than federal, and RECAP only holds what someone has already purchased and contributed — so absence of a filing means nothing
- Self-hosting the platform is a serious undertaking (Django, PostgreSQL, Elasticsearch, substantial storage) and almost never the right choice given the public service exists
- API rate limits and terms apply, and sustained heavy use should be discussed with the operator rather than assumed

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: session 1's a1disc/notes.md independently recorded 'courtlistener AGPL-3.0' after reading the licence text, resolving a NOASSERTION. Free Law Project's operation of CourtListener and RECAP is well documented and extensively used in US legal and investigative journalism.

## 7. Assessment

Adopt the service (not the self-hosted platform) if any of your work touches US courts — the API plus alerts is the foundation of a court beat, and RECAP's economics are decisive. For your profile the practical note is to contribute back: the RECAP extension uploads filings you purchase, which both reduces cost for others and builds the archive you depend on. Treat gaps in coverage as gaps, not as evidence that no filing exists.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under Free Law Project's maintenance, with continuous development supporting an operating public service. Session 1 verified the AGPL-3.0 licence by reading the text. The operating service is the stronger maintenance signal.

## 9. Licensing

**Licence:** AGPL-3.0 (verified in session 1 by reading the licence text, resolving a GitHub NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Court opinions are generally public records; API terms govern bulk access and were not itemised in this survey.

**Restrictions:** AGPL-3.0 on the platform code. API terms and rate limits govern use of the service — check before heavy automated use.

**Licence evidence:** https://github.com/freelawproject/courtlistener/blob/main/LICENSE

## 10. Costs

Free to use the public service and API within limits; bulk access terms not verified in this survey. PACER itself charges per page, which RECAP mitigates. Self-hosting would be a substantial infrastructure and storage commitment and is not recommended. Estimate.

## 11. Privacy and data flows

Queries go to CourtListener, disclosing which cases and parties you are researching to a non-profit operator — low risk, but non-zero if the subject is sensitive. Self-hosting is impractical, so Tor is the realistic mitigation if query privacy matters.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- US jurisdiction only; state-court and RECAP coverage is incomplete

## 13. Alternatives

- PACER directly, at per-page cost
- juriscraper for scraping court sites not covered by CourtListener
- National court portals for non-US jurisdictions

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/freelawproject/courtlistener
- https://www.courtlistener.com/help/api/
- `../sources/recovered/a1disc/notes.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |
| 9 | [edgartools](OSINT-C3-17.md) | 82 | Adopt |

---

← 103. [Hush Line](SUR-B3-06.md) · 105. [Nextcloud](SUR-B3-28.md) →
