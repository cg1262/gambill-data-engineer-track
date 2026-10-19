# Sharpen, Month 1: Lesson Scripts

Sharpen is modular, so "month one" is a choice. This file takes the path the Sharpen video sends people down: run the self-diagnostic, then take the first bundle it names, Incremental and CDC Mastery, which closes G3 (kill the full-refresh habit). That bundle is four modules: M13 (week 20), M15 (week 22), M16 (weeks 23 and 24), and M23 (weeks 35 and 36). Month one covers the diagnostic plus the first four weeks: M13, M15, and both halves of M16. M23, streaming, is month two.

One script per lesson week, plus a kickoff that walks the diagnostic.

Target: kickoff ~3 minutes; lesson videos about 5 minutes. Voice as the welcome videos. These learners are working engineers, so the scripts assume vocabulary and skip the "why Git" framing.

Design note for Chris: the four labs in this bundle run on the course's worked project, Provider Pricing Integrity (CMS hospital price transparency files plus NPPES providers), and they build on the bronze landed in week 21 (M14), which is not in the bundle. The kickoff tells Sharpen learners to either run the week 21 lab first as a warm-up or point the same steps at a source they already own. If you would rather add M14 to the bundle, the chip list in `build/render_paths.py` is the one place to change.

Source of truth: `site/sharpen.html` and `site/phase-2.html` weeks 20, 22, 23, 24. If the pages change, change the scripts.

---

## Kickoff: Run the diagnostic, pick your bundle
**Target:** ~3 minutes (~450 words)

You are already doing the job. So this is not a course start. It is an audit.

Ten questions. Rate yourself one to five on each, and be honest, because nobody is grading the rating. They are grading the pipeline you ship next quarter.

G1. Can you explain why you built something the way you did?
G2. Do you choose grain deliberately?
G3. Is overwrite ever your bronze strategy?
G4. Do you have a real testing taxonomy?
G5. Could you dedup a composite key in a stream?
G6. Do manual workspace changes ever survive deploy?
G7. Can you read a Spark UI and act on it?
G8. Is governance designed in, or bolted on?
G9. Can you defend an architecture, not just name tools?
G10. Can you narrate your work to a stakeholder?

Every gap on the Sharpen page maps to the modules that close it, and every module links straight to its lesson week. Score low on G7, you go to M17, M18, M19. Score low on G3, you go to M15 and M16. You do not need to have done the earlier modules. Every unit stands alone.

Or grab a bundle. Eight of them. Each one is a cluster of gaps that tend to travel together.

This month I am walking the first one: Incremental and CDC Mastery. It closes G3. If your bronze layer is a full overwrite every night, if a rerun after a failed job doubles a count, if you have ever typed "truncate and reload" into a production schedule, this is the bundle. Four weeks. Week 20, the architecture doc: ELT versus ETL, batch versus incremental, written down and defended. Week 22, medallion as enforceable layer contracts, with tests that fail loud. Week 23, watermarks. Week 24, idempotency, backfills, and the ten-times rerun test.

One practical note. These four labs run on the course's worked project, hospital price transparency files from CMS joined to NPPES provider records. They build on a bronze table landed in week 21. If you want the labs exactly as written, run week 21 first as a warm-up. It is a one-week ingestion lab. If you would rather not, point every step at a raw table you already own. The pattern is the same: append-only bronze with an ingest timestamp, a control table, a keyed MERGE.

The weekly live review is there if you want to pressure-test anything. You do not have to come. But saying a decision out loud, to someone who will push back, is the fastest way to find out whether you understand it or just remember it.

Run the diagnostic. Pick the bundle. Week 20 starts with a blank architecture doc, and that is the point.

**[on-screen / b-roll]** Lower-third: "Sharpen · Self-diagnostic · 10 gaps." Cutaway A: the ten questions as a list, G3 highlighted. Cutaway B: the eight-bundle grid, Incremental and CDC lit, with the four module chips beneath it. Callout: "Week 21 first, or your own bronze."

---

## Week 20: ETL vs ELT, batch vs incremental. Write the architecture doc
**Module:** M13 · **Closes:** G9, G6, G1
**Target:** ~5.5 minutes (~750 words)

