# Week 30: Turn your evidence into a repeatable test

Module M25 · [Course lesson](../../../site/phase-2.html#w30)

## Script

You have screenshots proving that the pipeline survived a duplicate last month. Then a refactor changes the key and the duplicate returns. A screenshot preserves history. An automated test can challenge the next change.

This week, turn the checks you have already practiced into a focused test suite. Start with tiny deterministic fixtures representing the actual source problems: a malformed price, missing provider identity, duplicate input, changed dimension attribute, and late-arriving observation.

Separate the test levels by what they exercise. A unit test checks transformation behavior with controlled input. An integration test checks a real boundary, such as a Delta write and reread. A smoke test checks a small representative workflow. An end-to-end test runs the chosen source-to-consumer path in an isolated target. The names are useful when they tell you cost, dependencies, and failure scope.

Use pytest fixtures to create independent test data and temporary targets. Make the Spark fixture compatible with your actual runtime; a local filesystem path is not automatically usable from remote or serverless Spark. Keep test tables and volumes in an explicit disposable development namespace.

Assert business behavior. A missing key produces a rejection with its reason and lineage. A changed Type 2 attribute closes the prior interval and creates one replacement. Running the same batch twice preserves business rows. A broken reconciliation stops publication. These tests are like alarm drills: they need to exercise the sensor and the response, not merely confirm that the alarm box exists.

Compare DataFrames without assuming row order unless ordering is part of the contract. Preserve multiplicity when duplicates matter. For small fixtures, inspect complete rows; a count-only assertion can miss an incorrect price or wrong provider assignment.

Keep the fast suite independent of today's live source. Run a separate integration or end-to-end check against pinned project inputs and record the versions. A real-data run captures useful current KPIs, but it should not make every unit test depend on a public API staying available.

For the lab, show executed test counts, one intentionally failing negative case, and the corrected passing run. Then assemble the portfolio with measured results, linked architecture decisions, and the golden-record lineage.

Your practical goal is to give the next change a fair examination. Keep the fixtures small enough to understand, and choose assertions that would fail if the behavior you care about actually broke.

## Screen example — not spoken

Self-contained illustration of behavior-focused pytest cases:

```python
import pytest

def classify_price(price):
    return "reject" if price is None or price < 0 else "accept"

@pytest.mark.parametrize("price, expected", [
    (None, "reject"), (-1, "reject"), (0, "accept"), (10, "accept")
])
def test_price_policy(price, expected):
    assert classify_price(price) == expected
```

Use the project's real imported transform in the lab. Zero is valid in this teaching policy; the actual price-type contract decides whether it is valid for a particular source field.
