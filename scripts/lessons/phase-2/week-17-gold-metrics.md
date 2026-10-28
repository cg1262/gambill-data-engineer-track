# Week 17: Give the metric one definition

Module M10 · [Course lesson](../../../site/phase-2.html#w17)

## Script

Two dashboards both report pricing completeness. One counts rows with any price. The other requires a valid procedure, payer, and negotiated amount. Both teams used the same source. They built different metrics.

This week, make gold the place where the business definition becomes explicit and reusable. Start with the consumer question from your charter. Write the population, qualifying rule, period, numerator, denominator, and treatment of missing values before writing the final select.

Suppose the agreed KPI is the proportion of eligible facilities meeting a required-field completeness rule in a source period. First produce one evaluated result per facility and period. Then aggregate those results. If you calculate the proportion directly over raw price lines, hospitals with larger files can dominate the answer. You changed the denominator without saying so.

It is like taking a class attendance rate by counting submitted homework pages. Students who wrote more pages would receive more votes. Your metric needs to count the entity the business actually cares about.

Build gold from the validated silver model. Keep source parsing and common standardization in silver so multiple marts do not each invent their own cleaning rules. Business aggregations and consumption-friendly naming belong in gold, with their definitions documented alongside them.

When using Type 2 dimensions, choose current versus as-of semantics explicitly. Current means describe every fact using today's selected attributes. As-of means use the version valid at the relevant fact time. Joining a fact to full dimension history without a temporal condition can inflate your results.

Choose a view when querying the underlying data is affordable and you want the current definition applied immediately. Materialize when refresh cost and response time justify storing the result. A stored table adds a freshness obligation: someone must refresh it and expose when that happened.

For the lab, define the canonical completeness calculation once, link the consumer-facing output to it, and reconcile its evaluated population with silver. Test nulls, duplicate facility-period evaluations, and an empty denominator. An undefined rate should not quietly become zero percent.

Finish by explaining one metric row in ordinary language. Name exactly who was counted and who was excluded. A useful semantic layer lets a consumer understand the answer without reconstructing all of your pipeline code.

## Screen example — not spoken

DuckDB; the input is already unique at facility-period grain:

```sql
WITH evaluated(facility_id, period, eligible, passes) AS (
  VALUES ('A', '2024-01', TRUE, TRUE),
         ('B', '2024-01', TRUE, FALSE),
         ('C', '2024-01', FALSE, FALSE)
)
SELECT period,
       SUM(CASE WHEN eligible AND passes THEN 1 ELSE 0 END) AS numerator,
       SUM(CASE WHEN eligible THEN 1 ELSE 0 END) AS denominator,
       1.0 * SUM(CASE WHEN eligible AND passes THEN 1 ELSE 0 END)
         / NULLIF(SUM(CASE WHEN eligible THEN 1 ELSE 0 END), 0) AS completeness
FROM evaluated GROUP BY period;
```

Expect numerator 1, denominator 2, completeness 0.5. The production rule for `passes` must come from the charter.
