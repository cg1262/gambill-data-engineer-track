# Week 48: Get one source record through the foundation

Module M37 · Capstone sprint, week 1 · [Course capstone](../../../site/phase-4.html#w48)

## Script

You have three weeks to ship the capstone. If the first week ends with infrastructure and no interpretable record, the hardest assumptions are still untested. This week, get one narrow source slice through a working foundation.

Return to the Week 44 charter. Freeze the consumer question and declare the first output grain. Check that the chosen source still supports the required fields, access, and license. If a critical assumption failed, reduce or revise the scope now and record the decision.

Pin a small source version for development and save its provenance. Keep the extraction bounded so you can inspect it completely. Your full-volume run comes after the core semantics are credible; a huge download does not compensate for an unknown key.

Land the raw input with a stable source-version identity and replay location. Build the silver parser and validation boundary. Separate source parsing failures from row-level rule failures, and give the rejected records reasons and lineage. Produce a small preview at the intended analytical grain, even if the complete gold product is next week's work.

Think of this as testing a water pipe before closing the wall. You need to know that the connections fit and that a leak is visible. The decorative finish can wait until the flow is correct.

Choose the first write strategy from the table's meaning. Reprocessing the same snapshot should not create extra business rows. Define keys, completeness checks, and deterministic tie rules before adding an incremental cursor. A complete rebuild of a small fixture is a reasonable starting point when you understand its limits.

Inject three cases now: a malformed field, a repeated record, and a missing required identifier. Predict the outcome and compare it with actual accepted, rejected, and collapsed records. These fixtures become next week's regression tests.

Keep the repository runnable from documented commands. External storage, credentials, and workspace features need named prerequisites; do not rely on your current interactive session to supply them invisibly. Store no credential values in source or recordings.

For this checkpoint, show the fixed input, raw landing, validated output, rejection evidence, and a second run with unchanged business content. Update the architecture with what you actually built and list the remaining sprint tasks.

Practical advice: finish a narrow connected path before broadening the source. At the end of this week, you should be able to trace one real record and explain exactly what your code did to it.

## Screen example — not spoken

```text
Sprint checkpoint 1
Pinned source version + documented access/license
Raw replay location + logical input identity
Declared silver grain + implemented parser
Good row -> expected clean output
Malformed / missing-key row -> reasoned rejection
Repeated row -> documented duplicate policy
Second run -> same business content
README -> another person can repeat the small run
```

Weeks 48–50 share one course card. This video covers the first week's foundation only, not a newly invented curriculum unit.
