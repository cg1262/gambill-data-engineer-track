# Week 10: Define what your count counts

Module M05 · [Course lesson](../../../site/phase-1.html#w10)

## Script

Two queries both say count. One returns ten, the other returns eight. Neither is necessarily broken. They may be counting different things, and your report needs to say which one it means.

Use the Chinook data to build a small analytics pack. Before each query, state its output grain. A `GROUP BY` creates one row per distinct grouping combination. If you group by country and month, the result is at country-month grain even if the source was one row per invoice.

Now compare the count functions. `COUNT(*)` counts rows. `COUNT(column)` counts nonnull values in that column. `COUNT(DISTINCT column)` counts distinct nonnull values. A left join adds another trap: a customer with no invoice still has an output row. Count the invoice identifier when the question is about invoices.

Use `WHERE` to filter input rows before grouping. Use `HAVING` to filter groups after aggregation. For example, select invoices from the chosen year, group them by customer, and then keep customers above a revenue threshold. Think of `WHERE` as choosing the receipts for the calculation and `HAVING` as choosing which completed totals to show.

Next, test a missing relationship with `NOT EXISTS`. `NOT IN` becomes surprising if its subquery contains null. An otherwise unmatched value can compare as unknown and fail the filter. Show the difference on a two-row example before trusting a large reconciliation query.

Use set operations intentionally. `UNION ALL` preserves duplicates; `UNION` removes duplicate result rows. That removal can hide an upstream problem or add work you did not need. `EXCEPT` and `INTERSECT` help compare compatible result sets, but a matching count alone does not prove matching content.

For your lab, keep every query rerunnable and annotate it with the grain and the reason it is correct. Check a reported total against an independently calculated reference. If the totals differ, inspect join multiplicity and null handling before rounding the difference away.

Practical advice: include the population in the metric's name. “Customers with at least one qualifying invoice” is much clearer than “active customers” when nobody has agreed what active means. Your SQL should encode a definition somebody else can repeat in a sentence.

## Screen example — not spoken

```sql
WITH x(v) AS (VALUES (1), (NULL))
SELECT COUNT(*) AS rows_seen,
       COUNT(v) AS populated_values,
       COUNT(DISTINCT v) AS distinct_values
FROM x;
```

Expect `2, 1, 1`. Contrast:

```sql
SELECT 2 AS candidate WHERE 2 NOT IN (1, NULL);
SELECT 2 AS candidate
WHERE NOT EXISTS (
  SELECT 1 FROM (VALUES (1), (NULL)) AS excluded(v)
  WHERE excluded.v = 2
);
```

The first returns no rows; the second returns candidate 2.
