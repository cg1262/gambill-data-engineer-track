#!/usr/bin/env python3
"""Render the four phase lesson-plan pages from build/data/*.json.
Usage: python render_phases.py <linkmode>   where linkmode = 'artifact' or 'site'."""
import json, re, html, sys, os

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "data")
BASECSS = open(os.path.join(HERE, "base.css")).read()

# ---- link maps ---------------------------------------------------------------
ART = {
    "home": "https://claude.ai/code/artifact/bbf75ac1-4993-40ea-a08f-d488d2b5acf4",
    "cur":  "https://claude.ai/code/artifact/085627d8-ff0b-4b9a-a7cf-c83107cb71bf",
    "p1":   "https://claude.ai/code/artifact/59592bdb-3bce-4336-ba9a-69df5f936caf",
    "p2":   "https://claude.ai/code/artifact/d064d266-fe89-46d3-9b3a-f9094a6c2397",
    "p3":   "https://claude.ai/code/artifact/4f4034d2-8cab-4c0b-8d9d-bc6391654d4f",
    "p4":   "https://claude.ai/code/artifact/6fc11b3c-5ca1-4211-9672-58249453a740",
}

SITE = {
    "home": "index.html", "cur": "curriculum.html",
    "p1": "phase-1.html", "p2": "phase-2.html", "p3": "phase-3.html", "p4": "phase-4.html",
}

MODE = sys.argv[1] if len(sys.argv) > 1 else "artifact"
LINKS = dict(ART) if MODE == "artifact" else dict(SITE)
OUTDIR = os.path.join(HERE, "..", ("artifact_out" if MODE == "artifact" else "site"))
os.makedirs(OUTDIR, exist_ok=True)

# ---- helpers -----------------------------------------------------------------
URL_RE = re.compile(r"(https?://[^\s,)]+)")
def linkify(s):
    out, i = [], 0
    for m in URL_RE.finditer(s):
        out.append(html.escape(s[i:m.start()])); u = m.group(1)
        out.append(f'<a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(u)}</a>'); i = m.end()
    out.append(html.escape(s[i:])); return "".join(out)
def e(s): return html.escape(html.unescape(s or ""))
def li(items): return "".join(f"<li>{e(x)}</li>" for x in items or [])
def gap_chips(gaps):
    out, seen = [], set()
    for g in gaps or []:
        s = str(g).strip(); m = re.match(r"\s*(G\d+|foundation)", s, re.I)
        code = (m.group(1) if m else s[:8]).strip(); key = code.lower()
        if key in seen: continue
        seen.add(key); label = "foundation" if key == "foundation" else code.upper()
        cls = "gtag f" if key == "foundation" else "gtag"
        out.append(f'<span class="{cls}">{e(label)}</span>')
    return "".join(out)
def datasets_html(dss):
    rows = []
    for d in dss or []:
        url = (d.get("url", "") or "").strip()
        url_html = "&mdash;" if url in ("", "—", "&mdash;") else linkify(url)
        rows.append(f'<div class="ds"><div class="ds-name">{e(d.get("name",""))}</div>'
                    f'<div class="ds-url">{url_html}</div>'
                    f'<div class="ds-mess"><span class="ml">Mess to handle</span> {e(d.get("whatsMessy",""))}</div></div>')
    return "".join(rows)
def refs_html(refs):
    out = []
    for r in refs or []:
        t, u = e(r.get("title", "")), r.get("url", "")
        out.append(f'<li><a href="{html.escape(u)}" target="_blank" rel="noopener">{t}</a></li>' if u else f'<li>{t}</li>')
    return "".join(out)
def script_html(sc):
    if not sc: return ""
    fn = e(sc.get("filename", "starter")); lang = e(sc.get("language", "")); code = e(sc.get("code", "")); note = sc.get("note", "")
    note_html = f'<div class="sc-note"><span class="ml">Note</span> {e(note)}</div>' if note else ""
    return (f'<details class="script"><summary><span class="sc-ic">&lt;/&gt;</span> Starter scaffold &mdash; <span class="mono">{fn}</span> '
            f'<span class="sc-lang">{lang}</span></summary><pre><code>{code}</code></pre>{note_html}</details>')
def wnum(w):
    m = re.search(r"\d+", str(w.get("week", ""))); return int(m.group()) if m else 0

