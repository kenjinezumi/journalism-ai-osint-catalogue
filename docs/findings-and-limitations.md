# Findings, blockers and limitations

[← Catalogue home](../README.md) · [All rankings](rankings.md) · [Methodology](methodology.md) · [Stacks](stacks.md)

## Significant findings

### Licensing — the ones that will actually bite

1. **MVT and androidqf are not OSI-licensed.** MVT License 1.1 §3.0 requires the Data Owner's
   explicit, uncoerced, fully informed consent *including disclosure of your data-retention and
   disposal policy*. Quoted verbatim in `sources/evidence/leads.md`. Build the consent script.
2. **SuperGlue is academic/non-profit noncommercial only** (Magic Leap agreement, read this
   session). It is the most-cited matcher in geolocation pipelines, GitHub reports NOASSERTION so
   scanners miss it, and hloc's default pipelines can pull its weights. Use LoFTR (Apache-2.0).
3. **Marker and Surya weights are OpenRAIL-M** with a commercial threshold of **$5M revenue OR
   funding** ($2M for Chandra) — verified on datalab.to/pricing. Docling is the licence-clean
   alternative.
4. **Do No Harm licence** on Forensic Architecture's timemap and mtriage: clause 4 bars use by
   organisations deriving majority income from a listed set of activities, and clause 5 makes it
   viral on redistribution. Both repositories are also dormant.
5. **OpenSanctions: code MIT, data CC-BY-NC-4.0.** The data is the restricted layer and
   commercial use needs a paid licence (quote only). "OpenSanctions is open source" is true of
   the code only.
6. **Tracker Radar is CC-BY-NC-SA-4.0 data**, not software — NonCommercial plus ShareAlike, and
   GitHub reports NOASSERTION.
7. **CC-BY-NC on model weights** where you would not expect it: GLiNER v0/v1 checkpoints (the
   ones most tutorials link to), NVIDIA Sortformer diarisation, DeepfakeBench. The Apache-2.0
   code licence never cures a restricted weights licence.
8. **Non-OSI "open" tools:** n8n is Sustainable Use Licence (fair-code); MinerU is Apache-2.0
   *plus unread restrictive additional terms*; TruFor, Noiseprint, SBI and LAA-Net are all
   academic or non-profit-only.
9. **OnionShare is GPL-3.0** — session 1's error came from reading a bundled third-party licence.
   Corrected with primary evidence.
10. **AGPL network copyleft** matters in exactly one place people miss: embedding wabac.js in a
    public newsroom web application. Take advice before shipping that.

### Maintenance — what died, and why

Of 361 projects: 228 actively maintained, 72 stable with low activity, 18 declining, 25 dormant,
6 archived, 12 uncertain.

**Archived (confirmed `archived=true`):** Telethon (MIT, 12k stars — Telegram collection
pipelines inherit the risk) · Kùzu (embedded graph DB, final release 2025-10-10) ·
news-please (still widely recommended in data-journalism material) · pagodo · Whoogle ·
CooRnet · meedan/fetch.

**The pattern:** almost everything that died in 2024-2026 died because a **platform API or
scraping path was withdrawn**, not because maintainers lost interest. CrowdTangle killed CooRnet;
Google's anti-scraping killed Whoogle and automated dorking. Design collection layers so the data
source is replaceable without rewriting the analysis — CooRTweet versus CooRnet is the model.

**Declining but undeprecated, which is the dangerous state:** alephdata/aleph (use OpenAleph) ·
alephdata/followthemoney 3.x (use opensanctions/followthemoney 4.x — the old URL does *not*
redirect) · dedupe (no push since 2025-07-29; use Splink) · olmOCR (no activity since March 2026)
· Klaxon self-hosted (README warns it may miss changes) · Hyphe · Overview · Atlos (no release in
14 months, holding investigation-critical data).

**22 repository transfers verified by redirect**, including faster-whisper → SYSTRAN,
marker/surya → datalab-to, sentence-transformers → huggingface, DVC → **treeverse**,
Presidio → data-privacy-stack, NVIDIA/NeMo → NVIDIA-NeMo/Speech, Ragas → vibrantlabsai.
Pinned git URLs keep working; SBOMs and provenance records should be updated.

**17 session-1 candidate paths were genuine 404s** — bad discovery guesses, each resolved to its
real home in `sources/evidence/leads.md`.

### Pricing — verified, and deliberately unpriced

Verified from vendor pages with currency, period and basis: Transkribus (EUR0-449/yr plus credits)
· Datalab ($5M threshold; hosted Free/$400/mo Team) · Maltego (EUR3,000-7,500/yr per seat) ·
pyannote.ai (EUR0.035-0.198 per audio-hour) · Neo4j (Community free GPL-3; AuraDB from
$0.09/GB/hour; Enterprise quote-only) · Gemini API per-million-token rates with dated increases.

**Sentinel Hub / Planet: not publicly listed — quote required.** Re-verified twice: the
sentinel-hub pricing page returns only a redirect to planet.com/pricing, which renders no prices.
Treat commercial satellite imagery as an unpriced dependency and build on openly licensed
Sentinel/Landsat via pystac wherever the story allows.

**Have I Been Pwned figures are LOW confidence** — from secondary sources, not verified on the
vendor page. Do not budget against them.

**Deliberately not asserted:** DocumentCloud, Browsertrix hosted, Perma.cc, MuckRock, Shodan,
Censys, FOFA, Hunter, ZoomEye, Serper, OpenAI, Google Programmable Search, Carrot Search Lingo3G,
Artifex's PyMuPDF commercial licence, OpenCellID, Global Fishing Watch. Each is recorded as
unknown rather than estimated.

### Dependency and operational-security findings

