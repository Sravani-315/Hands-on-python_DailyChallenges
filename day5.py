print("=== Doraemon's Smart Transport System ===")
print("Doraemon opens Anywhere Door and starts loading packages...\n")

n = int(input("Enter number of packages Doraemon found: "))

weights = [0] * n
for i in range(n):
    weights[i] = int(input("Enter weight of package: "))

print("\nEntered Weights:", weights)
