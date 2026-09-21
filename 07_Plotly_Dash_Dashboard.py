# Plotly Dash Dashboard
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("spacex_clean.csv")
app = Dash(__name__)

sites = sorted(df["LaunchSite"].dropna().unique()) if "LaunchSite" in df else []

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard"),
    dcc.Dropdown(
        id="site",
        options=[{"label": s, "value": s} for s in sites],
        value=sites[0] if sites else None
    ),
    dcc.Graph(id="outcomes"),
    dcc.Graph(id="payload")
])

@app.callback(
    Output("outcomes","figure"),
    Output("payload","figure"),
    Input("site","value")
)
def update(site):
    d = df[df["LaunchSite"] == site]
    counts = d["Class"].map({1:"Success",0:"Failure"}).value_counts()
    fig1 = px.pie(values=counts.values, names=counts.index,
                  title=f"Launch Outcomes — {site}")
    fig2 = px.scatter(d, x="FlightNumber", y="PayloadMass",
                      color="Class",
                      title=f"Payload vs Flight Number — {site}")
    return fig1, fig2

if __name__ == "__main__":
    app.run(debug=True)
