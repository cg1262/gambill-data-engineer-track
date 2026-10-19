# Bridge, Month 1: Lesson Scripts

Bridge runs about twenty weeks and reuses the Launch lesson pages, so its first month is one stage: "Close the engineering gap" for analysts (M00 to M04), "Close the data gap" for software engineers (M01, M05, M06, M07). Where a module already has a Launch script, Bridge reuses that video. This file holds what Bridge needs on top: a kickoff per variant, and one script per module that Launch month one does not cover. Because Bridge compresses two Launch weeks into one, each of those scripts covers the whole module in a single video.

Target: kickoffs 2 to 3 minutes; module videos 4 to 5 minutes. Voice as the welcome videos: direct, warm, second person, no hype.

Source of truth: `site/bridge.html` and `site/phase-1.html` (weeks 6 to 13). If the pages change, change the scripts.

## Month 1 map

| Week | Analyst variant | Script | SWE variant | Script |
|---|---|---|---|---|
| 1 | M00 Dev env, CLI, Git + M01 DE mental model | Launch W1 + W2 | M01 DE mental model | Launch W2 |
| 2 | M02 Python fundamentals | Launch W3 + W4 (W5 on the page for modules) | M05 SQL fundamentals | SWE-2 below |
| 3 | M03 Python for data (pandas, APIs) | Analyst-3 below | M06 Advanced SQL | SWE-3 below |
| 4 | M04 Software engineering hygiene | Analyst-4 below | M07 Relational theory and normalization | SWE-4 below |

---

## Kickoff A: Analyst to DE, month one
**Target:** ~2.5 minutes (~330 words)

You took the diagnostic. The window function came easy. The star schema came easy. The Python reconciliation and the branch-test-deploy question, less so. That is the analyst profile, and it is exactly what this month is for.

You already own SQL, aggregation, business framing, the instinct for what a stakeholder actually asked. We skip M05, SQL fundamentals, because you proved it in the diagnostic. M06, advanced SQL, becomes a quick review later. What you do not own yet is engineering rigor: Git, Python as a language and not a notebook, APIs, tests, packaging. Month one closes that gap. Five modules, four weeks.

Week one is two modules. M00, the dev environment, the command line, and Git. You stand up a repo the way a real team would and merge a pull request you opened and reviewed yourself. Then M01, the data engineering mental model. Grain, owner, consumers, contract. You have been living downstream of these words for years. Now you write them.

Week two is Python fundamentals, M02. Control flow, functions, the four collections, file handling, and a quarantine pattern for bad records. If you have written Python in a notebook, this will feel slower than you expect. That is on purpose. Return versus print, specific exceptions, a script that runs from the command line. These are the habits that separate a script from a component.

Week three, M03, Python for data. Pandas with discipline: profile first, clean with a plan, state the grain of every aggregate, prove a merge did not multiply rows. Then APIs: pagination, backoff, and reconciling two sources that disagree.

Week four, M04, software engineering hygiene. Type hints, tests, a package you can pip install. This is the week your Python stops looking like analyst Python.

Every week ends in the live review. Bring the lab, defend a decision out loud. Plan on eight to twelve hours a week, and the lab is most of it.

Open your repo. Week one starts with Launch's week one video. Go.

**[on-screen / b-roll]** Lower-third: "Bridge · Analyst to DE · Month 1." Cutaway: the four-week map above as a table, analyst column highlighted, M05 crossed out with "proven in the diagnostic."

---

## Kickoff S: SWE to DE, month one
**Target:** ~2 minutes (~310 words)

You took the diagnostic. The reconciliation script and the deploy question were easy. The window function tie and the grain sentence, not so much. That is the software engineer profile. You can ship code. You have not yet had to think in rows.

You own Python, Git, pull requests, tests, CI/CD, packaging. So we skip M00, M02, and M27. No CLI tutorial, no Python fundamentals, no Git deep dive. What you do not own yet is data: SQL past the basics, modeling, grain, the difference between a join and a reconciliation. Month one closes that gap. Four modules, four weeks.

Week one, M01, the data engineering mental model. You will be tempted to skip it because it has no code. Do not. It is where you learn that the product is the table, not the pipeline, and that a data contract is a set of promises, not a schema file. Every modeling decision later hangs on this week.

