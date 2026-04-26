import random
import math
import numpy as np
import pandas as pd
import copy

def auth_dora():
    password = input("Enter Doraemon secret gadget code: ")
    if password != "AnywhereDoor":
        print("Authentication Failed")
        exit()
    print("Access Granted")

def generate():
    return [{
        "zone": i,
        "metrics": {
            "traffic": random.randint(50,150),
            "pollution": random.randint(30,120),
            "energy": random.randint(40,140)
        },
        "history": [random.randint(10,80) for _ in range(5)]
    } for i in range(1,16)]

def transform(data, roll):
    return data[::-1] if roll % 2 == 0 else data[3:] + data[:3]

def risk_fn(t,p,e):
    return math.log(t+p+e)

def mutate(data):
    for d in data:
        d["metrics"]["traffic"] += 7
        d["history"].append(random.randint(10,90))
        d["risk"] = risk_fn(
            d["metrics"]["traffic"],
            d["metrics"]["pollution"],
            d["metrics"]["energy"]
        )

def make_df(data):
    return pd.DataFrame([{
        "zone": d["zone"],
        "traffic": d["metrics"]["traffic"],
        "pollution": d["metrics"]["pollution"],
        "energy": d["metrics"]["energy"],
        "risk": d.get("risk",0)
    } for d in data])

def corr(x,y):
    xm, ym = np.mean(x), np.mean(y)
    return np.sum((x-xm)*(y-ym)) / math.sqrt(np.sum((x-xm)**2)*np.sum((y-ym)**2))

auth_dora()

roll = 62

original = transform(generate(), roll)
assign = original
shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("Before:", original[0])

mutate(shallow)

print("After (shallow affects original):", original[0])

mutate(deep)

df = make_df(original)

mean = df.mean()
std = df.std()

anomaly = df[df["traffic"] > mean["traffic"] + std["traffic"]]

stability = 1 / df["risk"].var()

max_risk = df["risk"].max()
min_risk = df["risk"].min()

decision = "System Stable" if stability > 0.5 else "High Corruption Risk"

print(df)
print("Anomalies:", list(anomaly["zone"]))
print("Correlation:", corr(df["traffic"], df["pollution"]))
print("Tuple:", (max_risk, min_risk, stability))
print("Decision:", decision)
