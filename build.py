#!/usr/bin/env python3
"""Generate every published artefact from the canonical records.

Single source of truth:
  records/*.json      hand-authored project records (one object per project)
  narrative/*.md      hand-authored prose fragments

Generated (never hand-edit these):
  catalogue.json      complete structured export
  catalogue.csv       complete tabular export
  report.md           complete consolidated report
  README.md           repository front page
  docs/*.md           browsable pages
  docs/projects/*.md  one page per project, keyed by stable project ID

Run:  python3 build.py
"""
import json, glob, csv, os, re, shutil
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
PROJ = os.path.join(DOCS, "projects")

W = {"relevance": 30, "capability": 20, "maintenance": 15,
     "privacy": 15, "usability": 10, "licence_cost": 10}

PILLAR_NAME = {
    "JAI": "Journalism and AI",
    "SUR": "Surveillance and journalist protection",
    "OSINT": "OSINT and digital investigations",
}
PILLAR_PAGE = {"JAI": "journalism-ai.md", "SUR": "surveillance.md", "OSINT": "osint.md"}
PILLAR_ORDER = ["JAI", "SUR", "OSINT"]

SEGMENT_NAME = {
    "A1": "A1 · Discovery, scraping, ingestion, data journalism and newsroom workflow",
    "A2": "A2 · Documents and language: OCR, transcription, translation, entities, entity resolution",
    "A3": "A3 · RAG, research agents, knowledge graphs, provenance and AI evaluation",
    "A4": "A4 · Fact-checking support and media verification",
    "B1": "B1 · Monitoring public information, narratives, disinformation, censorship and harassment",
    "B2": "B2 · Investigating surveillance companies, infrastructure, procurement and tracking tech",
    "B3": "B3 · Protecting journalists and sources",
    "C1": "C1 · Web and social research, archives and evidence capture",
    "C2": "C2 · Image/video verification, geolocation, satellite, aviation and maritime",
    "C3": "C3 · Public records, corporate ownership, finance, infrastructure, link analysis, collaboration",
}
SEG_ORDER = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "C1", "C2", "C3"]
SEG_OF_PILLAR = {"JAI": ["A1", "A2", "A3", "A4"], "SUR": ["B1", "B2", "B3"],
                 "OSINT": ["C1", "C2", "C3"]}

REQ = ["id", "name", "pillar", "segment", "subcategory", "project_type", "bucket", "purpose",
       "journalism_use_case", "audience", "pros", "cons", "feedback", "assessment",
       "maintenance_status", "maintenance_evidence", "licence", "costs", "privacy", "verdict",
       "evidence_urls", "verification_date", "confidence", "depth", "scores"]
VERDICTS = {"Adopt", "Pilot", "Integrate", "Monitor", "Reference only",
            "Avoid for new deployment"}
MSTATUS = {"Actively maintained", "Stable with low activity",
           "Maintenance appears to be declining", "Dormant",
           "Archived or discontinued", "Uncertain"}
VERDICT_ORDER = ["Adopt", "Integrate", "Pilot", "Monitor", "Reference only",
                 "Avoid for new deployment"]
MSTATUS_ORDER = ["Actively maintained", "Stable with low activity",
                 "Maintenance appears to be declining", "Dormant",
                 "Archived or discontinued", "Uncertain"]

ID_RE = re.compile(r"\b(?:JAI|SUR|OSINT)-[ABC][1-4]-\d{2}\b")


# ---------------------------------------------------------------- load + rank

def load():
    items, errs, seen = [], [], {}
    for p in sorted(glob.glob(os.path.join(ROOT, "records", "*.json"))):
        try:
            data = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            errs.append(f"{os.path.basename(p)}: UNPARSEABLE {e}")
            continue
        for d in data:
            pid = d.get("id", "<no id>")
            for f in REQ:
                if f not in d or d[f] in (None, "", [], {}):
                    errs.append(f"{pid}: missing {f}")
            if d.get("verdict") not in VERDICTS:
                errs.append(f"{pid}: bad verdict {d.get('verdict')!r}")
            if d.get("maintenance_status") not in MSTATUS:
                errs.append(f"{pid}: bad maintenance_status {d.get('maintenance_status')!r}")
            s = d.get("scores") or {}
            for k in W:
                v = s.get(k)
                if not isinstance(v, (int, float)) or not (0 <= v <= 5):
                    errs.append(f"{pid}: bad score {k}={v!r}")
            if pid in seen:
                errs.append(f"DUPLICATE id {pid} ({os.path.basename(p)} and {seen[pid]})")
            seen[pid] = os.path.basename(p)
            d["_file"] = os.path.basename(p)
            items.append(d)
    return items, errs


def total(d):
    s = d["scores"]
    return round(sum(s[k] / 5 * W[k] for k in W))


# ------------------------------------------------------------------ markdown

def md_esc(x):
    return str(x).replace("|", "\\|").replace("\n", " ")


def bullets(items):
    if not items:
        return "_none recorded_"
    return "\n".join(f"- {i}" for i in items)


PREFIX = {"root": "docs/projects/", "docs": "projects/", "proj": ""}


PROTECT_RE = re.compile(r"(\[[^\]]*\]\([^)]*\)|`[^`]*`)")


