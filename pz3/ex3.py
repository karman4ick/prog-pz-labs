import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
BASE_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
dates = []
usd_rates = []
pln_rates = []
eur_rates = []
today = datetime.now()
for i in range(1,8):
    date = today - timedelta(days=i)
    date_str = date.strftime("%Y%m%d")
    url = f"{BASE_URL}?date={date_str}&json"
    response = requests.get(url)
    if response.status_code != 200:
        continue
    data = response.json()
    usd_rate =  None
    pln_rate = None
    eur_rate = None
    for currency in data:
        if currency["cc"] == "USD":
            usd_rate = currency["rate"]
        elif currency["cc"] == "PLN":
            pln_rate = currency["rate"]
        elif currency["cc"] == "EUR":
            eur_rate = currency["rate"]
    if usd_rate and pln_rate and eur_rate:
        dates.append(date.strftime("%d.%m"))
        usd_rates.append(usd_rate)
        pln_rates.append(pln_rate)
        eur_rates.append(eur_rate)
plt.figure(figsize=(10,5))
plt.plot(dates, usd_rates, marker='o', label="USD")
plt.plot(dates, pln_rates, marker='o', label="PLN")
plt.plot(dates, eur_rates, marker='o', label="EUR")
plt.title("Currency exchange rate changes for the previous week")
plt.xlabel("Date")
plt.ylabel("UAH")
plt.legend()
plt.grid(True)
plt.savefig("exchange_rates_last_week.png")
plt.show()