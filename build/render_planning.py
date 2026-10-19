#!/usr/bin/env python3
"""Render the two self-contained in-repo planning pages for the SITE build:
  site/curriculum.html   — program overview: 3 paths, 38-module catalog, 10 gaps, phase map
  site/build-plan.html   — weekly template, the full ~49-week skeleton (from build/data), assessment model
Links are relative so the GitHub Pages site is fully self-contained (no claude.ai artifact dependency).
Usage: python render_planning.py            (writes to ../site)
"""
import html, os, re, json

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "site")
os.makedirs(OUT, exist_ok=True)
CSS = open(os.path.join(HERE, "paths.css")).read()

def e(s): return html.escape(str(s))

# ---- shared chrome ----------------------------------------------------------
def backlinks(active):
    links = [("index.html", "Course home", "home"),
             ("curriculum.html", "Curriculum", "cur"),
             ("build-plan.html", "Build plan", "build"),
             ("phase-1.html", "Phase 1", ""), ("phase-2.html", "Phase 2", ""),
             ("phase-3.html", "Phase 3", ""), ("phase-4.html", "Phase 4", "")]
    out = []
    for href, lab, cls in links:
        if cls == active:
            continue
        c = ' class="home"' if cls == "home" else ""
        out.append(f'<a{c} href="{href}">{lab}</a>')
    return '<div class="backlinks">' + "".join(out) + '</div>'

def page(title, body):
    return f'<title>{title}</title>\n<style>{CSS}\n{EXTRA_CSS}</style>\n{body}'

EXTRA_CSS = r'''
.table-scroll{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius-lg);background:var(--surface)}
table.cat{width:100%;border-collapse:collapse;min-width:720px;font-size:13.5px}
table.cat thead th{text-align:left;font-family:var(--font-mono);font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:600;padding:12px 13px;border-bottom:1px solid var(--line-strong);background:var(--surface);position:sticky;top:0;z-index:2}
table.cat thead th.c{text-align:center;width:72px}
table.cat td{padding:10px 13px;border-bottom:1px solid var(--line);vertical-align:top}
table.cat tr:last-child td{border-bottom:none}
.domrow td{background:var(--surface-2);font-family:var(--font-mono);font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2);font-weight:700;padding:9px 13px}
.domrow .dn{color:var(--accent-strong)}
.mc{font-family:var(--font-mono);font-size:11.5px;color:var(--muted);font-weight:600}
.mn{font-weight:640;color:var(--ink)}
.mn .g{display:inline-block;font-family:var(--font-mono);font-size:9.5px;font-weight:700;letter-spacing:.04em;color:var(--warn);background:var(--warn-soft);border-radius:3px;padding:1px 5px;margin-left:6px;vertical-align:middle}
td.c{text-align:center}
.fit{display:inline-block;min-width:28px;font-family:var(--font-mono);font-size:10.5px;font-weight:700;border-radius:4px;padding:3px 7px}
.fit-core{background:var(--good-soft);color:var(--good)}
.fit-comp{background:var(--warn-soft);color:var(--warn)}
.fit-elec{background:var(--blue-soft);color:var(--blue-strong)}
.fit-skip{background:var(--skip-soft);color:var(--skip)}
.legend{display:flex;flex-wrap:wrap;gap:14px;margin-top:14px;font-size:12.5px;color:var(--muted)}
.legend span{display:inline-flex;align-items:center;gap:6px}.legend .fit{min-width:0}
.anatomy{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}
.acard{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);padding:15px 16px}
.acard .ak{font-family:var(--font-mono);font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-strong)}
.acard h4{font-size:.96rem;font-weight:680;margin-top:6px}.acard p{font-size:12.5px;color:var(--muted);margin-top:5px;line-height:1.45}
table.skel{width:100%;border-collapse:collapse;min-width:760px;font-size:13px}
table.skel thead th{text-align:left;font-family:var(--font-mono);font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-weight:600;padding:11px 13px;border-bottom:1px solid var(--line-strong);background:var(--surface);position:sticky;top:0;z-index:2}
table.skel td{padding:9px 13px;border-bottom:1px solid var(--line);vertical-align:top}
table.skel .wc{font-family:var(--font-mono);font-weight:700;color:var(--ink);white-space:nowrap;width:52px}
table.skel .mc2{font-family:var(--font-mono);font-size:11px;color:var(--muted);white-space:nowrap;width:62px}
table.skel .tc{font-weight:600;color:var(--ink)}
.band td{font-family:var(--font-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;padding:10px 13px}
.band.b td{background:var(--bronze-soft);color:var(--bronze)}
.band.s td{background:#E4E8EC;color:var(--silver)}
.band.g td{background:#F1E9CE;color:var(--gold)}
.band.l td{background:var(--accent-soft);color:var(--accent-strong)}
@media (prefers-color-scheme:dark){.band.s td{background:#1E2831}.band.g td{background:#29230F}}
:root[data-theme="dark"] .band.s td{background:#1E2831}:root[data-theme="dark"] .band.g td{background:#29230F}
.port td{background:var(--surface-2);font-size:12.5px;color:var(--accent-ink);font-weight:600;padding:9px 13px}
.rubric{list-style:none;margin:14px 0 0;padding:0}
.rubric li{display:flex;gap:12px;padding:9px 0;border-bottom:1px solid var(--line);font-size:13.5px}
.rubric li:last-child{border-bottom:none}
.rubric .rk{font-family:var(--font-mono);font-size:11px;font-weight:700;color:var(--accent-strong);flex:none;width:92px;text-transform:uppercase;letter-spacing:.04em;padding-top:2px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);padding:22px 24px}
.card h4{font-size:1.05rem;font-weight:730}.card>p{color:var(--muted);font-size:13.5px;margin-top:8px}
.gates{list-style:none;margin:14px 0 0;padding:0;display:flex;flex-direction:column;gap:10px}
.gates li{font-size:13.5px;color:var(--ink-2);padding-left:24px;position:relative;line-height:1.45}
.gates li::before{content:"\25C6";position:absolute;left:0;color:var(--accent);font-size:10px;top:3px}
@media (max-width:860px){.two{grid-template-columns:1fr}}
'''

