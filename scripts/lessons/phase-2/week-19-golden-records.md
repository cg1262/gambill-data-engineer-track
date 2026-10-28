# Week 19: Make a match decision you can reverse

Module M11 · [Course lesson](../../../site/phase-2.html#w19)

## Script

Two provider names look almost identical. One is a hospital and the other is an independent practice in the same building. A high name similarity is useful evidence. It is not permission to collapse them into one business entity.

This week, score the candidate pairs from your blocking step and turn scores into governed decisions. Compare multiple features: normalized name, address, postal code, entity type, and trustworthy identifiers where available. Keep the individual feature values so somebody can explain the result.

An edit-distance score measures string difference. It does not directly measure the probability that two records represent the same provider. If you combine weighted features, call the result a score unless you have calibrated it as a probability. Evaluate on labeled examples that include plausible nonmatches, not only obvious duplicates.

Choose separate outcomes: automatic resolution, human review, and no match. Set the thresholds from the business cost of false merges and false splits. In our pricing project, a false merge can attach one facility's prices to another. That can be more damaging than leaving a duplicate for review.

Be careful when turning accepted pairs into clusters. If A matches B and B matches C, connected components will group all three even if A and C strongly disagree. Think of introductions at a conference: knowing the same person does not make two attendees the same person. Add cluster-level consistency checks and preserve the ability to split an incorrect cluster.

For survivorship, choose winning fields using explicit source priority, recency, completeness, and tie rules. Store which source row supplied each golden value. The golden record should be a documented decision with lineage, rather than a mysterious blend.

For a fixed member set, a deterministic cluster hash can make reruns repeatable. It does not keep the identifier stable when new members arrive. A persistent identity registry and merge-or-split history are the stronger approach when downstream systems need durable IDs. Explain that boundary in your lab.

Show five real candidate examples, your threshold evidence, the review queue, and a rerun with unchanged business output. Record steward decisions and their reasons.

Practical advice: keep enough evidence to undo a bad match. Entity resolution will encounter ambiguous cases. A reviewable decision and a repair path are part of the product you are building.

## Screen example — not spoken

```python
def route(score):
    # Illustrative thresholds only; calibrate on labeled project data.
    if score >= 0.98:
        return "auto_candidate"
    if score >= 0.85:
        return "review"
    return "no_match"

assert route(0.90) == "review"
```

Show feature-level evidence, a type-conflict veto, and field lineage beside the score. `auto_candidate` still requires the entity/cluster checks; these numbers are not recommended production thresholds.
