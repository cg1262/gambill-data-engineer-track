# Week 32: Prove the intended reader can access the intended table

Module M21 · [Course lesson](../../../site/phase-3.html#w32)

## Script

The analyst cannot read the gold table, so somebody grants access to the whole catalog. The report starts working, and the analyst can now see far more than the report requires. This week, solve the access problem at the correct scope.

Move through Unity Catalog's namespace deliberately: catalog, schema, table. Use fully qualified names in the project so the active notebook context does not quietly decide whether a write lands in development or production. Separate environments in the namespace and in the permissions, then test that separation.

Define account-level groups around responsibilities. The analyst reads the published gold product. The engineer develops and troubleshoots in an appropriate environment. The pipeline identity writes the tables it owns. Object ownership is powerful; do not use ownership as a convenient substitute for a narrow privilege.

For a basic table read, the principal needs the relevant catalog and schema usage privileges as well as select on the object, whether directly or through supported inheritance. Think of getting into an office building, entering the right suite, and opening the filing cabinet. Permission at one door does not automatically settle the others.

Test as the actual persona. A query succeeding as the workspace administrator tells you little about the analyst's rights. Show a successful intended read and a denied read outside the persona's scope. Record which identity performed each check.

Choose managed versus external tables from lifecycle responsibility. Managed tables let the platform manage data storage and table lifecycle within its supported model. External tables point to separately managed storage. Dropping table metadata is not a universal cleanup strategy for external bytes, and managed-table deletion behavior includes platform-specific lifecycle and recovery details. Check those before destructive operations.

Add classifications and owners to the relevant columns. Public provider records are not automatically patient health information. Classification should reflect actual contents and policy, especially if the project later adds restricted sources.

For the lab, document the namespace, per-table storage decision, persona grants, denied-access evidence, and supported lineage coverage. Build the lineage from real pipeline operations; a diagram alone does not prove the system captured it.

Practical advice: every broad grant should have a reason you can state and an owner who can revisit it. A working query is one check. A correctly bounded query is the result you are trying to achieve.

## Screen example — not spoken

Databricks SQL, run by an authorized grantor after creating the demo objects and account group:

```sql
GRANT USE CATALOG ON CATALOG ppi_dev TO `ppi_analysts`;
GRANT USE SCHEMA ON SCHEMA ppi_dev.gold TO `ppi_analysts`;
GRANT SELECT ON TABLE ppi_dev.gold.pricing_completeness TO `ppi_analysts`;
```

Query the gold table as an analyst, then attempt a deliberately ungranted silver read as that same analyst. Existing inherited grants can affect the expected denial; inspect them rather than assuming isolation.
