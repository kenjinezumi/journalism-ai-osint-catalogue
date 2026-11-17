# US Senate Lobbying Disclosure Act database

`SUR-B2-16` · **69/100** · overall rank 273 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 67) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 15) |
| **Subcategory** | Lobbying records |
| **Type** | dataset |
| **Bucket** | `proprietary-service` |
| **Maintainer** | US Senate Office of Public Records |
| **Maintenance** | Uncertain |
| **Licence** | US government records; specific reuse terms NOT verified in this survey |
| **Confidence** | low · **provisional** |
| **Verified** | 2026-11-17 |
| **Links** | [Documentation](https://lda.senate.gov/system/public/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 4/5 · usability 2/5 · licence+cost 4/5 → **weighted 69/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Official searchable database of lobbying registrations and quarterly activity reports filed under the US Lobbying Disclosure Act, naming clients, registrants, lobbyists, issues and expenditures.

## Journalism / investigative use case

Showing that a surveillance vendor lobbied a specific agency or on specific legislation: LDA filings name the client, the issues and often the agencies contacted, which is documentary evidence of an attempt to shape policy — the political half of a surveillance-industry story that procurement records cannot provide.

## 2. Audience

newsroom analyst, specialist investigator

## 3. Project type

dataset · bucket `proprietary-service`

## 4. Pros

- Primary official filings rather than a secondary compilation, so the record is citable and the vendor cannot dispute its own filing
- Issue descriptions and agency contacts reveal what a vendor wanted, which is frequently more revealing than the amount spent
- Quarterly cadence means a time series is available, so you can show lobbying intensifying around a procurement or a legislative moment
- Free and public with bulk data available

## 5. Cons

- The portal returned 403 to automated requests in this survey, which is bot protection rather than unavailability — but it means scripted collection needs care and may be blocked, so plan on manual or carefully-rate-limited access
- Filings are self-reported with broad issue descriptions, so a filing establishes that lobbying occurred without revealing what was said
- Coverage is federal US only, and much surveillance-policy influence occurs through channels that do not trigger LDA registration (trade associations, conferences, informal contact)
- Entity naming is inconsistent across filings, so aggregating a vendor's activity requires name normalisation

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: the portal returned HTTP 403 to curl on 2026-11-17 — recorded in sources/evidence/b2-sources.md as bot protection rather than evidence of removal, since a 403 says nothing about whether the resource exists. Verify in a browser before concluding anything about availability.

## 7. Assessment

Use it, with the honest caveat that this survey could not fully verify its current interface because of bot protection — check it in a browser before planning a pipeline. For your profile the analytically strongest use is correlation: lobbying filings by a vendor, plotted against procurement awards and legislative milestones, make a case about influence that neither dataset supports alone. OpenSecrets provides a cleaned, aggregated view that is easier to work with, at the cost of being secondary.

## 8. Maintenance

**Uncertain** — Not verifiable by automated request in this survey: the portal returned HTTP 403 to curl on 2026-11-17, which is consistent with bot protection on a live service rather than with removal. Classified Uncertain for honesty — the service is a statutory obligation and almost certainly operating, but I did not confirm it.

## 9. Licensing

**Licence:** US government records; specific reuse terms NOT verified in this survey _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same.

**Restrictions:** Not verified. US government records are generally freely reusable; confirm before publishing bulk extracts.

**Licence evidence:** https://lda.senate.gov/system/public/

## 10. Costs

Free. Cost is collection effort given bot protection, plus name normalisation.

## 11. Privacy and data flows

Public filings about organisations and named lobbyists. Your searches are visible to the portal.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Bot protection blocks automated collection; current interface not verified in this survey

## 13. Alternatives

- OpenSecrets for a cleaned, aggregated and more analysable view of the same filings
- House of Representatives lobbying disclosures for the other chamber's filings
- EU Transparency Register for the European equivalent — though its current entry point is unresolved, see the evidence note

## 14. Evidence

Verified **2026-11-17** · confidence **low** · assessment depth `docs-reviewed`

_Marked provisional: the evidence does not support a firm score._

- https://lda.senate.gov/system/public/
- `../sources/evidence/b2-sources.md`

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

← 272. [WebScrapBook](OSINT-C1-40.md) · 274. [ethereum-etl](OSINT-C3-20.md) →
