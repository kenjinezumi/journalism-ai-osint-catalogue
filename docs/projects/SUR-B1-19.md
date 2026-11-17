# Klaxon Cloud (DocumentCloud Add-On)

`SUR-B1-19` · **72/100** · overall rank 249 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 64) |
| **Segment** | B1 · Monitoring public information, narratives, disinformation, censorship and harassment (rank 21) |
| **Subcategory** | Web change monitoring |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | MuckRock |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-3-Clause (add-on script); the front-end monorepo carries NO licence file, so its reuse rights are unverified |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/MuckRock/Klaxon) · [Documentation](https://www.documentcloud.org/help/add-ons/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 2/5 · usability 5/5 · licence+cost 4/5 → **weighted 72/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Hosted reimplementation of Klaxon as a DocumentCloud Add-On, with a browser extension for selecting page regions, scheduled checking via GitHub Actions and Cloudflare Workers, and an Internet Archive snapshot attached to each detected change.

## Journalism / investigative use case

Lets a reporter with only a DocumentCloud account monitor web pages for newsworthy edits without running a server, with an Internet Archive snapshot attached as evidence of the before-and-after — which is the one thing self-hosted watchers typically omit.

## 2. Audience

journalist

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Zero infrastructure for the newsroom: a reporter with a DocumentCloud account can start monitoring the same day, which is decisive for teams with no engineering capacity
- Automatic Internet Archive snapshot per detected change gives you third-party-attested evidence of the before state — a genuine evidentiary advantage over local-diff-only tools
- Revives a capability that the self-hosted Klaxon no longer reliably provides, under active MuckRock stewardship (pushed 2026-09-10)
- The add-on script itself is BSD-3-Clause, so the automation logic is inspectable

## 5. Cons

- The front-end monorepo carries no licence file, so reuse rights for the extension and site code are not verified — only the add-on script's BSD-3-Clause is confirmed
- Hosted model means watch configuration, run history and detected changes live in MuckRock's DocumentCloud infrastructure rather than the newsroom's, with less control over retention — unsuitable for monitoring that should stay confidential
- Dependency chain is long and third-party-heavy (DocumentCloud, GitHub Actions, Cloudflare Workers, Internet Archive), so availability depends on several services you do not control
- Tiny repository footprint (9 stars, 1 open issue) and no releases, so it is hard to assess independently of MuckRock's operation of it

## 6. Feedback (documented)

No individual user reports verified. Documented: the add-on script is BSD-3-Clause while the front-end monorepo has no licence file (verified session 1, retained); 9 stars; last push 2026-09-10. MuckRock operates it as part of the DocumentCloud Add-On ecosystem.

## 7. Assessment

The right recommendation for a small newsroom with no server capacity, with one important caveat: what you are monitoring becomes visible to MuckRock's infrastructure, so do not use it to watch pages whose monitoring would itself be sensitive (a target's site, a procurement portal in an active investigation). For public-interest watching of government pages it is excellent, and the automatic Internet Archive snapshot is a feature I would want even in a self-hosted setup.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-10, no releases, 9 stars, 1 open issue. Maintained as part of MuckRock's operated add-on ecosystem; repository metadata is thin because the service rather than the code is the artefact.

## 9. Licensing

**Licence:** BSD-3-Clause (add-on script); the front-end monorepo carries NO licence file, so its reuse rights are unverified _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Add-on script is permissive. The extension and site code have no stated licence, so do not fork or redistribute those components without clarification.

**Licence evidence:** https://github.com/MuckRock/Klaxon

## 10. Costs

No direct fee; requires a DocumentCloud account (verified-journalist access has historically been free, with paid organisational tiers — current prices not verified in this survey). No infrastructure cost to you.

## 11. Privacy and data flows

Watch configuration, run history and detected changes live in MuckRock's DocumentCloud infrastructure rather than the newsroom's. Internet Archive snapshots are public by design. Appropriate for monitoring public-interest pages; inappropriate where the fact of monitoring is sensitive.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Hosted: monitoring activity and detected changes are visible to MuckRock infrastructure

## 13. Alternatives

- [changedetection.io](SUR-B1-15.md) self-hosted, where monitoring must stay internal
- Klaxon self-hosted for the same UX under your own control — but with maintenance caveats
- [webchanges](SUR-B1-17.md) plus Scoop for CLI monitoring with your own evidence capture

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/MuckRock/Klaxon
- https://www.documentcloud.org/help/add-ons/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [changedetection.io](SUR-B1-15.md) | 93 | Adopt |
| 2 | [OONI Explorer](SUR-B1-03.md) | 90 | Adopt |
| 3 | [IODA (Internet Outage Detection and Analysis)](SUR-B1-07.md) | 88 | Adopt |
| 4 | [OONI Probe CLI / probe-engine](SUR-B1-01.md) | 85 | Adopt |
| 5 | [OONI Probe Multiplatform](SUR-B1-02.md) | 85 | Adopt |
| 6 | [shot-scraper](SUR-B1-23.md) | 83 | Adopt |
| 7 | [webchanges](SUR-B1-17.md) | 82 | Adopt |
| 8 | [EDGI web-monitoring-diff](SUR-B1-21.md) | 81 | Integrate |

---

← 248. [Klaxon (self-hosted)](SUR-B1-18.md) · 250. [PyExifTool](OSINT-C2-02.md) →
