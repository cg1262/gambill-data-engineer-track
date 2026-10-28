# Week 49: Publish the answer and prove the replay

Module M37 · Capstone sprint, week 2 · [Course capstone](../../../site/phase-4.html#w48)

## Script

Your capstone produces clean tables. The consumer still cannot answer the question in your charter. This week, connect the foundation to one usable result, then prove that new input and replay do not undermine it.

Build the gold product at the declared grain. Write the KPI definition once, including the eligible population, period, null policy, and denominator. Trace the query back to silver so the consumer can understand where each counted entity came from. A table with attractive column names is not enough if its measure changes meaning across rows.

Implement the proportionate identity-resolution step. If two sources refer to the same entity differently, preserve their identities in a crosswalk and record the evidence for resolution. Use exact rules when they are sufficient. For fuzzy matching, evaluate labeled pairs, route ambiguous cases to review, and keep field-level lineage for golden values.

Think of the crosswalk as a bilingual directory. It connects names used by different systems without pretending the original names never existed. That preserved relationship is what makes corrections and downstream investigation possible.

Now add change processing. Use a durable source-version manifest or a justified progress marker, choose a fixed input boundary, and update the cursor only after target success. The input-discovery rule and the write-idempotency rule must work together.

Test a genuinely new change and the same change twice. Then backfill an older slice. Verify that current attributes do not regress and that historical observations remain at the intended grain. If golden cluster membership changes, use your documented identity-update policy rather than silently assigning unrelated IDs to downstream consumers.

Compare content as well as counts. A price or entity assignment can change incorrectly while every row count remains constant. Reconcile the correct populations and control totals at each semantic boundary, especially when gold aggregates many source rows into one result.

For this checkpoint, show the consumer answer, its source lineage, a visible identity decision, the new-input run, and the replay or backfill evidence. Keep a small fixture that would fail if each guarantee broke.

Your practical advice is to resist adding another dashboard now. Spend that time making the first answer repeatable and explainable. One trustworthy result with a repair path demonstrates far more engineering judgment than several views nobody can reconcile.

## Screen example — not spoken

```text
Sprint checkpoint 2
Canonical KPI -> expected result on a hand-checked fixture
Crosswalk -> source IDs, master ID, status, decision evidence
Golden fields -> winning source row and rule
New source version -> expected changed result
Same version again -> unchanged business state
Historical replay -> no duplicate facts, no current-state regression
Reconciliation -> exact record dispositions and compatible metric controls
```

Use the domain from the student's own capstone. A static population with no identity ambiguity needs a documented exact policy, not an unnecessary fuzzy matcher.
