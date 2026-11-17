# VeraCrypt

`SUR-B3-22` · **83/100** · overall rank 123 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 34) |
| **Segment** | B3 · Protecting journalists and sources (rank 21) |
| **Subcategory** | Disk and volume encryption |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | IDRIX / Mounir Idrassi |
| **Maintenance** | Actively maintained |
| **Licence** | Apache-2.0 plus TrueCrypt Licence 3.0 for inherited code (GitHub reports NOASSERTION) |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/veracrypt/VeraCrypt) · [Documentation](https://veracrypt.io/en/Documentation.html) |

**Scores** — relevance 4/5 · capability 4/5 · maintenance 4/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 83/100**

> **Material blockers recorded.** See [section 12](#material-blockers).

---

## 1. Purpose

Disk-encryption software creating encrypted containers and full-disk encryption on Windows, macOS and Linux, with hidden volumes and plausible-deniability features, derived from TrueCrypt.

## Journalism / investigative use case

Encrypting the archive of source material that must travel or be stored outside a controlled environment — an external drive carried across a border, a backup held off-site, or a container holding a leak on a shared workstation. The hidden-volume feature is sometimes used in high-risk travel, with serious caveats.

## 2. Audience

journalist, engineer, specialist investigator

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Cross-platform encrypted containers are the practical answer for material that must move between operating systems, where platform-native encryption (BitLocker, FileVault, LUKS) does not interoperate
- Full-disk and container modes cover both the laptop and the external drive cases with one tool and one mental model
- Actively maintained (VeraCrypt_1.26.31, 2026-11-02; pushed 2026-11-16) with a large user base (12,148 stars) and a TrueCrypt lineage that has been independently audited over the years
- Open source, so the encryption implementation can be examined rather than trusted on vendor assurance

## 5. Cons

- Hidden volumes provide plausible deniability only in theory: under coercive questioning at a border, the existence of VeraCrypt plus a refusal to produce a second password can itself be the problem, and several jurisdictions can compel disclosure — do not present this feature to journalists as safety
- GitHub reports SPDX NOASSERTION; the project is licensed under the Apache-2.0 plus TrueCrypt Licence 3.0 combination, which is unusual and needs reading before redistribution
- 515 open issues and a complex codebase with a single principal maintainer — a notable bus factor for security-critical software
- Full-disk encryption on a machine that is seized while running or suspended offers much less protection than users assume

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 12,148 stars with 515 open issues, release VeraCrypt_1.26.31 (2026-11-02), pushed 2026-11-16, SPDX NOASSERTION (the project's licensing combines Apache-2.0 with the TrueCrypt Licence 3.0 for inherited code). VeraCrypt and its TrueCrypt ancestor have been the subject of published independent audits, which is the strongest assurance signal available for encryption software here.

## 7. Assessment

Adopt for cross-platform encrypted containers, and be careful about how you present it. Two messages for the people you support: encryption protects data at rest on a powered-off device and little else, so shut down rather than suspend when crossing a border; and hidden volumes are not a safe answer to coercion, because the threat at a border is a person, not a cryptanalyst. Where the platform permits, native full-disk encryption (LUKS, FileVault) is simpler and better integrated — use VeraCrypt specifically for portable, cross-platform containers.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-16, latest release VeraCrypt_1.26.31 (2026-11-02), 12,148 stars, 515 open issues. Regular releases over many years; the large backlog and single-principal-maintainer structure are the notable risks, not activity.

## 9. Licensing

**Licence:** Apache-2.0 plus TrueCrypt Licence 3.0 for inherited code (GitHub reports NOASSERTION) _(SPDX not verified — resolved from the licence file or project documentation)_

**Model / data licence:** n/a

**Restrictions:** The TrueCrypt Licence 3.0 component is not an OSI-approved licence and has known redistribution ambiguities — relevant if you bundle VeraCrypt into a distributed product or image, immaterial for ordinary use.

**Licence evidence:** https://github.com/veracrypt/VeraCrypt/blob/master/License.txt

## 10. Costs

No fee. No infrastructure. Cost is user training and the discipline of key management — a forgotten passphrase on an encrypted archive is a permanent data loss.

## 11. Privacy and data flows

Strong at-rest protection when used correctly on a powered-off device. Residual risks are the ones that actually occur: suspended machines, keys in memory, coerced disclosure, and passphrases written down or reused.

## 12. Verdict

**Adopt**

## Material blockers

_Tracked separately from the score._

- Hidden-volume plausible deniability should not be relied on against coercive questioning

## 13. Alternatives

- LUKS (Linux), FileVault (macOS) or BitLocker (Windows) for native full-disk encryption where cross-platform portability is not needed
- age or GPG for encrypting individual files for transfer
- [Tails](SUR-B3-19.md) with an encrypted persistent volume for a portable working environment

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/veracrypt/VeraCrypt
- https://veracrypt.io/en/Documentation.html
- https://github.com/veracrypt/VeraCrypt/blob/master/License.txt

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

← 122. [shot-scraper](SUR-B1-23.md) · 124. [MarkItDown](JAI-A1-09.md) →
