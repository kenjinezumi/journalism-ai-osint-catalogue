# GlobaLeaks

`SUR-B3-05` · **86/100** · overall rank 69 of 361 · verdict **Pilot**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 22) |
| **Segment** | B3 · Protecting journalists and sources (rank 15) |
| **Subcategory** | Secure submission |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Hermes Center for Transparency and Digital Human Rights |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/globaleaks/globaleaks-whistleblowing-software) · [Documentation](https://docs.globaleaks.org/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 3/5 · usability 4/5 · licence+cost 4/5 → **weighted 86/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Configurable whistleblowing platform supporting anonymous submissions over Tor or HTTPS, multi-tenant deployments, customisable questionnaires, case management and multilingual interfaces.

## Journalism / investigative use case

A whistleblowing channel you can shape to the reporting context: unlike SecureDrop's deliberately minimal model, GlobaLeaks lets you build structured intake (questionnaires, categories, recipient routing), which suits a newsroom running several tip lines or a consortium where submissions must route to different partners.

## 2. Audience

engineer, newsroom analyst

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Configurability and multi-tenancy are the distinguishing features: one deployment can serve multiple outlets or desks with separate recipients, which matters for consortium investigations
- Supports both Tor and HTTPS access, so a source who cannot use Tor still has a protected channel — broader reach than Tor-only systems, at a stated cost in anonymity
- AGPL-3.0, very actively maintained (v5.0.101, 2026-10-28; pushed 2026-11-17), with a long deployment history across NGOs, anti-corruption bodies and public institutions
- Repository renamed (globaleaks/globaleaks → globaleaks/globaleaks-whistleblowing-software, transfer verified by redirect), so the canonical path is current

## 5. Cons

- The HTTPS option is a genuine trade-off, not just convenience: a submission over HTTPS exposes the source's IP to the hosting path, so the default must be understood and the choice explained to sources
- 620 open issues — the largest backlog in this subcategory — reflecting a broad feature surface and configurability that can be misconfigured
- Decryption happens on the platform rather than on an air-gapped station, so a compromised server is a more consequential event than with SecureDrop's model
- Configuration flexibility means security depends on your choices; a badly configured GlobaLeaks can retain far more than it should

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 1,529 stars with 620 open issues, release v5.0.101 (2026-10-28), pushed 2026-11-17, AGPL-3.0; repository transfer confirmed by API redirect on 2026-11-17. GlobaLeaks' use by anti-corruption authorities and NGOs is documented by the project, which is relevant institutional adoption evidence.

## 7. Assessment

The right choice when you need structured intake or multi-recipient routing and can accept a weaker threat model than SecureDrop's; the wrong choice if your sources face state-level adversaries and you want minimal retained data. For your profile the decisive question is who you are protecting sources from: GlobaLeaks protects against opportunistic exposure and gives you workflow, while SecureDrop is built for the case where the newsroom itself may be compelled. Document which model you are offering, publicly and accurately.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-17, latest release v5.0.101 (2026-10-28), 1,529 stars, 620 open issues. Same-day commits and a very frequent release cadence under an established non-profit maintainer.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified instance offered over a network obliges source publication. Relevant if you customise the platform for partners, which is a common GlobaLeaks use.

**Licence evidence:** https://github.com/globaleaks/globaleaks-whistleblowing-software/blob/main/LICENSE

## 10. Costs

No software fee. Infrastructure estimate: a hardened VM or dedicated server with Tor and HTTPS endpoints, plus encrypted storage — modest hardware, but security-critical hosting and permanent administrator attention. Assumptions: single-tenant newsroom deployment.

## 11. Privacy and data flows

Tor submissions give no IP to the newsroom; HTTPS submissions do expose source IPs to the network path, which must be communicated to sources rather than left implicit. Server-side decryption means a seized or compromised server is a serious event — plan key handling and retention accordingly.

## 12. Verdict

**Pilot**

## Material blockers

_Tracked separately from the score._

- HTTPS submission path exposes source IPs; server-side decryption weakens the seizure threat model relative to SecureDrop

## 13. Alternatives

- [SecureDrop](SUR-B3-01.md) where the threat model requires air-gapped decryption and minimal retained data
- [Hush Line](SUR-B3-06.md) for a lightweight encrypted tip line
- [OnionShare](SUR-B3-04.md) receive mode for ad-hoc intake with no platform at all

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/globaleaks/globaleaks-whistleblowing-software
- https://docs.globaleaks.org/
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
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |

---

← 68. [Exodus Privacy](SUR-B2-01.md) · 70. [Outline](SUR-B3-31.md) →
