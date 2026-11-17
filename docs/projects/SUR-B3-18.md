# Autopsy

`SUR-B3-18` · **72/100** · overall rank 253 of 361 · verdict **Monitor**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 65) |
| **Segment** | B3 · Protecting journalists and sources (rank 31) |
| **Subcategory** | Digital forensics platform |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Basis Technology / Sleuth Kit project |
| **Maintenance** | Stable with low activity |
| **Licence** | Apache-2.0 per the project's own documentation; GitHub API reports no detected licence (confirm the LICENSE file for compliance records) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/sleuthkit/autopsy) · [Documentation](https://www.autopsy.com/) |

**Scores** — relevance 3/5 · capability 4/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 72/100**

---

## 1. Purpose

Graphical digital-forensics platform built on The Sleuth Kit, providing disk-image analysis, timeline reconstruction, keyword search, file carving, hash matching and extensible modules.

## Journalism / investigative use case

Examining computers rather than phones: analysing a disk image from a laptop that may have been tampered with during a border crossing, reconstructing a timeline of file access on a device handed over by a source, or carving deleted documents from a drive that forms part of a leak.

## 2. Audience

specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- The standard open forensic platform for disk analysis, with timeline reconstruction and file carving that have no real open alternative at this level of maturity
- Graphical interface and case-management model make it usable by an analyst without command-line forensics fluency, and reports are presentable to lawyers
- Extensible module system, so you can add keyword lists or hash sets specific to an investigation
- Long institutional history with a release in 2026 (autopsy-4.23.1, 2026-05-07) and a substantial community (3,455 stars)

## 5. Cons

- Slowing cadence and a large backlog: last push 2026-06-20 with 406 open issues, and no SPDX licence detected by the GitHub API (the project is Apache-2.0 per its own documentation, but this needed resolving rather than assuming)
- Java desktop application with a heavy footprint and a Windows-first orientation; Linux use is possible but less smooth
- Designed for law-enforcement workflows, so the framing assumes an adversarial investigation of a device owner rather than a protective examination for them — the ethics are yours to impose
- Disk forensics requires real expertise, and the gap between running Autopsy and producing a defensible finding is large

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,455 stars with 406 open issues, release autopsy-4.23.1 (2026-05-07), last push 2026-06-20, no SPDX detected. Autopsy's standing in digital forensics is well established; its journalism use is not separately evidenced here.

## 7. Assessment

Keep it available for computer rather than phone examinations, which is a less frequent but real need — particularly device-tampering questions after travel or detention. For your profile I would not build in-house disk-forensics capability unless the need recurs; the expertise threshold is high and a practitioner relationship is usually better value. Where you do use it, work from a verified image of the drive and never from the original, and document the hash chain.

## 8. Maintenance

**Stable with low activity** — GitHub API 2026-11-17: archived=false, pushed_at 2026-06-20, latest release autopsy-4.23.1 (2026-05-07), no SPDX detected, 3,455 stars, 406 open issues. Five months since last push with a 2026 release; a mature platform at reduced velocity with a substantial backlog.

## 9. Licensing

**Licence:** Apache-2.0 per the project's own documentation; GitHub API reports no detected licence (confirm the LICENSE file for compliance records) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Hash sets and keyword lists you import carry their own terms.

**Restrictions:** None material if Apache-2.0 as documented; verify the licence file before redistributing a bundled product.

**Licence evidence:** https://github.com/sleuthkit/autopsy

## 10. Costs

No fee. A workstation with substantial disk for images (a full disk image is the size of the drive) and RAM. Commercial support and training are available from the vendor at prices not verified here.

## 11. Privacy and data flows

Local analysis. Disk images contain everything on a device, so handling obligations are at the highest level: encrypted storage, access control, documented retention and disposal.

## 12. Verdict

**Monitor**

## 13. Alternatives

- The Sleuth Kit command-line tools for scripted analysis
- A professional forensic practitioner for high-stakes device-tampering questions
- [iLEAPP](SUR-B3-15.md)/ALEAPP where the device is a phone rather than a computer

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/sleuthkit/autopsy
- https://www.autopsy.com/

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

← 252. [Arelle](OSINT-C3-18.md) · 254. [brozzler](OSINT-C1-23.md) →
