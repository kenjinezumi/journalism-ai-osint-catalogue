# Dangerzone

`SUR-B3-03` · **92/100** · overall rank 24 of 361 · verdict **Adopt**

[← Catalogue home](../../README.md) · [All rankings](../rankings.md) · [Surveillance and journalist protection](../surveillance.md) · [Methodology](../methodology.md)

| | |
|---|---|
| **Pillar** | Surveillance and journalist protection (rank 7) |
| **Segment** | B3 · Protecting journalists and sources (rank 5) |
| **Subcategory** | Document sanitisation |
| **Type** | application |
| **Bucket** | `verified-oss` |
| **Maintainer** | Freedom of the Press Foundation |
| **Maintenance** | Actively maintained |
| **Licence** | AGPL-3.0 |
| **Confidence** | high |
| **Verified** | 2026-11-17 |
| **Links** | [Repository](https://github.com/freedomofpress/dangerzone) · [Documentation](https://dangerzone.rocks/) |

**Scores** — relevance 5/5 · capability 4/5 · maintenance 5/5 · privacy 5/5 · usability 4/5 · licence+cost 4/5 → **weighted 92/100**

---

## 1. Purpose

Desktop application that converts potentially malicious PDFs, Office documents and images into safe PDFs by rendering them to pixels inside an isolated container and rebuilding a clean file, with optional OCR to restore a text layer.

## Journalism / investigative use case

The step before any other tool in this catalogue touches a document from an unknown source: a file is sanitised so opening it cannot execute an exploit or beacon out to the sender. That protects the reporter's machine and, just as importantly, prevents a document from signalling to its originator that it has been opened — which can expose that a leak is being investigated.

## 2. Audience

journalist, newsroom analyst, engineer

## 3. Project type

application · bucket `verified-oss`

## 4. Pros

- Addresses a threat that is real and routinely ignored: weaponised documents sent to journalists are a documented attack vector, and ordinary antivirus does not reliably stop a targeted exploit
- The pixel round-trip is a structural rather than detection-based defence — it does not need to recognise the exploit to neutralise it, which is why it works against unknown attacks
- Fully local by design: the whole premise is that nothing is uploaded and the conversion is isolated from the host, which distinguishes it from cloud sanitisation services
- Actively maintained (v0.11.1, 2026-10-22; pushed 2026-11-09) by FPF with a journalism-specific threat model and installable builds for all desktop platforms

## 5. Cons

- The pixel round-trip destroys the text layer unless OCR is enabled, and the OCR'd text is then only as accurate as Tesseract — so sanitised documents are worse for search and quotation than originals, and teams are tempted to skip it
- Conversion is slow on large documents, which again creates pressure to bypass it on exactly the big leaked set where it matters most
- Container runtime dependency (Docker or Podman) complicates installation on managed or locked-down machines
- AGPL-3.0 affects redistribution of a modified version; 193 open issues reflect the breadth of document formats in the wild

## 6. Feedback (documented)

No individual user reports verified in this survey. Documented: 5,850 stars with 193 open issues, release v0.11.1 (2026-10-22), pushed 2026-11-09, AGPL-3.0 (independently recorded in session 1's ground_truth.tsv). FPF builds it specifically for journalists, and the threat it addresses — malicious documents targeting newsrooms — is documented in published threat reporting.

## 7. Assessment

Adopt it as a mandatory first step and automate it so the choice is not left to a tired reporter at midnight: ingest pipelines should sanitise on arrival, keeping the original in a quarantined store for later forensic examination. For your profile the detail that matters most is preserving both artefacts — the sanitised copy for reading and the untouched original for analysis — because the original is evidence about the sender and discarding it loses that. Enable OCR, and accept the accuracy cost rather than skipping sanitisation.

## 8. Maintenance

**Actively maintained** — GitHub API 2026-11-17: archived=false, pushed_at 2026-11-09, latest release v0.11.1 (2026-10-22), 5,850 stars, 193 open issues. Regular releases from an institutional maintainer with a security-focused mission; session 1 independently verified the same licence and release line.

## 9. Licensing

**Licence:** AGPL-3.0 _(SPDX verified)_

**Model / data licence:** n/a

**Restrictions:** AGPL-3.0: distributing a modified version or offering it as a service obliges source publication. Desktop use is unaffected.

**Licence evidence:** https://github.com/freedomofpress/dangerzone/blob/main/LICENSE

## 10. Costs

No fee. A container runtime and CPU time — conversion is the cost, measured in minutes per large document. No paid dependencies. For a large leak, budget compute time in the ingest plan.

## 11. Privacy and data flows

Fully local — nothing is uploaded and the conversion is isolated from the host. This is the correct architecture and the direct contrast with commercial document-sanitisation services, which would receive your source documents.

## 12. Verdict

**Adopt**

## 13. Alternatives

- Opening documents inside a disposable Qubes VM or a Tails session for equivalent isolation without the text-layer loss
- A dedicated offline examination machine, which is slower but preserves fidelity
- Commercial sanitisation services — avoid, since they require uploading source documents

## 14. Evidence

Verified **2026-11-17** · confidence **high** · assessment depth `metadata-verified`

- https://github.com/freedomofpress/dangerzone
- https://dangerzone.rocks/
- https://github.com/freedomofpress/dangerzone/blob/main/LICENSE
- `../sources/recovered/cat/ground_truth.tsv`

---

## Related in this segment

| # | Project | Total | Verdict |
|--:|---|--:|---|
| 1 | [Signal (Android client)](SUR-B3-23.md) | 95 | Adopt |
| 2 | [mat2](SUR-B3-07.md) | 94 | Adopt |
| 3 | [SecureDrop](SUR-B3-01.md) | 92 | Adopt |
| 4 | [CryptPad](SUR-B3-27.md) | 92 | Adopt |
| 6 | [OnionShare](SUR-B3-04.md) | 92 | Adopt |
| 7 | [Orbot](SUR-B3-30.md) | 92 | Adopt |
| 8 | [Tails](SUR-B3-19.md) | 92 | Adopt |
| 9 | [MVT (Mobile Verification Toolkit)](SUR-B3-08.md) | 90 | Adopt |

---

← 23. [CryptPad](SUR-B3-27.md) · 25. [ICIJ Datashare](JAI-A2-23.md) →
