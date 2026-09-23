#!/usr/bin/env python3
"""Render the hub (landing) + Bridge + Sharpen path pages.
Usage: python render_paths.py <artifact|site>
- hub outbound links open in the SAME tab (no target=_blank)
- Bridge/Sharpen carry a 'Course home' backlink
- module chips deep-link to their lesson week (mode-aware)."""
import html, sys, os

MODE = sys.argv[1] if len(sys.argv) > 1 else "artifact"
HERE = os.path.dirname(__file__)
OUTDIR = os.path.join(HERE, "..", ("artifact_out" if MODE == "artifact" else "site"))
os.makedirs(OUTDIR, exist_ok=True)

ART = {
 "home":"https://claude.ai/code/artifact/bbf75ac1-4993-40ea-a08f-d488d2b5acf4",
 "cur":"https://claude.ai/code/artifact/085627d8-ff0b-4b9a-a7cf-c83107cb71bf",
 "build":"https://claude.ai/code/artifact/18e529a8-700b-447d-bae8-c4c0a3035e94",
 "p1":"https://claude.ai/code/artifact/59592bdb-3bce-4336-ba9a-69df5f936caf",
 "p2":"https://claude.ai/code/artifact/d064d266-fe89-46d3-9b3a-f9094a6c2397",
 "p3":"https://claude.ai/code/artifact/4f4034d2-8cab-4c0b-8d9d-bc6391654d4f",
 "p4":"https://claude.ai/code/artifact/6fc11b3c-5ca1-4211-9672-58249453a740",
 "bridge":"https://claude.ai/code/artifact/52d3eae7-e2ab-4e71-852c-4e42e08891e3",
 "sharpen":"https://claude.ai/code/artifact/a19e836b-6bd4-4f00-9217-7a625373b993",
}
# site mode: phases/paths/hub are local files; the two planning docs stay as artifacts (not in repo)
SITE = dict(ART)
SITE.update({"home":"index.html","p1":"phase-1.html","p2":"phase-2.html","p3":"phase-3.html","p4":"phase-4.html",
             "bridge":"bridge.html","sharpen":"sharpen.html"})
L = ART if MODE == "artifact" else SITE

MOD={
 'M00':'Dev env, CLI & Git','M01':'DE mental model & lifecycle','M02':'Python fundamentals',
 'M03':'Python for data (pandas, APIs)','M04':'Software engineering hygiene','M05':'SQL fundamentals',
 'M06':'Advanced SQL','M07':'Relational theory & normalization','M08':'Dimensional modeling',
 'M09':'SCD & history tracking','M10':'Lakehouse / gold modeling','M11':'MDM & entity resolution',
 'M12':'Data Vault (elective)','M13':'ETL vs ELT, batch vs incremental','M14':'Ingestion patterns',
 'M15':'Medallion architecture','M16':'CDC, watermarks & backfills','M17':'Spark & PySpark',
 'M18':'Spark internals','M19':'Performance tuning & cost','M20':'Delta Lake & table formats',
 'M21':'Databricks & Unity Catalog','M22':'Declarative pipelines & Jobs','M23':'Structured Streaming',
 'M24':'Data quality & quarantine','M25':'Testing taxonomy','M26':'Observability & lineage',
 'M27':'Git deep','M28':'CI/CD for data','M29':'DABs & IaC','M30':'Governance & security',
 'M31':'Cloud foundations (Azure/AWS)','M32':'Architecture decision-making','M33':'AI-assisted DE (elective)',
 'M34':'Communicating your work','M35':'Portfolio engineering','M36':'Interview prep','M37':'Capstone',
}
MW={  # module -> (phase key, week anchor)
 'M00':('p1','w1'),'M01':('p1','w2'),'M02':('p1','w3'),'M03':('p1','w6'),'M04':('p1','w8'),'M05':('p1','w9'),
 'M06':('p1','w11'),'M07':('p1','w13'),'M08':('p2','w14'),'M09':('p2','w16'),'M10':('p2','w17'),'M11':('p2','w18'),
 'M12':('p4','w45'),'M13':('p2','w20'),'M14':('p2','w21'),'M15':('p2','w22'),'M16':('p2','w23'),'M17':('p2','w25'),
 'M18':('p2','w27'),'M19':('p3','w31'),'M20':('p3','w31'),'M21':('p3','w32'),'M22':('p3','w33'),'M23':('p3','w35'),
 'M24':('p2','w28'),'M25':('p2','w30'),'M26':('p3','w37'),'M27':('p3','w38'),'M28':('p3','w39'),'M29':('p3','w40'),
 'M30':('p3','w41'),'M31':('p3','w42'),'M32':('p4','w44'),'M33':('p4','w45'),'M34':('p4','w46'),'M35':('p4','w46'),
 'M36':('p4','w46'),'M37':('p4','w48'),
}
WKLABEL={'M02':'W3–5','M03':'W6–7','M05':'W9–10','M06':'W11–12','M08':'W14–15','M11':'W18–19','M16':'W23–24',
 'M17':'W25–26','M22':'W33–34','M23':'W35–36','M36':'W46–47','M37':'W48–50'}
