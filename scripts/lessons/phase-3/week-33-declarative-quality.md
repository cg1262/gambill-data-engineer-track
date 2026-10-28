# Week 33: Declare the output and the rule that protects it

Module M22 · [Course lesson](../../../site/phase-3.html#w33)

## Script

Your notebook's cells run in the right order only because you remember which one to click next. This week, express the table dependencies and quality rules so the pipeline runtime can manage that order.

Use the workspace's supported Lakeflow declarative pipeline interface. The course also contains the older DLT naming. Confirm the available SQL or Python API in your selected runtime before recording, rather than mixing examples from different generations of the product.

Declare each dataset from the datasets it depends on. A streaming table and a materialized view have different update semantics. Choose the former for the supported streaming or incremental ingestion pattern, and the latter for the query result you need refreshed. A materialized view may be incrementally maintained when the query and platform support it; do not assume every query refresh is incremental.

Think of declaring spreadsheet formulas instead of telling someone the order to recalculate every cell. The dependency graph tells the system what depends on what. You still own the formulas and the meaning of the inputs.

Translate your existing validation rules rather than inventing a separate definition of quality. Decide what each expectation should do. A tracking expectation retains the row and records metrics. A drop expectation removes a failing row from that output. A fail expectation stops the update. Those choices have different consequences for publication and recovery.

An expectation that drops a row does not automatically create your repairable quarantine table. Preserve the original input and explicitly define the rejected branch with reasons and lineage. Otherwise you replaced visible rejects with a quality counter and lost the record needed for investigation.

Handle nulls explicitly in the boolean rule. A missing price should have the intended outcome under the runtime's expectation semantics. Test the actual behavior with a small injected fixture, including a row that fails more than one rule.

For the lab, run the initial update and a second update with controlled new input. Inspect the dependency graph, output rows, and current event-log metrics. Show one retained warning, one rejected record, and a critical condition that blocks publication in a separate controlled test.

Your practical advice is to keep the definitions readable. A small set of clearly named datasets and rules is easier to review than an abstraction that hides which records are kept, removed, or allowed to stop the product.

## Screen example — not spoken

Lakeflow SQL pipeline context; create the typed `ppi_dev.silver.price_parsed_input` fixture first:

```sql
CREATE OR REFRESH MATERIALIZED VIEW price_checked (
  CONSTRAINT price_present EXPECT (price IS NOT NULL)
)
AS SELECT * FROM ppi_dev.silver.price_parsed_input;

CREATE OR REFRESH MATERIALIZED VIEW price_rejected
AS SELECT *, 'missing_price' AS reason
FROM price_checked WHERE price IS NULL;

CREATE OR REFRESH MATERIALIZED VIEW price_accepted
AS SELECT * FROM price_checked WHERE price IS NOT NULL;
```

This example intentionally uses a retain-and-track expectation plus explicit accepted/rejected branches. Verify syntax and expectation metrics in the workspace used for recording; it is not a generic SQL warehouse script.
