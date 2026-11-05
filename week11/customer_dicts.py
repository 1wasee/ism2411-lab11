
# REFLECTION 1:
# I would use .get() when looking up information that might not exist,
# such as a customer's email or phone number. I would use brackets
# when I know the key exists and need its value. My rule of
# thumb is to use .get() for optional information and brackets for
# information that should always be available.

# REFLECTION 2:
# Exercise 8 reminds me of using a table in Excel to summarize
# sales. Python can be more useful for large datasets because
# it can automatically process a lot of transactions and update
# totals.

# EXERCISE 1: One customer

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 2500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2: Update and add

customer["phone"] = "813-555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3: Safe lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist in the dictionary")


# EXERCISE 4: Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives you the keys.
for key in customer:
    print(key)


# EXERCISE 5: Lookup table

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
purchase = 200
final_price = purchase * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")


# EXERCISE 6: List of dictionaries

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "gold"}
]

for customer in customers:
    tier = customer["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{customer['name']} | {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )


# EXERCISE 7: Nested catalog

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product in catalog:
    if catalog[product]["stock"] < 20:
        print(f"LOW STOCK: {product}")


# EXERCISE 8: Sales by region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]:.2f}")
