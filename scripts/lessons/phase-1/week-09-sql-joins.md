# Week 9: Keep the parent row you meant to keep

Module M05 · [Course lesson](../../../site/phase-1.html#w9)

## Script

Your customer report is supposed to include people who have never ordered. You write a left join, add a date filter, and those customers disappear. The join did exactly what you asked. The filter changed the question.

Start with the Chinook schema and trace the keys before writing the query. A customer can have several invoices. An invoice can have several lines. Joining through those relationships changes your result grain. Write “one row per customer” or “one row per invoice line” above the query so there is something specific to defend.

An inner join returns matches. A left join also keeps unmatched rows from the left side and fills the missing right-hand fields with nulls. SQL predicates use three-valued logic: true, false, and unknown. Comparing a null invoice date with a cutoff produces unknown, and a `WHERE` clause keeps only true.

That explains the disappearing customers. If your question is “all customers, with any invoices after this date,” place the invoice-date condition in the join condition. If your question is “customers who have qualifying invoices,” filtering in `WHERE` may be exactly right. Pick the location from the question you intend to answer.

Next, look at fan-out. One invoice total repeated across five invoice lines is still one invoice total. Summing the repeated header amount counts it five times. It is like photocopying a receipt for each purchased item and then adding all the receipt totals. Aggregate at the correct grain or use line amounts when the measure belongs to lines.

Use `IS NULL` when looking for an unmatched parent. Do not write equals null. For a self-join, such as employees and their managers, keep the top-level manager by using the same outer-join reasoning.

For your lab, run paired inner and left joins, record their row counts, and explain the exact difference. If your chosen Chinook extract has no customer without invoices, use an explicit synthetic example to demonstrate that case rather than claiming the dataset contains one.

Before you finish, point to one query that could inflate revenue and one that could erase a customer. Explain the business consequence of each. That is the skill you need when a report looks reasonable but answers a different question.

## Screen example — not spoken

Portable DuckDB teaching example:

```sql
WITH customers(id) AS (VALUES (1), (2)),
invoices(customer_id, invoice_date) AS (
  VALUES (1, DATE '2024-02-01')
)
SELECT c.id, i.invoice_date
FROM customers c
LEFT JOIN invoices i
  ON c.id = i.customer_id
 AND i.invoice_date >= DATE '2024-01-01'
ORDER BY c.id;
```

Expect two rows, including customer 2 with a null invoice date. Move the date predicate to `WHERE` and expect one.
