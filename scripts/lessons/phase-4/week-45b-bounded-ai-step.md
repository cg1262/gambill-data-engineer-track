# Week 45B: Give the model a narrow job and an exit route

Module M33 · Elective B · [Course lesson](../../../site/phase-4.html#w45)

## Script

The model returns a beautifully formatted category that does not exist in your reporting taxonomy. The JSON parser is happy. The dashboard now has another category nobody approved.

For this elective, add one bounded AI-assisted step to your capstone. Choose a task where language interpretation is useful, such as mapping messy descriptions to an approved category set. Keep deterministic parsing, joins, and arithmetic in ordinary code.

Define the output contract first: record identity, one permitted label or an abstention, and evidence tied to the input when the task requires it. Supply the relevant glossary and definitions. Treat source text as data to classify, even if it contains instructions. Do not allow an input record to redefine the task or request tools.

Think of the model as a junior classifier using a fixed form. It may suggest an answer, but the form's rules and the review process decide whether that answer enters the product.

Validate the response outside the model. Parse the JSON, verify the fields and types, enforce the allowed-value set, and reject an unexpected record identity. Schema correctness still does not prove the label is factually right. That requires evaluation against labeled examples and, for some decisions, human review.

Build a small development set and a separate held-out evaluation set. Include ambiguous descriptions, unknown categories, contradictory text, and instruction-like content. Choose per-label precision or recall, abstention coverage, and the cost of errors from the business use. A single overall accuracy can hide failure on the rare category that matters most.

Do not treat the model's self-reported confidence as a calibrated probability. Use measured decision criteria, route uncertain or invalid cases to review, and preserve the source record and response for investigation under an appropriate data policy.

Log model and prompt versions, input identity, validation result, latency, and cost. A fixed prompt does not guarantee deterministic outputs. If replay must reproduce a prior result, version and retain the accepted decision with its evidence rather than assuming a fresh call will match.

For the lab, compare the bounded step with a simple deterministic baseline. Show an invalid response being rejected, an ambiguous case abstaining, and held-out results without invented numbers.

Your practical advice is to keep the model replaceable. A narrow contract, explicit failure path, and measured evaluation let you improve the component without surrendering ownership of the data product.

## Screen example — not spoken

```python
ALLOWED = {"inpatient", "outpatient", "unknown"}

def validate_label(record_id, response):
    if not isinstance(response, dict):
        return "quarantine"
    if set(response) != {"record_id", "label"}:
        return "quarantine"
    if response["record_id"] != record_id:
        return "quarantine"
    if not isinstance(response["label"], str) or response["label"] not in ALLOWED:
        return "quarantine"
    return "review" if response["label"] == "unknown" else "eligible_for_eval_policy"

assert validate_label("r1", {"record_id": "r1", "label": "invented"}) == "quarantine"
```

No API key is needed for this local contract demonstration. An actual model call requires an authorized service and suitable data handling. A valid label still needs the task's measured acceptance policy.
