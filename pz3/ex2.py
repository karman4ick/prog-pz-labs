import requests
from datetime import datetime, timedelta
BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
today = datetime.now()
for i in range(1, 8):
    date = today - timedelta(days=i)
    date_str = date.strftime("%Y%m%d")
    url = f"{BASE_URL}?date={date_str}&json"
    response = requests.get(url)
    print(f"\nExchange rates as of {date_str}:")
    if response.status_code != 200:
        print("Request error")
        continue
    data = response.json()
    usd_found = False
    pln_found = False
    eur_found = False
    for currency in data:
        if currency["cc"] == "USD":
            print(f"USD: {currency['rate']}")
            usd_found = True
        elif currency["cc"] == "PLN":
            print(f"PLN: {currency['rate']}")
            pln_found = True
        elif currency["cc"] == "EUR":
            print(f"EUR: {currency['rate']}")
            eur_found = True
    if not usd_found:
        print("USD: not found")
    if not pln_found:
        print("PLN: not found")
    if not eur_found:
        print("EUR: not found")