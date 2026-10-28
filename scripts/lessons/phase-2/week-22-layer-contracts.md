# Week 22: Turn layer names into enforceable promises

Module M15 · [Course lesson](../../../site/phase-2.html#w22)

## Script

You have bronze, silver, and gold folders. A dashboard still cleans prices differently from the compliance report. The folder names did not create a shared definition of clean.

This week, write the contract at each boundary and implement checks that can fail. Bronze preserves the landed source representation with provenance. Silver parses, validates, standardizes, and applies the declared entity or record grain. Gold presents business measures and consumption models using that trusted foundation.

Be precise about the word raw. Metadata such as retrieval time can be typed. The requirement is that the original payload remains recoverable and unaltered. A source that already contains JSON numbers does not need every value converted to a string merely to earn a bronze label.

For silver, choose four concrete standardizations. Parse the chosen monetary format into a decimal. Normalize provider-name whitespace. Validate state codes. Preserve postal codes as strings with the source's country-specific rules. Zero-padding every postal code in the world would create another cleaning bug.

Tag validation results before splitting rows. Use the same classified input to produce accepted and rejected outputs. A row may violate several rules, so keep all applicable reasons. Write the source payload and lineage with the rejection so you can repair the transformation and replay it later.

Think of the layers as a restaurant kitchen's handoff stations. Receiving checks the shipment, preparation produces usable ingredients, and plating assembles the dish. If every server cleans ingredients differently at the table, the handoff has failed.

Enforce the promises with more than a naming convention. Assert required provenance, expected types, grain uniqueness, and conservation of records at the boundary. Check the dependency graph so a gold view cannot quietly start reading an unvalidated bronze source. A schema check alone cannot prove arbitrary cleaning logic stayed out of gold; use code review and targeted architecture tests as well.

For the lab, inject a deliberate violation. Remove a provenance field or change a required field's type and show the check failing. Restore it and demonstrate that accepted plus rejected accounts for the classified input, with duplicates tracked separately if the step collapses them.

Finally, rerun a fixed input ten times and compare business content. Your contract should tell the next engineer where a change belongs and which test will complain if they put it in the wrong place.

## Screen example — not spoken

```python
from decimal import Decimal, InvalidOperation

def parse_demo_usd(raw):
    if raw is None or not str(raw).strip():
        return None, "missing_price"
    try:
        value = Decimal(str(raw).replace("$", "").replace(",", "").strip())
    except InvalidOperation:
        return None, "invalid_price"
    if not value.is_finite() or value < 0:
        return None, "invalid_price"
    return value, None

assert parse_demo_usd("$1,234.50") == (Decimal("1234.50"), None)
assert parse_demo_usd("not a price")[1] == "invalid_price"
```

This parser handles a deliberately narrow US-dollar fixture. Production parsing needs the actual source's locale, currency, rate type, and unit contract.
