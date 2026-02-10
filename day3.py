n = int(input("Enter no.of students: "))
marks = []
for i in range(n):
    k = int(input("Enter mark: "))
    marks.append(k)
valid = 0
failed = 0
for m in marks:
    if m < 0 or m > 100:
        print(m, "→ Invalid")
    else:
        valid = valid + 1
        if m>=90 and m<=100:
            print(m, "→ Excellent")
        elif m>=75 and m<=89:
            print(m, "→ Very Good")
        elif m>=60 and m<=74:
            print(m, "→ Good")
        elif m>=40 and m<=59:
            print(m, "→ Average")
        else:
            print(m, "-> Fail (Don't worry failure is the stepping stone to succes)")
            failed = failed + 1
print("Final summary:")
print("Total Valid Students:", valid)
print("Total Failed Students:", failed)
