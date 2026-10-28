# Week 3: Parse first, then make the decision

Module M02 · [Course lesson](../../../site/phase-1.html#w3)

## Script

A missing earthquake magnitude is not a magnitude of zero. If you turn every blank into zero, your script still runs, but you have changed what the source told you. This week you build a small command-line program that keeps that distinction visible.

Download one USGS CSV snapshot and keep it fixed while you develop. If you download a new live feed for every test, a changed result could come from your code or from a new earthquake. A fixed input lets you reason about the difference.

Break the program into three decisions. Parse the row. Classify a valid magnitude. Summarize the events above your threshold. Each function takes an input and returns a value. Printing is for the final report. A returned value is something another function can use; a printed value is a message you have already sent to the terminal.

For parsing, read the magnitude string. A blank becomes a rejected record with a reason. A nonnumeric value gets a different reason. A valid string becomes a float. Be careful with truthiness: zero is a valid number, even though Python treats it as false in an `if` statement. Test explicitly for missing values.

Then classify the clean number using the lesson's boundaries: below three is minor, below five is light, below six is moderate, and six or above is strong. The order matters. Once an earlier branch matches, later branches are skipped. Hand-check values right on the boundaries, including three, five, and six.

Read your threshold from the command line and fail clearly if the argument is missing or invalid. A bad operator argument should stop the run. A bad source row should follow the documented quarantine path. Those are different problems with different responses.

Now run the same snapshot with thresholds of two and four point five. On a snapshot with events between those values, the higher threshold gives fewer accepted events. Your rejected records stay the same because validation happens before threshold filtering. Write `rejected.csv` from scratch on each run so a retry does not duplicate the evidence.

Keep your functions small enough to explain without scrolling. For the lab, show the two reports and one rejected row. Then trace that row from its original string through your parsing decision. Being able to account for a record is more useful than merely showing a script that exits successfully.

## Screen example — not spoken

```python
def parse_magnitude(raw):
    if raw is None or not str(raw).strip():
        return None, "blank magnitude"
    try:
        return float(raw), None
    except ValueError:
        return None, "nonnumeric magnitude"

assert parse_magnitude("0") == (0.0, None)
assert parse_magnitude("") == (None, "blank magnitude")
```

This is the parsing decision only; the lab adds CSV input, classification, argument validation, summaries, and quarantine output.
