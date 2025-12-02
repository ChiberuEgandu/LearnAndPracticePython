import requests
import json

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=DKLYLX12C0FGX2K2'

r = requests.get(url)

data = r.json()

print(json.dumps(data, indent=4))