Week two, M05, SQL fundamentals. Joins and their set semantics, NULL logic, GROUP BY and the grain of a grouped result, HAVING, subqueries. Two Launch weeks in one. If you think you know SQL because you wrote queries in an ORM, this is the week that proves otherwise.

Week three, M06, advanced SQL. Window functions, the ranking family and how ties behave, lag and lead, frames, CTEs. Then query plans: EXPLAIN ANALYZE, sargability, which index helps and which one the planner ignores.

Week four, M07, relational theory and normalization. Keys, functional dependencies, first through third normal form, referential integrity, and the one deliberate denormalization you can defend. It closes with the Phase 1 portfolio assembled.

Every week ends in the live review. Bring the lab, defend a decision out loud. Plan on eight to twelve hours a week.

Week one starts with Launch's week two video, the mental model. Go.

**[on-screen / b-roll]** Lower-third: "Bridge · SWE to DE · Month 1." Cutaway: the four-week map, SWE column highlighted, M00 and M02 crossed out with "already owned."

---

## Analyst-3: M03, Python for data (pandas, APIs, and reconciliation)
**Covers:** Launch weeks 6 and 7 · **Closes:** G1, G4, G2
**Target:** ~5 minutes (~700 words)

You have merged two tables in a notebook and watched the row count go up. Maybe you noticed. Maybe the dashboard just ran a little hot that month. A non-unique join key multiplies rows silently, and most people find out from the finance team.

This module is pandas and APIs with the discipline that stops that from happening. Two Launch weeks in one. Week six is DataFrames. Week seven is APIs and reconciliation. You already think in tables, so the mechanics will come fast. The discipline is the point.

Why it matters. Gap four is data quality. Gap two is grain. An analyst who can state the grain of every aggregate and prove every merge kept its row count is already thinking like an engineer.

The ideas, first half: DataFrames.

The DataFrame and Series model. The index, dtypes, and why vectorized operations beat Python loops.

Selection and filtering. loc versus iloc, boolean masks, and the copy-versus-view trap that produces the SettingWithCopy warning everyone ignores.

The cleaning toolkit. Missing values, fillna or dropna. Duplicates. Type coercion. String and datetime normalization.

Transformation. Derived columns. map and apply versus vectorized ops. Binning.

Split-apply-combine. groupby to a stated grain, then merge with how=, key uniqueness, and a row-count check.

Second half: APIs.

HTTP basics. Methods, status codes, headers, query params, JSON payloads. The request-response model.

Calling an API with requests. Params, timeouts, raise_for_status, flattening nested JSON into rows.

Pagination and rate limits. Offset-limit, page and per_page, cursors. A 429, Retry-After, exponential backoff.

Reconciliation. Join keys. Matched, source-only, value-mismatch. Numeric tolerance. Why provenance and an as-of date belong on every reconciled row.

Lab one, pandas. Load a raw NYC 311 subset into a notebook. Profile it before you touch it: row count, nulls per column, dtypes, a duplicate check. Write a five-line cleaning plan. Then execute it. Parse the created date. Standardize borough and complaint type. Drop or impute nulls by a rule you wrote down. Dedupe on the unique key.

Aggregate to a stated grain: complaint type by borough by month, as a request count. Merge that to a borough population reference and compute requests per ten thousand residents. Then validate the merge. Assert the output row count equals the grain cardinality. Report unmatched borough keys. Confirm no row inflation. Export to parquet.

Lab two, APIs. Pull total population per country from the World Bank Indicators API. Page through every result. Back off on a 429 or a timeout. Normalize the nested JSON into a frame keyed by ISO3 and year. Separately load the Our World in Data population CSV. Align the keys. Outer join. Classify every key: matched, API-only, CSV-only. Compare the values against a tolerance you state. Write one reconciled table with a source and as-of column, plus a summary: counts per class and the top discrepancies.

A pass, lab one. The profile exists before any cleaning. Every cleaning decision is justified. The final grain is stated and every key in it is unique. The merge check proves no duplication.