def e(s): return html.escape(s)
def wkref(m): return WKLABEL[m] if m in WKLABEL else "W"+MW[m][1][1:]
def chip(m):
    key, anch = MW[m]
    return (f'<a class="mchip" href="{L[key]}#{anch}">'
            f'<b>{m}</b> {e(MOD[m])} <span class="wk">{wkref(m)}</span></a>')
def chips(ms): return "".join(chip(m) for m in ms)

CSS=open(os.path.join(HERE,"paths.css")).read()

def page(title, body): return f'<title>{title}</title>\n<style>{CSS}</style>\n{body}'

# ---------- BRIDGE ----------
analyst_stages=[("Close the engineering gap","~5 wks",['M00','M01','M02','M03','M04']),
 ("Core data engineering","~8 wks",['M06','M07','M08','M09','M10','M11','M13','M14','M15','M16','M17','M18','M24','M25']),
 ("Platform & production","~6 wks",['M20','M21','M22','M23','M26','M28','M29','M30','M31']),
 ("Launch","~4 wks",['M32','M12','M36','M37'])]
swe_stages=[("Close the data gap","~5 wks",['M01','M05','M06','M07']),
 ("Model, pipeline & Spark","~8 wks",['M08','M09','M10','M11','M13','M14','M15','M16','M17','M18','M24','M25','M26']),
 ("Platform & production","~6 wks",['M20','M21','M22','M23','M28','M29','M30','M31']),
 ("Launch","~4 wks",['M32','M33','M36','M37'])]
def stages_html(stages):
    return "".join(f'<div class="stage"><div class="st"><span>{e(n)}</span><span class="wks">{e(w)}</span></div><div class="chipwrap">{chips(ms)}</div></div>' for n,w,ms in stages)

def backlinks(active):
    # Course home first, then curriculum + the four phases; same-tab.
    out=[f'<a class="home" href="{L["home"]}">Course home</a>',
         f'<a href="{L["cur"]}">Curriculum overview</a>']
    for k,lab in (("p1","Phase 1"),("p2","Phase 2"),("p3","Phase 3"),("p4","Phase 4")):
        out.append(f'<a href="{L[k]}">{lab}</a>')
    return '<div class="backlinks">'+"".join(out)+'</div>'

