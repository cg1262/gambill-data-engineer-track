# Week 35: Restart from progress you have actually saved

Module M23 · [Course lesson](../../../site/phase-3.html#w35)

## Script

The ingestion job restarts and reads every source file again. Someone suggests deleting the checkpoint whenever the output looks wrong. That can turn a repair into a full replay you did not plan for.

This week, use Auto Loader with a dedicated schema location and checkpoint for the chosen source-to-target query. Confirm support in your workspace and storage configuration before the demo. The source files need a defined naming and immutability policy; discovering a filename does not resolve every possible overwrite of its contents.

A streaming checkpoint records the query's progress and, for stateful operations, state needed to continue. It belongs to that logical query. Think of it as a detailed journey log, not a disposable cache. Sharing one checkpoint between unrelated streams makes their histories conflict.

Use an available-now trigger when the requirement is to process currently available input and stop. That can give a scheduled file-processing job streaming progress semantics without keeping compute active continuously. It is still subject to startup time, source discovery, and processing latency. Call it a freshness target you can measure rather than promising instant data.

Write with a supported transactional Delta sink and preserve the checkpoint across restarts. The source, checkpoint, query, and sink together determine replay behavior. A built-in Delta streaming sink can avoid duplicate committed batches under its supported guarantees; arbitrary external side effects do not inherit that guarantee.

Handle schema surprises deliberately. Configure the supported inference or explicit schema behavior and the rescued-data path. Rescued data needs monitoring and investigation. Merely storing an unexpected field in a special column does not mean downstream consumers understand it.

For the exercise, land three controlled file sets. Show the input metrics for the initial run, a no-new-file run, and a run with one added file. Interrupt processing in development, restart with the same checkpoint, and verify the target's business keys and content.

Then introduce a schema change and demonstrate the configured response. Document which query changes can reuse the checkpoint and which need a planned migration or replay.

Practical advice: when progress and output disagree, preserve evidence first. Record the checkpoint location, source versions, and target history before choosing a recovery action. Deleting progress should be an explicit replay decision with a deduplication plan.

## Screen example — not spoken

Databricks PySpark with Auto Loader support; create the source JSON fixture and writable UC volumes first:

```python
source_path = "/Volumes/ppi_dev/bronze/landing/cms_demo"
state_root = "/Volumes/ppi_dev/ops/state/cms_demo_v1"
incoming = (spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", state_root + "/schema")
    .load(source_path))
query = (incoming.writeStream.format("delta")
    .option("checkpointLocation", state_root + "/checkpoint")
    .trigger(availableNow=True)
    .toTable("ppi_dev.bronze.cms_demo"))
query.awaitTermination()
```

Choose separate state paths for every logical query. Set and demonstrate the desired schema-evolution/rescue policy before recording the schema-change portion.