A pass, lab two. Pagination returns the complete set, row count matches the API's reported total, no duplicates. Every key is classified and the class counts sum to the union. Discrepancies are flagged against the stated tolerance. The output carries provenance. A rerun is deterministic, and a 429 does not crash it.

The hot seat, and there are two this module.

First: "State the grain of your final 311 table. Prove each key in it is unique. Show me the check that proves your merge did not silently duplicate rows. And for one column, tell me why you imputed where you dropped elsewhere."

Second: "Defend your join key and your tolerance. When the two sources disagree on a country's population, how do you decide which one is right? And what would you do if there were no shared code to join on?"

The misconceptions I am hunting. One: that a merge is safe and can't change the row count. Two: that a join is a reconciliation. An inner join silently drops the non-matching rows, and those rows are the exact discrepancies you are paid to surface.

Two sources that both call themselves authoritative will disagree. Your job is to say by how much, and why.

**[on-screen / b-roll]** Lower-third: "Bridge · M03 · Python for data." Cutaway A: a merge before and after, row count 1,204 becoming 1,377, with the duplicate key highlighted. Cutaway B: a reconciliation summary table, matched / api-only / csv-only / mismatch, four counts summing to the union. Callout: "Profile first. State the grain. Prove the merge."

---

## Analyst-4: M04, Software engineering hygiene
**Covers:** Launch week 8 · **Closes:** G6, G1, G4
**Target:** ~4 minutes (~580 words)

A green test run does not prove your code is correct. It proves the lines you tested ran. If the test asserts nothing useful, coverage is a number, not a fact. And type hints are not enforced at runtime, so a wrong annotation sits there looking reassuring until a string arrives where an int was promised.

This is the week analyst Python becomes engineering. Take last week's reconciliation script and turn it into a typed, tested, packaged component. One Launch week, one Bridge week.

Why it matters. Gap six, the dev workflow. Hiring managers for data engineering roles will open your repo. They want to see a package, a test suite, and a type checker passing. Not a notebook with cell seventeen that only works if you ran cell four twice.

The ideas.

Type hints and static checking. Annotate parameters and returns. list of dict, Optional, TypedDict, dataclasses. Run mypy or pyright. Understand why the check happens before the code runs, not during.

Docstrings as contracts. Args, returns, raises. The docstring has to agree with the signature, and the tests have to agree with both.

Unit testing with pytest. Assert. Arrange, act, assert. Fixtures. Parametrize. Test the boundaries, not just the happy path. Tests as an executable spec.

Modular structure. Pure functions versus I/O. Testability is a consequence of structure: if the logic is tangled with the fetch, you can't test it offline.

Packaging. pyproject.toml. Build a wheel. Editable versus regular install. A console entry point.

The lab. Harden the reconciliation script into a real package. Refactor to a src layout with three seams. An io module that fetches and reads. A pure reconcile module that compares two record sets and flags count drift and duplicate IDs. A cli module that wires them together.

Add type hints everywhere and get mypy to zero errors. Add contract docstrings. Write a pytest suite that loads a committed sample of the USGS feed as a fixture and parametrizes four edge cases: an empty feed, duplicate event IDs, a record missing a key field, and a metadata count that disagrees with the actual feature count. Every test runs against the pure function, so the suite runs offline and deterministically.

Write pyproject.toml. Build a wheel. pip install it into a clean venv. Run the reconciliation through its console command. README with install and run steps. Three-sentence why note: why the pure logic was split from I/O, and why that split is what made it testable.

A pass. The wheel installs into a fresh venv and the console command runs end to end. pytest passes, including all four edge cases. mypy or pyright reports zero errors. The reconcile logic is exercised by tests, not just imported. Docstrings match signatures.

The hot seat.

"Walk me to the seam between your pure reconcile function and your I/O. Why did you cut it there? Show me the one test that only exists because of that cut. Then tell me what a passing test suite does not prove about your package."

That last part matters. The honest answer is something like: it does not prove the live feed matches the fixture, it does not prove the API will not change shape, and it does not prove the annotation on this parameter is true at runtime. If you can name what your tests do not cover, I trust what they do.

Next month you carry this package into the core data engineering stage. Everything from here on imports from it.