"Why Databricks?" An interviewer asked a candidate that last year and got "because it's modern." That answer is worth nothing. The real answer names the alternatives you rejected and the specific reason each one lost. If you can't produce that, you did not make an architecture decision. You picked a logo.

Week 20 has no new data. It is a design week. You write the four-part architecture doc for the Provider Pricing Integrity project, and you decide, in writing, ELT over ETL, medallion over folders, incremental over full reload. Then you defend each one.

Why it matters. Gap nine is the one that costs senior engineers the senior title: naming tools instead of defending choices. And gap six, confusing batch with incremental, is why so many pipelines reprocess a full month of provider data every night and call it safe.

The ideas.

ETL versus ELT. Where the transform lives. ELT lands raw bytes in Delta first, then transforms in place with Spark SQL. Classic ETL transforms in flight before landing. ELT wins when storage is cheap, sources are messy and re-parseable, and you want replayable raw. The CMS pricing files are the argument: every hospital publishes its own format, CSV, JSON, XML, inconsistent column names. You can't pre-clean a schema you have not seen yet.

Batch versus incremental versus streaming. Full reload, delta load, continuous. Latency, cost, complexity. CMS republishes monthly. NPPES drops a full bulk file monthly. That is incremental batch. Not streaming, there is no sub-daily source. And not full reload, millions of rows every run melts a Free Edition budget and misses the month-end deadline. One more thing: a small conformed dimension is often correctly a full overwrite. The decision is per table, not a slogan.

Medallion as enforceable layer contracts. Bronze: raw, append-only, source and ingest timestamp, no transforms. Silver: validated, typed, conformed, historized, quality-gated with quarantine. Gold: business-ready, serve-only. The useful question for each layer is what is forbidden there. If you can't say what would violate the contract, you drew folders.

Architecture decision records and the tool-selection log. Context, options considered, decision, consequences. "We chose Databricks" is worthless without the rejected alternatives. The log is your interview answer to "why this stack."

The lab. Write ARCHITECTURE.md and link it from the project README. Four parts.

One, a data-flow map. Bronze to silver to gold, with the grain, the layer contract, and the exact transform boundary at each hop. The starter scaffold introspects the Delta tables you already have, so the map cites real table names and real row counts, not a fictional diagram.

Two, two ADRs, ELT over ETL and incremental over full, plus a tool-selection log naming at least three rejected alternatives. Snowflake, dbt on Postgres, Airflow with pandas, whatever you seriously considered, each with a specific reason it lost against Databricks and Delta for this project.

Three, a failure plan. At least four named failure modes. A 429 from the NPPES API. Schema drift in a hospital pricing file. A late-arriving CMS republish. A duplicate provider explosion in MDM. Each with a detection signal and a response: quarantine, retry, alert, or fail loud.

Four, an idempotency plan. A rerun strategy per layer, MERGE on key, replace partition, or full overwrite, and the ten-times rerun test that proves identical row counts.

Add a one-page why note on the hardest trade-off.

A pass. The map states grain, contract, and transform boundary for all three hops and cites real counts. The ELT and incremental decisions each list options and at least two project-specific consequences. Generic "ELT is modern" gets rejected. The log names three rejected alternatives with specific reasons. The failure plan has four modes with distinct detection and a concrete response that references the actual quarantine tables. The idempotency plan assigns a strategy per layer with justification. The doc does not require Unity Catalog, DLT, or DABs; that is Phase 3. And a peer can read it in five minutes and predict what week 21 builds.

The hot seat. I play a skeptical staff engineer.

"This is overengineered. Just full-overwrite every table from the raw files every night. It's trivially idempotent and you never worry about late records or MERGE bugs. Why ELT? Why incremental? Why the whole medallion ceremony?"

You have to justify ELT with a specific CMS file-format reason. Justify incremental against both full reload and streaming. And concede where full overwrite actually is your chosen strategy, because the decision is per layer, not dogma. If you can't concede, you are not defending, you are reciting.

