# Week 28: Keep every reason a record failed

Module M24 · [Course lesson](../../../site/phase-2.html#w28)

## Script

A pricing row has no provider key and an invalid amount. Your validator reports only the missing key. The amount problem stays hidden until somebody fixes the key and runs the record again.

This week, classify records before splitting them. Define named rules with a business reason, severity, owner, and expected response. Include schema and type conformance, required fields, grain uniqueness, and accepted values. A ten-digit NPI-shaped string passes a format check; that alone does not prove a valid checksum or a real registry identity.

Build a reason collection for each record. Evaluate all applicable rules, then send records with reasons to quarantine and the others to the accepted output. This makes the reasons an audit trail rather than whichever exception happened to fire first.

Watch null behavior in Spark and SQL. A condition involving null may itself be null. Filtering on a condition and filtering on its negation can lose the null cases from both outputs. Convert unknown validity into an explicit failed or separately classified state according to the rule.

Think of an inspection checklist. The inspector marks every failed item before deciding whether the shipment can proceed. A record with three issues is still one rejected record, even though it contributes to three rule-failure counts. Do not add those rule counts together and call them rejected rows.

Store the original payload, source identity, record key, reasons, and observation time. Use a stable logical input identity for reruns so retrying validation does not create duplicate quarantine records. Keep attempt-level observations separately if you need to analyze repeated failures.

Then decide the publication policy. A few isolated bad records may allow clean records to continue. A critical missing-key spike or an exceeded quality budget may block publication. Persist the rejection and quality evidence before raising the run-level failure, and test that the evidence survives the failed run.

For the lab, inject a deck of bad records and predict every reason. Verify at least eight meaningful rules, accepted-versus-rejected accounting, a threshold breach, and ten fixed-input reruns.

The practical advice is to make quarantine repairable. Somebody should be able to locate the source record, understand all of its failures, correct the rule or input through a reviewed process, and replay it without creating duplicate business rows.

## Screen example — not spoken

```python
def reasons(row):
    result = []
    if not row.get("provider_id"):
        result.append("missing_provider")
    price = row.get("price")
    if price is None or price < 0:
        result.append("invalid_price")
    return result

bad = {"provider_id": None, "price": -1}
assert reasons(bad) == ["missing_provider", "invalid_price"]
```

This fixture assumes numeric-or-null prices after parsing. In Spark, implement the reason collection with built-in expressions and explicitly handle null validity conditions.
