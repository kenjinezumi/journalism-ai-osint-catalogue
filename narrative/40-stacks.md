## Suggested stacks

### A. Small newsroom, little or no engineering capacity

The principle is that every component must work without a platform engineer, and the privacy
properties must hold by default rather than by configuration.

- **Receive and protect:** Hush Line (SUR-B3-06) (self-hosted) for tips · Dangerzone (SUR-B3-03) on every arriving
  document · mat2 (SUR-B3-07) before anything is published · Signal (SUR-B3-23) for source contact.
- **Documents:** ICIJ Datashare (JAI-A2-23) in desktop mode · OCRmyPDF (JAI-A2-33) for scans · Tabula (JAI-A2-53) or pdfplumber (JAI-A2-39) for
  tables (Tabula is frozen since 2018 — use it knowingly) · x-ray (JAI-A4-23) before publishing any PDF.
- **Audio:** Buzz (JAI-A2-05) on reporters' laptops; noScribe (JAI-A2-31) where speaker attribution matters.
- **Monitoring:** changedetection.io (SUR-B1-15) · FreshRSS (JAI-A1-03) · Klaxon Cloud (SUR-B1-19) if you cannot run a server at all.
- **Verification:** InVID-WeVerify plugin (JAI-A4-04) for public media only · Sherloq (OSINT-C2-12) locally for anything
  unpublished · MediaInfo (OSINT-C2-04) on every submitted video.
- **Publish:** DocumentCloud (JAI-A2-13) for documents · Datasette (JAI-A2-09) for data · Leaflet (JAI-A1-21) with self-hosted
  PMTiles (JAI-A1-24) for maps.
- **Deliberately excluded:** OpenAleph (JAI-A2-35), SecureDrop (SUR-B3-01), Browsertrix platform, Qubes. Each needs
  capacity this stack does not have, and a half-maintained SecureDrop is worse than none.
- **Indicative cost:** no licence fees; one small VM plus one shared GPU-less workstation.

### B. Engineering-led investigative team

- **Ingest:** Apache Tika (JAI-A2-02) (sandboxed) · openaleph/ingest-file (JAI-A2-25) or ICIJ extract (JAI-A2-24) · libpff (JAI-A1-12) for PST ·
  Docling (JAI-A2-12) for layout-aware parsing (licence-clean) · datasketch (JAI-A2-10) to deduplicate before anyone reads.
- **Platform:** OpenAleph with Elasticsearch · Datasette and DuckDB (JAI-A1-19) for tabular work · Solr (JAI-A2-01) or
  OpenSearch if you need a bespoke index.
- **Entity work:** rigour (JAI-A2-44) → RapidFuzz (JAI-A2-43) → Splink (JAI-A2-48) for linkage; nomenklatura (JAI-A2-30) and yente (JAI-A2-61) where
  FollowTheMoney fits; GLiNER (JAI-A2-19) (pin a v2.1 Apache-2.0 checkpoint) for investigation-specific types.
- **Local AI:** vLLM (JAI-A3-03) on the GPU host, llama.cpp (JAI-A3-01) and Ollama (JAI-A3-02) elsewhere, one OpenAI-compatible
  endpoint for everything · Haystack (JAI-A3-05) for RAG with evaluation · simonw/llm (JAI-A3-12) for the audit trail ·
  promptfoo (JAI-A3-14) to choose the model and test for prompt injection from hostile documents.
- **Capture and evidence:** browsertrix-crawler (OSINT-C1-29) · Scoop (OSINT-C1-36) for cited pages · warcio (OSINT-C1-41) validation on
  every capture · pywb (OSINT-C1-27) for replay · OpenTimestamps (OSINT-C3-41) on every received file at ingest.
- **OSINT:** SearXNG (OSINT-C1-01) · subfinder (OSINT-C3-23) → httpx (OSINT-C3-24) → asn (OSINT-C3-27) · certstream (SUR-B2-10) on a watchlist · NetworkX (OSINT-C3-31) and Gephi (OSINT-C3-33) ·
  QGIS (OSINT-C2-19), geopandas (OSINT-C2-21) and rasterio (OSINT-C2-22) · pystac (OSINT-C2-44) for free satellite imagery before paying for any.
- **Reproducibility:** Quarto (OSINT-C3-39) for published methodology · git-history (JAI-A1-32) over scraped data ·
  frictionless (OSINT-C3-40) for released datasets.
- **Indicative cost:** no licence fees for this stack; one GPU host plus an Elasticsearch cluster
  is the budget. The unpriced dependencies are satellite imagery (quote required) and
  OpenSanctions commercial data if your outlet is commercial.

### C. Team handling highly sensitive material (media in exile, hostile-state threat model)

Ordered by what protects people rather than by capability.

- **Devices and environments:** Qubes OS (SUR-B3-20) for those handling unsolicited material · Tails (SUR-B3-19) for
  sessions on untrusted machines · VeraCrypt (SUR-B3-22) for anything that travels · security-misc (SUR-B3-21) on servers.
- **Communications:** Signal (teach safety-number verification) · Molly (SUR-B3-24) on Android where seizure
  is the risk, checking the upstream version gap · SimpleX (SUR-B3-25) for identifier-free first contact ·
  Delta Chat (SUR-B3-26) over chatmail where messengers are blocked · Orbot (SUR-B3-30) and Outline (SUR-B3-31) for circumvention you
  operate.
- **Submission:** SecureDrop with the Qubes Workstation · OnionShare (SUR-B3-04) for ad-hoc transfer ·
  Hush Line as the honest fallback.
- **Document handling:** Dangerzone always · mat2 and PyMuPDF (JAI-A2-42) true redaction before release ·
  x-ray to verify the redaction worked · kuroi (JAI-A4-24) only against a self-hosted model.
- **Device examination:** MVT (SUR-B3-08) and androidqf (SUR-B3-09) with a **written consent script and a disclosed
  retention policy** — the MVT License 1.1 §3.0 makes that contractual, not optional ·
  stalkerware-indicators (SUR-B3-10) and Amnesty IOCs (check securitylab.amnesty.org, the GitHub mirror has
  not been pushed since December 2024) · SpyGuard (SUR-B3-12) for non-invasive screening · Rayhunter (SUR-B3-13) for
  cell-site simulators.
- **Collaboration:** CryptPad (SUR-B3-27) for documents · Nextcloud (SUR-B3-28) for files, understanding that server-side
  encryption does not protect against the server · Tella (OSINT-C3-06) for field documentation.
- **AI:** local only, no exceptions. llama.cpp or Ollama, never a hosted API, and audit the
  simonw/llm log store because it holds full document content.
- **Rules that matter more than tools:** never use the InVID plugin on unpublished media (it
  uploads) · never run `datasette publish` on source-derived data · never create a Perma link
  during an investigation (it publishes the URL and date) · never request an ArchiveBot crawl of
  a target (the request is public IRC).
