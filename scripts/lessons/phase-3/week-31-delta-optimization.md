# Week 31: Optimize a measured query and preserve recovery

Module M20 · [Course lesson](../../../site/phase-3.html#w31)

## Script

Your table has the same number of rows as last week, but the dashboard is slower. You find thousands of tiny files. Before changing the cluster size, inspect the table's physical layout and the query reading it.

Delta stores data files and a transaction log describing table versions. A logical delete or file replacement changes which files belong to the current snapshot. The older files may still support historical reads until retention cleanup removes them. A table version is more than whichever Parquet files happen to be visible in a directory listing.

Start with `DESCRIBE DETAIL`, `DESCRIBE HISTORY`, and the query profile. Record table size, file count, recent operations, filters, and elapsed time for a representative query. A high file count is a clue, not proof of the bottleneck. Check whether time is going into file discovery, scanning, shuffling, or something else.

Compaction combines small files into larger ones. Clustering organizes data so relevant queries can skip more unrelated data. Think of packing loose papers into folders, then arranging the folders by the topics people actually search for. Those are related but different improvements.

Choose layout from the workload. If the pricing consumer filters by facility and payer, investigate those access patterns. Do not partition a small table by every provider identifier simply because that identifier is important in the model. Excessive partition cardinality can produce tiny fragments.

Check which clustering and automatic maintenance features your runtime and table type support. Do not stack liquid clustering, legacy partitioning, and Z-order commands as though every combination is valid. Choose a supported design and record the migration or compatibility implications.

Measure the same query after one change, compare business results, and explain the observed improvement or lack of one. Include warm-cache effects and compute differences in your notes.

Then rehearse recovery on a disposable table. Query a previous version and distinguish that read from restoring the table's current state. Set retention from recovery, reader, and stream requirements. Do not shorten cleanup retention to make the demonstration dramatic.

For the lab, save the baseline, one justified tuning experiment, and a successful recovery drill. Your practical responsibility is to improve the query without removing the historical files your recovery plan still depends on.

## Screen example — not spoken

Databricks SQL on a disposable project table; replace the example name:

```sql
DESCRIBE DETAIL ppi_dev.silver.pricing_demo;
DESCRIBE HISTORY ppi_dev.silver.pricing_demo;
OPTIMIZE ppi_dev.silver.pricing_demo;
```

Inspect history, select an actually retained prior version, and run a read-only `SELECT ... VERSION AS OF <version>`. Demonstrate `RESTORE` separately on the disposable table. Measure before and after; do not claim a speedup from the command's success alone.
