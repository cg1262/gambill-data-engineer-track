# Week 12: Tune the work the database actually does

Module M06 · [Course lesson](../../../site/phase-1.html#w12)

## Script

You added an index and the query barely changed. Before adding another one, ask what the database actually did. An index is an available route. The planner still decides whether that route is useful for this query and this data.

Use the multi-year weather table in PostgreSQL for this lesson. Load the documented data volume, record the row count, and run `ANALYZE` so the planner has current statistics. Keep this environment separate from the earlier DuckDB exercises; the operators and index behavior we are examining here are PostgreSQL's.

Capture a baseline with `EXPLAIN (ANALYZE, BUFFERS)`. Plain explain shows estimates. Analyze executes the query and reports observed execution statistics. Start with a read-only select so the measurement does not unexpectedly modify data.

Look at estimated versus actual rows, scan type, loops, and buffer activity. Node times and repeated loops need interpretation; do not add every displayed duration together and call that total runtime. Find the expensive part of the plan before changing anything.

Now inspect your predicate. Wrapping a date column in a year-extraction function can prevent a normal index on that column from supporting the filter directly. Rewrite the condition as a half-open range: on or after January first, and before January first of the next year. This tells the database which interval you want without transforming every stored date for the comparison.

Create an index that matches the actual access pattern. If queries select one station and then a date range, a composite index beginning with station and then date is a candidate. Think of a book index organized by subject and then page: its ordering helps particular lookups, not every possible question.

Measure again under comparable conditions. Keep the dataset, parameters, and relevant configuration fixed. Account for warm caches and background activity. A sequential scan can still be the right plan when you need much of the table; do not force an index just to match a screenshot.

For the lab, save both plans, row counts, timings, and buffer evidence. Verify that the rewritten query returns the same result. Explain one index you chose and one you declined, including storage and write costs.

Your useful deliverable is a diagnosis supported by evidence. If the planner still scans, investigate selectivity and statistics rather than reporting an improvement you did not observe.

## Screen example — not spoken

PostgreSQL; replace `weather_obs` and column names with the learner's loaded schema:

```sql
ANALYZE weather_obs;
EXPLAIN (ANALYZE, BUFFERS)
SELECT AVG(temperature)
FROM weather_obs
WHERE station_id = 'YOUR_STATION'
  AND obs_date >= DATE '2023-01-01'
  AND obs_date <  DATE '2024-01-01';

CREATE INDEX IF NOT EXISTS weather_station_date_idx
ON weather_obs (station_id, obs_date);
```

Rerun the same explain after index creation. No particular plan or speedup is guaranteed in advance.
