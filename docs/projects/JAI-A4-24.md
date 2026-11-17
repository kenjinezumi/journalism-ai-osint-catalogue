# kuroi

`JAI-A4-24` · **71/100** · overall rank 259 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 104) |
| **Segment** | A4 · Fact-checking support and media verification (rank 5) |
| **Subcategory** | Pre-publication redaction |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | International Consortium of Investigative Journalists |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/ICIJ/kuroi) · [Documentation](https://github.com/ICIJ/kuroi#readme) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 4/5 · privacy 3/5 · usability 3/5 · licence+cost 4/5 → **weighted 71/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

CLI tool that uses an LLM backend to identify personal and source-identifying information in documents at scale, so it can be redacted before publication.

## Journalism / investigative use case

The publishing-side counterpart to x-ray: before an investigative team releases primary-source documents, use it to find source-identifying and personal data across thousands of pages rather than redacting page by page — the step that makes large document releases feasible without burning sources.

## 2. Audience

engineer

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Addresses a real bottleneck: manual redaction is why many newsrooms publish three documents instead of three hundred, and automating the detection stage changes what is publishable
- Built by ICIJ for its own large-scale document releases, which is the most relevant provenance possible for this task
- Recent and released (v0.1.3, 2026-10-13) under AGPL-3.0
- Backend-agnostic in principle, so it can be pointed at a self-hosted model

## 5. Cons

- LLM-based detection of sensitive data is probabilistic, NOT conclusive — it will miss identifiers and flag non-sensitive text, so output must be human-reviewed before any release, and treating it as complete would be dangerous
- CRITICAL privacy issue: if configured against a hosted LLM, the sensitive document content being redacted is sent to that provider — the exact material you are trying to protect
- Very low adoption (6 stars, 0 open issues) and version 0.1.x — early software for a high-stakes task
- AGPL-3.0 affects redistribution of modified network services built around it

## 6. Feedback (documented)

No individual user reports verified — 6 stars means there is no community signal, which I state rather than embellish. The ICIJ provenance is the substantive evidence; the hosted-LLM exposure risk is inherent to the architecture and is flagged in this catalogue rather than reported by users.

## 7. Assessment

Conceptually the right tool for a real problem, and I would pilot it — but only against a self-hosted model, never a hosted API. The irony is sharp: a tool for protecting sources that, misconfigured, transmits unredacted source documents to a third party. For your profile the deployment shape is: local LLM (via vLLM or llama.cpp), kuroi for candidate detection, human review of every candidate, PyMuPDF for the actual redaction, then x-ray as a verification sweep before release. That chain is genuinely useful; any link using a hosted model is not.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-13, latest release v0.1.3 published the same day, 6 stars, 0 open issues. Recent release from an institutional maintainer; early-stage but current. Low adoption means little external testing.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a — depends on whichever LLM the operator configures; that model's licence and the provider's terms apply.

**Restrictions:** AGPL-3.0: modified network-service redistribution triggers source-release obligations. Internal use unaffected.

**Licence evidence:** https://github.com/ICIJ/kuroi/blob/main/LICENSE

## 10. Costs

Software free. Cost depends entirely on the LLM backend: a self-hosted model means GPU infrastructure; a hosted model means per-token charges (not priced here) plus an unacceptable disclosure. Human review time remains the dominant cost and is not reduced to zero.

## 11. Privacy and data flows

Depends on configuration and the difference is total. Self-hosted LLM: fully local and appropriate. Hosted LLM: the unredacted sensitive content is transmitted to that provider, which defeats the purpose. This must be a locked configuration, not a per-user choice.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- Hosted-LLM configuration would transmit unredacted sensitive documents to a third party — must be pinned to a self-hosted model

## 13. Alternatives

- [Presidio](JAI-A2-40.md) for rule-and-NER-based PII detection without an LLM — more predictable, less capable on unusual identifiers
- [x-ray](JAI-A4-23.md) for the complementary check that redactions actually removed the text
- Manual redaction for small, high-stakes document sets

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/ICIJ/kuroi
- https://github.com/ICIJ/kuroi/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [x-ray](JAI-A4-23.md) | 91 | Adopt |
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 258. [suncalc-py](OSINT-C2-39.md) · 260. [overpass-turbo](OSINT-C2-24.md) →
