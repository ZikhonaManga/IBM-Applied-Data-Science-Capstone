# EDA and Visualization
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spacex_clean.csv")
required = ["FlightNumber","LaunchSite","PayloadMass","Orbit","Class"]
missing = [c for c in required if c not in df.columns]
print("Missing columns:", missing)

# The complete Coursera dataset is required for the following charts
# if those columns are not present.
if not missing:
    plt.figure(figsize=(10,6))
    plt.scatter(df["FlightNumber"], df["LaunchSite"])
    plt.xlabel("Flight Number"); plt.ylabel("Launch Site")
    plt.title("Flight Number vs Launch Site"); plt.show()

    plt.figure(figsize=(10,6))
    plt.scatter(df["PayloadMass"], df["LaunchSite"])
    plt.xlabel("Payload Mass (kg)"); plt.ylabel("Launch Site")
    plt.title("Payload vs Launch Site"); plt.show()

    success = df.groupby("Orbit")["Class"].mean()*100
    success.plot(kind="bar", figsize=(10,5))
    plt.ylabel("Success Rate (%)")
    plt.title("Success Rate vs Orbit Type")
    plt.show()
