# Week 39: Make the failed check block the risky change

Module M28 · [Course lesson](../../../site/phase-3.html#w39)

## Script

Your repository has a test workflow. The tests fail, and the pull request still merges. You have automated feedback, but you have not enforced the release condition you thought you had.

This week, connect meaningful tests to repository rules and environment promotion. Start with the fast deterministic suite on each pull request. Use a supported Python version, install the project's declared test dependencies, and run the command that actually discovers your tests. Record the test count and preserve the exit status.

A green job with zero tests is not evidence for your pipeline. Neither is a workflow that catches an exception and prints a friendly warning. Make the runner fail when the underlying validation fails, then confirm the relevant status check is required by the repository's branch rules.

Think of the workflow as an inspection station and the branch rule as the gate after it. The station can report a defect all day; the gate still needs to prevent the unchecked shipment from leaving.

Keep test levels honest about dependencies. Local unit tests should use tiny fixtures. A Databricks integration test needs a configured identity, compatible compute, and a disposable catalog. The production workspace should not be the convenient default when a test cannot find its target.

Separate permissions for checking code, deploying resources, and running the production workload. Prefer the supported short-lived workload identity or machine authentication for your platform. Do not pass deployment credentials to untrusted pull-request code. Forked contributions need a deliberate trust boundary.

Promote the reviewed code revision through development and staging evidence, then the configured production gate. An approval protects the action only when the job actually uses that protected environment and identity. Changing a label in YAML does not isolate the data.

For the lab, capture a planted failing assertion, a blocked merge, the corrected green run, and the production job waiting at its configured gate. Demonstrate the promotion in an environment you are authorized to change, using the intended catalog and identity.

Your practical advice is to trace one release from commit to target. Name the exact revision, the checks it passed, the identity that deployed it, and the data boundary it could modify. That is the evidence that makes automation trustworthy.

## Screen example — not spoken

Illustrative CI portion for the learner's pipeline repository, which must provide a pinned `requirements-dev.txt` and collected tests:

```yaml
name: Pipeline tests
on: pull_request
permissions:
  contents: read
jobs:
  unit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install -r requirements-dev.txt
      - run: python -m pytest -q
```

Check supported action releases and pin approved revisions for the recording project. This CI illustration does not configure branch protection, remote integration, authentication, or deployment gates; show those separately.