def navbar(items, weeknums):
    parts = []
    for i, (label, key, home) in enumerate(items):
        cls = ' class="navhome"' if home else ""
        parts.append(f'<a{cls} href="{LINKS[key]}">{label}</a>')
    parts.append('<span class="navsep"></span>')
    parts.append('<span class="nl">Weeks</span>')
    parts += [f'<a href="#w{n}">W{n}</a>' for n in weeknums]
    return '<nav class="weeknav"><div class="wrap">' + "".join(parts) + '</div></nav>'

def page(title, extra_css, hero, nav, cards, footer):
    return (f'<title>{title}</title>\n<style>\n{BASECSS}\n{extra_css}\n</style>\n'
            f'{hero}\n{nav}\n<main class="wrap">\n{cards}\n</main>\n{footer}\n')

# ---- Phase 1 (base + enhanced merge) ----------------------------------------
META = {
 1:("M00","Dev environment, the command line & Git",["foundation","G6"]),
 2:("M01","The DE mental model & the data lifecycle",["G1","G9","G10"]),
 3:("M02","Python I — control flow & functions",["G1","G6"]),
 4:("M02","Python II — data structures & files",["G1","G6","G4"]),
 5:("M02","Python III — modules, environments & OOP basics",["G1","G6"]),
 6:("M03","pandas — DataFrames: select, clean, transform, group & merge",["G1","G4","G2"]),
 7:("M03","Python for data II — APIs & reconciliation",["G1","G4"]),
 8:("M04","Software engineering hygiene — typed, tested, packaged",["G6","G1","G4"]),
 9:("M05","SQL I — joins & filtering",["G1","G2"]),
 10:("M05","SQL II — aggregation & subqueries",["G1","G10"]),
 11:("M06","Advanced SQL I — window functions & CTEs",["G1","G10"]),
 12:("M06","Advanced SQL II — query plans & tuning",["G1","G7"]),
 13:("M07","Relational theory & normalization — keys, FDs, 1NF→3NF",["G2","G1","G10"]),
}
W1_BASE = {
 "objectives":["Move around a filesystem and run common shell commands with confidence",
   "Initialize a Git repo; stage, commit, branch, push, and open a pull request",
   "Create a reproducible Python environment and manage its dependencies",
   "Structure a project repo with a README, .gitignore, and env manifest"],
 "lessons":["Terminal & shell basics: paths, files, pipes","The Git model: working tree → stage → history",
   "Branches, remotes, and the PR workflow","Environments & dependency management (venv/conda)",
   "Repo hygiene: structure, README, ignore rules"],
 "lessonHours":4,
 "liveRecap":"the Git mental model.",
 "liveMisconception":"conflating stage vs commit vs push.",
 "liveHotSeat":"Walk me through exactly what happens, and where your code lives, at each step of add → commit → push.",
 "portfolio":"Initializes the portfolio repository that every later week's work is committed into — the backbone of the whole Phase 1 project.",
 "prereqs":"Assumes nothing. The Git / PR / venv workflow established here is used in every subsequent week.",
}

def card_p1(n, base, enh):
    mod, title, gaps = META[n]
    b = W1_BASE if n == 1 else base[n]
    x = enh[n]
    modline = f"{mod} · Phase 1 · bronze" + (" · Phase 1 capstone" if n == 13 else "")
    lh = x.get("labHours") or 5; ch = b.get("lessonHours") or 4
    return f'''
  <article class="wk-card" id="w{n}">
    <div class="wk-head">
      <span class="wk-num">W{n:02d}</span>
      <span class="wk-title">{e(title)}</span>
      <span class="wk-mod">{e(modline)}</span>
      <span class="wk-gaps">{gap_chips(gaps)}</span>
    </div>
    <div class="framing"><span class="fl">Why this matters</span> {e(x.get("businessFraming",""))}</div>
    <div class="wk-grid">
      <div class="blk"><div class="bh">Objectives</div><ul>{li(b.get("objectives",[]))}</ul></div>
      <div class="blk"><div class="bh">Concept lessons <span class="hrs">· ~{ch}h</span></div><ul>{li(b.get("lessons",[]))}</ul></div>
      <div class="blk full lab">
        <div class="bh">Hands-on lab <span class="hrs">· ~{lh}h</span></div>
        <p>{e(x.get("labSummary",""))}</p>
        <div class="lab-sub">Step by step</div>
        <ol class="steps">{li(x.get("labSteps",[]))}</ol>
        <div class="lab-sub">Data</div>
        <div class="ds-list">{datasets_html(x.get("datasets"))}</div>
        <div class="lab-sub">Reference material</div>
        <ul class="refs">{refs_html(x.get("referenceMaterials"))}</ul>
        {script_html(x.get("sampleScript"))}
      </div>
      <div class="blk"><div class="bh">Deliverable &amp; acceptance</div>
        <div class="deliver">{e(x.get("deliverable",""))}</div>
        <div class="accept"><b>Pass when</b> {e(x.get("acceptance",""))}</div></div>
      <div class="blk live"><div class="bh">Live session focus</div>
        <p><b>Recap</b> {e(b.get("liveRecap",""))}</p>
        <p><b>Misconception</b> {e(b.get("liveMisconception",""))}</p>
        <p class="hot"><b>Hot seat</b> "{e((b.get("liveHotSeat","") or "").strip(chr(34)))}"</p></div>
      <div class="blk full foot">
        <div class="pf"><span class="fl2">Portfolio</span> {e(b.get("portfolio",""))}</div>
        <div class="pf"><span class="fl2">Prereqs &amp; carry-forward</span> {e(b.get("prereqs",""))}</div>
      </div>
    </div>
  </article>'''

