#!/usr/bin/env python3
"""Merge agent JSONL outputs into one catalogue, dedupe by repo URL, assign stable IDs."""
import json, sys, csv, re, os
FIELDS=["id","name","maintainer","primary_category","tags","project_type","description",
        "journalism_use_case","repo_url","docs_url","licence","licence_spdx_verified",
        "model_or_data_licence","licence_evidence_url","language_stack","deployment",
        "latest_release","last_activity","archived","external_dependencies","data_flows",
        "limitations","readiness","bucket","verification_date","evidence_urls"]
def norm(u):
    if not u: return ""
    u=u.strip().rstrip("/").lower()
    u=re.sub(r"^https?://(www\.)?","",u)
    u=re.sub(r"\.git$","",u)
    return u
def load(path):
    out=[]
    for line in open(path):
        line=line.strip()
        if not line or not line.startswith("{"): continue
        try: out.append(json.loads(line))
        except Exception: pass
    return out
