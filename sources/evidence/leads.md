# Preserved research leads — resolution with primary evidence
All GitHub facts below come from this session's own `gh api` calls on **2026-11-17**
(saved in `../../work/meta.jsonl` and `licences/*`). Licence texts were read from the
repository's own licence blob via `GET /repos/{owner}/{repo}/license`, not inferred.

---
## L1 — MVT and androidqf licence restrictions  → CONFIRMED, material blocker
- `mvt-project/mvt`: licence blob `LICENSE`, GitHub SPDX = **NOASSERTION**, actual text
  = **MVT License 1.1** (an MPL-2.0 derivative). archived=false, pushed 2026-11-17,
  release `v2026.11.2` (2026-11-02), 16,096 stars.
- `mvt-project/androidqf`: same **MVT License 1.1**. pushed 2026-11-07, release `v1.8.3`
  (2026-05-12), 387 stars.
- The operative restriction, quoted verbatim from `LICENSE` §3.0 (full text saved at
  `licences/mvt-project_mvt.LICENSE.txt`, lines 177-183):

  > 3.0. Consensual Use Restriction
  > Use of Covered Software or of a Larger Work is permitted provided that
  > the Data Owner must explicitly consent to the procedure, free from any
  > form of coercion, and must be fully informed about the nature of the
  > procedure, its privacy implications, and any data retention and disposal
  > policy.

- Consequence: **not an OSI-approved licence** (field-of-use restriction). Lawful and
  practical for consensual device checks on a journalist's or source's own phone — which is
  exactly the intended use — but it forbids non-consensual forensic acquisition, and the
  informed-consent + retention-disclosure duty is a contractual obligation, not just ethics.
  Any newsroom offering device checks needs a written consent script and a data-retention
  policy to stay inside the licence. Redistribution in a larger product carries the same
  restriction downstream (MPL-style file-level copyleft plus §3.0).
- Evidence: https://github.com/mvt-project/mvt/blob/main/LICENSE ,
  https://github.com/mvt-project/androidqf/blob/main/LICENSE (read 2026-11-17, confidence high)

---
## L2 — Do No Harm licensing in Forensic Architecture projects  → CONFIRMED, material blocker
- `forensic-architecture/timemap`: licence blob `LICENSE.md`, SPDX NOASSERTION, actual text
  = **Do No Harm License**. archived=false but pushed **2025-06-02**, last release `0.3.0`
  (2019-08-19) → dormant, not active.
- `forensic-architecture/mtriage`: same **Do No Harm License**; pushed **2023-08-25**, no
  releases → dormant.
- Clause 4 (saved at `licences/forensic-architecture_timemap.LICENSE.txt`, lines 24-50)
  bars use by any organisation, website, product or service that lobbies for, promotes or
  derives a majority of income from (inter alia) gambling, tobacco, nuclear energy, warfare,
  weapons manufacturing, violence "except when required to protect public safety", deforestation,
  or hate speech/discrimination; and by anyone deriving a majority of income from frustrating
  peace, UDHR rights, peaceful assembly, climate action or democratic processes.
  Clause 5 makes the terms viral on redistribution and forbids altering who may use it.
- Consequence: **not OSI-approved** (ethical-source field-of-use restriction). For an
  independent newsroom the clause-4 list is unlikely to bite on its own conduct, but it is viral:
  any derivative you ship inherits it, and a downstream recipient (a media partner owned by a
  conglomerate with tobacco/weapons/gambling revenue, or a platform you distribute through)
  can be out of compliance. Treat as a licensing-review item before embedding in a product,
  and never relicense.
- Evidence: https://github.com/forensic-architecture/timemap/blob/master/LICENSE.md ,
  https://github.com/forensic-architecture/mtriage/blob/master/LICENSE.md (read 2026-11-17, high)

---
## L3 — Aleph vs the independent OpenAleph fork  → CONFIRMED, two separate projects
- `alephdata/aleph` (OCCRP): MIT, archived=**false**, pushed **2026-02-20**, latest release
  `4.1.7` (2025-10-27), 2,513 stars. Live repository, but no substantive push in ~9 months and
  no release in ~13 months → *maintenance appears to be declining* for the public repo.
- `openaleph/openaleph` (DARC — Data and Research Center): MIT, `fork=true`,
  `parent=alephdata/aleph` (confirmed by the GitHub API, not inferred), pushed **2026-11-16**,
  latest release **`5.4.0` (2026-11-16)**, 156 stars → *actively maintained*.
- They are **not interchangeable**: OpenAleph has diverged (own 5.x line, own ingest stack —
  `openaleph/ingest-file` is the maintained fork of the archived `alephdata/ingest-file`),
  and OCCRP continues to run Aleph for its own network. Catalogued as **two separate entries**,
  cross-referenced, not merged.
