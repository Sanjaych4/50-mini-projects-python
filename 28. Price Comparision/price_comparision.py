# Day 28: Price comparison (flight)
# Note: replace the API key in the header section with your api key to work.

import requests

# Skyscanner API endpoint for flight prices
url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0"

# API parameters for flight search
params = {
    "originPlace": "LHR-sky",  # London Heathrow Airport
    "destinationPlace": "JFK-sky",  # New York JFK Airport
    "outboundDate": "2022-04-01",
    "inboundDate": "2022-04-10",
    "adults": 1,
    "currency": "USD",
    "locale": "en-US"
}

# Headers with API key
headers = {
    "X-RapidAPI-Key": "<YOUR_API_KEY>"
}

# Make API request to Skyscanner and get response
response = requests.get(url, headers=headers, params=params)

# Check if request was successful
if response.status_code == 200:
    # Parse response JSON and get prices
    data = response.json()
    quotes = data["Quotes"]
    prices = [quote["MinPrice"] for quote in quotes]
    # Print prices
    print("Flight prices from London Heathrow to New York JFK:")
    for i, price in enumerate(prices):
        print(f"{i+1}. ${price}")
else:
    print("Failed to retrieve flight prices.")
