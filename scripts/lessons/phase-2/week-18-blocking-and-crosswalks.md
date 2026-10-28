# Week 18: Find plausible matches without comparing everyone

Module M11 · [Course lesson](../../../site/phase-2.html#w18)

## Script

You want to find duplicate providers, so you compare every record with every other record. A million records gives you roughly half a trillion unordered pairs. Before choosing a similarity function, reduce the number of comparisons you are asking the system to make.

This week, build standardized match attributes and candidate pairs. Preserve raw names and addresses. Add normalized versions for comparison: consistent case, whitespace, punctuation, and documented address abbreviations. Standardization is a search aid, not evidence that two entities are identical.

Keep identifiers as strings. Leading zeros and source formatting rules can matter. Separate individual providers from organizations before comparing names. A person's first and last name and a hospital organization's name require different matching assumptions.

Create blocks that group plausible matches. One pass might use postal code and a normalized name prefix. Another might use city, street number, and a different name representation. Compare only within each block, union the candidate sets, and remove duplicate pairs.

Think of looking for a misplaced book. You check the expected shelf, then the neighboring shelf. You avoid searching the whole building, but you also avoid assuming that every misplaced book will still be in exactly the right section.

That is the trade-off. Narrow blocks are cheap but can miss true matches when an address or name is wrong. Broad blocks improve reach but can create huge pair sets. Record block sizes, put guardrails on oversized blocks, and inspect the records those guardrails exclude. A fast candidate generator with poor recall can make the later matcher look better than it is.

For self-comparison, use an ordering rule such as left ID less than right ID so you do not score both A-B and B-A, or compare a record with itself. Stable ordering also makes candidate output repeatable.

Build a crosswalk that records source identity, candidate or resolved master identity, status, and lineage. An unresolved source record remains visible. You have generated possibilities this week; you have not yet earned the right to merge them.

For the lab, show two blocking passes, the reduction from the all-pairs baseline, and the fate of un-blockable records. Test candidate recall against a small labeled set of known matches. Your practical goal is to make the expensive decision smaller while keeping track of the matches you might have missed.

## Screen example — not spoken

Spark SQL; standardized provider fixture with unique string `record_id` values:

```sql
WITH candidates AS (
  SELECT a.record_id AS left_id, b.record_id AS right_id
  FROM provider_match_input a JOIN provider_match_input b
    ON a.zip = b.zip AND a.name_prefix = b.name_prefix
   AND a.entity_type = b.entity_type AND a.record_id < b.record_id
  UNION
  SELECT a.record_id, b.record_id
  FROM provider_match_input a JOIN provider_match_input b
    ON a.city = b.city AND a.street_number = b.street_number
   AND a.entity_type = b.entity_type AND a.record_id < b.record_id
)
SELECT * FROM candidates;
```

Apply block-size limits before the joins. `UNION` intentionally deduplicates pairs found by both passes.
