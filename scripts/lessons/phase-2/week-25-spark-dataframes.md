# Week 25: Build a plan, then choose when to execute it

Module M17 · [Course lesson](../../../site/phase-2.html#w25)

## Script

You changed five lines in a Spark notebook and nothing happened. Then you called `show`, and the cluster started working. That is the execution model you need to understand before optimizing the code.

Spark DataFrame transformations build a query plan. Selecting columns, filtering rows, and adding expressions usually describe work rather than immediately processing the full dataset. An action such as a write, collection, or count triggers execution of the plan needed for that result.

Think of writing a shopping list before going to the store. You can combine and simplify the list while it is still a plan. Once you make the trip, the work becomes real. Spark uses that planning opportunity to optimize the computation.

Re-express your silver transformation with DataFrame column expressions. Use `F.col` for a column, built-in functions for standard operations, and explicit aliases for the output contract. A Python `if` evaluates on the driver; `F.when` builds a per-row expression for Spark to execute.

Keep validation visible. A failed price conversion should route to the existing rejection policy. Depending on runtime settings, a cast may raise instead of returning null; choose and test the supported parsing behavior you intend. Do not change error behavior accidentally while translating SQL into Python.

Use `explain` to inspect the plan before execution. It shows the planned operations; it does not prove the data passes validation. Even a successful count may allow the optimizer to skip expressions irrelevant to counting rows. Exercise the actual columns and write path you care about.

Avoid collecting the full registry into Python. `collect` brings rows to the driver, which can exhaust one machine's memory even when the cluster has plenty of aggregate capacity. For inspection, choose a bounded sample. For production output, keep the transformation and write distributed.

Also watch notebook exploration. Repeated `show`, `count`, and writes can run related work multiple times. Persist only when reuse and measurement justify it, and release cached data when you are finished. Caching is a resource decision, not a default decoration.

For the lab, produce the same accepted and rejected business rows as the existing silver logic. Save the plan, identify an action, and show the resulting Delta write. Your practical goal is to understand which code describes work and which command asks the system to perform it.

## Screen example — not spoken

Run in a Spark session:

```python
from pyspark.sql import functions as F

raw = spark.createDataFrame([(" a ", "10.00"), ("b", None)],
                            "provider STRING, price_text STRING")
prepared = raw.select(
    F.upper(F.trim("provider")).alias("provider"),
    F.col("price_text").cast("decimal(12,2)").alias("price")
)
prepared.explain()
prepared.show()
```

The fixture deliberately contains only castable strings and null. Add invalid text in the real exercise and verify the runtime's chosen rejection behavior.