**[on-screen / b-roll]** Lower-third: "Bridge · M04 · Software engineering hygiene." Cutaway A: the src layout tree, io / reconcile / cli, with a dashed line labeled "the seam." Cutaway B: pytest output, four parametrized cases passing, then mypy "Success: no issues found." Callout: "Green tests prove what you asserted. Nothing more."

---

## SWE-2: M05, SQL fundamentals (joins, filtering, aggregation, subqueries)
**Covers:** Launch weeks 9 and 10 · **Closes:** G1, G2, G10
**Target:** ~5 minutes (~720 words)

Write a LEFT JOIN from customers to invoices. Now add WHERE invoice date is after January. Congratulations, you just turned it back into an INNER JOIN. The customers with no invoices had NULL dates, the NULLs failed the filter, and they vanished. Nobody warned you. SQL never does.

You can code. This module is about thinking in sets and rows, which is a different skill, and two Launch weeks of it compressed into one. Week nine is joins and filtering. Week ten is aggregation and subqueries. No ORM. You write the SQL and you read the result like it might be lying to you.

Why it matters. Gap two is grain. Every bug in a data pipeline that is not a crash is a grain bug: a join that fanned out, a count that skipped NULLs, a group that means something different than the stakeholder thinks. You learn to state what one row of every result means.

The ideas, first half.

The query skeleton. SELECT, WHERE, ORDER BY, LIMIT. Predicates: comparison, IN, BETWEEN, LIKE, IS NULL.

Keys as the contract of a relational model. Primary and foreign keys, and how a relationship encodes grain.

Join types and their set semantics. INNER, LEFT and RIGHT OUTER, FULL OUTER, CROSS, self-join. What each one keeps and what it drops.

NULL and three-valued logic. How NULLs disappear from filters, behave in join keys, and appear from unmatched outer rows.

Reading an ERD and planning the join path before you type.

Second half.

Aggregates and GROUP BY. The grain of a grouped result. COUNT star versus COUNT column versus COUNT DISTINCT, and which NULLs each one skips.

WHERE versus HAVING, and the logical order of evaluation: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY. Why you can't filter an aggregate in WHERE.

Set operations. UNION versus UNION ALL, INTERSECT, EXCEPT.

Subqueries. Scalar, IN and EXISTS, derived tables, correlated versus not. And the NOT IN plus NULL trap that returns zero rows and looks like a correct answer.

The lab, in two parts, both on the Chinook database in DuckDB. No server. It loads from a file.

Part one. Eight to ten queries answering stated business questions. Filters that use IN, BETWEEN, LIKE, IS NULL. Multi-hop INNER JOINs down the artist, album, track, invoice item, invoice, customer chain. A LEFT JOIN that surfaces parents with no children: artists with zero tracks sold, customers with no invoices. A self-join from employee to manager. And one query that shows row fan-out, the count before and after a one-to-many join. Every query gets a comment naming the join type and why. One query is written twice, INNER and LEFT, so the diff in rows and counts is visible.

Part two. About ten analytical questions. Revenue per genre. Customers whose total spend is above the average. Top country by invoice count with a HAVING threshold. Tracks that appear in playlists but were never purchased, with EXCEPT or NOT EXISTS. Per-customer averages through a derived table. Each query gets a one or two sentence note stating the grain of the result and why the number is right. And you flag the one query where NOT IN would break on NULLs.

A pass. Every query runs and returns correct rows. The LEFT version returns parent rows with NULL child columns that the INNER version drops, and your note states the exact count difference. The fan-out query shows the count rising. The self-join resolves managers. Every grain note is factually correct. The pack shows GROUP BY with HAVING, a set operation, and a subquery. And you correctly identify the NOT IN trap and its EXISTS fix.

The hot seat, two questions.

"Show me your customers and invoice totals query. Defend LEFT versus INNER. Tell me exactly which rows appear or vanish if I swap it, and predict the row count change. Then run it and show me you were right."

"Point at one row of a GROUP BY result and tell me exactly what it represents. Then defend that your COUNT is counting the right thing and is not skipping NULLs or double-counting from a join."

