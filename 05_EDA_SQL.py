# EDA with SQL
import pandas as pd
import sqlite3

df = pd.read_csv("spacex_clean.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("SPACEXTBL", conn, index=False, if_exists="replace")

def sql_query(q):
    return pd.read_sql_query(q, conn)

if "LaunchSite" in df.columns:
    display(sql_query("SELECT DISTINCT LaunchSite FROM SPACEXTBL;"))

if {"BoosterVersion","PayloadMass"}.issubset(df.columns):
    display(sql_query("""
    SELECT AVG(PayloadMass) AS AveragePayloadMass
    FROM SPACEXTBL
    WHERE BoosterVersion LIKE '%F9 v1.1%';
    """))

display(sql_query("""
SELECT MissionOutcome, COUNT(*) AS Count
FROM SPACEXTBL
GROUP BY MissionOutcome;
"""))
