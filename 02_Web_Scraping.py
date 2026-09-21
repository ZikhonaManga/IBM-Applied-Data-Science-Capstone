# Web Scraping
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"
html = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=30).text
tables = pd.read_html(html)

for i, table in enumerate(tables[:15]):
    print(i, table.shape, list(table.columns)[:8])

# Inspect candidate tables and select the one appropriate to your lab.
