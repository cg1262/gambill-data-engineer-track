# Week 44: Choose a problem small enough to finish

Module M32 · [Course lesson](../../../site/phase-4.html#w44)

## Script

Your capstone idea includes five sources, real-time ingestion, an AI agent, and three dashboards. You have three build weeks. Before adding another service, identify the smallest useful data product you can complete and defend.

Start with a person and a decision. A transit planner needs to compare route reliability by service day. A retailer needs a trustworthy inventory position at a defined snapshot. Choose something connected to the industry you want to work in, then write the consequence of a wrong answer.

Inspect a real public source before committing to the design. Check its license, access method, sample volume, refresh behavior, key quality, missingness, and historical availability. Save a bounded sample and provenance. A source that only exposes today's state cannot automatically support years of historical analysis.

Declare the grain and a testable KPI. For route reliability, specify whether you measure trips, stops, or route-days, and define the eligible population. A small clear measure gives the project a finish line. Think of building a useful room before promising an entire house.

Write the charter and a four-part architecture document: context, data flow, governance, and deployment. Keep the grain visible at each layer. Show where duplicates, late records, and malformed input go. Include a bounded operational cost and freshness expectation you can actually evaluate.

Then write three decision records. For each, name the alternatives, chosen approach, consequences, and revisit trigger. Batch versus streaming should follow source cadence and latency needs. Star schema versus a more elaborate model should follow the consumer and source complexity. Exact versus fuzzy matching should follow the identity problem and the cost of a wrong match.

Avoid adding MDM as decoration. Find the real identity conflict in your sources and choose a proportionate resolution strategy. If an exact crosswalk is sufficient, document why. If there is no credible second source, use the course's extension option with a genuinely new source and business question in Project 1.

For this week's lab, ship the design artifacts and feasibility evidence. Do not spend the week building a pipeline around an untested source assumption. List the capabilities you will implement during the three-week sprint and what you deliberately leave out.

Your practical advice is to define done while the project is still small. A complete, recoverable answer to one meaningful question gives you much stronger interview evidence than an impressive architecture with no reliable output.

## Screen example — not spoken

```text
Persona: transit service planner
Decision: prioritize routes for reliability investigation
Candidate grain: one scheduled trip on one service day
Feasibility check: can source data link schedule to actual operation?
KPI: defined late/cancelled trips / eligible scheduled trips
Identity problem: source route IDs and renamed routes across versions
Failure cases: missing trip, duplicate event, late correction
Out of scope: live passenger routing, prediction, multi-city platform
```

This is a design example, not a claim that a particular public feed contains all required fields.