The misconceptions: that a LEFT JOIN always preserves the left side, and that COUNT of a column counts every row. Both are wrong in ways that produce plausible numbers. That is what makes them dangerous.

**[on-screen / b-roll]** Lower-third: "Bridge · M05 · SQL fundamentals." Cutaway A: the same LEFT JOIN with and without the WHERE on the right table, row counts 59 and 47. Cutaway B: the logical order of evaluation as a vertical list, HAVING sitting below GROUP BY. Callout: "What does one row mean?"

---

## SWE-3: M06, Advanced SQL (windows, CTEs, query plans)
**Covers:** Launch weeks 11 and 12 · **Closes:** G1, G10, G7
**Target:** ~5 minutes (~700 words)

Top five pickup zones by trip count, per day. Easy. Now two zones tie for fifth. Does your query return five rows or six? And did the stakeholder get the answer they asked for, or the answer your ranking function happened to give?

Advanced SQL, two Launch weeks in one. Week eleven is window functions and CTEs. Week twelve is query plans and tuning. The first half is about getting the right answer. The second half is about getting it before the meeting.

Why it matters. Gap ten, communicating the work, hides in here. When you can explain why rank and row_number differ on a tie, or why the planner ignored your index, you can explain the result to someone who has to act on it. Gap seven, Spark intuition, starts with reading a plan on a single machine.

The ideas, first half.

Window function anatomy. OVER, PARTITION BY, ORDER BY, and the fact that rows are not collapsed. A window keeps every row. GROUP BY does not.

The ranking family. row_number, rank, dense_rank, and how each handles ties.

Offset functions. lag and lead for deltas, gaps, previous and next, without a self-join.

Frames. Running totals and moving averages with ROWS BETWEEN versus RANGE, and the default-frame trap: adding ORDER BY silently changes the frame.

CTEs for layered logic. Name each step. Chain them. A reviewer should read your query top to bottom.

Second half.

How a planner works. Logical plan, physical plan, cost model, and the table statistics it depends on.

EXPLAIN versus EXPLAIN ANALYZE. Estimated versus actual rows, BUFFERS, per-node timing.

Scan and join operators. Seq scan, index scan, bitmap heap scan. Nested loop versus hash join.

Indexes in depth. B-tree. Composite column order. Covering indexes. Selectivity.

Sargability. The predicate patterns that silently disable an index: a function on the column, a leading wildcard, an implicit cast.

Lab one. One month of NYC yellow taxi trips in DuckDB, joined to the zone lookup. Four business questions, one CTE-structured query each. Top five pickup zones per day, and you defend your ranking function on tie days. Day-over-day percent change in revenue using lag, flagging the biggest drop. A seven-day moving average of daily fare revenue with an explicit ROWS frame. A running cumulative total of trips within each day, partitioned by hour. Named CTEs only, no nested subquery pyramids. Every window has a PARTITION BY, ORDER BY, and frame you chose on purpose.

Lab two. The same month, about three million rows, loaded into local PostgreSQL. You are handed a slow query: a date range plus a pickup zone filter feeding an aggregation. Capture EXPLAIN ANALYZE with BUFFERS as the baseline. Name the bottleneck operator. Fix it: add or compose an index, rewrite the non-sargable datetime predicate, fix the composite key order. Re-measure. Every change is proven against the plan, not guessed.

A pass, lab one. Correct results, every query built from named CTEs, no subquery nested more than one level. The ranking query breaks ties the way your note claims. The lag query has the first day correctly NULL. The moving average uses an explicit six-preceding-to-current frame. The running total resets per day.

A pass, lab two. Both plans included. A measured, material speedup, seq scan to index or bitmap scan, runtime down five times or the gap explained. At least one non-sargable predicate rewritten. Every added index justified by selectivity. Row counts match the baseline, so no change hid cost by changing the answer.

The hot seat.

"You used rank, or row_number, for top five zones. What happens on a day where two zones tie for fifth? Who shows up in your output? Would the stakeholder's answer change if you had picked the other function?"

And: "Walk me through your plan. Which operator was the bottleneck? Why does your index fix it? Now name a query where this same index would be ignored, or would actually hurt."