- Related relocation, same ecosystem: **FollowTheMoney**. `alephdata/followthemoney` is MIT,
  not archived, but pushed 2026-02-28 with latest release `v3.8.2` (2025-03-24), whereas
  `opensanctions/followthemoney` is MIT, pushed 2026-11-11, latest release `v4.11.3`
  (2026-11-07). FTM's active 4.x development is at OpenSanctions; the alephdata repo is the
  stale 3.x line. This is a **relocation of development, not a GitHub rename** — the old URL
  does **not** redirect and both repos resolve independently. Anyone pinning `followthemoney`
  from the alephdata path is on an abandoned major version.
- Evidence: GitHub API 2026-11-17 for all four repos (`work/meta.jsonl`), confidence high.

---
## L4 — Repository transfers and renames  → verified by following redirects, nothing "broken"
Verified with `GET /repos/{old}` (REST follows renames and returns the new `full_name`).
Confirmed transfers, old URL **redirects**:
| old path | current path |
|---|---|
| guillaumekln/faster-whisper | **SYSTRAN/faster-whisper** |
| VikParuchuri/marker | **datalab-to/marker** |
| VikParuchuri/surya | **datalab-to/surya** |
| UKPLab/sentence-transformers | **huggingface/sentence-transformers** |
| iterative/dvc | **treeverse/dvc** |
| deltachat/deltachat-core-rust | **chatmail/core** |
| microsoft/presidio | **data-privacy-stack/presidio** |
| NVIDIA/NeMo | **NVIDIA-NeMo/Speech** |
| facebook/ThreatExchange | **meta/ThreatExchange** |
| globaleaks/globaleaks | **globaleaks/globaleaks-whistleblowing-software** |
| edsu/diffengine | **DocNow/diffengine** |
| hoover/search | **liquidinvestigations/hoover-search** |
| webrecorder/conifer | **Rhizome-Conifer/conifer** |
| micahflee/torbrowser-launcher | **torproject/torbrowser-launcher** |
| guardianproject/orbot | **guardianproject/orbot-android** |
| guardianproject/proofmode | **guardianproject/proofmode-android** |
| kermitt2/grobid | **grobidOrg/grobid** |
| meteostat/meteostat-python | **meteostat/meteostat** |
| ascribe/image-match | **rhsimplex/image-match** |
| corteva/rioxarray | **vylor/rioxarray** |
| expectocode/telegram-export | **tnjd/telegram-export** |
| Jigsaw-Code/outline-apps | **OutlineFoundation/outline-apps** |

**followthemoney is NOT in this table** — see L3; it is a relocation with two live repos.
Note on DVC: `iterative/dvc` now redirects to `treeverse/dvc`; the transfer follows
Iterative's acquisition. Governance change is a monitoring item, not a licence change
(still Apache-2.0 per the API).
Note on sentence-transformers: now under the `huggingface` org, still Apache-2.0.
Practical implication: pinned git URLs keep working (GitHub serves 301s), but
`go get`-style tooling, SBOM scanners and provenance records should be updated to the
canonical paths. Confidence high (API, 2026-11-17).

Session-1 candidate paths that are genuine **404s** (not redirects) — these were bad
discovery guesses and are excluded from the catalogue, with the real project named:
`0xacab/mat2` and `rhaberkorn/mat2` → real: `jvoisin/mat2` (GitHub) / 0xacab.org GitLab home ·
`bellingcat/sherlock` → `sherlock-project/sherlock` · `bellingcat/edgar-tool` →
`bellingcat/EDGAR` (GPL-3.0, last release v2.1.2 2025-05-15) · `coornet/CooRnet` and
`JasonRBowling/CooRnet` → `fabiogiglietto/CooRnet` (**archived**, pushed 2024-08-14) ·
`estebanpdl/osintgram` → `Datalux/Osintgram` · `mozilla/blacklight` →
`the-markup/blacklight-collector` · `palewire/warn-scraper` → `biglocalnews/warn-scraper` ·
`webrecorder/awesome-web-archiving` → `iipc/awesome-web-archiving` (CC0-1.0) ·
`freedomofpress/hushline` → `scidsg/hushline` (AGPL-3.0, v0.7.36 2026-11-05) ·
`KasperskyLab/TinyCheck`, `Whonix/Whonix`, `occrp/hazard`, `OpenUpSA/open-gazettes`,
`MuckRock/muckrock-addons`, `jsvine/pdfplumber-template-maker` → no GitHub repo at that path
on 2026-11-17 (404 with no redirect; Whonix and Tails are developed on their own
GitLab/Git infrastructure, which is the correct home to cite).