**[on-screen / b-roll]** Lower-third: "Week 20 · M13 · The architecture doc." Cutaway A: the four-part doc as four cards: data-flow map, ADRs and tool log, failure plan, idempotency plan. Cutaway B: a tool-selection log table, three rejected rows with a reason column. Callout: "Name what you rejected."

---

## Week 22: Medallion architecture. Enforcing layer contracts
**Module:** M15 · **Closes:** G3 · **Seeds:** G2
**Target:** ~4.5 minutes (~650 words)

Two dashboards. Same hospital. Two different total charges. Finance built one, compliance built the other, and each team cleaned the pricing data its own way because nobody agreed on where cleaning happens. Now an auditor is asking which number is right, and the honest answer is "depends which notebook."

This week you put the bronze you landed in week 21 under contract. Bronze, silver, gold stop being three folder names and become three written, tested promises. Then you break one on purpose to watch the guardrail catch it.

Why it matters. G3 is the full-refresh and leaky-layer gap. Transforms leak into bronze, re-cleaning sneaks into gold, and reproducibility dies quietly. Enforced contracts make one layer the single source of clean truth, so a hospital's price is computed once, provably, and the same everywhere.

The ideas.

Medallion as contracts, not folders. Each layer promises something to its consumer, and a leaked transform breaks the promise silently. Frame every layer as a contract with a producer and a consumer.

The bronze contract. Raw, append-only, provenance: source file, ingest timestamp, source system. Untyped and unfiltered, so you can always replay history and prove what CMS actually published on a given day.

The silver contract. Clean, conform, and later, historize. Typing, trimming, code and unit standardization. A documented primary-key grain. Quality gates and quarantine. This week you build the clean and conform half. SCD2 is flagged as the week 23-plus extension so silver stays honest about what it does.

The gold contract. Serve-only. Reads from silver only. No cleaning downstream of silver. The enforcement rule: if you need to clean it in gold, it belongs in silver.

Enforcing contracts with cheap tests. Schema assertions. StringType checks. Row-count monotonicity. Reconciliation: passed plus rejected equals input. Guardrails that fail loud in Databricks so a broken layer is never silent.

The lab. Write LAYER_CONTRACTS.md, one page, each layer with allowed, forbidden, grain, and owner. Then encode it.

Three automated assertions on bronze. The ingest-metadata columns are present. The payload columns are still raw strings. The row count only ever grows. Each one raises a named error on violation.

A thin silver conform step. Type, trim, and standardize at least four fields: charge as a decimal, provider name, two-letter state, zero-padded ZIP. Declare the silver primary-key grain in writing. Every row that fails the contract goes to a rejected table with a specific reject reason and a reject timestamp. Zero silent drops. Assert in code that passed plus rejected equals input.

Gold as a view over silver. Then add a line of cleaning logic in gold and show the contract test failing.

Finish with the break-it drill. Cast a column in bronze. Watch the assertion fire. Revert. Run the notebook ten times and show identical silver counts. Write a README why note: your idempotency choice, which contract you broke, how the guardrail caught it.

A pass. Bronze assertions fail loud when metadata is missing, a payload column is cast, or the count shrinks. Silver standardizes four fields and has a written grain that matches the dedupe key. Every non-passing row is in silver_rejects with a reason, and the reconciliation is asserted in code. Ten runs, identical counts. Gold is a view over silver only, and its test fails when cleaning or a bronze reference is added.

The hot seat.

"Why is this the grain of one silver charge row, and what breaks if you picked a coarser or finer key? You put ZIP zero-padding in silver and currency-symbol stripping in silver. Justify why neither belongs in bronze or gold. Now show me the one line where you chose MERGE on key versus overwrite partition, and defend it against the alternative."

Be ready to point at the code and at the line in LAYER_CONTRACTS.md that authorizes it. The misconception I am hunting: that silver should do everything, including business aggregates. Aggregates are gold. Silver stops at clean, conform, and historize.

**[on-screen / b-roll]** Lower-third: "Week 22 · M15 · Layer contracts." Cutaway A: three columns, bronze / silver / gold, each with an ALLOWED and FORBIDDEN list. Cutaway B: a notebook cell casting a bronze column, then the assertion error in red with its name. Callout: "If you clean it in gold, it belongs in silver."

---

