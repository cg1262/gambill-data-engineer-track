# Practical lesson video scripts

51 short scripts cover all 50 course weeks. Week 45 has a separate video for each elective; a learner chooses one. The shared Weeks 48–50 capstone card is split into three weekly checkpoint videos. Each file contains clean spoken copy under **Script** and a separate **Screen example — not spoken** with setup context and an observation to demonstrate.

Aim for **3–5 minutes per video**, including screen walkthroughs and pauses. Spoken copy is roughly 350–400 words per script; the table below gives actual counts. Use a natural recording pace rather than treating the estimate as a stopwatch target. The videos teach a focused technique and brief the practical work; they do not replace the longer readings and labs.

## How to record

Start with the recognizable failure, explain the decision, show the small example, and finish with the student's next exercise. Read only the Script section as teleprompter copy. Keep the screen example ready in the appropriate learner-project environment. Explain each result before moving on. Use synthetic fixtures where indicated and actual measured project results where the script asks for evidence.

Examples are intentionally small demonstrations, not complete lab solutions. Commands referencing a Python package, Chinook database, weather table, Unity Catalog objects, bundle, GitHub workflow, or cloud resource assume the learner has created that lesson's project and prerequisites. They are not commands to run against this static course website repository. Fill placeholders from the real project; never put credentials or restricted data into the recording.

The course pages linked in each file define the full objectives and deliverables. The spoken lesson expands one practical thread rather than reading every concept bullet aloud. Important distinctions include price versus spend, historical versus current grain, business versus audit timestamps, event-time versus ingestion progress, and exact record accounting versus aggregate controls.

## Recording order

### Phase 1

| Week | Script | Module(s) | Spoken words |
|---|---|---|---:|
| 1 | [Make your setup reproducible](phase-1/week-01-environment-and-git.md) | M00 | 376 |
| 2 | [Say what one row means](phase-1/week-02-data-product-contract.md) | M01 | 384 |
| 3 | [Parse first, then make the decision](phase-1/week-03-python-functions.md) | M02 | 394 |
| 4 | [Give every bad record somewhere to go](phase-1/week-04-python-files-and-errors.md) | M02 | 385 |
| 5 | [Make the code run outside its own folder](phase-1/week-05-python-packaging.md) | M02 | 374 |
| 6 | [Catch a merge that multiplies your answer](phase-1/week-06-pandas-join-safety.md) | M03 | 368 |
| 7 | [Keep the records that disagree](phase-1/week-07-api-reconciliation.md) | M03 | 380 |
| 8 | [Test the component you will ship](phase-1/week-08-tests-and-wheel.md) | M04 | 372 |
| 9 | [Keep the parent row you meant to keep](phase-1/week-09-sql-joins.md) | M05 | 367 |
| 10 | [Define what your count counts](phase-1/week-10-sql-aggregation.md) | M05 | 356 |
| 11 | [Make the window match the question](phase-1/week-11-sql-windows.md) | M06 | 367 |
| 12 | [Tune the work the database actually does](phase-1/week-12-postgres-query-plans.md) | M06 | 382 |
| 13 | [Put each fact about a restaurant in one place](phase-1/week-13-normalization.md) | M07 | 384 |

### Phase 2

| Week | Script | Module(s) | Spoken words |
|---|---|---|---:|
| 14 | [Separate the price from its context](phase-2/week-14-facts-and-dimensions.md) | M08 | 385 |
| 15 | [Write the grain before choosing the key](phase-2/week-15-grain-and-conformed-dimensions.md) | M08 | 381 |
| 16 | [Answer what was true on the report date](phase-2/week-16-scd-history.md) | M09 | 368 |
| 17 | [Give the metric one definition](phase-2/week-17-gold-metrics.md) | M10 | 369 |
| 18 | [Find plausible matches without comparing everyone](phase-2/week-18-blocking-and-crosswalks.md) | M11 | 382 |
| 19 | [Make a match decision you can reverse](phase-2/week-19-golden-records.md) | M11 | 378 |
| 20 | [Design the failure path before the next load](phase-2/week-20-architecture-decisions.md) | M13 | 399 |
| 21 | [Land a source version you can replay](phase-2/week-21-bronze-ingestion.md) | M14 | 395 |
| 22 | [Turn layer names into enforceable promises](phase-2/week-22-layer-contracts.md) | M15 | 385 |
| 23 | [Keep a durable record of what you consumed](phase-2/week-23-incremental-watermarks.md) | M16 | 387 |
| 24 | [Make the second run as safe as the first](phase-2/week-24-idempotency-and-backfills.md) | M16 | 380 |
| 25 | [Build a plan, then choose when to execute it](phase-2/week-25-spark-dataframes.md) | M17 | 382 |
| 26 | [Move the small lookup, keep the big work distributed](phase-2/week-26-spark-joins-and-functions.md) | M17 | 393 |
| 27 | [Find the task everybody is waiting for](phase-2/week-27-spark-skew.md) | M18 | 393 |
| 28 | [Keep every reason a record failed](phase-2/week-28-quality-and-quarantine.md) | M24 | 375 |
| 29 | [Balance the pipeline to the record](phase-2/week-29-reconciliation-ledger.md) | M24 | 377 |
| 30 | [Turn your evidence into a repeatable test](phase-2/week-30-pipeline-test-suite.md) | M25 | 389 |

