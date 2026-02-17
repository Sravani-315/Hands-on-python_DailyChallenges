print("=== Doraemon's Smart Transport System ===")
print("Doraemon says: No passwords today! Trusting you like Nobita\n")
print("Doraemon opens Anywhere Door and starts loading packages...\n")

n = int(input("Enter number of packages Doraemon found: "))

weights = [0] * n
for i in range(n):
    k = int(input("Enter weight of package: "))
    weights[i] = k

print("\nEntered Weights:", weights)

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

valid_count = 0
affected_count = 0

name = "Nobitaa"
L = len(name)
PLI = L % 3

for w in weights:
    if w < 0:
        invalid_entries.append(w)
    elif w <= 5:
        very_light.append(w)
        valid_count += 1
    elif w <= 25:
        normal_load.append(w)
        valid_count += 1
    elif w <= 60:
        heavy_load.append(w)
        valid_count += 1
    else:
        overload.append(w)
        valid_count += 1

if PLI == 0:
    for i in overload:
        invalid_entries.append(i)
        affected_count += 1
    overload = []

elif PLI == 1:
    affected_count = len(very_light)
    very_light = []

elif PLI == 2:
    affected_count = len(very_light) + len(overload)
    very_light = []
    overload = []

print("\n--- Doraemon Transport Report ---")
print("Nobita Name Length (L):", L)
print("PLI Value:", PLI)
print("Total Valid Packages:", valid_count)
print("Packages affected by Doraemon's PLI magic:", affected_count)

print("\n--- Final Loading Plan ---")
print("Very Light Packages:", very_light)
print("Normal Load Packages:", normal_load)
print("Heavy Load Packages:", heavy_load)
print("Overload Packages:", overload)
print("Invalid Entries:", invalid_entries)

print("\nDoraemon says: All trucks are ready! Time to go Anywhere")
