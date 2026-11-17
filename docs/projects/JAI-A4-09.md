# ClaimsKG extractor

`JAI-A4-09` · **29/100** · overall rank 361 of 361 · verdict **Avoid for new deployment**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 144) |
| **Segment** | A4 · Fact-checking support and media verification (rank 31) |
| **Subcategory** | Fact-check aggregation |
| **Type** | cli |
| **Bucket** | `uncertain` |
| **Maintainer** | ClaimsKG project (academic consortium) |
| **Maintenance** | Dormant |
| **Licence** | NOT CONFIRMED — GitHub licence API returns 404 and no LICENSE file detected; code is a fork of vwoloszyn/fake_news_extractor, compounding provenance uncertainty |
| **Confidence** | medium · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/claimskg/claimskg-extractor) · [Documentation](https://data.gesis.org/claimskg/) |

**Scores** — relevance 2/5 · capability 1/5 · maintenance 1/5 · privacy 2/5 · usability 1/5 · licence+cost 1/5 → **weighted 29/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Scraper and knowledge-graph builder that extracts published fact-checks from fact-checking websites and emits a structured RDF knowledge graph of claims, verdicts and entities.

## Journalism / investigative use case

Build a cross-organisation database of already-published fact-checks (Full Fact, Snopes, PolitiFact, Africa Check, AFP Fact Check, EUvsDisinfo) so a desk can check whether a circulating claim has already been debunked before spending reporter time on it.

## 2. Audience

engineer

## 3. Project type

cli · bucket `uncertain`

## 4. Pros

- Produces a structured, queryable knowledge graph rather than a flat list, so you can ask cross-cutting questions (which claims about a given entity have been checked, by whom, with what verdict)
- Covers a useful spread of fact-checking organisations including non-Western ones (Africa Check), which the Google Fact Check API under-represents
- Self-hosted scraping means you are not dependent on a vendor API's quota or deprecation

## 5. Cons

- Licence could NOT be confirmed: the GitHub licence API returns 404 and no LICENSE file is detected; the code is also a fork of vwoloszyn/fake_news_extractor, which compounds provenance uncertainty — reuse is legally unresolved
- Dormant: last push 2022-09-01, tag v0.2, 21 stars, 0 open issues — four years inactive, and web scrapers decay faster than almost any other code because target sites change
- Scrapes third-party fact-checker websites directly, so your crawling traffic is visible to them and may breach their terms
- English-dominant coverage despite the multi-organisation ambition

## 6. Feedback (documented)

No individual user reports verified. Documented: the licence gap (GitHub licence API 404, no LICENSE file) and the fork provenance, both recorded in session 1 and retained; last push 2022-09-01.

## 7. Assessment

Not usable as-is: a four-year-old scraper against sites that have certainly changed, with no licence. The idea is sound and worth reimplementing if cross-organisation fact-check lookup matters to you — but build it against ClaimReview markup (which publishers emit deliberately) rather than by scraping, and consider the Google Fact Check Tools API for coverage with the trade-off that queries go to Google.

## 8. Maintenance

**Dormant** — GitHub API 2026-11-17: archived=false, pushed_at 2022-09-01, latest tag v0.2, no releases, no detected licence, 21 stars, 0 open issues. Four years inactive. For a web scraper this is effectively non-functional, since target site structures will have changed.

## 9. Licensing

**Licence:** NOT CONFIRMED — GitHub licence API returns 404 and no LICENSE file detected; code is a fork of vwoloszyn/fake_news_extractor, compounding provenance uncertainty _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Unresolved. Do not redistribute or build a product on it. Separately, scraping fact-checkers' sites may breach their terms of use regardless of the code licence.

**Licence evidence:** https://github.com/claimskg/claimskg-extractor

## 10. Costs

No fee. Operating cost would be scraper maintenance, which is the dominant and recurring cost of this approach.

## 11. Privacy and data flows

Scrapes third-party fact-checker websites directly; your crawling pattern and IP are visible to those sites. No credentials required.

## 12. Verdict

**Avoid for new deployment**

## Material blockers

_Tracked separately from the score._

- No licence file and fork provenance unclear — legally unresolved
- Four-year-old scraper against changed target sites

## 13. Alternatives

- [Google Fact Check Tools API](JAI-A4-16.md) for maintained claim lookup (hosted, Google terms, ClaimReview-based coverage)
- Writing your own ClaimReview harvester against publishers' structured markup
- [Meedan Check](JAI-A4-01.md) if you need a desk workflow rather than a lookup database

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `repo-inspected`

_Marked provisional: the evidence does not support a firm score._

- https://github.com/claimskg/claimskg-extractor
- https://data.gesis.org/claimskg/

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

← 360. [NewsDiffs](SUR-B1-26.md)