def render_phase1():
    base = {wnum(w): w for w in json.load(open(f"{DATA}/phase1_base.json"))}
    enh  = {wnum(w): w for w in json.load(open(f"{DATA}/phase1_enh.json"))}
    cards = "\n".join(card_p1(n, base, enh) for n in range(1, 14))
    nav = navbar([("← Course home","home",True),("Curriculum","cur",False),("Phase 2 →","p2",False)], list(range(1,14)))
    hero = f'''<div class="hero"><div class="wrap">
    <span class="eyebrow hero-tag"><span class="dot"></span>Gambill Data Engineer Track · Launch · Phase 1 of 4</span>
    <h1>Foundations, <span class="thin">week by week.</span></h1>
    <p class="lede">All 13 weeks of Phase 1 (Foundations · bronze depth), with deepened labs — a business framing, step-by-step instructions, linked real datasets, reference docs, and a starter scaffold where the setup earns one. Every lab runs on free, open, deliberately-messy public data; nothing is client data, and no canned tutorial sets.</p>
    <div class="sources"><span class="src">NYC 311 · Socrata</span><span class="src">USGS Earthquakes</span><span class="src">World Bank + OWID</span><span class="src">Chinook · DuckDB</span><span class="src">NOAA GHCN-Daily</span><span class="src">NYC DOHMH Inspections</span></div>
  </div></div>'''
    footer = '''<footer><div class="wrap"><div class="foot-note">
      <span>Launch · Phase 1 — 13 weekly lesson plans · deepened labs on real open data · method per the Gambill DE career videos.</span>
      <span class="mono">Gambill Data Engineer Track</span></div></div></footer>'''
    open(f"{OUTDIR}/{'phase-1.html' if MODE=='site' else 'phase1.html'}","w").write(
        page("Launch · Phase 1 — Weekly Lesson Plans", "", hero, nav, cards, footer))

# ---- Phases 2/3/4 (single source) -------------------------------------------
def card_generic(w, tier, capweeks):
    n = wnum(w); mod = e(w.get("module","")); title = e(w.get("title",""))
    cap = ""
    if capweeks and n >= capweeks[0]:
        cap = capweeks[1]
    modline = f"{mod} · {tier['label']}{cap}"
    lh = w.get("labHours") or 5; ch = w.get("lessonHours") or 4
    role = w.get("projectRole","")
    role_html = f'<div class="project-role"><span class="pl">{tier["roletag"]}</span> {e(role)}</div>' if role else ""
    mirror = w.get("mirrorNote","")
    mirror_html = f'<div class="mirror"><span class="ml2">Adapt to your industry</span> {e(mirror)}</div>' if mirror else ""
    return f'''
  <article class="wk-card" id="w{n}">
    <div class="wk-head">
      <span class="wk-num">W{n:02d}</span>
      <span class="wk-title">{title}</span>
      <span class="wk-mod">{modline}</span>
      <span class="wk-gaps">{gap_chips(w.get("gaps"))}</span>
    </div>
    <div class="framing"><span class="fl">Why this matters</span> {e(w.get("businessFraming",""))}</div>
    {role_html}
    <div class="wk-grid">
      <div class="blk"><div class="bh">Objectives</div><ul>{li(w.get("objectives",[]))}</ul></div>
      <div class="blk"><div class="bh">Concept lessons <span class="hrs">· ~{ch}h</span></div><ul>{li(w.get("lessons",[]))}</ul></div>
      <div class="blk full lab">
        <div class="bh">Hands-on lab <span class="hrs">· ~{lh}h</span></div>
        <p>{e(w.get("labSummary",""))}</p>
        <div class="lab-sub">Step by step</div>
        <ol class="steps">{li(w.get("labSteps",[]))}</ol>
        <div class="lab-sub">Data</div>
        <div class="ds-list">{datasets_html(w.get("datasets"))}</div>
        <div class="lab-sub">Reference material</div>
        <ul class="refs">{refs_html(w.get("referenceMaterials"))}</ul>
        {script_html(w.get("sampleScript"))}
        {mirror_html}
      </div>
      <div class="blk"><div class="bh">Deliverable &amp; acceptance</div>
        <div class="deliver">{e(w.get("deliverable",""))}</div>
        <div class="accept"><b>Pass when</b> {e(w.get("acceptance",""))}</div></div>
      <div class="blk live"><div class="bh">Live session focus</div>
        <p><b>Recap</b> {e(w.get("liveRecap",""))}</p>
        <p><b>Misconception</b> {e(w.get("liveMisconception",""))}</p>
        <p class="hot"><b>Hot seat</b> "{e((w.get("liveHotSeat","") or "").strip(chr(34)))}"</p></div>
      <div class="blk full foot">
        <div class="pf"><span class="fl2">Portfolio</span> {e(w.get("portfolio",""))}</div>
        <div class="pf"><span class="fl2">Prereqs &amp; carry-forward</span> {e(w.get("prereqs",""))}</div>
      </div>
    </div>
  </article>'''

