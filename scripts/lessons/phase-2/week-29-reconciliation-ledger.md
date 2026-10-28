# Week 29: Balance the pipeline to the record

Module M24 · [Course lesson](../../../site/phase-2.html#w29)

## Script

The source has a thousand records. Silver has nine hundred. Somebody says the missing hundred were probably duplicates. This week, replace probably with an accounting identity you can verify.

Define the reconciliation boundary first. At a row-preserving validation and dedupe boundary, input records should equal accepted records plus rejected records plus deliberately collapsed duplicates. Give each input a single final disposition so the categories do not overlap.

For example, a row that fails two rules is one rejection with two reasons. A duplicate removed by the declared policy belongs in the collapsed count. An inner join that removed an unmatched provider is another disposition you must account for; it cannot disappear into the word clean.

Think of balancing a cash drawer. You cannot explain a missing twenty dollars by saying the totals are approximately equal. Exact record accounting needs zero unexplained variance. A business measure may allow a documented rounding tolerance, but that is a separate control with a separate reason.

Do not apply the same row-count equation blindly across an aggregation. A thousand price observations can legitimately become ten facility summaries. At that boundary, reconcile the covered entity population and appropriate control totals at compatible grains. Posted prices are not additive spend; choose a control that preserves the meaning of the measure.

Create a persistent run ledger with source and target versions, logical run ID, layer, input and output counts, rejects, collapsed records, cursor bounds, duration, status, and error details. Define the ledger grain. One logical run per layer can use an idempotent upsert, while separate attempt records preserve retry history.

When variance is nonzero, persist the failed ledger record and stop publication. Your alert needs enough context to find the source version and target affected. A printed count in a notebook output is difficult to join with the incident tomorrow.

For the lab, remove one accepted row on purpose and show the balance fail. Restore the transform, rerun the same logical batch, and demonstrate a balanced ledger without duplicate success records. Then trace one gold result back to the evaluated silver population.

Practical advice: reconcile transformations where the meaning changes, not only at the end. A final discrepancy is much easier to diagnose when you can point to the first boundary where records stopped balancing.

## Screen example — not spoken

```python
def reconcile(rows_in, accepted, rejected, collapsed):
    variance = rows_in - accepted - rejected - collapsed
    if variance:
        raise ValueError(f"unexplained record variance: {variance}")
    return "PASS"

assert reconcile(1000, 940, 40, 20) == "PASS"
try:
    reconcile(1000, 939, 40, 20)
except ValueError as error:
    assert "variance: 1" in str(error)
else:
    raise AssertionError("The injected lost record was not detected")
```

The real pipeline writes failure evidence durably before raising. This identity applies to the declared validation/dedupe boundary.
