[← Catalogue home](../README.md) · [All rankings](rankings.md) · [Methodology](methodology.md) · [Findings](findings-and-limitations.md)

# Suggested stacks

### A. Small newsroom, little or no engineering capacity

The principle is that every component must work without a platform engineer, and the privacy
properties must hold by default rather than by configuration.

- **Receive and protect:** Hush Line ([SUR-B3-06](projects/SUR-B3-06.md)) (self-hosted) for tips · Dangerzone ([SUR-B3-03](projects/SUR-B3-03.md)) on every arriving
  document · mat2 ([SUR-B3-07](projects/SUR-B3-07.md)) before anything is published · Signal ([SUR-B3-23](projects/SUR-B3-23.md)) for source contact.
- **Documents:** ICIJ Datashare ([JAI-A2-23](projects/JAI-A2-23.md)) in desktop mode · OCRmyPDF ([JAI-A2-33](projects/JAI-A2-33.md)) for scans · Tabula ([JAI-A2-53](projects/JAI-A2-53.md)) or pdfplumber ([JAI-A2-39](projects/JAI-A2-39.md)) for
  tables (Tabula is frozen since 2018 — use it knowingly) · x-ray ([JAI-A4-23](projects/JAI-A4-23.md)) before publishing any PDF.
- **Audio:** Buzz ([JAI-A2-05](projects/JAI-A2-05.md)) on reporters' laptops; noScribe ([JAI-A2-31](projects/JAI-A2-31.md)) where speaker attribution matters.
- **Monitoring:** changedetection.io ([SUR-B1-15](projects/SUR-B1-15.md)) · FreshRSS ([JAI-A1-03](projects/JAI-A1-03.md)) · Klaxon Cloud ([SUR-B1-19](projects/SUR-B1-19.md)) if you cannot run a server at all.
- **Verification:** InVID-WeVerify plugin ([JAI-A4-04](projects/JAI-A4-04.md)) for public media only · Sherloq ([OSINT-C2-12](projects/OSINT-C2-12.md)) locally for anything
  unpublished · MediaInfo ([OSINT-C2-04](projects/OSINT-C2-04.md)) on every submitted video.
- **Publish:** DocumentCloud ([JAI-A2-13](projects/JAI-A2-13.md)) for documents · Datasette ([JAI-A2-09](projects/JAI-A2-09.md)) for data · Leaflet ([JAI-A1-21](projects/JAI-A1-21.md)) with self-hosted
  PMTiles ([JAI-A1-24](projects/JAI-A1-24.md)) for maps.
- **Deliberately excluded:** OpenAleph ([JAI-A2-35](projects/JAI-A2-35.md)), SecureDrop ([SUR-B3-01](projects/SUR-B3-01.md)), Browsertrix platform, Qubes. Each needs
  capacity this stack does not have, and a half-maintained SecureDrop is worse than none.
- **Indicative cost:** no licence fees; one small VM plus one shared GPU-less workstation.

### B. Engineering-led investigative team

- **Ingest:** Apache Tika ([JAI-A2-02](projects/JAI-A2-02.md)) (sandboxed) · openaleph/ingest-file ([JAI-A2-25](projects/JAI-A2-25.md)) or ICIJ extract ([JAI-A2-24](projects/JAI-A2-24.md)) · libpff ([JAI-A1-12](projects/JAI-A1-12.md)) for PST ·
  Docling ([JAI-A2-12](projects/JAI-A2-12.md)) for layout-aware parsing (licence-clean) · datasketch ([JAI-A2-10](projects/JAI-A2-10.md)) to deduplicate before anyone reads.
- **Platform:** OpenAleph with Elasticsearch · Datasette and DuckDB ([JAI-A1-19](projects/JAI-A1-19.md)) for tabular work · Solr ([JAI-A2-01](projects/JAI-A2-01.md)) or
  OpenSearch if you need a bespoke index.
- **Entity work:** rigour ([JAI-A2-44](projects/JAI-A2-44.md)) → RapidFuzz ([JAI-A2-43](projects/JAI-A2-43.md)) → Splink ([JAI-A2-48](projects/JAI-A2-48.md)) for linkage; nomenklatura ([JAI-A2-30](projects/JAI-A2-30.md)) and yente ([JAI-A2-61](projects/JAI-A2-61.md)) where
  FollowTheMoney fits; GLiNER ([JAI-A2-19](projects/JAI-A2-19.md)) (pin a v2.1 Apache-2.0 checkpoint) for investigation-specific types.
- **Local AI:** vLLM ([JAI-A3-03](projects/JAI-A3-03.md)) on the GPU host, llama.cpp ([JAI-A3-01](projects/JAI-A3-01.md)) and Ollama ([JAI-A3-02](projects/JAI-A3-02.md)) elsewhere, one OpenAI-compatible
  endpoint for everything · Haystack ([JAI-A3-05](projects/JAI-A3-05.md)) for RAG with evaluation · simonw/llm ([JAI-A3-12](projects/JAI-A3-12.md)) for the audit trail ·
  promptfoo ([JAI-A3-14](projects/JAI-A3-14.md)) to choose the model and test for prompt injection from hostile documents.
