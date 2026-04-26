import copy

def auth():
    print("\n Doraemon Secret Door Authentication")

    user = input("Enter username: ")
    key = input("Enter secret key: ")

    valid = {
        "Nobita": "doraemon123",
        "Sravani": "futureKey",
        "Aslam": "cse205",
        "Datta": "secure",
        "Doraemon": "anywhereDoor"
    }

    if user in valid and valid[user] == key:
        print(" Access Granted! Secret Door Opened ")
        return True
    else:
        print(" Access Denied! Door Locked ")
        return False

def gen_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]

def rep_data(original):
    assigned = original             
    shallow = copy.copy(original)    
    deep = copy.deepcopy(original)   
    return assigned, shallow, deep

def mod_data(data, roll):
    for user in data:
        if roll % 2 == 0:
            user["data"]["files"].append("secret_door.txt")
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop(0)

        user["data"]["usage"] += 100

def integrity_check(original, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_files = set()

    for i in range(len(original)):
        org_files = set(original[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])

        if org_files == shallow_files:
            leakage_count += 1

        if org_files != deep_files:
            safe_count += 1

        overlap_files.update(org_files.intersection(shallow_files))

    return (leakage_count, safe_count, len(overlap_files))

def explain_mutation():
    print("\n--- EXPLANATION ---")
    print("Inner list got affected because shallow copy shares references of nested mutable objects.")
    print("So when the 'files' list is modified, both original and shallow copy reflect the change.")
    print("Deep copy avoids this by creating completely independent nested objects.")
    print("Doraemon Analogy: Sharing the same gadget pocket causes both users to see the same changes.")

def main():
    roll_number = 62  

    access = auth()
    original = gen_data()

    print("\n--- BEFORE MODIFICATION ---")
    print("Original:", original)

    assigned, shallow, deep = rep_data(original)

    if access:
        mod_data(shallow, roll_number)
        mod_data(deep, roll_number)
    else:
        print("\n Modification Blocked due to Failed Authentication")

    print("\n--- AFTER MODIFICATION ---")
    print("Original:", original)
    print("Assigned:", assigned)
    print("Shallow Copy:", shallow)
    print("Deep Copy:", deep)

    report = integrity_check(original, shallow, deep)

    print("\n--- INTEGRITY REPORT ---")
    print("Tuple Output:", report)

    explain_mutation()

main()
