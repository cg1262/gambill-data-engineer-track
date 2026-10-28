# Week 47: Tell the decision through evidence

Modules M36 / M34 · [Course lesson](../../../site/phase-4.html#w47)

## Script

You spend five minutes describing your pipeline's tools. The listener still cannot tell who needed the result or which decision you made. This week, make your explanation follow the problem and the evidence.

Choose one real incident from your work or one clearly labeled failure drill from the course. Write what you observed before writing what you believe caused it. “The row count doubled after the retry” is an observation. “The merge was broken” is a diagnosis that still needs support.

Tell the sequence in order: the situation, the evidence, the investigations, the change, and what verified the repair. Include the first plausible explanation you ruled out if it helps the listener understand your judgment. Do not invent a dramatic outage or business impact that you did not measure.

For a trade-off story, name the choice, alternative, reason, cost, and revisit trigger. “I chose scheduled incremental processing because the source updates in batches and the freshness target allowed it. I accepted schedule-bound latency. I would revisit if measured consumer needs changed.” Replace those assumptions with your actual project evidence.

Think of the walkthrough as a guided inspection. You are choosing a few doors to open so someone can verify the building, rather than reading them the list of construction materials.

For the portfolio recording, begin with the consumer and question. State the grain. Show the architecture briefly, then follow one actual record from landed source through validation into the consumer result or golden identity. Pause at one meaningful failure or retry decision and show the proof.

Use the second project to demonstrate that you repeated the method in another context. Explain what changed between the two problems instead of giving a second full tool tour. Close with ownership: how the product is monitored, repaired, and improved.

Practice a fixed-duration camera answer as well as a conversational mock. Automated interview formats vary by provider and employer, so use the instructions for the actual assessment rather than assuming a universal timer or scoring rubric.

For the lab, record the five-to-eight-minute walkthrough, review your audio and screen legibility, and score clarity, evidence, trade-off honesty, and time. Remove any claim you cannot substantiate.

Practical advice: a thoughtful limitation can strengthen an answer. Explain what the project proves, what remains untested, and what evidence would change your next decision. That sounds like an engineer who understands the work they are presenting.

## Screen example — not spoken

```text
Story card
Person and consequence:
Observed evidence:
Hypotheses checked, in order:
Decision and rejected alternative:
Cost accepted:
Verification:
Revisit trigger:

Walkthrough route
Question -> grain -> architecture -> one record -> one failure/recovery proof
-> second-project comparison -> ownership and limits
```

Use actual evidence or explicitly label a course simulation. The lesson video is short; the student's recorded portfolio deliverable remains five to eight minutes.