- **Capture and evidence:** browsertrix-crawler ([OSINT-C1-29](projects/OSINT-C1-29.md)) · Scoop ([OSINT-C1-36](projects/OSINT-C1-36.md)) for cited pages · warcio ([OSINT-C1-41](projects/OSINT-C1-41.md)) validation on
  every capture · pywb ([OSINT-C1-27](projects/OSINT-C1-27.md)) for replay · OpenTimestamps ([OSINT-C3-41](projects/OSINT-C3-41.md)) on every received file at ingest.
- **OSINT:** SearXNG ([OSINT-C1-01](projects/OSINT-C1-01.md)) · subfinder ([OSINT-C3-23](projects/OSINT-C3-23.md)) → httpx ([OSINT-C3-24](projects/OSINT-C3-24.md)) → asn ([OSINT-C3-27](projects/OSINT-C3-27.md)) · certstream ([SUR-B2-10](projects/SUR-B2-10.md)) on a watchlist · NetworkX ([OSINT-C3-31](projects/OSINT-C3-31.md)) and Gephi ([OSINT-C3-33](projects/OSINT-C3-33.md)) ·
  QGIS ([OSINT-C2-19](projects/OSINT-C2-19.md)), geopandas ([OSINT-C2-21](projects/OSINT-C2-21.md)) and rasterio ([OSINT-C2-22](projects/OSINT-C2-22.md)) · pystac ([OSINT-C2-44](projects/OSINT-C2-44.md)) for free satellite imagery before paying for any.
- **Reproducibility:** Quarto ([OSINT-C3-39](projects/OSINT-C3-39.md)) for published methodology · git-history ([JAI-A1-32](projects/JAI-A1-32.md)) over scraped data ·
  frictionless ([OSINT-C3-40](projects/OSINT-C3-40.md)) for released datasets.
- **Indicative cost:** no licence fees for this stack; one GPU host plus an Elasticsearch cluster
  is the budget. The unpriced dependencies are satellite imagery (quote required) and
  OpenSanctions commercial data if your outlet is commercial.

### C. Team handling highly sensitive material (media in exile, hostile-state threat model)

Ordered by what protects people rather than by capability.

- **Devices and environments:** Qubes OS ([SUR-B3-20](projects/SUR-B3-20.md)) for those handling unsolicited material · Tails ([SUR-B3-19](projects/SUR-B3-19.md)) for
  sessions on untrusted machines · VeraCrypt ([SUR-B3-22](projects/SUR-B3-22.md)) for anything that travels · security-misc ([SUR-B3-21](projects/SUR-B3-21.md)) on servers.
- **Communications:** Signal (teach safety-number verification) · Molly ([SUR-B3-24](projects/SUR-B3-24.md)) on Android where seizure
  is the risk, checking the upstream version gap · SimpleX ([SUR-B3-25](projects/SUR-B3-25.md)) for identifier-free first contact ·
  Delta Chat ([SUR-B3-26](projects/SUR-B3-26.md)) over chatmail where messengers are blocked · Orbot ([SUR-B3-30](projects/SUR-B3-30.md)) and Outline ([SUR-B3-31](projects/SUR-B3-31.md)) for circumvention you
  operate.
- **Submission:** SecureDrop with the Qubes Workstation · OnionShare ([SUR-B3-04](projects/SUR-B3-04.md)) for ad-hoc transfer ·
  Hush Line as the honest fallback.
- **Document handling:** Dangerzone always · mat2 and PyMuPDF ([JAI-A2-42](projects/JAI-A2-42.md)) true redaction before release ·
  x-ray to verify the redaction worked · kuroi ([JAI-A4-24](projects/JAI-A4-24.md)) only against a self-hosted model.
- **Device examination:** MVT ([SUR-B3-08](projects/SUR-B3-08.md)) and androidqf ([SUR-B3-09](projects/SUR-B3-09.md)) with a **written consent script and a disclosed
  retention policy** — the MVT License 1.1 §3.0 makes that contractual, not optional ·
  stalkerware-indicators ([SUR-B3-10](projects/SUR-B3-10.md)) and Amnesty IOCs (check securitylab.amnesty.org, the GitHub mirror has
  not been pushed since December 2024) · SpyGuard ([SUR-B3-12](projects/SUR-B3-12.md)) for non-invasive screening · Rayhunter ([SUR-B3-13](projects/SUR-B3-13.md)) for
  cell-site simulators.
- **Collaboration:** CryptPad ([SUR-B3-27](projects/SUR-B3-27.md)) for documents · Nextcloud ([SUR-B3-28](projects/SUR-B3-28.md)) for files, understanding that server-side
  encryption does not protect against the server · Tella ([OSINT-C3-06](projects/OSINT-C3-06.md)) for field documentation.
- **AI:** local only, no exceptions. llama.cpp or Ollama, never a hosted API, and audit the
  simonw/llm log store because it holds full document content.
- **Rules that matter more than tools:** never use the InVID plugin on unpublished media (it
  uploads) · never run `datasette publish` on source-derived data · never create a Perma link
  during an investigation (it publishes the URL and date) · never request an ArchiveBot crawl of
  a target (the request is public IRC).

---

Every project named above has a full assessment under [`docs/projects/`](projects/), reachable from the [complete ranking](rankings.md).
