# SecureDrop

`SUR-B3-01` · **92/100** · overall rank 22 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 5) |
| **Segment** | B3 · Protecting journalists and sources (rank 3) |
| **Subcategory** | Secure submission |
| **Type** | platform |
| **Bucket** | `verified-oss` |
| **Maintainer** | Freedom of the Press Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 (project's own licensing; GitHub API reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/freedomofpress/securedrop) · [Documentation](https://docs.securedrop.org/) |

**Scores** — relevance 5/5 · capability 5/5 · maintenance 5/5 · privacy 5/5 · usability 2/5 · licence+cost 4/5 → **weighted 92/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Whistleblower submission system where sources upload documents and messages over a Tor onion service to hardware controlled by the news organisation, with per-source codenames, no accounts and an air-gapped decryption model.

## Journalism / investigative use case

The reference system for receiving documents from a source who must not be identifiable, including by the news organisation itself: the source connects over Tor, receives a codename rather than an account, and submissions are decrypted on an air-gapped machine so a server compromise does not expose plaintext.

## 2. Audience

engineer, journalist

## 3. Project type

platform · bucket `verified-oss`

## 4. Pros

- Threat model is explicit and unusually honest: it is designed on the assumption that the server will be seized or compromised, which is why decryption is air-gapped rather than server-side
- Tor onion service means no IP address is exposed to the newsroom or its hosting provider, so the organisation cannot be compelled to produce what it never had
- Maintained by an organisation whose sole purpose is press freedom, with regular releases (2.16.2, 2026-10-29), published security audits and a documented support process
- Codename-based pseudonymity avoids collecting any source identifier at all — the strongest available posture against legal compulsion

## 5. Cons

- Heavy operational requirement: dedicated hardware (application server, monitor server, air-gapped Secure Viewing Station), physical security, and a maintenance routine — this is an institutional commitment, not a deployment
- Journalists must actually use the workstation discipline, and the system's security collapses if submissions are copied onto an ordinary laptop — the human failure mode dominates the technical one
- GitHub reports SPDX NOASSERTION (the project is AGPL-3.0 per its own licensing) and carries 479 open issues, reflecting a large, complex system
- Sources must find and trust the onion address, so publicising it safely is part of the work, and a source using Tor in a hostile country may itself attract attention

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 3,896 stars with 479 open issues, release 2.16.2 (2026-10-29), pushed 2026-11-14; session 1's ground_truth.tsv independently recorded AGPL-3.0 and the same release line. SecureDrop's deployment by major news organisations is publicly documented by FPF, and the project publishes independent security audits — the strongest assurance evidence in this catalogue.

## 7. Assessment

If your organisation intends to solicit documents from sources at real risk, this is the standard and I would adopt it — but only with the institutional commitment it requires, because a half-maintained SecureDrop is worse than none (it implies a protection it does not deliver). For an exile outlet the specific advantage is that it minimises what you hold: you cannot be compelled to produce source identities you never collected. If you cannot meet the operational bar, Hush Line or an OnionShare-based workflow is the honest fallback, and you should say publicly what protection you do and do not offer.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-14, latest release 2.16.2 (2026-10-29), 3,896 stars, 479 open issues. Regular versioned releases, a dedicated institutional maintainer (FPF), published security audits and a documented vulnerability-disclosure process — maintenance assessed on security process, not commit count.

## 9. Licensing

**Licence:** AGPL-3.0 (project's own licensing; GitHub API reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: a modified instance offered over a network obliges source publication. Running the released version for your own newsroom carries no obligation. Do not fork quietly — security-critical modifications should go upstream.

**Licence evidence:** https://github.com/freedomofpress/securedrop/blob/develop/LICENSE

## 10. Costs

No software fee. Real costs are hardware and staff: two servers plus an air-gapped Secure Viewing Station and a dedicated USB workflow (low four figures in hardware, estimate), a Tor-reachable hosting arrangement, and — dominantly — ongoing administrator time for updates and a journalist-training routine. Budget this as a permanent staffed service rather than a project.

## 11. Privacy and data flows

The strongest privacy design in this catalogue: Tor onion service (no source IP), no accounts (no identifiers), air-gapped decryption (no plaintext on a networked machine). Residual risks are real and must be managed: source-side risk from using Tor in a hostile network, metadata inside submitted documents (run Dangerzone and mat2), and the organisational discipline of never moving submissions onto ordinary devices.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Requires dedicated hardware, an air-gapped workstation and permanent administrator capacity — a partial deployment is actively misleading to sources

## 13. Alternatives

- [Hush Line](SUR-B3-06.md) for a far lighter encrypted tip line where SecureDrop's operational bar cannot be met
- [GlobaLeaks](SUR-B3-05.md) for a more configurable whistleblowing platform used widely by NGOs and public bodies
- [OnionShare](SUR-B3-04.md) for one-off direct transfers between two people who are already in contact

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/freedomofpress/securedrop
- https://docs.securedrop.org/
- `../sources/recovered/cat/ground_truth.tsv`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 5 | [Dangerzone](SUR-B3-03.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 21. [Datasette](JAI-A2-09.md) · 23. [CryptPad](SUR-B3-27.md) →
