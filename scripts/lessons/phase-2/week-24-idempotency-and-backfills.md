# Week 24: Make the second run as safe as the first

Module M16 · [Course lesson](../../../site/phase-2.html#w24)

## Script

The write completed, but the job lost its connection before recording success. You cannot tell whether to retry. If retrying can duplicate prices, the pipeline's recovery procedure is a gamble.

This week, make the logical output idempotent: processing the same input again produces the same intended business state. Define what you compare. A new audit observation timestamp may be expected; a changed provider attribute or duplicated price is not.

Choose the strategy by table. A current provider dimension can merge on a validated business key. Deduplicate the incoming batch with a deterministic winning rule before merging. An arbitrary duplicate winner can change the result between runs even when the row count stays constant.

A complete pricing-month snapshot can replace its target month. Check that the incoming slice is complete before replacement, and restrict the replacement predicate to that slice. Partial data plus a broad overwrite can remove good rows. For a small reference table, a full rebuild may be simpler and safer than an incremental algorithm.

Think of saving a document versus adding another page to it. Replacing the intended version can be repeatable. Appending the same page after every retry keeps changing the document. Neither operation is universally right; the operation must match the table's meaning.

History needs another guardrail. Backfilling an old snapshot must not overwrite newer current attributes merely because it ran later. Use business effective ordering and a documented history-repair algorithm. A current-state merge and a Type 2 history writer are different implementations.

Build the ten-run harness over a fixed source version. Compare row counts, key sets, current-row invariants, and business column values. Counts alone miss a transform that changes a price on every run. Exclude attempt metadata only through an explicit comparison policy.

Then inject a failure between target commit and progress update. Rerun and show the same business result. Use a stable logical batch identity for data writes, and record individual attempts separately so operational evidence remains accurate.

For your lab, preserve the original append-duplication example, demonstrate the repaired rerun, and execute one historical backfill. Explain the blast radius of each table's write strategy.

The practical payoff is confidence under uncertainty. When a job dies at an awkward moment, you can retry from durable input and know which state the system should converge to.

## Screen example — not spoken

```python
target = {}
batch = [{"npi": "0000000001", "name": "Example Provider"}]

def upsert_current(rows):
    assert len({r["npi"] for r in rows}) == len(rows)
    for row in rows:
        target[row["npi"]] = dict(row)

upsert_current(batch)
expected = {key: dict(value) for key, value in target.items()}
for _ in range(10):
    upsert_current(batch)
    assert target == expected
```

This in-memory analogy demonstrates current-state convergence only. The lab must repeat writes against actual Delta tables and separately test historical ordering.
