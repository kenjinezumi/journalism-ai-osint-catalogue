# Evidence records

## `recovered/` — session 1 artefacts, UNMODIFIED
48 files copied verbatim from `/private/tmp/claude-501/-Users-ktsuchiya/abac6511-.../scratchpad`
on 2026-11-17. Do not edit. Of particular value:
- `cat/A2.jsonl`, `cat/A4.jsonl`, `cat/B1.jsonl`, `cat/C1.jsonl`, `cat/C2.jsonl` — the 185-record
  (184 unique) recovered inventory, with dated GitHub-API activity evidence inside each record.
- `cat/ground_truth.tsv` — 15 hand-verified repos (licence, archive status, release).
- `cat/pricing.tsv` — 23 verified vendor price line items, verification_date 2026-11-16.
- `cat/RUBRIC.md` — the scoring rubric, adopted unchanged in session 2.
- `cat/mvt.txt` — full MVT License 1.1 text (evidence for lead L1).
- `cat/consolidate.py` — dedupe script with session 1's RENAMES and FORKS maps.
- `a1disc/notes.md` — resolved licences for 30 NOASSERTION repos plus 11 with none found.
- `urls.txt`, `u2.txt` — candidate source URLs, all verified in `evidence/b2-sources.md`.

## `evidence/` — this session's own records
- `leads.md` — the nine preserved research leads resolved with primary evidence (L1-L8), plus
  two new lead groups found this session: L9 SuperGlue noncommercial licence and six more
  NOASSERTION resolutions; L10 two transfers and seven archivals.
- `pricing.md` — inherited verified prices, the re-confirmed Sentinel Hub/Planet "not publicly
  listed" finding, and an explicit list of prices deliberately NOT asserted.
- `b2-sources.md` — URL verification for every session-1 candidate source URL: 4 genuine 404s
  with corrections, 2 bot-blocks recorded as live-but-unverified, 1 unresolved (EU Transparency
  Register).
- `licences/` — licence blobs read directly from repositories, saved as `*.LICENSE.txt` with the
  GitHub API response as `*.license.json`. Covers OnionShare, Tracker Radar, MVT, androidqf,
  timemap, mtriage, warn-scraper, OpenSanctions, SuperGlue, GDAL, rasterio, maplibre-gl-js,
  PMTiles, pystac, dump1090, rtl-ais, overpass-turbo.

## `../work/` — working data
- `meta.jsonl` — this session's GitHub metadata sweep over 583 candidate repos (2026-11-17):
  full_name, rename flag, SPDX, archived, pushed_at, release, tag, stars, open issues, fork
  parent. The primary maintenance evidence for most entries.
- `candidates.txt`, `sweep.py`, `probe.py`, `show.py`, `join.py`, `dump_*.txt` — the sweep and
  join tooling plus per-segment joined views used while authoring records.
- `inventory.json` — the consolidated recovered inventory (185 rows, 184 unique after the
  ThreatExchange correction).
