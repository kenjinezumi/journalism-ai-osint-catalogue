# OpenTimestamps

`OSINT-C3-41` · **74/100** · overall rank 227 of 361 · verdict **Integrate**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [OSINT and digital investigations](../osint.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | OSINT and digital investigations (rank 77) |
| **Segment** | C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration (rank 23) |
| **Subcategory** | Evidence timestamping |
| **Type** | cli |
| **Bucket** | `verified-oss` |
| **Maintainer** | OpenTimestamps project (Peter Todd) |
| **Maintenance** | Stable with low activity |
| **Licence** | LGPL-3.0 (project licensing — confirm from the repository licence file) |
| **Confidence** | medium |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/opentimestamps/opentimestamps-client) · [Documentation](https://opentimestamps.org/) |

**Scores** — relevance 4/5 · capability 3/5 · maintenance 3/5 · privacy 5/5 · usability 3/5 · licence+cost 4/5 → **weighted 74/100**

---

## 1. Purpose

Client for creating and verifying trustless timestamp proofs anchored in the Bitcoin blockchain, attesting that a file existed at a given time without relying on a trusted timestamping authority.

## Journalism / investigative use case

Proving when you received material without revealing it: timestamp the hash of a leaked document on receipt, and you can later demonstrate that you held that exact file from that date — which matters if the authenticity or the timing of your acquisition is challenged, and which discloses nothing because only the hash is published.

## 2. Audience

engineer, specialist investigator

## 3. Project type

cli · bucket `verified-oss`

## 4. Pros

- Hash-only anchoring means you prove possession at a time without disclosing content — exactly the property source protection requires, and a notarisation service cannot offer
- Trustless verification: the proof depends on the Bitcoin blockchain rather than on a company that must still exist and be trusted when you need it, which for a decade-long legal horizon is a real advantage
- Free to use with no account, so timestamping every received document at ingest costs nothing and requires no relationship
- Simple and auditable: the proof format is specified and verifiable independently of the original client

## 5. Cons

- Proves existence at a time, nothing more: it says nothing about where a document came from, whether it is authentic, or who made it — and a published claim must be precise about that narrow meaning
- Confirmation waits on Bitcoin block inclusion, so a proof takes hours to become complete — fine for ingest, not for a same-hour claim
- Depends on public calendar servers for aggregation, so your hash submissions are visible to those operators (the hash only, not the content)
- Niche and single-maintainer-adjacent, with modest activity; the specification's durability matters more than the client's

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented from the metadata sweep: the repository is live and non-archived. OpenTimestamps is an established approach to trustless timestamping with a published specification; journalism use is uncommon and unverified here.

## 7. Assessment

Integrate it into document ingest — timestamping the hash of every received file is a few lines in a pipeline and gives you an evidentiary property you cannot retrofit. For your profile the specific scenario it addresses is a government later claiming a document was fabricated after an event: a timestamp proof from the date of receipt rebuts that directly. Be precise in any published claim about what it proves, which is possession of that exact file at that time and nothing else.

## 8. Maintenance

**Stable with low activity** — Verified via the GitHub API 2026-11-17 as live and non-archived with modest activity. Classified stable-low: the specification and proof format are the durable artefacts, and the client is small and feature-complete, so low velocity carries less risk than usual.

## 9. Licensing

**Licence:** LGPL-3.0 (project licensing — confirm from the repository licence file) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** LGPL permits linking from your own tooling provided the library remains replaceable.

**Licence evidence:** https://github.com/opentimestamps/opentimestamps-client

## 10. Costs

Free. No Bitcoin transaction fee for the user — the calendar servers aggregate submissions. Negligible compute.

## 11. Privacy and data flows

Only the hash is submitted, so content is never disclosed — the property that makes it usable on source material. The calendar operators see your hash submissions and their timing, which reveals that you timestamped something on a date, not what.

## 12. Verdict

**Integrate**

## 13. Alternatives

- A commercial trusted timestamping authority (RFC 3161), which is faster and requires trusting a company
- Publishing a hash in a dated public venue, which is cruder and still effective
- Sigstore for signing rather than timestamping

## 14. Evidence

Verified **2026-11-17** · confidence **medium** · assessment depth `metadata-verified`

- https://github.com/opentimestamps/opentimestamps-client
- https://opentimestamps.org/

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

← 226. [Leaflet](JAI-A1-21.md) · 228. [Tabula](JAI-A2-53.md) →
