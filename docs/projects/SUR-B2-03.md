# DuckDuckGo Tracker Radar

`SUR-B2-03` · **82/100** · overall rank 129 of 361 · verdict **Reference only**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 35) |
| **Segment** | B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech (rank 8) |
| **Subcategory** | Tracker reference dataset |
| **Type** | dataset |
| **Bucket** | `source-available-restricted` |
| **Maintainer** | DuckDuckGo |
| **Maintenance** | Actively maintained |
| **Licence** | CC-BY-NC-SA-4.0 (licence blob read 2026-11-17; GitHub reports NOASSERTION) — a DATASET licence, not a software licence |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/duckduckgo/tracker-radar) · [Documentation](https://github.com/duckduckgo/tracker-radar#readme) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 2/5 → **weighted 82/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Regularly regenerated dataset describing the most common third-party domains on the web: who owns them, what they do, their prevalence, fingerprinting behaviour and cookie usage.

## Journalism / investigative use case

The reference layer that turns a tracker domain into a named company: Blacklight tells you a site contacted a particular third-party domain, and Tracker Radar tells you which corporate entity owns it and what it does — which is the step that makes a story nameable rather than technical.

## 2. Audience

newsroom analyst, engineer, specialist investigator

## 3. Project type

dataset · bucket `source-available-restricted`

## 4. Pros

- Ownership attribution at scale is the specific gap it fills, and doing it yourself would mean weeks of corporate research per domain
- Actively regenerated with dated releases (2026.11.10 on 2026-11-10; pushed 2026-11-16), so prevalence figures reflect the current web rather than a snapshot
- Includes fingerprinting and cookie behaviour per domain, so you can characterise what a tracker does, not merely that it is present
- Public and free to consult, backed by a company with a commercial interest in its accuracy

## 5. Cons

- LICENCE BLOCKER: the licence file states CC BY-NC-SA 4.0 — NonCommercial bars use by a commercially operated newsroom in a product or derived dataset, and ShareAlike means any derivative dataset you publish must carry the same licence. GitHub reports NOASSERTION, so scanners will not flag this
- It is a dataset, not software, and should not be described as open-source tooling — the crawler that produces it (duckduckgo/tracker-radar-collector) is separately licensed and must be checked on its own terms
- Coverage is of common third parties, so the obscure regional tracker on a government site in a smaller market may be absent
- Ownership data ages as companies are acquired, so an attribution should be re-checked against corporate records before publication

## 6. Feedback (documented)

No individual user reports verified in this survey. The decisive documented fact, read from the licence blob on 2026-11-17: 'Licensed under the CC BY-NC-SA 4.0 license... Note that this license does not apply to any DuckDuckGo logos or marks that may be contained in this repo.' Status is healthy: archived=false, release 2026.11.10, 1,749 stars (recorded in leads.md L7).

## 7. Assessment

Use it as reference while reporting, and do not build it into a product or publish a derived dataset if your outlet is commercially operated — the NonCommercial and ShareAlike terms both bite, and 'we are journalism' does not satisfy NonCommercial. Practically: look up the ownership, verify it against corporate registries, and cite the registry in print. That keeps the finding defensible and sidesteps the licence entirely.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release 2026.11.10 (2026-11-10), 1,749 stars, SPDX NOASSERTION (actual: CC-BY-NC-SA-4.0 per the licence blob). Dated release cadence indicating regular regeneration.

## 9. Licensing

**Licence:** CC-BY-NC-SA-4.0 (licence blob read 2026-11-17; GitHub reports NOASSERTION) — a DATASET licence, not a software licence _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** Same. The producing crawler (duckduckgo/tracker-radar-collector) is separately licensed and was not assessed here.

**Restrictions:** NonCommercial: no commercial use without permission, which includes a commercially operated newsroom embedding it in a product. ShareAlike: derivative datasets must carry CC-BY-NC-SA-4.0, which can contaminate a combined dataset you intend to publish. DuckDuckGo logos and marks are excluded from the licence.

**Licence evidence:** https://github.com/duckduckgo/tracker-radar/blob/main/LICENSE

## 10. Costs

No fee for permitted non-commercial use. Commercial use requires permission — no published price. Negligible infrastructure (it is a git repository of JSON).

## 11. Privacy and data flows

Static public data; consulting it discloses nothing.

## 12. Verdict

**Reference only**

## Material blockers

_Tracked separately from the score._

- CC-BY-NC-SA-4.0 — NonCommercial bars commercial productisation; ShareAlike propagates to derived datasets

## 13. Alternatives

- Corporate registry research to establish tracker ownership in a citable, licence-free way
- Whotracks.me as an alternative tracker dataset with its own terms
- EasyList/EasyPrivacy for blocklist-based identification without ownership data

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/duckduckgo/tracker-radar/blob/main/LICENSE
- `../sources/evidence/leads.md`

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
| 9 | [Blacklight collector](SUR-B2-02.md) | 81 | Adopt |

---

← 128. [Crawlee](OSINT-C1-17.md) · 130. [edgartools](OSINT-C3-17.md) →
