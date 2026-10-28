# Week 36: Bound deduplication without losing the evidence

Module M23 · [Course lesson](../../../site/phase-3.html#w36)

## Script

An event arrives twice, then another arrives three hours late. You add a watermark and assume both problems are solved. You still need to decide what counts as a duplicate, how much state to keep, and what happens to records outside that state window.

Start by landing an immutable raw event log. Include a stable event identity, provider identity, event time, arrival evidence, and payload. Provider ID alone is not an event key: two legitimate changes to the same provider must remain distinguishable.

Measure lateness on representative input. Event time describes when the source says the change happened. Processing time describes when your system handles it. Choose the allowed delay from observed behavior and the business cost of waiting, then document the cases that delay will not cover.

A streaming watermark follows observed event-time progress and helps the engine bound state for supported operations. It is not a wall-clock timer for every row. Events within the supported delay receive the operator's documented protection; older events may be discarded, and exact boundary behavior depends on the operator and execution progress.

Think of keeping a guest list for a rolling event. You can check recent arrivals against the list, but once you archive old pages, you need another process for someone who turns up with last month's invitation.

Use the runtime's supported bounded deduplication operator at the true event grain. Then make the target write safe on retry. For a current-provider table, dedupe each microbatch to one winning update per provider and merge only when its ordering is newer than the target. Equal timestamps need a documented tiebreaker. A retried microbatch should not reverse a later update.

If you use `foreachBatch`, assume your function can run again for the same batch. Arbitrary side effects need their own idempotency. A stable checkpoint and batch ID do not make every external write exactly once.

Crucially, a stateful operator's discarded late rows do not automatically appear in quarantine. Preserve the raw log and build a separate, explicit reconciliation or late-record adjudication path. Show which raw events reached the target and which need replay or review.

For the lab, demonstrate a duplicate, a within-policy late event, an older event, and restart recovery. Inspect state metrics as well as target content. Your practical goal is bounded online work with a durable explanation for every event that still needs attention.

## Screen example — not spoken

PySpark; requires a runtime supporting `dropDuplicatesWithinWatermark` and a landed raw table with timestamp-typed `event_ts`:

```python
raw = spark.readStream.table("ppi_dev.bronze.provider_events")
deduped = (raw.withWatermark("event_ts", "2 hours")
              .dropDuplicatesWithinWatermark(["provider_id", "event_id"]))
```

Two hours is an illustrative policy, not a recommendation. Add the idempotent sink and independent raw-to-disposition reconciliation in the lab. Do not show this snippet as if it automatically captures late rejects.