TIER_CSS = {
 "silver": '.wk-head::before{background:var(--silver)}.wk-num{background:var(--silver)}.src.silver{color:var(--silver);background:var(--surface-2)}',
 "gold":   '.wk-head::before{background:var(--gold)}.wk-num{background:var(--gold)}.mirror .ml2{color:var(--gold)}.src.gold{color:var(--gold);background:var(--surface-2)}',
 "launch": '.wk-head::before{background:var(--accent)}.wk-num{background:var(--accent)}.mirror .ml2{color:var(--accent-strong)}.src.launch{color:var(--accent-strong);background:var(--accent-soft)}',
}

NOTE2 = '''<div class="platform-note"><b>What you'll need:</b> this phase runs on <b>Databricks Free Edition</b> — a no-cost, fully-hosted account you create in minutes with an email or Google/Microsoft login; no AWS/Azure/GCP account or credit card required. It is serverless and includes Unity Catalog, Delta Lake, Lakeflow pipelines, Jobs, streaming, and the CLI under fair-use quotas. A few scale-out topics later need the 14-day full-platform trial or a paid/employer workspace &mdash; those are flagged where they appear (see Phase 3).</div>'''
NOTE3 = '''<div class="platform-note"><b>What you'll need:</b> the full <b>Databricks Free Edition</b> (no cloud account or card &mdash; email / Google / Microsoft login) covers most of this phase: Unity Catalog, Delta tuning, Lakeflow pipelines, Jobs, streaming / Auto Loader, Git, and the CLI, under fair-use quotas.
      <div class="pn-cav"><b>Needs a 14-day trial or paid/employer workspace</b> (flagged in-week): multi-pipeline DLT &amp; more than 5 concurrent Job tasks; service principals / machine-to-machine automation (teach the concept, but authenticate CI/CD with a personal access token); CLI &amp; DABs OAuth login (use a PAT instead); Auto Loader from arbitrary external endpoints (ingest from cloud storage, or verify the account); Scala / R (use Python / SQL); and column/row masking on streaming tables &amp; materialized views (apply on managed tables/views).</div>
    </div>'''

