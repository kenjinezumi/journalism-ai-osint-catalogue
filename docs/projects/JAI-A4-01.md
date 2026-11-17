# Meedan Check

`JAI-A4-01` · **80/100** · overall rank 150 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 61) |
| **Segment** | A4 · Fact-checking support and media verification (rank 3) |
| **Subcategory** | Fact-checking workflow platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Meedan |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/meedan/check) · [Documentation](https://meedan.com/check) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 4/5 · usability 3/5 · licence+cost 5/5 → **weighted 80/100**

---

## 1. Purpose

Collaborative platform for fact-checking desks: ingests claims from tiplines and social monitoring, deduplicates against previously checked items, assigns and tracks verification tasks across a team, and publishes outputs.

## Journalism / investigative use case

The operational backbone for a tipline-driven desk: a WhatsApp tipline feeds Check, incoming claims are matched against work already done, and the remaining novel claims are assigned to reporters with an auditable status trail — the difference between a desk that scales and one that re-verifies the same rumour weekly.

## 2. Audience

newsroom analyst, journalist, engineer

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Purpose-built for fact-checking desk workflow rather than adapted from generic ticketing — tipline ingestion, claim deduplication and publication are first-class
- Self-hostable under MIT, so claims and reader submissions can stay on infrastructure you control
- Used by fact-checking organisations in multiple countries and sustained by an established non-profit, giving it institutional durability
- Pairs with Alegre for similarity matching, so the deduplication is real rather than keyword-based

## 5. Cons

- Multi-service stack (Docker, PostgreSQL, Elasticsearch/OpenSearch, Redis) with non-trivial operational burden; the public dev-environment repository is not a production install, which trips teams up
- Similarity matching produces ranked probabilistic suggestions, not determinations that two claims are the same — a reviewer must adjudicate
- Optional integrations send data off-box: Google Translate API, Sentry error reporting, Smooch/Sunshine Conversations for messaging — each needs a deliberate decision
- Release cadence is modest (v0.194.0, 2026-02-10 with last push 2026-09-23), and 131 stars means a thin external community for self-hosters

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: Meedan publishes Check as the platform behind partner tiplines, and the repository shows sustained multi-year development with 131 stars and only 7 open issues. The 'dev environment, not production install' caveat is stated by the project itself.

## 7. Assessment

The right choice if you are running a claims desk with reader submissions; overkill if you are not. For your profile the honest read is that self-hosting Check is a platform-engineering commitment comparable to OpenAleph, so I would only recommend it where tipline volume justifies it. Disable the Google Translate and Sentry integrations by default — a translation call on a reader's submitted message is a disclosure of that reader's material to a third party.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-23, latest release v0.194.0 (2026-02-10), 131 stars, 7 open issues. Low open-issue count and a long release history under an established non-profit; the two-month gap since last push is normal for a platform at this stage. Classified active on institutional backing plus release history, not push recency.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a for the platform; bundled ML components live in Alegre and carry their own terms.

**Restrictions:** None material.

**Licence evidence:** https://github.com/meedan/check/blob/develop/LICENSE

## 10. Costs

No software fee. Infrastructure estimate: a multi-container deployment with PostgreSQL, Elasticsearch/OpenSearch and Redis — realistically one well-provisioned VM minimum, more for tipline volume. Optional paid dependencies if you enable Google Translate or a messaging provider (not priced here). Operating effort is the dominant cost.

## 11. Privacy and data flows

Self-hosting keeps claims and submitted media on your infrastructure, which matters because tipline content can identify the person who submitted it. The optional integrations are the exposure points and should be off by default. Reader-submitted material deserves the same handling discipline as source material.

## 12. Verdict

**Pilot**

## 13. Alternatives

- Alegre alone if you only need similarity matching inside an existing workflow
- [ClaimsKG extractor](JAI-A4-09.md) or the Google Fact Check Tools API for checking whether a claim is already debunked
- A simple issue tracker plus Alegre for a small desk that cannot operate the full stack

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/meedan/check
- https://meedan.com/check
- https://github.com/meedan/check/blob/develop/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 149. [Gephi](OSINT-C3-33.md) · 151. [Molly](SUR-B3-24.md) →
