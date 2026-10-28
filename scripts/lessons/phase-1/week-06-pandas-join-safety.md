# Week 6: Catch a merge that multiplies your answer

Module M03 · [Course lesson](../../../site/phase-1.html#w6)

## Script

Your borough report has five rows before a merge and six afterward. The command succeeded. The numbers are wrong. This week, learn to treat a join's row count as something you must explain.

Use pandas on a bounded local sample of NYC 311 data. It is useful for inspecting a small dataset and prototyping a transformation. Keep the full production ingestion problem separate; loading an arbitrarily large source into one machine's memory is a different design decision.

Start by inspecting dtypes and missing values. A column of dates stored as strings will not automatically behave like a timestamp. Convert deliberately, retain evidence of failures, and decide which fields are required. Selecting columns with `.loc` and copying the subset you intend to change makes your transformations easier to follow.

Now group the clean requests by borough and month. Say the new grain aloud: one row per borough per month. You have changed what a row means. The population reference must match the dimensions of the rate you are calculating, including the population year or other reference period.

Before merging, prove that the reference has one row for the key you chose. If a borough appears twice in the population table, every matching request aggregate appears twice too. It is like attaching two price labels to the same item and asking a cashier to total both. The arithmetic works; the relationship is wrong.

Use `validate="many_to_one"` when many monthly aggregates should map to one population reference. Add `indicator=True` to expose missing matches. Check that every required borough found its denominator before calculating requests per ten thousand residents. A missing denominator should become a visible failure or a documented exception, never a convincing-looking rate.

For the lab, deliberately duplicate one reference key and watch validation fail. Remove the injected error, rerun, and compare the aggregate row count before and after the merge. Keep rejected source rows with reasons, and overwrite the output when reprocessing the same sample.

The practical habit is simple: write the grain and the expected relationship beside the merge. Your future self will remember why the validation exists. Your reviewer can then challenge the assumption instead of reverse-engineering it from a dashboard that happens to look plausible.

## Screen example — not spoken

```python
import pandas as pd

counts = pd.DataFrame({"borough": ["Queens", "Queens"],
                       "month": ["2024-01", "2024-02"], "requests": [10, 20]})
population = pd.DataFrame({"borough": ["Queens"], "population": [100_000]})
out = counts.merge(population, on="borough", how="left",
                   validate="many_to_one", indicator=True)
assert len(out) == len(counts)
assert out["_merge"].eq("both").all()
out["per_10k"] = out["requests"] / out["population"] * 10_000
assert out["per_10k"].tolist() == [1.0, 2.0]
```

Add a second Queens reference row to demonstrate the cardinality error. These are synthetic teaching values.
