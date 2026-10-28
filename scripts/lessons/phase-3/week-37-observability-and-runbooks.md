# Week 37: Make the alert point to a recovery action

Module M26 · [Course lesson](../../../site/phase-3.html#w37)

## Script

The job is green. The newest published pricing period is still last month's. A successful process and a fresh data product are different signals, and this week you monitor both.

Define a service-level indicator before setting a target. For freshness, specify which timestamp or expected source period you compare with which clock. Maximum event time can hide a missing file if another source is still active. Monitor the expected source inventory as well as the newest observed record.

Your objective is the target you operate toward. An agreement adds a commitment and consequences between parties. Do not call a number an SLA just because you put it on a dashboard. In the course project, label proposed commitments and measured performance separately.

Record an idempotent logical-run ledger and distinguish individual attempts. Include source and target versions, input coverage, accepted and rejected counts, duration, status, and progress bounds. Use the job and pipeline metadata actually available in your workspace; do not assume every system table contains every field you want.

Think of the dashboard as an instrument panel. Engine running is one light. Fuel, temperature, and destination progress are others. Watching only the running light does not tell you whether the vehicle can finish the trip.

Turn thresholds into owned alerts. A quality breach should include the failed rule, source version, impacted output, severity, and the runbook entry. A freshness alert should identify the missing period and who can investigate the upstream source. Avoid paging somebody for a symptom they cannot act on.

Use lineage to find consumers that may be affected, while documenting gaps in automatic coverage. SQL outside supported capture paths, external exports, and manual extracts may need additional inventory. A graph is evidence for the paths it actually observes.

For the lab, deliberately miss a source arrival or exceed a quarantine threshold. Capture the current alert firing and follow the runbook on a disposable target. Rehearse a retained-version restore and explain which downstream outputs or checkpoints also need reconciliation afterward.

Your practical advice is to test the alert and the response together. An alert that nobody receives is broken. An alert that arrives with no owner or safe recovery instruction is unfinished. A useful monitoring layer shortens the path from a specific observed problem to a verified repair.

## Screen example — not spoken

```text
Alert: expected CMS source period missing
Observed: source_id, expected_period, last_accepted_version, checked_at
Impact: affected gold product and consumers from verified lineage
Owner: named project operator
Action: inspect source manifest -> verify upstream availability -> replay
Publication rule: retain clearly marked prior result or block, per contract
Recovery check: input coverage + quality + reconciliation + freshness
```

Trigger the configured alert in development and capture its actual delivery. Monitoring, notification, lineage, and system-table availability vary by workspace and permissions.
