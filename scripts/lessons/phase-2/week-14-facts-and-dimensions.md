# Week 14: Separate the price from its context

Module M08 · [Course lesson](../../../site/phase-2.html#w14)

## Script

A hospital appears under three names, and a pricing report treats those names as three different facilities. Before adding another dashboard calculation, you need a model that separates the thing being measured from the context describing it.

This week starts Provider Pricing Integrity, our running healthcare project. Inspect a bounded CMS hospital machine-readable file and a small NPPES extract. Keep the original files and document their versions. Public healthcare pricing and provider records give us useful modeling problems without needing patient data.

Classify the fields. A price amount is a candidate measure. Facility, procedure, payer, and plan describe the context in which that price applies. The fact table connects those contextual keys with the measure and the relevant date or publication period.

Do not confuse a price with a payment. Ten posted prices do not add up to actual spending. A rate is generally non-additive across procedures or contracts. To estimate spend, you need an appropriate quantity and a compatible unit of price, plus a clearly labeled methodology. Even a gross charge is not automatically realized revenue.

Think of a menu. The listed price describes an item under certain conditions. Summing every price on the menu does not tell you what the restaurant earned last night. That distinction protects you from building a mathematically valid but meaningless KPI.

Next, distinguish natural and surrogate keys. An NPI is an identifier from a source domain. A warehouse provider key identifies the dimension row your model uses. Surrogate keys help manage source changes and later history, but generating a new integer does not resolve two records that refer to the same provider. Entity resolution comes later.

Write the project charter around a named consumer and a real question. Define pricing completeness, quarantined records, duplicate resolution, and freshness using explicit numerators, denominators, and time windows. State which inputs each measure needs. If you have not measured a baseline, label it as pending rather than inventing a result.

For the lab, annotate representative source columns, draw the initial fact-and-dimension model, and create the empty typed skeleton. We will make the detailed grain decision next week, before loading the analytical fact.

Your practical advice is to challenge the measure before polishing the schema. Ask what the number means, where it is valid, and whether it can actually answer the consumer's question.

## Screen example — not spoken

```text
Source field                 Candidate role
negotiated dollar amount     Measure, only with rate type/unit/context
procedure code + code type   Procedure dimension business key components
payer name + plan name       Payer/plan context requiring normalization
facility source identifier   Facility key candidate; profile its quality
source file + publish date   Provenance and snapshot context

Example KPI specification:
Pricing completeness = eligible facilities meeting the agreed
required-field rule / eligible facilities evaluated, per source period.
```

Show one actual source row. Do not substitute the illustrative role list for source profiling.
