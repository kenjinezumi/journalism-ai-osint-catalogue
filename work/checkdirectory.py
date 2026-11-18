#!/usr/bin/env python3
"""Validate the generated directory against the canonical records.

Checks that the README directory, the per-project pages, catalogue.csv,
catalogue.json and docs/directory.json all describe the same 361 projects with
the same licence, open-source status and cost classifications, and that no row
leaves any of those three questions blank.

Run from the repository root:  python3 work/checkdirectory.py
Exits 1 on any problem.
"""
import collections
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

fail = []


def check(name, ok, detail=""):
    print(("  OK   " if ok else "  FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not ok:
        fail.append(name)


cat = json.load(open("catalogue.json", encoding="utf-8"))
projects = cat["projects"]
dirj = json.load(open("docs/directory.json", encoding="utf-8"))
readme = open("README.md", encoding="utf-8").read()
ids = [p["id"] for p in projects]
n = len(ids)

rows = re.search(r"<!-- DIRECTORY_TABLE_START -->(.*?)<!-- DIRECTORY_TABLE_END -->",
                 readme, re.S).group(1).strip().split("\n")[2:]
cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]

print(f"1. exactly {n} unique project IDs")
check(f"catalogue.json has {n} projects", n == 361, str(n))
check("all IDs unique", len(set(ids)) == n)
check("directory.json lists the same IDs in the same order",
      [p["id"] for p in dirj["projects"]] == ids)
check(f"README directory has {n} rows", len(rows) == n, str(len(rows)))
tbl_ids = [re.search(r"`((?:JAI|SUR|OSINT)-[ABC][1-4]-\d\d)`", r).group(1) for r in rows]
check("README directory IDs match the ranking exactly", tbl_ids == ids)

print("\n2. every entry links to its own assessment")
check("each row links to its own project page",
      all(f"docs/projects/{i}.md" in r for i, r in zip(ids, rows)))
check("every linked page exists on disk",
      all(os.path.exists(f"docs/projects/{i}.md") for i in ids))
check(f"{n} project pages on disk",
      len([f for f in os.listdir("docs/projects") if f.endswith(".md")]) == n)

print("\n3. licence, open-source status and cost explicit on every row")
check("every row has 9 columns", all(len(c) == 9 for c in cells),
      str(sorted({len(c) for c in cells})))
for i, col in ((4, "licence"), (5, "open-source status"), (6, "software price"),
               (7, "additional costs"), (8, "maintenance")):
    check(f"no empty {col} cell", all(c[i] for c in cells))
VOC = {"Open source", "Source available", "Mixed", "Proprietary", "Unverified"}
check("every status drawn from the controlled vocabulary",
      all(c[5] in VOC for c in cells),
      str(dict(collections.Counter(c[5] for c in cells))))
unk = [c for c in cells if "Unknown / not verified" in c[6]]
check("unverified prices carry the explicit label",
      len(unk) == cat["meta"]["price_unknown"], str(len(unk)))

print("\n4. mandatory and optional costs are distinguishable")
mand = [c for c in cells if c[7].startswith("**Mandatory paid dependency**")]
check("mandatory paid dependencies marked in bold",
      len(mand) == cat["meta"]["mandatory_paid"], str(len(mand)))
check("no optional cost borrows the mandatory wording",
      all("Mandatory paid" not in c[7]
          for c in cells if not c[7].startswith("**Mandatory")))
check("every mandatory row also carries the flag in the records",
      {re.search(r"`((?:JAI|SUR|OSINT)-[ABC][1-4]-\d\d)`", "|".join(c)).group(1)
       for c in mand}
      == {p["id"] for p in projects if "mandatory-paid" in (p.get("cost_flags") or [])})

print("\n5. the exports describe the same records")
csvr = list(csv.DictReader(open("catalogue.csv", encoding="utf-8")))
check(f"CSV has {n} rows", len(csvr) == n, str(len(csvr)))
check("CSV IDs match the ranking", [r["id"] for r in csvr] == ids)
check("CSV carries the licence and cost columns",
      all(k in csvr[0] for k in ("licence_type", "oss_status", "price_class", "cost_flags",
                                 "software_price_note", "additional_costs_note")))
mism = [p["id"] for p, q in zip(projects, dirj["projects"])
        if (p["licence_type"], p["oss_status"], p["price_class"], p["maintenance_status"])
        != (q["licence_type"], q["oss_status"], q["price_class"], q["maintenance_status"])]
check("directory.json agrees with catalogue.json on every classification",
      not mism, str(mism[:3]))
cmism = [r["id"] for r, p in zip(csvr, projects)
         if r["licence_type"] != p["licence_type"] or r["price_class"] != p["price_class"]]
check("catalogue.csv agrees with catalogue.json", not cmism, str(cmism[:3]))

print("\n6. the front page presents the whole set")
check(f"counter states {n} of {n}", f"Showing {n} of {n} projects" in readme)
check("top-20 kept as its own section", "## The 20 projects to examine first" in readme)
check("legend for the licence and cost labels present",
      "How to read the licence and cost columns" in readme)
check("build reported zero validation errors",
      cat["meta"]["validation_errors_count"] == 0)

print("\nRESULT: " + ("ALL CHECKS PASSED" if not fail else f"{len(fail)} FAILED: {fail}"))
sys.exit(1 if fail else 0)
