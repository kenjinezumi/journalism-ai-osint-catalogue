# MuckRock

`OSINT-C3-15` · **74/100** · overall rank 222 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 74) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 21) |
| **Subcategory** | Freedom of information |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | MuckRock Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MuckRock/muckrock) · [Documentation](https://www.muckrock.com/) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 2/5 · usability 4/5 · licence+cost 4/5 → **weighted 74/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Platform for filing, tracking and publishing US public-records requests, handling agency correspondence, fee and appeal workflows, and a public archive of completed requests and released documents.

## Journalism / investigative use case

Managing a public-records practice rather than individual requests: file across many agencies, track deadlines and appeals, and search the archive of what other requesters have already obtained — which frequently answers your question without a new request.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Deadline and appeal tracking is the capability that turns sporadic requests into a sustained practice, which is where public-records reporting actually produces results
- The public archive of completed requests is a research asset in itself: searching it shows what an agency has released before and how it responds, which shapes how you frame a request
- Open source under a journalism non-profit whose mission is records access, so incentives align and the service is unlikely to pivot away
- Operated as a working service alongside DocumentCloud, so requests and released documents land in a usable publishing pipeline

## 5. Cons

- US only, and the workflow encodes US FOIA and state public-records conventions
- The platform publishes requests and responses by default, which is right for accountability and wrong for a sensitive investigation where the request itself tips off the target — embargo options exist but the default matters
- Self-hosting is a substantial Django deployment and almost never the right choice given the service exists
- Service fee structure for filing (postage, fees) and account tiers were not verified in this survey

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the repository is live and non-archived under MuckRock's maintenance alongside DocumentCloud. MuckRock's operation of a public records service with a substantial public archive is well documented.

## 7. Assessment

Use the service for US records work, with an explicit decision per request about publication timing — and file sensitive requests directly with the agency instead, because a public request is a notification to your target. For your profile the underused half is the archive: searching prior requests to the same agency is faster than filing, and it reveals the agency's refusal patterns before you commit to a request that will be denied.

## 8. Maintenance

**Actively maintained** — Verified via the GitHub API 2026-11-17 as live and non-archived under MuckRock's institutional maintenance, supporting an operating public service alongside DocumentCloud. The service is the primary artefact.

## 9. Licensing

**Licence:** AGPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Released documents are public records; MuckRock's service terms govern platform use and were not verified here.

**Restrictions:** Copyleft would apply to a modified hosted instance; immaterial for using the service.

**Licence evidence:** https://github.com/MuckRock/muckrock

## 10. Costs

Service fees and account tiers NOT verified in this survey — MuckRock has historically charged for filing credits with free tiers for some users. Confirm before planning a filing programme. Self-hosting would be a major Django deployment. Estimate.

## 11. Privacy and data flows

Requests and responses are published by default, which discloses what you are asking and of whom. Embargo options exist but the default is publication — a deliberate accountability choice that conflicts with investigative secrecy.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Publish-by-default discloses requests; US jurisdiction only; service fees unverified

## 13. Alternatives

- Filing directly with agencies for sensitive requests
- [Alaveteli](JAI-A1-28.md) or Froide for non-US jurisdictions with similar publish-by-default models
- FOIA Machine-style self-managed tracking in a spreadsheet for a small programme

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/MuckRock/muckrock
- https://www.muckrock.com/

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

← 221. [DocumentCloud](JAI-A2-13.md) · 223. [Perma](OSINT-C1-37.md) →