bridge_body=f'''
<div class="hero"><div class="wrap">
  <span class="eyebrow hero-tag"><span class="dot"></span>Gambill Data Engineer Track · Path 02 — Bridge</span>
  <h1>Cross over into DE. <span class="thin">4–6 months.</span></h1>
  <p class="lede">Bridge is for people who already work with data — <b>analysts</b> and <b>software engineers</b> — who want to become data engineers. You skip what you already own and go deep on the rest, so it is faster than starting from zero. A short placement diagnostic routes you to the right variant; both converge on the same lakehouse core and capstone.</p>
  {backlinks("bridge")}
</div></div>
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Before week 1</span><h2>Placement diagnostic</h2>
  <p>~30 minutes. Four short tasks decide which variant you enter, because an analyst and an SWE arrive with mirror-image strengths.</p></div>
  <div class="diag"><h3>Four tasks</h3><ol>
    <li>Write a query with a window function and explain what it computes. <span class="mono">→ tests SQL depth</span></li>
    <li>Given a messy CSV and an API, write a small Python script that loads and reconciles them. <span class="mono">→ tests Python / engineering</span></li>
    <li>Model a simple business process into facts &amp; dimensions and justify the grain. <span class="mono">→ tests modeling</span></li>
    <li>Walk through how you would branch, PR, test, and deploy a change. <span class="mono">→ tests dev workflow</span></li>
  </ol></div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Two variants</span><h2>Your track</h2>
  <p>Each module below links to its real lesson week in the Launch phase pages — the content is identical, you just take a different route through it. Chips show the module and the week it lives in.</p></div>
  <div class="split">
    <div class="variant a">
      <h3>Analyst → DE</h3><div class="who">Strong SQL &amp; business sense; lighter on programming, distributed compute, and engineering practice.</div>
      <div class="meta"><div><div class="mv tnum">~23 wks</div><div class="ml">Duration</div></div><div><div class="mv">Variant A</div><div class="ml">Route</div></div></div>
      <div class="haveskip">
        <div class="row"><span class="lab have">You have</span><span>SQL, aggregation, business framing, BI reporting instincts.</span></div>
        <div class="row"><span class="lab skip">Skip</span><span><b>M05</b> SQL fundamentals (proven in the diagnostic); <b>M06</b> becomes a quick review.</span></div>
      </div>
      {stages_html(analyst_stages)}
    </div>
    <div class="variant s">
      <h3>SWE → DE</h3><div class="who">Strong Python, Git, CI/CD; lighter on data modeling, SQL depth, warehousing, and DQ discipline.</div>
      <div class="meta"><div><div class="mv tnum">~23 wks</div><div class="ml">Duration</div></div><div><div class="mv">Variant S</div><div class="ml">Route</div></div></div>
      <div class="haveskip">
        <div class="row"><span class="lab have">You have</span><span>Python, Git/PRs, testing, CI/CD, packaging.</span></div>
        <div class="row"><span class="lab skip">Skip</span><span><b>M00</b> CLI/Git basics, <b>M02</b> Python fundamentals, <b>M27</b> Git deep — already owned.</span></div>
      </div>
      {stages_html(swe_stages)}
    </div>
  </div>
  <div class="converge"><b>Both variants converge</b> on the same spine — the Databricks lakehouse core (<b>M20–M23</b>), data quality (<b>M24–M26</b>), governance (<b>M30</b>), architecture (<b>M32</b>), and the capstone (<b>M36–M37</b>) — and finish on a defensible portfolio project ending in golden records.</div>
</div></section>
<footer><div class="wrap"><div class="foot-note">
  <span>The Gambill Data Engineer Track · Bridge — analyst &amp; SWE crossover.</span>
  <span class="mono">Gambill Data Engineering</span></div></div></footer>'''

# ---------- SHARPEN ----------
gap_map=[("G1","Can you explain <em>why</em> you built something the way you did?",['M32','M34','M36']),
 ("G2","Do you choose grain deliberately?",['M08','M09','M10','M11']),
 ("G3","Is overwrite ever your bronze strategy?",['M15','M16']),
 ("G4","Do you have a real testing taxonomy?",['M24','M25','M26']),
 ("G5","Could you dedup a composite key in a stream?",['M23']),
 ("G6","Do manual workspace changes ever survive deploy?",['M27','M28','M29']),
 ("G7","Can you read a Spark UI and act on it?",['M17','M18','M19']),
 ("G8","Is governance designed in, or bolted on?",['M21','M30']),
 ("G9","Can you defend an architecture, not just name tools?",['M32']),
 ("G10","Can you narrate your work to a stakeholder?",['M34','M35','M36'])]
def gapdiag_html():
    return "".join(f'<li><b>{g}</b> {q} <span class="mono">→ {" ".join(ms)}</span></li>' for g,q,ms in gap_map)
