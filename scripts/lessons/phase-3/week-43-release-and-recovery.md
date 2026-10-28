# Week 43: Let someone else operate the release

Modules M20–M31 · [Course lesson](../../../site/phase-3.html#w43)

## Script

You can run the pipeline because you know which notebook needs a manual fix first. That knowledge is a release blocker. This week, hand the operating instructions to someone else and find out what the project actually requires.

Freeze the feature scope. Use the reviewed source revision, declared deployment target, workload identity, and known source versions. Record them in the release evidence so you can distinguish a code change from a changing input.

Start with a cold deployment into an isolated release-test target. Verify that the documented setup creates or finds the required objects, applies the intended access, and runs the source-to-consumer path. Keep the test target separate from an existing production namespace so the drill does not erase somebody's working state.

Then inject a known failure. A contract violation should preserve diagnostic evidence and prevent the unsafe publication path. A failed task should be repairable using the documented procedure. A repeated logical batch should converge to the same business output.

Think of a fire drill in a building you already occupy. You are testing whether the exits, signs, and responsibilities work together. You do not prove preparedness by showing a floor plan and saying you would probably leave through that door.

Rehearse recovery with a disposable copy and an actually retained table version. A Delta restore changes the table's current state; it does not automatically rewind the input manifest, streaming checkpoint, audit ledger, or every downstream mart. Your recovery playbook must reconcile those related states before restarting publication.

Finalize numbered procedures for deploy, source replay, historical backfill, quarantine repair, alert triage, and recovery. Each procedure needs prerequisites, the command or action, expected evidence, and a stop condition. Ask your reviewer to follow one without your verbal help.

Only claim measured improvements. Include baseline conditions, actual query or job metrics, and preserved correctness. If the project has not run under sustained production conditions, describe it as a production-style course release rather than implying a live operational track record.

For the lab, cut the tagged release after the checks pass in your authorized project. Assemble the charter, architecture, performance notes, runbook, and readable README around the same version.

Practical advice: the release is ready when its important actions can be repeated by someone who did not build it. Every undocumented manual rescue you discover becomes the next concrete improvement.

## Screen example — not spoken

```text
Release evidence
Code revision and tag:
Bundle target and resolved catalog:
Deploy identity / workload identity:
Source versions and input window:
Cold-run outcome and current test counts:
Injected failure -> publication blocked -> repair result:
Replay/backfill result and business-content comparison:
Restore drill -> related-state reconciliation -> verified restart:
Operator who followed the runbook:
```

Fill this with actual current-run evidence. A tag, deployment exit code, or open job page alone does not prove the workflow works.