## Week 23: CDC and incremental I. Watermarks: load only what changed
**Module:** M16 · **Closes:** G3
**Target:** ~5 minutes (~730 words)

Here is a sentence that sounds right and is wrong: "a watermark makes my reruns safe." It does not. A watermark tells you what to read. It says nothing about whether writing that slice twice corrupts silver. You will see the double-count this week with your own eyes, and we leave it in on purpose. Next week fixes it.

Week 23 turns the one-shot medallion load from week 22 into a resumable, incremental load. You stand up a control table, read only what is newer than the stored mark, and advance the mark only on success.

Why it matters. CMS republishes pricing files on a rolling schedule. A pipeline that reprocesses every historical file and all of NPPES on every run takes hours, melts a Free Edition budget, and misses the month-end compliance deadline. Touch only the periods that changed and the freshness SLA is met.

The ideas.

Full refresh versus incremental, the money argument. When full refresh is actually correct: small dimensions, first load, a schema break. When incremental is mandatory: millions of rows, a monthly republish, a freshness promise.

What a watermark is. The maximum value of a monotonic column you have already processed. The loop: read past the mark, process, advance the mark. Bootstrapping with a null or epoch mark on the first run. Backfill versus steady state.

Where the watermark lives. A notebook variable, a widget, a config cell: all bugs. Lost on restart, not shared, not auditable. A Delta control table is the home. One row per source and layer, updated transactionally, queryable as an audit trail.

Change detection for CMS data. File arrival, a last-updated column, or the Delta ingest timestamp. Bronze to silver should watermark on ingest time. It is append-only, monotonic, and you control it. The source's last-updated date is none of those things.

Late and out-of-order data, and the honest limit. A record with an old event date but a new ingest time. An event-time watermark silently skips it. An ingest-time watermark catches it. And the boundary you write down: a watermark decides what to read, idempotency decides whether a rerun is safe. Different problems.

The lab. Land the CMS pricing source as three simulated republish periods into append-only bronze, with source, ingest timestamp, and a period label. Mutate a subset of rows between periods so something actually changes.

Create a Delta control table: source, layer, watermark column, watermark value, run timestamp. Read only rows where the ingest timestamp is past the stored mark into silver. Measure incremental count against the full-table count. Advance the mark only on success.

Then prove it. A rerun with no new data processes zero rows and leaves the mark untouched. A new period flows only its own rows and the mark advances to that period's max ingest timestamp. A simulated failure before the write leaves the mark where it was. And a deliberately late record, old event date, new ingest time, shows which watermark drops it.

Write a two to three hundred word why note. Update the architecture doc's data-flow map with an incremental node, seed the idempotency section, and add the advance-on-success guard to the failure plan.

A pass. The watermark value lives in a Delta table, not a variable, and survives a cluster restart. A no-new-data run processes exactly zero rows and leaves the value byte for byte unchanged. After a new period, the incremental count equals only that period's rows. The failure guard is proven. The late-record case is demonstrated and the ingest-versus-event-time choice is explained in writing. And the why note names the append double-count as next week's follow-up instead of hiding it.

The hot seat. Three decisions.

"Why did you watermark on ingest timestamp instead of the source's last-updated column? Give me the specific CMS failure that choice protects against. Why is the mark in a Delta control table and not a notebook widget? What breaks if a hiring manager reruns your notebook on a fresh cluster? And show me your advance-on-success-only guard. What does the pipeline do on the next run after a mid-run failure?"

Bonus: "Your append still double-counts on rerun. Why did you ship it that way this week instead of hiding it?" The right answer is that you know exactly what the gap is and what closes it. That is engineering honesty, and it reads better in a review than a hidden bug.

**[on-screen / b-roll]** Lower-third: "Week 23 · M16 · Watermarks." Cutaway A: the control table, one row per source and layer, with the watermark value advancing across three runs. Cutaway B: a late record, event date in March, ingest in May, with the event-time mark skipping it and the ingest-time mark catching it. Callout: "A watermark decides what to read. Not whether a rerun is safe."

---

## Week 24: CDC and incremental II. Idempotency, backfills, and the ten-times test
**Module:** M16 · **Closes:** G3, G4
**Target:** ~5 minutes (~730 words)

