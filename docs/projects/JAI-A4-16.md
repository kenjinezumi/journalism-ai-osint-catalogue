# Google Fact Check Tools API

`JAI-A4-16` · **57/100** · overall rank 335 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 128) |
| **Segment** | A4 · Fact-checking support and media verification (rank 16) |
| **Subcategory** | Fact-check lookup service |
| **Type** | platform |
| **Bucket** | `proprietary-service` |
| **Maintainer** | Google |
| **Maintenance** | Uncertain |
| **Licence** | Not applicable (hosted service under Google API Terms of Service); specific terms not verified in this survey |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://developers.google.com/fact-check/tools/api) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 2/5 · privacy 1/5 · usability 4/5 · licence+cost 2/5 → **weighted 57/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Hosted API with a Claim Search endpoint for querying fact-checks published worldwide as ClaimReview structured data, plus a write API for submitting your own ClaimReview markup.

## Journalism / investigative use case

Check whether a circulating claim has already been fact-checked by any publisher worldwide before spending desk time on it, and publish your own fact-checks as structured ClaimReview so they are discoverable by others — the two halves of not duplicating work.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

platform · bucket `proprietary-service`

## 4. Pros

- By far the broadest coverage of published fact-checks available through one interface, because it aggregates ClaimReview markup globally
- The write side matters strategically: emitting ClaimReview makes your own fact-checks discoverable and citable by other desks and by search surfaces
- No infrastructure to operate, and the lookup is fast enough for live use during a breaking story

## 5. Cons

- NOT open source: a hosted service under Google's API Terms, with deprecation and quota risk entirely outside your control — the same class of dependency that killed CooRnet
- Coverage is limited to publishers emitting valid ClaimReview markup, which skews toward larger and English-language organisations and silently under-represents smaller and non-Western fact-checkers
- Queries and submitted markup go to Google, so your checking activity on a sensitive subject is visible to a third party
- Licence and current pricing/quota terms were not verified in this survey — treat both as unconfirmed here

## 6. Feedback (documented)

No individual user reports verified. Documented from the project's own documentation: API users must inform their own users that results come from the Fact Check Tools API, and coverage depends on publisher ClaimReview emission. Quota and pricing details were not verified in this survey.

## 7. Assessment

Use it, with eyes open about what it is: a convenience layer over other people's structured markup, operated by a company that has retired APIs before. For your profile the asymmetry is worth noting — the write side (publishing ClaimReview) has lasting value independent of Google, because the markup is a standard; the read side is a dependency. I would emit ClaimReview regardless and treat the lookup as a useful but replaceable step, with a manual search fallback documented.

## 8. Maintenance

**Uncertain** — No repository to inspect. The service was live and documented at developers.google.com/fact-check/tools/api as of this survey, but I did not verify current quota, pricing or deprecation status from the vendor in this session. Classified Uncertain deliberately: a hosted API's maintenance cannot be evidenced the way a repository's can, and Google's API deprecation record justifies caution rather than an assumption of continuity.

## 9. Licensing

**Licence:** Not applicable (hosted service under Google API Terms of Service); specific terms not verified in this survey _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Note that the underlying ClaimReview content belongs to the publishing fact-checkers.

**Restrictions:** Service terms rather than a software licence. Documentation states an attribution obligation to end users. Republishing aggregated fact-check content raises the publishers' own rights, separate from Google's terms.

**Licence evidence:** https://developers.google.com/fact-check/tools/api

## 10. Costs

Pricing and quota NOT verified in this survey — treat as not publicly confirmed here and check the current terms before relying on it. Historically free within quota; a Google API key is required, and Search Console verification is required for the ClaimReview write API.

## 11. Privacy and data flows

Queries and submitted ClaimReview markup go to Google. Your lookup activity discloses which claims you are examining, which is a consideration if the subject is sensitive or if the target might observe published queries indirectly.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Hosted proprietary API with deprecation and quota risk outside your control; terms and pricing unverified in this survey

## 13. Alternatives

- Emitting ClaimReview markup yourself regardless of the read API
- [ClaimsKG extractor](JAI-A4-09.md) for a self-hosted database — but dormant and unlicensed
- Manual search across the major fact-checking sites as a documented fallback

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `docs-reviewed`

_Marked provisional: the evidence does not support a firm score._

- https://developers.google.com/fact-check/tools/api

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |

---

← 334. [Full Fact AI Trust Benchmark](JAI-A4-15.md) · 336. [Zingg](JAI-A1-20.md) →
