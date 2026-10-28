# Week 8: Test the component you will ship

Module M04 · [Course lesson](../../../site/phase-1.html#w8)

## Script

A test calls today's live earthquake feed and fails tomorrow because the feed changed. You do not know whether the component broke. This week, make your tests answer a more useful question: does the code honor its contract on an input whose expected result we know?

Take the reconciliation component and separate reading, transforming, and writing. A pure transformation accepts records and returns results without fetching a URL or modifying a file. That boundary lets you build a small committed fixture containing exactly the cases you need to explain.

Start with four cases: an empty feed, repeated event IDs, a missing ID, and a mismatch between reported and actual counts. For each case, write the expected outcome first. A missing identifier should produce the documented rejection. A duplicate should follow your dedupe policy. A count mismatch should become a visible result or exception according to the component's contract.

Use pytest parametrization to run the same rule against several inputs. Keep assertions about behavior. Checking that a function was called tells you less than checking that a bad record carries the correct reason and never enters the clean output. Think of a test fixture as a small examination paper where you already have the answer key.

Add type hints and run the static checker. A hint says what shape a function expects; Python does not automatically enforce it at runtime. Keep runtime validation at the source boundary. A `TypedDict` annotation cannot make a missing field appear in a JSON response.

Now build a wheel with `python -m build`. Install that wheel into a fresh environment and run its console command against the committed fixture. Editable installation can hide missing package files because it points back to your working tree. The wheel is what you are actually handing to somebody else.

For the lab, show the static check, meaningful passing tests, wheel installation, and command output. Include a negative case so we can see the guardrail working. Test reruns against the same fixture and inspect record content, not only row count.

Practical advice: when a real bug escapes, reduce it to a small fixture before fixing it. That gives you a permanent example of the failure and a focused way to prove the repair.

## Screen example — not spoken

Commands run in the learner's completed `quake-recon` project, with its development tools installed:

```bash
mypy src/
pytest -q
python -m build
```

In a new venv, install the specific wheel produced by this run and run:

```bash
quake-recon --input tests/fixtures/all_day.geojson
```

Show current test counts and the missing-ID rejection; do not substitute a zero-test exit or an old build artifact.
