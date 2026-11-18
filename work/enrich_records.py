#!/usr/bin/env python3
"""One-off enrichment: add structured licensing, pricing and summary fields to records/.

This is NOT run by build.py. It derives candidate values from the already-verified
free-text fields (licence, model_or_data_licence, licence_restrictions, costs, bucket,
project_type), applies hand-reviewed overrides from work/enrich_overrides.json, and
writes the result back into the canonical records so the values are visible and
diffable in git.

Nothing here invents a price. Where the records do not establish a price, the derived
value is "Unknown / not verified".

    python3 work/enrich_records.py --audit    # one review line per project (TSV)
    python3 work/enrich_records.py --write    # write fields into records/
"""
import json, glob, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- vocabularies

LICENCE_TYPES = ["Permissive", "Weak copyleft", "Strong copyleft", "Dual-licensed",
                 "Public domain", "Open data licence", "Restricted / non-OSI",
                 "Mixed (code vs weights/data)", "Proprietary", "Unresolved"]

# Filterable status: the five values the brief asks for.
OSS_STATUS = ["Open source", "Source available", "Mixed", "Proprietary", "Unverified"]
# oss_detail carries the precise wording, so a dataset or a hosted public-records
# portal is never described as "open-source software".

PRICE_CLASSES = ["No software fee", "No fee below threshold", "Free tier", "Paid",
                 "Quote required", "Unknown / not verified"]

COST_FLAGS = {
    "mandatory-paid": "Mandatory paid dependency (API, data, model or tool)",
    "optional-hosted": "Optional paid hosted service or commercial licence",
    "infrastructure": "Self-hosting infrastructure cost (compute, storage, ops)",
    "hardware": "Dedicated hardware required",
    "staff-effort": "Material staff or analyst effort",
    "none-material": "No material additional cost recorded",
}

# ------------------------------------------------------------------- summaries

def summarise(purpose, limit=130):
    """First clause or sentence of the verified purpose, trimmed at a natural break."""
    t = " ".join(purpose.split())
    if len(t) <= limit:
        return t.rstrip(".")
    m = re.match(r"(.{40,%d}?)[.;]\s" % limit, t)
    if m:
        return m.group(1).rstrip(".;,")
    cut = t[:limit]
    # Cut at the LATEST natural break before the limit, not the first one found,
    # so the summary keeps as much of the leading clause as it can.
    best = max((cut.rfind(sep) for sep in
                (", with ", ", and ", ", ", " — ", " – ", "; ", " that ", " which ")),
               default=-1)
    # Only break at a separator if doing so keeps most of the allowance; otherwise a
    # word-boundary cut at the limit carries more information.
    if best > limit * 0.6:
        return cut[:best].rstrip(" ,;—–") + "…"
    return cut[:cut.rfind(" ")].rstrip(" ,;") + "…"


# -------------------------------------------------------------------- licences

PERMISSIVE = r"\b(MIT|Apache-2\.0|BSD-2-Clause|BSD-3-Clause|ISC|0BSD)\b"
WEAK_COPY = r"\b(LGPL-[\d.]+(?:-or-later)?|MPL-2\.0)\b"
STRONG_COPY = r"\b(GPL-[\d.]+(?:-or-later)?|AGPL-[\d.]+(?:-or-later)?)\b"
PUBLIC_DOMAIN = r"\b(CC0-1\.0|Unlicense|0BSD)\b|public domain"
NONCOMM = r"CC-BY-NC|NonCommercial|non-commercial only|noncommercial|non-profit"
RESTRICTED = (r"NOT OSI|not OSI-approved|NOT OSS|academic|research[- ]only|"
              r"Do No Harm|OpenRAIL|Sustainable Use|MVT License|SnT|GRIP-UNINA|"
              r"informational and non-profit|ADDITIONAL TERMS|Terms of Use|"
              r"consensual|field-of-use")
UNRESOLVED = (r"NOT CONFIRMED|Not detected|not detected|could not be confirmed|"
              r"no licence detected|no LICENSE|NOT verified")
