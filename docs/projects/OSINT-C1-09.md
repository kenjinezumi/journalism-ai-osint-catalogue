# Metabigor

`OSINT-C1-09` · **70/100** · overall rank 267 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 96) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 29) |
| **Subcategory** | Infrastructure footprinting |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | j3ssie |
| **Maintenance** | Stable with low activity |
| **Licence** | MIT |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/j3ssie/metabigor) · [Documentation](https://github.com/j3ssie/metabigor#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 3/5 · usability 3/5 · licence+cost 5/5 → **weighted 70/100**

---

## 1. Purpose

Go tool that gathers organisational internet footprint data — IP netblocks, ASNs, related hosts, certificate and scan data — from public sources without requiring API keys for its core functions.

## Journalism / investigative use case

Quickly map an organisation's internet footprint (netblocks, ASNs, related hosts) from public sources before deeper investigation — for example establishing which IP ranges a surveillance vendor controls before looking at what runs on them.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Works without paid API keys for core functions, which distinguishes it from uncover and makes it usable without a budget or vendor account
- ASN and netblock mapping is the right first step in infrastructure investigation and is tedious to do by hand
- MIT licensed, single Go binary, actively released (v2.2.0, 2026-08-08) with a near-empty issue tracker (2 open)

## 5. Cons

- Infrastructure-oriented rather than social-media oriented, so it answers only one class of question
- Output needs manual validation: public ASN and netblock attribution is frequently stale or wrong, and publishing an incorrect 'company X controls this range' claim is a real risk
- Queries are sent from your host to third-party public services, so those services see your targets
- Last push 2026-08-08 — three months before this survey, with no activity since the release

## 6. Feedback (documented)

No individual user reports verified. Documented: 1,871 stars with only 2 open issues, release v2.2.0 on 2026-08-08 (same-day push). The very low issue count suggests either good triage or light use; with 1,871 stars the former is more likely.

## 7. Assessment

A good first instrument for the surveillance-infrastructure investigations in the B2 part of your work: cheap, no vendor account, and it narrows the search space fast. The discipline required is verification — confirm netblock ownership against RIR records (RIPE, ARIN) before any published claim, because public attribution data lags reality by months. Pair with uncover or direct certificate-transparency queries for what is actually running.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-08-08, latest release v2.2.0 published the same day, 1,871 stars, 2 open issues. Three months since last activity; a small, feature-complete Go tool with a clean tracker. Not classified actively maintained because there is no activity in the last quarter.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a — queries third-party public services whose own terms apply.

**Restrictions:** None material for the code. The third-party services it queries have their own terms on automated access.

**Licence evidence:** https://github.com/j3ssie/metabigor/blob/master/LICENSE

## 10. Costs

No fee and no required API keys for core functions — unusual and valuable in this category. Negligible compute.

## 11. Privacy and data flows

Queries are sent from your host to third-party public services, which therefore learn which organisations you are mapping. Use a dedicated egress or Tor where the target should not learn of your interest.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [uncover](OSINT-C1-10.md) for scan-database queries (paid API keys, broader data)
- amass or subfinder for subdomain-focused enumeration
- Direct RIR (RIPE/ARIN) and certificate-transparency queries for authoritative ownership data

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/j3ssie/metabigor
- https://github.com/j3ssie/metabigor/blob/master/LICENSE

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

← 266. [bellingcat/EDGAR](OSINT-C3-16.md) · 268. [Pelias](OSINT-C2-30.md) →
