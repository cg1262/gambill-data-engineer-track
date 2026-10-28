# Week 50: Ship something another engineer can verify

Module M37 · Capstone sprint, week 3 · [Course capstone](../../../site/phase-4.html#w48)

## Script

Your project runs on your machine. The README says to contact you for setup help. This final week, remove yourself as a hidden dependency and prepare to defend the decisions behind the result.

Freeze the feature scope and make the release reproducible. Record the code revision, declared dependencies, target environment, identity requirements, and source versions. Run the documented setup from a clean environment or isolated target. If a paid workspace capability is required, say so and provide the precise prerequisite instead of implying the project runs everywhere.

Execute the meaningful tests and the small end-to-end path. Show that malformed input is accounted for, a duplicate does not inflate the product, a late correction follows policy, and a failed write has a safe recovery route. Keep pass, fail, skip, and unrun outcomes distinct.

Think of the final repository as a laboratory notebook another engineer can follow. The result matters, but so do the method, observations, and conditions under which the result holds. A badge without reproducible evidence is a weak substitute.

Apply the intended access model and prove it as the actual personas. Check that development and production targets resolve to the expected data boundaries. Run the deployment and smoke check through the declared release process. Keep real credentials and restricted data out of the recording.

Rehearse one recovery action from the runbook. Choose a disposable target and verify the related ledger, progress, and downstream state after recovery. Do not demonstrate rollback by restoring a table and ignoring the stream that will immediately write the unwanted input again.

Then prepare the defense. Why this grain? What happens to a duplicate, malformed record, or late correction? Which part would fail first at higher volume, and what measurement would justify changing it? Use actual fixture results and measured runs in the answers. Label estimates and future work honestly.

Record the portfolio walkthrough from Week 47 and connect the healthcare project with your own-domain capstone. Explain the method you repeated and the decisions that changed. Finish the README with the consumer question, measured result, run instructions, architecture, tests, and known limits.

For the final checkpoint, tag the verified release in your project and have another person run or inspect it. Your practical goal is a complete data product whose behavior, recovery, and trade-offs someone else can verify without depending on your memory.

## Screen example — not spoken

```text
Final defense evidence
1. Consumer question, output grain, actual KPI result
2. Source version -> accepted/rejected accounting -> gold -> golden lineage
3. Clean setup and current executed test results
4. Retry, backfill, and one verified recovery drill
5. Persona access tests and resolved deployment target
6. Two costly decisions, alternatives, and revisit triggers
7. Known limitations and the next measurement to make
```

Use a release tag only after the relevant checks pass. Do not describe a course simulation as production customer experience or invent business impact.
