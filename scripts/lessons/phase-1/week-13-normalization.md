# Week 13: Put each fact about a restaurant in one place

Module M07 · [Course lesson](../../../site/phase-1.html#w13)

## Script

A restaurant changes its name. Your inspection export contains the old name on fifty rows and the new name on ten. Which name should a report show? Repeating an attribute creates opportunities for the copies to disagree.

Use the NYC restaurant-inspection extract to discover those dependencies before splitting tables. A functional dependency says that one set of attributes determines another. If restaurant ID determines the current restaurant name, each ID should map to one name in the modeled snapshot. Profile distinct values per key and inspect exceptions.

Be careful with history. Two addresses for one restaurant may be bad data, or a legitimate move across time. A sample that happens to have one value does not establish an eternal business rule. Write the time boundary and confirm the meaning of the key before treating a dependency as guaranteed.

Now separate restaurant attributes from inspection events and violation details. First normal form removes repeating groups within the chosen relational design. Second normal form removes dependencies on only part of a candidate key. Third normal form removes inappropriate transitive dependencies between nonkey attributes. Adding an integer ID does not repair those dependencies by itself.

Picture an address book and an appointment calendar. You keep the contact's address with the contact, and the appointment time with the appointment. Copying the address into every appointment makes a simple correction become a search through the entire calendar.

Define primary keys and foreign keys in DuckDB. A primary key prevents duplicate identifiers; a foreign key prevents a child row from referring to a missing parent. Neither constraint decides whether your business key was modeled correctly. You still need a defensible inspection identifier when the source has multiple violations per inspection.

Before loading constrained tables, quarantine null keys, invalid dates, and orphan records with reasons. Keep those rows visible instead of disabling the constraints to make the load finish.

For the lab, show three profiled dependencies, the decomposition diagram, and the rerunnable load. Deliberately attempt a duplicate primary key and an invalid foreign key in your disposable exercise database, and capture the expected errors.

Then defend one deliberate denormalization. Name the query it helps and the update risk it brings back. The practical skill is deciding where an attribute belongs and understanding the maintenance cost when you choose to repeat it.

## Screen example — not spoken

DuckDB, in an empty disposable database:

```sql
CREATE TABLE restaurant (
  restaurant_id VARCHAR PRIMARY KEY,
  name VARCHAR
);
CREATE TABLE inspection (
  inspection_id VARCHAR PRIMARY KEY,
  restaurant_id VARCHAR REFERENCES restaurant(restaurant_id),
  inspection_date DATE
);
INSERT INTO restaurant VALUES ('R1', 'Example Cafe');
INSERT INTO inspection VALUES ('I1', 'R1', DATE '2024-01-01');
```

Run these separately and capture each expected constraint error:

```sql
INSERT INTO restaurant VALUES ('R1', 'Duplicate');
INSERT INTO inspection VALUES ('I2', 'UNKNOWN', DATE '2024-01-02');
```
