# Week 46: State the grain before you start typing

Modules M36 / M35 · [Course lesson](../../../site/phase-4.html#w46)

## Script

The interviewer asks for the latest provider record. You immediately type a window function. Then they ask what happens when two records have the same timestamp, and you discover you never defined latest.

This week, practice a technical answer with a clear sequence. Restate the requested output grain. Clarify the ordering and tie policy. Choose the pattern. Then write the query and test the uncomfortable case.

For latest-per-provider, `ROW_NUMBER` over a provider partition is a familiar pattern. Order by the appropriate business update time and a stable tiebreaker supported by the source. A random row order is not a policy. If the source gives no way to resolve conflicting equal-time records, say that and propose review or another explicit rule.

For running totals, name the partition and frame. For an as-of lookup, name the effective-time interval. For reconciliation, consider anti-joins. Recognizing the pattern is useful, but explaining the conditions under which it is correct is the part that transfers between systems.

Think of the answer as assembling a small proof. The grain is the claim, the query is the method, and the fixture is the evidence. A tiny counterexample can reveal a mistake much faster than narrating every keyword.

For system design, use six connected decisions: output grain, source and change detection, layer boundaries, retry and backfill behavior, quality controls, and governed serving. Start from the latency and volume requirements. Do not add streaming or a distributed engine before the problem needs them.

Use your own project to provide concrete evidence, while separating a course simulation from production experience. You can say you injected a duplicate and proved a rerun safe. You do not need to turn that into an invented client incident.

For the take-home exercise, build a complete thin slice. Include a runnable entry point, small fixtures, meaningful tests, and a README that names assumptions and trade-offs. Leave a clear boundary around work you could not complete rather than hiding unfinished behavior behind a broad architecture.

For the lab, time a SQL drill, a system-design explanation, and a clean-clone review. Grade correctness, failure reasoning, and clarity separately from speed.

Practical advice: speak while the reasoning is still small. A sentence about the grain and one boundary test will usually help the interviewer follow you more than a silent page of code followed by a long explanation.

## Screen example — not spoken

DuckDB, synthetic update ordering:

```sql
WITH updates(provider_id, updated_at, source_sequence, name) AS (
  VALUES ('P1', TIMESTAMP '2024-01-01', 1, 'Old'),
         ('P1', TIMESTAMP '2024-01-01', 2, 'Corrected')
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY provider_id ORDER BY updated_at DESC, source_sequence DESC
  ) AS position
  FROM updates
)
SELECT provider_id, name FROM ranked WHERE position = 1;
```

Expect `P1, Corrected`. Explain why the source sequence is authoritative in this fixture before using it as a tiebreaker.