def linkify(text, ctx, byid):
    """Turn bare project IDs in prose into links to the project page.

    Existing markdown links and inline code spans are protected, so an ID that is
    already part of a link target or shown as literal code is left untouched.
    """
    pre = PREFIX[ctx]

    def rep(m):
        pid = m.group(0)
        return f"[{pid}]({pre}{pid}.md)" if pid in byid else pid

    parts = PROTECT_RE.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = ID_RE.sub(rep, parts[i])
    return "".join(parts)


def link_project(d, ctx):
    return f"[{md_esc(d['name'])}]({PREFIX[ctx]}{d['id']}.md)"


def frag(name):
    p = os.path.join(ROOT, "narrative", name)
    return open(p, encoding="utf-8").read().rstrip() if os.path.exists(p) else ""


def alt_bullets(d, ctx, byname):
    """Render the alternatives list, linking a leading project name where it matches."""
    out = []
    for a in d.get("alternatives", []) or []:
        txt = str(a)
        hit = None
        for nm in byname:
            if txt.startswith(nm) and (len(txt) == len(nm) or not txt[len(nm)].isalnum()):
                if hit is None or len(nm) > len(hit):
                    hit = nm
        if hit:
            o = byname[hit]
            txt = f"[{md_esc(hit)}]({PREFIX[ctx]}{o['id']}.md)" + txt[len(hit):]
        out.append(f"- {txt}")
    return "\n".join(out) if out else "_none recorded_"


def score_line(d):
    s = d["scores"]
    return (f"relevance {s['relevance']}/5 · capability {s['capability']}/5 · "
            f"maintenance {s['maintenance']}/5 · privacy {s['privacy']}/5 · "
            f"usability {s['usability']}/5 · licence+cost {s['licence_cost']}/5 → "
            f"**weighted {d['weighted_total']}/100**")


def card_body(d, ctx, byname, heading_level=2):
    """The fourteen assessment fields. Shared by report.md and the per-project pages."""
    h = "#" * heading_level
    o = []
    o.append(f"{h} 1. Purpose\n\n{d['purpose']}")
    o.append(f"\n{h} Journalism / investigative use case\n\n{d['journalism_use_case']}")
    o.append(f"\n{h} 2. Audience\n\n{', '.join(d['audience'])}")
    o.append(f"\n{h} 3. Project type\n\n{d['project_type']} · bucket `{d['bucket']}`")
    o.append(f"\n{h} 4. Pros\n\n{bullets(d['pros'])}")
    o.append(f"\n{h} 5. Cons\n\n{bullets(d['cons'])}")
    o.append(f"\n{h} 6. Feedback (documented)\n\n{d['feedback']}")
    o.append(f"\n{h} 7. Assessment\n\n{d['assessment']}")
    o.append(f"\n{h} 8. Maintenance\n\n**{d['maintenance_status']}** — {d['maintenance_evidence']}")
    lic = [f"**Licence:** {d['licence']}" +
           (" _(SPDX verified)_" if d.get("licence_spdx_verified")
            else " _(SPDX not verified — resolved from the licence file or project documentation)_")]
    if d.get("model_or_data_licence"):
        lic.append(f"**Model / data licence:** {d['model_or_data_licence']}")
    if d.get("licence_restrictions"):
        lic.append(f"**Restrictions:** {d['licence_restrictions']}")
    if d.get("licence_evidence_url"):
        u = d["licence_evidence_url"]
        lic.append(f"**Licence evidence:** {u if u.startswith('http') else f'`{u}`'}")
    o.append(f"\n{h} 9. Licensing\n\n" + "\n\n".join(lic))
    o.append(f"\n{h} 10. Costs\n\n{d['costs']}")
    o.append(f"\n{h} 11. Privacy and data flows\n\n{d['privacy']}")
    o.append(f"\n{h} 12. Verdict\n\n**{d['verdict']}**")
    if d.get("blockers"):
        o.append(f"\n{h} Material blockers\n\n_Tracked separately from the score._\n\n{bullets(d['blockers'])}")
    o.append(f"\n{h} 13. Alternatives\n\n{alt_bullets(d, ctx, byname)}")
    ev = [f"- {e}" if str(e).startswith("http") else f"- `{e}`" for e in d["evidence_urls"]]
    o.append(f"\n{h} 14. Evidence\n\n"
             f"Verified **{d['verification_date']}** · confidence **{d['confidence']}** · "
             f"assessment depth `{d['depth']}`"
             + ("\n\n_Marked provisional: the evidence does not support a firm score._" if d.get("provisional") else "")
             + "\n\n" + ("\n".join(ev) if ev else "_none recorded_"))
    return "\n".join(o)


# ----------------------------------------------------------------- doc pages

