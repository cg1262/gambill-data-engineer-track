# Week 42: Trace the identity from the job to the storage

Module M31 · [Course lesson](../../../site/phase-3.html#w42)

## Script

Your pipeline can read cloud storage because somebody pasted a key into a notebook. Then the key rotates, the notebook fails, and nobody remembers which account owns it. This week, connect the storage through an identity and access model you can explain.

Choose one cloud for the lab. On Azure, trace the supported managed identity or access connector and its storage role assignments to the ADLS location. On AWS, trace the supported IAM role, trust relationship, and storage permissions to the S3 location. The details differ, but in both cases you need to know who is asking and what that identity may access.

Use Unity Catalog storage credentials and external locations through the workspace's supported setup. A storage credential represents the platform's authorized route to the storage. An external location binds that route to a defined path. Grant the intended principals access at the necessary scopes and test with the workload identity.

Think of a loading dock permit. Knowing the dock's address does not give a driver permission to enter. The driver's identity, the permit, and the gate's rules all have to agree. Likewise, a correct bucket URI does not settle identity, storage policy, or network connectivity.

Separate those checks while troubleshooting. Can the identity authenticate? Does it have object permissions? Is the network route supported? An authorization error and a network timeout call for different investigations. Keyless access does not automatically make traffic private; private networking requires its own supported configuration and evidence.

Now measure cost. Record the actual workload interval, compute type, usage quantity, unit, and attribution tags or metadata. Databricks usage and list-price tables can support a list-price estimate where available. Align SKU, unit, currency, and price-effective interval. A list-price estimate is not necessarily the contracted bill.

Include other relevant costs, such as storage, cloud compute where billed separately, and network transfer. Do not call a DBU-only calculation the total platform cost.

For the lab, show a governed read and write using the intended identity, one denied out-of-scope path, and a measured cost baseline. If your workspace lacks external-location or billing capabilities, use an appropriate authorized cloud workspace and mark those checks pending until executed.

Practical advice: choose one working cloud path and trace it end to end. A narrow, verified design teaches more than a diagram showing every cloud service at once.

## Screen example — not spoken

Workspace-wide usage inspection, where system-table access is available:

```sql
SELECT sku_name, usage_unit, SUM(usage_quantity) AS quantity
FROM system.billing.usage
WHERE usage_start_time >= current_timestamp() - INTERVAL 1 DAY
GROUP BY sku_name, usage_unit
ORDER BY sku_name, usage_unit;
```

This is a usage inventory, not a per-run cost report. For the lab, filter attributable job/run usage and join the correct effective price records; explain unallocated usage, delayed records, and costs outside this table.
