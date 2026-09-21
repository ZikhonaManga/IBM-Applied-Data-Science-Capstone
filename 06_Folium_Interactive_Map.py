# Folium Interactive Map
import requests
import pandas as pd
import folium

pads = requests.get(
    "https://api.spacexdata.com/v4/launchpads", timeout=30
).json()

pads = pd.DataFrame([
    {"LaunchSite": p.get("name"),
     "Latitude": p.get("latitude"),
     "Longitude": p.get("longitude")}
    for p in pads
])

m = folium.Map(location=[25, -20], zoom_start=2)

for _, row in pads.dropna(
    subset=["Latitude","Longitude"]
).iterrows():
    folium.Marker(
        [row["Latitude"], row["Longitude"]],
        popup=row["LaunchSite"]
    ).add_to(m)

m.save("spacex_launch_sites_map.html")
m
