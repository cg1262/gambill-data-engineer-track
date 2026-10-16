#!/usr/bin/env python3
"""Generate the Bridge placement-diagnostic datasets into site/diagnostic/.
Deterministic (fixed seed) so re-running produces identical files.

Task 1 (window functions): task1_sales.csv — regional sales by rep by month, with a deliberate tie.
Task 2 (Python + reconcile): task2_customers.csv (messy) + task2_customers_api.json (the "API"),
        reconcile on customer_id — matched / csv-only / api-only / value-mismatch all present.
Task 3 (dimensional modeling): task3_orders.csv — a wide denormalized order-line file.
"""
import csv, json, os, random

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "site", "diagnostic")
os.makedirs(OUT, exist_ok=True)
random.seed(42)

# ---------- Task 1: sales (clean, for window functions) ----------
regions = {
    "North": ["Ava Nguyen", "Ben Ortiz", "Cara Webb"],
    "South": ["Dan Reyes", "Elan Cho", "Faye Ingram"],
    "East":  ["Gus Patel", "Hana Lund", "Ivan Serra"],
    "West":  ["Jo Mbeki", "Kit Rao", "Lia Frost"],
}
months = ["2024-01", "2024-02", "2024-03"]
rows = []
base = {"Ava Nguyen": 42000, "Ben Ortiz": 38000, "Cara Webb": 51000,
        "Dan Reyes": 33000, "Elan Cho": 47000, "Faye Ingram": 29000,
        "Gus Patel": 60000, "Hana Lund": 44000, "Ivan Serra": 44000,  # Gus/Hana tie setup in Jan
        "Jo Mbeki": 36000, "Kit Rao": 52000, "Lia Frost": 41000}
for region, reps in regions.items():
    for mi, month in enumerate(months):
        for rep in reps:
            rev = base[rep] + mi * random.randrange(-3000, 7000, 1000)
            rows.append({"region": region, "sales_rep": rep, "order_month": month, "revenue": rev})
# Force an exact tie in East / 2024-01 so RANK vs ROW_NUMBER vs DENSE_RANK differ
for r in rows:
    if r["region"] == "East" and r["order_month"] == "2024-01" and r["sales_rep"] in ("Hana Lund", "Ivan Serra"):
        r["revenue"] = 44000
