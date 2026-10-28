# Week 15: Write the grain before choosing the key

Module M08 · [Course lesson](../../../site/phase-2.html#w15)

## Script

You have two rows for the same hospital and procedure. Are they duplicates? Maybe one is a different payer. Maybe one is an inpatient rate and the other is outpatient. Deduping before answering that question can erase a legitimate price.

This week, turn last week's sketch into an explicit fact grain. Profile the actual CMS file and write what one row represents. Your candidate may need facility, procedure code and code system, payer, plan, setting, rate type, and source period. Include every attribute required to distinguish legitimate observations in your chosen source.

Then build a uniqueness query over that candidate key. A duplicate result is an investigation queue. Look at the differing columns and decide whether the grain is incomplete, the source duplicated an observation, or the record cannot be interpreted safely. Do not use `DISTINCT` as a substitute for that decision.

A useful analogy is a shipping label. Street address alone might identify a building, but you still need the apartment number to identify the delivery. Adding the missing field changes a false duplicate into two valid destinations.

Now design conformed provider and service dimensions. Conformed means compatible keys, attributes, and business definitions across processes. Two tables called provider are not automatically conformed. Pricing and a future claims process must agree on which identity a provider key represents.

Make a bus matrix with business processes down one side and shared dimensions across the top. This exposes where you expect reuse. It also makes disagreement visible before separate teams create incompatible versions of the same concept.

For now, keep dimension updates simple and document the static or Type 1 behavior. Next week introduces Type 2 history. When mapping natural keys to surrogate keys, quarantine missing or ambiguous mappings, or use a deliberately defined unknown-member policy. Never let an inner join silently remove the problem.

For the lab, materialize the declared grain, build the conformed dimensions, and prove that rerunning the same input produces the same business rows. If you use an early silver fixture before the later ingestion build, label it as a staged exercise input.

Before finishing, pick one apparent duplicate and explain its resolution. Your model becomes trustworthy when you can say why two rows are the same observation, why they are different, and what evidence supports that decision.

## Screen example — not spoken

Spark SQL; `pricing_candidate` is the learner's staged, profiled source:

```sql
SELECT facility_id, code_system, procedure_code, payer, plan,
       setting, rate_type, source_period, COUNT(*) AS copies
FROM pricing_candidate
GROUP BY facility_id, code_system, procedure_code, payer, plan,
         setting, rate_type, source_period
HAVING COUNT(*) > 1;
```

Adapt this candidate key to the source's actual distinctions. Zero rows is evidence for this input, not proof that the business grain will never evolve.
