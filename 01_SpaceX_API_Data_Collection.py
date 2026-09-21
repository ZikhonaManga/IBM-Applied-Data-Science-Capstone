# SpaceX API Data Collection
import requests
import pandas as pd

url = "https://api.spacexdata.com/v4/launches/past"
response = requests.get(url, timeout=30)
response.raise_for_status()
launches = response.json()

rows = []
for launch in launches:
    cores = launch.get("cores") or [{}]
    core = cores[0]
    rows.append({
        "FlightNumber": launch.get("flight_number"),
        "Date": launch.get("date_utc"),
        "MissionOutcome": "Success" if launch.get("success") else "Failure",
        "LandingSuccess": core.get("landing_success"),
        "Serial": core.get("core")
    })

df = pd.DataFrame(rows)
display(df.head())
df.to_csv("spacex_api_raw.csv", index=False)
