
# Courier Charge Optimization

weight = float(input("Enter parcel weight (kg): "))
length = float(input("Enter length (cm): "))
width = float(input("Enter width (cm): "))
height = float(input("Enter height (cm): "))
distance = int(input("Enter distance zone (1-Local, 2-National, 3-International): "))
urgent = input("Urgent delivery? (yes/no): ").lower()
restricted = input("Restricted item? (yes/no): ").lower()

if weight <= 0 or min(length, width, height) <= 0 or distance not in [1, 2, 3]:
    print("Invalid parcel details")
else:
    rates = {1: 30, 2: 60, 3: 150}
    volume = length * width * height
    volumetric_weight = volume / 5000
    charge_weight = max(weight, volumetric_weight)

    services = {
        "Standard": (0, 7),
        "Express": (100, 2),
        "Premium": (200, 1)
    }

    eligible = []

    for service, (extra, days) in services.items():
        if urgent == "yes" and days > 2:
            continue
        if restricted == "yes" and service != "Standard":
            continue

        charge = charge_weight * rates[distance] + extra
        eligible.append((service, charge, days))

    print("\n----- COURIER OPTIONS -----")

    for service, charge, days in eligible:
        print(service, "- Rs.", round(charge, 2),
              "- Delivery:", days, "days")

    if eligible:
        best = min(eligible, key=lambda x: x[1])
        print("\nSelected service:", best[0])
        print("Minimum charge: Rs.", round(best[1], 2))
    else:
        print("No eligible courier service available")