bundles=[("Incremental & CDC Mastery","closes G3",['M13','M15','M16','M23'],"Kill the full-refresh habit: watermarks, snapshots, backfills, idempotency."),
 ("Spark Performance & Cost","closes G7",['M17','M18','M19'],"Build the scale/shuffle instinct and know when tuning is actually worth it."),
 ("Modeling Depth","closes G2",['M08','M09','M10','M11','M12'],"Grain, history, semantic layer, MDM, and Data Vault when it earns its place."),
 ("DQ, Testing & Observability","closes G4",['M24','M25','M26'],"Expectations, quarantine, reconciliation, and the full test taxonomy."),
 ("DevOps for Data","closes G6",['M27','M28','M29'],"Git → DABs → CI/CD with no manual drift and clean env promotion."),
 ("Governance & Security","closes G8",['M21','M30'],"Unity Catalog design, RBAC, masking/hashing, PII/PHI, service identities."),
 ("Streaming Semantics","closes G5",['M23','M16'],"Triggers, state, keys, idempotency — and why streaming is not real-time."),
 ("Architecture & Communication","closes G1 · G9 · G10",['M32','M34','M35','M36'],"Choose and defend approaches; narrate the work to any audience.")]
def bundles_html():
    return "".join(f'<div class="bundle"><h4>{e(n)}</h4><div class="gr">{e(gr)}</div><p>{b}</p><div class="chipwrap">{chips(ms)}</div></div>' for n,gr,ms,b in bundles)

sharpen_body=f'''
<div class="hero"><div class="wrap">
  <span class="eyebrow hero-tag"><span class="dot"></span>Gambill Data Engineer Track · Path 03 — Sharpen</span>
  <h1>Close the gaps. <span class="thin">On your schedule.</span></h1>
  <p class="lede">Sharpen is for working data engineers who "missed things along the way." Start with the self-diagnostic against the ten recurring gaps, then take individual modules or a pre-built bundle. Every unit stands alone and links straight to its lesson — no need to have done the earlier modules.</p>
  {backlinks("sharpen")}
</div></div>
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Start here</span><h2>Self-diagnostic — rate yourself 1–5 on each gap</h2>
  <p>Each gap maps to the modules that close it. Pick the ones you score low on; the module codes link to their lessons.</p></div>
  <div class="diag cols"><ol>{gapdiag_html()}</ol></div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Pre-built bundles</span><h2>Or grab a bundle</h2>
  <p>Eight curated gap-clusters. Each chip opens the real lesson week in the Launch phase pages.</p></div>
  <div class="bundles">{bundles_html()}</div>
</div></section>
<footer><div class="wrap"><div class="foot-note">
  <span>The Gambill Data Engineer Track · Sharpen — gap-fill for working DEs.</span>
  <span class="mono">Gambill Data Engineering</span></div></div></footer>'''

# ---------- LANDING (hub) ----------
GAPS=[("G1","Explaining &amp; defending your own work"),("G2","Modeling fundamentals — grain, facts, dims"),
 ("G3","Incremental, CDC &amp; history"),("G4","Data quality &amp; the testing taxonomy"),
 ("G5","Streaming semantics (≠ real-time)"),("G6","Dev workflow — Git → CI/CD → DABs"),
 ("G7","Spark intuition — scale, shuffles, skew"),("G8","Governance designed in, not bolted on"),
 ("G9","Architecture decisions you can defend"),("G10","Communicating the work to stakeholders")]
def gaps_html(): return "".join(f'<div class="gap"><span class="idx">{g}</span><div class="gt">{t}</div></div>' for g,t in GAPS)
PHASECARDS=[("b","Phase 1","Foundations","Weeks 1–13 · bronze","p1","CLI/Git, Python, SQL, relational modeling — real-data labs from day one."),
 ("s","Phase 2","Core data engineering","Weeks 14–30 · silver","p2","One running medallion pipeline → SCD2, MDM golden records, incremental, DQ."),
 ("g","Phase 3","Platform &amp; production","Weeks 31–43 · gold","p3","Unity Catalog, Lakeflow, streaming, DABs/CI-CD, PHI governance — productionized."),
 ("l","Phase 4","Advanced &amp; launch","Weeks 44–50","p4","Architecture, elective, interview prep, and your own independent capstone.")]
def phasecards_html():
    return "".join(f'<a class="phcard {c}" href="{L[k]}"><div class="pk">{kk}</div><h4>{t}</h4><div class="pd">{sub}</div><div class="pd" style="color:var(--ink-2);margin-top:8px">{d}</div></a>' for c,kk,t,sub,k,d in PHASECARDS)

