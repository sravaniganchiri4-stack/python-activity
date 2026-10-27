
# Laboratory Chemical Inventory Validation

max_quantity = {
    "Flammable": 50,
    "Corrosive": 30,
    "Oxidizer": 20,
    "General": 100
}

incompatible = [
    ("Flammable", "Oxidizer"),
    ("Acid", "Base")
]

inventory = []
n = int(input("Enter number of chemical records: "))

for i in range(n):
    print("\nChemical", i + 1)

    name = input("Enter chemical name: ")
    category = input(
        "Enter category (Flammable/Corrosive/Oxidizer/General/Acid/Base): "
    ).title()
    quantity = float(input("Enter quantity in liters: "))

    inventory.append({
        "name": name,
        "category": category,
        "quantity": quantity
    })

print("\n----- VALIDATION REPORT -----")

invalid_found = False

for chemical in inventory:
    name = chemical["name"]
    category = chemical["category"]
    quantity = chemical["quantity"]

    errors = []

    if category not in max_quantity and category not in ["Acid", "Base"]:
        errors.append("Invalid storage category")

    if category in max_quantity:
        if quantity > max_quantity[category]:
            errors.append("Maximum quantity exceeded")

    if quantity <= 0:
        errors.append("Quantity must be positive")

    for other in inventory:
        if chemical["name"] == other["name"]:
            continue

        pair = (category, other["category"])
        reverse_pair = (other["category"], category)

        if pair in incompatible or reverse_pair in incompatible:
            errors.append(
                "Incompatible category with " + other["name"]
            )

    if errors:
        invalid_found = True
        print("\n", name, "- INVALID")
        for error in set(errors):
            print("-", error)
    else:
        print("\n", name, "- VALID")

if not invalid_found:
    print("\nAll chemical records are valid.")
