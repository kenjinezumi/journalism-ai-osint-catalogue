# Browsertrix

`OSINT-C1-30` · **83/100** · overall rank 116 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 36) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 13) |
| **Subcategory** | Archiving platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/browsertrix) · [Documentation](https://docs.browsertrix.com/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 4/5 · usability 3/5 · licence+cost 3/5 → **weighted 83/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | AGPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | AGPL-3.0: a modified self-hosted instance offered to users obliges source publication — relevant if you customise it for partner organisations. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Optional paid hosting / commercial licence; self-hosted infrastructure; staff effort |
| **Cost conditions** | Optional paid hosting or commercial licence; Self-hosting infrastructure; Staff effort |
| **Verified** | 2026-11-17 · confidence **medium** |

**Recorded cost detail.** Self-hosting: no software fee but a Kubernetes cluster plus S3-compatible storage — a four-figure annual infrastructure and ops commitment at minimum, dominated by staff time. Hosted Browsertrix is a paid service whose current prices were NOT verified in this survey — check the vendor before budgeting. Assumptions for self-hosting: small cluster, moderate capture volume.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/webrecorder/browsertrix/blob/main/LICENSE
- https://github.com/webrecorder/browsertrix
- https://docs.browsertrix.com/

---

## 1. Purpose

Multi-user web-archiving platform that orchestrates browsertrix-crawler on Kubernetes, with crawl scheduling, quality assurance review, collection management, replay and organisation-level access control.

## Journalism / investigative use case

Team-scale archiving programme where multiple reporters schedule crawls and share replayable collections — the step up from one engineer running captures to a newsroom where anyone can preserve a source and everyone can browse what has been preserved.

## 2. Audience

newsroom analyst, engineer, journalist

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Solves the organisational problem rather than the technical one: scheduling, shared collections and access control are what make archiving a newsroom capability instead of one person's habit
- Built directly on browsertrix-crawler, so capture fidelity is the same as the standalone tool with none of the configuration burden pushed onto reporters
- Quality-assurance review features let you check whether a capture actually worked before relying on it — a step most workflows skip
- Very actively developed (v1.26.6 released 2026-11-05, pushed 2026-11-17) with AGPL-3.0 source available

## 5. Cons

- Kubernetes operational burden for self-hosting is substantial — realistically it needs someone who runs Kubernetes already, and small newsrooms usually end up on the paid hosted service instead
- 341 open issues, the largest backlog in the Webrecorder stack, reflecting the surface area of a full platform
- If you use the hosted service, captures live in Webrecorder's infrastructure — a third-party custody decision that is fine for public material and not for confidential captures
- S3-compatible storage plus a cluster means this is a platform commitment, not a tool you try casually

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 501 stars with 341 open issues, release v1.26.6 (2026-11-05), tag v1.27.0-beta.0, pushed 2026-11-17. The hosted service is Webrecorder's commercial offering, which is the realistic path for teams without Kubernetes capability — its pricing was not verified in this survey.

## 7. Assessment

The right answer for a newsroom that has decided archiving is a programme, provided you can either run Kubernetes or accept hosted custody. For your profile I would be explicit about the split: hosted Browsertrix for public-interest preservation where third-party custody is acceptable, and self-hosted browsertrix-crawler for captures tied to confidential investigations. Trying to run the full platform without Kubernetes experience is the failure mode to avoid.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v1.26.6 (2026-11-05), tag v1.27.0-beta.0, 501 stars, 341 open issues. Same-day commits and frequent releases under a funded organisation; the large backlog is platform surface area rather than neglect.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified self-hosted instance offered to users obliges source publication — relevant if you customise it for partner organisations.

**Licence evidence:** https://github.com/webrecorder/browsertrix/blob/main/LICENSE

## 10. Costs

Self-hosting: no software fee but a Kubernetes cluster plus S3-compatible storage — a four-figure annual infrastructure and ops commitment at minimum, dominated by staff time. Hosted Browsertrix is a paid service whose current prices were NOT verified in this survey — check the vendor before budgeting. Assumptions for self-hosting: small cluster, moderate capture volume.

## 11. Privacy and data flows

Crawls and WACZ files are stored in your own cluster when self-hosted. On the hosted service they are held by Webrecorder — acceptable for public material, not for confidential captures. Organisation-level access control is a genuine benefit either way.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Kubernetes requirement for self-hosting; hosted option places captures in third-party custody

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md) alone for engineer-run capture without the platform
- [ArchiveBox](OSINT-C1-28.md) for a much lighter self-hosted team archive
- [Conifer](OSINT-C1-35.md) for a hosted collection-oriented alternative — but note its slower cadence

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/webrecorder/browsertrix
- https://docs.browsertrix.com/
- https://github.com/webrecorder/browsertrix/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Scrapy](OSINT-C1-16.md) | 95 | Adopt |
| 2 | [yt-dlp](OSINT-C1-45.md) | 95 | Adopt |
| 3 | [browsertrix-crawler](OSINT-C1-29.md) | 94 | Adopt |
| 4 | [ArchiveWeb.page](OSINT-C1-31.md) | 94 | Adopt |
| 5 | [ReplayWeb.page](OSINT-C1-32.md) | 94 | Adopt |
| 6 | [ArchiveBox](OSINT-C1-28.md) | 91 | Adopt |
| 7 | [Scoop](OSINT-C1-36.md) | 91 | Adopt |
| 8 | [SingleFile](OSINT-C1-38.md) | 90 | Adopt |

---

← 115. [Global Fishing Watch API client](OSINT-C2-50.md) · 117. [datasketch](JAI-A2-10.md) →