A cluster died halfway through the CMS ingest. The team reran it. The silver load was append-only, so the same provider batch landed twice. "Facilities analyzed" went up by a number nobody could explain, and the average negotiated rate on a compliance filing shifted. That is not a bug report. That is a retraction.

This week closes the gap you left open on purpose last week. The silver load becomes idempotent. You backfill a historical month without regret. And you build a harness that proves it, ten runs, zero variance, fails loud if anything moves.

Why it matters. G3 and G4 together. Safe to rerun and safe to backfill is the difference between a defensible number and a public correction. And "safe to rerun" is a claim you demonstrate, not assert.

The ideas.

What idempotent means for data. At-least-once delivery, retries after a half-finished job, and why append-only loads silently duplicate. A rerun that doubles a provider count is a silent compliance error, and silent is the worst kind.

Delta MERGE, properly. The ON clause has to be the true natural key. whenMatched, update on change or update all. whenNotMatched, insert. MERGE requires at most one source row per key, so you dedupe in-batch first. And MERGE combined with the SCD2 two-step, close the old row, insert the new one.

Three idempotency strategies. MERGE on key, best for dimensions and entities. replaceWhere or dynamic partition overwrite, best for reloading one month of a partitioned fact. Full overwrite, for small reference tables. When each is correct, and the blast radius of each when you are wrong.

Backfills without regret. Reprocessing a historical month versus incremental append. Deterministic transforms as the precondition. The ordering hazard when you backfill into SCD2 history. A backfill reruns an old batch ID, not a new one.

Idempotency as a testable contract. The ten-times test. An assertion harness. "Safe to rerun" as something you show an interviewer.

The lab. Convert the week 23 silver load from append to MERGE keyed on the provider's NPI. Dedupe in-batch first, because the monthly NPPES file can contain the same NPI twice. Switch the pricing fact to month-partition overwrite with replaceWhere, because you reprocess a whole month at a time and row-level MERGE is the wrong tool for that grain.

Backfill one historical NPPES month into the existing silver provider dimension. No duplicates, and the backfill must not flip a newer current-flag row to an older version.

Build the ten-times harness. Reload the same batch ten times. Assert row count, distinct-key count, and current-flag count never move. Raise if they do. Then feed it a deliberately non-deterministic transform, a current_timestamp in a business column, and watch it fail.

Screenshot the original append duplication bug. Keep it. Write the idempotency plan section of the architecture doc, one row per table: strategy, natural key, ten-times evidence. Add a backfill runbook. One hundred fifty to two hundred fifty word why note defending strategy per table.

A pass. Ten runs on the same batch: identical row count, distinct NPI count, and current-flag count. Current-flag rows equal distinct NPIs. The historical backfill adds zero duplicate NPIs and leaves exactly one current row per provider. The pricing fact uses partition overwrite, not MERGE, with a written reason. The harness raises on the non-idempotent transform. Quarantined records are not resurrected by a rerun. Each run appends one audit-log row.

The hot seat.

"You used MERGE on key for providers but partition overwrite for pricing. Why not the same strategy for both? What is the blast radius if your idempotency assumption is wrong? And prove to me, right now, that a rerun of last month's backfill will not double-count facilities."

The misconception, and it is the big one: "MERGE makes any load idempotent." It does not. MERGE is idempotent only if the ON clause is the true natural key, there is at most one source row per key, and every transform is deterministic. A timestamp written into a business column, or a duplicate key in the batch, fails the ten-times test even with MERGE. Idempotency is a property of the whole load, not of a keyword.

That is the bundle's first month. You walked in with a full-refresh habit. You walk out with a watermark, a keyed MERGE, a backfill runbook, and ten runs of evidence. Next month is streaming semantics, where the same questions show up with state and time attached.

**[on-screen / b-roll]** Lower-third: "Week 24 · M16 · Idempotency and the 10x test." Cutaway A: the original bug, provider count 41,207 then 82,414 after a rerun, in red. Cutaway B: the harness output, ten rows, three columns, every value identical, in green. Callout: "Idempotency is a property of the load, not the MERGE keyword."
