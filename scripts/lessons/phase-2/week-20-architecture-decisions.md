# Week 20: Design the failure path before the next load

Module M13 · [Course lesson](../../../site/phase-2.html#w20)

## Script

Your architecture diagram has six service logos and no answer to this question: what happens when the pricing file arrives twice? This week, turn the diagram into decisions an engineer can operate.

Start with the actual source behavior. A monthly bulk registry and irregularly republished pricing files do not automatically justify an always-running stream. Measure arrival cadence, size, and the freshness requirement. Incremental batch can be the right fit when new files need processing promptly but continuous compute buys little value.

Then decide where transformation happens. Landing a replayable raw copy before applying business rules lets you fix a parser without requesting the source again. That is useful for inconsistent CMS formats. Keep the raw bytes or an appropriate lossless representation, provenance, and immutable source-version identity. A folder called bronze is not sufficient evidence of replayability.

Write four parts in your architecture document. First, the flow: source to bronze, silver, gold, and golden records, with a grain and owner at every boundary. Second, the decisions: options, choice, consequences, and a trigger for revisiting the choice. Third, the failure plan. Fourth, the rerun and backfill plan.

A failure plan pairs detection with response. A rate limit gets bounded retry. A schema change gets captured evidence and a publication decision. A missing expected file gets a freshness incident. Duplicate source keys get a documented resolution or quarantine. “Log an error” is incomplete if nobody knows whether gold is safe to publish afterward.

Think of the document as the instructions taped inside an electrical panel. It needs to tell the next person which circuit they are changing and what else will lose power. A beautiful picture cannot replace that operational detail.

Choose the write strategy per table. A small reference table may be rebuilt completely. A current dimension may use a keyed merge. A complete monthly fact snapshot may use partition replacement. Each choice has a different blast radius when the input is incomplete or the key is wrong.

For your lab, ground the document in the tables you already built. Name at least three rejected alternatives and specific reasons. Do not claim streaming is too expensive or a database is too slow without evidence or a clearly stated assumption.

Finish by asking someone to predict the next ingestion run from your document alone. If they can explain the duplicate-file case, partial failure, and recovery, your architecture is becoming an operating agreement.

## Screen example — not spoken

```text
Table               Strategy            Failure to design around
bronze source log   append immutable      crash between landing and manifest commit
provider current   MERGE on profiled key  duplicate incoming keys
pricing month      replace full month    incomplete snapshot deletes valid rows
small code list    full replacement      empty upstream response

ADR: incremental batch instead of continuous processing
Context: observed arrivals + agreed freshness target
Decision: process new source versions on a defined schedule
Cost: freshness bounded by schedule; need durable manifest/replay
Revisit: measured arrivals or consumer latency requirement changes
```

Use measured project values when recording; the table is a decision prompt, not a universal prescription.
