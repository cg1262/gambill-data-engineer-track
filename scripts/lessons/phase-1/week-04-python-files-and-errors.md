# Week 4: Give every bad record somewhere to go

Module M02 · [Course lesson](../../../site/phase-1.html#w4)

## Script

Your feed has a duplicate ID, a missing magnitude, and a record with the wrong shape. You could put a broad exception handler around the loop and keep going. The report would finish. You would have no idea what disappeared.

This week, make the accounting visible using Python's basic collections. A list holds the records you will process. A dictionary represents a record's named fields or an aggregate keyed by region. A set tracks IDs you have already seen. A tuple can represent a fixed combination of values. Choose the collection for the operation you need, rather than converting everything into nested lists.

Use a context manager when opening files. `with open` gives the file a clear lifetime and closes it when you leave the block. Use `json.load` for a file object and `json.loads` for a string. That small naming difference matters when you start moving between files and HTTP responses.

Validate at the right boundary. A syntactically broken JSON document may prevent you from parsing the file at all. Record that as a file-level failure. A valid document containing one malformed feature can go through a row-level quarantine path. You cannot quarantine individual rows you were never able to parse.

For each parsed feature, require the fields your contract needs. Check the ID, structure, and magnitude before adding its ID to the accepted set. Otherwise, a broken first occurrence could block a valid later occurrence of the same event. Write down your policy for conflicting duplicates as well as exact repeats.

Catch the exceptions you expect, such as a failed numeric conversion. Include the original payload, a reason, and a rejection timestamp. Think of the rejects file as the returns desk: the item needs a label explaining why it came back and enough information for somebody to investigate.

For the exercise, inject four cases into a fixed sample: missing ID, null magnitude, malformed feature, and duplicate ID. Predict where each should go before running the program. Compare that prediction with accepted, rejected, and collapsed counts.

Finally, rerun the same input. Business aggregates should match, and the rejects file should contain one run's evidence rather than two appended copies. A new observation timestamp may change, so compare the meaningful record content separately. Save the validation rules and overwrite policy in your decision note.

## Screen example — not spoken

```python
seen = set()
accepted = []
rejected = []
collapsed = 0
for row in [{"id": "a", "mag": 2.1}, {"id": "a", "mag": 2.1},
            {"id": "b", "mag": None}]:
    if row.get("mag") is None:
        rejected.append({"payload": row, "reason": "missing magnitude"})
    elif row["id"] in seen:
        collapsed += 1
    else:
        seen.add(row["id"])
        accepted.append(row)
assert len(accepted) + len(rejected) + collapsed == 3
```

The lab extends this tiny accounting example with shape checks, timestamps, region aggregates, and file output.
