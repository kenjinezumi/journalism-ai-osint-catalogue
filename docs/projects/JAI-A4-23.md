# x-ray

`JAI-A4-23` · **91/100** · overall rank 37 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Journalism and AI](../journalism-ai.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Journalism and AI (rank 13) |
| **Segment** | A4 · Fact-checking support and media verification (rank 1) |
| **Subcategory** | Redaction failure detection |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Free Law Project |
| **Maintenance** | Actively maintained |
| **Licence** | BSD-2-Clause |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/freelawproject/x-ray) · [Documentation](https://github.com/freelawproject/x-ray#readme) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 5/5 → **weighted 91/100**

---

## 1. Purpose

Python library that inspects PDFs for bad redactions — text that remains in the content stream beneath a drawn black rectangle — and reports the recoverable text.

## Journalism / investigative use case

Triaging FOIA releases, court filings and leaked document sets for failed redactions that reveal names, figures or passages the releasing body intended to withhold. This is a recurring source of scoops, and also the routine check you run before relying on a document being genuinely redacted.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Automates a check that is otherwise accidental: failed redactions are found when someone happens to copy-paste, and x-ray turns that into a systematic sweep over thousands of documents
- Built by Free Law Project against a very large corpus of real court filings, so the heuristics are tuned on the documents that actually exhibit the failure
- BSD-2-Clause, pure Python, fully local — appropriate for sensitive leaked documents
- Dual value: offensive (find what others hid) and defensive (check your own publications before release)

## 5. Cons

- Detection is heuristic: outputs are candidate bad redactions, not conclusive findings, and both false positives and missed redactions occur
- Finds text-layer failures only — an image-based redaction that is merely a low-opacity overlay, or a scan of a poorly redacted page, is outside its scope
- GitHub release metadata lags the tag line (release v0.3.5 from 2025-12-08 versus tag v0.4.0), so pinning requires care
- 44 open issues against 837 stars with a small maintainer team

## 6. Feedback (documented)

No individual user reports verified in this survey. The institutional context is strong and checkable: Free Law Project operates CourtListener over millions of filings and built x-ray for that corpus, which is credible production provenance. Failed redactions in court and government documents are a well-documented recurring phenomenon.

## 7. Assessment

Adopt it twice over: as a sweep on every document set you receive, and as a mandatory pre-publication check on every document you release. The second use is the one newsrooms skip and the one that protects sources — publishing a 'redacted' PDF whose text layer is intact has burned sources before. Pair it with PyMuPDF for applying true redactions, and remember x-ray cannot see image-based failures, so visual spot-checks remain necessary.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v0.3.5 (2025-12-08), latest tag v0.4.0, 837 stars, 44 open issues. Current commits with a tag ahead of the published release; maintained by a functioning non-profit that uses it operationally.

## 9. Licensing

**Licence:** BSD-2-Clause _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/freelawproject/x-ray/blob/main/LICENSE

## 10. Costs

No fee, negligible compute. No paid dependencies.

## 11. Privacy and data flows

Local processing with no third-party service — essential, since the documents you run it over are by definition ones containing information someone tried to withhold.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [kuroi](JAI-A4-24.md) for the publishing-side problem of finding and removing sensitive data at scale (LLM-based, with its own caveats)
- [PyMuPDF](JAI-A2-42.md) to apply genuine redactions that remove underlying text
- Manual copy-paste spot checks, which x-ray systematises

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/freelawproject/x-ray
- https://github.com/freelawproject/x-ray/blob/main/LICENSE

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 2 | [InVID-WeVerify Verification Plugin](JAI-A4-04.md) | 82 | Adopt |
| 3 | [Meedan Check](JAI-A4-01.md) | 80 | Pilot |
| 4 | [CooRTweet](JAI-A4-13.md) | 77 | Adopt |
| 5 | [kuroi](JAI-A4-24.md) | 71 | Pilot |
| 6 | [Community Forensics](JAI-A4-21.md) | 65 | Pilot |
| 7 | [Alegre (Meedan)](JAI-A4-02.md) | 63 | Monitor |
| 8 | [CAT-Net](JAI-A4-19.md) | 63 | Pilot |
| 9 | [TruFor](JAI-A4-18.md) | 61 | Monitor |

---

← 36. [trafilatura](JAI-A1-01.md) · 38. [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) →
