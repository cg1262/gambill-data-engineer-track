# Week 7: Keep the records that disagree

Module M03 · [Course lesson](../../../site/phase-1.html#w7)

## Script

You reconcile two population sources with an inner join. Every row in the result has a match. That sounds reassuring until you realize your query removed every country that existed on only one side.

This week, fetch a bounded World Bank API extract and compare it with a saved CSV at the same country-and-year grain. Check the source's country codes and exclude regional aggregates through an explicit rule. A country name is a display label; it is a fragile join key.

An HTTP call needs a timeout and status handling. Call `raise_for_status` before assuming the body is a successful response. A server can return a perfectly valid JSON error document. Parsing JSON alone does not tell you the request succeeded.

Read pagination metadata. For the World Bank response used in the lab, metadata and observations occupy different elements of the response. Request every reported page and record which pages you received. A successful first page is like receiving the first box of a shipment; you still need to compare it with the packing list.

Use bounded retries for transient failures. Respect `Retry-After` on a rate-limit response, handling its documented seconds or HTTP-date form. Otherwise use exponential backoff with jitter. Give up visibly after a configured limit. A bad parameter or unauthorized request should not sit in an endless retry loop.

Once both extracts are validated and unique at country and year, use an outer join. Separate matched keys, API-only keys, and CSV-only keys. Among matched keys, compare values using a stated tolerance. A relative percentage needs a defined denominator and an explicit rule for zero. Missing values are a separate condition.

Attach provenance to both sides: source, retrieval time, and the source's observation or publication period when available. Two valid sources may disagree because one revised a historical estimate. Do not overwrite that disagreement and call it cleaning.

For the exercise, choose two actual discrepancies and investigate plausible causes in the source documentation. Save the evidence and label unconfirmed explanations as hypotheses. Then rerun from the same saved responses and confirm the output is replaced rather than appended.

Your result should tell somebody what matched, what was missing, and what disagreed. That gives an analyst something to act on, including the cases your first inner join would have made disappear.

## Screen example — not spoken

```python
import pandas as pd

csv = pd.DataFrame({"country": ["AAA", "BBB"], "year": [2023, 2023],
                    "population_csv": [100, 200]})
api = pd.DataFrame({"country": ["AAA", "CCC"], "year": [2023, 2023],
                    "population_api": [105, 300]})
out = csv.merge(api, on=["country", "year"], how="outer",
                validate="one_to_one", indicator=True)
assert set(out["_merge"].astype(str)) == {"both", "left_only", "right_only"}
```

The fictional country codes isolate reconciliation mechanics. The course lab adds real API pagination, retry evidence, tolerance, provenance, and rejects.
