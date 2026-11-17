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