OPEN_DATA = r"CC-BY-4\.0|CC-BY 4\.0|CC0|ODbL|Open Government Licence|public domain"


def licence_type(d):
    lic = d["licence"]
    mdl = d.get("model_or_data_licence", "") or ""
    res = d.get("licence_restrictions", "") or ""
    if d["bucket"] == "proprietary-service":
        return "Proprietary"
    code_open = bool(re.search(PERMISSIVE, lic) or re.search(WEAK_COPY, lic)
                     or re.search(STRONG_COPY, lic))
    # "\sOR\s" is case-sensitive on purpose: a lowercase "or" matches inside
    # "GPL-3.0-or-later", which is one licence, not a choice of two.
    dual = (re.search(r"\sOR\s", lic) or re.search(r"dual[- ]licens|\(dual[,)]|\bdual\b",
                                                   lic, re.I))
    if dual and code_open:
        return "Dual-licensed"
    if re.search(RESTRICTED, lic) or re.search(NONCOMM, lic):
        return "Restricted / non-OSI"
    if re.search(UNRESOLVED, lic) and not code_open:
        return "Unresolved"
    weights_restricted = bool(re.search(NONCOMM, mdl) or re.search(RESTRICTED, mdl)
                              or re.search(r"OpenRAIL|threshold", f"{mdl} {res}"))
    if code_open and weights_restricted:
        return "Mixed (code vs weights/data)"
    if re.search(PUBLIC_DOMAIN, lic):
        return "Public domain"
    if d["project_type"] == "dataset" and re.search(OPEN_DATA, f"{lic} {mdl}"):
        return "Open data licence"
    if re.search(STRONG_COPY, lic):
        return "Strong copyleft"
    if re.search(WEAK_COPY, lic):
        return "Weak copyleft"
    if re.search(PERMISSIVE, lic):
        return "Permissive"
    return "Unresolved"


def _restricted_part(mdl):
    """Name what is restricted. Several mixed projects distribute no weights at
    all — the restriction is on the DATA they consume or serve — so defaulting
    to "model weights" would misdescribe them."""
    if re.search(r"VARIES", mdl):
        return "model weights that vary by checkpoint — some non-commercial"
    if re.search(r"carr(?:y|ies) (?:its|their) own licen|retain the licence of the source",
                 mdl, re.I):
        return "data or models you load carrying their own terms, some non-commercial"
    has_data = bool(re.search(r"\bdata(?:set|base)?\b|CC-BY|ODbL|ODC", mdl, re.I))
    has_weights = bool(re.search(r"\bweights?\b|\bmodels?\b|checkpoint", mdl, re.I))
    if has_data and has_weights:
        return "restricted model weights and data terms"
    if has_data:
        return "restricted data licence"
    return "restricted model weights"


def oss_status(d):
    """Return (status, detail): a filterable five-value status plus precise wording."""
    b, pt = d["bucket"], d["project_type"]
    mdl = d.get("model_or_data_licence", "") or ""
    weights_restricted = bool(re.search(NONCOMM, mdl)
                              or re.search(r"OpenRAIL|research[- ]only|academic", mdl))
    if b == "proprietary-service":
        return "Proprietary", ("Hosted service or proprietary software — governed by "
                               "service terms, not a software licence")
    if b == "uncertain":
        return "Unverified", "Licence could not be confirmed — reuse legally unresolved"
    if b == "source-available-weights":
        return "Mixed", "Open-source code, " + _restricted_part(mdl)
    if b == "source-available-restricted":
        if pt == "dataset":
            return "Source available", "Restricted data licence"
        if pt == "model":
            return "Source available", "Restricted model weights"
        return "Source available", "Source published under a restricted, non-OSI licence"
    # verified-oss
    if pt == "dataset":
        return "Open source", "Open data licence"
    if pt == "model":
        return "Open source", "Open model weights"
    if weights_restricted:
        return "Mixed", "Open-source code, " + _restricted_part(mdl)
    return "Open source", "Open-source software licence"


# --------------------------------------------------------------------- pricing