landing_body=f'''
<div class="hero"><div class="wrap">
  <span class="eyebrow hero-tag"><span class="dot"></span>Gambill Data Engineering</span>
  <h1>The Data Engineer Track. <span class="thin">Zero to hired.</span></h1>
  <p class="lede">A modular curriculum that takes you from no data experience to a job-ready data engineer — self-paced, with a weekly live review and a portfolio built on real, messy public data. Three ways in depending on where you start. The spine throughout: data engineering is not "writing pipelines," it is designing reliable <b>data products</b> you can defend in an interview.</p>
  <div class="backlinks">
    <a href="{L["cur"]}">Curriculum architecture</a>
    <a href="{L["build"]}">Weekly build plan</a>
  </div>
</div></div>
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Choose your path</span><h2>Three ways in</h2>
  <p>One shared module catalog, sequenced for where you are today.</p></div>
  <div class="paths">
    <div class="pcard launch"><span class="k">Path 01 — Launch</span><h3>Ground up</h3><div class="for">No data experience (maybe Excel)</div>
      <p>The full ~50-week course across four phases, ending on a governed capstone. This is where all the weekly lessons live.</p>
      <a class="go" href="{L["p1"]}">Start at Phase 1 →</a></div>
    <div class="pcard bridge"><span class="k">Path 02 — Bridge</span><h3>Cross over</h3><div class="for">Analysts &amp; software engineers</div>
      <p>A 4–6 month crossover. A placement diagnostic routes you to the analyst or SWE variant; skip what you own, go deep on the rest.</p>
      <a class="go" href="{L["bridge"]}">See the Bridge path →</a></div>
    <div class="pcard sharpen"><span class="k">Path 03 — Sharpen</span><h3>Fill the gaps</h3><div class="for">Working data engineers</div>
      <p>A self-diagnostic against the ten gaps, plus eight pre-built bundles. Every unit stands alone and links straight to its lesson.</p>
      <a class="go" href="{L["sharpen"]}">See the Sharpen path →</a></div>
  </div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">The Launch path</span><h2>Phase by phase</h2>
  <p>Bronze → silver → gold → launch. Each phase ends in a portfolio artifact; the whole path ends in a defensible, governed data product.</p></div>
  <div class="phases">{phasecards_html()}</div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Why it's built this way</span><h2>Ten gaps, closed on purpose</h2>
  <p>The curriculum was engineered backward from where people with certs and theory still stall — mined from hundreds of real coaching calls. Every module is tagged to the gap it closes.</p></div>
  <div class="gaps">{gaps_html()}</div>
</div></section>
<section style="border-bottom:none"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">How it works</span><h2>Self-paced, with accountability</h2></div>
  <div class="how">
    <div class="hcard"><div class="hn">1</div><h4>Build every week</h4><p>Short lessons scaffold a hands-on lab on real, deliberately-messy public data. The lab is the point.</p></div>
    <div class="hcard"><div class="hn">2</div><h4>Defend it live</h4><p>A weekly live review with a "defend your decision" hot seat — where theory becomes something you can articulate under questioning.</p></div>
    <div class="hcard"><div class="hn">3</div><h4>Ship a portfolio</h4><p>Each phase produces a shippable artifact; the course ends on a governed medallion project → golden records, with a recorded walkthrough.</p></div>
  </div>
</div></section>
<footer><div class="wrap"><div class="foot-note">
  <span>The Gambill Data Engineer Track · 0 → job-ready · self-paced with weekly live review.</span>
  <span class="mono">Gambill Data Engineering</span></div></div></footer>'''

open(f"{OUTDIR}/bridge.html","w").write(page("Bridge · Cross into Data Engineering", bridge_body))
open(f"{OUTDIR}/sharpen.html","w").write(page("Sharpen · Close your DE gaps", sharpen_body))
open(f"{OUTDIR}/{'index.html' if MODE=='site' else 'landing.html'}","w").write(page("The Gambill Data Engineer Track", landing_body))
print(f"[{MODE}] wrote bridge, sharpen, landing/index")