# ---- module catalog ---------------------------------------------------------
# (code, name, weeks, launch, bridgeA, bridgeS, gaptag)
CATALOG = [
 ("D0","Orientation & tooling",[
   ("M00","Dev environment, CLI & Git","1","core","core","skip",""),
   ("M01","The DE mental model & data lifecycle","1","core","core","core",""),
 ]),
 ("D1","Programming — Python",[
   ("M02","Python fundamentals for DE","3","core","core","skip",""),
   ("M03","Python for data — files, APIs, pandas","2","core","core","comp",""),
   ("M04","Software engineering hygiene","1","core","core","skip",""),
 ]),
 ("D2","SQL & relational",[
   ("M05","SQL fundamentals","2","core","skip","core",""),
   ("M06","Advanced SQL — windows, CTEs, plans","2","core","comp","core",""),
   ("M07","Relational theory & normalization","1","core","comp","core",""),
 ]),
 ("D3","Data modeling & warehousing · closes G2",[
   ("M08","Dimensional modeling — grain, facts, dims","2","core","core","core",""),
   ("M09","SCD & history tracking","1","core","core","core","G3"),
   ("M10","Warehouse/lakehouse & the gold layer","1","core","core","core",""),
   ("M11","Reference data, crosswalks, MDM & entity resolution","2","core","core","core","G2"),
   ("M12","Data Vault & advanced patterns","1","elec","elec","elec",""),
 ]),
 ("D4","Pipelines & ingestion · closes G3",[
   ("M13","ETL vs ELT, batch vs incremental","1","core","core","core",""),
   ("M14","Ingestion patterns & source systems","1","core","core","core",""),
   ("M15","Medallion architecture","1","core","core","core",""),
   ("M16","CDC, watermarks, snapshots & backfills","2","core","core","core","G3"),
 ]),
 ("D5","Distributed compute — Spark · closes G7",[
   ("M17","Spark fundamentals & the PySpark DataFrame API","2","core","core","core",""),
   ("M18","Spark internals — partitions, shuffles, skew","1","core","core","core",""),
   ("M19","Performance tuning & cost","1","core","core","core",""),
 ]),
 ("D6","Lakehouse platform — Databricks · closes G5",[
   ("M20","Delta Lake & table formats","1","core","core","core",""),
   ("M21","Databricks & Unity Catalog fundamentals","1","core","core","core",""),
   ("M22","Declarative pipelines (Lakeflow/DLT) & Jobs","2","core","core","core",""),
   ("M23","Structured Streaming semantics","2","core","core","core","G5"),
 ]),
 ("D7","Data quality, testing & observability · closes G4",[
   ("M24","Data quality — expectations, quarantine, reconciliation","2","core","core","core","G4"),
   ("M25","Testing taxonomy for data — pytest","1","core","core","core",""),
   ("M26","Observability, monitoring, SLAs & lineage","1","core","core","core",""),
 ]),
 ("D8","DevOps & engineering practice · closes G6",[
   ("M27","Git deep — branching, PRs, review","1","core","core","skip",""),
   ("M28","CI/CD for data — Actions, env promotion","1","core","core","comp",""),
   ("M29","Databricks Asset Bundles (DABs) & IaC","1","core","core","core","G6"),
 ]),
 ("D9","Governance, security & cloud · closes G8",[
   ("M30","Governance & security — UC RBAC, masking, PII/PHI","1","core","core","core","G8"),
   ("M31","Cloud foundations — Azure or AWS track","1","core","core","comp",""),
 ]),
 ("D10","Architecture & AI-assisted DE · closes G9",[
   ("M32","Architecture decision-making","1","core","core","core","G9"),
   ("M33","AI-assisted data engineering","1","elec","elec","elec",""),
 ]),
 ("D11","Career & proof · closes G1 · G10",[
   ("M34","Communicating your engineering work","◇","core","core","core","G10"),
   ("M35","Portfolio engineering","◇","core","core","core",""),
   ("M36","Interview prep — SQL, design, behavioral","2","core","core","core","G1"),
   ("M37","Capstone — end-to-end governed data product","3–4","core","core","core",""),
 ]),
]
FITLABEL = {"core":"core","comp":"comp","elec":"elec","skip":"skip"}
def fitcell(v): return f'<span class="fit fit-{v}">{FITLABEL[v]}</span>'