---
## L5 — Telethon archival status  → CONFIRMED archived
`LonamiWebs/Telethon`: `archived=true`, pushed 2026-02-21, MIT, 12,066 stars, no "latest
release" exposed by the API. The repository is read-only on GitHub.
Consequence: a MIT-licensed, widely used Telegram MTProto client that is now **archived** —
Telegram layer changes will break it and no upstream fixes will come. Material blocker for
new Telegram-collection pipelines; Telethon-based tooling (telegram-tracker, Telerecon,
tdl-adjacent scripts) inherits the risk. Use it only with a plan to fork or migrate.
Evidence: GitHub API 2026-11-17, confidence high.

---
## L6 — OpenSanctions: different code and dataset licences  → CONFIRMED, split licensing
- Code: `opensanctions/opensanctions` licence blob `LICENSE` = **MIT**, SPDX MIT
  (copyright OpenSanctions Datenbanken GmbH 2023-2026; earlier Friedrich Lindenberg and
  Journalism Development Network). archived=false, pushed 2026-11-17. Same for the
  surrounding code: `yente` (search API), `nomenklatura`, `rigour`, `followthemoney`.
- Data: the published entity data is **CC-BY-NC 4.0**; commercial use requires a paid licence.
  Screening API sells prepaid credit bundles; Screening Licence and Reseller/OEM are
  **quote-only**. Verified from the vendor licensing page 2026-11-16 (`../recovered/cat/pricing.tsv`).
- Consequence: you may self-host the whole stack for free and lawfully, but the **data** is the
  restricted layer. A commercially operated newsroom cannot assume NGO status satisfies "NonCommercial";
  publishing an article informed by the data is ordinary journalistic use, whereas building a
  paid product or client-facing screening service on the dataset needs the paid licence.
  Treat "OpenSanctions is open source" as true of the code only.
- Evidence: https://github.com/opensanctions/opensanctions/blob/main/LICENSE (2026-11-17, high);
  https://www.opensanctions.org/licensing/ (2026-11-16, high)

---
## L7 — Tracker Radar status and dataset licence  → CONFIRMED, non-commercial dataset
`duckduckgo/tracker-radar`: SPDX NOASSERTION; licence blob `LICENSE` reads verbatim:
> Copyright 2020 Duck Duck Go, Inc.
> Licensed under the CC BY-NC-SA 4.0 license, available at
> https://creativecommons.org/licenses/by-nc-sa/4.0/. Note that this license does not apply
> to any DuckDuckGo logos or marks that may be contained in this repo.

Status: archived=false, pushed 2026-11-16, latest release `2026.11.10` (2026-11-10),
1,749 stars → **actively maintained**, released on a dated cadence.
Consequence: this is a **dataset, not software** — CC-BY-NC-SA 4.0 means (a) no commercial
use without permission, (b) **ShareAlike**: derivative datasets must carry the same licence.
Excellent as reference evidence for a tracker-attribution story; a blocker for embedding in a
commercially operated product, and the SA term can contaminate a combined dataset you publish.
The crawler that produces it (`duckduckgo/tracker-radar-collector`) is separately licensed
software — check it independently rather than inheriting the dataset licence.
Evidence: https://github.com/duckduckgo/tracker-radar/blob/main/LICENSE (2026-11-17, high)

