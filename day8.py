import random
import math
import numpy as np
import pandas as pd

ROLL_NUMBER = 62

def auth():
    print("Smart City System Login")

    name = input("Enter your name: ")
    fav = input("Are you a Doraemon fan? (yes/no): ").lower()

    if fav == "yes":
        print(f"Welcome {name}! Doraemon fan detected")
        role = "Premium User"
    else:
        print(f"Welcome {name}")
        role = "Normal User"

    return name, role


def gen_data(n=15):
    data = []
    for i in range(n):
        data.append({
            "zone": i+1,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })
    data.append({"zone": n+1, "traffic": 0, "air_quality": 50, "energy": 100})
    data.append({"zone": n+2, "traffic": 90, "air_quality": 280, "energy": 450})

    return data

def classify(d):
    if d["air_quality"] > 200 or d["traffic"] > 80:
        return "High Risk"
    elif d["energy"] > 400:
        return "Energy Critical"
    elif d["traffic"] < 30 and d["air_quality"] < 100:
        return "Safe"
    else:
        return "Moderate"


def risk(d):
    return (d["traffic"]*0.4 +
            d["air_quality"]*0.4 +
            d["energy"]*0.2 +
            math.sqrt(d["air_quality"]))   # modified formula


def bubble_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def detect_patterns(df):
    threshold = df["risk_score"].mean()

    df["aqi_diff"] = df["air_quality"].diff().fillna(0)

    multi = df[(df["risk_score"] > threshold) & (df["aqi_diff"] > 0)]

    stability = "Stable" if np.var(df["traffic"]) < 200 else "Unstable"

    clusters = []
    temp = []
    for i, row in df.iterrows():
        if row["risk_score"] > threshold:
            temp.append(row["zone"])
        else:
            if len(temp) >= 2:
                clusters.append(temp)
            temp = []

    return multi, stability, clusters


user, role = auth()

data = gen_data()

if ROLL_NUMBER % 3 == 0:
    random.shuffle(data)
else:
    data = bubble_sort(data, "traffic")

for d in data:
    d["category"] = classify(d)
    d["risk_score"] = risk(d)
    d["log_energy"] = math.log(d["energy"]+1)

df = pd.DataFrame(data)

means = np.mean(df[["traffic","air_quality","energy"]], axis=0)

sorted_data = bubble_sort(data.copy(), "risk_score")
top3 = sorted_data[-3:]

risk_tuple = (df["risk_score"].max(),
              df["risk_score"].mean(),
              df["risk_score"].min())

multi, stability, clusters = detect_patterns(df)

avg = risk_tuple[1]
if avg < 100:
    decision = "City Stable"
elif avg < 200:
    decision = "Moderate Risk"
elif avg < 300:
    decision = "High Alert"
else:
    decision = "Critical Emergency"


print("\n===== DATAFRAME =====")
print(df)

print("\nMean Values:", means)

print("\nTop 3 Risk Zones:")
for z in top3:
    print(z)

print("\nRisk Tuple:", risk_tuple)

print("\nMulti-factor Risk Zones:")
print(multi[["zone","risk_score"]])

print("\nStability:", stability)
print("Clusters:", clusters)

print("\nFinal Decision:", decision)

print("\n===== USER INFO =====")
print("User:", user)
print("Role:", role)

if role == "Premium User":
    print("Doraemon says: Use smart gadgets for a better city like my secret door!!!")
else:
    print("Upgrade to Premium for Doraemon insights")

print("\nInsight: A smart city is where sensors work harder than humans to keep traffic smooth, air clean, and energy stable.")
