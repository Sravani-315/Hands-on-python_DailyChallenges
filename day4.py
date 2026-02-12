print("Enter numbers and words:")
user_input = input()
data = user_input.split()
n = []
s = []
count_num = 0
count_str = 0
name = input("Enter your Name: ")
name_length = 0
for ch in name:
    name_length = name_length + 1
if name_length < 5:
    print("Access Denied: Name length must be at least 5 characters")
else:
    reg_no = int(input("Enter last digit of Register Number: "))
    for item in data:
        is_number = True
        for ch in item:
            if ch < '0' or ch > '9':
                is_number = False
        if is_number == True:
            n = n + [int(item)]
            count_num = count_num + 1
        else:
            if item != "":
                s = s + [item]
                count_str = count_str + 1

    if reg_no % 2 == 0:
        if count_num > 0:
            n.pop(0)
            count_num = count_num - 1
        if count_str > 0:
            s.pop(0)
            count_str = count_str - 1
    else:
        if count_num > 0:
            n.pop()
            count_num = count_num - 1
        if count_str > 0:
            s.pop()
            count_str = count_str - 1

    if count_str >= 2:
        rev = []
        i = count_num - 1
        while i >= 0:
            rev = rev + [n[i]]
            i = i - 1
        n = rev

    print("Numbers List:", n)
    print("Strings List:", s)
    print("Total Numbers:", count_num)
    print("Total Strings:", count_str)
