# py-wacz

`OSINT-C1-43` · **73/100** · overall rank 245 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 83) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 26) |
| **Subcategory** | WACZ packaging |
| **Type** | library |
| **Bucket** | `verified-oss` |
| **Maintainer** | Webrecorder |
| **Maintenance** | Actively maintained |
| **Licence** | MIT |
| **Licence type** | Permissive |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/webrecorder/py-wacz) · [Documentation](https://github.com/webrecorder/py-wacz#readme) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 3/5 · licence+cost 5/5 → **weighted 73/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Permissive |
| **Exact licence (as recorded)** | MIT |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a |
| **Restrictions** | None. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Local file packaging; negligible resources.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/webrecorder/py-wacz/blob/main/LICENSE
- https://github.com/webrecorder/py-wacz

---

## 1. Purpose

Python library and CLI that packages WARC files into the WACZ (Web Archive Collection Zipped) format, generating the required indexes, pages list and optional datapackage metadata.

## Journalism / investigative use case

Package captures into a single self-contained WACZ for archiving, sharing with lawyers, or embedding in a published story — the step that converts loose WARC files into something a colleague can open in ReplayWeb.page with no instructions.

## 2. Audience

engineer

## 3. Project type

library · bucket `verified-oss`

## 4. Pros

- Produces the one archive format that a non-technical recipient can actually open (via ReplayWeb.page), which is the practical difference between holding evidence and being able to show it
- Includes index and page-list generation, so the resulting WACZ is browsable rather than just a zip of WARCs
- MIT licensed with current releases (v0.6.0, 2026-09-10) under Webrecorder maintenance
- Small and scriptable, so it drops into a capture pipeline as a final packaging step

## 5. Cons

- Niche utility with a small user base (63 stars) and a relatively high open-issue count for its size (21), reflecting spec-tracking churn
- Spec-tracking rather than feature-rich: it follows the WACZ specification, so its capabilities are bounded by that spec's evolution
- Does nothing on its own — requires WARC inputs from a separate capture tool
- If you use browsertrix-crawler, WACZ output is already produced, making this redundant for the common path

## 6. Feedback (documented)

No individual user reports verified. Documented: 63 stars with 21 open issues, release v0.6.0 (2026-09-10), last push 2026-10-13, MIT. The WACZ specification itself is a Webrecorder-led effort, so this is the reference implementation.

## 7. Assessment

Needed only if you produce WARCs by some route other than browsertrix-crawler — for example warcprox-proxied scraping, Heritrix crawls, or wget --warc captures — and want them in a shareable form. That is a real case: a Heritrix collection packaged as WACZ becomes something counsel can review. Otherwise it is already covered by your capture tool, and I would not seek it out.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-10-13, latest release v0.6.0 (2026-09-10), 63 stars, 21 open issues. Current releases as the reference implementation of a specification the maintainer leads.

## 9. Licensing

**Licence:** MIT _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** None.

**Licence evidence:** https://github.com/webrecorder/py-wacz/blob/main/LICENSE

## 10. Costs

No fee. Local file packaging; negligible resources.

## 11. Privacy and data flows

Local file packaging only, no network calls. Note that packaging does not sanitise content — credentials captured in a WARC remain in the WACZ.

## 12. Verdict

**Integrate**

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md), which emits WACZ directly
- [warcio](OSINT-C1-41.md) for record-level WARC work without packaging
- Distributing raw WARCs plus pywb if the recipient has infrastructure

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/webrecorder/py-wacz
- https://github.com/webrecorder/py-wacz/blob/main/LICENSE

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

← 244. [Oxigraph](JAI-A3-17.md) · 246. [olmOCR](JAI-A2-34.md) →
