n = int(input("Enter no.of readings: "))
readings = []
for i in range(n):
    value = int(input("Enter reading: "))
    readings.append(value)
valid = [e for e in readings if e >= 0]
total = sum(valid)
avg = total / len(valid) if valid else 0
print("\nCampus Average Energy:", round(avg, 2))
user = int(input("Enter your building energy: "))
if user > avg:
    print("\n Access Granted: Your energy is above average\n")
    energy_dict = {
        "efficient": [],
        "moderate": [],
        "high": [],
        "invalid": []
    }
    for i in readings:
        if i < 0:
            energy_dict["invalid"].append(i)
        elif i <= 50:
            energy_dict["efficient"].append(i)
        elif i <= 150:
            energy_dict["moderate"].append(i)
        else:
            energy_dict["high"].append(i)

    buildings = len(readings)

    summary = (total, buildings)

    high_c = len(energy_dict["high"])
    eff_c = len(energy_dict["efficient"])
    mod_c = len(energy_dict["moderate"])

    if total > 600:
        result = "Energy Waste Detected"
    elif high_c > 3:
        result = "Overconsumption"
    elif abs(eff_c - mod_c) <= 1:
        result = "Balanced Usage"
    elif eff_c > mod_c and eff_c > high_c:
        result = "Efficient Campus"
    else:
        result = "Moderate Usage"
    print("--- Smart Campus Energy Report ---")
    print("Categorized Readings:")
    for key, value in energy_dict.items():
        print(f"{key.capitalize()}: {value}")

    print("\nTotal Consumption:", summary[0])
    print("Number of Buildings:", summary[1])
    print("Efficiency Result:", result)
else:
    print("\n Access Denied: Your energy is below or equal to average")
