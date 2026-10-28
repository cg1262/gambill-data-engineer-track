# Week 41: Test access with the identity you intend to restrict

Module M30 · [Course lesson](../../../site/phase-3.html#w41)

## Script

You apply a mask, query the table as its owner, and see the original value. Is the policy broken? Maybe the owner is explicitly allowed to see it. You need to test the actual restricted persona before drawing a conclusion.

This week, classify the data and verify access behavior. Start with a column inventory: meaning, source, sensitivity, business use, owner, retention, and intended readers. Public NPPES provider data is not automatically patient PHI. For the security demonstration, use synthetic restricted fields and label them clearly. Do not introduce real patient records to make a course demo realistic.

Apply least privilege through account groups and a dedicated workload identity. Give the job the privileges it needs to operate. Give analysts the published product they need to consume. Avoid broad ownership or catalog-wide rights as an easy way to silence a permission error.

Then decide the control. A column mask changes what a qualifying reader sees. A row filter limits which rows are visible. A restricted schema or separate product may be easier to reason about when access patterns are substantially different. Check feature support and interactions in the actual workspace.

Think of a hotel key. It should open your room and the shared spaces you need. Giving everyone a master key makes the front desk quieter, but it defeats the purpose of the lock.

Be careful with hashing identifiers. A deterministic hash can support consistent joins, but it is not automatically anonymization. Small identifier spaces can be guessed, and stable hashes can link records across datasets. Choose redaction, controlled tokenization, or another policy from the real requirement.

Test side by side as the intended analyst, engineer, and job identities. Include a denied operation, a masked value, and a row-restricted result where those controls are part of the design. Capture outputs without exposing real sensitive values.

Use audit records for supported access events and keep policy definitions and persona test evidence alongside them. Do not claim an audit row proves the exact masked value displayed unless the logging feature actually records that information. Access events and result contents are different evidence.

For the lab, run the job with its machine identity and demonstrate the restricted persona's experience. Your practical advice is to verify behavior from the reader's side, then document both the control and its limits so the next engineer can test it again.

## Screen example — not spoken

Databricks SQL, on a synthetic demonstration table; requires supported masks, a function schema, and suitable privileges:

```sql
CREATE OR REPLACE FUNCTION ppi_dev.governance.mask_demo(value STRING)
RETURN CASE WHEN is_account_group_member('ppi_engineers')
            THEN value ELSE 'REDACTED' END;

ALTER TABLE ppi_dev.gold.access_demo
ALTER COLUMN synthetic_identifier
SET MASK ppi_dev.governance.mask_demo;
```

Query as an actual engineer-group member and an actual nonmember with table read access. Test inherited rights and alternate access paths. This is a masking demonstration, not a claim of regulatory compliance.