PHASECFG = {
 2:{"file":"phase2","tier":{"label":"Phase 2 · silver","css":"silver","roletag":"Project 1 · this week"},
    "cap":(30," · Phase 2 portfolio"),
    "nav":[("← Course home","home",True),("Curriculum","cur",False),("← Phase 1","p1",False),("Phase 3 →","p3",False)],
    "title":"Launch · Phase 2 — Core Data Engineering",
    "h1":'Core data engineering, <span class="thin">one real project.</span>',
    "eyebrow":"Gambill Data Engineer Track · Launch · Phase 2 of 4",
    "lede":'Weeks 14–30 (Core DE · silver depth) build <b>one running medallion pipeline</b> — the portfolio\'s Project 1 — on Databricks Free Edition + Delta. Modeled with SCD2 history, deduplicated into <b>golden provider records (MDM)</b>, run incrementally with quarantine and tests. Worked in healthcare (CMS + NPPES); every lab tells you how to <b>mirror it on your own target industry</b>.',
    "sources":'<span class="src">Databricks Free Edition + Delta</span><span class="src">CMS Price Transparency</span><span class="src">NPPES Provider Registry</span><span class="src silver">Project 1 · Provider Pricing Integrity</span>',
    "note":NOTE2,
    "footnote":"Launch · Phase 2 — 17 weekly lesson plans · one running project → MDM golden records · Databricks Free Edition + Delta."},
 3:{"file":"phase3","tier":{"label":"Phase 3 · gold","css":"gold","roletag":"Project 1 · this week"},
    "cap":(43," · Phase 3 portfolio"),
    "nav":[("← Course home","home",True),("Curriculum","cur",False),("← Phase 2","p2",False),("Phase 4 →","p4",False)],
    "title":"Launch · Phase 3 — Platform & Production",
    "h1":'Platform &amp; production, <span class="thin">one governed system.</span>',
    "eyebrow":"Gambill Data Engineer Track · Launch · Phase 3 of 4",
    "lede":'Weeks 31–43 (Platform &amp; Production · gold depth) turn <b>the same Project 1 pipeline</b> into a governed, observable, continuously-deployed platform: Unity Catalog, Delta tuning, Lakeflow declarative pipelines, streaming with Auto Loader, DABs + CI/CD, PHI governance, and a chosen cloud. Same worked example (CMS + NPPES); every lab still tells you how to <b>mirror it on your own industry</b>.',
    "sources":'<span class="src">Unity Catalog · Lakeflow</span><span class="src">Structured Streaming · Auto Loader</span><span class="src">DABs · CI/CD</span><span class="src">PHI governance</span><span class="src gold">Project 1 · now production-grade</span>',
    "note":NOTE3,
    "footnote":"Launch · Phase 3 — 13 weekly lesson plans · Project 1 productionized on the full Databricks platform."},
 4:{"file":"phase4","tier":{"label":"Phase 4 · launch","css":"launch","roletag":"Launch · this week"},
    "cap":(48," · capstone · W48–50"),
    "nav":[("← Course home","home",True),("Curriculum","cur",False),("← Phase 3","p3",False)],
    "title":"Launch · Phase 4 — Advanced & Launch",
    "h1":'Advanced &amp; launch, <span class="thin">ship your own.</span>',
    "eyebrow":"Gambill Data Engineer Track · Launch · Phase 4 of 4",
    "lede":'Weeks 44–50 take the learner <b>solo</b>: design and ship an <b>independent, governed capstone</b> on their own industry, and get interview-ready. Final portfolio = the healthcare Project 1 (productionized) <b>+</b> the learner\'s own capstone — a two-project story that ends on golden records.',
    "sources":'<span class="src">Your own industry &amp; data</span><span class="src">Architecture Decision Records</span><span class="src">Interview prep · "why not what"</span><span class="src">Capstone + recorded walkthrough</span><span class="src launch">Portfolio · 2 projects</span>',
    "note":"",
    "footnote":"Launch · Phase 4 — Advanced & Launch (W44–50) · architecture, elective, interview prep, and the independent capstone."},
}

def render_phaseN(pnum):
    cfg = PHASECFG[pnum]
    weeks = sorted(json.load(open(f"{DATA}/phase{pnum}.json")), key=wnum)
    nums = [wnum(w) for w in weeks]
    cards = "\n".join(card_generic(w, cfg["tier"], cfg["cap"]) for w in weeks)
    nav = navbar(cfg["nav"], nums)
    hero = f'''<div class="hero"><div class="wrap">
    <span class="eyebrow hero-tag"><span class="dot"></span>{cfg["eyebrow"]}</span>
    <h1>{cfg["h1"]}</h1>
    <p class="lede">{cfg["lede"]}</p>
    <div class="sources">{cfg["sources"]}</div>
    {cfg["note"]}
  </div></div>'''
    footer = f'''<footer><div class="wrap"><div class="foot-note">
      <span>{cfg["footnote"]}</span>
      <span class="mono">Gambill Data Engineer Track</span></div></div></footer>'''
    extra = TIER_CSS[cfg["tier"]["css"]]
    fname = f'phase-{pnum}.html' if MODE == "site" else f'{cfg["file"]}.html'
    open(f"{OUTDIR}/{fname}","w").write(page(cfg["title"], extra, hero, nav, cards, footer))

render_phase1()
for p in (2,3,4):
    render_phaseN(p)
print(f"[{MODE}] rendered phase pages to {OUTDIR}")