- **Tools that upload by default and are easy to use anyway:** InVID-WeVerify plugin (media to
  AFP/vera.ai plus Google/Baidu/Yandex) · `datasette publish` · Perma.cc link creation ·
  ArchiveBot requests (public IRC) · OpenRefine reconciliation · Marker's LLM-enhancement mode ·
  Surya's configurable remote inference endpoint · webchanges' AI summaries · kuroi against a
  hosted model. Each is one click or one config line from disclosing an investigation.
- **Queries that disclose your targets to commercial vendors:** uncover and Mihari (scan
  databases) · streetlevel (Google/Apple/**Yandex**) · Maltego transforms · OpenCellID API.
- **The worst irony in the catalogue:** kuroi exists to find and remove source-identifying data
  and, pointed at a hosted LLM, transmits the unredacted documents to that provider.
- **Three tools whose own presence endangers the user** in a hostile jurisdiction: Tails (the
  USB), Orbot (the app), Tella (the camouflaged app). Brief people honestly.
- **Two dependency traps worth naming:** `alephdata/followthemoney` is two major versions behind
  with no redirect; grab-site depends on wpull, dormant since April 2024, so both layers stalled.

---

## Projects carrying material blockers

149 of 361 projects carry at least one recorded blocker. Blockers are tracked separately from scores, so a project can rank well and still be unusable for a particular organisation.

| Project | Total | Verdict | Blockers |
|---|--:|---|---|
| [mitmproxy](projects/SUR-B2-06.md) | 96 | Adopt | Certificate pinning blocks interception for many apps; intercepting traffic you are not authorised to intercept is unlawful |
| [Signal (Android client)](projects/SUR-B3-23.md) | 95 | Adopt | Requires a phone number — unsuitable where the source must not be identifiable |
| [OpenSanctions (dataset)](projects/OSINT-C3-01.md) | 94 | Adopt | Data is CC-BY-NC 4.0 — commercial-use licence required, price not publicly listed |
| [Ollama](projects/JAI-A3-02.md) | 94 | Adopt | Model licences in the library vary and are easy to overlook — verify before publishing work derived from a pulled model |
| [SecureDrop](projects/SUR-B3-01.md) | 92 | Adopt | Requires dedicated hardware, an air-gapped workstation and permanent administrator capacity — a partial deployment is actively misleading to sources |
| [CryptPad](projects/SUR-B3-27.md) | 92 | Adopt | Document keys travel in URLs — link handling is key handling |
| [Orbot](projects/SUR-B3-30.md) | 92 | Adopt | Presence of the app may itself be incriminating in some jurisdictions |
| [Tails](projects/SUR-B3-19.md) | 92 | Adopt | Requires firmware access to boot from USB; possession may itself carry risk in hostile jurisdictions |
| [MVT (Mobile Verification Toolkit)](projects/SUR-B3-08.md) | 90 | Adopt | MVT License 1.1 §3.0 consensual-use restriction — written informed consent and a disclosed retention policy are contractual requirements, and the licence is not OSI-approved |
| [EFF Rayhunter](projects/SUR-B3-13.md) | 90 | Adopt | Requires specific supported hotspot hardware; operating cellular monitoring may engage local radio law |
| [Qubes OS](projects/SUR-B3-20.md) | 89 | Pilot | Restrictive certified-hardware requirement; substantial learning curve and resource needs |
| [Tella](projects/OSINT-C3-06.md) | 89 | Adopt | Camouflage delays rather than prevents discovery; app presence may itself be incriminating |
| [IODA (Internet Outage Detection and Analysis)](projects/SUR-B1-07.md) | 88 | Adopt | Academic-use licence on the code — not usable as commercial newsroom infrastructure (the public dashboard is fine to use and cite) |
| [WhisperX](projects/JAI-A2-60.md) | 88 | Adopt | Gated pyannote diarisation weights — plan a central download for air-gapped deployments |
| [yente](projects/JAI-A2-61.md) | 88 | Adopt | OpenSanctions data is CC-BY-NC-4.0 — commercial-use licence required, price not publicly listed |
| [MobSF (Mobile Security Framework)](projects/SUR-B2-04.md) | 88 | Adopt | Reverse-engineering an app may engage terms of service and local law — obtain a legal view first |
| [SecureDrop Workstation](projects/SUR-B3-02.md) | 87 | Adopt | Requires Qubes-certified hardware; narrow compatibility list |
| [SimpleX Chat](projects/SUR-B3-25.md) | 87 | Pilot | Much less independent cryptographic review than Signal; large open-issue backlog for security-critical software |
| [Marker](projects/JAI-A2-28.md) | 86 | Pilot | Weights are OpenRAIL-M with a $5M revenue-or-funding commercial threshold — a licence decision, not a technical one |
| [GlobaLeaks](projects/SUR-B3-05.md) | 86 | Pilot | HTTPS submission path exposes source IPs; server-side decryption weakens the seizure threat model relative to SecureDrop |
| [USAspending.gov (custom award data)](projects/SUR-B2-14.md) | 86 | Adopt | Classified and some national-security procurement excluded; recipient naming requires entity resolution before aggregation |
| [PyMuPDF](projects/JAI-A2-42.md) | 86 | Integrate | AGPL-3.0 network copyleft if deployed inside a public-facing service without a commercial licence |
| [Apktool](projects/SUR-B2-05.md) | 86 | Adopt | Reverse engineering may breach app terms and local law |
| [OONI Probe CLI / probe-engine](projects/SUR-B1-01.md) | 85 | Adopt | Operator risk in repressive jurisdictions; ASN and network name are published with results |
| [androidqf](projects/SUR-B3-09.md) | 85 | Adopt | MVT License 1.1 §3.0 consensual-use restriction; not OSI-approved |
| [OONI Probe Multiplatform](projects/SUR-B1-02.md) | 85 | Adopt | Volunteer risk: app presence on device plus published network metadata |
| [n8n](projects/JAI-A1-17.md) | 85 | Monitor | Sustainable Use Licence (fair-code) is not open source and restricts offering n8n as a service to third parties |
| [TED — Tenders Electronic Daily (EU public procurement)](projects/SUR-B2-13.md) | 84 | Adopt | Above-threshold publication only; national-security exemptions hide much surveillance procurement |
| [CourtListener](projects/OSINT-C3-11.md) | 84 | Adopt | US jurisdiction only; state-court and RECAP coverage is incomplete |
| [Nextcloud](projects/SUR-B3-28.md) | 84 | Adopt | Server-side encryption does not protect documents from the server operator or a host compromise |
| [Nominatim](projects/OSINT-C2-28.md) | 84 | Integrate | Public instance forbids bulk geocoding; self-hosting required for the primary use case |
| [monolith](projects/OSINT-C1-39.md) | 84 | Adopt | No JavaScript execution — fails silently on client-rendered pages |
| [Global Fishing Watch API client](projects/OSINT-C2-50.md) | 83 | Adopt | Data terms and current access tiers not verified — confirm before publishing derived datasets |
| [Browsertrix](projects/OSINT-C1-30.md) | 83 | Pilot | Kubernetes requirement for self-hosting; hosted option places captures in third-party custody |
| [Querido Diário](projects/OSINT-C3-14.md) | 83 | Integrate | Brazil-specific coverage; per-municipality coverage is uneven |
| [VeraCrypt](projects/SUR-B3-22.md) | 83 | Adopt | Hidden-volume plausible deniability should not be relied on against coercive questioning |
| [InVID-WeVerify Verification Plugin](projects/JAI-A4-04.md) | 82 | Adopt | Uploads media to third-party backends — unsuitable for unpublished or source-sensitive material |
| [DuckDuckGo Tracker Radar](projects/SUR-B2-03.md) | 82 | Reference only | CC-BY-NC-SA-4.0 — NonCommercial bars commercial productisation; ShareAlike propagates to derived datasets |
| [LlamaIndex](projects/JAI-A3-04.md) | 82 | Pilot | Default configurations use hosted embedding and model providers — must be explicitly made local for source material |
| [GLiNER](projects/JAI-A2-19.md) | 81 | Adopt | CC-BY-NC-4.0 on the v0/v1 checkpoints — a commercial-use blocker if the wrong model ID is pinned |
| [Neo4j Community Edition](projects/OSINT-C3-35.md) | 81 | Integrate | Community Edition lacks access control and clustering; Enterprise pricing is quote-only |
| [pyannote.audio](projects/JAI-A2-41.md) | 81 | Integrate | Gated weights requiring HuggingFace identity disclosure — plan a one-time central download for air-gapped or anonymity-sensitive deployments |
| [streetlevel](projects/OSINT-C2-32.md) | 80 | Integrate | Uses providers' internal interfaces — terms-of-service risk and breakage; queries disclose target coordinates to the providers |
| [Molly](projects/SUR-B3-24.md) | 80 | Pilot | Release cadence trails upstream Signal — verify the current version gap before deploying |
| [stalkerware-indicators](projects/SUR-B3-10.md) | 79 | Integrate | No licence — redistribution legally unresolved |
| [httpx](projects/OSINT-C3-24.md) | 79 | Adopt | Active probing is visible to the target and may engage computer-misuse law |
| [Stanza](projects/JAI-A2-49.md) | 79 | Integrate | Model-archive licence is unstated — unresolved commercial-use risk for derived published datasets |
| [Open Contracting Data Standard](projects/SUR-B2-18.md) | 79 | Integrate | Value depends on publisher adoption, which is uneven and often partial |
| [Surya](projects/JAI-A2-52.md) | 78 | Pilot | Weights are OpenRAIL-M with a $5M revenue-or-funding commercial threshold |
| [OpenSecrets lobbying data](projects/SUR-B2-17.md) | 78 | Integrate | Data reuse terms not verified — confirm before republishing as a dataset |
| [Aleph (alephdata, original)](projects/OSINT-C3-02.md) | 77 | Reference only | Development has moved to the OpenAleph fork; no deprecation notice makes the stale line easy to adopt by mistake |
| [Delta Chat / chatmail core](projects/SUR-B3-26.md) | 77 | Integrate | Mail metadata exposes the sender-recipient relationship unless both parties use chatmail servers |
| [FollowTheMoney (alephdata 3.x line)](projects/JAI-A2-18.md) | 77 | Avoid for new deployment | This repository is a stale major version with no deprecation notice; development moved to opensanctions/followthemoney and the old URL does not redirect |
| [Media Cloud API client](projects/JAI-A1-14.md) | 77 | Integrate | Service dependency with unverified access terms; uneven archive coverage by country and period |
| [openstates-scrapers](projects/OSINT-C3-13.md) | 77 | Integrate | US only; per-state coverage quality varies |
| [Amnesty International investigations (indicators of compromise)](projects/SUR-B3-11.md) | 76 | Integrate | No licence; repository not pushed since December 2024 — do not treat as a live indicator feed |
| [OWASP Amass](projects/OSINT-C3-22.md) | 75 | Adopt | Active scanning modes are detectable and may engage computer-misuse law |
| [RIPE Atlas tooling (Magellan CLI, Cousteau, Sagan)](projects/SUR-B1-12.md) | 75 | Adopt | Thin probe coverage in many high-interest countries; measurements are public by default |
| [uncover](projects/OSINT-C1-10.md) | 75 | Integrate | Queries disclose your investigation targets to commercial scan vendors; several required APIs are paid |
| [Ushahidi Platform](projects/OSINT-C3-07.md) | 75 | Pilot | Submitter database is a high-value target in repressive environments; SMS channel has real per-message costs |
| [Citizen Lab URL test lists](projects/SUR-B1-06.md) | 75 | Integrate | CC-BY-NC-SA-4.0 NonCommercial clause — blocks commercial redistribution and productisation |
| [Ragas](projects/JAI-A3-13.md) | 75 | Adopt | LLM-as-judge metrics are relative signals, not absolute measures; a hosted judge would disclose source documents |
| [sugartrail](projects/OSINT-C3-19.md) | 75 | Adopt | UK only; shared addresses and officers indicate association, not wrongdoing |
| [Open-Meteo](projects/OSINT-C2-41.md) | 75 | Integrate | Hosted service is framed as free for non-commercial use — commercial newsrooms must self-host or verify their position |
| [titiler](projects/JAI-A1-27.md) | 75 | Monitor | Publishing commercial satellite imagery as tiles is redistribution and usually needs explicit permission |
| [HTTrack](projects/OSINT-C1-18.md) | 75 | Integrate | Not WARC: weak provenance, unsuitable as evidence of record |
| [DocumentCloud](projects/JAI-A2-13.md) | 74 | Pilot | Hosted custody of documents is unsuitable for unpublished sensitive material in a hostile-state threat model |
| [MuckRock](projects/OSINT-C3-15.md) | 74 | Integrate | Publish-by-default discloses requests; US jurisdiction only; service fees unverified |
| [Perma](projects/OSINT-C1-37.md) | 74 | Integrate | Hosted captures and links are public — discloses what you archived and when |
| [Tabula](projects/JAI-A2-53.md) | 74 | Reference only | No release since 2018 and 541 open issues — frozen GUI; use the maintained libraries for anything new |
| [wabac.js](projects/OSINT-C1-33.md) | 74 | Monitor | AGPL-3.0 embedding in a public web application — legal review required |
| [Overpass API](projects/OSINT-C2-23.md) | 73 | Integrate | Public-instance queries disclose geolocation targets; self-hosting is required for private querying |
| [dedupe](projects/JAI-A2-11.md) | 73 | Monitor | No commits or releases since July 2025 — unsuitable as a new long-term dependency |
| [ProofMode](projects/SUR-B3-32.md) | 73 | Pilot | Proof-strengthening metadata can identify the photographer — configuration is a safety trade-off |
| [SAM.gov](projects/SUR-B2-15.md) | 73 | Integrate | Some data and API access require registration, creating a record of your interest |
| [NVIDIA NeMo Speech](projects/JAI-A2-32.md) | 73 | Pilot | CC-BY-NC-4.0 on the Sortformer diarisation checkpoint — commercial-publication blocker for that specific model |
| [olmOCR](projects/JAI-A2-34.md) | 72 | Pilot | No repository activity since March 2026 — do not build a long-lived pipeline on it without accepting fork responsibility |
| [Klaxon (self-hosted)](projects/SUR-B1-18.md) | 72 | Monitor | Project's own README warns it may break and may miss changes; individual-user support discontinued |
| [Klaxon Cloud (DocumentCloud Add-On)](projects/SUR-B1-19.md) | 72 | Pilot | Hosted: monitoring activity and detected changes are visible to MuckRock infrastructure |
| [PyExifTool](projects/OSINT-C2-02.md) | 72 | Integrate | Dormant since 2023; have a direct-subprocess fallback in mind |
| [kuroi](projects/JAI-A4-24.md) | 71 | Pilot | Hosted-LLM configuration would transmit unredacted sensitive documents to a third party — must be pinned to a self-hosted model |
| [overpass-turbo](projects/OSINT-C2-24.md) | 71 | Integrate | Public instance discloses queries and bounding boxes |
| [MinerU](projects/JAI-A1-11.md) | 71 | Monitor | Licence is Apache-2.0 plus unread additional terms recorded as restrictive — legal review required before commercial use |
| [sentinelhub-py](projects/OSINT-C2-43.md) | 70 | Pilot | Service pricing not publicly listed — quote required; post-acquisition availability of free/research tiers unconfirmed<br>Requests disclose target coordinates and dates to the vendor |
| [bellingcat/EDGAR](projects/OSINT-C3-16.md) | 70 | Monitor | Eighteen months without maintenance against a changing official interface |
| [Pelias](projects/OSINT-C2-30.md) | 70 | Monitor | Mixed data-source licensing requires per-source review before publishing derived datasets |
| [unitedstates/congress](projects/OSINT-C3-42.md) | 70 | Integrate | US federal only; volunteer maintenance against changing official sites |
| [US Senate Lobbying Disclosure Act database](projects/SUR-B2-16.md) | 69 | Integrate | Bot protection blocks automated collection; current interface not verified in this survey |
| [ethereum-etl](projects/OSINT-C3-20.md) | 69 | Monitor | Requires archive-node access or a commercial provider; address attribution is not solved by this tool |
| [smolagents](projects/JAI-A3-11.md) | 69 | Pilot | Code-executing agents require deliberate sandboxing and egress denial before touching source material |
| [Mihari](projects/SUR-B2-11.md) | 67 | Pilot | Continuous querying discloses your investigative watchlist to commercial scan vendors; several required APIs are paid |
| [AnalyticsRelationships](projects/SUR-B2-09.md) | 67 | Pilot | Depends on third-party reverse-analytics services whose availability and terms are outside your control |
| [Hierarchical-Localization (hloc)](projects/OSINT-C2-35.md) | 67 | Pilot | Default pipelines can pull noncommercially licensed SuperGlue weights — component audit required |
| [LoFTR](projects/OSINT-C2-34.md) | 66 | Pilot | Dormant since mid-2024 — pin dependencies and expect to own maintenance |
| [YaCy](projects/OSINT-C1-06.md) | 66 | Pilot | P2P mode would disclose index fragments — must be explicitly disabled |
| [GraphSense](projects/OSINT-C3-21.md) | 64 | Monitor | Substantial ingestion infrastructure required; clustering heuristics are probabilistic and must be stated as such |
| [warcprox](projects/OSINT-C1-42.md) | 64 | Integrate | WARCs contain credentials and session tokens from proxied traffic; requires installing a local CA certificate |
| [Katna](projects/OSINT-C2-11.md) | 64 | Monitor | Dormant since 2024; frame selection optimises for appeal rather than completeness |
| [Overview](projects/OSINT-C3-04.md) | 64 | Reference only | Development pace has declined; the architecture is heavy relative to modern alternatives |
| [WhatWeb](projects/SUR-B2-08.md) | 64 | Integrate | Active scanning is detectable and may engage computer-misuse law |
| [OpenCellID](projects/SUR-B2-19.md) | 63 | Integrate | Licence and access terms unverified; crowdsourced coverage gaps mean an unknown cell is not evidence of a simulator |
| [Alaveteli](projects/JAI-A1-28.md) | 63 | Reference only | Publish-by-default model is unsuitable for sensitive journalistic requests |
| [SpiderFoot](projects/OSINT-C3-29.md) | 63 | Monitor | A full scan discloses the target to many third parties at once and includes active probing |
| [CouncilSearcher](projects/OSINT-C1-14.md) | 63 | Monitor | UK/Ireland only; scraper-dependent with ten months of no maintenance |
| [ArchiveBot](projects/OSINT-C1-26.md) | 62 | Integrate | Requests and captures are public — unusable for confidential investigation |
| [DataIndex.us (Federal Data Terminations Tracker)](projects/SUR-B1-27.md) | 62 | Reference only | No public repository located; licence and terms unverified; hosted single point of failure |
| [Internet Society Pulse](projects/SUR-B1-14.md) | 62 | Reference only | Code not public and public repository unlicensed — reuse terms unverified, not self-hostable |
| [mapillary_tools](projects/OSINT-C2-31.md) | 62 | Monitor | Uploading discloses reporter movements with timestamps to a third-party platform |
| [OpenOversight](projects/SUR-B2-12.md) | 62 | Reference only | Jurisdiction-specific coverage; operating a comparable database raises significant data-protection obligations outside the US |
| [TruFor](projects/JAI-A4-18.md) | 61 | Monitor | Licence restricts use to informational and non-profit purposes — commercial newsroom use requires permission |
| [theHarvester](projects/OSINT-C3-28.md) | 61 | Integrate | Harvested email addresses are regulated personal data requiring a retention and protection decision |
| [Kùzu](projects/JAI-A3-18.md) | 61 | Avoid for new deployment | Archived as of 2025-10-10 — a frozen database engine is an unacceptable dependency for investigation data |
| [Microsoft Planetary Computer](projects/OSINT-C2-45.md) | 60 | Pilot | Hosted third-party custody of analysis and areas of interest; current access terms unverified |
| [gdelt-doc-api](projects/JAI-A1-15.md) | 60 | Integrate | Dormant client; GDELT data noise means counts are not publishable as findings |
| [grab-site](projects/OSINT-C1-24.md) | 60 | Monitor | Dormant since May 2025; depends on wpull, dormant since April 2024 |
| [news-please](projects/JAI-A1-02.md) | 60 | Avoid for new deployment | Archived as of 2026-04-14 — read-only, and news-site changes will silently degrade coverage |
| [VFRAME](projects/OSINT-C2-14.md) | 60 | Reference only | Dormant since 2023; deep-learning dependency stack requires porting |
| [Maltego](projects/OSINT-C3-36.md) | 59 | Reference only | Proprietary with substantial per-seat annual cost; every transform discloses investigation targets to the vendor and data providers |
| [Froide](projects/JAI-A1-29.md) | 59 | Reference only | German-law orientation; publish-by-default unsuitable for sensitive requests |
| [PhotoHolmes](projects/JAI-A4-17.md) | 59 | Pilot | Bundled methods carry mixed and partly non-commercial licences — per-method audit required before commercial publication |
| [recon-ng](projects/OSINT-C3-30.md) | 59 | Monitor | Slowed maintenance against degraded data sources means silent module failure |
| [Bellingcat smart-image-sorter](projects/OSINT-C2-15.md) | 59 | Monitor | Dormant since 2024; model generation behind current capability |
| [DeepfakeBench](projects/JAI-A4-25.md) | 58 | Monitor | CC-BY-NC-4.0 — non-commercial only<br>Some referenced datasets are not rights-cleared |
| [AASIST](projects/JAI-A4-29.md) | 58 | Pilot | Dormant since 2023; trained against pre-2024 synthesis methods |
| [Google Fact Check Tools API](projects/JAI-A4-16.md) | 57 | Integrate | Hosted proprietary API with deprecation and quota risk outside your control; terms and pricing unverified in this survey |
| [Zingg](projects/JAI-A1-20.md) | 56 | Monitor | Spark dependency is disproportionate for most newsroom volumes; open-core capability boundary unverified |
| [wpull](projects/OSINT-C1-25.md) | 54 | Avoid for new deployment | Dormant since April 2024 with a 208-issue backlog; superseded by wget's own WARC support |
| [blockhash-python](projects/OSINT-C2-09.md) | 54 | Reference only | Dormant since 2023 and superseded by better-maintained alternatives |
| [SuperGlue (pretrained network)](projects/OSINT-C2-33.md) | 53 | Avoid for new deployment | Noncommercial academic-only licence — unusable by a commercial newsroom, and invisible to SPDX scanners |
| [ClaimBuster-Spotter](projects/JAI-A4-05.md) | 51 | Reference only | Dormant since 2023; checkpoint licensing unresolved |
| [SelfBlendedImages (SBI)](projects/JAI-A4-27.md) | 51 | Monitor | Research-only licence; commercial use requires a separate agreement |
| [Andriller](projects/SUR-B3-17.md) | 51 | Avoid for new deployment | Dormant since 2022; Android internals have changed substantially since |
| [diffengine](projects/SUR-B1-25.md) | 50 | Reference only | Unmaintained since 2020; social integration depends on a withdrawn Twitter API |
| [DEFAME](projects/JAI-A4-11.md) | 49 | Monitor | Hosted LLM and external search by default — images and claims leave your infrastructure |
| [LAA-Net](projects/JAI-A4-28.md) | 49 | Monitor | Academic-only licence — not usable as commercial newsroom infrastructure |
| [Deepfake-Eval-2024](projects/JAI-A4-31.md) | 47 | Reference only | No licence for code or data — redistribution legally unresolved<br>No evaluation code included |
| [ASVspoof 2021 baseline systems](projects/JAI-A4-30.md) | 46 | Reference only | No licence file — reuse legally unresolved<br>MATLAB dependency for original baselines |
| [Noiseprint](projects/JAI-A4-22.md) | 46 | Avoid for new deployment | Non-commercial licence<br>TensorFlow 1.2.1 dependency pin |
| [dorks_hunter](projects/OSINT-C1-08.md) | 43 | Avoid for new deployment | No licence — reuse legally unresolved<br>Automated Google dorking degraded by anti-scraping measures |
| [Fetch (Meedan ClaimReview aggregator)](projects/JAI-A4-03.md) | 43 | Reference only | Archived by the maintainer — do not build on it |
| [FacTool](projects/JAI-A4-12.md) | 42 | Reference only | Requires hosted LLM and search APIs<br>Dormant since August 2024 |
| [FaceForensics++](projects/JAI-A4-26.md) | 42 | Reference only | Gated research-use dataset agreement — not usable as commercial infrastructure<br>Predates current generative models, limiting relevance |
| [Whoogle Search](projects/OSINT-C1-04.md) | 39 | Avoid for new deployment | Archived; the Google scraping path it depends on is closed |
| [Loki (OpenFactVerification)](projects/JAI-A4-10.md) | 38 | Avoid for new deployment | Requires OpenAI and Serper API keys — text leaves your infrastructure by design<br>Dormant since October 2024 |
| [AVeriTeC dataset and baseline](projects/JAI-A4-07.md) | 36 | Reference only | No licence file — redistribution and commercial use legally unresolved<br>Requires Google Search API; not a local pipeline |
| [CooRnet](projects/JAI-A4-14.md) | 36 | Reference only | Archived, and its sole data source (CrowdTangle) was discontinued |
| [pagodo](projects/OSINT-C1-07.md) | 36 | Reference only | Archived; automated Google dorking is non-functional as of late 2026 |
| [NewsDiffs](projects/SUR-B1-26.md) | 34 | Reference only | Python 2.6-era stack, abandoned since 2018, mixed per-file licensing |
| [ClaimsKG extractor](projects/JAI-A4-09.md) | 29 | Avoid for new deployment | No licence file and fork provenance unclear — legally unresolved<br>Four-year-old scraper against changed target sites |

---

## Licensing and pricing that remain unverified

Counted from [`records/`](../records/) at build time, across all 361 projects. Licensing and payment are counted separately because they are separate questions.

| Measure | Projects | What it means |
|---|--:|---|
| Licence unresolved or open-source status unverified | 13 | No licence file, no SPDX identifier and no licence statement that the evidence could confirm. Reuse is legally unresolved |
| SPDX identifier not independently verified | 116 | A licence is recorded and in most cases named by the GitHub API or the project's documentation, but the licence file itself was not read in this survey. The recorded licence is a research note, not a verified SPDX determination |
| Software price not established | 8 | The records do not establish a price. **Not** a finding that the project is free |
| Mandatory paid dependency recorded | 12 | A paid API, dataset, model, licence or tool is required for the core function, whatever the software itself costs |

### Licence unresolved or status unverified (13)

| Project | Recorded licence | Status |
|---|---|---|
| [AVeriTeC dataset and baseline](projects/JAI-A4-07.md) | NOT CONFIRMED — no LICENSE/COPYING file in the repository root, GitHub licence API reports none, README has no licence section | Unverified |
| [ClaimsKG extractor](projects/JAI-A4-09.md) | NOT CONFIRMED — GitHub licence API returns 404 and no LICENSE file detected; code is a fork of vwoloszyn/fake_news_extractor, compounding provenance uncertainty | Unverified |
| [ASVspoof 2021 baseline systems](projects/JAI-A4-30.md) | NOT CONFIRMED — no root LICENSE file found (direct fetch of /blob/main/LICENSE returned 404); terms may differ per baseline subdirectory | Unverified |
| [Deepfake-Eval-2024](projects/JAI-A4-31.md) | NOT CONFIRMED — no licence for code or data visible on the repository page | Unverified |
| [dorks_hunter](projects/OSINT-C1-08.md) | NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found | Unverified |
| [rtl-ais](projects/OSINT-C2-49.md) | GPL (from source headers: derived from rtl_fm by Kyle Keen, AISDecoder by Astra Paging/AISHub and GNUAIS; GitHub reports NOASSERTION) | Open source |
| [unitedstates/congress](projects/OSINT-C3-42.md) | Public domain / CC0 (unitedstates project convention — confirm from the repository licence file) | Open source |
| [stalkerware-indicators](projects/SUR-B3-10.md) | NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found (2026-11-17) | Unverified |
| [Amnesty International investigations (indicators of compromise)](projects/SUR-B3-11.md) | NOT CONFIRMED — no licence detected by the GitHub API and no LICENSE file found (2026-11-17) | Unverified |
| [security-misc (Kicksecure)](projects/SUR-B3-21.md) | Not detected by the GitHub API — read the repository licence file before redistribution (the Kicksecure/Whonix ecosystem is predominantly GPL-family) | Open source |
| [Delta Chat / chatmail core](projects/SUR-B3-26.md) | Not detected by the GitHub API — read the repository licence file (the Delta Chat/chatmail ecosystem is GPL-family) before redistribution | Open source |
| [Orbot](projects/SUR-B3-30.md) | Not detected by the GitHub API — read the repository licence file (Guardian Project projects are predominantly BSD/GPL-family) | Open source |
| [Privacy Badger](projects/SUR-B3-33.md) | GPL-family per EFF's licensing (GitHub reports NOASSERTION — read the repository licence file for records) | Open source |

### Software price not established (8)

These are hosted services or platforms whose current terms were not confirmed in this survey. Several have historically had free or free-for-journalists tiers; that history is recorded on the project pages and is not treated as a current price.

| Project | Recorded cost position |
|---|---|
| [DocumentCloud](projects/JAI-A2-13.md) | Hosted DocumentCloud access has historically been free to verified journalists with paid organisational tiers; current prices were NOT verified in this survey — treat as not publicly verified here and check with MuckRock. Cloud OCR add-ons incur the underlying vendor's per-page charges (not priced here). Self-hosting costs are Django app servers, object storage and a search index, plus substantial undocumented-deployment engineering effort. |
| [Google Fact Check Tools API](projects/JAI-A4-16.md) | Pricing and quota NOT verified in this survey — treat as not publicly confirmed here and check the current terms before relying on it. Historically free within quota; a Google API key is required, and Search Console verification is required for the ClaimReview write API. |
| [Perma](projects/OSINT-C1-37.md) | Hosted perma.cc uses institutional tiers (library and organisation subscriptions) whose current prices were NOT verified in this survey — check before budgeting. Self-hosting: no software fee but a Django stack plus storage, realistically a multi-VM deployment. Assumptions for self-hosting: moderate capture volume. |
| [Microsoft Planetary Computer](projects/OSINT-C2-45.md) | Historically free for catalogue access and Hub compute, but current terms and limits were NOT verified in this survey — treat as unknown and confirm before planning work around it. No software fee. |
| [MuckRock](projects/OSINT-C3-15.md) | Service fees and account tiers NOT verified in this survey — MuckRock has historically charged for filing credits with free tiers for some users. Confirm before planning a filing programme. Self-hosting would be a major Django deployment. Estimate. |
| [Awesome Website Change Monitoring](projects/SUR-B1-24.md) | None to read. Note that the commercial services it catalogues have their own pricing, none of which was verified in this survey. |
| [OpenCellID](projects/SUR-B2-19.md) | Not verified in this survey. Historically a free tier with API keys and paid tiers above it; confirm current pricing before planning. No software cost. |
| [Hush Line](projects/SUR-B3-06.md) | Self-hosting: a small VM plus a Tor onion service — low. The hosted service has free and paid tiers whose current prices were NOT verified in this survey. Staff cost is PGP key management and monitoring the channel. |

### Mandatory paid dependencies (12)

| Project | Software price | What must be paid for |
|---|---|---|
| [yente](projects/JAI-A2-61.md) | No software fee | mandatory paid data licence for commercial use (quote); self-hosted Elasticsearch/OpenSearch |
| [AVeriTeC dataset and baseline](projects/JAI-A4-07.md) | No software fee | mandatory paid dependency; self-hosted infrastructure |
| [Loki (OpenFactVerification)](projects/JAI-A4-10.md) | No software fee | mandatory paid dependency; self-hosted infrastructure |
| [DEFAME](projects/JAI-A4-11.md) | No software fee | mandatory paid dependency; self-hosted infrastructure |
| [FacTool](projects/JAI-A4-12.md) | No software fee | mandatory paid dependency |
| [CooRTweet](projects/JAI-A4-13.md) | No software fee | mandatory paid dependency |
| [uncover](projects/OSINT-C1-10.md) | No software fee | mandatory paid scan-database API keys for useful coverage (Shodan, Censys, FOFA, Hunter, ZoomEye — prices not verified); negligible compute |
| [sentinelhub-py](projects/OSINT-C2-43.md) | No software fee | mandatory paid satellite-imagery service for commercial constellations (quote required); self-hosted compute |
| [OpenSanctions (dataset)](projects/OSINT-C3-01.md) | No software fee | mandatory paid data licence for commercial use (quote); optional hosted Screening API (prepaid credits); self-hosted Elasticsearch |
| [Ushahidi Platform](projects/OSINT-C3-07.md) | No software fee | mandatory per-message SMS gateway charges for the SMS channel (rates vary by country, not priced); self-hosted infrastructure; staff triage effort |
| [ethereum-etl](projects/OSINT-C3-20.md) | No software fee | mandatory archive-node access — self-run (multi-terabyte storage) or a paid commercial node provider (not priced); warehouse storage |
| [Mihari](projects/SUR-B2-11.md) | No software fee | mandatory paid dependency; self-hosted infrastructure |

---

## Remaining evidence gaps and provisional conclusions

23 projects are marked **provisional** and 13 are **low confidence**. The substantive gaps:

1. **Unresolved licences** (treat reuse as legally unclear): AVeriTeC, ClaimsKG extractor,
   ASVspoof 2021 baselines, Deepfake-Eval-2024, dorks_hunter, stalkerware-indicators,
   AmnestyTech/investigations. Indicator repositories without licences are a systemic problem.
2. **MinerU's additional terms were recorded as restrictive in session 1 but not characterised.**
   Get a legal reading before any commercial use.
3. **Stanza's model archives have no stated licence** while the code is Apache-2.0. Unresolved
   commercial-use risk for derived published datasets.
4. **Hosted-service maintenance cannot be evidenced like a repository's.** Google Fact Check
   Tools API, Internet Society Pulse, DataIndex.us, Microsoft Planetary Computer, OpenCellID and
   the Senate LDA database are classified Uncertain on purpose, not by omission.
5. **Bot protection is not evidence of removal.** OpenSecrets and lda.senate.gov returned 403 to
   `curl`; both are recorded as live-but-unverified. The **EU Transparency Register** is the one
   genuinely unresolved source URL — the old ec.europa.eu path 404s.
6. **Scoop's cryptographic signing format was not independently verified** beyond the
   maintainers' description. Confirm with Harvard LIL before relying on it in a legal filing.
7. **Model weights not individually verified** for Docling, PaddleOCR, Alegre's bundled
   checkpoints, RAGFlow's parsing models, Kraken's Zenodo models and several spaCy and Stanza
   language packs. In each case the code licence is clear and the weights are not.
8. **No project was installed or run.** Every capability claim rests on documentation, repository
   inspection and API metadata. The three I would want hands-on before committing budget are
   OpenAleph (Elasticsearch sizing), RAGFlow (whether reporters trust it appropriately) and
   Rayhunter (false-positive rate on your actual networks).
9. **Feedback is thin by design.** Where I found no documented user reports, the card says so.
   Issue-to-star ratios and release cadence are used as *maintenance* evidence, never as proxies
   for quality or for user satisfaction.

### Provisional assessments (23)

| Project | Total | Confidence | Verdict |
|---|--:|---|---|
| [stalkerware-indicators](projects/SUR-B3-10.md) | 79 | medium | Integrate |
| [OpenSecrets lobbying data](projects/SUR-B2-17.md) | 78 | low | Integrate |
| [Amnesty International investigations (indicators of compromise)](projects/SUR-B3-11.md) | 76 | medium | Integrate |
| [MinerU](projects/JAI-A1-11.md) | 71 | medium | Monitor |
| [US Senate Lobbying Disclosure Act database](projects/SUR-B2-16.md) | 69 | low | Integrate |
| [AnalyticsRelationships](projects/SUR-B2-09.md) | 67 | low | Pilot |
| [GraphSense](projects/OSINT-C3-21.md) | 64 | low | Monitor |
| [OpenCellID](projects/SUR-B2-19.md) | 63 | low | Integrate |
| [Hoover](projects/OSINT-C3-03.md) | 63 | low | Monitor |
| [HURIDOCS preserve](projects/OSINT-C3-10.md) | 63 | low | Monitor |
| [juditha](projects/OSINT-C3-09.md) | 63 | low | Monitor |
| [DataIndex.us (Federal Data Terminations Tracker)](projects/SUR-B1-27.md) | 62 | low | Reference only |
| [Internet Society Pulse](projects/SUR-B1-14.md) | 62 | low | Reference only |
| [Microsoft Planetary Computer](projects/OSINT-C2-45.md) | 60 | low | Pilot |
| [Full Fact AI Trust Benchmark](projects/JAI-A4-15.md) | 58 | medium | Reference only |
| [Google Fact Check Tools API](projects/JAI-A4-16.md) | 57 | low | Integrate |
| [Zingg](projects/JAI-A1-20.md) | 56 | low | Monitor |
| [CenAlert](projects/SUR-B1-10.md) | 54 | medium | Monitor |
| [Deepfake-Eval-2024](projects/JAI-A4-31.md) | 47 | medium | Reference only |
| [ASVspoof 2021 baseline systems](projects/JAI-A4-30.md) | 46 | medium | Reference only |
| [dorks_hunter](projects/OSINT-C1-08.md) | 43 | medium | Avoid for new deployment |
| [AVeriTeC dataset and baseline](projects/JAI-A4-07.md) | 36 | medium | Reference only |
| [ClaimsKG extractor](projects/JAI-A4-09.md) | 29 | medium | Avoid for new deployment |

---

## Reconciliation

| Count | Value |
|---|---|
| Unique projects in `records/` | **361** |
| Rows in `catalogue.json` `projects[]` | **361** |
| Rows in `catalogue.csv` (excluding header) | **361** |
| Assessment cards in this report | **361** |
| Entries in the overall ranked table | **361** |
| Duplicate IDs | 0 |
| Validation errors from `build.py` | 0 |

**Recovered versus new.** Session 1's consolidation reported 185 unique projects. That count was
**one too high**: ThreatExchange appeared twice because A4 recorded it as `meta/ThreatExchange`
and C2 as `facebook/ThreatExchange`, and session 1's RENAMES map lacked that transfer. The GitHub
API confirms the redirect, so **184 recovered projects** carry into this catalogue, all of them
assessed. The remaining **177 are new work** in this session: the four segments session 1 never
reached (A1 32, A3 20, B2 20, B3 31 new of 33) plus 32 new C2 records filling the truncated
geospatial, satellite, aviation and maritime coverage, and 42 new C3 records.

**Segment totals:** A1 32 · A2 61 · A3 20 · A4 31 · B1 27 · B2 20 · B3 33 · C1 45 · C2 50 · C3 42.
**Pillars:** Journalism and AI 144 · Surveillance and journalist protection 80 · OSINT 137.

**Segment re-homing.** Each project appears in exactly one segment. Where session 1's assignment
did not match a project's primary role it was moved and the move recorded in `STATE.md`:
Dangerzone and mat2 to B3; yt-dlp to C1; ExifTool, PyExifTool, ImageHash, MediaInfo,
PySceneDetect, Sherloq, GeoCLIP, ShadowFinder and SunCalc to C2. No project is counted twice.
