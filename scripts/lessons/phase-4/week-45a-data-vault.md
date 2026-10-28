# Week 45A: Use a vault when source history earns the extra model

Module M12 · Elective A · [Course lesson](../../../site/phase-4.html#w45)

## Script

Three source systems disagree about the same customer, and the business needs to preserve exactly what each source said. Overwriting a single clean dimension loses evidence. This is the kind of pressure that can justify a Data Vault model.

For this elective, choose one subject area. A hub records a business key in its defined domain. A link records a relationship between keys. A satellite records descriptive context and history associated with the relevant hub or link. Keep load metadata and record source so an observation can be traced back to its origin.

Think of a case file. The identity section tells you who the case concerns, the relationship section connects the parties, and the dated evidence preserves what each source reported. You do not replace yesterday's evidence simply because a new document arrived.

Define the business-key policy before hashing. Two systems may use the same string for unrelated identities, or different strings for the same entity. A hash makes a chosen key reproducible; it does not solve that semantic conflict. Specify normalization, domain, field ordering, null representation, and encoding.

Load hubs and links idempotently at their declared key grain. For satellites, define the observation grain and change policy, including when a previously seen value returns after an intervening change. Deduping all history only by entity and payload hash can erase that recurrence. Preserve source-effective ordering where needed and separate it from load time.

Do not apply a generic Type 2 update algorithm and call every resulting table a raw vault. The model's insert-oriented history and lineage rules need a coherent loading design.

Then build a small star-schema mart for the actual consumer. A vault can make integration and audit history easier while requiring more joins and another presentation layer. Those costs are part of the decision, especially for a capstone with one stable source.

For the lab, show one hub, one meaningful relationship, and one descriptive history. Load the same fixed batch twice and prove no unintended duplicates. Demonstrate a changed attribute and trace the consumer-facing value back to source evidence.

Your practical advice is to use the extra structure only where it answers a real requirement. Write the ADR explaining what this model preserved that your simpler alternative would have lost, and what additional work you accepted to preserve it.

## Screen example — not spoken

Canonical hash-input demonstration, not a complete vault loader:

```python
import hashlib
import json

def hub_key(domain, normalized_business_key):
    encoded = json.dumps([domain, normalized_business_key],
                         ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

assert hub_key("customer-domain-a", "001") == hub_key("customer-domain-a", "001")
assert hub_key("customer-domain-a", "001") != hub_key("customer-domain-b", "001")
```

Choose whether source systems share a business-key domain from actual identity semantics. Do not automatically add source system to every hub key or strip leading zeros without a policy.
