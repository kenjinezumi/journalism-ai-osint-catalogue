# Perma

`OSINT-C1-37` · **74/100** · overall rank 223 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 75) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 23) |
| **Subcategory** | Citation preservation |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Harvard Library Innovation Lab |
| **Maintenance** | Actively maintained |
| **Licence** | MIT AND GPL-3.0 (dual, per README; GitHub reports no SPDX and there is no LICENSE file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/harvard-lil/perma) · [Documentation](https://perma.cc/docs) |
| **Also known as** | Perma.cc |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 2/5 · usability 5/5 · licence+cost 3/5 → **weighted 74/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Link-preservation service and platform: captures a cited web page and issues a permanent 'perma link' that resolves to the archived copy, designed for legal and scholarly citation.

## Journalism / investigative use case

Preserve cited sources as stable links so a published investigation does not rot when the source page changes or disappears — the reader clicking a citation three years later sees what you saw, which is a basic integrity property most published journalism lacks.

## 2. Audience

journalist, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Solves link rot in published work, which is a real and under-addressed problem: a story whose sources have all 404'd is much harder to defend
- Institutional durability: Harvard LIL and a library consortium behind it, which is a better continuity bet than a startup or a volunteer project
- Perma links are recognised in legal and scholarly citation practice, so they carry conventional authority
- Open source (MIT AND GPL-3.0 dual, per README) and self-hostable in principle

## 5. Cons

- Self-hosting is heavy — a Django stack plus storage — and the hosted service is the realistic path for almost everyone
- On perma.cc, captures and target URLs are held by Harvard LIL and the links are public, so using it discloses what you cited and when; for a pre-publication investigation that is a leak
- Licence is declared in the README rather than a LICENSE file (GitHub reports no SPDX), so the dual MIT/GPL-3.0 position needs confirmation for compliance records
- Hosted access requires a perma.cc account with institutional tiers whose current prices were not verified in this survey; 95 open issues and no release objects (latest tag v-.59.1)

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 540 stars with 95 open issues, no release objects, SPDX none with licensing declared in the README, last push 2026-11-16. Perma.cc's adoption in legal citation is well established in that field, which is relevant institutional evidence.

## 7. Assessment

Use the hosted service at publication time, not during reporting — that distinction is the whole operational guidance. A perma link created while you are still investigating publicly records your interest in a URL; created at publication, it is exactly the right artefact. For your profile I would pair it with your own Scoop or ArchiveBox capture so you are not solely dependent on a third party for your evidence of record, and confirm the licence position in writing if you ever plan to self-host.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, no release objects, latest tag v-.59.1, SPDX none, 540 stars, 95 open issues. Current commits with an operating hosted service and institutional backing; release engineering is informal because the service, not the package, is the product.

## 9. Licensing

**Licence:** MIT AND GPL-3.0 (dual, per README; GitHub reports no SPDX and there is no LICENSE file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Archived content belongs to the original publishers.

**Restrictions:** Dual-licence position is declared only in the README, which is weak for compliance purposes — confirm with the maintainers before self-hosting or redistributing. The GPL-3.0 element would constrain a proprietary derivative.

**Licence evidence:** https://github.com/harvard-lil/perma

## 10. Costs

Hosted perma.cc uses institutional tiers (library and organisation subscriptions) whose current prices were NOT verified in this survey — check before budgeting. Self-hosting: no software fee but a Django stack plus storage, realistically a multi-VM deployment. Assumptions for self-hosting: moderate capture volume.

## 11. Privacy and data flows

On perma.cc, captures and target URLs are held by Harvard LIL and the resulting links are public — so creating a perma link publishes the fact that someone archived that URL at that time. Appropriate at publication, inappropriate during a confidential investigation.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Hosted captures and links are public — discloses what you archived and when

## 13. Alternatives

- [Scoop](OSINT-C1-36.md) (same lab) for provenance-attested local captures with no disclosure
- [ArchiveBox](OSINT-C1-28.md) for a self-hosted archive of everything you cite
- Internet Archive 'Save Page Now' as a free public alternative, with the same disclosure caveat

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/harvard-lil/perma
- https://perma.cc/docs

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

← 222. [MuckRock](OSINT-C3-15.md) · 224. [ICIJ Prophecies](OSINT-C3-08.md) →
