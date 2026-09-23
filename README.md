# The Gambill Data Engineer Track

A modular **0 → job-ready Data Engineer** curriculum (self-paced, ~50 weeks, with a weekly live review) built around real, messy public data and a portfolio you can defend in an interview. It has three entry paths — **Launch** (from scratch), **Bridge** (analyst/SWE crossover), and **Sharpen** (gap-fill for working DEs) — over one shared 38-module catalog, engineered backward from ten recurring skill gaps.

## View the course

Open **`site/index.html`** in a browser — it's the course hub. From there:

| Page | File |
|---|---|
| Course home (hub) | `site/index.html` |
| Phase 1 · Foundations (W1–13) | `site/phase-1.html` |
| Phase 2 · Core DE → MDM golden records (W14–30) | `site/phase-2.html` |
| Phase 3 · Platform & Production (W31–43) | `site/phase-3.html` |
| Phase 4 · Advanced & Launch + capstone (W44–50) | `site/phase-4.html` |
| Bridge path (analyst / SWE) | `site/bridge.html` |
| Sharpen path (working DEs) | `site/sharpen.html` |

The pages are self-contained HTML (no build step, no dependencies) and are light/dark theme-aware. Intra-course navigation is relative, so the `site/` folder works opened locally or hosted anywhere. The two planning docs — the **Curriculum Architecture** and the **Weekly Build Plan** — currently live as hosted Claude artifacts and are linked from the hub (see below).

## Hosted versions (Claude artifacts)

The same pages are published as shareable Claude artifacts:

- **Course home:** https://claude.ai/code/artifact/bbf75ac1-4993-40ea-a08f-d488d2b5acf4
- Curriculum architecture: https://claude.ai/code/artifact/085627d8-ff0b-4b9a-a7cf-c83107cb71bf
- Weekly build plan: https://claude.ai/code/artifact/18e529a8-700b-447d-bae8-c4c0a3035e94
- Phase 1: https://claude.ai/code/artifact/59592bdb-3bce-4336-ba9a-69df5f936caf
- Phase 2: https://claude.ai/code/artifact/d064d266-fe89-46d3-9b3a-f9094a6c2397
- Phase 3: https://claude.ai/code/artifact/4f4034d2-8cab-4c0b-8d9d-bc6391654d4f
- Phase 4: https://claude.ai/code/artifact/6fc11b3c-5ca1-4211-9672-58249453a740
- Bridge: https://claude.ai/code/artifact/52d3eae7-e2ab-4e71-852c-4e42e08891e3
- Sharpen: https://claude.ai/code/artifact/a19e836b-6bd4-4f00-9217-7a625373b993

## Rebuilding from source

Every lesson page is generated from the per-week data in `build/data/*.json`.

```bash
cd build
python3 render_phases.py site       # -> ../site/phase-*.html   (relative links, this repo)
python3 render_paths.py  site       # -> ../site/index|bridge|sharpen.html
python3 render_phases.py artifact   # -> ../artifact_out/*.html  (absolute claude.ai links)
python3 render_paths.py  artifact
```

- `build/base.css`, `build/paths.css` — the two shared stylesheets (brand orange `#E8842A` + steel blue `#6FA3D2`, light/dark tokens).
- `build/extract.py` — regenerates `build/data/*.json` from the original authoring runs (kept for provenance).
- `artifact_out/` is git-ignored (it's just the hosted mirror with absolute links).

## Design notes

- **Method** mirrors the Gambill career-video philosophy: recognition-before-evaluation business framing, real messy public data, quarantine + idempotency + a written "why," and documentation as interview prep.
- **Phase 2–4 are one running project** ("Provider Pricing Integrity", healthcare/CMS + NPPES) that each learner mirrors on their own industry, ending on MDM golden records.
- **Platform:** neutral core → Databricks Free Edition (Delta, Unity Catalog, Lakeflow, streaming, DABs/CI-CD); cloud is a choose-your-track Azure/AWS fork.
