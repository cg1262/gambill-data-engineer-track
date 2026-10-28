# Week 11: Make the window match the question

Module M06 · [Course lesson](../../../site/phase-1.html#w11)

## Script

Your dashboard says yesterday's temperature changed by twelve degrees. The previous observation was actually three days ago. The subtraction is correct. Calling it a daily change is wrong.

This week, work with a fixed NOAA weather extract and use window functions to keep that distinction visible. First quarantine the source's missing-value sentinels and disallowed quality flags. Document the unit conversion for each measurement. A value of minus nine thousand nine hundred ninety-nine is a missing-value marker in the fields covered by this lab, not a record-breaking temperature.

A window function calculates across related rows while preserving the rows themselves. `PARTITION BY` chooses the group. `ORDER BY` chooses the sequence. The frame chooses which neighbors participate. Think of it as a moving reading lens over a stack of station observations: changing the stack, order, or lens changes the answer.

Use `LAG` for the previous observed value, and also lag the observation date. Calculate a daily delta only when the two dates are adjacent. Otherwise return null or a separately labeled gap result. Do not silently treat missing days as measured days.

Now calculate the lesson's seven-observation average with an explicit `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` frame. That is seven rows, not automatically seven calendar days. If the business question needs calendar coverage, build a date spine or use an appropriate time-based frame and define how missing days affect the result.

For ranking, choose your tie behavior. `ROW_NUMBER` assigns different positions and needs a deterministic tiebreaker if you want repeatable ordering. `RANK` leaves gaps after ties. `DENSE_RANK` does not. The function name is part of your metric definition.

Use CTEs to name the steps: clean observations, previous observation, then final metrics. They make the reasoning readable; they do not guarantee a particular materialization or performance improvement.

For the lab, show a station gap and a tied ranking. Explain the result before executing the query. Then rerun the clean load and confirm both the accepted and rejected populations are accounted for without duplication.

The practical habit is to put the time assumption beside the calculation. “Previous reported observation” and “previous calendar day” are different promises. Your consumer should never have to discover that difference after making a decision.

## Screen example — not spoken

DuckDB example, already-clean synthetic temperatures:

```sql
WITH obs(station, day, temp) AS (
  VALUES ('A', DATE '2024-01-01', 10),
         ('A', DATE '2024-01-02', 12),
         ('A', DATE '2024-01-05', 20)
), previous AS (
  SELECT *, LAG(day) OVER w AS prev_day, LAG(temp) OVER w AS prev_temp
  FROM obs WINDOW w AS (PARTITION BY station ORDER BY day)
)
SELECT day,
       CASE WHEN day - prev_day = 1 THEN temp - prev_temp END AS daily_delta,
       AVG(temp) OVER (PARTITION BY station ORDER BY day
                      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS avg_observed
FROM previous ORDER BY day;
```

January 5 has no daily delta. Its observed-row average still includes January 1 and 2.
