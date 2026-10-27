
# Progressive Water Tariff Analysis

n = int(input("Enter number of households: "))

fixed_fee = 50
total_collection = 0
excess_count = 0

for i in range(n):
    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    units = float(input("Enter water consumption (units): "))

    if units < 0:
        print("Invalid consumption")
        continue

    # Progressive tariff calculation
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill += fixed_fee

    # Penalty for excessive usage
    penalty = 0
    if units > 300:
        penalty = 200
        excess_count += 1

    bill += penalty
    total_collection += bill

    print("Household:", name)
    print("Consumption:", units, "units")
    print("Fixed fee: Rs.", fixed_fee)
    print("Penalty: Rs.", penalty)
    print("Total bill: Rs.", bill)

    if units > 300:
        print("Warning: Excessive water usage!")
    else:
        print("Water usage: Normal")

print("\n----- FINAL REPORT -----")
print("Total collection: Rs.", total_collection)
print("Households with excessive usage:", excess_count)
