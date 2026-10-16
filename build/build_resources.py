#!/usr/bin/env python3
"""Populate videos.json 'resources' (the per-module 'Go deeper' slots) from the
approved channel videos + affiliate books/courses + own free templates.
Excluded per Chris: Maven Analytics (don't share); Databricks referral (none exists).
Keyed by the module code that actually RENDERS on a phase page (phase-4 multi-code
weeks render their first code, so M33→M12 week, M34/M35→M36 week).
Each list kept to <=5 to avoid overwhelm. Re-run, then render_phases.py + commit."""
import json, os
HERE = os.path.dirname(__file__)
VJ = os.path.join(HERE, "videos.json")

def v(title, url, why): return {"title": title, "url": url, "why": why}

RES = {
 "M00": [
   v("If I Started Over As A Data Engineer", "https://www.youtube.com/watch?v=CEGN-LbiX4Y", "Orientation to the field"),
   v("The 2026 Data Engineer Roadmap", "https://www.youtube.com/watch?v=uCTVYf9FBQY", "Where each module fits"),
   v("Free DE Checklist (template)", "https://gambilldata.com/resources/", "Starter checklist"),
   v("DE Honeycomb roadmap (free)", "https://www.gambilldataengineering.com/data-engineering-honeycomb", "Visual field map"),
 ],
 "M01": [
   v("The Last Day of the Month Is Why You Have This Job!", "https://www.youtube.com/watch?v=-C015y7n1mQ", "What a DE actually does"),
   v("Fundamentals of Data Engineering (book)", "https://amzn.to/4wmq0cb", "The field's core text"),
   v("Designing Data-Intensive Applications (book)", "https://amzn.to/45QIzci", "Systems thinking"),
 ],
 "M02": [
   v("The Most Expensive Python Mistakes You're Making", "https://www.youtube.com/watch?v=Co24yhV_6rc", "Python footguns"),
   v("Automate the Boring Stuff with Python (book)", "https://amzn.to/4fYPIKD", "Beginner Python"),
   v("DataCamp — Data Engineer in Python track (course)", "https://datacamp.pxf.io/m4EjNa", "Structured practice"),
   v("Better-Python template (free)", "https://www.gambilldataengineering.com/business-templates#better-python", "Clean-code starter"),
 ],
 "M03": [
   v("Big Data Kills Pandas Performance | Use This Instead", "https://www.youtube.com/watch?v=BYK7bp8MpSU", "pandas→Polars→Spark ladder"),
   v("PySpark vs Pandas - Which Gets You Hired?", "https://www.youtube.com/watch?v=t3vfNTvRFaI", "When to scale up"),
   v("DataFrame Upgrade Roadmap (free)", "https://www.gambilldataengineering.com/business-templates#dataframe-upgrade-roadmap", "One-pager"),
 ],
 "M04": [
   v("Your Code Works Perfectly? That's A Problem", "https://www.youtube.com/watch?v=jPgM3yghV5Q", "Guardrails mindset"),
   v("$180k Data Engineers Don't Make These Python Mistakes", "https://www.youtube.com/watch?v=D5bln7fqMZQ", "Production hygiene"),
   v("The Pragmatic Programmer (book)", "https://amzn.to/47eXsaz", "Craft fundamentals"),
 ],
 "M05": [
   v("DataCamp — Associate Data Engineer in SQL track (course)", "https://datacamp.pxf.io/m4Gqbq", "SQL practice path"),
   v("The Complete SQL Bootcamp (course)", "https://trk.udemy.com/N9qkav", "Hands-on SQL"),
   v("SQL in 10 Minutes (book)", "https://amzn.to/4ajcv2E", "Fast reference"),
 ],
 "M06": [
   v("SQL Performance Explained (book)", "https://amzn.to/4lOy1QK", "Indexing & query plans"),
   v("SQL for Data Engineering (course)", "https://trk.udemy.com/aOdoyQ", "DE-flavored SQL"),
 ],
 "M07": [
   v("Data Warehouse Schemas Explained", "https://www.youtube.com/watch?v=529MqZgvgug", "Normalized vs star"),
   v("Database Design for Mere Mortals (book)", "https://amzn.to/3C4uLju", "Relational design"),
   v("The Data Warehouse Toolkit — Kimball (book)", "https://amzn.to/45Sd0yH", "The modeling bible"),
 ],
 "M08": [
   v("The Star Schema: Fact vs Dimension", "https://www.youtube.com/watch?v=JI-_Qk94OH0", "Facts vs dims"),
   v("Data Warehouse Schemas Explained", "https://www.youtube.com/watch?v=529MqZgvgug", "Pick the right schema"),
   v("The Data Warehouse Toolkit — Kimball (book)", "https://amzn.to/45Sd0yH", "Dimensional modeling"),
 ],
 "M09": [
   v("SCD Type 2 Still Rules In Regulated Industries", "https://www.youtube.com/watch?v=fJFqoambT54", "Why history tracking matters"),
 ],
 "M10": [
   v("How to Design a Data Pipeline That's LLM-Ready", "https://www.youtube.com/watch?v=tkFr-4r906Q", "Shaping the gold/serving layer"),
 ],
 "M11": [
   v("Deterministic Matching vs Fuzzy Matching", "https://www.youtube.com/watch?v=ROF_c7p3Uvc", "Entity resolution for golden records"),
 ],
 "M13": [
   v("Become a Data Engineer From Scratch: Start with ETL/ELT!", "https://www.youtube.com/watch?v=7HLVrkYIdCE", "ETL vs ELT intro"),
   v("Why the ETL Developers are Gone in 2026", "https://www.youtube.com/watch?v=qmnfNhMMxXs", "Why the shift to ELT"),
 ],
 "M14": [
   v("Schema Drift Ruined Their Pipeline | Prevent It", "https://www.youtube.com/watch?v=CrGJTYQ8PVE", "Robust ingestion"),
   v("Surviving Schema Drift (article)", "https://www.gambilldataengineering.com/data-engineering/how-to-survive-schema-drift-the-silent-killer-of-data-pipelines", "Deep dive"),
 ],
 "M15": [
   v("The Medallion Architecture Most Teams Get Wrong", "https://www.youtube.com/watch?v=uNtMetMNVgw", "Bronze/silver/gold done right"),
   v("End-to-End Unity Catalog Setup — Medallion", "https://www.youtube.com/watch?v=s_UkMM_4cLw", "Hands-on build"),
   v("Real-World Medallion template (free)", "https://www.gambilldataengineering.com/gambill-data-business-templates#real-world-medallion", "Starter layout"),
 ],
 "M16": [
   v("The Last Day of the Month Is Why You Have This Job!", "https://www.youtube.com/watch?v=-C015y7n1mQ", "Late data, idempotent reruns, backfills"),
   v("Schema Drift Ruined Their Pipeline | Prevent It", "https://www.youtube.com/watch?v=CrGJTYQ8PVE", "Detecting upstream change"),
 ],
 "M17": [
   v("PySpark vs Pandas - Which Gets You Hired?", "https://www.youtube.com/watch?v=t3vfNTvRFaI", "When to reach for Spark"),
   v("Databricks & PySpark Zero to Expert (course)", "https://trk.udemy.com/RGeRR7", "Hands-on PySpark"),
   v("Taming Big Data with Apache Spark (course)", "https://trk.udemy.com/vPaNdO", "Spark fundamentals"),
   v("PySpark-on-Databricks template (free)", "https://www.gambilldataengineering.com/business-templates#pyspark-on-dbx", "Starter"),
 ],
 "M18": [
   v("Designing Data-Intensive Applications (book)", "https://amzn.to/45QIzci", "Partitioning & distributed internals"),
   v("Big Data Kills Pandas Performance | Use This Instead", "https://www.youtube.com/watch?v=BYK7bp8MpSU", "Scale/shuffle intuition"),
 ],
 "M20": [
   v("Managed vs External Tables in Databricks: The $15K Mistake", "https://www.youtube.com/watch?v=xravKkAElUE", "Storage & table-format decisions"),
 ],
 "M21": [
   v("End-to-End Unity Catalog Setup", "https://www.youtube.com/watch?v=s_UkMM_4cLw", "Live UC setup"),
   v("$180k Databricks Engineers Mastered This One Method", "https://www.youtube.com/watch?v=EFtUY27bEng", "Working method"),
   v("Databricks Certified DE Associate (course)", "https://trk.udemy.com/o4rnzY", "Cert prep"),
 ],
 "M22": [
   v("Your Orchestration Isn't Ready for AI", "https://www.youtube.com/watch?v=b6-ygCqlhDQ", "Orchestration expectations"),
   v("Databricks Notebooks in Production: Director's Verdict", "https://www.youtube.com/watch?v=oj4MXPEnTDA", "Notebooks vs jobs"),
   v("Hybrid Notebook/Script Architecture Map (free)", "https://gambilldata.com/resources/hybrid-notebook-script-architecture-map/", "Structure guide"),
   v("Hands-On Apache Airflow 3 (course)", "https://trk.udemy.com/3JNe1X", "Orchestration deep-dive"),
 ],
 "M23": [
   v("Build a Real-Time Streaming Project | Live Demo", "https://www.youtube.com/watch?v=u8D-xQ_4Z4Y", "Hands-on streaming"),
   v("DE Vol.2 AWS: Spark & Kafka (course)", "https://trk.udemy.com/194bRD", "Streaming at scale"),
 ],
 "M24": [
   v("Databricks Data Quality: Quarantine Tables Are Not Dumping Grounds", "https://www.youtube.com/watch?v=OEwnU3ooFwo", "Quarantine done right"),
   v("The Last Day of the Month Is Why You Have This Job!", "https://www.youtube.com/watch?v=-C015y7n1mQ", "Reconciliation & fail-fast"),
 ],
 "M25": [
   v("Your Production and Test Environments Are Drifting Apart", "https://www.youtube.com/watch?v=1qAtbwm1tT8", "Why prod/test parity matters"),
   v("Your Code Works Perfectly? That's A Problem", "https://www.youtube.com/watch?v=jPgM3yghV5Q", "Tests over a green run"),
 ],
 "M26": [
   v("Mature Data Teams Don't Look Like Yours", "https://www.youtube.com/watch?v=eMfescivhvY", "What observability looks like"),
   v("AIOps Is About to Explode—Here's Why", "https://www.youtube.com/watch?v=DDco8Hw_OI4", "Ops direction of travel"),
   v("Data-Maturity Tracker (free)", "https://www.gambilldataengineering.com/gambill-data-business-templates#maturity-tracker", "Self-assessment"),
 ],
 "M28": [
   v("Your Production and Test Environments Are Drifting Apart", "https://www.youtube.com/watch?v=1qAtbwm1tT8", "The problem CI/CD solves"),
 ],
 "M30": [
   v("Data Governance (book)", "https://amzn.to/4myGcBZ", "Governance foundations"),
 ],
 "M31": [
   v("Pick the Right Data Platform (Before It's Too Late)", "https://www.youtube.com/watch?v=oCVsQbOxEQM", "Platform selection"),
   v("Watch This Before Choosing a Data Platform", "https://www.youtube.com/watch?v=ot4ptVx3AmI", "Cloud trade-offs"),
   v("Microsoft Fabric Complete Guide (course)", "https://bit.ly/Fabric-Tutorial", "Cloud platform skills"),
   v("DP-700 Fabric Practice Test (course)", "https://bit.ly/DP-700-Practice", "Cert practice"),
 ],
 # Phase 4 — keyed to the code each week actually renders:
 "M32": [  # W44 Architecture decision-making
   v("Most Dangerous Data Architecture Decisions (Ranked)", "https://www.youtube.com/watch?v=UiHljb8Qtl8", "Ranked pitfalls"),
   v("The $50K Pipeline Mistake Every Data Engineer Makes", "https://www.youtube.com/watch?v=j1p1SGVARnY", "Cost of a bad call"),
   v("The Question Every Engineer Should Ask Before Coding", "https://www.youtube.com/watch?v=Hluh6OyQN2U", "Decide before you build"),
   v("Designing Data-Intensive Applications (book)", "https://amzn.to/45QIzci", "Architecture reference"),
 ],
 "M12": [  # W45 elective — Data Vault OR AI-assisted DE
   v("What Senior Data Engineers Actually Use AI For", "https://www.youtube.com/watch?v=SKscBzgxkTo", "Grounded AI-assisted DE"),
   v("The Four Things Your AI Agent Needs Before Production", "https://www.youtube.com/watch?v=bQrIYV5Ugmk", "Production readiness"),
   v("2026 AI-Readiness Checklist (free)", "https://bit.ly/4lIJm6F", "Self-assessment"),
   v("Senior-Engineer AI Architecture Checklist (free)", "https://gambilldata.com/resources/senior-engineer-ai-architecture-checklist/", "Design checklist"),
 ],
 "M36": [  # W46 & W47 interview prep (+ comms/portfolio woven)
   v("The Senior Engineer Interview Question Exposing Impostors", "https://www.youtube.com/watch?v=f60m674RIFo", "A senior-level question"),
   v("Your Portfolio Project Is Getting You Rejected!", "https://www.youtube.com/watch?v=zwJWeyCPJLg", "Portfolio credibility"),
   v("Storytelling With Data (book)", "https://amzn.to/4lH98pZ", "Communicate the work"),
   v("DataCamp — DE Certification (course)", "https://datacamp.pxf.io/QYbLeM", "Credential"),
   v("TopResume — resume review (service)", "https://topresume.sjv.io/4G1mJ0", "Resume help"),
 ],
 "M37": [  # W48 capstone
   v("30-Day Databricks Portfolio Projects That Get You Hired", "https://www.youtube.com/watch?v=JWKz0Hcdg-8", "Capstone blueprint"),
   v("The Data Project That Actually Gets You Hired!", "https://www.youtube.com/watch?v=2mvdlgO7MSw", "Project selection"),
   v("Example repo: ca-public-health-facility", "https://github.com/cg1262/ca-public-health-facility", "A real worked example"),
   v("DE Job-Search Blueprint (free)", "https://gambilldata.com/resources/data-engineer-job-search-blueprint/", "Launch plan"),
 ],
}

# Module-level "Go deeper" now holds ONLY Chris's OWN content (channel videos +
# his free templates / repos). Third-party courses & books come from the
# curated per-week affiliate workbook (build/week_resources.json), so drop any
# scraped Amazon/DataCamp/Udemy/O'Reilly/Coursera links here to avoid conflicts.
OWN = ("youtube.com", "youtu.be", "gambilldata.com", "gambilldataengineering.com", "github.com/cg1262")
def _own(url): return any(h in (url or "") for h in OWN)
RES = {m: [r for r in items if _own(r.get("url", ""))] for m, items in RES.items()}
RES = {m: items for m, items in RES.items() if items}

data = json.load(open(VJ))
data["resources"] = RES  # Chris's own content only
json.dump(data, open(VJ, "w"), indent=2, ensure_ascii=False)
total = sum(len(x) for x in RES.values())
print(f"wrote {len(RES)} modules, {total} own-content resource links into videos.json")
