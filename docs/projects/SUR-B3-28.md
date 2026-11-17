# Nextcloud

`SUR-B3-28` · **84/100** · overall rank 105 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 31) |
| **Segment** | B3 · Protecting journalists and sources (rank 19) |
| **Subcategory** | Self-hosted collaboration |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Nextcloud GmbH and community |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/nextcloud/server) · [Documentation](https://docs.nextcloud.com/) |

**Scores** — relevance 4/5 · capability 5/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 84/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Self-hosted file-sync, sharing and collaboration platform with an app ecosystem covering documents, calendars, chat, forms and workflow, plus server-side and optional end-to-end encryption.

## Journalism / investigative use case

The practical replacement for commercial cloud storage in a newsroom that must keep documents on its own infrastructure: file sync for reporters, controlled external sharing with partners, and an app ecosystem that covers the ordinary office needs that would otherwise push people back to Google Drive.

## 2. Audience

engineer, newsroom analyst, journalist

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Breadth is the reason it works socially: file sync, sharing, calendars and collaborative editing in one self-hosted platform means reporters have fewer reasons to use a commercial alternative
- Mature external-sharing controls (password-protected links, expiry, upload-only shares) make partner collaboration manageable without handing documents to a third party
- AGPL-3.0 with an enormous community (37,542 stars) and a very active release cadence (v33.0.11, 2026-11-12; pushed 2026-11-17), plus a commercial support option for newsrooms that need it
- Self-hosted means full control over location, retention and backups — which for an exile outlet can also mean choosing a jurisdiction deliberately

## 5. Cons

- Server-side encryption protects against disk theft, not against the server operator or a server compromise — so unlike CryptPad, Nextcloud's default model does not protect documents from whoever controls the host, and the optional end-to-end encryption app has historically been limited in scope and maturity
- 3,948 open issues, the largest in the catalogue, reflecting a very large application surface — operating it well means staying on top of updates, and a neglected Nextcloud is a serious liability holding your documents
- Operational burden is real: PHP application, database, background jobs, storage and regular upgrades, with a history of upgrade friction between major versions
- Release-object and tag divergence (v33.0.11 release against a v35.0.3 tag) means version tracking needs care

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 37,542 stars with 3,948 open issues, release v33.0.11 (2026-11-12), tag v35.0.3, pushed 2026-11-17, AGPL-3.0. The scale of adoption is clear from the metrics; the limitations of server-side encryption are documented by the project itself.

## 7. Assessment

Adopt it as the newsroom's general document infrastructure, and be precise about what it protects against: Nextcloud keeps your documents out of a commercial cloud and under your jurisdiction, which is valuable, but it does not make them unreadable to whoever holds the server. Put genuinely sensitive material in CryptPad or encrypted containers, and use Nextcloud for the everyday. Budget permanent administrator attention — the open-issue count is a fair warning about surface area.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v33.0.11 (2026-11-12), tag v35.0.3, 37,542 stars, 3,948 open issues. Very frequent releases with commercial backing; the enormous backlog reflects application breadth and a large user base.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Some enterprise-oriented apps and integrations have separate commercial terms.

**Restrictions:** AGPL-3.0: a modified instance offered to users obliges source publication. Nextcloud GmbH also sells enterprise subscriptions with support and some additional components — a commercial relationship, not a licence restriction on the server.

**Licence evidence:** https://github.com/nextcloud/server/blob/master/COPYING

## 10. Costs

No software fee for the community server. Infrastructure estimate: one VM with a database for a small newsroom, scaling with storage — the cost is storage plus permanent administrator time, which is the dominant item. Nextcloud GmbH enterprise subscriptions are priced per user (not verified in this survey). Assumptions: self-hosted, small team, moderate storage.

## 11. Privacy and data flows

Self-hosting gives you control of location, retention and access. The important limitation: server-side encryption does not protect against the operator or a compromised server, so Nextcloud is a jurisdiction-and-control improvement over commercial cloud rather than a confidentiality guarantee. Treat the server as able to read everything on it.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Server-side encryption does not protect documents from the server operator or a host compromise

## 13. Alternatives

- [CryptPad](SUR-B3-27.md) for documents that must be unreadable to the server
- Syncthing for peer-to-peer file sync with no server at all
- Commercial cloud storage — the thing this replaces; avoid for source material

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/nextcloud/server
- https://docs.nextcloud.com/
- https://github.com/nextcloud/server/blob/master/COPYING

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |

---

← 104. [CourtListener](OSINT-C3-11.md) · 106. [ALEAPP](SUR-B3-16.md) →
