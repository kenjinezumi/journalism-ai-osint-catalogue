# security-misc (Kicksecure)

`SUR-B3-21` · **69/100** · overall rank 275 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 68) |
| **Segment** | B3 · Protecting journalists and sources (rank 32) |
| **Subcategory** | System hardening |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Kicksecure / Whonix developers |
| **Maintenance** | Actively maintained |
| **Licence** | Not detected by the GitHub API — read the repository licence file before redistribution (the Kicksecure/Whonix ecosystem is predominantly GPL-family) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/Kicksecure/security-misc) · [Documentation](https://www.kicksecure.com/wiki/Security-misc) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 69/100**

---

## 1. Purpose

Package of Linux security-hardening settings — kernel parameters, module blacklists, access restrictions, boot and memory protections — applied as a coherent set rather than individually.

## Journalism / investigative use case

Hardening the Linux machines a newsroom actually runs — the document-processing workstation, the evidence machine, the server holding an archive — using settings maintained by a security-focused distribution rather than assembling kernel flags from blog posts.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Provides a curated, maintained hardening baseline, which is substantially better than the ad-hoc hardening most organisations attempt and then never revisit
- Developed for Kicksecure and Whonix, so the settings come from a project whose purpose is a hardened system rather than from general-purpose advice
- Modular enough to apply selectively, and documented so you can understand what each setting costs in functionality
- Active maintenance (pushed 2026-09-30, tag 54.2-1) with a focused community (600 stars)

## 5. Cons

- Hardening breaks things: module blacklists and restrictive kernel parameters can disable hardware or software you need, and diagnosing the cause afterwards is unpleasant — test before deploying to a working machine
- No release objects (tag-based versioning only) and GitHub reports no SPDX licence, so the licence must be read from the repository for compliance records
- Debian-family oriented, so applying it to other distributions requires adaptation
- Hardening is not a substitute for architecture: a hardened machine that still opens untrusted documents directly is less safe than an unhardened one using Dangerzone or disposable VMs

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 600 stars with 36 open issues, no releases, latest tag 54.2-1, last push 2026-09-30, no SPDX detected. Its use as a component of Kicksecure and Whonix is documented by those projects, which is the relevant production context.

## 7. Assessment

Worth applying to your infrastructure machines, with testing — and worth understanding as the second line of defence rather than the first. For your profile the priority order matters: compartmentalisation and document sanitisation (Qubes, Tails, Dangerzone) prevent whole classes of attack, while hardening reduces the damage of what gets through. Apply it to the archive server and the evidence workstation, test thoroughly, and document which settings you disabled and why.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-09-30, no release objects, latest tag 54.2-1, no SPDX detected, 600 stars, 36 open issues. Regular tag-based versioning with current commits as a component of an actively maintained distribution.

## 9. Licensing

**Licence:** Not detected by the GitHub API — read the repository licence file before redistribution (the Kicksecure/Whonix ecosystem is predominantly GPL-family) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Unverified in this survey; confirm from the repository before including it in a distributed image.

**Licence evidence:** https://github.com/Kicksecure/security-misc

## 10. Costs

No fee. Cost is testing and troubleshooting time, which is non-trivial on diverse hardware.

## 11. Privacy and data flows

Local system configuration; no data flows. Note that some settings reduce telemetry and network exposure, which is a privacy improvement in itself.

## 12. Verdict

**Integrate**

## 13. Alternatives

- Distribution-provided hardening guides (Debian, Ubuntu security guides) for a more conservative baseline
- [Qubes OS](SUR-B3-20.md), which addresses the same risk architecturally rather than by configuration
- CIS benchmarks for a formal, auditable hardening standard

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/Kicksecure/security-misc
- https://www.kicksecure.com/wiki/Security-misc

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

← 274. [ethereum-etl](OSINT-C3-20.md) · 276. [SiteOne Crawler](OSINT-C1-19.md) →