---
## L8 — OnionShare licence-identification error  → CORRECTED to GPL-3.0
Session 1 recorded an incorrect licence for OnionShare after reading a bundled third-party
licence. Resolved from the project's own blob: `onionshare/onionshare` licence path
**`LICENSE.txt`**, whose first line is literally
`(Note: Third-party licenses can be found under licenses/.)` followed by
`OnionShare / Copyright (C) 2014-2026 Micah Lee, et al.` and the full
**GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007**.
GitHub reports SPDX NOASSERTION purely because of that prepended note, which is why an
automated reader plus a glance at `licenses/` produced the wrong answer.
**Correct licence: GPL-3.0** (project's own code). Third-party components under `licenses/`
have their own terms and must not be read as the project licence.
Status: archived=false, pushed 2026-11-16, latest release `v2.7.2` (2026-11-07), 7,238 stars
→ actively maintained.
Evidence: https://github.com/onionshare/onionshare/blob/main/LICENSE.txt (read 2026-11-17, high)
This also matches session 1's `ground_truth.tsv` note ("LICENSE.txt heading = GPLv3"), so the
corrected value is the one carried into the catalogue.

---
## Cross-cutting lesson recorded for the catalogue
GitHub SPDX `NOASSERTION` means "the detector could not match", and it resolves three
different ways: a real non-OSI licence (MVT 1.1, Do No Harm), a standard licence with a
prepended note (OnionShare GPL-3.0, warn-scraper Apache-2.0), or a licence that is a dataset
licence rather than a software one (Tracker Radar CC-BY-NC-SA-4.0). Every NOASSERTION in this
catalogue was resolved by reading the blob; none were left as "Other".

---
## L9 — NEW finding this session: SuperGlue is non-commercial, and six more NOASSERTION licences resolved
Discovered while extending the truncated C2 segment. Not in session 1's lead list; recorded here
because it is a material blocker of the same class as L1/L2.

- `magicleap/SuperGluePretrainedNetwork`: licence blob `LICENSE`, SPDX NOASSERTION. The text opens:
  > SUPERGLUE: LEARNING FEATURE MATCHING WITH GRAPH NEURAL NETWORKS
  > SOFTWARE LICENSE AGREEMENT
  > **ACADEMIC OR NON-PROFIT ORGANIZATION NONCOMMERCIAL RESEARCH USE ONLY**
  > ... agreement between your academic institution or non-profit organization or self ... and
  > Magic Leap, Inc.

  SuperGlue is the most-cited feature matcher used in image-geolocation pipelines, and it is
  **unusable by a commercially operated newsroom**. Dormant too (pushed 2024-08-30, no releases).
  Permissive alternative: `zju3dv/LoFTR` (Apache-2.0) or `cvg/Hierarchical-Localization`
  (Apache-2.0), though hloc's own pipelines can pull SuperGlue weights — check what you enable.
  Evidence: https://github.com/magicleap/SuperGluePretrainedNetwork/blob/master/LICENSE (2026-11-17, high)

Other NOASSERTION values resolved by reading the blob (all 2026-11-17, confidence high):
| repo | GitHub SPDX | actual licence (from blob) |
|---|---|---|
| OSGeo/gdal | NOASSERTION | aggregate `LICENSE.TXT` — MIT-licensed core plus many component licences; read the file before redistribution |
| rasterio/rasterio | NOASSERTION | BSD-3-Clause (Mapbox copyright) |
| maplibre/maplibre-gl-js | NOASSERTION | BSD-3-Clause (MapLibre contributors) |
| protomaps/PMTiles | NOASSERTION | BSD-3-Clause for the reference implementations; the **specification itself is public domain / CC0**; bundled sample tilesets have their own terms |
| stac-utils/pystac | NOASSERTION | Apache-2.0 |
| flightaware/dump1090 | NOASSERTION | GPL-2.0-or-later, with the maintainer inviting contact for GPL-incompatible uses |
| dgiardini/rtl-ais | NOASSERTION | GPL (from source headers; derived from rtl_fm/AISDecoder/GNUAIS lineage) |
| tyrasd/overpass-turbo | NOASSERTION | MIT, with a note that bundled libraries carry their own licences |

Licence blobs saved under `licences/`.

---
## L10 — NEW findings this session: two more transfers and two more archivals
Found while researching the segments session 1 never reached. Same class of hazard as L4/L5.

**Transfers (old path redirects, verified 2026-11-17):**
| old path | current path | note |
|---|---|---|
| explodinggradients/ragas | **vibrantlabsai/ragas** | RAG evaluation library; still Apache-2.0, v0.4.4 released 2026-11-14. Governance moved to a company — monitor |
| meteostat/meteostat-python | **meteostat/meteostat** | weather data client, MIT, v2.2.3 released 2026-11-11 |

**Archived (read-only, verified by `archived=true` on the GitHub API 2026-11-17):**
| repo | last push | note |
|---|---|---|
| **kuzudb/kuzu** | 2025-10-10 | embedded graph database, MIT, final release v0.11.3 the same day, 4,022 stars. A serious option for newsroom knowledge graphs is now frozen — use DuckDB, Neo4j Community or Oxigraph instead |
| **fhamborg/news-please** | 2026-04-14 | news crawler and article extractor, Apache-2.0, 2,493 stars, no releases. Widely recommended in data-journalism material; now archived. Use trafilatura for extraction and Scrapy for crawling |
| **opsdisk/pagodo** | 2026-11-01 | Google-dorking tool, GPL-3.0, archived with a final release v2.8.0. Consistent with the wider collapse of automated Google dorking in 2026 |
| **benbusby/whoogle-search** | 2026-08-14 | self-hosted Google front end, MIT, 11,551 stars. Google closed the scraping path it depended on |
| **fabiogiglietto/CooRnet** | 2024-08-14 | coordinated-link-sharing detection, MIT. Archived in step with the CrowdTangle shutdown that removed its only data source |
| **LonamiWebs/Telethon** | 2026-02-21 | see L5 |
| **meedan/fetch** | 2026-05-21 | ClaimReview aggregator, MIT |

Pattern worth carrying into planning: in this catalogue, the tools that died in 2024-2026 died
overwhelmingly because a **platform API or scraping path was withdrawn** (CrowdTangle, Google
search, Twitter), not because maintainers lost interest. Design collection layers so the data
source is replaceable without rewriting the analysis — CooRTweet versus CooRnet is the model.
