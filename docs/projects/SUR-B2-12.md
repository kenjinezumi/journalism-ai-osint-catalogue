# OpenOversight

`SUR-B2-12` · **62/100** · overall rank 313 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 76) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 20) |
| **Subcategory** | Police accountability records |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Lucy Parsons Labs |
| **Maintenance** | Stable with low activity |
| **Licence** | GPL-3.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/lucyparsons/OpenOversight) · [Documentation](https://github.com/lucyparsons/OpenOversight#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 3/5 · usability 3/5 · licence+cost 4/5 → **weighted 62/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Public, crowdsourced database and web application for identifying police officers from photographs and badge numbers, linking officers to departments, assignments and complaint records.

## Journalism / investigative use case

Identifying officers in protest footage or complaint records — the specific accountability problem where a journalist has an image and a badge number but no name, and where departments decline to assist. It is also a model for building an identifiable-public-official database in other jurisdictions.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Addresses a concrete accountability gap that journalists hit repeatedly, and does so with a crowdsourcing model that scales beyond what one newsroom could compile
- Self-hostable, so the approach is transferable to other jurisdictions and other categories of public official where records exist but are not searchable
- Built by a civil-liberties organisation with an explicit accountability purpose, so the data model and ethics are oriented to public-interest use
- Open source, so the methodology for assembling such a database is inspectable and reusable

## 5. Cons

- Jurisdiction-specific in practice: the deployed instances cover particular US departments, so outside those it is a template rather than a resource
- Building and operating such a database raises serious legal and ethical questions — data protection, accuracy obligations, the consequences of a wrong identification — that are entirely on the operator and are heavier outside the US
- A crowdsourced identification is a lead, not a fact: publishing a name from a photographic match without independent confirmation would be indefensible
- Small project with a specialist focus, so maintenance capacity is limited and a self-hosted deployment means owning the code

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. Lucy Parsons Labs operates public instances and the project's accountability purpose is documented, which is the relevant context; I verified no specific newsroom use.

## 7. Assessment

Relevant mainly as a model unless you work in a covered US jurisdiction. For your profile the transferable idea is strong — a searchable database of identifiable public officials, built from public records, is a durable accountability asset — but the legal exposure differs sharply by jurisdiction, and in Europe a comparable database of named officials with photographs would need a serious data-protection assessment before a line of code was written. Treat identifications as leads requiring independent confirmation.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived, maintained by a small civil-liberties organisation at modest velocity. Operating instances exist, which is the stronger signal for a database project than commit frequency.

## 9. Licensing

**Licence:** GPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** The database contents are compiled from public records and crowdsourced contributions; terms vary by instance and jurisdiction.

**Restrictions:** Copyleft on the application. The substantive constraints are data-protection law and accuracy obligations, which differ by jurisdiction and are far more restrictive than the software licence.

**Licence evidence:** https://github.com/lucyparsons/OpenOversight

## 10. Costs

No software fee. Self-hosting is a web application plus image storage — modest. The real costs are legal review and the editorial labour of verifying records. Estimate.

## 11. Privacy and data flows

The project's purpose is to make public officials identifiable, so its privacy posture is deliberately asymmetric: it protects contributors and exposes officials acting in a public capacity. Operating an instance makes you a data controller with the obligations that follow, which in some jurisdictions is a substantial undertaking.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- Jurisdiction-specific coverage; operating a comparable database raises significant data-protection obligations outside the US

## 13. Alternatives

- Direct public-records requests for officer rosters and assignments
- A purpose-built internal database (Datasette over curated records) scoped to one investigation
- Collaboration with a local civil-liberties organisation that already holds the records

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/lucyparsons/OpenOversight

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [mitmproxy](SUR-B2-06.md) | 96 | Adopt |
| 2 | [MobSF (Mobile Security Framework)](SUR-B2-04.md) | 88 | Adopt |
| 3 | [Citizen Lab publication directory](SUR-B2-20.md) | 86 | Reference only |
| 4 | [Exodus Privacy](SUR-B2-01.md) | 86 | Adopt |
| 5 | [USAspending.gov (custom award data)](SUR-B2-14.md) | 86 | Adopt |
| 6 | [Apktool](SUR-B2-05.md) | 86 | Adopt |
| 7 | [TED — Tenders Electronic Daily (EU public procurement)](SUR-B2-13.md) | 84 | Adopt |
| 8 | [DuckDuckGo Tracker Radar](SUR-B2-03.md) | 82 | Reference only |

---

← 312. [mapillary_tools](OSINT-C2-31.md) · 314. [uroman](JAI-A2-56.md) →
