# Conifer

`OSINT-C1-35` · **63/100** · overall rank 304 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 116) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 36) |
| **Subcategory** | Hosted capture platform |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Rhizome (transferred from webrecorder/conifer) |
| **Maintenance** | Maintenance appears to be declining |
| **Licence** | Apache-2.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Rhizome-Conifer/conifer) · [Documentation](https://conifer.rhizome.org/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 2/5 · privacy 3/5 · usability 4/5 · licence+cost 5/5 → **weighted 63/100**

---

## 1. Purpose

Web-archiving platform providing remote-browser capture sessions and organised, replayable collections, available as a hosted service or self-hosted Docker stack.

## Journalism / investigative use case

Capture a dynamic page or social feed through a remote browser session and keep it in an organised, replayable collection — the remote-browser aspect means the capture originates from Conifer's infrastructure rather than your own address, which can be useful when you do not want your newsroom IP visiting a target.

## 2. Audience

newsroom analyst, journalist

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Remote-browser capture provides a degree of separation between your network and the target, which is a genuine (if partial) operational-security benefit
- Collection organisation and replay in one place, usable by non-engineers without any infrastructure
- Apache-2.0 with a self-hostable Docker stack if you want the same model under your own control
- Substantial community (1,549 stars) and an institutional home at Rhizome, with the repository transfer from webrecorder confirmed by redirect

## 5. Cons

- Slower cadence than Webrecorder's newer tools: last push 2026-07-22 (four months before this survey) with no release objects at all, and 128 open issues
- Hosted quotas are small, so sustained use pushes you toward self-hosting or another tool
- Captures are held by the hosted instance unless you self-host, which is a third-party custody decision
- Superseded in practice by Browsertrix and ArchiveWeb.page for most use cases, so adopting it now means choosing the less-developed option

## 6. Feedback (documented)

No individual user reports verified. Documented: repository transfer webrecorder/conifer → Rhizome-Conifer/conifer confirmed by API redirect on 2026-11-17; 1,549 stars with 128 open issues; last push 2026-07-22; no release objects. The transfer plus slowing cadence is the significant pattern.

## 7. Assessment

Hard to recommend for new work when ArchiveWeb.page covers manual capture and Browsertrix covers team-scale, both under faster maintenance. The one feature that still distinguishes Conifer is remote-browser capture, which has a real use when you want capture traffic not to originate from your network — though a dedicated VPS running browsertrix-crawler achieves the same with more control. Treat as a monitoring item, and note the transfer when updating any old links.

## 8. Maintenance

**Maintenance appears to be declining** — GitHub API 2026-11-17: archived=false (repository transferred to Rhizome-Conifer), pushed_at 2026-07-22, no release objects, 1,549 stars, 128 open issues. Four months without commits, no release engineering, and functional overlap with faster-moving tools from the original maintainer. Declining rather than dormant.

## 9. Licensing

**Licence:** Apache-2.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None material.

**Licence evidence:** https://github.com/Rhizome-Conifer/conifer/blob/develop/LICENSE

## 10. Costs

Self-hosting: no fee, a Docker stack plus storage. Hosted conifer.rhizome.org has storage quotas; any paid tiers were not verified in this survey. Estimate for self-hosting: one moderate VM plus capture storage.

## 11. Privacy and data flows

Captures are held by the hosted instance unless you self-host. The remote-browser model means the target sees Conifer's address rather than yours — a partial benefit, since the hosted operator then sees what you captured.

## 12. Verdict

**Monitor**

## 13. Alternatives

- [ArchiveWeb.page](OSINT-C1-31.md) for manual capture under your own control
- [Browsertrix](OSINT-C1-30.md) for a maintained team platform
- [browsertrix-crawler](OSINT-C1-29.md) on a dedicated VPS to get network separation with full control

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/Rhizome-Conifer/conifer
- https://conifer.rhizome.org/
- `../sources/evidence/leads.md`

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

← 303. [CAT-Net](JAI-A4-19.md) · 305. [Hoover](OSINT-C3-03.md) →
