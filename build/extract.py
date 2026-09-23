#!/usr/bin/env python3
"""Rebuild the per-week JSON data from the workflow journals (the durable source)."""
import json, re, os
WF = "/home/cgamb/.claude/projects/-home-cgamb-DE-Full-Course/03a1c4db-2f7a-487e-ad56-da138a801b9a/subagents/workflows"
OUT = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT, exist_ok=True)

def load(wf):
    rows=[]
    for line in open(f"{WF}/{wf}/journal.jsonl"):
        try: o=json.loads(line)
        except: continue
        if o.get("type")=="result" and isinstance(o.get("result"), dict):
            rows.append(o["result"])
    return rows

def wnum(w):
    m=re.search(r"\d+", str(w.get("week",""))); return int(m.group()) if m else 0

def dump(name, rows, dedupe=False):
    if dedupe:
        by={}
        for r in rows: by[wnum(r)]=r   # keep last occurrence
        rows=[by[k] for k in sorted(by)]
    else:
        rows=sorted(rows, key=wnum)
    json.dump(rows, open(f"{OUT}/{name}.json","w"), indent=1)
    print(f"{name}: {len(rows)} weeks -> {[wnum(r) for r in rows]}")

dump("phase1_base", load("wf_0a317148-c45"))            # W2-W13 base
dump("phase1_enh",  load("wf_6ef44fc8-279"))            # W1-W13 enhanced labs
dump("phase2",      load("wf_de8438d1-29a"))            # W14-W30
dump("phase3",      load("wf_eb488478-4dd"))            # W31-W43
dump("phase4",      load("wf_47169290-37d"), dedupe=True)  # W44-W48 (dedupe resume)
