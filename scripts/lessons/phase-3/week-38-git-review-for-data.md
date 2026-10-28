# Week 38: Review what a change does to the data

Module M27 · [Course lesson](../../../site/phase-3.html#w38)

## Script

The pull request changes one line: a merge key loses the source-period field. The code still runs, the style check passes, and historical observations start overwriting each other. A useful data review has to ask more than whether the Python looks tidy.

This week, put the pipeline's deployable source under Git and practice reviewing its data consequences. Export notebooks in a reviewable source format where appropriate. Keep the committed source and declared deployment configuration as the baseline, rather than depending on edits somebody made in an interactive workspace.

Use a short-lived branch for a focused change. The branch gives reviewers a bounded diff; it does not provide data isolation by itself. A feature branch writing to the production catalog is still a production writer. Separate target configuration and permissions must enforce the safe environment.

Before reviewing syntax, ask five questions. Did the row grain or key change? Can the write be rerun? Did a validation or quarantine path become weaker? Does the target resolve to the intended catalog? Did the change expose data or credentials to another principal?

Think of the diff as an amendment to a contract. A deleted field in an agreement may matter far more than several pages of formatting changes. Small code changes can have large data effects.

Use `git diff` to inspect the patch and compare the expected behavior against a tiny fixture. If the key changes, show a case where two previously distinct records now collide. If a rule changes, show the record it used to reject. This makes the review concrete instead of an exchange of preferences.

Create ownership rules for sensitive paths and configure the repository's protection features where available. A CODEOWNERS file identifies reviewers; the repository's rules determine whether their review is required. Test the actual merge gate rather than assuming the file enforces itself.

For the lab, plant the key, validation, and target risks in a development change and capture the review that catches them. Demonstrate workspace drift on a disposable object, then show the reviewed source restoring the intended definition.

Practical advice: write the pull request around the behavior and evidence. Say which product changes, how it can fail, and what proves the new behavior is correct. That gives a reviewer a much better starting point than a list of edited filenames.

## Screen example — not spoken

In the learner's repository:

```bash
git status --short
git diff main...HEAD
git log --oneline main..HEAD
```

Review exercise:

```text
Before key: facility + procedure + payer + period
After key:  facility + procedure + payer
Counterexample: same contract, January and February prices differ
Question: does the target represent current state or historical observations?
```

The right key depends on the declared table grain. Do not apply the example blindly to an SCD2 target.