def catalog_html():
    rows = []
    for dn, dt, mods in CATALOG:
        rows.append(f'<tr class="domrow"><td colspan="5"><span class="dn">{e(dn)}</span> &nbsp; {e(dt)}</td></tr>')
        for code, name, wk, la, ba, bs, gap in mods:
            g = f' <span class="g">{gap}</span>' if gap else ""
            rows.append(
              f'<tr><td><span class="mc">{code}</span> · <span class="mn">{e(name)}{g}</span></td>'
              f'<td class="c mc">{wk}</td>'
              f'<td class="c">{fitcell(la)}</td><td class="c">{fitcell(ba)}</td><td class="c">{fitcell(bs)}</td></tr>')
    return "".join(rows)

GAPS = [
 ("G1","Concept vs. application — can't explain own code or defend a tradeoff"),
 ("G2","Modeling fundamentals — grain, facts/dims, reference data"),
 ("G3","Incremental, CDC & history — overwrite isn't a bronze strategy"),
 ("G4","Data quality & testing — schema, reconciliation, quarantine, taxonomy"),
 ("G5","Streaming semantics — triggers, state, keys, composite-key dedup"),
 ("G6","Dev workflow — Git → CI/CD → DABs, no manual drift"),
 ("G7","Spark intuition — scale, shuffle, skew, when to tune"),
 ("G8","Governance designed in, not bolted on — RBAC, masking, PII/PHI"),
 ("G9","Architecture decisions — choose and defend, don't list tools"),
 ("G10","Communicating the work — a narrative for interviews & stakeholders"),
]
def gaps_html():
    return "".join(f'<div class="gap"><span class="idx">{g}</span><div class="gt">{t}</div></div>' for g,t in GAPS)

