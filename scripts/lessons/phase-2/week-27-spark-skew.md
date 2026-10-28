# Week 27: Find the task everybody is waiting for

Module M18 · [Course lesson](../../../site/phase-2.html#w27)

## Script

Most tasks finished in seconds. One is still running after several minutes. Adding more workers may leave even more workers waiting for that same task. You need to find out whether the work is unevenly distributed.

This week, baseline the candidate-pair or provider join from your project. Record the input versions, code version, result checks, and run configuration. Then inspect the slow stage in the Spark UI. Compare task durations, input records, shuffle bytes, spill, and the largest task against the median.

Spark partitions are units of work. Too few can limit useful parallelism. Too many can add scheduling overhead and small tasks. A hot key creates another problem: a large fraction of the data must come together for the same join or group. Increasing the partition count does not automatically split that one key.

Think of a supermarket with twenty checkout lanes and one enormous family order that must stay together. Opening another empty lane does not shorten that order. You need a strategy that changes how the work is assigned.

First ask whether the candidate-generation logic created a giant block. If a block was defined only by state, the right fix may be a better blocking strategy with measured recall. An enormous all-pairs block can remain infeasible even after execution tuning.

For joins, evaluate a genuinely small-side broadcast and the runtime's adaptive skew handling. If you use salting, make it deterministic for repeatable experiments. The large side gets a salt bucket; the matching small-side rows must be replicated across the relevant buckets. Salting both sides independently will lose valid matches.

For aggregations, a two-stage salted partial aggregation is appropriate only when the aggregate can be combined correctly. An average needs sum and count, not an average of arbitrary subgroup averages.

Change one justified thing, rerun under comparable conditions, and compare output content. A faster query that dropped candidate pairs did not solve the same problem. Preserve duplicate multiplicity in your equality check when duplicates are meaningful.

For your lab, show the original straggler, the diagnosis, the revised plan, and before-and-after evidence. If adaptive execution already handles the case, report that honestly instead of inventing a manual tuning win.

Your practical habit is to locate the bottleneck before choosing a knob. A screenshot of the slow stage plus a correct explanation is more valuable than a long list of copied Spark settings.

## Screen example — not spoken

```text
Experiment record
Input versions: fixed bronze/silver snapshots
Baseline: elapsed time, slow-stage task median/max, shuffle bytes, spill
Diagnosis: show the largest key/block and its share of input
One change: better block / measured broadcast / supported skew handling
Correctness: equal business rows and multiplicity, not just equal counts
Remeasure: same input, comparable cache/compute conditions
```

Use actual current-run Spark UI metrics. Do not promise a particular speedup before measuring.
