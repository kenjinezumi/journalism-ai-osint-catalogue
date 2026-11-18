# OnionShare

`SUR-B3-04` · **92/100** · overall rank 26 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 8) |
| **Segment** | B3 · Protecting journalists and sources (rank 6) |
| **Subcategory** | Secure file transfer |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Micah Lee and contributors |
| **Maintenance** | Actively maintained |
| **Licence** | GPL-3.0 (project's own LICENSE.txt read directly 2026-11-17; GitHub reports NOASSERTION because a note about bundled third-party licences is prepended to the GPL text) |
| **Licence type** | Strong copyleft |
| **Open-source status** | Open source |
| **Software price** | **No software fee** |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/onionshare/onionshare) · [Documentation](https://docs.onionshare.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 92/100**

---

## Licence and costs

_Licensing and payment are two separate questions. The classifications are defined in the [directory legend](../../README.md#how-to-read-the-licence-and-cost-columns)._

| | |
|---|---|
| **Licence classification** | Strong copyleft |
| **Exact licence (as recorded)** | GPL-3.0 (project's own LICENSE.txt read directly 2026-11-17; GitHub reports NOASSERTION because a note about bundled third-party licences is prepended to the GPL text) |
| **SPDX identifier verified** | no — resolved from the licence file or project documentation, not confirmed as an SPDX identifier |
| **Model / dataset terms** | n/a. Third-party components under licenses/ have their own terms and must not be read as the project licence — this was the cause of session 1's misidentification. |
| **Restrictions** | GPL-3.0 on the project's own code; immaterial for ordinary use. |
| **Open-source status** | **Open source** — Open-source software licence |
| **Software price** | **No software fee** |
| **Additional costs** | Self-hosted infrastructure |
| **Cost conditions** | Self-hosting infrastructure |
| **Verified** | 2026-11-17 · confidence **high** |

**Recorded cost detail.** Free. No infrastructure — the point is that there is no server. Bandwidth only.

**Evidence for the licence and cost position** (verified 2026-11-17):

- Licence evidence: https://github.com/onionshare/onionshare/blob/main/LICENSE.txt
- https://docs.onionshare.org/
- `../sources/evidence/leads.md`

---

## 1. Purpose

Desktop and CLI tool that uses Tor onion services to share files, receive files, host a static website or run an ephemeral chat room directly between participants, with no intermediary server.

## Journalism / investigative use case

Direct, serverless transfer between a reporter and a source who are already in contact: the source runs OnionShare and sends a one-time onion address, the reporter downloads, and no third-party service ever holds the file or the metadata. The receive mode also gives a lightweight drop box without SecureDrop's infrastructure.

## 2. Audience

journalist, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- No intermediary at all — the file goes device to device over Tor, so there is no provider to subpoena, no account, and no retained copy
- Receive mode provides a usable drop box in minutes, which is the right tool when a source materialises and you have no SecureDrop
- Licence corrected in this survey: the project's own LICENSE.txt is GPL-3.0 (GitHub's NOASSERTION is caused by a prepended note pointing to bundled third-party licences, which is what produced session 1's incorrect reading)
- Very actively maintained (v2.7.2, 2026-11-07; pushed 2026-11-16) with 7,238 stars and a small backlog (63 open issues)

## 5. Cons

- Both parties must be online simultaneously for a transfer, which is a real coordination problem across time zones and for sources with intermittent connectivity
- Requires the source to install and run software and to understand onion addresses — a meaningful barrier for a non-technical source under stress
- Using Tor may itself be conspicuous on a monitored network, so in some countries the act of running OnionShare carries risk even though the transfer is protected
- Nothing protects against metadata inside the transferred documents, so mat2 and Dangerzone remain necessary afterwards

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 7,238 stars with 63 open issues, release v2.7.2 (2026-11-07), pushed 2026-11-16. The licence question is resolved with primary evidence: LICENSE.txt opens with '(Note: Third-party licenses can be found under licenses/.)' followed by the OnionShare copyright and the full GPL-3.0 text — recorded in sources/evidence/leads.md as lead L8.

## 7. Assessment

Adopt as the standard answer for ad-hoc secure transfer, and specifically teach reporters the receive mode — it is the fastest route from 'a source has documents' to 'we have them, with no intermediary'. For your profile the operational caveats to brief are the simultaneity requirement and the conspicuousness of Tor in some networks; where the latter matters, a bridge or a pre-arranged time window helps. Always follow a transfer with Dangerzone and mat2 before the documents touch anything else.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release v2.7.2 (2026-11-07), 7,238 stars, 63 open issues. Frequent releases with a clean tracker; long-standing project with a security-literate maintainer base.

## 9. Licensing

**Licence:** GPL-3.0 (project's own LICENSE.txt read directly 2026-11-17; GitHub reports NOASSERTION because a note about bundled third-party licences is prepended to the GPL text) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a. Third-party components under licenses/ have their own terms and must not be read as the project licence — this was the cause of session 1's misidentification.

**Restrictions:** GPL-3.0 on the project's own code; immaterial for ordinary use.

**Licence evidence:** https://github.com/onionshare/onionshare/blob/main/LICENSE.txt

## 10. Costs

Free. No infrastructure — the point is that there is no server. Bandwidth only.

## 11. Privacy and data flows

Among the strongest in the catalogue: no intermediary, no account, ephemeral onion address, nothing retained after the transfer. Residual risks are the conspicuousness of Tor on a monitored network and document metadata, neither of which OnionShare addresses.

## 12. Verdict

**Adopt**

## 13. Alternatives

- [SecureDrop](SUR-B3-01.md) where sources must be protected from the newsroom itself and cannot coordinate live
- [Hush Line](SUR-B3-06.md) for asynchronous encrypted tips
- Signal for messages and small files between parties who can both install it

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `repo-inspected`

- https://github.com/onionshare/onionshare/blob/main/LICENSE.txt
- https://docs.onionshare.org/
- `../sources/evidence/leads.md`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 25. [ICIJ Datashare](JAI-A2-23.md) · 27. [Orbot](SUR-B3-30.md) →
