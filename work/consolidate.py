#!/usr/bin/env python3
"""Consolidate pillar-agent JSONL into one deduplicated inventory with stable IDs."""
import json, glob, re, sys, os

# Verified renames/transfers (old -> canonical). Old URL REDIRECTS, so not "broken".
RENAMES = {
 "github.com/guillaumekln/faster-whisper":"github.com/systran/faster-whisper",
 "github.com/vikparuchuri/marker":"github.com/datalab-to/marker",
 "github.com/vikparuchuri/surya":"github.com/datalab-to/surya",
 "github.com/ukplab/sentence-transformers":"github.com/huggingface/sentence-transformers",
 "github.com/iterative/dvc":"github.com/treeverse/dvc",
 "github.com/microsoft/presidio":"github.com/data-privacy-stack/presidio",
 "github.com/deltachat/deltachat-core-rust":"github.com/chatmail/core",
 "github.com/nvidia/nemo":"github.com/nvidia-nemo/speech",
 "github.com/alephdata/fingerprints":"github.com/opensanctions/fingerprints",
 "github.com/micahflee/torbrowser-launcher":"github.com/torproject/torbrowser-launcher",
 "github.com/tails-project/tails":"gitlab.tails.boum.org/tails/tails",
}
# Independent FORKS - deliberately kept as SEPARATE entries, cross-referenced not merged.
FORKS = {
 "github.com/openaleph/openaleph":"independent fork of github.com/alephdata/aleph",
 "github.com/camelot-dev/camelot":"community fork of archived github.com/atlanhq/camelot",
 "github.com/openaleph/ingest-file":"maintained fork of archived github.com/alephdata/ingest-file",
 "github.com/enthec/webappanalyzer":"community continuation of discontinued Wappalyzer OSS",
}
PILLAR = {"A1":"JAI","A2":"JAI","A3":"JAI","A4":"JAI","B1":"SUR","B2":"SUR","B3":"SUR",
          "C1":"OSINT","C2":"OSINT","C3":"OSINT"}

def canon(u):
    if not u: return ""
    u = u.strip().rstrip("/")
    u = re.sub(r"^https?://", "", u, flags=re.I)
    u = re.sub(r"^www\.", "", u, flags=re.I)
    u = re.sub(r"\.git$", "", u, flags=re.I)
    u = u.lower()
    # strip github deep paths to repo root
    m = re.match(r"(github\.com/[^/]+/[^/]+)", u)
    if m: u = m.group(1)
    m = re.match(r"(gitlab\.com/[^/]+/[^/]+)", u)
    if m: u = m.group(1)
    return RENAMES.get(u, u)

rows, dupes = {}, []
for path in sorted(glob.glob("[ABC][0-9].jsonl")):
    seg = os.path.basename(path)[:2]
    n = 0
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line.startswith("{"): continue
        try: d = json.loads(line)
        except Exception: continue
        n += 1
        key = canon(d.get("repo_url","")) or ("name::" + (d.get("name","") or "").strip().lower())
        d["_segment"] = seg
        d["_canonical"] = key
        if key in rows:
            prev = rows[key]
            dupes.append((key, prev["_segment"], seg, d.get("name")))
            # merge: keep richer record, union tags, record cross-pillar membership
            prev.setdefault("_also_in", [])
            if seg not in prev["_also_in"] and seg != prev["_segment"]:
                prev["_also_in"].append(seg)
            for t in (d.get("tags") or []):
                prev.setdefault("tags", [])
                if t not in prev["tags"]: prev["tags"].append(t)
            # prefer a verified licence over 'not verified'
            if str(prev.get("licence","")).lower().startswith("not verified") and d.get("licence"):
                prev["licence"] = d["licence"]; prev["licence_evidence_url"] = d.get("licence_evidence_url","")
            if len(str(d.get("journalism_use_case",""))) > len(str(prev.get("journalism_use_case",""))):
                prev["journalism_use_case"] = d["journalism_use_case"]
        else:
            rows[key] = d
    print(f"{path}: {n} rows read", file=sys.stderr)

# stable IDs per pillar
counters = {}
out = []
for key, d in sorted(rows.items(), key=lambda kv: (kv[1]["_segment"], (kv[1].get("name") or "").lower())):
    p = PILLAR.get(d["_segment"], "MISC")
    counters[p] = counters.get(p, 0) + 1
    d["id"] = f"{p}-{counters[p]:03d}"
    if key in FORKS: d["fork_note"] = FORKS[key]
    out.append(d)

json.dump(out, open("inventory.json","w"), indent=1, ensure_ascii=False)
print(f"\nUNIQUE PROJECTS: {len(out)}")
print(f"DUPLICATE/CROSS-PILLAR MERGES: {len(dupes)}")
for k,a,b,n in dupes: print(f"  merged {n} ({a} + {b})")
from collections import Counter
print("\nBy segment:", dict(Counter(d["_segment"] for d in out)))
print("By bucket:", dict(Counter(d.get("bucket","?") for d in out)))
