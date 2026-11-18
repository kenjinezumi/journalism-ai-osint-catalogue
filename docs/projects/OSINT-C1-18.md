# HTTrack

`OSINT-C1-18` · **75/100** · overall rank 218 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 73) |
| **Segment** | C1 · Web and social research, archives and evidence capture (rank 22) |
| **Subcategory** | Site mirroring |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Xavier Roche (xroche) |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/xroche/httrack) · [Documentation](https://www.httrack.com/) |

**Scores** — relevance 3/5 · capability 3/5 · maintenance 4/5 · privacy 5/5 · usability 5/5 · licence+cost 4/5 → **weighted 75/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 |
| **SPDX identifier verified** | yes — read from the licence file |
| **Model / dataset terms** | n/a. Mirrored content belongs to the original publisher. |
| **Restrictions** | GPL-3.0 on the software. Mirroring engages the target's terms of service and copyright in the mirrored material — relevant if you redistribute the mirror rather than using it internally. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | No material additional cost recorded |
| **Cost conditions** | No material additional cost recorded |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** No fee. Disk proportional to site size. Negligible.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/xroche/httrack/blob/master/LICENSE
- https://github.com/xroche/httrack
- https://www.httrack.com/

---

## 1. Purpose

Website copier that recursively downloads a site to a local directory tree, rewriting links so the copy is browsable offline.

## Journalism / investigative use case

Take a quick offline mirror of a site likely to be edited or taken down, for later reading and keyword search — the low-ceremony option when a page is about to disappear and you need a copy now, on a machine with no Python or Docker.

## 2. Audience

journalist, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Extremely easy to run with a GUI and a CLI, available packaged in most distributions, and still releasing (3.51.0, 2026-10-28) after decades
- No dependencies of consequence, so it works on a borrowed or locked-down machine where installing a toolchain is not possible
- Produces a browsable, grep-able file tree, which is immediately useful for reading and keyword search without replay infrastructure
- Astonishingly clean issue tracker (5 open against 4,844 stars) for a project of this age

## 5. Cons

- Produces a loose file tree, not WARC, so it is weak as evidence of record: no HTTP headers, no request/response fidelity, no capture provenance — a mirror can be edited afterwards and nothing in it proves otherwise
- Poor with dynamic and JavaScript-dependent sites, which describes most modern government portals — you will get shells
- Link rewriting alters the content, which is itself a problem for evidentiary use
- Aggressive defaults can hammer a target; rate limiting must be set deliberately

## 6. Feedback (documented)

No individual user reports verified. Documented: 4,844 stars with 5 open issues and a release on 2026-10-28, pushed 2026-11-17 — an exceptionally well-kept long-lived project. Its weakness relative to WARC-based capture is a general property of mirroring, widely discussed in web-archiving practice.

## 7. Assessment

Keep it for the convenience case and do not use it as your evidence path. For your profile the rule is simple: HTTrack for reading and searching a site offline, WARC-based capture (browsertrix-crawler, Scoop, wget --warc) for anything that may be cited or disputed. Its enduring value is deployability — when a reporter abroad needs a copy of a site in the next ten minutes on an unfamiliar laptop, this is what will work.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release 3.51.0 (2026-10-28), 4,844 stars, 5 open issues. Current releases and near-zero backlog after many years; a mature tool under continuing care.

## 9. Licensing

**Licence:** GPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a. Mirrored content belongs to the original publisher.

**Restrictions:** GPL-3.0 on the software. Mirroring engages the target's terms of service and copyright in the mirrored material — relevant if you redistribute the mirror rather than using it internally.

**Licence evidence:** https://github.com/xroche/httrack/blob/master/LICENSE

## 10. Costs

No fee. Disk proportional to site size. Negligible.

## 11. Privacy and data flows

Direct downloads from the target to local disk, so the target sees your IP and a heavy request pattern. Nothing is uploaded anywhere.

## 12. Verdict

**Integrate**

## Material blockers

_Tracked separately from the score._

- Not WARC: weak provenance, unsuitable as evidence of record

## 13. Alternatives

- [browsertrix-crawler](OSINT-C1-29.md) or wget --warc for evidentiary WARC capture
- [monolith](OSINT-C1-39.md) or SingleFile for single-page portable snapshots
- [grab-site](OSINT-C1-24.md) for steerable rapid-response archiving — but note its maintenance status

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/xroche/httrack
- https://www.httrack.com/
- https://github.com/xroche/httrack/blob/master/LICENSE

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

← 217. [titiler](JAI-A1-27.md) · 219. [Turf.js](JAI-A1-26.md) →
