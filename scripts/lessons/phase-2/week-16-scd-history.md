# Week 16: Answer what was true on the report date

Module M09 · [Course lesson](../../../site/phase-2.html#w16)

## Script

A provider changes address in April. You rerun a March report and it suddenly shows the April address. The latest data is correct, but you have lost the ability to reconstruct the earlier report.

This week, preserve selected attribute changes with slowly changing dimension Type 2. First decide which changes deserve history. A genuine address change may create a new version. A spelling correction may be Type 1, depending on your business policy. Keep that policy explicit so every changed column does not automatically produce another historical row.

Each version needs a business key, a version-specific surrogate key, an effective start, an effective end, and a current-row indicator. Use half-open intervals: include the start, exclude the end. If the old version ends exactly when the new one starts, a timestamp at that boundary resolves to the new version only.

Half-open notation makes the boundary clear; it does not enforce valid history by itself. Test that intervals do not overlap, that required continuity holds, and that each business key has exactly one current row. Think of a lease history: the dates must agree, not merely use the same date format.

Detect changes using the tracked attributes. If you hash them, serialize field boundaries and nulls unambiguously. Plain concatenation can make different records produce the same input string before hashing even begins.

For a changed key, close the existing version and insert the replacement. A straightforward matched branch of a merge cannot also insert the replacement for that same matched source row. Use a documented staged-merge pattern, or make a two-step implementation recoverable. If expiration succeeds and insertion fails, your recovery must repair the missing current version.

For an as-of join, require the fact's relevant time to fall within the version interval. Verify one matching version per fact. Joining to every version of the provider will multiply the fact rows.

For your lab, use two fixed snapshots. Show one real change, one unchanged row, a rerun, and an as-of query across the boundary. Separate business effective time from when you learned about the change.

The practical advice is to test historical behavior as deliberately as current behavior. A current-row count can look perfect while last month's report is already wrong.

## Screen example — not spoken

DuckDB, synthetic history:

```sql
WITH versions(provider, address, start_at, end_at) AS (
  VALUES ('P1', 'Old address', TIMESTAMP '2024-01-01', TIMESTAMP '2024-04-01'),
         ('P1', 'New address', TIMESTAMP '2024-04-01', NULL::TIMESTAMP)
)
SELECT address FROM versions
WHERE provider = 'P1'
  AND TIMESTAMP '2024-04-01' >= start_at
  AND (end_at IS NULL OR TIMESTAMP '2024-04-01' < end_at);
```

Expect only `New address`. The example demonstrates interval lookup, not a complete SCD2 writer.
