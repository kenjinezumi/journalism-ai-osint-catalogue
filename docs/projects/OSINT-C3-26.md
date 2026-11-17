# SSLyze

`OSINT-C3-26` · **64/100** · overall rank 297 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 114) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 35) |
| **Subcategory** | TLS analysis |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | Alban Diquet (nabla-c0d3) |
| **Maintenance** | Stable with low activity |
| **Licence** | AGPL-3.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/nabla-c0d3/sslyze) · [Documentation](https://nabla-c0d3.github.io/sslyze/documentation/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 3/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 64/100**

---

## 1. Purpose

TLS and SSL configuration scanner that reports supported protocols, cipher suites, certificate chains, and known weaknesses, with a Python API and JSON output.

## Journalism / investigative use case

Two uses: documenting that an organisation handling sensitive citizen data runs demonstrably weak TLS — a concrete, checkable security-negligence finding — and examining certificate chains on suspected infrastructure to find shared issuance patterns that link hosts.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Produces specific, verifiable technical findings: 'this government portal accepts a deprecated protocol' is a factual claim a reader can re-test, which is unusually solid ground for a technology story
- Certificate-chain detail supports infrastructure attribution: shared intermediate certificates or unusual issuance patterns link hosts that otherwise look unrelated
- Python API and JSON output make it scriptable across a list of targets, so a survey of a sector's TLS posture is feasible
- Well-established with a long maintenance history and a focused scope

## 5. Cons

- Active scanning: each check connects to the target, so the target can see it — and scanning a government portal's TLS, while unremarkable, is still a visible act
- Interpreting results requires TLS literacy: a 'weak' cipher may be present but unused, and publishing a misread finding would be embarrassing and correctable by the target
- Narrow scope by design — it tells you about TLS configuration and nothing else
- Findings age quickly as configurations change, so a published claim needs a date and ideally a saved JSON record

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived with a long release history. SSLyze is a standard TLS assessment tool, well established in the security community.

## 7. Assessment

Integrate it for the specific story type where it produces hard findings — the security posture of organisations holding sensitive data — and for certificate-based infrastructure linking. For your profile the publication discipline is to save the raw JSON with a timestamp, have someone TLS-literate review the interpretation, and give the organisation an opportunity to respond, since configurations can be fixed between your scan and publication and you want the record of what you found.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with a long release history and steady maintenance. Classified stable-low: a mature, focused tool where the pace reflects completeness.

## 9. Licensing

**Licence:** AGPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** Copyleft would apply to a modified network service built on it; immaterial for command-line use. Note that AGPL on a scanning tool is unusual and worth confirming if you embed it.

**Licence evidence:** https://github.com/nabla-c0d3/sslyze

## 10. Costs

No fee. Negligible compute.

## 11. Privacy and data flows

Active connections to the target, which are visible in its logs. Unremarkable for TLS assessment but still a disclosure of interest.

## 12. Verdict

**Integrate**

## 13. Alternatives

- testssl.sh as a shell-based alternative with similar coverage
- Qualys SSL Labs for a hosted assessment, which discloses the target to a third party and produces a citable public report
- Certificate transparency data for issuance patterns without connecting to the host

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/nabla-c0d3/sslyze
- https://nabla-c0d3.github.io/sslyze/documentation/

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [OpenSanctions (dataset)](OSINT-C3-01.md) | 94 | Adopt |
| 2 | [Uwazi](OSINT-C3-05.md) | 94 | Adopt |
| 3 | [Tella](OSINT-C3-06.md) | 89 | Adopt |
| 4 | [NetworkX](OSINT-C3-31.md) | 88 | Adopt |
| 5 | [Quarto](OSINT-C3-39.md) | 85 | Adopt |
| 6 | [CourtListener](OSINT-C3-11.md) | 84 | Adopt |
| 7 | [Querido Diário](OSINT-C3-14.md) | 83 | Integrate |
| 8 | [subfinder](OSINT-C3-23.md) | 83 | Adopt |

---

← 296. [Photon](OSINT-C1-20.md) · 298. [WhatWeb](SUR-B2-08.md) →