The misconceptions: that a window collapses rows like GROUP BY, that the three ranking functions are interchangeable, and that adding an index always makes a query faster. An index can exist and be correctly skipped. If you can't say why, you do not understand the plan yet.

**[on-screen / b-roll]** Lower-third: "Bridge · M06 · Advanced SQL." Cutaway A: three columns, row_number / rank / dense_rank, on a five-row tie. Cutaway B: the EXPLAIN ANALYZE tree before and after, seq scan in red becoming index scan in green, with runtime numbers. Callout: "Prove it against the plan."

---

## SWE-4: M07, Relational theory and normalization
**Covers:** Launch week 13 · **Closes:** G2, G1, G10
**Target:** ~4.5 minutes (~620 words)

Adding a surrogate ID column to a table does not normalize it. It gives it a unique key. Those are different things, and a lot of production schemas have the first while claiming the second. Restaurant name, address, and cuisine repeated on every inspection row, with an auto-increment ID on the front, is still one wide denormalized file with a number on it.

This module is relational theory. Keys, functional dependencies, normal forms, referential integrity, and the deliberate denormalization you can defend. It is also the week you assemble the Phase 1 portfolio. One Launch week, one Bridge week, and the end of month one.

Why it matters. Gap two again. A schema is a set of claims about what depends on what. If you can't name the functional dependency that forced a table split, you drew boxes. And an interviewer will ask.

The ideas.

Keys. Super, candidate, primary, foreign. Natural versus surrogate. Why every table needs a declared primary key.

Functional dependencies. What X determines Y means, and how to find them by profiling the actual data rather than guessing from column names.

Normal forms. First: atomic values, no repeating groups. Second: no partial dependency on part of a composite key. Third: no transitive dependency through a non-key column. The decomposition procedure, and a nod to BCNF.

Referential integrity. Primary and foreign key constraints. Orphan rows. Cascade versus restrict.

Denormalization. The update, insert, and delete anomalies third normal form prevents, versus the read-speed reasons to deliberately break it.

The lab. NYC restaurant inspection results, a classic denormalized flat file: restaurant, inspection, and violation facts all in one wide row.

Profile it in pandas to discover the dependencies and the redundancy. Restaurant name and address repeat on every inspection. Cuisine and borough repeat. Draw an ERD. Design a third normal form schema: restaurant, inspection, violation, and lookup tables for cuisine and borough.

Write the DDL with declared primary keys and foreign key constraints in DuckDB or Postgres. Load the flat file into staging. Split it into the normalized tables with SQL. Then prove the constraints work: insert an inspection for a restaurant that does not exist, and show it rejected. Insert a duplicate primary key, and show it rejected.

Then add one deliberate denormalization, a reporting view or a column, and defend it in writing. Write a rationale doc listing the dependencies you found and justifying every split by the anomaly it removes.

Last, assemble the portfolio. A Phase 1 README that stitches this schema together with the SQL analytics and the Python work from the earlier weeks into one project that runs end to end from a fresh clone.

A pass. Every table declares a primary key. The schema is in third normal form or documents each exception with a reason. The constraints demonstrably reject the orphan and the duplicate. The rationale lists the actual dependencies in the data and ties each split to a specific normal form rule. The denormalization is justified in read-versus-write terms. The portfolio runs from its README on a fresh clone.

The hot seat.

"Walk me through one table you normalized. Name the exact functional dependency that forced the split. Name the specific anomaly it prevents. Then defend one place where you chose not to normalize."

The misconception I am hunting: blurring second and third normal form. Partial dependency on part of a composite key is second. Transitive dependency through a non-key column is third. If you say "it's normalized" and can't tell me which rule, we are going to the whiteboard.

That is month one for the SWE track. Next month you and the analyst track are on the same modules: dimensional modeling, SCD, lakehouse, MDM. The data gap is closed. Now you build on it.

**[on-screen / b-roll]** Lower-third: "Bridge · M07 · Relational theory and normalization." Cutaway A: one wide inspection row splitting into restaurant / inspection / violation boxes with the dependency arrows labeled. Cutaway B: a terminal showing the orphan insert rejected by the FK constraint. Callout: "Which rule forced the split?"
