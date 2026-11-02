

import pandas as pd
import requests

ALPHA_VANTAGE_KEY = "LQWI6KX13FV3C4LQ"
SYMBOL = "GOOL"

# Endpoint for Daily Price History
url = f"https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": SYMBOL,
    "outputsize": "compact",  # "compact" returns 100 data points; "full" returns up to 20+ years
    "apikey": ALPHA_VANTAGE_KEY,
}

response = requests.get(url, params=params)
data = response.json()
print(data)
# Parse the JSON response into a clean Pandas DataFrame
if "Time Series (Daily)" in data:
    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    # Clean up column names (remove numbers)
    df.columns = [col.split(". ")[1] for col in df.columns]
    df.index = pd.to_datetime(df.index)
    print(df.head())
    print(df.info())
else:
    print("Error fetching data:", data)
