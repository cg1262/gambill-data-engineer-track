# Week 2: Say what one row means

Module M01 · [Course lesson](../../../site/phase-1.html#w2)

## Script

You have a table with a million rows. Someone asks how many service requests the city received. Can you answer by counting rows? Only if you know what one row represents.

This week, use the NYC 311 source to practice that decision before writing a pipeline. Open the publisher's documentation and inspect a small sample. Find the request identifier, creation time, complaint type, and location fields. Keep the source URL and the date you inspected it. A live source can change after you record your observations.

Write a grain sentence: one row represents one service request identified by its request key. Treat that as a claim to investigate. Compare row count with distinct request-key count in your sample. A repeated key might be a duplicate export, an update, or evidence that your grain sentence is incomplete. Fifty rows help you ask better questions; they do not prove the entire source is unique.

Next, draw the lifecycle. A request starts in an operational system. The public portal publishes a copy. Your ingestion lands a snapshot. Your transformations produce a table for a consumer. Label where each copy lives and who owns the handoff. This is like following a package through a delivery network: every transfer needs an address and somebody responsible for receiving it.

Now write the contract. Include field types, which values may be missing, the grain, the owner, and a freshness expectation. Separate a measured source refresh cadence from the service level you propose for your own product. You cannot promise an hourly report from a source you have only observed updating daily.

Give two consumers different questions. An operations manager might need an open-request backlog. A planning analyst might need monthly complaint trends. The backlog requires a reliable definition of open. The trend needs a stable date definition. Those are business semantics your schema alone cannot explain.

Your practical advice this week is to make every promise checkable. Replace “data is fresh” with a defined timestamp, threshold, and response when it is breached. Replace “unique ID” with the actual key and a duplicate-handling policy.

For your lab, commit the lifecycle diagram, contract, and grain statement. Have somebody read them without your explanation. If they can name the consumer, the question, and what would make the answer wrong, your design is becoming useful.

## Screen example — not spoken

```text
Product: 311 monthly complaint trends
Grain: one request per request key in the chosen source snapshot
Business time: request creation timestamp, with timezone documented
Observed source cadence: measure and record it
Proposed product freshness: define after checking source feasibility
Duplicate-key policy: investigate updates; never silently count both
Owner: name the person responsible for this learning project
```

Contrast a sample observation with a production-wide guarantee.
