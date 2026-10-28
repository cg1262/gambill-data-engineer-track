# Week 23: Keep a durable record of what you consumed

Module M16 · [Course lesson](../../../site/phase-2.html#w23)

## Script

Your notebook remembers the last processed timestamp until the notebook restarts. Then it either reloads everything or skips a batch. A value in notebook memory is not a durable record of progress.

This week, persist a high-water mark in a control table. Keep one record for the source and target boundary it describes. The mark tells you what input has been consumed. It does not automatically make writing that input twice safe.

First choose the ordering carefully. A source event date can be old even when the record arrives today. An ingestion marker is often better for discovering newly landed records, but a wall-clock timestamp alone is not guaranteed to follow commit order. Two batches can share a timestamp, or an earlier timestamp can commit later.

For the lab's controlled source, define a committed batch sequence or a timestamp-and-tiebreaker rule that supports your assumptions. Another design uses an overlap window plus idempotent deduplication. Document the guarantee instead of assuming that “greater than the last timestamp” cannot miss anything.

At run start, choose a fixed upper boundary. Read the interval after the stored mark through that boundary. This makes the input slice stable while new records continue landing. Think of putting a bookmark at the end of the pages you intend to read today; you do not keep moving it every time the author adds another chapter.

Write and validate the target before advancing the mark. If the target write fails, leave the mark unchanged. If the target write succeeds but the mark update fails, the next run may reread the same slice. That is why next week's idempotent write is necessary.

Prevent concurrent workers from advancing the same control record inconsistently. Use a single-writer policy or a conditional update that verifies the previously read mark. Separate backfill execution from ordinary forward progress so an old replay cannot move the live cursor backward.

For the exercise, demonstrate an initial load, a no-new-data run, a new committed batch, and a late business event arriving in that new batch. Then fail before the target write and show the mark remains unchanged.

The practical advice is to describe the progress record as a claim with a recovery rule. You need to know what it covers, how it advances, and what happens when the output and the cursor disagree after a crash.

## Screen example — not spoken

Controlled, monotonically committed batch sequence:

```python
rows = [{"batch": 1, "event_day": "2024-03-01"},
        {"batch": 2, "event_day": "2024-01-01"}]
stored_mark = 1
upper_bound = 2
slice_to_process = [r for r in rows if stored_mark < r["batch"] <= upper_bound]
assert slice_to_process == [{"batch": 2, "event_day": "2024-01-01"}]
# Persist mark=2 only after target commit and validation.
```

The old event date does not hide a newly committed input. The real exercise stores the mark in Delta, not a Python variable.
