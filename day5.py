print("=== Doraemon's Smart Transport System ===")
print("Doraemon opens Anywhere Door and starts loading packages...\n")

n = int(input("Enter number of packages Doraemon found: "))

weights = [0] * n
for i in range(n):
    weights[i] = int(input("Enter weight of package: "))

print("\nEntered Weights:", weights)

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

valid_count = 0

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

print("Very Light Packages:", very_light)
print("Normal Load Packages:", normal_load)
print("Heavy Load Packages:", heavy_load)
print("Overload Packages:", overload)
print("Invalid Entries:", invalid_entries)