with open(os.path.join(OUT, "task1_sales.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["region", "sales_rep", "order_month", "revenue"])
    w.writeheader(); w.writerows(rows)

# ---------- Task 2: messy customers CSV + JSON "API" ----------
first = ["Maria", "John", "Wei", "Amara", "Luca", "Priya", "Noah", "Zara", "Omar", "Elena",
         "Hiro", "Sofia", "Kwame", "Ingrid", "Diego", "Fatima", "Sean", "Yuki", "Pavel", "Rosa",
         "Tariq", "Nadia", "Ethan", "Lena", "Mateo"]
last = ["Alvarez", "Smith", "Zhang", "Okafor", "Rossi", "Patel", "Kim", "Haddad", "Novak", "Reed",
        "Tanaka", "Moreau", "Mensah", "Larsen", "Costa", "Rahman", "Walsh", "Sato", "Ivanov", "Diaz",
        "Aziz", "Petrov", "Brown", "Berg", "Cruz"]
regions_list = ["North", "South", "East", "West"]
def money(v, style):
    if style == 0: return str(v)
    if style == 1: return f"${v:,}"
    return f"{v:.2f}"
date_styles = ["2023-%02d-%02d", "%02d/%02d/2023", "%s %d, 2023"]
monthnames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def make_date(i):
    mm = (i % 12) + 1; dd = (i % 27) + 1
    s = date_styles[i % 3]
    if "%s" in s: return s % (monthnames[mm - 1], dd)
    if s.startswith("2023-"): return s % (mm, dd)
    return s % (mm, dd)

csv_rows = []
# CSV holds ids 1001..1025 (+ two duplicates); API holds 1010..1035
for n, i in enumerate(range(1001, 1026)):
    name = f"{first[n % len(first)]} {last[(n * 3) % len(last)]}"
    # inject mess: trailing spaces, mixed money, some blanks
    name_field = name + ("  " if i % 4 == 0 else "")
    region = "" if i % 7 == 0 else regions_list[i % 4]
    ltv = money(1000 + (i - 1000) * 37, i % 3)
    email = "" if i % 5 == 0 else f"{name.split()[0].lower()}.{name.split()[1].lower()}@example.com"
    csv_rows.append({"customer_id": i, "name": name_field, "signup_date": make_date(i),
                     "region": region, "lifetime_value": ltv, "email": email})
# duplicate ids 1007 and 1013 with a slightly different name (dedup practice)
dup7 = dict(csv_rows[6]); dup7["name"] = dup7["name"].strip() + "-Jr"; csv_rows.append(dup7)
dup13 = dict(csv_rows[12]); dup13["email"] = ""; csv_rows.append(dup13)
with open(os.path.join(OUT, "task2_customers.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["customer_id", "name", "signup_date", "region", "lifetime_value", "email"])
    w.writeheader(); w.writerows(csv_rows)

# API: authoritative-ish records, clean numeric types; ids 1010..1035
api = []
for n, i in enumerate(range(1010, 1036)):
    name = f"{first[n % len(first)]} {last[(n * 3) % len(last)]}"
    region = regions_list[(i + 1) % 4]  # deliberately differs from CSV region for some ids -> value-mismatch
    ltv = 1000 + (i - 1000) * 37
    # make a few ltv values disagree with CSV to force value-mismatch detection
    if i in (1012, 1018, 1022):
        ltv += 500
    api.append({"customer_id": i, "name": name, "region": region,
                "lifetime_value": ltv, "status": "active" if i % 3 else "churned"})
with open(os.path.join(OUT, "task2_customers_api.json"), "w") as f:
    json.dump({"generated": "static diagnostic endpoint", "count": len(api), "customers": api}, f, indent=2)

# ---------- Task 3: wide denormalized order lines ----------
customers = {
    "C001": ("Acme Retail", "Enterprise", "West"),
    "C002": ("Bluebird Cafe", "SMB", "North"),
    "C003": ("Cedar Clinic", "Healthcare", "East"),
    "C004": ("Delta Logistics", "Enterprise", "South"),
    "C005": ("Echo Studio", "SMB", "West"),
}
products = {
    "SKU-100": ("Standard Widget", "Widgets", 12.50),
    "SKU-200": ("Pro Widget", "Widgets", 24.00),
    "SKU-300": ("Gadget Mini", "Gadgets", 8.75),
    "SKU-400": ("Gadget Max", "Gadgets", 33.00),
    "SKU-500": ("Service Plan", "Services", 99.00),
}
cust_ids = list(customers); sku_ids = list(products)
order_rows = []
line_id = 0
for o in range(1, 26):  # 25 orders
    order_id = f"ORD-{3000 + o}"
    cust = cust_ids[o % len(cust_ids)]
    cname, cseg, creg = customers[cust]
    day = (o % 27) + 1
    order_ts = f"2024-02-{day:02d}T{9 + (o % 8):02d}:{(o * 7) % 60:02d}:00"
    n_lines = 1 + (o % 3)
    for _ in range(n_lines):
        line_id += 1
        sku = sku_ids[(line_id * 2) % len(sku_ids)]
        pname, pcat, price = products[sku]
        qty = 1 + (line_id % 5)
        order_rows.append({
            "order_id": order_id, "order_line_id": f"L-{line_id:04d}", "order_ts": order_ts,
            "customer_id": cust, "customer_name": cname, "customer_segment": cseg, "customer_region": creg,
            "product_sku": sku, "product_name": pname, "product_category": pcat,
            "unit_price": price, "quantity": qty,
        })
with open(os.path.join(OUT, "task3_orders.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["order_id", "order_line_id", "order_ts", "customer_id",
                                      "customer_name", "customer_segment", "customer_region",
                                      "product_sku", "product_name", "product_category",
                                      "unit_price", "quantity"])
    w.writeheader(); w.writerows(order_rows)

# ---------- folder README ----------
with open(os.path.join(OUT, "README.md"), "w") as f:
    f.write(
        "# Bridge placement-diagnostic datasets\n\n"
        "Generated by `build/make_diagnostic_data.py` (deterministic). Used by the four diagnostic tasks on the Bridge page.\n\n"
        "- **task1_sales.csv** — regional sales by rep by month (window-function practice; contains a deliberate revenue tie in East / 2024-01).\n"
        "- **task2_customers.csv** + **task2_customers_api.json** — reconcile on `customer_id`. The CSV is messy (duplicate ids, mixed date formats, blank fields, money as `$1,234`); the JSON is the clean 'API'. Expect matched / csv-only / api-only / value-mismatch records.\n"
        "- **task3_orders.csv** — a wide, denormalized order-line file for designing a star schema (one fact + customer/product/date dimensions).\n"
    )

print("wrote diagnostic datasets to", OUT)
for fn in sorted(os.listdir(OUT)):
    print("  ", fn, os.path.getsize(os.path.join(OUT, fn)), "bytes")
print("task1 rows:", len(rows), "| task2 csv rows:", len(csv_rows), "api:", len(api), "| task3 lines:", len(order_rows))
