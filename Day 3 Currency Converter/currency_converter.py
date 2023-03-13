# Day 3: The currency converter

# install requests module before running this program
# pip install requests

import requests

def currency_converter(amount, from_currency, to_currency):
    # API endpoint
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    
    # make a GET request to the API endpoint
    response = requests.get(url)

    # get the response JSON
    data = response.json()
    
    # get the converted amount from the JSON
    converted_amount = data["rates"][to_currency] * amount
    
    return converted_amount

#user input
amount = float(input("Enter the amount you want to convert: "))
from_currency = input("Enter the currency code you want to convert from (e.g. USD): ")
to_currency = input("Enter the currency code you want to convert to (e.g. EUR): ")


converted_amount = currency_converter(amount, from_currency, to_currency)

# print the result
print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