PHASECARDS = [
 ("b","Phase 1","Foundations","Weeks 1–13 · bronze","phase-1.html","CLI/Git, Python, SQL, relational modeling — real-data labs from day one."),
 ("s","Phase 2","Core data engineering","Weeks 14–30 · silver","phase-2.html","One running medallion pipeline → SCD2, MDM golden records, incremental, DQ."),
 ("g","Phase 3","Platform & production","Weeks 31–43 · gold","phase-3.html","Unity Catalog, Lakeflow, streaming, DABs/CI-CD, PHI governance — productionized."),
 ("l","Phase 4","Advanced & launch","Weeks 44–50","phase-4.html","Architecture, elective, interview prep, and your own independent capstone."),
]
def phasecards_html():
    return "".join(
      f'<a class="phcard {c}" href="{u}"><div class="pk">{k}</div><h4>{t}</h4><div class="pd">{sub}</div>'
      f'<div class="pd" style="color:var(--ink-2);margin-top:8px">{d}</div></a>'
      for c,k,t,sub,u,d in PHASECARDS)

curriculum_body = f'''
<div class="hero"><div class="wrap">
  <span class="eyebrow hero-tag"><span class="dot"></span>Gambill Data Engineer Track · Curriculum Architecture</span>
  <h1>Zero to Data Engineer, <span class="thin">by design.</span></h1>
  <p class="lede">A modular curriculum with three entry paths, a neutral conceptual core, and a deep Databricks lakehouse track — engineered backward from the ten gaps that actually stall people. Data engineering is not "writing pipelines"; it is designing reliable <b>data products</b> you can defend.</p>
  {backlinks("cur")}
</div></div>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Three ways in</span><h2>The paths</h2>
  <p>One shared module catalog, three sequencings — each standalone, all ending on a defensible portfolio.</p></div>
  <div class="paths">
    <div class="pcard launch"><span class="k">Path 01 — Launch</span><h3>Ground up</h3><div class="for">No data experience (maybe Excel)</div>
      <p>The full ~50-week course across four phases, ending on a governed capstone.</p><a class="go" href="phase-1.html">Start at Phase 1 →</a></div>
    <div class="pcard bridge"><span class="k">Path 02 — Bridge</span><h3>Cross over</h3><div class="for">Analysts &amp; software engineers</div>
      <p>About five months, less if the diagnostic lets you skip more; it routes you to the analyst or SWE variant.</p><a class="go" href="bridge.html">See the Bridge path →</a></div>
    <div class="pcard sharpen"><span class="k">Path 03 — Sharpen</span><h3>Fill the gaps</h3><div class="for">Working data engineers</div>
      <p>A self-diagnostic against the ten gaps, plus eight pre-built bundles.</p><a class="go" href="sharpen.html">See the Sharpen path →</a></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">The building blocks</span><h2>Module catalog</h2>
  <p>38 units across 12 domains. The neutral core is taught first; the Databricks/lakehouse track is where it gets implemented deeply. Fit columns show how each path treats a module.</p></div>
  <div class="table-scroll"><table class="cat">
    <thead><tr><th>Module</th><th class="c">Weeks</th><th class="c">Launch</th><th class="c">Bridge·A</th><th class="c">Bridge·S</th></tr></thead>
    <tbody>{catalog_html()}</tbody>
  </table></div>
  <div class="legend">
    <span>{fitcell("core")} required</span><span>{fitcell("comp")} condensed / review</span>
    <span>{fitcell("elec")} optional deepening</span><span>{fitcell("skip")} assumed known</span>
    <span class="mono" style="color:var(--muted)">◇ woven throughout, not a fixed week</span>
    <span class="mn"><span class="g">Gx</span> flagship gap-closer</span>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">The Launch path</span><h2>Phase by phase</h2>
  <p>Bronze → silver → gold → launch. Each phase ends in a portfolio artifact; the path ends in a governed data product.</p></div>
  <div class="phases">{phasecards_html()}</div>
</div></section>

<section style="border-bottom:none"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Why it's built this way</span><h2>Ten gaps, closed on purpose</h2>
  <p>Mined from hundreds of real coaching calls — where people with certs and theory still stall. Every module is tagged to the gap it closes.</p></div>
  <div class="gaps">{gaps_html()}</div>
</div></section>

<footer><div class="wrap"><div class="foot-note">
  <span>The Gambill Data Engineer Track · Curriculum Architecture · 3 paths · 38 modules · 10 gaps.</span>
  <span class="mono">Gambill Data Engineering</span></div></div></footer>'''