### Phase 3

| Week | Script | Module(s) | Spoken words |
|---|---|---|---:|
| 31 | [Optimize a measured query and preserve recovery](phase-3/week-31-delta-optimization.md) | M20 | 369 |
| 32 | [Prove the intended reader can access the intended table](phase-3/week-32-unity-catalog.md) | M21 | 384 |
| 33 | [Declare the output and the rule that protects it](phase-3/week-33-declarative-quality.md) | M22 | 389 |
| 34 | [Repair the failed work without corrupting the good work](phase-3/week-34-job-orchestration.md) | M22 | 371 |
| 35 | [Restart from progress you have actually saved](phase-3/week-35-auto-loader-and-checkpoints.md) | M23 | 371 |
| 36 | [Bound deduplication without losing the evidence](phase-3/week-36-streaming-event-time.md) | M23 | 392 |
| 37 | [Make the alert point to a recovery action](phase-3/week-37-observability-and-runbooks.md) | M26 | 379 |
| 38 | [Review what a change does to the data](phase-3/week-38-git-review-for-data.md) | M27 | 383 |
| 39 | [Make the failed check block the risky change](phase-3/week-39-ci-and-promotion.md) | M28 | 369 |
| 40 | [Inspect where the deployment will land](phase-3/week-40-bundles-and-targets.md) | M29 | 368 |
| 41 | [Test access with the identity you intend to restrict](phase-3/week-41-access-and-masking.md) | M30 | 392 |
| 42 | [Trace the identity from the job to the storage](phase-3/week-42-cloud-storage-and-cost.md) | M31 | 386 |
| 43 | [Let someone else operate the release](phase-3/week-43-release-and-recovery.md) | M20–M31 | 388 |

### Phase 4

| Week | Script | Module(s) | Spoken words |
|---|---|---|---:|
| 44 | [Choose a problem small enough to finish](phase-4/week-44-capstone-design.md) | M32 | 394 |
| 45A | [Use a vault when source history earns the extra model](phase-4/week-45a-data-vault.md) | M12 | 382 |
| 45B | [Give the model a narrow job and an exit route](phase-4/week-45b-bounded-ai-step.md) | M33 | 389 |
| 46 | [State the grain before you start typing](phase-4/week-46-technical-interview.md) | M36 / M35 | 388 |
| 47 | [Tell the decision through evidence](phase-4/week-47-explain-your-work.md) | M36 / M34 | 396 |
| 48 | [Get one source record through the foundation](phase-4/week-48-capstone-first-slice.md) | M37 | 401 |
| 49 | [Publish the answer and prove the replay](phase-4/week-49-capstone-product-and-replay.md) | M37 | 374 |
| 50 | [Ship something another engineer can verify](phase-4/week-50-capstone-release-and-defense.md) | M37 | 388 |

## Bridge and Sharpen reuse

Record the technical lesson once and reuse it wherever that module appears. Week numbers here are **Launch curriculum references**, not a claim that Bridge takes 50 weeks. Bridge learners follow the analyst/SWE routing and diagnostic in [the Bridge page](../../site/bridge.html); Sharpen learners select the bundles in [the Sharpen page](../../site/sharpen.html).

