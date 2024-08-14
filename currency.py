import requests
import time

def converter(amount, from_currency, to_currency):

    api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    response = requests.get(api_endpoint)

    data = response.json()

    exchange_rate = data["rates"][to_currency]

    converted_amount = amount * exchange_rate

    return converted_amount


amount = float(input("Enter amount: "))
from_curr = input("Enter source currency code: ").upper()
to_curr = input("Enter target currency code: ").upper()

res = converter(amount, from_curr, to_curr)
print(f"{amount} {from_curr} is equal to {round(res,2)} { to_curr}")
time.sleep(5)