def write_project_pages(order, byid, byname):
    os.makedirs(PROJ, exist_ok=True)
    for old in glob.glob(os.path.join(PROJ, "*.md")):
        os.remove(old)
    by_rank = {d["rank_overall"]: d for d in order}
    for d in order:
        ctx = "proj"
        o = []
        o.append(f"# {d['name']}")
        o.append(f"\n`{d['id']}` · **{d['weighted_total']}/100** · overall rank "
                 f"{d['rank_overall']} of {len(order)} · verdict **{d['verdict']}**")
        o.append(f"\n[← Catalogue home](../../README.md) · "
                 f"[All rankings](../rankings.md) · "
                 f"[{PILLAR_NAME[d['pillar']]}](../{PILLAR_PAGE[d['pillar']]}) · "
                 f"[Methodology](../methodology.md)")
        o.append("\n| | |\n|---|---|")
        o.append(f"| **Pillar** | {PILLAR_NAME[d['pillar']]} (rank {d['rank_pillar']}) |")
        o.append(f"| **Segment** | {SEGMENT_NAME[d['segment']]} (rank {d['rank_segment']}) |")
        o.append(f"| **Subcategory** | {md_esc(d.get('subcategory', ''))} |")
        o.append(f"| **Type** | {d['project_type']} |")
        o.append(f"| **Bucket** | `{d['bucket']}` |")
        o.append(f"| **Maintainer** | {md_esc(d.get('maintainer', 'not recorded'))} |")
        o.append(f"| **Maintenance** | {d['maintenance_status']} |")
        o.append(f"| **Licence** | {md_esc(d['licence'])} |")
        o.append(f"| **Confidence** | {d['confidence']}"
                 + (" · **provisional**" if d.get("provisional") else "") + " |")
        o.append(f"| **Verified** | {d['verification_date']} |")
        links = []
        if d.get("repo_url"):
            links.append(f"[Repository]({d['repo_url']})")
        if d.get("docs_url"):
            links.append(f"[Documentation]({d['docs_url']})")
        if links:
            o.append(f"| **Links** | {' · '.join(links)} |")
        if d.get("aka"):
            o.append(f"| **Also known as** | {md_esc(d['aka'])} |")
        o.append(f"\n**Scores** — {score_line(d)}")
        if d.get("blockers"):
            o.append("\n> **Material blockers recorded.** See [section 12](#material-blockers).")
        o.append("\n---\n")
        o.append(linkify(card_body(d, ctx, byname), ctx, byid))
        same = [x for x in order if x["segment"] == d["segment"] and x["id"] != d["id"]][:8]
        if same:
            o.append("\n---\n\n## Related in this segment\n")
            o.append("| # | Project | Total | Verdict |\n|--:|---|--:|---|")
            for x in same:
                o.append(f"| {x['rank_segment']} | {link_project(x, ctx)} | "
                         f"{x['weighted_total']} | {x['verdict']} |")
        nav = []
        prev_, next_ = by_rank.get(d["rank_overall"] - 1), by_rank.get(d["rank_overall"] + 1)
        if prev_:
            nav.append(f"← {prev_['rank_overall']}. {link_project(prev_, ctx)}")
        if next_:
            nav.append(f"{next_['rank_overall']}. {link_project(next_, ctx)} →")
        if nav:
            o.append("\n---\n\n" + " · ".join(nav))
        with open(os.path.join(PROJ, f"{d['id']}.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(o) + "\n")
    return len(order)


def master_table(order, ctx, head=None):
    rows = order if head is None else order[:head]
    o = ["| # | Project | ID | Seg | Total | Rel | Cap | Mnt | Priv | Use | Lic | Verdict | Maintenance | Conf |",
         "|--:|---|---|---|--:|--:|--:|--:|--:|--:|--:|---|---|---|"]
    for d in rows:
        s = d["scores"]
        o.append(f"| {d['rank_overall']} | {link_project(d, ctx)} | `{d['id']}` | {d['segment']} | "
                 f"**{d['weighted_total']}** | {s['relevance']} | {s['capability']} | "
                 f"{s['maintenance']} | {s['privacy']} | {s['usability']} | {s['licence_cost']} | "
                 f"{d['verdict']} | {d['maintenance_status']} | {d['confidence']}"
                 + ("·P" if d.get("provisional") else "") + " |")
    return "\n".join(o)


def seg_table(rows, ctx):
    o = ["| Seg # | Overall # | Project | Subcategory | Total | Verdict | Maintenance | Licence |",
         "|--:|--:|---|---|--:|---|---|---|"]
    for d in rows:
        o.append(f"| {d['rank_segment']} | {d['rank_overall']} | {link_project(d, ctx)} | "
                 f"{md_esc(d.get('subcategory', ''))} | **{d['weighted_total']}** | {d['verdict']} | "
                 f"{d['maintenance_status']} | {md_esc(d['licence'])[:44]} |")
    return "\n".join(o)


def counts_table(order, key, order_list=None, label="Value"):
    c = Counter(d[key] for d in order)
    keys = order_list or sorted(c, key=lambda k: -c[k])
    o = [f"| {label} | Projects |", "|---|--:|"]
    for k in keys:
        if k in c:
            o.append(f"| {k} | {c[k]} |")
    return "\n".join(o)


def write_rankings(order, byid):
    o = ["# Complete ranking — all {} projects".format(len(order))]
    o.append("\n[← Catalogue home](../README.md) · [Methodology](methodology.md) · "
             "[Journalism and AI](journalism-ai.md) · [Surveillance](surveillance.md) · "
             "[OSINT](osint.md) · [Findings](findings-and-limitations.md)")
    o.append("\nRanked by weighted total out of 100 under the "
             "[rubric weights](methodology.md#scoring-rubric). Ties are broken by relevance, then "
             "capability, then name. Score columns are **Rel**evance, **Cap**ability, "
             "**M**ai**nt**enance, **Priv**acy, **Use**ability and **Lic**ence+cost, each out of 5. "
             "**Conf** is evidence confidence, recorded separately from the score; `·P` marks a "
             "provisional assessment.")
    o.append("\nThe ranking encodes the priorities described in the "
             "[methodology](methodology.md#scoring-rubric), not a general quality ordering. A "
             "specialist tool scored against its intended role sits below a ubiquitous one even "
             "where it is excellent at its job.\n")
    o.append(master_table(order, "docs"))
    o.append("\n## Distribution\n")
    o.append("### By verdict\n")
    o.append(counts_table(order, "verdict", VERDICT_ORDER, "Verdict"))
    o.append("\n### By maintenance status\n")
    o.append(counts_table(order, "maintenance_status", MSTATUS_ORDER, "Status"))
    o.append("\n### By licence bucket\n")
    o.append(counts_table(order, "bucket", None, "Bucket"))
    o.append("\n### By evidence confidence\n")
    o.append(counts_table(order, "confidence", ["high", "medium", "low"], "Confidence"))
    band = Counter(f"{d['weighted_total'] // 10 * 10}–{d['weighted_total'] // 10 * 10 + 9}"
                   for d in order)
    o.append("\n### By score band\n")
    o.append("| Band | Projects |\n|---|--:|")
    for k in sorted(band, key=lambda x: -int(x.split("–")[0])):
        o.append(f"| {k} | {band[k]} |")
    open(os.path.join(DOCS, "rankings.md"), "w", encoding="utf-8").write("\n".join(o) + "\n")


def write_pillar_page(pl, order, byid):
    rows = [d for d in order if d["pillar"] == pl]
    name = PILLAR_NAME[pl]
    o = [f"# {name}"]
    o.append(f"\n{len(rows)} projects across {len(SEG_OF_PILLAR[pl])} segments.")
    o.append("\n[← Catalogue home](../README.md) · [All rankings](rankings.md) · "
             "[Methodology](methodology.md) · [Stacks](stacks.md) · "
             "[Findings](findings-and-limitations.md)")
    others = [p for p in PILLAR_ORDER if p != pl]
    o.append("\nOther pillars: " + " · ".join(
        f"[{PILLAR_NAME[p]}]({PILLAR_PAGE[p]})" for p in others))
    o.append("\n## Segments in this pillar\n")
    o.append("| Segment | Projects | Top-ranked |\n|---|--:|---|")
    for sg in SEG_OF_PILLAR[pl]:
        srows = [d for d in rows if d["segment"] == sg]
        if not srows:
            continue
        top = srows[0]
        o.append(f"| [{SEGMENT_NAME[sg]}](#{slug(SEGMENT_NAME[sg])}) | {len(srows)} | "
                 f"{link_project(top, 'docs')} ({top['weighted_total']}) |")
    o.append("\n## Pillar ranking\n")
    o.append("| Pillar # | Overall # | Project | Seg | Total | Verdict | Maintenance |")
    o.append("|--:|--:|---|---|--:|---|---|")
    for d in rows:
        o.append(f"| {d['rank_pillar']} | {d['rank_overall']} | {link_project(d, 'docs')} | "
                 f"{d['segment']} | **{d['weighted_total']}** | {d['verdict']} | "
                 f"{d['maintenance_status']} |")
    for sg in SEG_OF_PILLAR[pl]:
        srows = [d for d in rows if d["segment"] == sg]
        if not srows:
            continue
        o.append(f"\n## {SEGMENT_NAME[sg]}\n")
        o.append(f"{len(srows)} projects.\n")
        o.append(seg_table(srows, "docs"))
    o.append("\n## Distribution in this pillar\n")
    o.append(counts_table(rows, "verdict", VERDICT_ORDER, "Verdict"))
    o.append("\n")
    o.append(counts_table(rows, "maintenance_status", MSTATUS_ORDER, "Maintenance"))
    open(os.path.join(DOCS, PILLAR_PAGE[pl]), "w", encoding="utf-8").write("\n".join(o) + "\n")


def slug(s):
    """Emulate github-slugger: lowercase, drop punctuation, each space becomes a hyphen.

    Runs of spaces are NOT collapsed, because GitHub does not collapse them — a heading
    containing "A1 \u00b7 Discovery" anchors as "a1--discovery".
    """
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return s.replace(" ", "-")


def write_stacks(order, byid):
    o = ["[← Catalogue home](../README.md) · [All rankings](rankings.md) · "
         "[Methodology](methodology.md) · [Findings](findings-and-limitations.md)\n"]
    o.append(linkify(frag("40-stacks.md"), "docs", byid))
    o.append("\n---\n")
    o.append("Every project named above has a full assessment under "
             "[`docs/projects/`](projects/), reachable from the "
             "[complete ranking](rankings.md).")
    body = "\n".join(o)
    body = body.replace("## Suggested stacks", "# Suggested stacks", 1)
    open(os.path.join(DOCS, "stacks.md"), "w", encoding="utf-8").write(body + "\n")


def write_findings(order, byid):
    o = ["# Findings, blockers and limitations\n"]
    o.append("[← Catalogue home](../README.md) · [All rankings](rankings.md) · "
             "[Methodology](methodology.md) · [Stacks](stacks.md)\n")
    o.append(linkify(frag("50-findings.md"), "docs", byid))
    o.append("\n---\n")
    blocked = [d for d in order if d.get("blockers")]
    o.append(f"## Projects carrying material blockers\n")
    o.append(f"{len(blocked)} of {len(order)} projects carry at least one recorded blocker. "
             "Blockers are tracked separately from scores, so a project can rank well and still "
             "be unusable for a particular organisation.\n")
    o.append("| Project | Total | Verdict | Blockers |\n|---|--:|---|---|")
    for d in sorted(blocked, key=lambda x: -x["weighted_total"]):
        o.append(f"| {link_project(d, 'docs')} | {d['weighted_total']} | {d['verdict']} | "
                 + "<br>".join(md_esc(b) for b in d["blockers"]) + " |")
    o.append("\n---\n")
    o.append(linkify(frag("60-gaps.md"), "docs", byid))
    prov = [d for d in order if d.get("provisional")]
    o.append(f"\n### Provisional assessments ({len(prov)})\n")
    o.append("| Project | Total | Confidence | Verdict |\n|---|--:|---|---|")
    for d in sorted(prov, key=lambda x: -x["weighted_total"]):
        o.append(f"| {link_project(d, 'docs')} | {d['weighted_total']} | {d['confidence']} | "
                 f"{d['verdict']} |")
    low = [d for d in order if d["confidence"] == "low" and not d.get("provisional")]
    if low:
        o.append(f"\n### Low-confidence assessments not marked provisional ({len(low)})\n")
        o.append("| Project | Total | Verdict |\n|---|--:|---|")
        for d in sorted(low, key=lambda x: -x["weighted_total"]):
            o.append(f"| {link_project(d, 'docs')} | {d['weighted_total']} | {d['verdict']} |")
    o.append("\n---\n")
    o.append(linkify(frag("70-reconciliation.md"), "docs", byid))
    open(os.path.join(DOCS, "findings-and-limitations.md"), "w",
         encoding="utf-8").write("\n".join(o) + "\n")


def write_methodology(byid):
    body = linkify(frag("05-methodology.md"), "docs", byid)
    nav = ("[← Catalogue home](../README.md) · [All rankings](rankings.md) · "
           "[Stacks](stacks.md) · [Findings](findings-and-limitations.md)\n")
    body = body.replace("# Methodology\n", "# Methodology\n\n" + nav, 1)
    open(os.path.join(DOCS, "methodology.md"), "w", encoding="utf-8").write(body + "\n")


# -------------------------------------------------------------------- README

def write_readme(cat, order, byid):
    meta = cat["meta"]
    n = len(order)
    blocked = sum(1 for d in order if d.get("blockers"))
    o = []
    o.append("# Journalism AI, surveillance and OSINT tooling catalogue\n")
    o.append(f"An assessed, ranked and evidenced catalogue of **{n} open-source projects, "
             "datasets and services** used in investigative journalism, surveillance research "
             "and open-source investigation.\n")
    o.append("Every project carries a fourteen-field assessment, a six-dimension score, a "
             "maintenance classification with its evidence, a licence position verified against "
             "the licence file, and an explicit record of what could not be verified.\n")
    o.append("**Research verification dates: 2026-11-16 and 2026-11-17.** Each assessment records "
             "its own date. No project in this catalogue was installed or run — see "
             "[Methodology](docs/methodology.md) for what that means for the capability "
             "judgements.\n")
    o.append("## Who this is for\n")
    o.append("Engineers and technically-minded editors supporting independent journalism and "
             "media organisations, including media in exile, who can self-host, build "
             "integrations and run local AI. Hostile-state threat models and source protection "
             "are weighted accordingly: privacy and deployment control carry 15% of every "
             "score.\n")
    o.append("## Three research areas\n")
    o.append("| Pillar | Projects | Covers | Index |\n|---|--:|---|---|")
    for pl in PILLAR_ORDER:
        rows = [d for d in order if d["pillar"] == pl]
        segs = ", ".join(SEG_OF_PILLAR[pl])
        o.append(f"| **{PILLAR_NAME[pl]}** | {len(rows)} | segments {segs} | "
                 f"[{PILLAR_PAGE[pl]}](docs/{PILLAR_PAGE[pl]}) |")
    o.append("\n## Summary statistics\n")
    o.append(f"Calculated from [`records/`](records/) at build time; {n} projects, "
             f"{meta['validation_errors_count']} validation errors.\n")
    o.append("### Verdicts\n")
    o.append(counts_table(order, "verdict", VERDICT_ORDER, "Verdict"))
    o.append("\n### Maintenance\n")
    o.append(counts_table(order, "maintenance_status", MSTATUS_ORDER, "Status"))
    o.append("\n### Licence bucket\n")
    o.append(counts_table(order, "bucket", None, "Bucket"))
    o.append("\n### Evidence confidence\n")
    o.append(counts_table(order, "confidence", ["high", "medium", "low"], "Confidence"))
    o.append(f"\n{meta['provisional']} assessments are marked **provisional**. "
             f"{blocked} projects carry at least one **material blocker** — recorded separately "
             "from the score, so a project can rank well and still be unusable for a particular "
             "organisation. Both are listed in "
             "[Findings and limitations](docs/findings-and-limitations.md).\n")
    o.append("### Segments\n")
    o.append("| Segment | Projects |\n|---|--:|")
    for sg in SEG_ORDER:
        c = sum(1 for d in order if d["segment"] == sg)
        if c:
            o.append(f"| {SEGMENT_NAME[sg]} | {c} |")
    o.append("\n## Navigation\n")
    o.append("| Page | Contents |\n|---|---|")
    o.append("| [Complete ranking](docs/rankings.md) | All "
             f"{n} projects ranked, with score breakdowns and distributions |")
    o.append("| [Journalism and AI](docs/journalism-ai.md) | Pillar index and the A1–A4 segment rankings |")
    o.append("| [Surveillance and journalist protection](docs/surveillance.md) | Pillar index and the B1–B3 segment rankings |")
    o.append("| [OSINT and digital investigations](docs/osint.md) | Pillar index and the C1–C3 segment rankings |")
    o.append("| [Project assessments](docs/projects/) | One page per project, keyed by stable project ID |")
    o.append("| [Methodology](docs/methodology.md) | Research method, verification standard, scoring rubric, confidence definitions |")
    o.append("| [Suggested stacks](docs/stacks.md) | Three tool combinations for different team shapes |")
    o.append("| [Findings and limitations](docs/findings-and-limitations.md) | Licensing, maintenance and pricing findings; blockers; unresolved questions; coverage gaps |")
    o.append("| [Complete consolidated report](report.md) | Everything in one file, including all "
             f"{n} assessments |")
    o.append("\n### Data exports\n")
    o.append("| File | Format | Contents |\n|---|---|---|")
    o.append(f"| [`catalogue.json`](catalogue.json) | JSON | Complete structured export — "
             f"{n} projects with every field, plus computed ranks and summary counts |")
    o.append(f"| [`catalogue.csv`](catalogue.csv) | CSV | Spreadsheet-friendly export — {n} rows, "
             "43 columns; list fields are pipe-separated |")
    o.append("| [`records/`](records/) | JSON | Canonical hand-authored records; everything else is generated from these |")
    o.append("| [`sources/evidence/`](sources/evidence/) | Markdown, text | Resolved research leads, pricing evidence, source-URL verification, retrieved licence texts |")
    o.append("| [`work/meta.jsonl`](work/meta.jsonl) | JSON Lines | GitHub metadata sweep over 583 candidate repositories, 2026-11-17 |")
    o.append("\n## The 20 projects to examine first\n")
    o.append(linkify(frag("30-top20.md"), "root", byid)
             .replace("## The 20 projects to examine first\n", "", 1).lstrip())
    o.append("\n## Reading an assessment\n")
    o.append("### Verdicts\n")
    o.append("| Verdict | Meaning |\n|---|---|")
    o.append("| **Adopt** | Deploy it; the assessment states any conditions |")
    o.append("| **Integrate** | Worth building into a pipeline or stack as a component |")
    o.append("| **Pilot** | Promising, but evaluate on your own material before committing |")
    o.append("| **Monitor** | Not now; a specific change would alter the judgement |")
    o.append("| **Reference only** | Useful to read, cite or learn from, not to deploy |")
    o.append("| **Avoid for new deployment** | Do not build on it; a named alternative is given |")
    o.append("\n### Evidence confidence\n")
    o.append("Recorded separately from the score and never folded into it.\n")
    o.append("| Confidence | Meaning |\n|---|---|")
    o.append("| **high** | Primary sources verified — licence file read, API metadata captured, official pricing page retrieved |")
    o.append("| **medium** | Official documentation or README reviewed; some fields inferred from reliable secondary sources |")
    o.append("| **low** | Limited or conflicting evidence; several fields unverified |")
    o.append("\nAn assessment marked **provisional** still carries a score for comparability, with "
             "the gap stated in its Evidence section.\n")
    o.append("### Material blockers\n")
    o.append("A licence, dependency or operational-security problem that would stop a deployment. "
             "Blockers are listed in their own field on each project page and are **not** folded "
             "into the score, so they stay visible on projects that otherwise rank well — a "
             "non-commercial model licence, a withdrawn platform API, or a tool that uploads "
             "source material by default.\n")
    o.append("### Maintenance classifications\n")
    o.append("| Status | Basis |\n|---|---|")
    o.append("| **Actively maintained** | Substantive commits plus releases, issue throughput, or institutional backing with a security process |")
    o.append("| **Stable with low activity** | Mature and functionally complete; low velocity is appropriate, not a penalty |")
    o.append("| **Maintenance appears to be declining** | Activity has slowed materially against an open backlog, with no deprecation notice |")
    o.append("| **Dormant** | No substantive activity for an extended period; dependency rot likely |")
    o.append("| **Archived or discontinued** | `archived=true` on the API, or the upstream capability has been withdrawn |")
    o.append("| **Uncertain** | Maintenance cannot be evidenced — typically a hosted service with no public repository |")
    o.append("\nA recent push does not establish active maintenance, and infrequent commits do "
             "not establish abandonment. Each classification states its reasoning.\n")
    o.append("## Repository layout\n")
    o.append("```\n"
             "README.md                  this page (generated)\n"
             "report.md                  complete consolidated report (generated)\n"
             "catalogue.json             structured export (generated)\n"
             "catalogue.csv              tabular export (generated)\n"
             "build.py                   generator — reads records/ + narrative/, writes everything else\n"
             "records/                   canonical project records, hand-authored JSON\n"
             "narrative/                 hand-authored prose fragments composed into the pages\n"
             "docs/                      browsable pages (generated)\n"
             "  methodology.md\n"
             "  rankings.md\n"
             "  journalism-ai.md  surveillance.md  osint.md\n"
             "  stacks.md\n"
             "  findings-and-limitations.md\n"
             "  projects/                one page per project, named by project ID\n"
             "sources/evidence/          research leads, pricing, URL verification, licence texts\n"
             "sources/recovered/         first-session research artefacts, preserved unmodified\n"
             "work/                      metadata sweep output and the scripts that produced it\n"
             "STATE.md                   project state, open questions and next actions\n"
             "```\n")
    o.append("## Updating and regenerating\n")
    o.append("The canonical data is [`records/`](records/) and the prose fragments in "
             "[`narrative/`](narrative/). **Do not hand-edit** `README.md`, `report.md`, "
             "`catalogue.json`, `catalogue.csv` or anything under `docs/` — they are overwritten "
             "on every build.\n")
    o.append("To change an assessment, edit the project's object in the relevant "
             "`records/<SEGMENT>-NN.json` file. To add a project, append an object with all "
             "required fields and a new unused ID in the segment's series. Then:\n")
    o.append("```sh\npython3 build.py\n```\n")
    o.append("The build validates every record before writing anything: required fields present, "
             "verdict and maintenance status drawn from the controlled vocabularies, all six "
             "scores integers in 0–5, and no duplicate project IDs. It prints a validation-error "
             "count and a per-segment breakdown. The committed state builds with **zero "
             "validation errors**; treat any error as a blocker rather than a warning.\n")
    o.append("Ranks, counts, distribution tables, cross-references and all three exports are "
             "derived at build time, so they cannot drift from the records. Project IDs are "
             "stable and are the primary key across the records, the exports, the per-project "
             "pages and the cross-references between assessments.\n")
    o.append("## Status and intended use\n")
    o.append("This is a research catalogue prepared for internal use and possible later "
             "publication. It records judgements and the evidence behind them; it does not "
             "constitute an audit, a security review or a legal opinion. Licence summaries are "
             "research notes read from licence files on the dates stated — they are not legal "
             "advice, and several entries flag questions that need a lawyer rather than another "
             "survey. Prices were read from vendor pages on the dates stated and change without "
             "notice.\n")
    o.append("No licence has been chosen for this repository yet. That is a decision to take "
             "before any publication, and it needs to account for the third-party licence texts "
             "preserved under [`sources/evidence/licences/`](sources/evidence/licences/), which "
             "remain under their original terms.\n")
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write("\n".join(o) + "\n")


# -------------------------------------------------------------------- report

def write_report(cat, order, byid, byname):
    o = []
    o.append(frag("10-intro.md"))
    o.append("\n> This is the complete consolidated report. For a browsable version see "
             "[`README.md`](README.md) and the pages under [`docs/`](docs/) — in particular the "
             "[complete ranking](docs/rankings.md), the [methodology](docs/methodology.md) and "
             "the [per-project assessments](docs/projects/).\n")
    o.append(frag("20-how-to-read.md"))
    o.append("\n---\n")
    o.append(linkify(frag("30-top20.md"), "root", byid))
    o.append("\n---\n")
    o.append(linkify(frag("40-stacks.md"), "root", byid))
    o.append("\n---\n")
    o.append(linkify(frag("50-findings.md"), "root", byid))
    o.append("\n---\n")
    o.append(linkify(frag("60-gaps.md"), "root", byid))
    o.append("\n---\n")
    o.append(linkify(frag("70-reconciliation.md"), "root", byid))
    o.append("\n---\n\n# Complete ranked master table\n")
    o.append("Ranked by weighted total out of 100. `Conf` is evidence confidence, recorded "
             "separately from the score; `·P` marks a provisional assessment.\n")
    o.append(master_table(order, "root"))
    o.append("\n---\n\n# Rankings by pillar\n")
    for pl in PILLAR_ORDER:
        rows = [d for d in order if d["pillar"] == pl]
        o.append(f"\n## {PILLAR_NAME[pl]} — {len(rows)} projects\n")
        o.append("| Pillar # | Overall # | Project | Seg | Total | Verdict |")
        o.append("|--:|--:|---|---|--:|---|")
        for d in rows:
            o.append(f"| {d['rank_pillar']} | {d['rank_overall']} | {link_project(d, 'root')} | "
                     f"{d['segment']} | **{d['weighted_total']}** | {d['verdict']} |")
    o.append("\n---\n\n# Rankings by subcategory (segment)\n")
    for sg in SEG_ORDER:
        rows = [d for d in order if d["segment"] == sg]
        if not rows:
            continue
        o.append(f"\n## {SEGMENT_NAME[sg]} — {len(rows)} projects\n")
        o.append(seg_table(rows, "root"))
    o.append("\n---\n\n# Assessment of every project\n")
    o.append(f"All {len(order)} projects in overall rank order. Every assessment carries the same "
             "fourteen fields; project claims, documented feedback and the author's judgement are "
             "kept separate. Each heading links to the project's own page.\n")
    for d in order:
        o.append(f"\n---\n\n## {d['rank_overall']}. {d['name']} — {d['weighted_total']}/100\n")
        o.append(f"`{d['id']}` · {SEGMENT_NAME[d['segment']]} · {md_esc(d.get('subcategory',''))} · "
                 f"**{d['project_type']}** · bucket `{d['bucket']}` · "
                 f"maintainer {md_esc(d.get('maintainer','not recorded'))}")
        links = [f"[Project page](docs/projects/{d['id']}.md)"]
        if d.get("repo_url"):
            links.append(f"[repository]({d['repo_url']})")
        if d.get("docs_url"):
            links.append(f"[docs]({d['docs_url']})")
        o.append(" · ".join(links))
        o.append(f"\n**Scores** — {score_line(d)} "
                 f"(pillar rank {d['rank_pillar']}, segment rank {d['rank_segment']})")
        if d.get("provisional"):
            o.append("\n> **Provisional assessment** — the evidence does not support a firm "
                     "score; see Evidence below.")
        o.append("\n" + linkify(card_body(d, "root", byname, heading_level=3), "root", byid))
    open(os.path.join(ROOT, "report.md"), "w", encoding="utf-8").write("\n".join(o) + "\n")


# ---------------------------------------------------------------------- main

def main():
    items, errs = load()
    for d in items:
        d["weighted_total"] = total(d)
        d["status"] = d.get("status", "ranked")
    order = sorted(items, key=lambda d: (-d["weighted_total"], -d["scores"]["relevance"],
                                         -d["scores"]["capability"], d["name"].lower()))
    for i, d in enumerate(order, 1):
        d["rank_overall"] = i
    for key, field in (("pillar", "rank_pillar"), ("segment", "rank_segment")):
        groups = defaultdict(list)
        for d in order:
            groups[d[key]].append(d)
        for g in groups.values():
            for i, d in enumerate(g, 1):
                d[field] = i

    byid = {d["id"]: d for d in order}
    byname = {d["name"]: d for d in order}
    for d in order:
        if d.get("aka"):
            byname.setdefault(d["aka"], d)

    cat = {
        "meta": {
            "title": "Journalism AI, surveillance and OSINT tooling catalogue",
            "owner_context": "senior software/AI engineer supporting independent journalism and "
                             "media organisations, including media in exile",
            "generated": "2026-11-17",
            "verification_dates": ["2026-11-16", "2026-11-17"],
            "rubric": "sources/recovered/cat/RUBRIC.md",
            "weights": W,
            "unique_projects": len(items),
            "pillars": dict(Counter(d["pillar"] for d in order)),
            "segments": dict(Counter(d["segment"] for d in order)),
            "buckets": dict(Counter(d["bucket"] for d in order)),
            "verdicts": dict(Counter(d["verdict"] for d in order)),
            "maintenance": dict(Counter(d["maintenance_status"] for d in order)),
            "confidence": dict(Counter(d["confidence"] for d in order)),
            "provisional": sum(1 for d in order if d.get("provisional")),
            "with_blockers": sum(1 for d in order if d.get("blockers")),
            "validation_errors_count": len(errs),
            "validation_errors": errs,
        },
        "projects": order,
    }
    json.dump(cat, open(os.path.join(ROOT, "catalogue.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)

    cols = ["rank_overall", "id", "name", "pillar", "segment", "subcategory", "project_type",
            "bucket", "weighted_total", "score_relevance", "score_capability",
            "score_maintenance", "score_privacy", "score_usability", "score_licence_cost",
            "verdict", "maintenance_status", "licence", "model_or_data_licence",
            "licence_restrictions", "costs", "privacy", "purpose", "journalism_use_case",
            "audience", "pros", "cons", "feedback", "assessment", "maintenance_evidence",
            "alternatives", "blockers", "repo_url", "docs_url", "licence_evidence_url",
            "evidence_urls", "verification_date", "confidence", "depth", "provisional",
            "rank_pillar", "rank_segment", "status"]
    with open(os.path.join(ROOT, "catalogue.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for d in order:
            row = []
            for c in cols:
                v = d["scores"][c[6:]] if c.startswith("score_") else d.get(c, "")
                if isinstance(v, list):
                    v = " | ".join(str(x) for x in v)
                elif isinstance(v, bool):
                    v = "yes" if v else "no"
                row.append(v)
            w.writerow(row)

    os.makedirs(DOCS, exist_ok=True)
    npages = write_project_pages(order, byid, byname)
    write_rankings(order, byid)
    for pl in PILLAR_ORDER:
        write_pillar_page(pl, order, byid)
    write_methodology(byid)
    write_stacks(order, byid)
    write_findings(order, byid)
    write_readme(cat, order, byid)
    write_report(cat, order, byid, byname)

    print(f"projects:            {len(items)}")
    print(f"project pages:       {npages}")
    print(f"pillars:             {cat['meta']['pillars']}")
    print(f"segments:            {dict(sorted(cat['meta']['segments'].items()))}")
    print(f"buckets:             {cat['meta']['buckets']}")
    print(f"verdicts:            {cat['meta']['verdicts']}")
    print(f"provisional:         {cat['meta']['provisional']}")
    print(f"with blockers:       {cat['meta']['with_blockers']}")
    print(f"validation errors:   {len(errs)}")
    for e in errs[:40]:
        print("  !", e)
    if len(errs) > 40:
        print(f"  ... {len(errs)-40} more")


if __name__ == "__main__":
    main()