AMOUNT = re.compile(
    r"(?:EUR|USD|\$|€)\s?\d[\d,.]*(?:\s?(?:/|per\s)\s?"
    r"(?:year|yr|month|mo|hour|h|page|M tokens|GB/hour|audio-hour))?", re.I)
NOFEE = (r"\bno (?:software |licence |license )?fee\b|\bno fees\b|\bno licence fees?\b|"
         r"^Free\b|^Free\.|\bfree to use\b|\bNo fee\b|\bsoftware free\b|"
         r"\blibrary free\b|\bCode free\b|\bfree download\b|\bno direct fee\b|"
         r"\bOpen (?:library|core|edition) free\b|\bClient free\b|\bFramework free\b|"
         r"\bTool free\b|\bFree to read\b|\bFree to search\b|\bPublic service free\b|"
         r"\bCommunity Edition[^.]{0,40}free\b|\bopen engine free\b|\bFree\b(?=[.,])")
FREETIER = (r"free tier|Free \$0|free credits|free forever|Basic free|"
            r"historically free|free for (?:research|non-commercial|verified|permitted)|"
            r"free within|Free to use the (?:public )?(?:service|dashboard)|"
            r"free with no rate limit")
QUOTE = r"quote required|quote-only|not publicly listed|contact sales|custom quote"
UNKNOWN_PRICE = (r"NOT verified|not verified in this survey|not priced here|"
                 r"were not verified|was not verified|not publicly confirmed|"
                 r"not established|treat as unknown")
THRESHOLD = r"threshold"

MANDATORY = (r"requires? (?:an? )?(?:paid|OpenAI|Serper|MATLAB|Google Programmable|"
             r"archive-node|subscription)|operation requires paid|requires paid|"
             r"API keys?[^.]{0,80}paid|\bpaid API\b|required paid|"
             r"MATLAB \(a paid product\) is required|"
             r"commercial licence is required|needs a (?:paid|commercial)|"
             r"requires a Google|requires the OpenSanctions commercial|"
             r"SMS gateway costs|per-message")
OPTIONAL_HOSTED = (r"hosted[^.]{0,70}(?:priced|paid|subscription|tiers|\$|EUR)|"
                   r"paid tiers|managed (?:service|offering|Elasticsearch)|"
                   r"commercial (?:licence|product|support|version|offering|tier)|"
                   r"Enterprise|AuraDB|hosted service|paid hosted|sells a commercial|"
                   r"separate commercial")
INFRA = (r"[Ee]stimate|infrastructure|GPU|VM\b|cluster|storage|Elasticsearch|"
         r"PostgreSQL|compute|CPU|disk|bandwidth|self-host|container|server")
# Dedicated hardware the project cannot be used without. Deliberately narrow:
# "runs on commodity hardware" or "an analyst workstation" is infrastructure, not this.
HARDWARE = (r"RTL-SDR|dongle|antenna|Raspberry Pi|certified (?:hardware|laptop)|"
            r"Qubes-capable|Qubes-certified|two servers|air-gapped|supported[^.]{0,20}hotspot|"
            r"USB stick")
STAFF = (r"staff|analyst time|operator time|human (?:review|adjudication|transcription|"
         r"verification|labelling)|labour|engineer time|ops time|training|"
         r"curation time|moderation")


def _sentences(text):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", text) if x.strip()]


NEGATION = r"\bno paid\b|\bnot required\b|\boptional\b|\bOptional\b|\bwithout\b|\bhelpful but\b"