| Module(s) | Use these lesson recordings |
|---|---|
| M00 | Week 1 |
| M01 | Week 2 |
| M02 | Weeks 3–5 |
| M03 | Weeks 6–7 |
| M04 | Week 8 |
| M05 | Weeks 9–10 |
| M06 | Weeks 11–12 |
| M07 | Week 13 |
| M08 | Weeks 14–15 |
| M09 | Week 16 |
| M10 | Week 17 |
| M11 | Weeks 18–19 |
| M12 | Week 45A, optional Data Vault track |
| M13 | Week 20 |
| M14 | Week 21 |
| M15 | Week 22 |
| M16 | Weeks 23–24 |
| M17 | Weeks 25–26 |
| M18 | Week 27 |
| M19 | Performance thread in Weeks 27 and 31; the current curriculum has no standalone M19 week |
| M20 | Week 31; integrated release in Week 43 |
| M21 | Week 32 |
| M22 | Weeks 33–34 |
| M23 | Weeks 35–36 |
| M24 | Weeks 28–29 |
| M25 | Week 30 |
| M26 | Week 37 |
| M27 | Week 38 |
| M28 | Week 39 |
| M29 | Week 40 |
| M30 | Week 41 |
| M31 | Week 42 |
| M32 | Week 44 |
| M33 | Week 45B, optional bounded-AI track |
| M34 | Week 47 |
| M35 | Portfolio work in Weeks 30, 46–47, and 50 |
| M36 | Weeks 46–47 |
| M37 | Weeks 48–50; renumber the sprint checkpoints for the chosen path |

Prerequisites still matter for a standalone Sharpen recording. Use a pinned project fixture if the learner has not built the earlier pipeline, and identify the input tables and contracts before starting. The examples distinguish a small teaching fixture from full-scale ingestion or a deployed workflow.

## Source and technical review notes

Phase 1 follows `build/data/phase1_base.json` plus the enhanced labs in `build/data/phase1_enh.json`; Week 1 concept coverage also comes from the rendered course page. Phases 2–4 follow `build/data/phase2.json`, `phase3.json`, and `phase4.json`. Weeks 49 and 50 deliberately link to the existing `w48` capstone card. The original [Launch](launch-month-1.md), [Bridge](bridge-month-1.md), [Sharpen](sharpen-month-1.md), and [welcome](../welcome-video-scripts.md) drafts remain unchanged. Use this complete series for new practical lesson recordings; check earlier drafts against the current course before reusing their instructions or pass criteria.

Local Python and DuckDB examples can be checked offline. Spark, PostgreSQL, Lakeflow, Unity Catalog, Auto Loader, Jobs, GitHub protection/deployment, and cloud examples require their respective configured systems. Do not present them as executed merely because the script exists. Free Edition and other workspace tiers do not necessarily provide every governance, identity, external-storage, notification, networking, or billing feature in Phase 3. Mark an unavailable exercise pending or use a suitable authorized workspace.

Primary references to check in the recording environment:

- [Python documentation](https://docs.python.org/3/) and [pytest documentation](https://docs.pytest.org/en/stable/).
- [DuckDB SQL documentation](https://duckdb.org/docs/stable/sql/introduction) and [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html).
- [Apache Spark Structured Streaming](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html).
- [Databricks Lakeflow SQL reference](https://docs.databricks.com/aws/en/ldp/developer/sql-ref), [bundle settings](https://docs.databricks.com/aws/en/dev-tools/bundles/settings), and the matching cloud/runtime documentation for access and storage.
- [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and the action versions approved for the learner's repository.

Live Databricks/Spark documentation retrieval was blocked by this environment's network proxy during authoring. Runtime-sensitive examples therefore include recording prerequisites rather than claims of fresh cloud execution. Verify API support and the actual positive and negative results in the workspace you record. Never invent client incidents, benchmarks, business impact, or a production track record; course failure drills should remain clearly labeled as drills.

## Authoring checks completed

- Confirmed 51 scripts cover Weeks 1–50, with two Week 45 electives and three capstone checkpoints. Every script has spoken copy and a separate screen example; index word counts match the copy.
- Verified all 108 local Markdown links and course-page anchors across this index and the new scripts.
- Parsed all 18 Python examples. Executed 13 local examples, including the pandas fixtures, and ran the separate parametrized pytest example: **4 passed**. The four Spark snippets were not executed.
- Executed 11 DuckDB result checks across seven lessons, including the two deliberately rejected constraint writes. Verified the intended null, window, temporal-lookup, completeness, and tie-ordering outcomes.
- Parsed the illustrative CI YAML. This checks syntax only; no GitHub workflow, branch rule, deployment gate, or remote workload was executed.
- PostgreSQL, Databricks, identity, notification, cloud-storage, and billing demonstrations remain dependent on their recording environments. All pre-existing repository files were preserved.
