# Day 8: A world (digital) clock for at least 5 cities on different continents

import datetime
import pytz #Yes, we are using pytz again

#Define the cities and their time zones
cities = {
    'Hyderabad': 'Asia/Kolkata',
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Sydney': 'Australia/Sydney',
    'Cape Town' : 'Africa/Johannesburg'
}

# Get the current time in each city and print it out
for city, time_zone in cities.items():
    tz = pytz.timezone(time_zone)
    time = datetime.datetime.now(tz)
    print(f"{city}: {time.strftime('%d-%m-%Y %H:%M:%S')}") #formatted in DD/MM/YYYY and Hrs, Min and Sec.