def pricing(d):
    """Classify the project's OWN software price, then flag additional costs.

    The price class is read from the FIRST SENTENCE of `costs`, because the records
    consistently state the software price there. Scanning the whole paragraph
    conflates the project's price with a dependency's price (a search API's free
    tier is not the project's free tier).
    """
    c = d["costs"]
    sents = _sentences(c)
    head = sents[0] if sents else ""
    b = d["bucket"]
    amounts = sorted(set(a.strip() for a in AMOUNT.findall(c)))
    head_amounts = sorted(set(a.strip() for a in AMOUNT.findall(head)))

    h_nofee = bool(re.search(NOFEE, head, re.I))
    h_free = bool(re.search(FREETIER, head, re.I))
    h_quote = bool(re.search(QUOTE, head, re.I))
    h_unknown = bool(re.search(UNKNOWN_PRICE, head, re.I))
    thresh = bool(re.search(THRESHOLD, c, re.I))
    any_quote = bool(re.search(QUOTE, c, re.I))

    if b == "proprietary-service":
        if h_unknown:
            cls = "Unknown / not verified"
        elif h_free:
            cls = "Free tier"
        elif h_nofee:
            cls = "No software fee"
        elif head_amounts:
            cls = "Paid"
        elif h_quote or any_quote:
            cls = "Quote required"
        else:
            cls = "Unknown / not verified"
    else:
        if h_unknown and not h_nofee:
            cls = "Unknown / not verified"
        elif h_nofee and thresh:
            cls = "No fee below threshold"
        elif h_nofee:
            cls = "No software fee"
        elif h_free:
            cls = "Free tier"
        elif h_quote:
            cls = "Quote required"
        elif head_amounts:
            cls = "Paid"
        else:
            cls = "Unknown / not verified"

    # Additional-cost flags: sentence-aware, with negation guards so "no paid API"
    # and "optional API keys" are not read as mandatory.
    flags = []
    for sent in sents:
        if re.search(MANDATORY, sent, re.I) and not re.search(NEGATION, sent):
            flags.append("mandatory-paid")
            break
    if re.search(OPTIONAL_HOSTED, c, re.I) or any_quote or (
            re.search(MANDATORY, c, re.I) and "mandatory-paid" not in flags):
        flags.append("optional-hosted")
    if re.search(HARDWARE, c):
        flags.append("hardware")
    if re.search(INFRA, c):
        flags.append("infrastructure")
    if re.search(STAFF, c, re.I):
        flags.append("staff-effort")
    if not flags:
        flags = ["none-material"]
    return cls, amounts, flags


# ------------------------------------------------------------------- overrides

OVERRIDES = {}
_ov = os.path.join(ROOT, "work", "enrich_overrides.json")
if os.path.exists(_ov):
    _raw = json.load(open(_ov, encoding="utf-8"))
    # Keys and fields beginning with "_" are review annotations (_README, _reason)
    # and must never reach the records.
    OVERRIDES = {k: {f: v for f, v in ov.items() if not f.startswith("_")}
                 for k, ov in _raw.items() if not k.startswith("_")}

SHORT_FLAG = {"mandatory-paid": "mandatory paid dependency",
              "optional-hosted": "optional paid hosting / commercial licence",
              "infrastructure": "self-hosted infrastructure",
              "hardware": "dedicated hardware",
              "staff-effort": "staff effort",
              "none-material": "no material additional cost recorded"}
FLAG_ORDER = ["mandatory-paid", "optional-hosted", "hardware", "infrastructure",
              "staff-effort", "none-material"]


def price_note(cls, amounts):
    if cls == "Paid" and amounts:
        return "; ".join(amounts[:3])
    if cls == "No fee below threshold":
        return "free below the vendor revenue/funding threshold; paid licence above"
    if cls == "Quote required":
        return "not publicly listed"
    if cls == "Unknown / not verified":
        return "not established by the records"
    if cls == "Free tier" and amounts:
        return "free tier; paid tiers from " + amounts[0]
    return ""


def cost_note(flags):
    return "; ".join(SHORT_FLAG[f] for f in FLAG_ORDER if f in flags)


