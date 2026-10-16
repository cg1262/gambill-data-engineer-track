# "Go Deeper" Resource Proposal — Gambill Data Engineer Track

Proposed mapping of Chris's own YouTube videos to course modules, for the per-lesson
"Go deeper" slots (`build/videos.json` → `resources`). **Status: proposal — not yet wired
into the live site.** Review, then say the word and I'll spot-check the URLs and populate.

## Channel
**Chris Gambill | Data Engineering Strategy** — https://www.youtube.com/@gambilldataengineering
(14.2K subs, 576 videos). ~65 long-form videos reviewed; 2 confirmed via transcript.

**Honest read:** the channel skews **career / strategy / AI-era commentary**, with a smaller
but genuinely strong **technical/conceptual** core (modeling, medallion, Databricks, data
quality, Spark-vs-pandas). Richest for **M08–M09, M15, M19–M24, M31–M37**; thinnest on
foundations (M00, M05/M06, M27) and governance/IaC (M29/M30).

## Proposed mapping (drop-in shape for videos.json `resources`)

| Module | Video | Why |
|---|---|---|
| M01 | [The Last Day of the Month Is Why You Have This Job!](https://www.youtube.com/watch?v=-C015y7n1mQ) | Real month-end reconciliation failure, hour-by-hour — what a DE actually does. |
| M01 | [If I Started Over As A Data Engineer](https://www.youtube.com/watch?v=CEGN-LbiX4Y) | 25-yr practitioner's mental model of the field. |
| M01 | [The 2026 Data Engineer Roadmap…](https://www.youtube.com/watch?v=uCTVYf9FBQY) | Birds-eye map of the discipline. |
| M02 | [The Most Expensive Python Mistakes You're Making](https://www.youtube.com/watch?v=Co24yhV_6rc) | Common Python footguns. |
| M03 | [Big Data Kills Pandas Performance \| Use This Instead](https://www.youtube.com/watch?v=BYK7bp8MpSU) | Pandas→Polars→Spark decision ladder; pandas' limits. |
| M04 | [Your Code Works Perfectly? That's A Problem](https://www.youtube.com/watch?v=jPgM3yghV5Q) | Guardrails/validation mindset over "it runs". |
| M04 | [$180k Data Engineers Don't Make These Python Mistakes in Databricks!](https://www.youtube.com/watch?v=D5bln7fqMZQ) | Production Python hygiene in Databricks. |
| M07 | [Data Warehouse Schemas Explained…](https://www.youtube.com/watch?v=529MqZgvgug) | Normalized vs star/snowflake trade-offs. |
| M08 | [The Star Schema: Fact vs Dimension](https://www.youtube.com/watch?v=JI-_Qk94OH0) | Core facts-vs-dimensions explainer. |
| M08 | [Data Warehouse Schemas Explained…](https://www.youtube.com/watch?v=529MqZgvgug) | When to pick each schema. |
| M09 | [SCD Type 2 Still Rules In Regulated Industries](https://www.youtube.com/watch?v=fJFqoambT54) | Why SCD2/history still matters. |
| M10 | [How to Design a Data Pipeline That's LLM-Ready](https://www.youtube.com/watch?v=tkFr-4r906Q) | Shaping gold/serving layers. |
| M11 | [Deterministic Matching vs Fuzzy Matching: Which One Works?](https://www.youtube.com/watch?v=ROF_c7p3Uvc) | Entity resolution for golden records. |
| M13 | [Become a Data Engineer From Scratch: Start with ETL/ELT!](https://www.youtube.com/watch?v=7HLVrkYIdCE) | Plain ETL vs ELT intro. |
| M13 | [Why the ETL Developers are Gone in 2026](https://www.youtube.com/watch?v=qmnfNhMMxXs) | Why the industry shifted ETL→ELT. |
| M14 | [Schema Drift Ruined Their Pipeline \| Here's How to Prevent It](https://www.youtube.com/watch?v=CrGJTYQ8PVE) | Robust ingestion against changing sources. |
| M15 | [The Medallion Architecture Most Teams Get Wrong…](https://www.youtube.com/watch?v=uNtMetMNVgw) | Bronze/silver/gold done right vs anti-patterns. |
| M15 | [End-to-End Unity Catalog Setup - Medallion Architecture!](https://www.youtube.com/watch?v=s_UkMM_4cLw) | Hands-on medallion build. |
| M16 | [The Last Day of the Month Is Why You Have This Job!](https://www.youtube.com/watch?v=-C015y7n1mQ) | Late-arriving data, idempotent reruns, backfills. |
| M16 | [Schema Drift Ruined Their Pipeline…](https://www.youtube.com/watch?v=CrGJTYQ8PVE) | Detecting upstream change. |
| M17 | [PySpark vs Pandas - Which Gets You Hired?](https://www.youtube.com/watch?v=t3vfNTvRFaI) | When to reach for PySpark. |
| M17 | [Big Data Kills Pandas Performance…](https://www.youtube.com/watch?v=BYK7bp8MpSU) | Spark intuition (lazy eval, broadcast joins, scale). |
| M19 | [Why You Don't Need More Compute](https://www.youtube.com/watch?v=9j2c2vujtIM) | Tune before you scale up. |
| M19 | [Give Me 10 Minutes and I'll Speed Up Your Pipeline](https://www.youtube.com/watch?v=GjYCs-FcsHo) | Concrete pipeline-speedup tactics. |
| M20 | [Managed vs External Tables in Databricks: The $15K Mistake](https://www.youtube.com/watch?v=xravKkAElUE) | Table-format / storage-ownership decisions. |
| M21 | [End-to-End Unity Catalog Setup…](https://www.youtube.com/watch?v=s_UkMM_4cLw) | Live Unity Catalog setup. |
| M21 | [$180k Databricks Engineers Mastered This One Method!](https://www.youtube.com/watch?v=EFtUY27bEng) | Deep-dive Databricks working method. |
| M22 | [Your Orchestration Isn't Ready for AI…](https://www.youtube.com/watch?v=b6-ygCqlhDQ) | Orchestration/Jobs expectations. |
| M22 | [Databricks Notebooks in Production: Director's Verdict!](https://www.youtube.com/watch?v=oj4MXPEnTDA) | Notebooks-vs-jobs in production. |
| M23 | [Build a Real-Time Streaming Project with This App \| Live Demo](https://www.youtube.com/watch?v=u8D-xQ_4Z4Y) | Hands-on streaming build. |
| M24 | [Databricks Data Quality: Quarantine Tables Are Not Dumping Grounds](https://www.youtube.com/watch?v=OEwnU3ooFwo) | Quarantine done right — mirrors the course method. |
| M24 | [The Last Day of the Month…](https://www.youtube.com/watch?v=-C015y7n1mQ) | Row-count/null/freshness/reconciliation checks. |
| M25 | [Your Production and Test Environments Are Drifting Apart](https://www.youtube.com/watch?v=1qAtbwm1tT8) | Why prod/test parity + real tests matter. |
| M25 | [Your Code Works Perfectly? That's A Problem](https://www.youtube.com/watch?v=jPgM3yghV5Q) | Motivates tests/guardrails over a green run. |
| M26 | [Mature Data Teams Don't Look Like Yours](https://www.youtube.com/watch?v=eMfescivhvY) | What observability/maturity looks like. |
| M26 | [AIOps Is About to Explode—Here's Why](https://www.youtube.com/watch?v=DDco8Hw_OI4) | Ops/monitoring direction of travel. |
| M28 | [Your Production and Test Environments Are Drifting Apart](https://www.youtube.com/watch?v=1qAtbwm1tT8) | The problem CI/CD for data solves. |
| M31 | [Pick the Right Data Platform (Before It's Too Late)](https://www.youtube.com/watch?v=oCVsQbOxEQM) | Platform selection criteria. |
| M31 | [Watch This Before Choosing a Data Platform](https://www.youtube.com/watch?v=ot4ptVx3AmI) | Cloud/platform selection trade-offs. |
| M32 | [Most Dangerous Data Architecture Decisions (Ranked)](https://www.youtube.com/watch?v=UiHljb8Qtl8) | Ranked architecture pitfalls. |
| M32 | [The $50K Pipeline Mistake Every Data Engineer Makes](https://www.youtube.com/watch?v=j1p1SGVARnY) | Cost of a bad architecture call. |
| M32 | [Don't Start a Databricks Migration Until You Watch This](https://www.youtube.com/watch?v=uCxhMd4kEQg) | Reasoning about a major migration. |
| M32 | [The Question Every Engineer Should Ask Before Coding](https://www.youtube.com/watch?v=Hluh6OyQN2U) | Decide before you build. |
| M33 | [What Senior Data Engineers Actually Use AI For](https://www.youtube.com/watch?v=SKscBzgxkTo) | Grounded AI-assisted DE use cases. |
| M33 | [The Four Things Your AI Agent Needs Before It Touches Production](https://www.youtube.com/watch?v=bQrIYV5Ugmk) | Production readiness for AI/agents. |
| M33 | [Why Your AI Prompts Fail in Production (And How to Fix Them)](https://www.youtube.com/watch?v=ME93JMY1fNM) | Reliability of LLM calls in pipelines. |
| M34 | [Why 80% of Data Projects Fail (and How to Fix It)](https://www.youtube.com/watch?v=R0T3ojKm_uM) | Stakeholder alignment/communication. |
| M35 | [30-Day Databricks Portfolio Projects That Actually Gets You Hired](https://www.youtube.com/watch?v=JWKz0Hcdg-8) | Concrete portfolio-project blueprint. |
| M35 | [Your Portfolio Project Is Getting You Rejected!](https://www.youtube.com/watch?v=zwJWeyCPJLg) | What makes a portfolio credible. |
| M35 | [The Data Project That Actually Gets You Hired!](https://www.youtube.com/watch?v=2mvdlgO7MSw) | Project selection that signals capability. |
| M36 | [Data Warehouse Schemas Explained…](https://www.youtube.com/watch?v=529MqZgvgug) | Classic interview modeling question. |
| M36 | [The Senior Engineer Interview Question Exposing Impostors!](https://www.youtube.com/watch?v=f60m674RIFo) | A senior-level interview question. |
| M36 | [How to Actually Get Better at LeetCode](https://www.youtube.com/watch?v=Qhwl7_0DKIc) | Coding-interview prep. |
| M36 | [Resume Rejected in 11 Seconds? Here's Why](https://www.youtube.com/watch?v=OxvmxRvNVhY) | Resume-screening reality. |
| M37 | [30-Day Databricks Portfolio Projects…](https://www.youtube.com/watch?v=JWKz0Hcdg-8) | End-to-end project structure for the capstone. |
| M37 | [How to Design a Data Pipeline That's LLM-Ready](https://www.youtube.com/watch?v=tkFr-4r906Q) | 38-min full build to model a capstone on. |

## Affiliate-link opportunities (need Chris's URLs)
- **DataCamp** — Chris explicitly recommends it on camera (Associate Data Engineer in SQL track, DE cert). Natural fit: **M05, M06, M13, M01**. *Needs DataCamp affiliate URL.*
- **Databricks Free Edition** — repeatedly tells viewers to set it up to follow along. Fit: **M17, M20, M21, M22, M15**. *Needs referral/sign-up link if any.*
- **Books (Amazon)** — names on camera: *Fundamentals of Data Engineering* → M01; *Learning Spark 2e* → M17/M18; *Polars Cookbook* → M03/M17. His "[7 Books Every Data Engineer Needs to Read](https://www.youtube.com/watch?v=_oy683m_onI)" is a ready-made affiliate vehicle for M01. *Needs Amazon affiliate tag.*
- **Course bundles** — "[Most Data Engineers Learn These 5 Courses](https://www.youtube.com/watch?v=gzHAupiEbNQ)" — fit on an M00/M01 "recommended learning" page. *Needs course affiliate URLs.*
- **One-pagers / lead magnets** — several videos push a free cheat-sheet via the description; link as lesson downloads (M03/M17). *Needs the current one-pager links.*

## Coverage gaps (where new owned content adds most value)
- **M00** Dev env/CLI/Git — none.
- **M05 / M06** SQL fundamentals & Advanced SQL — no dedicated SQL teaching video.
- **M12** Data Vault — none.
- **M18** Spark internals (shuffle/skew/AQE) — only lightly touched inside BYK7bp8MpSU.
- **M27** Git deep — none.
- **M29** Databricks Asset Bundles & IaC — none.
- **M30** Governance & security (RBAC, masking, PII/PHI) — only indirect via Unity Catalog setup.
