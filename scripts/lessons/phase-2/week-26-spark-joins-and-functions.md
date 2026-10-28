# Week 26: Move the small lookup, keep the big work distributed

Module M17 · [Course lesson](../../../site/phase-2.html#w26)

## Script

You collect every provider ID into a Python set so you can filter the pricing table. It works on your sample. On the full registry, the driver runs out of memory before the actual transformation begins.

This week, express relationships as distributed joins. If you only need pricing rows that have a provider match, use a left-semi join. If you need the unmatched rows for investigation, use left-anti. You avoid carrying unnecessary provider columns and avoid moving the full key set into the driver.

Before a normal join, check uniqueness on the side that is supposed to be a lookup. A distributed engine can multiply rows just as efficiently as it can join them correctly. State the output grain and verify expected cardinality. Broadcasting a duplicate lookup makes a wrong result faster.

For a genuinely small reference, a broadcast join can send that reference to the workers instead of shuffling both large inputs by key. Think of distributing a short phone directory to every desk rather than sending every caller to one central desk. The directory still needs to fit where you send it.

Do not infer size from row count alone. A thousand very wide rows can be expensive, and the runtime's plan may change after optimization. Inspect the executed plan and metrics rather than assuming a broadcast hint was beneficial.

Use grouped aggregations to compute measures at the declared gold grain. Exact distinct counts and approximate distinct counts answer different precision requirements. If the business needs an audited provider count, an approximation requires an explicit error policy and justification.

Now look at custom functions. Built-in Spark expressions are the first choice for trimming, case normalization, and edit distance. A plain Python UDF adds serialization and execution overhead and can hide logic from optimization. Use one when the required behavior cannot be expressed reasonably with supported built-ins, then measure it on representative data.

For the lab, join pricing to the resolved provider mapping rather than guessing identity from similar names. Show matched and unmatched populations, compute the intended rollup, and compare one built-in expression with a custom alternative while checking identical semantics.

Practical advice: keep the relationship inside the query engine for as long as possible. You get a plan you can inspect, distributed execution, and a clearer place to enforce grain before a convenient sample turns into a large production job.

## Screen example — not spoken

Run in Spark:

```python
from pyspark.sql import functions as F

pricing = spark.createDataFrame([("p1", 100), ("p2", 200)],
                                "provider_id STRING, price INT")
providers = spark.createDataFrame([("p1", "Example")],
                                  "provider_id STRING, name STRING")
matched = pricing.join(providers, "provider_id", "left_semi")
unmatched = pricing.join(providers, "provider_id", "left_anti")
assert matched.count() == 1
assert unmatched.count() == 1
pricing.join(F.broadcast(providers), "provider_id", "left").explain()
```

The tiny fixture makes broadcast plausible. Measure the real lookup and inspect its plan before using the same choice at scale.