# ---- build-plan skeleton (from build/data) ----------------------------------
P1_TITLES = {  # W1 + phase1_base gives 2-13; keep short titles
 1:("M00","Dev environment, CLI & Git"),
}
def load_phase(fn):
    return json.load(open(os.path.join(HERE, "data", fn)))
def wn(w):
    m = re.search(r"\d+", str(w.get("week",""))); return int(m.group()) if m else 0
def mcode(w):
    m = re.search(r"M\d{2}", str(w.get("module",""))); return m.group() if m else str(w.get("module",""))
def shorttitle(t):
    t = str(t)
    for sep in (" — ", " (", " - "):
        if sep in t: t = t.split(sep)[0]
    return t.strip()

def skeleton_rows():
    rows = []
    # Phase 1
    rows.append('<tr class="band b"><td colspan="3">Phase 1 · Foundations · bronze · Weeks 1–13</td></tr>')
    p1 = {wn(w): w for w in load_phase("phase1_base.json")}
    p1[1] = {"week":"W1","module":"M00","title":"Dev environment, CLI & Git"}
    for n in range(1, 14):
        w = p1[n]
        rows.append(f'<tr><td class="wc">{n}</td><td class="mc2">{mcode(w)}</td><td class="tc">{e(shorttitle(w["title"]))}</td></tr>')
    rows.append('<tr class="port"><td colspan="3">◆ Phase 1 portfolio → a SQL + Python analytics project on real data, in a clean, documented repo.</td></tr>')
    # Phases 2-4
    bands = {2:("s","Core data engineering","silver","14–30"),3:("g","Platform & production","gold","31–43"),4:("l","Advanced & launch","job-ready","44–50")}
    ports = {2:"a batch medallion pipeline (bronze→gold) with SCD2 history, MDM, and DQ checks.",
             3:"a production incremental + streaming pipeline with CI/CD, tests, and Unity Catalog governance.",
             4:"the capstone data product + a recorded walkthrough you can defend in interviews."}
    for p in (2,3,4):
        cls, nm, tier, rng = bands[p]
        rows.append(f'<tr class="band {cls}"><td colspan="3">Phase {p} · {nm} · {tier} · Weeks {rng}</td></tr>')
        for w in sorted(load_phase(f"phase{p}.json"), key=wn):
            rows.append(f'<tr><td class="wc">{wn(w)}</td><td class="mc2">{mcode(w)}</td><td class="tc">{e(shorttitle(w["title"]))}</td></tr>')
        label = "Capstone" if p == 4 else f"Phase {p} portfolio"
        rows.append(f'<tr class="port"><td colspan="3">◆ {label} → {ports[p]}</td></tr>')
    return "".join(rows)

