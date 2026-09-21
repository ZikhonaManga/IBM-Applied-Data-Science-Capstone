# Data Wrangling
import pandas as pd

df = pd.read_csv("spacex_api_raw.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Class"] = (df["MissionOutcome"] == "Success").astype(int)
df = df.drop_duplicates()

print(df.info())
print(df.isna().sum())

df.to_csv("spacex_clean.csv", index=False)
