# Week 21: Land a source version you can replay

Module M14 · [Course lesson](../../../site/phase-2.html#w21)

## Script

The job ran twice after a timeout. Your bronze table now contains two copies of the same file, and nobody can tell which copy belongs to the successful run. This week, give each source version an identity before it becomes pipeline input.

Work with a bounded NPPES API extract, the documented bulk option, and a CMS pricing file. Inspect the source's access limits rather than assuming an API can serve an entire national registry. Use bulk distribution for the large snapshot when that is the supported route. An API is useful for targeted retrieval; pagination limits still apply.

Land the raw response or source file without changing its business values. Attach source, source file, retrieval time, batch identity, and a content checksum or reliable source version. Keep the bytes you need to replay the parser. A parsed row table alone may not preserve everything the original file contained.

Now create a manifest: one record per logical source version with landing location, checksum, status, and timing. Think of it as the receiving log at a warehouse. The boxes on the floor are not enough; the log tells you which shipment arrived, whether it is complete, and whether it was already accepted.

Design the retry boundary. If landing succeeded but the manifest update failed, the next attempt must recognize the same source version and reconcile that incomplete state. A new random run ID on every retry is useful for attempts, but it should not make the same source file look like new business input.

Keep accepted bronze history immutable across different source versions. If your lab uses partition replacement to make a retry safe, scope the replacement to the complete logical slice. Overwriting an entire ingest date from one partial retry can erase other files from that day. Daily replacement is safe only when the rerun contains the complete intended daily contents.

Handle transient HTTP errors with bounded retry and preserve permanent failures. Record missing expected sources separately from successful no-change runs. You need a source-arrival expectation to distinguish the two.

For the exercise, demonstrate success, missing source, and failed retrieval. Rerun the same fixed source version ten times and inspect business rows, manifest state, and attempt evidence.

Your practical advice is to make replay a concrete operation: choose a landed version, locate its bytes, verify its identity, and process it again without silently creating another shipment.

## Screen example — not spoken

```python
import hashlib

raw = b'{"provider": "example", "price": "$100"}'
checksum = hashlib.sha256(raw).hexdigest()
logical_source_version = ("demo-pricing-source", checksum)
assert logical_source_version == (
    "demo-pricing-source", hashlib.sha256(raw).hexdigest()
)
print(checksum)
```

Demonstrate the manifest's already-landed path on the second attempt. Content identity must be combined with source context; identical bytes from unrelated sources need not be the same shipment.
