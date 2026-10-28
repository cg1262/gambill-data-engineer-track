# Week 34: Repair the failed work without corrupting the good work

Module M22 · [Course lesson](../../../site/phase-3.html#w34)

## Script

Bronze succeeded, silver failed, and the gold task still published yesterday's data with today's success timestamp. This week, make the job's dependency graph reflect what success actually means.

Split the workflow into meaningful tasks: ingest or update the declarative pipeline, validate and resolve identities, refresh the consumer outputs, and record the final outcome. A task boundary should represent a useful retry or dependency boundary. You do not need a separate task for every function.

Declare dependencies so gold requires the successful validated inputs it consumes. Set failure handling on a separate path rather than letting a cleanup task make the whole run look healthy. Think of an assembly line: passing the packaging station does not prove the inspection station signed off.

Give the logical batch a stable identity and pass it through job parameters or supported task values. Pass small metadata, such as batch ID or row count, through task values. Keep datasets in governed storage rather than attempting to move a large result through orchestration metadata.

Configure bounded retries, timeouts, and concurrency deliberately. Retry a transient retrieval problem. Do not repeatedly retry a deterministic contract violation without changing anything. Limit overlapping writers when the control table or target design assumes one active run.

Set the schedule with an explicit timezone and check daylight-saving implications if the business deadline uses local time. A successful scheduled run is insufficient if the source file did not arrive. Include the arrival and freshness checks you already designed.

Now break a downstream task in development. Inspect the run timeline and prove which tasks succeeded and which did not. Use Repair Run where supported to rerun the failed and required downstream work. A repair reuses earlier outputs, so verify that their input versions remain appropriate and that each retried write is idempotent.

For the lab, capture a real failure notification, the repair, and the unchanged business results after repeated fixed-input runs. Use a controlled notification destination you own; record who should respond and what information they receive.

Your practical advice is to rehearse repair before you need it. The important question is whether a teammate can identify the failed boundary, choose the safe recovery action, and verify the consumer did not receive a partly updated product.

## Screen example — not spoken

```text
ingest_and_validate -> resolve_providers -> publish_gold -> success_ledger
        |                    |                  |
        +--------------------+------------------+-> failure_handler

Parameters: logical_batch_id, source_version, target_catalog
Concurrency: match the pipeline's single-writer assumptions
Retries: bounded, for named transient failures
Repair drill: fail resolve_providers; confirm publish_gold is blocked
```

Implement the failure-handler dependency condition in the workspace's Jobs configuration. Demonstrate the actual run status and notification, not only the intended diagram.