def enrich(d):
    cls, amounts, flags = pricing(d)
    out = {
        "summary": summarise(d["purpose"]),
        "licence_type": licence_type(d),
        "oss_status": oss_status(d)[0],
        "oss_detail": oss_status(d)[1],
        "price_class": cls,
        "software_price_note": price_note(cls, amounts),
        "cost_flags": flags,
        "additional_costs_note": cost_note(flags),
    }
    ov = OVERRIDES.get(d["id"], {})
    out.update(ov)
    if "cost_flags" in ov and "additional_costs_note" not in ov:
        out["additional_costs_note"] = cost_note(out["cost_flags"])
    if "price_class" in ov and "software_price_note" not in ov:
        out["software_price_note"] = price_note(out["price_class"], amounts)
    # The flag drives the filters and the bold label; the note is what a reader sees.
    # If an override writes one without the other they disagree silently, so fail loudly.
    says_mandatory = out["additional_costs_note"].lower().startswith("mandatory")
    has_flag = "mandatory-paid" in out["cost_flags"]
    if says_mandatory != has_flag:
        raise SystemExit(
            f"{d['id']}: additional_costs_note and cost_flags disagree about a mandatory "
            f"paid dependency (note says {says_mandatory}, flag says {has_flag})")
    return out


# Most record files use a compact hand-authored style ('{"id":"X-00-00","name":...');
# records/B1-02.json is pretty-printed. Both are matched.
ID_LINE = re.compile(r'^\s*\{?\s*"id":\s*"([A-Z]+-[ABC][1-4]-\d{2})"')
SCORES_LINE = re.compile(r'^(\s*)"scores":')
FIELD_ORDER = ["summary", "licence_type", "oss_status", "oss_detail",
               "price_class", "software_price_note", "cost_flags",
               "additional_costs_note"]


def splice(path, enriched):
    """Insert the derived fields as one new line per record, immediately before
    that record's "scores" line.

    The records were hand-authored in a compact style that json.dump cannot
    reproduce; re-dumping them reformats all 361 objects and buries the actual
    change in a 26,000-line diff. Splicing a single line per record keeps every
    existing line byte-identical, so the diff shows exactly what was added and
    stays reviewable. The result is re-parsed and compared against `enriched`
    before it is written, so a malformed splice fails loudly.
    """
    lines = open(path, encoding="utf-8").read().split("\n")
    out, current = [], None
    for line in lines:
        m = ID_LINE.match(line)
        if m:
            current = m.group(1)
        sm = SCORES_LINE.match(line)
        if sm and current:
            e, pad = enriched[current], sm.group(1)
            frag = ",".join(json.dumps(k, ensure_ascii=False) + ":" +
                            json.dumps(e[k], ensure_ascii=False)
                            for k in FIELD_ORDER)
            out.append(pad + frag + ",")
            current = None
        out.append(line)
    text = "\n".join(out)

    check = json.loads(text)
    for d in check:
        for k in FIELD_ORDER:
            if d[k] != enriched[d["id"]][k]:
                raise SystemExit(f"splice mismatch: {d['id']} {k}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--audit"
    files = sorted(glob.glob(os.path.join(ROOT, "records", "*.json")))
    stats, rows = collections.Counter(), []
    for p in files:
        data = json.load(open(p, encoding="utf-8"))
        enriched = {}
        for d in data:
            e = enrich(d)
            stats[("type", e["licence_type"])] += 1
            stats[("oss", e["oss_status"])] += 1
            stats[("price", e["price_class"])] += 1
            for f in e["cost_flags"]:
                stats[("flag", f)] += 1
            rows.append((d, e))
            enriched[d["id"]] = e
        if mode == "--write":
            splice(p, enriched)
    if mode == "--audit":
        for d, e in rows:
            print("\t".join([d["id"], d["name"][:34], d["bucket"][:12],
                             d["project_type"][:9], e["licence_type"][:28],
                             e["oss_status"][:18], e["price_class"][:22],
                             ",".join(e["cost_flags"]), d["licence"][:38],
                             " ".join(d["costs"].split())[:160]]))
    print("\n--- derived distribution ---", file=sys.stderr)
    for grp in ("type", "oss", "price", "flag"):
        print(f"[{grp}]", file=sys.stderr)
        for (g, k), v in sorted(stats.items(), key=lambda x: -x[1]):
            if g == grp:
                print(f"  {v:4d}  {k}", file=sys.stderr)
    if mode == "--write":
        print(f"\nwrote enrichment into {len(files)} record files "
              f"({len(rows)} projects)", file=sys.stderr)


if __name__ == "__main__":
    main()
