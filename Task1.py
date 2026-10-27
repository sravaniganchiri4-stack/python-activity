# Traffic Violation Penalty Calculator

fine_rules = {
    "Car": {
        "Over Speeding": 1000,
        "No Helmet": 0,
        "Drunk Driving": 10000,
        "Signal Jump": 1000
    },
    "Bike": {
        "Over Speeding": 1000,
        "No Helmet": 500,
        "Drunk Driving": 10000,
        "Signal Jump": 1000
    }
}

total_fine = 0
violations = int(input("Enter number of violations: "))
disqualified = False

for i in range(violations):
    print("\nViolation", i + 1)

    vehicle = input("Enter vehicle category (Car/Bike): ").title()
    offence = input(
        "Enter offence (Over Speeding/No Helmet/Drunk Driving/Signal Jump): "
    ).title()
    repeat = input("Is it a repeat offence? (yes/no): ").lower()

    if vehicle not in fine_rules:
        print("Invalid vehicle category!")
        continue

    if offence not in fine_rules[vehicle]:
        print("Invalid offence type!")
        continue

    fine = fine_rules[vehicle][offence]

    if repeat == "yes":
        fine = fine * 2

    if offence == "Drunk Driving":
        disqualified = True

    total_fine += fine

    print("Penalty for this violation: Rs.", fine)

print("\n----- FINAL REPORT -----")
print("Total violations:", violations)
print("Total penalty: Rs.", total_fine)

if disqualified:
    print("Driving disqualification: Possible")
else:
    print("Driving disqualification: Not flagged")