ANATOMY = [
 ("Field 01","Header & context","Week number, title, module(s), phase/depth tier, and the gap(s) it closes."),
 ("Field 02","Learning objectives","3–5 measurable “by end of week you can…” statements. The bar for done."),
 ("Field 03","Concept lessons","Self-paced topics with rough hours — scaffolding for the lab, not the point."),
 ("Field 04","Hands-on lab","The build task on real data: steps, dataset links, references, a starter scaffold."),
 ("Field 05","Deliverable + acceptance","What they submit (code + a “why” note) and the criteria that make it a pass."),
 ("Field 06","Live session focus","Recap point, the likely misconception, and the “defend your decision” prompt."),
 ("Field 07","Portfolio linkage","Whether the week feeds the phase artifact or the capstone."),
 ("Field 08","Prereqs & carry-forward","What it assumes and what later weeks build on it."),
]
def anatomy_html():
    return "".join(f'<div class="acard"><span class="ak">{k}</span><h4>{e(n)}</h4><p>{e(p)}</p></div>' for k,n,p in ANATOMY)

buildplan_body = f'''
<div class="hero"><div class="wrap">
  <span class="eyebrow hero-tag"><span class="dot"></span>Gambill Data Engineer Track · Launch · Build Plan</span>
  <h1>The course, <span class="thin">week by week.</span></h1>
  <p class="lede">How the Launch path is produced: a fixed weekly template, the complete ~49-week skeleton, and the assessment model. Every week is one card with eight fields; the full detail lives in the four phase pages.</p>
  {backlinks("build")}
</div></div>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Anatomy of a week</span><h2>The weekly lesson-plan template</h2>
  <p>Every week fills these eight fields. The structure enforces the spine: nothing is “learned” until it is built (lab) and defended (deliverable + live session).</p></div>
  <div class="anatomy">{anatomy_html()}</div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">The full map</span><h2>~49-week skeleton</h2>
  <p>Every week mapped to its module and title. Phase bands mark depth; portfolio rows mark where a shippable artifact is assembled. Open any phase page for the full weekly detail.</p></div>
  <div class="table-scroll"><table class="skel">
    <thead><tr><th>Wk</th><th>Module</th><th>Title</th></tr></thead>
    <tbody>{skeleton_rows()}</tbody>
  </table></div>
</div></section>

<section style="border-bottom:none"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Making "done" mean something</span><h2>Assessment &amp; portfolio gates</h2>
  <p>Every deliverable is graded on the same four-part rubric; each phase targets a shippable artifact — a checkpoint, not a turnstile.</p></div>
  <div class="two">
    <div class="card"><h4>The weekly rubric</h4><p>The “reasoning” and “defense” lines are where the concept-vs-application gap (G1) is enforced.</p>
      <ul class="rubric">
        <li><span class="rk">Correctness</span><span>Does it meet the acceptance criteria and actually run?</span></li>
        <li><span class="rk">Craft</span><span>Clean, readable, idiomatic — would it survive code review?</span></li>
        <li><span class="rk">Reasoning</span><span>Does the “why” note justify the key decisions and tradeoffs?</span></li>
        <li><span class="rk">Defense</span><span>Can they explain and defend it live, under questioning?</span></li>
      </ul></div>
    <div class="card"><h4>Phase checkpoints</h4><p>Progression stays open — learners advance and catch up as time allows; the artifact is the proof, not a gate.</p>
      <ul class="gates">
        <li><b>Phase 1</b> — SQL + Python analytics project in a clean, documented repo.</li>
        <li><b>Phase 2</b> — batch medallion pipeline with SCD2 history, MDM, and DQ checks.</li>
        <li><b>Phase 3</b> — production incremental + streaming pipeline with CI/CD and governance.</li>
        <li><b>Capstone</b> — governed end-to-end data product + a recorded, defensible walkthrough.</li>
      </ul></div>
  </div>
</div></section>

<footer><div class="wrap"><div class="foot-note">
  <span>The Gambill Data Engineer Track · Launch build plan · weekly template + ~49-week skeleton.</span>
  <span class="mono">Gambill Data Engineering</span></div></div></footer>'''

open(os.path.join(OUT, "curriculum.html"), "w").write(page("Curriculum · The Gambill Data Engineer Track", curriculum_body))
open(os.path.join(OUT, "build-plan.html"), "w").write(page("Build Plan · The Gambill Data Engineer Track", buildplan_body))
print("wrote site/curriculum.html and site/build-plan.html")
